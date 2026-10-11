# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
# agent-doctor 配置诊断面:四端 agent 客户端配置静检(claude、codex、grok、kimi)。
# 判据分档沿研究档 cfg-01(2026-10-12):error = 客户端不可能成功或写错载体的硬伤;
# advisory = 客户端容忍但值得治理的残留与演进面(文档容忍态不升 error)。
# 只报不改,修复手册见同 skill references/config-face.md;
# 豁免走 PEVO_CONFIG_LINT_ALLOW(分号隔,收字段名与枚举值)。
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tomllib
from pathlib import Path

SECRET_KEY = re.compile(r"(TOKEN|API_KEY|SECRET|PASSWORD)$")
PLACEHOLDER = re.compile(r"^\$\{[^}]*\}$")
# 高置信秘密形态:PEM 私钥块、AWS 访问键、sk- 长令牌(只对高置信升 error,URL 与模型名不误伤)
SECRET_VALUE = [
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"\bsk-[A-Za-z0-9_-]{20,}"),
]

# 白名单是先验判据(cfg-01 对照官方索引),随客户端版本演进走 advisory 与豁免变量,不做闭合白名单。
CLAUDE_FIELDS = {
    "env", "permissions", "enableAllProjectMcpServers", "enabledPlugins",
    "extraKnownMarketplaces", "hooks", "statusLine", "model", "outputStyle",
    "viewMode", "alwaysThinkingEnabled", "effortLevel", "tui", "autoMemoryEnabled",
    "showThinkingSummaries", "skipDangerousModePermissionPrompt",
    "hasCompletedOnboarding", "includeCoAuthoredBy", "apiKeyHelper",
    "forceLoginMethod", "cleanupPeriodDays", "spinnerTipsEnabled",
    "todoFeatureEnabled", "respectGitIgnore", "preferredNotifChannel",
}
# claude doctor 2.1.296 实测拒绝的枚举集(cfg-01 件 1 实证)
CLAUDE_MODES = {"default", "acceptEdits", "auto", "plan", "bypassPermissions", "dontAsk"}
CODEX_KEYS = {
    "model", "model_provider", "model_providers", "model_reasoning_effort",
    "model_verbosity", "model_catalog_json", "approval_policy", "sandbox_mode",
    "sandbox_workspace_write", "mcp_servers", "features", "projects",
    "shell_environment_policy", "history", "tls", "chatgpt_base_url", "notify",
    "file_watcher", "show_raw_agent_reasoning", "forced_login_method",
    "preferred_auth_method", "hooks", "marketplaces", "plugins", "tui",
}
CODEX_APPROVAL = {"untrusted", "on-request", "on-failure", "never"}
CODEX_SANDBOX = {"read-only", "workspace-write", "danger-full-access"}
GROK_SECTIONS = {"cli", "marketplace", "plugins", "privacy", "ui", "models"}
KIMI_KEYS = {
    "default_model", "default_permission_mode", "extra_skill_dirs", "telemetry",
    "hooks", "models", "providers", "services", "thinking",
}


def _extra_allow() -> set[str]:
    return {x for x in os.environ.get("PEVO_CONFIG_LINT_ALLOW", "").split(";") if x}


def _on_win() -> bool:
    return sys.platform.startswith("win")


def _cmd_tokens(cmd: str) -> list[str]:
    """命令串拆 token:引号段(可含空格)优先,变量展开段跳过。"""
    toks = []
    for m in re.finditer(r'"([^"]+)"|\'([^\']+)\'|(\S+)', cmd):
        tok = next(g for g in m.groups() if g is not None)
        if "$" in tok or tok.startswith("%"):
            continue
        toks.append(tok)
    return toks


def _is_abs(p: str) -> bool:
    return p.startswith("/") or bool(re.match(r"^[A-Za-z]:[\\/]", p)) or p.startswith("\\\\")


def _is_current_os_abs(tok: str) -> bool:
    """kimi 配置按设计共存双 OS 形:只查当前 OS 形的绝对路径。"""
    if tok.startswith("/"):
        return not _on_win()
    if re.match(r"^[A-Za-z]:[\\/]", tok) or tok.startswith("\\\\"):
        return _on_win()
    return False


