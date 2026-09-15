---
id: ADR-0001
title: 单插件多 skill 市场形态,不四插件各一 skill
status: accepted
date: 2026-09-10
deciders:
  - raystyle
supersedes: []
superseded_by: null
tags:
  - marketplace
  - plugin
---

# ADR-0001:单插件多 skill 市场形态,不四插件各一 skill

## Context

v0.2.x 时代四个 skill 各自成插件(project-evo、super-research、secret-scan、office-pro),市场显示 Skill(office-pro:office-pro) 双名重叠,且一个前缀挂一个 skill 让市场清单膨胀四份,双 manifest 同步成本随插件数翻倍。

## Decision

市场应是一个前缀下挂不同 skill 名:四插件收敛为唯一插件 project-evo,skill 目录并进 skills/,客户端显示 project-evo:dev-evo(时为 docs-evo)、project-evo:super-research、project-evo:secret-scan。市场清单与 manifest 单条化,同装同版。

## Consequences

- 好:市场一条安装得全部 skill;版本与清单同步面从八份降到两份;客户端显示语义正确。
- 坏:单 skill 变更牵动整插件版本前进;skill 间耦合在同一发布节奏里。
- 后续沿革:v0.4.0 移除 office-pro 收敛为三 skill(ADR-0003);v0.5.0 docs-evo 改名 dev-evo 并转文档即代码体系 [实证: CHANGELOG 第四十七、四十九、五十批]
