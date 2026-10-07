---
id: REQ-013
title: herdr-flywheel 跨机器 machine 原语语义补强
status: implemented
priority: must
trace: tests/test_project_evo.py
---

# REQ-013:herdr-flywheel 跨机器 machine 原语语义补强

## Scenario

用户立单(2026-10-07):跨仓之外再研究跨机器,herdr 现有 machine 原语;按活权威 `herdr --skill`(本机 0.9.1)直读补强 flywheel 跨机器工位节。

## Criteria

- [x] 跨机器工位节按活权威补强:ID 与名 scoped 单机、TUI 选机不重定命令向、selector 语义与 --remote 互斥、转发前提与边界(双侧 API 转发、不装不起不重启、不转发面、远端路径约束)、连接失败不证未应用、machine list 是 profile 清册、add 默认远端默认会话
- [x] 六态标注([实证: herdr 0.9.1 --skill 直读]);既有实证条目原样保留
- [x] CHANGELOG 第九十二批、AGENTS 阶段行;pytest 全绿加 md-ref-scan 零断链
