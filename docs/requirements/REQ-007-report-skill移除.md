---
id: REQ-007
title: report skill 移除,evo-research 收敛为单 skill
status: implemented
priority: must
trace: tests/test_project_evo.py
---

# REQ-007:report skill 移除,evo-research 收敛为单 skill

## Scenario

用户立单(2026-09-23):移除 evo-research 的 `report` 研究成文 skill,四插件十一 skill 收敛为十 skill;成文路由归 doc-gov 投影纪律。

## Criteria

- [x] `plugins/evo-research/skills/report/` 全目录移除
- [x] 守卫测试 SKILLS 清单去 report、report 断言段删除;docsring 计数十一改十
- [x] 双 manifest 与市场条目描述去 report 化(codex 面 interface 同步),版本线不动
- [x] pre-commit 断链扫描段去 report;gates 计数十一改十
- [x] research 与 doc-gov 互引路由改指投影纪律,不留死链
- [x] ADR-0015 与索引、根 README 意图表与 docs 地图、evo-research README 单 skill 化、AGENTS 合同计数
- [x] pytest 全绿加 md-ref-scan 十 skill 零断链
