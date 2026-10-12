---
id: REQ-023
title: herdr:s5 删除并入 agent-s5,s5 归一为全 agent 共享看板与实时流
status: implemented
priority: must
trace: tests/test_project_evo.py
---

# REQ-023:herdr:s5 并入 agent-s5

## Scenario

用户令(2026-10-12,两轮):先令 herdr:s5 触发词去重叠(批 123),再裁「还是删除合并成一个,就是 agent-s5,s5 就是所有 agent 可以共享的看板和实时流,不要太复杂」。s5 技能面归一:evo-agent:agent-s5 为唯一载体,herdr:s5(批 111 立,用户令 evo-04)删除;调用名 evo-herdr:s5 失效。

## Criteria

- [x] plugins/evo-herdr/skills/s5 整目录删除,evo-herdr 收两 skill(orch、flywheel);flywheel 与 orch 对 s5 零交叉引用,净删无断链
- [x] agent-s5 吸收:定位改「所有 agent 共享的看板与实时流」,触发词收编(上云、三件套上云、轮次档、跨机研究档、对象道、流道、轨迹流、S3、S2、garage、streamstore),分工句简化(herdr 管信号与消息,共享内容一律走本 skill)
- [x] naming.md 增跨机轮次与研究档键空间节(rounds、research、streams;三件套整份 put),判例簿记合并
- [x] 版图五插件九 skill 全同步(AGENTS、根 README、双市场清单、evo-herdr 双 manifest 与 README、docs 地图、pre-commit、测试清单)
- [x] 四门禁全绿;kimi 五端镜像同步(旧 s5 目录退场)