def check_cmd_paths(face: str, where: str, cmd: str, out: list, current_os_only: bool = False) -> None:
    for tok in _cmd_tokens(cmd):
        if not _is_abs(tok):
            continue
        if current_os_only and not _is_current_os_abs(tok):
            continue
        if not os.path.exists(tok):
            out.append(("error", face, where, f"命令绝对路径不存在: {tok}"))


def _scan_secret_values(face: str, where: str, obj, out: list) -> None:
    """递归扫高置信秘密形态(PEM、AWS 键、sk- 令牌):写错载体即 error。"""
    if isinstance(obj, dict):
        for v in obj.values():
            _scan_secret_values(face, where, v, out)
    elif isinstance(obj, list):
        for v in obj:
            _scan_secret_values(face, where, v, out)
    elif isinstance(obj, str):
        for pat in SECRET_VALUE:
            if pat.search(obj):
                out.append(("error", face, where, f"配置文件内高置信秘密形态: {pat.pattern}"))
                return


def check_claude(path: Path, home: Path, out: list) -> None:
    face = "claude"
    is_user_file = path.is_relative_to(home / ".claude")
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        out.append(("error", face, str(path), f"JSON 解析失败: {e}"))
        return
    if not isinstance(data, dict):
        out.append(("error", face, str(path), "顶层必须是对象"))
        return
    allow = _extra_allow()
    for k in data:
        if k not in CLAUDE_FIELDS and k not in allow:
            out.append(("advisory", face, str(path), f"未知顶层字段: {k}"))
    # 悬空引用是文档容忍态(项目文件指向未装插件为稳态),报 advisory(cfg-01 件 1)
    for key, on in data.get("enabledPlugins", {}).items():
        if not isinstance(key, str) or "@" not in key or not on:
            continue
        name, _, mkt = key.partition("@")
        cand = home / ".claude" / "skills" / name if mkt == "skills-dir" \
            else home / ".claude" / "plugins" / "cache" / mkt / name
        if not cand.is_dir():
            out.append(("advisory", face, str(path), f"enabledPlugins 悬空引用: {key} 不在 {cand}"))
    # 用户面明文凭证是文档允许形态(网关页),提示迁移;会进库的项目面才 error
    env = data.get("env", {})
    for k, v in env.items():
        if isinstance(v, str) and v and SECRET_KEY.search(k) and not PLACEHOLDER.match(v):
            level = "advisory" if is_user_file else "error"
            hint = "宜走 apiKeyHelper 或环境注入" if is_user_file else "项目文件会进库,凭证必须移出"
            out.append((level, face, str(path), f"env 明文凭据: {k} 值落在配置文件,{hint}"))
    # 网关键组配对(overcast 诊断配置对齐层):钉组形 BASE_URL 配了则鉴权与模型映射宜齐
    if isinstance(env.get("ANTHROPIC_BASE_URL"), str) and env["ANTHROPIC_BASE_URL"]:
        if not any(isinstance(env.get(k), str) and env[k] for k in ("ANTHROPIC_AUTH_TOKEN", "ANTHROPIC_API_KEY")):
            out.append(("advisory", face, str(path), "网关键组不齐: ANTHROPIC_BASE_URL 配了但鉴权键缺"))
        if not any(k.startswith("ANTHROPIC_DEFAULT_") and k.endswith("_MODEL") for k in env):
            out.append(("advisory", face, str(path), "网关键组不齐: 无 ANTHROPIC_DEFAULT_*_MODEL 模型映射"))
    mode = data.get("permissions", {}).get("defaultMode")
    if mode is not None and mode not in CLAUDE_MODES and mode not in allow:
        out.append(("error", face, str(path), f"permissions.defaultMode 非法值: {mode}"))
    cmds = [data.get("statusLine", {}).get("command", "")]
    for entries in data.get("hooks", {}).values():
        if not isinstance(entries, list):
            continue
        for ent in entries:
            for h in ent.get("hooks", []) if isinstance(ent, dict) else []:
                if isinstance(h, dict):
                    cmds.append(h.get("command", ""))
    for cmd in cmds:
        if isinstance(cmd, str) and cmd:
            check_cmd_paths(face, str(path), cmd, out)


