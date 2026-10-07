---
id: REQ-015
title: herdr 集成 py 脚本重评估:总台运维面翻转建 fleet-exec,lane 与插件面维持零脚本
status: implemented
priority: must
trace: tests/test_project_evo.py
---

# REQ-015:herdr 集成 py 脚本重评估:总台运维面翻转建 fleet-exec,lane 与插件面维持零脚本

## Scenario

用户立单(2026-10-08):重评估 ROADMAP 待定行「herdr 集成 py 脚本重评估」(批 90 裁定暂不开发,触发条件 = 探针或扫描循环手拼二犯、state 台账单行不可读)。

## Criteria

- [x] 触发审计:S011 原写触发(lane 探针/扫描循环)未 fired(lane 无实跑);但 v0.11.0 舰队清理与安装轮中「send-text 加 enter 加 wait-output 收标加 read 回执」普通进程通道手拼十余次、四种任务形(探针、清缓存、装插件、扫尾),仓级沉淀铁律(手拼两次即升格)在总台运维面成立
- [x] 评估结论(部分翻转):建本仓 `.tools/fleet-exec.py` 运维薄封装(逐条回显 herdr 命令,活权威语义不藏);herdr 插件面维持纯知识(ADR-0018 不动);lane 探针/扫描触发条件保留(lane 实跑二犯再议)
- [x] 实证准入:对 pi-server shell 格端到端实跑(四步回显、收标命中、回执含 hostname,exit 0)
- [x] 测试:test_fleet_exec_tool(--help 可跑、--machine 前缀组装断言);.tools/README 登记
- [x] ROADMAP 待定行翻转为已完成;CHANGELOG 第九十六批;pytest 全绿
