---
id: ADR-0009
title: herdr 飞轮 skill 增编与 flow-flywheel.md 退役
status: accepted
date: 2026-09-16
deciders:
  - raystyle
supersedes: [ADR-0008]
superseded_by: null
tags:
  - governance
  - terminal-state
---

# ADR-0009:herdr 飞轮 skill 增编与 flow-flywheel 退役

## Context

ADR-0007 定形单插件四 skill 终态与参考边界,ADR-0008 首例修订边界新增 flow-flywheel.md(17 至 18 篇)。总台派单(2026-09-16)要求新建稳定 herdr 飞轮 SKILL 并各仓治理实践;补令裁定二择一为「老的清除」:协议全量吸收进新 skill 后该参考退役,不留双份并行维护。

## Decision

- 插件由四 skill 扩为五:新增 `herdr-flywheel`(多仓 herdr 工位飞轮协作治理:派单、回执、断言、吸收四步协议加命令面要点加治理操作坑);ADR-0007 四 skill 形态条款据此扩展,五件套与其余条款不变
- `flow-flywheel.md` 全量并入新 skill 后从 dev-evo references 删除,references 由 18 篇回落至 17 篇(数量同 ADR-0007 边界,构成异);dev-evo SKILL 路由、references 三层索引、env-platform 第十节交叉引用改指新 skill
- ADR-0008 整体 supersede:其 env-platform 第十节条款不受影响,由该篇自身继续承载

## Consequences

- 好:多仓协作治理有独立激活面,市场消费者按需取用;协议单一真相在 skill,双份并行风险消除;新坑可独立沉淀(pitfalls.md)
- 坏:形态面变更成本一次结清(双 marketplace、双 manifest、AGENTS 合同、守卫测试、文档地图同步);dev-evo 单仓使用者取跨仓协议须跨 skill [假设]
