---
id: ADR-0015
title: report skill 移除,evo-research 收敛为单 skill
status: accepted
date: 2026-09-23
deciders:
  - raystyle
supersedes: []
superseded_by: null
tags:
  - skill-scope
---

# ADR-0015:report skill 移除,evo-research 收敛为单 skill

## Context

用户立单(2026-09-23):移除 `report` 研究成文 skill。成文面与 doc-gov 投影纪律重合(正式成文按投影纪律出 md 即可),三件套渲染面带外部依赖(typst 加 cmarker)使用频率低;四插件十一 skill 收敛为十 skill,市场面更聚焦。

## Decision

移除 `plugins/evo-research/skills/report/` 全目录;evo-research 收敛为单 skill `research`;清单、双 manifest、市场条目、守卫测试、各 skill 互引路由同步去 report 化;research 与 doc-gov 的成文路由改指投影纪律;manifest 版本线不动(四插件同版本线 0.4.0 不变,批次级变更不升版)。

## Consequences

- 好:插件面聚焦;render.py 与 Typst 依赖面整体退出;守卫与断链扫描面缩小一档。
- 坏:依赖 report 三件套的用户失去该面(git 历史与 ~/.kimi 备份仍在,可按历史版本自行恢复);需要正式成文的按 doc-gov 投影纪律出 md 自理。
