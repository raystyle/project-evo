---
name: research
description: >-
  检索域知识面:按研究目标路由通道,gh 搜 GitHub(API 面)、browse 搜 Bing(网页主通道,
  无头即通)与 scholar.google.com 学术面(fetch 直通)、rn 编排与油猴探针过重采集面。
  Use when: 调研某主题、找库选型、学术检索、跨源对照搜索、GitHub 找仓找码找 issue、
  要引擎采集或写采集编排时;触发词 research、检索、调研、搜索、找库、选型、学术、
  scholar、文献、找仓。
  不要用于检索结论的档案沉淀(走 dev:dev-doc 研究档案面)与 agent 消息操作(走 evo 原语域)。
---

规则面已转 hook_rules(意图注入与路径注入);注入未发生时(非 Claude 端或 hook 缺位)直读 `plugins/evo/hook_rules/` 下同名与拆件。
