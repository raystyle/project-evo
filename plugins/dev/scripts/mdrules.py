"""markdown 禁字检测基元(唯一权威;check PE-12 / scan / md-guard 同源引用)。

标准:《中英文 Markdown 技术文档字符与标点硬禁令》四类禁字。
本模块只提供逐行检测与判定,不做修正(修正属人工/编辑器职责)。
豁免区判定:YAML frontmatter、围栏代码块、行内代码、markdown 链接/图片、裸 URL。
零第三方依赖,标准库即可运行。
"""

from __future__ import annotations

import re

DASHES = "—–―−ー"
DOUBLE_DASH = "——"
ARROWS = re.compile("[←-⇿➜⬅⬆⬇⬀-⬏]")
EMOJI = re.compile("[☀-➿\U0001f000-\U0001faff✅⚠]")
SMART_QUOTES = re.compile("[“”‘’]")
FW_ALNUM = re.compile("[Ａ-Ｚａ-ｚ０-９]")
SKIP_DIRS = {".git", ".venv", "node_modules", "__pycache__", ".pytest_cache",
             ".claude", ".agents", ".rumdl_cache", "target", "dist", "build"}

_INLINE = re.compile(r"(`[^`]+`)|(\[[^\]]*\]\([^)\s]*(?:\([^)]*\)[^)\s]*)*\))|(https?://[^\s)\]]+)")


def strip_inline_exemptions(line: str) -> str:
    """去掉行内豁免段(行内代码/链接/URL),返回待判定文本。"""
    return _INLINE.sub("", line)


def line_violations(raw_line: str, in_fence: bool) -> list[str]:
    """单行违规类别(空列表=合规)。in_fence 时整行豁免。

    error 级四类:破折号/连接号、Unicode 箭头、emoji、智能引号与全角字母数字。
    中文语境半角标点属排版偏好,不做 error 告警(修正交由人工,同家族 mdcharlint 分级)。
    """
    if in_fence or raw_line.lstrip().startswith("```"):
        return []
    line = strip_inline_exemptions(raw_line)
    out = []
    if DOUBLE_DASH in line or any(c in line for c in DASHES):
        out.append("破折号/连接号")
    if ARROWS.search(line):
        out.append("Unicode 箭头")
    if EMOJI.search(line):
        out.append("emoji")
    if SMART_QUOTES.search(line):
        out.append("智能引号")
    if FW_ALNUM.search(line):
        out.append("全角字母数字")
    return out


def file_violations(text: str) -> dict[int, list[str]]:
    """整文件逐行扫描(YAML frontmatter 与围栏块豁免),返回 {行号(1 起): 类别列表}。"""
    out: dict[int, list[str]] = {}
    in_fence = False
    lines = text.splitlines()
    start = 0
    if lines[:1] == ["---"]:
        close = next((i for i in range(1, len(lines)) if lines[i] == "---"), None)
        if close is not None:
            start = close + 1
    for i in range(start, len(lines)):
        if lines[i].lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        v = line_violations(lines[i], in_fence)
        if v:
            out[i + 1] = v
    return out


def skill_description_violations(text: str) -> list[str]:
    """SKILL.md frontmatter description 面检(REQ-057 规范 A2/A3;md-guard 挡板接线)。

    - 折叠后 ≤400 字符(治理层收紧,官方 spec 硬顶 1024 不在此重复检)
    - 三句形:含 Use when 触发句与「不要用于」排除句
    非 SKILL.md 形态(无 frontmatter)返回空,不误报。
    """
    lines = text.splitlines()
    if lines[:1] != ["---"]:
        return []
    close = next((i for i in range(1, len(lines)) if lines[i] == "---"), None)
    if close is None:
        return []
    desc: list[str] = []
    in_desc = False
    for l in lines[1:close]:
        if l.startswith("description:"):
            in_desc = True
            v = l.split(":", 1)[1]
            if v.lstrip().startswith(">-"):
                v = v.lstrip()[2:]
            desc.append(v.strip())
        elif in_desc and l[:1] in (" ", "\t"):
            desc.append(l.strip())
        else:
            in_desc = False
    joined = "".join(desc)
    if not joined:
        return ["description 为空"]
    out: list[str] = []
    if len(joined) > 400:
        out.append(f"description {len(joined)} 字符超 400 上限(规范 A2)")
    if "Use when" not in joined:
        out.append("description 缺 Use when 触发句(规范 A2 三句形)")
    if "不要用于" not in joined:
        out.append("description 缺「不要用于」排除句(规范 A2 三句形)")
    return out
