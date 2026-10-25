# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
# term-lint:约束术语表静检(非标准中文、英文黑话俚语),只报不改。
# 词表唯一权威 termrules.py(ENFORCED 层);PENDING 存量层 --pending 列出不计门禁。
# 退出码三态:0 干净 / 1 有违规 / 2 用法或出错(门禁惯例同 check 与 scan)。
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from termrules import (  # noqa: E402
    PENDING,
    file_pending_violations,
    file_term_violations,
)

from mdrules import SKIP_DIRS  # noqa: E402


def iter_md_files(paths: list[str]) -> list[Path]:
    """收集 .md 文件(目录递归,跳 SKIP_DIRS;文件直收)。"""
    out: list[Path] = []
    for raw in paths:
        p = Path(raw)
        if p.is_file():
            out.append(p)
        elif p.is_dir():
            for f in sorted(p.rglob("*.md")):
                if not any(part in SKIP_DIRS for part in f.parts):
                    out.append(f)
    return out


def scan(files: list[Path], with_pending: bool) -> int:
    total = 0
    pending_total = 0
    for p in files:
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except OSError as e:  # 只报不改,读失败按错误退出
            print(f"[error] 读失败 {p}: {e}", file=sys.stderr)
            return 2
        for lineno, hits in file_term_violations(text).items():
            for cat, fix in hits:
                print(f"[error][{p}:{lineno}] {cat}:{fix}")
                total += 1
        if with_pending:
            for lineno, hits in file_pending_violations(text).items():
                for w, fix in hits:
                    print(f"[pending][{p}:{lineno}] 存量词「{w}」:{fix}")
                    pending_total += 1
    if total:
        print(f"共 {total} 项违规")
    if with_pending:
        print(f"PENDING 存量 {pending_total} 项(不计门禁,收紧计划见 term-rules.md)")
    return 1 if total else 0


def scan_staged(with_pending: bool) -> int:
    """暂存区模式:检已 staged 的 .md(同 md-guard --staged 形)。"""
    r = subprocess.run(
        ["git", "diff", "--cached", "--name-only", "--diff-filter=ACMR"],
        capture_output=True, text=True,
    )
    if r.returncode != 0:
        print(f"[error] git 调用失败:{r.stderr.strip()}", file=sys.stderr)
        return 2
    files = [Path(f) for f in r.stdout.splitlines() if f.endswith(".md")]
    files = [f for f in files if f.exists()]
    return scan(files, with_pending)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="约束术语表静检(非标准中文、英文黑话俚语),词表权威 termrules.py",
    )
    ap.add_argument("paths", nargs="*", help="待检文件或目录(空则看用法)")
    ap.add_argument("--staged", action="store_true", help="检暂存区 .md(提交挡板)")
    ap.add_argument("--pending", action="store_true",
                    help="额外列 PENDING 存量层命中(advisory,不计退出码)")
    args = ap.parse_args(argv)
    if args.staged:
        return scan_staged(args.pending)
    if not args.paths:
        ap.print_usage()
        return 2
    return scan(iter_md_files(args.paths), args.pending)


if __name__ == "__main__":
    sys.exit(main())
