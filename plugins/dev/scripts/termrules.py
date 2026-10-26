"""约束术语表(唯一权威;term-lint / check PE-13 / pre-commit 同源引用,不复制规则)。

表源:zh-lint 词表(批 145 裁撤,git 9189048^ 复原)加 gw_logs 语料挖词
(方法与实证见 dev-doc skill 的 term-rules.md 与 docs/research/S020)。
两层政策:ENFORCED = 当下强制(本仓基线零命中);PENDING = 存量待清(基线
有命中,先清存量再迁入 ENFORCED,迁移即收紧)。豁免:行内代码、围栏、
frontmatter(复用 mdrules 机制);PEVO_TERM_ALLOW 正则豁免下游仓 docs/
档案,根三件永不受益(与 PEVO_CHECK_ALLOW 同惯例)。
"""

from __future__ import annotations

import re
from typing import Iterator

from mdrules import strip_inline_exemptions

# ENFORCED 禁用词:词 -> 修法提示(一句,可执行)。条目自 zh-lint CORE_BANNED
# 逐条过仓基线,有存量命中的移 PENDING;新词自语料挖词入列(须零基线命中)。
ZH_BANNED: dict[str, str] = {
    "加以": "删除,直接用后面的动词",
    "予以": "删除,直接用后面的动词",
    "作出": "直接用动词",
    "做出": "直接用动词",
    "的话": "删除",
    "一下": "删除",
    "尽快": "写具体时限",
    "众所周知": "删除",
    "不难看出": "删除",
    "赋能": "写出提供、支持或具体能力",
    "抓手": "用措施、方法",
    "拉通": "用连接、同步",
    "赛道": "用领域、市场",
    "颗粒度": "用粒度",
    "打法": "用方法、方案",
    "组合拳": "写出具体措施",
    "牵头": "用负责",
    "倒逼": "用促使、要求",
    "体感": "写出具体数值或现象",
    "拉齐": "用统一",
    "打通": "写出具体连接与通路",
    "顶层设计": "用总体设计",
    "底层逻辑": "用原理、原因",
    "出参": "用返回值",
    "登陆": "用登录",
    "帐号": "用账号",
    "阀值": "用阈值",
    "布署": "用部署",
    # 批 177 扩表(CH 块频 26.9 万块双源,仓基线零命中;判据见 S021)
    "挂了": "名词用故障,动词用崩溃或退出",
    "捞": "写具体检索或取回动作",
    "打样": "用示例、参照实现",
    "阵地": "用领域、方面",
    "秀": "删除或写具体效果",
    "炸了": "写具体错误与现象",
    "崩了": "写具体错误与现象",
    "爆炸": "写具体数量级或现象",
    "过一遍": "写具体步骤或检查项",
    "战场": "用场景、领域",
    "重起": "用重启",
    "做实验": "用跑实验、测试",
    "先对齐": "写出要对齐的口径或事项",
    "排期": "写具体日期或里程碑",
}

# ENFORCED 选词表:不批准词 -> 批准词。
ZH_CHOICE: dict[str, str] = {
    "单击": "点击",
    "点选": "点击",
    "摁": "按",
}

# ENFORCED 英文黑话与俚语:词 -> 修法提示(小写键,词边界匹配,大小写不敏感)。
# 语料实测(gw_logs 14 天 16 万块,2026-10-26):magic 591、stuff 426、synergy 71、
# hacky 44;仓基线零命中故 ENFORCED。
# 批 177 扩表:ground truth 776、edge case 111、actionable 80、sanity check 69 等
# (CH 块频,仓基线零命中;S021)。短语在此表按整串词边界匹配。
EN_JARGON: dict[str, str] = {
    "leverage": "用 use",
    "utilize": "用 use",
    "synergy": "写出具体协作效果",
    "basically": "删除或写出准确判断",
    "obviously": "删除(显然类断言不立)",
    "stuff": "写出具体对象名",
    "hacky": "写出具体缺陷与修法",
    "magic": "写出具体机制(魔法数字写数值来源)",
    # 批 177 扩表
    "ground truth": "用实测基准、标注数据",
    "ping me": "用来信通知我、联系我",
    "edge case": "用边界情况",
    "actionable": "用可执行的、可操作的",
    "sanity check": "用基本校验、快速自检",
    "race condition": "技术术语,用竞态(首现括注可留)",
    "bandwidth": "按语境用吞吐、精力、带宽",
    "source of truth": "用唯一权威源",
    "quick win": "用低成本快改",
    "drop-in": "用直接替换、即插即用",
    "paradigm": "用范式或写具体模式",
    "nitpick": "写具体小问题",
    "utilization": "用 usage、使用率",
    "going forward": "用 from now on、later",
    "seamless": "写出具体衔接点",
}

# 同一概念多写法归一(stc 1.8,首版留空,候补自语料挖词)。
TERM_VARIANTS: dict[str, str] = {}

