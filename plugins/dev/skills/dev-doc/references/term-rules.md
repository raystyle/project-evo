# 约束术语表 lint

> 本篇只写格式、政策与挖词过程;词表本体永不复制于此(唯一权威在 `plugins/dev/scripts/termrules.py`,term-lint、check PE-13、pre-commit 三面同源引用)。文中引用具体词一律反引号包裹(行内代码豁免,词表不自扫)。

## 判据源

- zh-lint 词表:简明技术中文规范 0.2 蒸馏(批 145 裁撤,git 9189048^ 可复);1.3 禁用词、1.7 行业黑话与空泛词、1.8 英文术语全文一种写法
- gw_logs 语料挖词:对话语料高频黑话候选,蒸馏分流入表(方法与实证见研究档案 S020)

## 两层政策

- **ENFORCED(强制)**:本仓基线零命中的词。term-lint 退出码 1、check PE-13 FAIL、pre-commit 挡提交
- **PENDING(存量待清)**:本仓有基线命中或下游仓大概率有存量的词。`--pending` advisory 列出不计退出码;清完存量才迁入 ENFORCED(迁移即收紧,守在 `tests/test_repo_md_clean.py` 仓级回归)
- 迁移纪律:迁词前先清仓内存量;`进行` 迁入须排除「进行中/进行后」状态形(加负向环视)

## 工具面(全部 plugins/dev/scripts/,PEP 723 零依赖)

```bash
uv run plugins/dev/scripts/term-lint.py .             # ENFORCED 层(0 净/1 违规/2 用法)
uv run plugins/dev/scripts/term-lint.py . --pending   # 加列 PENDING 存量(advisory)
uv run plugins/dev/scripts/term-lint.py --staged      # 暂存区挡板(pre-commit 挂)
uv run .tools/check.py .                              # PE-13(机器面 --json 同)
uv run plugins/dev/scripts/term-mine.py --since 2026-10-12 --slice 14d \
  --kind client_request --sample 5 --out-dir /tmp/term-mine/   # 语料挖词(研究道)
```

## 豁免通道

- 行内代码、围栏代码块、frontmatter:结构豁免(复用 mdrules 机制,同禁字面)
- `PEVO_TERM_ALLOW="正则;正则"`:docs/ 历史档案存量豁免(匹配 `docs/相对路径:行`,报 SKIP 不 FAIL;根三件 AGENTS/README/CHANGELOG 永不受益;与 PEVO_CHECK_ALLOW 同惯例)
- 引用具体禁词时用反引号包裹(示例见 termrules.py 注释),豁免即合规的引用写法

## 挖词程序(term-mine,一次性研究道)

1. 连接:`~/.ctx/reader.env`(只读);HTTP 主道客户端证书强制时自动落 ssh 备道(SQL 走 stdin)
2. 限流三板:payload 截头 2000 字 + 5% 随机抽样 + LIMIT;禁 `ORDER BY`(实测爆 ClickHouse 内存上限)
3. kind 选 `client_request`(对话正文;`sse` 是流块噪声)
4. 候选提取:种子词频扫验活 + CJK 二字组离群(需停用词,原始 top 全常用词)+ 英文俚语种子表词边界扫
5. 蒸馏分流:零基线命中入 ENFORCED、有存量入 PENDING、低频不足立据弃(判例记 S020)
6. 原文语料不进仓(落 /tmp 等仓外位),蒸馏结论进研究档案

## 表式(条目格式)

dict 形,词为键、修法提示为值(一句可执行,如 `词: 用批准词`);四表 ZH_BANNED、ZH_CHOICE、EN_JARGON、TERM_VARIANTS(变体归一,首版空)+ PENDING 层。zh 最长优先匹配防短词误命中长词内部;en 词边界匹配大小写不敏感。
