---
id: ADR-0019
title: herdr 双模式定形:开发模式 herdr-dev 含 review 窗格,跨仓模式 herdr-flywheel
status: accepted
date: 2026-10-07
deciders:
  - raystyle
supersedes: []
superseded_by: null
tags:
  - skill-scope
---

# ADR-0019:herdr 双模式定形:开发模式 herdr-dev 含 review 窗格,跨仓模式 herdr-flywheel

## Context

用户立单(2026-10-07):herdr 应是两个 skill:开发模式(已包含 review 窗格:通用四窗格布局定式、评审闸门、自省验收、任务分发 lane)与跨仓模式(不同仓库 agent 工作台的对话交流:四步协议、跨机器、义务图)。前两批已把布局定式与 lane 内容落进 herdr-flywheel,评审闸门独立为 herdr-review,与双模式定位不合。

## Decision

evo-herdr 收敛为双 skill:`herdr-dev` = 开发模式(窗格布局定式节、评审闸门与自省验收双闸门、任务分发 lane 模型,references 收 request、receipt、findings、panes、lane-dispatch 五篇),由 herdr-review 整目录改名重组并吸收 flywheel 中的布局与 lane 两节;`herdr-flywheel` = 跨仓模式(工位形态与多 kind 带起、跨机器工位、四步协议、并行义务图、命令面与坑),不再载开发面内容。manifest 版本线不动(两插件同版本线 0.4.3 不变,统一打版随后批)。

## Consequences

- 好:双模式边界清晰(开发 = 一个工位的布局与闸门,跨仓 = 多仓工作台对话交流);触发词分流,检索面各归各;评审知识不再横跨两 skill。
- 坏:herdr-review 触发词失效,依赖旧名的消费者按 herdr-dev 重学(git 历史可恢复);flywheel 与 dev 经指针互引,跨 skill 跳转多一跳。
