---
id: REQ-052
title: tasks 三键措辞随批 163 落 skill(D5/D6/D9)
status: implemented
priority: must
trace: tests/test_project_evo.py
---

# REQ-052:tasks 三键措辞随批 163 落 skill

## Scenario

总台收正回执(2026-10-15,ai-ccoe 7b233ee):evo 批162 审出两失属实：domains.py 六键修曾因多文件脚本中段断言死而全未落盘(总台误宣全修,教训入档:commit 前逐文件核 diff),本笔真落:D3 goal 死码清 / D5 set-show 带 --agent 会话隔离 / D6 view 直读 task.text 行 / D9 set 只写不扰(emit_ok 即返,知会归 to);pyproject 3.3.0 真滚。本台拉 7b233ee 逐行核过四键并源装实弹:view 出 task.text 行加「(无 task)」降级、set 打本格即返无投递、--agent 键面读写清一条龙。批163:D5/D6/D9 措辞落 tasks skill;D6 的 view 行原本措辞(「本机各仓任务直读」)在修复后即为真,不改。

## Criteria

- [x] ai-ccoe 7b233ee 拉取逐行核 + 本机源装 prim v3.3.0,四键实弹(view/set/--agent 读写清)
- [x] tasks SKILL:set 动词行补「只写不扰,知会走 to」(D9);文法补任务键按格 agent 隔离行(D5);坑表补「想知会却用 set」行(D9)
- [x] evo 独立升 0.15.13;门禁全绿 + fleet 回执
