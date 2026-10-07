# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
"""fleet-exec:跨机 shell 格普通进程通道薄封装(pane send-text 加 enter 加 wait-output 收标加 read 回执)。

用法:
  uv run .tools/fleet-exec.py [--machine <label>] --pane <pane> --cmd "<shell 命令>" --marker <收标> [--timeout <毫秒>] [--lines <N>]

本机省 --machine。逐条回显所执行的 herdr 命令(活权威语义不藏,可审计);回执为 pane read 正文;
退出码 0 收标命中 / 1 未收标或通道失败(仍打印 pane 实读供判送达) / 2 参数错。
通道纪律对照 herdr-flywheel pitfalls:stalled 与未收标都不证未送达,重发前必实读;TUI 未就绪期键入会被吞。
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys


def build_cmd(args: list[str], machine: str | None) -> list[str]:
    """组装 herdr 命令行;--machine 恒为全局前缀且不与其他 launch 选项叠加。"""
    cmd = ["herdr"]
    if machine:
        cmd += ["--machine", machine]
    return cmd + args


def run_herdr(args: list[str], machine: str | None) -> subprocess.CompletedProcess:
    cmd = build_cmd(args, machine)
    print("+ " + " ".join(cmd), file=sys.stderr)
    return subprocess.run(cmd, capture_output=True, text=True,
                          encoding="utf-8", errors="replace")


def main(argv: list[str] | None = None) -> int:
    for stream in (sys.stdout, sys.stderr):
        if stream.encoding and stream.encoding.lower().replace("-", "") != "utf8":
            stream.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(
        prog="fleet-exec.py",
        description="普通进程通道薄封装:send-text 加 enter 加 wait-output 收标加 read 回执",
    )
    parser.add_argument("--machine", help="远程机器 label(本机省略)")
    parser.add_argument("--pane", required=True, help="目标 shell 格 pane ID")
    parser.add_argument("--cmd", required=True, help="要在格内执行的 shell 命令(自带收标 echo 更稳)")
    parser.add_argument("--marker", required=True, help="wait-output 收标文本")
    parser.add_argument("--timeout", type=int, default=30000, help="收标等待毫秒(默认 30000)")
    parser.add_argument("--lines", type=int, default=12, help="回执读取行数(默认 12)")
    args = parser.parse_args(argv)

    r = run_herdr(["pane", "send-text", args.pane, args.cmd], args.machine)
    if r.returncode != 0:
        print(f"send-text 失败: {r.stderr.strip()[:200]}", file=sys.stderr)
        return 1
    r = run_herdr(["pane", "send-keys", args.pane, "enter"], args.machine)
    if r.returncode != 0:
        print(f"send-keys 失败: {r.stderr.strip()[:200]}", file=sys.stderr)
        return 1
    r = run_herdr(["pane", "wait-output", args.pane, "--match", args.marker,
                   "--timeout", str(args.timeout)], args.machine)
    hit = r.returncode == 0
    if not hit:
        print(f"未收标({args.marker});不证命令失败,以下实读供判送达", file=sys.stderr)
    r = run_herdr(["pane", "read", args.pane, "--source", "visible",
                   "--lines", str(args.lines)], args.machine)
    try:
        print(json.loads(r.stdout)["result"]["read"]["text"])
    except (json.JSONDecodeError, KeyError, TypeError):
        print(r.stdout or r.stderr)
    return 0 if hit else 1


if __name__ == "__main__":
    sys.exit(main())
