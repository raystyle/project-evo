---
name: dev-cli
description: >-
  Agent 原生友好开发指导:把 agent 当第一用户设计 CLI 与工具面。--llms 紧凑手册面(至多
  120 行)、旗标全家与类型化 CTA 输出协议、默认帮助面节序、活命令树三面同源自省(禁手
  维护)、裸调用面(不弹交互 exit 恒 0)、Rust CLI 舰队公约分级、发现通道选型与 token 经济学、
  双面可拷实现模板。
  Use when: design agent-friendly CLI, llms manual, 造或改 agent 友好 CLI、配 --llms 手册、
  定输出协议与帮助面、做命令自省与漂移守卫、定裸调用面或发现通道或舰队公约时;触发词
  dev-cli、原生、agent 友好、llms、手册面、CTA、信封、帮助面、自省、裸调用、公约、
  发现通道、token 经济学、workspace。
  不要用于图形界面或非 CLI 产品的交互设计。
---

规则面已转 hook_rules(意图注入与路径注入);注入未发生时(非 Claude 端或 hook 缺位)直读 `plugins/dev/hook_rules/` 下同名与拆件。
