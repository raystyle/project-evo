---
name: dev-doc
description: >-
  项目文档治理知识库:ADR 架构决策与 REQ 需求登记状态机、代码 doc 注释契约、文档即代码投影
  守卫、研究档案、项目工具链;md 静检(禁字断链)、约束术语表 term-lint(非标准中文与英文
  黑话)、四类型结构模板卡与声明式规则件、门禁三态退出码与 pre-commit 挡板。
  Use when: ADR, REQ, lint, 立架构决策或需求、写代码 doc 注释与文档即代码、配静态检查门禁
  或术语表 lint、新仓脚手架或结构 lint 时;触发词 doc-gov、dev-lint、ADR、REQ、决策、
  需求登记、trace、doc 注释、文档即代码、研究档案、工具链、lint、禁字、断链、术语表、
  term-lint、md-guard、pre-commit、脚手架、门禁。
  不要用于运行时行为验证、与文档治理无关的代码实现或一次性脚本。
---

规则面已转 hook_rules(意图注入与路径注入);注入未发生时(非 Claude 端或 hook 缺位)直读 `plugins/dev/hook_rules/` 下同名与拆件。