def _load_toml(path: Path, face: str, out: list) -> dict | None:
    try:
        with path.open("rb") as f:
            return tomllib.load(f)
    except (OSError, tomllib.TOMLDecodeError) as e:
        out.append(("error", face, str(path), f"TOML 解析失败: {e}"))
        return None


def check_codex(path: Path, home: Path, out: list) -> None:
    face = "codex"
    data = _load_toml(path, face, out)
    if data is None:
        return
    allow = _extra_allow()
    for k in data:
        if k not in CODEX_KEYS and k not in allow:
            out.append(("advisory", face, str(path), f"未知顶层键: {k}"))
    _scan_secret_values(face, str(path), data, out)
    for name, tbl in data.get("mcp_servers", {}).items():
        if not isinstance(tbl, dict) or not isinstance(tbl.get("command"), str):
            out.append(("error", face, str(path), f"mcp_servers.{name} 形态非法: command 须为字符串"))
        elif "args" in tbl and not (isinstance(tbl["args"], list) and all(isinstance(a, str) for a in tbl["args"])):
            out.append(("error", face, str(path), f"mcp_servers.{name} 形态非法: args 须为字符串列表"))
    pol = data.get("approval_policy")
    if pol is not None and pol not in CODEX_APPROVAL and pol not in allow:
        out.append(("error", face, str(path), f"approval_policy 非法值: {pol}"))
    sb = data.get("sandbox_mode")
    if sb is not None and sb not in CODEX_SANDBOX and sb not in allow:
        out.append(("error", face, str(path), f"sandbox_mode 非法值: {sb}"))
    # 配置残留候选:plugins 键指向的插件在 cache 无目录(卸载不清配置,判例 2026-10-12 wsl)
    plugins = data.get("plugins", {})
    if isinstance(plugins, dict):
        for key in plugins:
            if not isinstance(key, str) or "@" not in key:
                continue
            name, _, mkt = key.partition("@")
            if not (home / ".codex" / "plugins" / "cache" / mkt / name).is_dir():
                out.append(("advisory", face, str(path), f"plugins 配置残留候选: {key} 不在 cache,宜清"))


def check_grok(path: Path, home: Path, out: list) -> None:
    face = "grok"
    data = _load_toml(path, face, out)
    if data is None:
        return
    allow = _extra_allow()
    for k in data:
        if k not in GROK_SECTIONS and k not in allow:
            out.append(("advisory", face, str(path), f"未知节: {k}"))
    _scan_secret_values(face, str(path), data, out)
    cache = home / ".grok" / "marketplace-cache"
    installed: set[str] = set()
    if cache.is_dir():
        for d in cache.iterdir():
            plugins = d / "plugins"
            if plugins.is_dir():
                installed |= {p.name for p in plugins.iterdir() if p.is_dir()}
    for name in data.get("plugins", {}).get("enabled", []):
        if name not in installed:
            out.append(("error", face, str(path), f"plugins.enabled 悬空引用: {name} 不在 {cache}"))
    cmd = data.get("ui", {}).get("status_line", {}).get("command", "")
    if isinstance(cmd, str) and cmd:
        check_cmd_paths(face, str(path), cmd, out)


def check_kimi_config(path: Path, out: list) -> None:
    face = "kimi"
    data = _load_toml(path, face, out)
    if data is None:
        return
    allow = _extra_allow()
    for k in data:
        if k not in KIMI_KEYS and k not in allow:
            out.append(("advisory", face, str(path), f"未知顶层键: {k}"))
    _scan_secret_values(face, str(path), data, out)
    for name, tbl in data.get("providers", {}).items():
        if isinstance(tbl, dict) and isinstance(tbl.get("api_key"), str) and tbl["api_key"]:
            out.append(("error", face, str(path), f"providers.{name}.api_key 明文非空: 凭证应走 oauth/环境"))
    hooks = data.get("hooks", [])
    if isinstance(hooks, list):
        for h in hooks:
            if isinstance(h, dict) and isinstance(h.get("command"), str):
                # kimi 配置按设计共存双 OS 形,只查当前 OS 形路径(hst init 双形部署)
                check_cmd_paths(face, str(path), h["command"], out, current_os_only=True)