# PENDING 存量待清层:本仓有基线命中,暂不强制;--pending advisory 列出。
# 迁入 ENFORCED 前先清仓内存量;「进行」迁入须排除「进行中/进行后」状态形。
# 基线实测(2026-10-26,term-lint 首跑):收口 45、沉淀 39、报错 21、进行 10、
# 缺省 31、对标 5、入参 4、删掉 2、点按 1、心智 1、若干 1、痛点 2。
# 语料高频黑话存量:闭环 19;落地、兜底、链路、打通、串联语料高频但仓内零命中,
# 已入 ENFORCED(见 docs/research/S020 蒸馏分流)。
PENDING: dict[str, str] = {
    "进行": "删除,直接用后面的动词",
    "沉淀": "用保存、形成、积累",
    "收口": "用统一、汇总",
    "报错": "名词用错误,动词用返回错误或显示错误",
    "痛点": "写出具体困难或需求",
    "缺省": "用默认",
    "对标": "用参照、对比",
    "入参": "用参数",
    "删掉": "删除",
    "点按": "点击",
    "心智": "用认知、印象",
    "若干": "写数字",
    "串联": "按顺序写各步,或用链表、流水线",
    "反哺": "写出具体输入与去向",
    "闭环": "写出具体完整流程或验证回路",
    "落地": "写出具体实现或生效位置",
    "兜底": "写出具体默认行为或异常处理",
    "链路": "用调用路径、数据流",
    # 批 177 扩表(CH 块频加 ctxs 双源,仓内有存量;S021)
    "翻车": "写具体失败与原因",
    "定谳": "用敲定、确认结论",
    "卡点": "写具体阻塞项",
    "复盘": "用回顾、总结",
    "口径": "用说法、表述、约定",
    "拍板": "用决定、确认",
    "踩坑": "写具体问题与根因",
    "舰队": "机构隐喻,技术文改用集群、一组机器",
    "战役": "改用专项、集中变更",
    "样板": "用示例、模板",
    "smoke test": "用冒烟测试(中文写法)或首现括注",
    "nit": "评审术语面可留,正文写具体问题与位置",
}

# 域词白名单:舰队操作面技能术语(streams/tasks/agents 语义),禁用表不收
DOMAIN_ALLOW: set[str] = {"知会", "翻台", "翻台重载"}


def _compile_zh(table: dict[str, str]) -> list[tuple[str, str, re.Pattern[str]]]:
    """zh 表编译:最长优先,防短词命中长词内部。"""
    return [
        (w, fix, re.compile(re.escape(w)))
        for w, fix in sorted(table.items(), key=lambda kv: -len(kv[0]))
    ]


def _compile_en(table: dict[str, str]) -> list[tuple[str, str, re.Pattern[str]]]:
    """en 表编译:词边界,大小写不敏感。"""
    return [
        (w, fix, re.compile(rf"\b{re.escape(w)}\b", re.IGNORECASE))
        for w, fix in sorted(table.items(), key=lambda kv: -len(kv[0]))
    ]


_ZH_BANNED_C = _compile_zh(ZH_BANNED)
_ZH_CHOICE_C = _compile_zh(ZH_CHOICE)
_EN_JARGON_C = _compile_en(EN_JARGON)
_FENCE = re.compile(r"^\s*(```|~~~)")


def line_term_violations(raw_line: str) -> list[tuple[str, str]]:
    """单行扫描(围栏行与行内代码豁免后):返回 [(类别(词), 修法)]。"""
    if _FENCE.match(raw_line):
        return []
    body = strip_inline_exemptions(raw_line)
    hits: list[tuple[str, str]] = []
    for w, fix, pat in _ZH_BANNED_C:
        if pat.search(body):
            hits.append((f"禁用词「{w}」", fix))
    for w, fix, pat in _ZH_CHOICE_C:
        if pat.search(body):
            hits.append((f"选词「{w}」不批准", f"用「{fix}」"))
    for w, fix, pat in _EN_JARGON_C:
        if pat.search(body):
            hits.append((f"英文黑话「{w}」", fix))
    return hits


def _body_lines(text: str) -> Iterator[tuple[int, str]]:
    """产出可检行号与行文:跳 frontmatter 与围栏内(机制同 mdrules.file_violations)。"""
    lines = text.splitlines()
    in_fence = False
    in_front = False
    front_done = False
    for i, line in enumerate(lines, 1):
        if i == 1 and line.strip() == "---":
            in_front = True
            continue
        if in_front:
            if line.strip() == "---":
                in_front = False
                front_done = True
            continue
        if not front_done and line.strip() == "---" and i <= 3:
            continue
        if _FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        yield i, line


def file_term_violations(text: str) -> dict[int, list[tuple[str, str]]]:
    """文件扫描:返回 {行号: [(类别, 修法)]}(ENFORCED 层)。"""
    out: dict[int, list[tuple[str, str]]] = {}
    for i, line in _body_lines(text):
        hits = line_term_violations(line)
        if hits:
            out[i] = hits
    return out


def file_pending_violations(text: str) -> dict[int, list[tuple[str, str]]]:
    """PENDING 层扫描(advisory,不计门禁):返回 {行号: [(词, 修法)]}。"""
    pending_c = _compile_zh(PENDING)
    out: dict[int, list[tuple[str, str]]] = {}
    for i, line in _body_lines(text):
        if _FENCE.match(line):
            continue
        body = strip_inline_exemptions(line)
        hits = [(w, fix) for w, fix, pat in pending_c if pat.search(body)]
        if hits:
            out[i] = hits
    return out
