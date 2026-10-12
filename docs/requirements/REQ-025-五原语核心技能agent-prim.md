---
id: REQ-025
title: evo-agent 第四技能 agent-prim:舰队互操作五原语操作面
status: implemented
priority: must
trace: tests/test_project_evo.py
---

# REQ-025:agent-prim 五原语核心技能

## Scenario

总台派单(2026-10-12,prim-skill-01):舰队互操作协议已定型落地,五命令 agents/shares/streams/tasks/pipes 三段式(VIEW/OPERATE/DELIVER)、裸名全局寻址、投递门控加拒投代记、取用行模板、ack/force 审计流、streams 回放。契约单一真源 = ai-ccoe 仓 plugins/CONTRACT.md(研究补句已并,v2.3)。本仓铸核心 skill:面向 agent 第一读者,读了就会用;不复述契约全文只路由。裁定挂 evo-agent 第四 skill(客户端 evo-agent:agent-prim):agent 协作能力域;与 agent-s5 分工 = s5 是引擎命令面,五原语是骑在其上的协议面。

## Criteria

- [x] SKILL.md 意图路由:五域路由(消息/文件/流/目标/管道何时用哪条)、三段式文法速览、目标文法速览、DELIVER 门控速览、协作惯例速览、契约真源与版本对齐行(对齐 v2.3,本机实装 v2.0.0 差异六态标注)
- [x] references/ 四篇加索引:commands.md(五命令逐条文法与示例、输出契约、错误码表、本机实装差异表)、addressing.md(裸名全局寻址算法、机:名、命名纪律、回信地址与 src 核验)、deliver-gate.md(门控判据、force 审计、代记补收、幂等 id 与 v 字段、信封三行形)、collab.md(IM 映射、回执惯例、cursor 回放、保留期、与 herdr 及 agent-s5 及 agent-rloop 分工)
- [x] 版本随 ai-ccoe 契约版对齐标注(契约 v2.3;演进纪律 = 契约升版本 skill 随批对齐)
- [x] 版图全同步:测试 SKILLS 守卫、pre-commit 断链清单、AGENTS、根 README、docs 地图、插件 README、REQ 索引(五插件十一 skill)
- [x] 四门禁全绿 + 回执走 streams append fleet(自吃狗粮)
