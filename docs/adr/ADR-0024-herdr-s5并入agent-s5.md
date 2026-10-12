---
id: ADR-0024
title: herdr:s5 删除并入 agent-s5,s5 归一为全 agent 共享看板与实时流
status: accepted
date: 2026-10-12
deciders:
  - raystyle
supersedes: []
superseded_by: null
tags:
  - skill-scope
  - s5
---

# ADR-0024:herdr:s5 并入 agent-s5

## Context

批 111 立 evo-herdr:s5(跨机共享内容协议技能,用户令 evo-04),批 117 立 evo-agent:agent-s5(全 agent 看板与频道操作面,总台插队令)。两 skill 同教 s5 CLI,触发词撞车、清单不自解释。用户两轮裁定(2026-10-12):先触发词分治,终裁「还是删除合并成一个,就是 agent-s5,s5 就是所有 agent 可以共享的看板和实时流,不要太复杂」。

## Decision

- **归一**:删 evo-herdr:s5(调用名失效),evo-agent:agent-s5 为 s5 唯一技能面;定位 = 所有 agent 共享的看板与实时流,从简三节(命令面活权威 s5 --llms、命名约定、读写礼仪)
- **语义不损并入**:原 herdr:s5 的跨机键空间规范(rounds 三件套文件名形与三方同步律、research 与 artifacts、streams 分 diary 与 events)、协同律、双道选型三问与 backend 形、evals 五条、候 s5 首版实测定稿标态,随迁 agent-s5(批 125 保真修复)
- **分工保持**:herdr 管信号与消息(派单、回执、状态),共享内容一律走 agent-s5;同机轮次走本地共享目录不上 s5
- evo-herdr 收两 skill(orch、flywheel);版图五插件九 skill

## Consequences

- 好:s5 技能面唯一,触发无撞车,清单自解释;跨机轮次协议语义保留在 agent-s5 一处
- 坏:herdr 插件域描述收窄;若未来轮次协议再长重,可能需要 references 分篇扩(届时按蒸馏环走)
- 部署:已装端缓存随下次封版滚动(版本线不变不刷新,既议)
