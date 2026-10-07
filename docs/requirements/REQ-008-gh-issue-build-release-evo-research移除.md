---
id: REQ-008
title: gh-issue 与 build-release 与 evo-research 移除,四插件收敛三插件七 skill
status: implemented
priority: must
trace: tests/test_project_evo.py
---

# REQ-008:gh-issue 与 build-release 与 evo-research 移除,四插件收敛三插件七 skill

## Scenario

用户立单(2026-10-07):移除 evo-adr 的 `gh-issue` 与 `build-release` 两 skill,下线 evo-research 整插件,四插件十 skill 收敛为三插件七 skill;版本线 0.4.3 不动,统一打版留待整理重构批。

## Criteria

- [x] `plugins/evo-adr/skills/gh-issue/` 与 `plugins/evo-adr/skills/build-release/` 全目录移除;`plugins/evo-research/` 整插件移除
- [x] 守卫测试 PLUGIN_NAMES 与 SKILLS 清单同步,docstring 与断言消息改三插件七 skill
- [x] 双市场清单与 evo-adr 双 manifest 描述同笔去化(codex 面 interface 同步),版本线不动
- [x] pre-commit 断链段去三目标;CI smoke 删悬空 report 行(修复既有断链)
- [x] 幸存 skill 互引路由(doc-gov、cli-docs、code-kit references)不留死链
- [x] ADR-0016 与两索引、CHANGELOG 第八十七批、ROADMAP、根 README 与 AGENTS 计数刷齐(顺手修两处既有计数漂移)
- [x] pytest 全绿加 md-ref-scan 七 skill 零断链
