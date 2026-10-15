---
id: REQ-049
title: 英文面自查与 hst 2.15.0 台对齐(批159续)
status: implemented
priority: must
trace: tests/test_project_evo.py
---

# REQ-049:英文面自查与 hst 2.15.0 台对齐

## Scenario

总台续单(2026-10-15 批159 续):0.15.9 英文面(use: 前缀、取用行英文)自查六 SKILL 对 prim v3.2.6 --llms 零漂移;hst_rs 台(wG:p1)复活后派单对齐 tasks skill 与 hst 2.15.0 命令面;重启正名纪律(重启后第一动作 = agents view 查无名格)进 evo 台 memory。自查实态:六面动词表与五域 --llms 逐面对过零漂移,但信封取用行文档面三处旧中文形残留(`取用:` 前缀、`<回复>` 位形、「(流已附)」注)、agents reload 行缺 done 态(2026-10-15 修:idle/done 皆可翻)、streams 文法行「管道道」叠字,本批修正并升 evo 0.15.10。

## Criteria

- [x] 六 SKILL 动词面 + references 对 prim v3.2.6 --llms 逐面核对,漂移四项修正:deliver-gate 模板行 `use:` 前缀与第三行注、取用行 reply 字面量形(agents/shares/streams/addressing/collab 五处)、streams `(stream <流> attached)` 注形、reload 行补 idle/done 皆可翻
- [x] streams SKILL 文法行「stdin 管道道」叠字修
- [x] hst_rs 派单:hst 2.15.0 命令面与 tasks skill 三动词对照,漂移清单随 fleet 回执(单已投,hst_rs ack 在案;回执未归前本单状态 implemented 以代码面为准,台面对齐结果随后续回执闭环)
- [x] 重启正名纪律进 evo 台 memory(重启后第一动作 = agents view 查无名格及时正名)
- [x] evo 独立升 0.15.10;门禁全绿 + fleet 回执
