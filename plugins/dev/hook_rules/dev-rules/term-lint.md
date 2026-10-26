---
match: .md
---

## 约束术语纪律(改 md 时)

- ENFORCED 词表(termrules.py)强制:zh 黑话禁用词 42 枚(`赋能`、`抓手`、`挂了`、`炸了` 等,批 177 扩表)、选词三枚、en 黑话与短语 22 枚(单词加多词短语同表词边界匹配)
- 每词修法见 term-lint 输出;PENDING 存量词 30 枚(`口径`、`落地`、`nit`、`收口` 等)advisory 不挡,清完存量才迁入强制;域词白名单(`知会`、`翻台` 等)永不收
- 引用具体禁词时反引号包裹(行内代码豁免);扩表与挖词方法见 S020 与 S021
- 门禁:`uv run plugins/dev/scripts/term-lint.py .`(退出码 0/1/2);pre-commit --staged 挡板
