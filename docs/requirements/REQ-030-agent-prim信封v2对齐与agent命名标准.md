---
id: REQ-030
title: agent-prim 信封 v2 对齐与 agent 命名标准(工作台-类型-编号)
status: implemented
priority: must
trace: tests/test_project_evo.py
---

# REQ-030:agent-prim 信封 v2 对齐与 agent 命名标准

## Scenario

总台 skill 对齐令(2026-10-13,与 R1 批合轮;ai-ccoe main fb701a7+41ca290):1) 信封字段行新标准 from=host:pane to=<id> 域字段 v=1(人话行 @收方;pydantic 真源 prim/src/prim/msg.py);2) CTA 专业标准(『下一步:』前缀,俚语清零);3) 触发词自然语化(fleet seq 44:告诉/委派/让干/找格/读屏/窗格/邻居/tab/工作台/流/共享/管道/持久任务等意图词路由五原语);另门控尾窗修(只扫 TUI 尾 12 行,正文文档引用不误判)。用户同令两条:各 agent 名字定标准不乱取,标准形 = 工作台-agent类型-编号(工作台 = 仓别名,台以仓为单位);按此方案同步总台。

## Criteria

- [x] 信封 v2 收编:deliver-gate.md 信封节重写(from/to 恒在、v 恒带、人话行 @收方、pydantic 真源与 parse_fieldline 机读、旧形 src= 收旧拒);addressing.md src 核验改 from 核验加 host-only 判例;SKILL 与 commands 随改(开吃等俚语清零);差异表幂等行拆(v=1 已落,幂等 id 与 tasks prev 未落)
- [x] 门控尾窗与 CTA:门控判据补尾 12 行(正文文档引用不误判,evo 实弹案);commands 通则补 CTA 专业标准(『下一步:』前缀与 target= 键值形)
- [x] 触发词自然语化:SKILL description 按 fleet seq 44 全单重写(意图词路由五原语,table 即 tab,管道即 pipes)
- [x] 命名标准(用户裁定):addressing.md 命名纪律升命名标准,标准形 = 工作台标签-agent类型-编号(台标签 = 仓别名,agents ws 以仓为单位;类型 = TUI 家族;编号同台同类从 1 起),结构性全局唯一,存量名兼容新起一律标准形;AI-LAB 取用行断点与机标签不合入判例与报件
- [x] 实证:本机重装 prim(fb701a7 后)本地渲染信封 v2 与 parse_fieldline 双向过;`agents to AI-LAB` not_found 实测(取用行断点入档)
- [x] 版本线 0.12.0 进 0.12.1;四门禁全绿 + 回执走 streams append fleet + 回信总台(取用行信道,经 lan-win:w13:p1)
