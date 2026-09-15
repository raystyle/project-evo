---
id: ADR-0003
title: office-pro skill 移除,收敛为三 skill
status: accepted
date: 2026-09-15
deciders:
  - raystyle
supersedes: []
superseded_by: null
tags:
  - skill-scope
---

# ADR-0003:office-pro skill 移除,收敛为三 skill

## Context

office-pro(OfficeCLI 专业面)使用频率低,与 skill 市场定位(项目进化工具链)偏离;四 skill 同装里它是唯一非核心工作流面。S007 研究档案保留完整沿革。

## Decision

移除 office-pro 全目录与 office-cli 斜杠命令,插件收敛为 dev-evo(时为 docs-evo)、super-research、secret-scan 三 skill;清单面同步三 skill 并升版。

## Consequences

- 好:插件面聚焦;清单与测试守卫简化;维护面缩小。
- 坏:依赖 officecli 的用户失去 skill 面(OfficeCLI 本体与 S007 档案仍在,可按档案自行使用) [实证: CHANGELOG 第四十九批]
