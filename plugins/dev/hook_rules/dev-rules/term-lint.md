---
match: .md
---

## 约束术语纪律(改 md 时)

- ENFORCED 词表(termrules.py)强制:zh 黑话禁用词(`赋能`、`抓手` 等 28 词,全表见 termrules.py)、选词三枚、en 黑话八枚(全表见 termrules.py)
- 每词修法见 term-lint 输出;PENDING 存量词(收口/沉淀/缺省/报错/闭环 等)advisory 不挡,清完存量才迁入强制
- 引用具体禁词时反引号包裹(行内代码豁免)
- 门禁:`uv run plugins/dev/scripts/term-lint.py .`(退出码 0/1/2);pre-commit --staged 挡板
