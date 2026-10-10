---
name: native-design
description: >-
  Agent 原生友好开发指导:把 agent 当第一用户设计 CLI 与工具面。--llms 紧凑手册面(至多 120 行
  附机器形)、旗标全家与类型化 CTA 输出协议、默认帮助面节序、活命令树三面同源自省(禁手维护)、
  裸调用面(不弹交互 exit 恒 0)、agent CLI 发现通道选型与 token 经济学、任务脚本 workspace、
  双面可拷实现模板(README 骨架、信封 schema、TS 与 Rust)。
  Use when 造或改 agent 友好 CLI、配 --llms 手册、定输出协议与帮助面、做命令自省与漂移守卫、
  定裸调用面或发现通道、为 agent 时代设计命令与工具面时;触发词 native-design、原生、agent
  友好、llms、手册面、CTA、信封、帮助面、自省、裸调用、发现通道、token 经济学、workspace。
---

# native-design - evo-doc Agent 原生友好开发

**渐进知识库型 skill**:本文件只做意图路由与速览,完整标准在 `references/` 三篇,按需定点读。

核心思想:**agent 是第一用户**。agent 读的不是宣传页,是输出流、退出码与手册面;命令面为 agent 设计 = 手册可发现(--llms 面)、输出可解析(类型化 CTA 协议)、自省可信(三面同源)、误用不炸(裸调用面恒 0)。

## 一、意图路由

> 表未覆盖的意图:用文件名或关键字直搜 references/,或查 `references/README.md` 索引。

| 意图 / 你要做的事 | 参考 |
| --- | --- |
| 给 CLI 配 --llms 手册面 | `references/agent-face.md` 第一节加 `references/templates.md` 第二节 |
| 定旗标全家与信封协议(类型化 CTA) | `references/agent-face.md` 第二节加 `references/templates.md` 第三与四节 |
| 定默认帮助面节序 | `references/agent-face.md` 第三节加 `references/templates.md` 第四节 |
| 做命令自省与漂移守卫 | `references/agent-face.md` 第四节加 `references/templates.md` 第五节 |
| 定裸调用面(不弹交互,exit 恒 0) | `references/agent-face.md` 第五节加 `references/templates.md` 第三节 |
| agent CLI 发现通道选型与 token 经济学 / 任务脚本 workspace | `references/tool-cli-agents.md` |

## 二、五件速览

- **--llms 手册面**:紧凑手册(至多 120 行)加机器形,agent 一读即会用;模板见 templates.md
- **类型化 CTA 协议**:旗标全家、输出信封 schema(退出码三态、结果与错误分型),可解析优于可读
- **默认帮助面**:节序固定,人读面与 --llms 面同源不双维护
- **活命令树自省**:帮助、手册、自省三面同一来源生成,漂移守卫进门禁
- **裸调用面**:无参调用不弹交互、exit 恒 0,输出给 agent 的下一步提示
