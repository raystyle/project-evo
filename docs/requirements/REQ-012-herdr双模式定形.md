---
id: REQ-012
title: herdr 双模式定形:herdr-dev 开发模式含 review 窗格,herdr-flywheel 跨仓模式
status: implemented
priority: must
trace: tests/test_project_evo.py
---

# REQ-012:herdr 双模式定形:herdr-dev 开发模式含 review 窗格,herdr-flywheel 跨仓模式

## Scenario

用户立单(2026-10-07):herdr 收敛两个 skill:开发模式(已包含 review 窗格)与跨仓模式(不同仓库 agent 工作台对话交流);herdr-review 并入开发模式。

## Criteria

- [x] herdr-review 目录改名 herdr-dev 并重写 SKILL(布局定式、评审闸门、自省验收、lane 分发四主线;意图路由五参考篇)
- [x] references/lane-dispatch.md 移入 herdr-dev;references 索引更新;flywheel 去布局与 lane 两节
- [x] herdr-flywheel 收敛跨仓模式(description、标题句、参考节指针到 herdr-dev)
- [x] 双 manifest 与市场条目描述同笔双模式化(codex 面 interface 同步),版本线不动
- [x] 守卫 SKILLS、pre-commit 断链段、AGENTS 定位与阶段行、根 README、docs 地图刷齐
- [x] ADR-0019 与两索引、CHANGELOG 第九十一批、ROADMAP;pytest 全绿加 md-ref-scan 零断链
