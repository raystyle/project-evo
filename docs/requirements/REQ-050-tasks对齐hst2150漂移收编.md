---
id: REQ-050
title: tasks skill 对齐 hst 2.15.0 漂移收编(D4/D7)
status: implemented
priority: must
trace: tests/test_project_evo.py
---

# REQ-050:tasks skill 对齐 hst 2.15.0 漂移收编

## Scenario

批159续单 hst_rs 台对齐回执(2026-10-15):tasks skill 三动词面对 hst 2.15.0 实态(装机位与 Cargo.toml 双证)核毕,漂移 9 键四面。分诊:D4(坑表反例引 hst goal show,该形 hst 2.15.0 已摘、反例失效)与 D7(坑表称 view 跳不可达机出单行告警,实装 tasks 域静默跳过,告警行在 agents 域)为 skill 事实漂移,本批修;D1-D3/D5/D6/D9 为代码面(远机插件 show action 仍 goal 形、apply 受体序、prim 死码、--agent 会话隔离、kv 首行取 text、set 也知会)转呈总台裁定,其 skill 措辞候代码裁定后随批对齐;D8(远机零 ssh 唤醒路径)相合,三注记(受体只消费最新一笔、pending 不消圈、pending 异步与知会竞态窗)随单转呈。

## Criteria

- [x] tasks SKILL 坑表 D4 修:反例改引擎裸命令泛形并注 goal 组 hst 2.15.0 已摘
- [x] tasks SKILL 坑表 D7 修:改「静默跳过不可达机不挂死(离线告警行在 agents 域)」
- [x] 漂移 9 键分诊回执:hst_rs ack、总台转呈(代码面六键加 D8 三注记)
- [x] evo 独立升 0.15.11;门禁全绿 + fleet 回执
