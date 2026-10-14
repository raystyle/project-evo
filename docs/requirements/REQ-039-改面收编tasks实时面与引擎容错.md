---
id: REQ-039
title: 改面收编:tasks 实时任务面与 herdr_run 容错
status: implemented
priority: must
trace: tests/test_project_evo.py
---

# REQ-039:改面收编（tasks 实时任务面与引擎容错）

## Scenario

总台改面通知(2026-10-14,prim 369e57b):tasks view 改实时任务面 = fleet 各格状态总览(标记在跑)加各格仓内 hst task show 直读,弃 tasks/shared 历史事件流;herdr_run 容错 = 超时/离线机回 rc=124 不抛栈,view 跳过不可达机单行告警。令 = 下批顺手收编勿专批。

## Criteria

- [x] tasks SKILL:description 与动词面与语义节随改(实时任务面、事件流弃用注记);坑表加离线机容错行
- [x] agents SKILL 坑表加目标机离线行;addressing.md 坑簿离线行随改(不挂死,单行告警跳过)
- [x] commands.md 五域速查与差异表随改(tasks view 行转实时面;tasks 事件 prev 随事件流弃用销账);streams 与 collab 保留策略去 tasks/shared 面(旧档只读)
- [x] 实证:本机重装 prim 369e57b 后 tasks view 实测(实时总览带在跑标记);包源直读 rc=124 容错;evo 0.14.4;四门禁全绿 + fleet 回执