def _skill_name(skill_md: Path) -> str | None:
    text = skill_md.read_text(encoding="utf-8", errors="replace").splitlines()
    if not text or text[0].strip() != "---":
        return None
    for line in text[1:60]:
        if line.strip() == "---":
            break
        m = re.match(r"^name:\s*(\S+)", line)
        if m:
            return m.group(1)
    return None


def check_kimi_skills(skills: Path, out: list, source: Path | None = None) -> None:
    face = "kimi"
    for d in sorted(skills.iterdir()):
        if not d.is_dir():
            continue
        sk = d / "SKILL.md"
        if not sk.is_file():
            out.append(("error", face, str(d), "缺 SKILL.md"))
            continue
        name = _skill_name(sk)
        if name != d.name:
            out.append(("error", face, str(sk), f"frontmatter name({name}) 与目录名({d.name})不一致"))
    if source is not None:
        expected = {p.name for p in source.glob("*/skills/*") if p.is_dir()}
        actual = {d.name for d in skills.iterdir() if d.is_dir()}
        for extra in sorted(actual - expected):
            out.append(("error", face, str(skills), f"漂移余账: {extra} 不在源 {source}"))
        for miss in sorted(expected - actual):
            out.append(("error", face, str(skills), f"缺失: {miss} 未从源 {source} 安装"))


def run(home: Path, claude: Path, codex: Path, grok: Path, kimi_config: Path, kimi: Path,
        kimi_source: Path | None) -> tuple[list, list[str]]:
    out: list = []
    notes: list[str] = []
    for p in (claude, claude.with_name("settings.local.json")):
        if p.is_file():
            check_claude(p, home, out)
    if not claude.is_file():
        notes.append(f"claude 面跳过: 无 {claude}")
    if codex.is_file():
        check_codex(codex, home, out)
    else:
        notes.append(f"codex 面跳过: 无 {codex}")
    if grok.is_file():
        check_grok(grok, home, out)
    else:
        notes.append(f"grok 面跳过: 无 {grok}")
    if kimi_config.is_file():
        check_kimi_config(kimi_config, out)
    else:
        notes.append(f"kimi 配置面跳过: 无 {kimi_config}")
    if kimi.is_dir():
        check_kimi_skills(kimi, out, kimi_source)
    else:
        notes.append(f"kimi skills 面跳过: 无 {kimi}")
    return out, notes


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="四端 agent 配置诊断(claude/codex/grok/kimi),只报不改")
    ap.add_argument("--home", type=Path, default=Path.home())
    ap.add_argument("--claude", type=Path, default=None, help="claude settings.json 路径(非用户面则凭证判据升 error)")
    ap.add_argument("--codex", type=Path, default=None, help="codex config.toml 路径")
    ap.add_argument("--grok", type=Path, default=None, help="grok config.toml 路径")
    ap.add_argument("--kimi-config", type=Path, default=None, help="kimi config.toml 路径")
    ap.add_argument("--kimi", type=Path, default=None, help="kimi skills 目录")
    ap.add_argument("--kimi-source", type=Path, default=None, help="源 plugins 目录,给则做 kimi 漂移对账")
    ap.add_argument("--json", action="store_true", help="机读输出")
    args = ap.parse_args(argv)
    h = args.home
    findings, notes = run(
        h,
        args.claude or h / ".claude" / "settings.json",
        args.codex or h / ".codex" / "config.toml",
        args.grok or h / ".grok" / "config.toml",
        args.kimi_config or h / ".kimi-code" / "config.toml",
        args.kimi or h / ".kimi" / "skills",
        args.kimi_source,
    )
    errors = [f for f in findings if f[0] == "error"]
    advisories = [f for f in findings if f[0] == "advisory"]
    if args.json:
        print(json.dumps({
            "errors": [{"face": f, "file": w, "msg": m} for _, f, w, m in errors],
            "advisories": [{"face": f, "file": w, "msg": m} for _, f, w, m in advisories],
            "notes": notes,
        }, ensure_ascii=False, indent=2))
    else:
        for level, face, where, msg in findings:
            print(f"[{level}][{face}][{where}] {msg}")
        for n in notes:
            print(f"[note] {n}")
        print(f"共 {len(errors)} 错 {len(advisories)} 警")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
