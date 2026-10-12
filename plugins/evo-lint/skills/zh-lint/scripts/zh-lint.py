# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
# zh-lint:简明技术中文(STC)静检,给技术文档与解释性回答用。
# 判据源:简明技术中文规范 0.2(六节四十条,上游仓为活权威)+ 词表三张表;内置先验核,
# --wordlist 可外接上游词表全表(兼容其表式);只报不改。禁用词命中与句长超限为 error,建议级为 advisory。
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# 先验核:无条件、低误报的禁用词(词 -> 改用提示)。条件形(仅操作句等)走 --wordlist 或人工。
CORE_BANNED: dict[str, str] = {
    "进行": "删除,直接用后面的动词",
    "加以": "删除,直接用后面的动词",
    "予以": "删除,直接用后面的动词",
    "作出": "直接用动词",
    "做出": "直接用动词",
    "的话": "删除",
    "一下": "删除",
    "大概": "描述句用约,操作句写数值",
    "大约": "描述句用约,操作句写数值",
    "若干": "写数字",
    "尽快": "写具体时限",
    "及时": "写具体时限或删除",
    "基本": "删除或写出例外",
    "基本上": "删除或写出例外",
    "比较": "删除或给出比较对象",
    "较为": "删除或给出比较对象",
    "大量": "写数值或比例",
    "少量": "写数值或比例",
    "大部分": "写数值或比例",
    "多数": "写数值或比例",
    "少数": "写数值或比例",
    "一定要": "用必须",
    "务必": "用必须",
    "千万": "用必须",
    "最好": "用建议",
    "不得": "用禁止或不要",
    "不准": "用禁止或不要",
    "不许": "用禁止或不要",
    "关掉": "窗口连接用关闭,程序用停止或退出",
    "众所周知": "删除",
    "显然": "删除",
    "不难看出": "删除",
    "其实": "删除",
    "事实上": "删除",
    "实际上": "删除",
    "也就是说": "用即",
    "赋能": "写出提供、支持或具体能力",
    "抓手": "用措施、方法",
    "拉通": "用连接、同步",
    "沉淀": "用保存、形成、积累",
    "赛道": "用领域、市场",
    "心智": "用认知、印象",
    "收口": "用统一、汇总",
    "颗粒度": "用粒度",
    "打法": "用方法、方案",
    "组合拳": "写出具体措施",
    "痛点": "写出具体困难或需求",
    "牵头": "用负责",
    "倒逼": "用促使、要求",
    "体感": "写出具体数值或现象",
    "拉齐": "用统一",
    "对标": "用参照、对比",
    "顶层设计": "用总体设计",
    "底层逻辑": "用原理、原因",
    "入参": "用参数",
    "出参": "用返回值",
    "报错": "名词用错误,动词用返回错误或显示错误",
    "登陆": "用登录",
    "帐号": "用账号",
    "缺省": "用默认",
    "阀值": "用阈值",
    "布署": "用部署",
}
# 先验核:选词表(不批准词 -> 批准词,仅无条件形)
CORE_CHOICE: dict[str, str] = {
    "单击": "点击", "点按": "点击", "点选": "点击",
    "按压": "按", "摁": "按",
    "删掉": "删除",
}

INLINE = re.compile(r"`[^`]*`")
NUM_ITEM = re.compile(r"^\s*(\d+[.、)])\s*")


def count_units(text: str) -> int:
    """字数算法:汉字 1、英文单词或数字串 1、行内代码段 1、标点不计。"""
    t = INLINE.sub(" W ", text)
    han = len(re.findall(r"[一-鿿]", t))
    words = len(re.findall(r"[A-Za-z0-9]+", t))
    return han + words


def parse_wordlist(path: Path) -> tuple[dict[str, str], dict[str, str]]:
    """解析上游词表三张表:禁用词表与选词表(自动检查=是 的条目;「仅」条件仅支持操作句与编号项内两种)。"""
    banned: dict[str, str] = {}
    choice: dict[str, str] = {}
    in_banned = in_choice = False
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line.startswith("| 禁用词"):
            in_banned, in_choice = True, False
            continue
        if line.startswith("| 意义"):
            in_banned, in_choice = False, True
            continue
        if line.startswith("|") and in_banned:
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) >= 4 and cells[3] == "是":
                for w in cells[0].split("、"):
                    if w:
                        banned[w] = cells[1]
        elif line.startswith("|") and in_choice:
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) >= 4 and cells[3] == "是" and len(cells) >= 5:
                for w in cells[2].split("、"):
                    if w:
                        choice[w] = cells[1]
    return banned, choice


def check_line(line: str, lineno: int, name: str, banned: dict[str, str],
               choice: dict[str, str], strict: bool, out: list) -> None:
    body = INLINE.sub(" ", line)  # 行内代码内容不参检
    is_op = bool(NUM_ITEM.match(line))
    for w, fix in sorted(banned.items(), key=lambda kv: -len(kv[0])):
        if w in body:
            out.append((lineno, "error", f"禁用词「{w}」:{fix}"))
    for w, fix in choice.items():
        if w in body:
            out.append((lineno, "error", f"选词:「{w}」不批准,用「{fix}」"))
    # 句长:按句末标点拆句;操作句限 30,描述句限 40(严格模式降为建议也报,常规同为必须)
    for sent in re.split(r"(?<=[。;!?])", body):
        sent = sent.strip()
        if not sent or len(sent) < 8:
            continue
        n = count_units(sent)
        limit = 30 if is_op or NUM_ITEM.match(sent) else 40
        if n > limit:
            kind = "操作句" if limit == 30 else "描述句"
            out.append((lineno, "error", f"句长超限:{kind} {n} 字 > {limit}(「{sent[:18]}…」)"))


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="简明技术中文(STC)静检,只报不改")
    ap.add_argument("files", nargs="*", help="待检 md 或文本文件")
    ap.add_argument("--wordlist", type=Path, default=None, help="外接词表(上游 词表.md 表式,三张表)")
    ap.add_argument("--strict", action="store_true", help="严格模式(未实现差异面,预留)")
    args = ap.parse_args(argv)
    banned, choice = dict(CORE_BANNED), dict(CORE_CHOICE)
    if args.wordlist and args.wordlist.is_file():
        b, c = parse_wordlist(args.wordlist)
        banned.update(b)
        choice.update(c)
    if not args.files:
        ap.print_usage()
        return 2
    total = 0
    for f in args.files:
        p = Path(f)
        if not p.is_file():
            print(f"[note] 跳过不存在的 {f}")
            continue
        out: list = []
        for i, line in enumerate(p.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            if line.lstrip().startswith(("#", "|", "```", "---")) and not line.lstrip().startswith("#") is False:
                pass
            if line.lstrip().startswith("```"):
                continue
            check_line(line, i, str(p), banned, choice, args.strict, out)
        for lineno, level, msg in out:
            print(f"[{level}][{p}:{lineno}] {msg}")
        total += len(out)
    print(f"共 {total} 项发现")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
