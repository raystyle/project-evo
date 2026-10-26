---
patterns: [doc 注释, docstring, 契约注释, 文档即代码, docs as code, 投影, 单一权威源, 生成物, 漂移守卫]
---

## 代码 doc 注释与文档即代码指导

- 公开项注释即契约:改公开项同步注释与测试同提交;what 进注释,why 进 ADR(缘由取舍不塞函数注释)
- 单一权威源:README、手册、--llms 面皆投影,可再生成不手改;漂移守卫进门禁(凡投影必带 --check 严格门禁进 CI);发现第二份真相即删或降指针
- 三语言面:Rust missing_docs deny、Python docstring(D 系)、TS JSDoc;公开 API 全覆盖
- 生成物进仓 clone 即得,但生成物手改即违规(改模板重生成)
