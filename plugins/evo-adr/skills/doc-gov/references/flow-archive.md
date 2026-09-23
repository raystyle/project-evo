# 日记与研究档案机制：过程留痕与证据沉淀

> docs 骨架中 diary 与 research 两目录的运转机制。结构地位红线:diary 与 research 是保留核心结构,不可裁撤(用户裁定 2026-09-16);guides 才按需生长。

## diary 日记（过程档案）

- 一天一篇,命名 `YYYY-MM-DD-主题.md`;初始化当天记首笔(骨架验收项)
- 记当日裁定、踩坑与门禁实录;过程性文档不改写,存量禁字走 PE-11 豁免通道(`PEVO_CHECK_ALLOW` 路径级,历史不改写)
- 分工:过程进 diary,不可逆决策进 ADR,需求与实现进 REQ;日记是二者的素材池,择要升格出档(沉淀链见 exp-sedimentation.md)

## research 研究（证据档案）

- 编号 `SNNN` 落 docs/research,编号退役不复用;README 索引登记(编号、链接、主题、状态、日期)
- 研究结论必须标六态;结论被工程采用后择要升 ADR(证据变决策),全文留档
- 无真实研究的仓 research 暂空合法(PE-09 SKIP);发现/获取/研读管线见同市场 skill `evo-research:research`,正式成文按 doc-gov 投影纪律出 md(ADR-0015 起 evo-research 不再带 report skill)

## 与旧体系的承接

- 旧 proven 语义(已完成方案全文)由 implemented REQ 加关联 ADR 承接,proven 目录择要升 ADR 后全文留档
- 旧 mistakes 并入 ADR(被否决的选择也是决策)或 exp 沉淀链
- 迁移仓的 diary 与 research 存量直接归位,不推倒重写(迁移不是搬运是重审)
