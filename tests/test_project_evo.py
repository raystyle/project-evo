"""project-evo 脚本与插件面测试。

脚本为 PEP 723 零依赖形态,从 plugins/ 树按文件路径加载(无安装态包,单源无副本)。
覆盖:init 幂等、check 抓违(PE-01/PE-11/围栏感知)、scan 历史泄漏与 md 告警、
退出码、市场清单与双 manifest 一致性守卫(改一面须同步另一面)。
"""

from __future__ import annotations

import importlib.util
import json
import os
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
PLUGIN = REPO / "plugins" / "project-evo"
SCRIPTS = PLUGIN / "skills" / "dev-evo" / "scripts"


def _load(name: str):
    spec = importlib.util.spec_from_file_location(f"pevo_{name}", SCRIPTS / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


init_mod = _load("init")
check_mod = _load("check")
scan_mod = _load("scan")


def test_scaffold_creates_and_idempotent(tmp_path: Path):
    created, skipped = init_mod.generate(tmp_path, "demo")
    assert len(created) >= 10, "骨架文件不少于 10 件"
    assert (tmp_path / "AGENTS.md").exists()
    assert "demo" in (tmp_path / "AGENTS.md").read_text(encoding="utf-8"), "AGENTS 标题渲染项目名"
    assert (tmp_path / "docs" / "adr" / "0000-template.md").exists()
    assert (tmp_path / "docs" / "requirements" / "0000-template.md").exists()
    assert "{name}" not in (tmp_path / "AGENTS.md").read_text(encoding="utf-8"), "占位符已渲染"
    # 幂等:二次生成全跳过,内容不变
    before = (tmp_path / "AGENTS.md").read_text(encoding="utf-8")
    created2, skipped2 = init_mod.generate(tmp_path, "demo")
    assert not created2 and len(skipped2) == len(created)
    assert (tmp_path / "AGENTS.md").read_text(encoding="utf-8") == before, "已有文件不被覆盖"


def test_check_passes_on_scaffold(tmp_path: Path):
    init_mod.generate(tmp_path, "demo")
    results, ok = check_mod.check(tmp_path)
    assert ok, [r for r in results if r[1] == "FAIL"]


def test_check_catches_violations(tmp_path: Path):
    init_mod.generate(tmp_path, "demo")
    (tmp_path / "AGENTS.md").unlink()  # PE-01 是 AGENTS 五节合同
    results, ok = check_mod.check(tmp_path)
    assert not ok
    assert "PE-01" in {r[0] for r in results if r[1] == "FAIL"}, "缺 AGENTS 应被 PE-01 抓住"


def test_check_adr_state_machine(tmp_path: Path):
    """PE-06:status 非法与 superseded_by 悬空都要 FAIL,合法状态过。"""
    init_mod.generate(tmp_path, "demo")
    adr = tmp_path / "docs" / "adr"
    (adr / "ADR-0001-选库.md").write_text(
        "---\nid: ADR-0001\nstatus: accepted\ndate: 2026-09-15\n---\n# ADR-0001\n", encoding="utf-8")
    (adr / "ADR-0002-换库.md").write_text(
        "---\nid: ADR-0002\nstatus: bogus\n---\n# ADR-0002\n", encoding="utf-8")
    (adr / "ADR-0003-又换.md").write_text(
        "---\nid: ADR-0003\nstatus: superseded\nsuperseded_by: ADR-0099\n---\n# ADR-0003\n",
        encoding="utf-8")
    results, _ = check_mod.check(tmp_path)
    fails = {r[0]: r[2] for r in results if r[1] == "FAIL"}
    assert "PE-06" in fails and "bogus" in fails["PE-06"], "非法 status 应被 PE-06 抓住"
    assert "悬空" in fails["PE-06"], "superseded_by 悬空应被 PE-06 抓住"
    # 修成合法状态与可达 supersede 链后 PE-06 通过
    (adr / "ADR-0002-换库.md").write_text(
        "---\nid: ADR-0002\nstatus: proposed\n---\n# ADR-0002\n", encoding="utf-8")
    (adr / "ADR-0003-又换.md").write_text(
        "---\nid: ADR-0003\nstatus: superseded\nsuperseded_by: ADR-0001\n---\n# ADR-0003\n",
        encoding="utf-8")
    results, _ = check_mod.check(tmp_path)
    assert "PE-06" not in {r[0] for r in results if r[1] == "FAIL"}


def test_check_req_trace_and_index(tmp_path: Path):
    """PE-07:implemented 缺 trace FAIL;PE-08:未登记索引 FAIL。"""
    init_mod.generate(tmp_path, "demo")
    req = tmp_path / "docs" / "requirements"
    (req / "REQ-001-骨架.md").write_text(
        "---\nid: REQ-001\nstatus: implemented\npriority: must\ntrace: null\n---\n# REQ-001\n",
        encoding="utf-8")
    results, _ = check_mod.check(tmp_path)
    fails = {r[0]: r[2] for r in results if r[1] == "FAIL"}
    assert "PE-07" in fails and "trace" in fails["PE-07"], "implemented 缺 trace 应被 PE-07 抓住"
    assert "PE-08" in fails and "REQ-001" in fails["PE-08"], "未登记索引应被 PE-08 抓住"


def test_check_title_bracket(tmp_path: Path):
    init_mod.generate(tmp_path, "demo")
    (tmp_path / "docs" / "guides" / "cook-面条.md").write_text(
        "# 指南:命名(详版)\n\n## 一、命名\n", encoding="utf-8"
    )
    _, ok = check_mod.check(tmp_path)
    assert not ok, "标题带括号应被 PE-10 抓住"


def test_check_ignores_fenced_code_comments(tmp_path: Path):
    """代码块内的 # 注释带括号不算标题违规(PE-10 围栏感知)。"""
    init_mod.generate(tmp_path, "demo")
    (tmp_path / "docs" / "guides" / "cook-面条.md").write_text(
        "# 指南\n\n## 命名\n\n```powershell\n"
        "# 1. 看 skill 本体(意图路由入口)\nGet-Content SKILL.md\n```\n",
        encoding="utf-8",
    )
    _, ok = check_mod.check(tmp_path)
    assert ok, "围栏内 # 注释不应触发 PE-10"


def test_check_pe11_allowlist_exempts_history(tmp_path: Path, monkeypatch):
    """PEVO_CHECK_ALLOW 命中的历史档案禁字报 SKIP 不 FAIL,豁免不掩护活跃面。"""
    init_mod.generate(tmp_path, "demo")
    (tmp_path / "docs" / "diary" / "2026-01-01-旧档.md").write_text(
        "# 旧档\n\n改造走向全量镜像 —— 第一批落定\n", encoding="utf-8"
    )
    monkeypatch.delenv("PEVO_CHECK_ALLOW", raising=False)
    _, ok = check_mod.check(tmp_path)
    assert not ok, "未设豁免时存量禁字应 FAIL"
    monkeypatch.setenv("PEVO_CHECK_ALLOW", r"docs/diary/2026-01-01-旧档\.md:3")
    results, ok = check_mod.check(tmp_path)
    assert ok, "豁免命中后应通过(退出码 0)"
    pe11 = next(r for r in results if r[0] == "PE-11")
    assert pe11[1] == "SKIP", "豁免面应显式报 SKIP 留审计痕迹"
    (tmp_path / "README.md").write_text("# demo\n\n走向 —— 全量\n", encoding="utf-8")
    monkeypatch.setenv("PEVO_CHECK_ALLOW", ".*")
    _, ok = check_mod.check(tmp_path)
    assert not ok, "根三件是活跃面,全域正则也不得掩护"


def _git(cwd: Path, *args: str) -> None:
    subprocess.run(["git", "-C", str(cwd), *args], check=True, capture_output=True,
                   env={**__import__("os").environ, "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t",
                        "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@t"})


def test_scan_finds_secret_in_history(tmp_path: Path):
    _git(tmp_path, "init", "-b", "main")
    (tmp_path / "cfg.txt").write_text("token = ghp_0123456789abcdefghijklmnop\n", encoding="utf-8")
    _git(tmp_path, "add", "-A"); _git(tmp_path, "commit", "-m", "leak")
    (tmp_path / "cfg.txt").unlink()
    _git(tmp_path, "add", "-A"); _git(tmp_path, "commit", "-m", "remove")
    finds = scan_mod.scan_history_secrets(tmp_path)
    assert any(f["rule"] == "GitHub token" for f in finds), "历史中的 token 应被抓到"
    _, clean = scan_mod.run_scan(tmp_path)
    assert not clean
    # 报告脱敏:不回显完整 token
    joined = " ".join(f["snippet"] for f in finds)
    assert "ghp_0123456789abcdefghijklmnop" not in joined


def test_scan_md_reports_file_and_line(tmp_path: Path):
    (tmp_path / "A.md").write_text(
        "# 标题\n\n规则:登记到立项——执行“完”\n\n```text\n# 注释(豁免)—— →\n```\n",
        encoding="utf-8",
    )
    finds, clean = scan_mod.run_scan(tmp_path, history=False)
    assert not clean
    md = [f for f in finds if f["kind"] == "md"]
    assert md and md[0]["file"] == "A.md" and md[0]["line"] == 3, "标注文件与行号"
    assert any("破折号" in f["rule"] for f in md) and any("智能引号" in f["rule"] for f in md)
    assert all(f["line"] != 6 for f in md), "围栏内豁免"


def test_init_creates_missing_target(tmp_path: Path):
    """脚手架语义:目标目录不存在则创建(同日两犯升格:本地 e2e 与 CI 冒烟各踩一次)。"""
    target = tmp_path / "nested" / "demo"
    r = subprocess.run([sys.executable, str(SCRIPTS / "init.py"), str(target), "--name", "demo"],
                       capture_output=True, text=True, encoding="utf-8")
    assert r.returncode == 0, r.stderr
    assert (target / "AGENTS.md").is_file()


def test_check_script_exit_codes(tmp_path: Path):
    """子进程直跑:PEP 723 零依赖,系统 python 即可;退出码 0/1。"""
    init_mod.generate(tmp_path, "demo")
    r_ok = subprocess.run([sys.executable, str(SCRIPTS / "check.py"), str(tmp_path)],
                          capture_output=True, text=True, encoding="utf-8")
    assert r_ok.returncode == 0, r_ok.stdout + r_ok.stderr
    (tmp_path / "AGENTS.md").unlink()
    r_bad = subprocess.run([sys.executable, str(SCRIPTS / "check.py"), str(tmp_path)],
                           capture_output=True, text=True, encoding="utf-8")
    assert r_bad.returncode == 1


def test_marketplace_catalog_consistency():
    """清单守卫:市场只收一个插件、双清单一致、双 manifest 与市场版本同步、四 skill 与命令面在位。"""
    claude_mkt = json.loads((REPO / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
    codex_mkt = json.loads((REPO / ".agents" / "plugins" / "marketplace.json").read_text(encoding="utf-8"))
    claude_man = json.loads((PLUGIN / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    codex_man = json.loads((PLUGIN / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))

    names_c = {p["name"] for p in claude_mkt["plugins"]}
    names_x = {p["name"] for p in codex_mkt["plugins"]}
    assert names_c == names_x == {"project-evo"}, "市场只收一个插件 project-evo(三 skill 同装同版)"
    for p in claude_mkt["plugins"]:
        assert (REPO / p["source"].removeprefix("./")).is_dir(), f"Claude source 不可达: {p['source']}"
    for p in codex_mkt["plugins"]:
        assert (REPO / p["source"]["path"].removeprefix("./")).is_dir(), "Codex source 不可达"

    for k in ("name", "version", "description"):
        assert claude_man[k] == codex_man[k], f"{k} 双 manifest 漂移,须同步改两面"
    entry = next(p for p in claude_mkt["plugins"] if p["name"] == "project-evo")
    assert entry["version"] == claude_man["version"], "市场清单版本与 manifest 漂移"

    skills = PLUGIN / "skills"
    dirs = sorted(d.name for d in skills.iterdir() if d.is_dir())
    assert dirs == ["dev-evo", "secret-scan", "security-audit", "super-research"], f"四 skill 须齐备: {dirs}"
    for name in dirs:
        text = (skills / name / "SKILL.md").read_text(encoding="utf-8")
        assert text.startswith("---\n"), f"{name}/SKILL.md 缺 frontmatter"
        head = text.split("---")[1]
        declared = next(l.split(":", 1)[1].strip() for l in head.splitlines() if l.startswith("name:"))
        assert declared == name, f"frontmatter name({declared}) 须与目录名({name})一致"

    docs = skills / "dev-evo"
    assert (docs / "references").is_dir() and (docs / "assets" / "templates").is_dir()
    for s in ("init.py", "check.py", "scan.py", "mdrules.py", "md-guard.py"):
        assert (docs / "scripts" / s).is_file(), f"脚本缺失: {s}"
    for name in dirs:
        assert (skills / name / "references").is_dir(), f"参考目录缺失: {name}"
    assert (skills / "secret-scan" / "scripts" / "scan.py").is_file()
    assert (skills / "secret-scan" / "scripts" / "ab.py").is_file()
    assert (skills / "security-audit" / "scripts" / "validate-findings.cjs").is_file()
    assert (skills / "security-audit" / "scripts" / "report-schema.json").is_file()
    for c in ("init.md", "check.md", "scan.md", "secret-scan-cli.md"):
        assert (PLUGIN / "commands" / c).is_file(), f"斜杠命令缺失: {c}"
    json.loads((PLUGIN / "hooks" / "hooks.json").read_text(encoding="utf-8")), "hooks.json 须为合法 JSON"


def _run_md_guard(payload: str) -> subprocess.CompletedProcess:
    env = {**os.environ, "PYTHONIOENCODING": "utf-8"}
    return subprocess.run(
        [sys.executable, str(SCRIPTS / "md-guard.py")],
        input=payload, capture_output=True, text=True, encoding="utf-8",
        errors="replace", env=env,
    )


def test_md_guard_hook_tolerates_alien_payload(tmp_path: Path):
    """Codex apply_patch 面载荷宽容:tool_input 是对象但无 file_path,或整体不是对象,均放行 0。"""
    codex_shape = json.dumps({
        "hook_event_name": "PostToolUse",
        "tool_name": "apply_patch",
        "tool_input": {"command": "*** Begin Patch\n*** Update File: note.md\n+x\n*** End Patch\n"},
        "tool_response": "Success. Updated files.",
    })
    assert _run_md_guard(codex_shape).returncode == 0
    alien_shape = json.dumps({"hook_event_name": "PostToolUse", "tool_input": "*** Begin Patch"})
    assert _run_md_guard(alien_shape).returncode == 0
    assert _run_md_guard("not json at all").returncode == 0


def test_md_guard_hook_flags_forbidden_chars(tmp_path: Path):
    """Claude 面判据不回退:file_path 指向含禁字的 .md 时退出 2 并写 stderr。"""
    bad = tmp_path / "bad.md"
    bad.write_text("正常一行\n带破折号 \u2014 的一行\n", encoding="utf-8")
    bad_payload = json.dumps({"hook_event_name": "PostToolUse", "tool_input": {"file_path": str(bad)}})
    r = _run_md_guard(bad_payload)
    assert r.returncode == 2, r.stdout + r.stderr
    assert "禁字" in r.stderr
    clean = tmp_path / "ok.md"
    clean.write_text("干净一行\n", encoding="utf-8")
    ok_payload = json.dumps({"hook_event_name": "PostToolUse", "tool_input": {"file_path": str(clean)}})
    assert _run_md_guard(ok_payload).returncode == 0


def test_plugin_hooks_use_braced_plugin_root():
    """hook 命令须写 ${CLAUDE_PLUGIN_ROOT}。

    Codex 只替换花括号形态(codex-rs/hooks/src/engine/discovery.rs: fold replace "${key}"),
    且在 Windows 用 cmd.exe /C 执行(command_runner.rs: COMSPEC 兜底 cmd.exe /C)。
    故裸 $VAR 与 PowerShell 的 $env: 在 Windows 面都不展开,脚本路径必失效。
    """
    hooks = json.loads((PLUGIN / "hooks" / "hooks.json").read_text(encoding="utf-8"))
    handlers = [h for g in hooks["hooks"]["PostToolUse"] for h in g["hooks"]]
    assert handlers, "hooks.json 须有 PostToolUse 处理器"
    for h in handlers:
        for field in ("command", "commandWindows"):
            cmd = h.get(field)
            assert cmd, f"hooks.json 缺 {field}"
            assert "${CLAUDE_PLUGIN_ROOT}" in cmd, f"{field} 须用花括号形态(Codex 只替换 ${{VAR}})"
            assert "$env:" not in cmd, f"{field} 禁 PowerShell 语法:Windows 走 cmd.exe /C"
