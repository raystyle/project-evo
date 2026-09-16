# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
"""研究报告渲染工具:Markdown -> PDF(Typst + cmarker,模板 assets/templates/report.typ)。

报告 Markdown 是唯一真源,PDF 由模板渲染,禁止手工编辑产物。
本工具只做三件事:定位 typst、拼装渲染命令、报告结果。

用法:
    uv run render.py <报告.md> [--root <项目根>]      # 生成同名 PDF
    uv run render.py <报告.md> --check                # 只校验能否编译,不覆盖产物
    uv run render.py <报告.md> --typst <typst 路径>   # 显式指定 typst 可执行文件
    uv run render.py <报告.md> -o <输出.pdf>

根目录缺省为报告所在目录(Typst --root,约束模板与报告的可见范围);
模板随 skill 发行,渲染时复制到根下 .report-render/ 再编译,用完即删。

退出码:全部成功为 0;任一失败为其退出码(便于接入门禁)。
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
TEMPLATE = HERE.parent / "assets" / "templates" / "report.typ"
RENDER_DIR_NAME = ".report-render"

# CommonMark 里 ** 想闭合,定界符前面是标点、后面又是文字时不算 right-flanking,
# 加粗会失效并把星号原样印进 PDF(实测:**关键词:**正文 会印出星号)。
RISKY_BOLD = re.compile(r"[^\w\s]\*\*(?=\w)")


def _wsl_to_win(path: Path) -> str:
    """WSL 下调 Windows typst.exe 时,路径参数须转 Windows 形态(interop 不转 /mnt/wsl 类挂载)。"""
    try:
        out = subprocess.run(["wslpath", "-w", str(path)], capture_output=True, text=True)
        if out.returncode == 0 and out.stdout.strip():
            return out.stdout.strip()
    except FileNotFoundError:
        pass
    return str(path)


def lint_markdown(text: str) -> list[str]:
    warnings: list[str] = []
    for lineno, line in enumerate(text.splitlines(), start=1):
        for match in RISKY_BOLD.finditer(line):
            warnings.append(
                f"第 {lineno} 行:{match.group(0)!r} 处加粗可能不生效"
                f"(标点后紧跟 ** 且后面接文字),建议写成 **标签**:内容"
            )
    return warnings


def find_typst(explicit: str | None) -> Path:
    """定位 typst:显式 --typst、TYPST 环境变量、PATH 三选一。

    跨平台命令分发由宿主工具链统一维护(各平台 typst 落 PATH),本工具不烙死机器路径。
    """
    if explicit:
        p = Path(explicit).expanduser()
        if not p.exists():
            sys.exit(f"[render] 指定的 typst 不存在:{p}")
        return p

    env = os.environ.get("TYPST")
    if env and Path(env).expanduser().exists():
        return Path(env).expanduser()

    on_path = shutil.which("typst")
    if on_path:
        return Path(on_path)

    sys.exit(
        "[render] 找不到 typst。二选一:让 typst 进 PATH(跨平台命令分发由宿主工具链维护)、"
        "设置 TYPST 环境变量,或用 --typst 显式指定可执行文件路径。"
    )


def render_one(md: Path, typst: Path, root: Path, out: Path | None, check: bool, quiet: bool) -> int:
    if not md.exists():
        print(f"[render] 失败:文件不存在 {md}", file=sys.stderr)
        return 2
    if md.suffix.lower() != ".md":
        print(f"[render] 跳过(不是 Markdown):{md}", file=sys.stderr)
        return 2

    for warning in lint_markdown(md.read_text(encoding="utf-8")):
        print(f"[render] 警告:{md.name} {warning}", file=sys.stderr)

    if check:
        target = Path(tempfile.gettempdir()) / f"render-check-{md.stem}.pdf"
    else:
        target = out or md.with_suffix(".pdf")

    # 入口模板必须落在 --root 内;skill 目录可能不在根内,复制后编译,完删
    render_dir = root / RENDER_DIR_NAME
    render_dir.mkdir(parents=True, exist_ok=True)
    local_template = render_dir / "report.typ"
    shutil.copyfile(TEMPLATE, local_template)
    try:
        # WSL 调 Windows exe 时路径参数转 Windows 形态;Linux typst 原样直传
        convert = _wsl_to_win if (sys.platform != "win32" and typst.suffix == ".exe") else str
        rel = "/" + md.resolve().relative_to(root).as_posix()
        cmd = [
            str(typst),
            "compile",
            "--root",
            convert(root),
            "--input",
            f"md={rel}",
            convert(local_template),
            convert(target),
        ]
        proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")

        if not quiet:
            for stream, sink in ((proc.stdout, sys.stdout), (proc.stderr, sys.stderr)):
                text = (stream or "").strip()
                if text:
                    print(text, file=sink)

        if proc.returncode != 0:
            print(f"[render] 失败:{md.name}(typst 退出码 {proc.returncode})", file=sys.stderr)
            return proc.returncode or 1
    finally:
        local_template.unlink(missing_ok=True)
        try:
            render_dir.rmdir()
        except OSError:
            pass  # 目录非空(用户自建文件),留着

    size_kb = target.stat().st_size / 1024 if target.exists() else 0
    verb = "校验通过" if check else "已生成"
    print(f"[render] {verb}:{target}({size_kb:.0f} KB)")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="render",
        description="研究报告 Markdown -> PDF(Typst + cmarker,模板 assets/templates/report.typ)",
    )
    parser.add_argument("inputs", nargs="+", help="报告 Markdown 路径(可多个)")
    parser.add_argument("--root", help="项目根目录(默认报告所在目录;Typst --root)")
    parser.add_argument("-o", "--out", help="输出 PDF 路径(仅单个输入时可用)")
    parser.add_argument("--check", action="store_true", help="只校验编译,不覆盖正式产物")
    parser.add_argument("--typst", help="typst 可执行文件路径(覆盖 PATH 与环境探测)")
    parser.add_argument("-q", "--quiet", action="store_true", help="只输出结果行")
    args = parser.parse_args()

    if args.out and len(args.inputs) != 1:
        sys.exit("[render] --out 只能配合单个输入使用")

    typst = find_typst(args.typst)
    out = Path(args.out) if args.out else None

    failures = 0
    for md_arg in args.inputs:
        md = Path(md_arg).expanduser()
        root = (Path(args.root).expanduser() if args.root else md.parent).resolve()
        try:
            md.resolve().relative_to(root)
        except ValueError:
            sys.exit(f"[render] 报告必须位于根目录内:{md}(root={root})")
        code = render_one(md, typst, root, out, args.check, args.quiet)
        failures += 0 if code == 0 else 1
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
