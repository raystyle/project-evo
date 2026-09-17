---
id: ADR-0014
title: cli-docs 对外面双标准 skill 增编,evo-adr 四 skill 四扩五
status: accepted
date: 2026-09-17
deciders:
  - raystyle
supersedes: []
superseded_by: null
tags:
  - governance
  - readme
  - agent-face
---

# ADR-0014:cli-docs 对外面双标准 skill 增编,evo-adr 四 skill 四扩五

## Context

总台立单(2026-09-17):CLI 项目需要两面仓无关标准:甲面 README 标准(研究 ripgrep、fzf、bat、fd 四业界标杆提炼,人类阅读优先,四节骨架为起点按研究定稿);乙面 agent 友好三件起步,经三号补单定为四件(--llms 手册面、旗标全家与类型化 CTA 协议、默认帮助面、自省三面同源、裸调用面)。归口裁定:新立 skill(照 build-release 形),与 doc-gov(文档体系治理,管仓内文档骨架)和 code-kit 的 tool-cli-agents(发现通道与 token 经济学设计面)分工互引不重述;私有名零出现,实现出处(hst 输出契约、omc 信封、四标杆 README)只留仓内 diary。

## Decision

- evo-adr 增编第五 skill `cli-docs`(CLI 对外面双标准:甲面 readme-standard 四节骨架定稿与写法纪律反面清单,乙面 agent-face 四件:--llms 紧凑手册至多 120 行加机器形与活命令树渲染禁手维护、必选旗标七件加可选扩展件显式裁剪与信封类型化 CTA、默认帮助面节序与同源、自省三面同源与漂移守卫;mcp 与 http api 裁为可选附录);references 含可拷改模板五节,双语言模板各带帮助输出示例;修订 ADR-0010 的十 skill 清单条款为十一 skill,四插件形态与分域不变
- 分工边界:README 人类优先与手册 agent 优先互指不互抄;发现通道选型留 tool-cli-agents,本 skill 管四件实现标准
- 总台追正纪律照 build-release 先例:轻量追正一笔,CI 绿即收

## Consequences

- 好:CLI 对外面从逐仓手感变成双标准配方,新仓与存量改造都有可拷骨架;agent 四件与 README 面互指形成完整对外面闭环
- 坏:evo-adr 五 skill 后清单面与守卫同步成本续增;README 标杆研究有时效性,四标杆形变时标准需复研
- 无破坏性:新增能力,既有安装不受影响;版本线随四插件同版前进
