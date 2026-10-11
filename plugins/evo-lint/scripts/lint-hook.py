# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
# evo-lint 后缀静检 hook:Edit/Write/MultiEdit 落盘后按后缀自动静检,报错信息回传(exit 2)。
# 纪律:只做快检查(秒级),重检查(clippy/tsc 全量)进门禁与 CI;工具缺位放行(分发归 omc/ark,只认 PATH)。
import json
import os
import re
import shutil
import subprocess
import sys

MD_FORBIDDEN = [
    ("emoji", re.compile(r"[\U0001F300-\U0001FAFF☀-➿]")),
    ("box-drawing", re.compile(r"[─-╿]")),
    ("em-dash", re.compile(r"——|—")),
]

AGENTS_MAX_LINES = int(os.environ.get("EVO_LINT_AGENTS_MAX", "200"))
CLAUDE_MAX_LINES = int(os.environ.get("EVO_LINT_CLAUDE_MAX", "50"))
SKILL_MAX_LINES = int(os.environ.get("EVO_LINT_SKILL_MAX", "500"))


def check_md(text: str, name: str) -> list[str]:
    errs = []
    for lineno, line in enumerate(text.splitlines(), 1):
        for label, pat in MD_FORBIDDEN:
            if pat.search(line):
                errs.append(f"{name}:{lineno} 禁字({label})")
        if line.startswith("#") and ("(" in line or ")" in line):
            errs.append(f"{name}:{lineno} 标题含括号")
    n = len(text.splitlines())
    base = os.path.basename(name)
    if base == "AGENTS.md" and n > AGENTS_MAX_LINES:
        errs.append(f"{name} 行数 {n} 超 AGENTS 上限 {AGENTS_MAX_LINES}(EVO_LINT_AGENTS_MAX 可裁)")
    if base == "CLAUDE.md" and n > CLAUDE_MAX_LINES and "@AGENTS.md" not in text:
        errs.append(f"{name} 行数 {n} 超 CLAUDE 上限 {CLAUDE_MAX_LINES}(单行桥接形免检)")
    if base == "SKILL.md" and n > SKILL_MAX_LINES:
        errs.append(f"{name} 行数 {n} 超 SKILL 上限 {SKILL_MAX_LINES}")
    return errs


def run_tool(cmd: list[str]) -> list[str]:
    exe = shutil.which(cmd[0])
    if not exe:
        return []
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=20)
    except (subprocess.TimeoutExpired, OSError):
        return []
    if r.returncode != 0:
        out = (r.stdout + r.stderr).strip().splitlines()
        keep = [ln for ln in out if ln.strip()][:8]
        return keep or [f"{cmd[0]} 退出码 {r.returncode}"]
    return []


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        return 0
    if not isinstance(payload, dict):
        return 0
    ti = payload.get("tool_input")
    if not isinstance(ti, dict):
        return 0
    path = ti.get("file_path") or ti.get("filePath") or ""
    if not path or not os.path.isfile(path):
        return 0
    # 辖域限仓内(ADR-0017 同批裁定,与 md-guard 同律):事件带 cwd 且 file_path 在其外时放行
    cwd = payload.get("cwd")
    if cwd:
        try:
            rp, rc = os.path.realpath(path), os.path.realpath(cwd)
            if os.path.commonpath([rp, rc]) != rc:
                return 0
        except ValueError:
            return 0
    ext = os.path.splitext(path)[1].lower()
    errs: list[str] = []
    if ext == ".md":
        try:
            text = open(path, encoding="utf-8").read()
        except OSError:
            return 0
        errs = check_md(text, path)
    elif ext == ".py":
        errs = run_tool(["ruff", "check", "--no-cache", "--quiet", path])
    elif ext == ".rs":
        errs = run_tool(["rustfmt", "--check", "--edition", "2024", path])
    elif ext in (".ts", ".tsx", ".mts", ".cts"):
        errs = run_tool(["eslint", path])
    if errs:
        print("evo-lint 静检报错(逐条修,豁免留因由):", file=sys.stderr)
        for e in errs:
            print(f"  {e}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
