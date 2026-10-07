---
id: ADR-0016
title: gh-issue 与 build-release 与 evo-research 移除,四插件收敛三插件七 skill
status: accepted
date: 2026-10-07
deciders:
  - raystyle
supersedes: []
superseded_by: null
tags:
  - skill-scope
---

# ADR-0016:gh-issue 与 build-release 与 evo-research 移除,四插件收敛三插件七 skill

## Context

用户立单(2026-10-07):移除 evo-adr 的 `gh-issue` 与 `build-release` 两 skill,并下线 evo-research 整插件(唯一 skill `research`)。市场收敛为三插件七 skill(evo-adr: doc-gov、code-kit、cli-docs;evo-codesec: secret-scan、security-audit;evo-herdr: herdr-flywheel、herdr-review),治理面更聚焦;用户同期预告后续有整理重构批,统一打版随后走。

## Decision

移除 `plugins/evo-adr/skills/gh-issue/` 与 `plugins/evo-adr/skills/build-release/` 全目录,`plugins/evo-research/` 整插件下线(双市场清单条目删除);清单、双 manifest、守卫测试、幸存 skill 互引路由、pre-commit 断链段、CI smoke 同步去三目标化(顺手修复 test.yml 悬空 report 引用与两处计数漂移);manifest 版本线不动(三插件同版本线 0.4.3 不变,统一打版留待整理重构批)。

## Consequences

- 好:插件面聚焦三插件七 skill;gh-issue 的 gh 写权限面与 research 的 browse/aria2c 外部依赖面退出;CI smoke 既有断链一并修复。
- 坏:依赖三目标的用户失去该面(evo-research 为破坏性变更,已装者须卸载;git 历史与 ~/.kimi 备份仍在,可按历史版本自行恢复);资料检索与错报上报需求走通用通道自理。
