---
id: ADR-0023
title: 第五插件 evo-agent:agent-doctor 四端环境诊断修复,判据两级,增强 hst doctor 编排
status: accepted
date: 2026-10-12
deciders:
  - raystyle
supersedes: []
superseded_by: null
tags:
  - plugin-scope
  - skill-scope
  - agent-config
  - doctor
---

# ADR-0023:第五插件 evo-agent 与 agent-doctor 技能

## Context

用户令经三轮收敛(2026-10-12):先令增 config-lint 检查四端 agent 配置,再裁「不应该是 lint,就是独立技能」,再裁「单独一个插件 evo-agent」;扩面令:检查修复管理 hook,特别是 hst goal 与默认 goal、loop 的状态,再加 overcast API 网关诊断(候实装,现状配置端在 lan-mac 工作台)。当日五端插件清扫实证病灶族(claude enabledPlugins 悬空、明文 token、debug 构建路径、codex 卸载配置与缓存残留、grok plugins.enabled 残留已卸名),研究档 cfg-01 给出官方文档对照与判据分档依据。宿主已有 hst doctor(hook 形态诊断)、hst init(幂等修复)、hst goal(goal 自治面)、hst diagnose(网关活性),skill 不重造轮子。

## Decision

- **第五插件 evo-agent,单 skill agent-doctor**(客户端 evo-agent:agent-doctor),四参考面:config-face(配置诊断修复)、hooks-face(hook 诊断修复)、goal-loop(goal 与 loop 状态)、gateway-face(overcast 网关诊断,候实装框架);载体脚本 `skills/agent-doctor/scripts/config-lint.py`(PEP 723 零依赖,tomllib)
- **判据两级**:error = 客户端不可能成功或写错载体的硬伤(解析失败、枚举非法、绝对路径缺失、高置信秘密形态、grok 悬空引用、kimi 形态);advisory = 客户端容忍的治理面(claude 悬空引用是文档容忍态、用户面明文凭证、未知字段、codex 配置残留候选);不做闭合白名单门禁(官方 schema 落后索引 45 键且根上放行额外属性)
- **只报不改**:config-lint 出 findings 与退出码;修复走 hst init 幂等重部署与逐条手修(修复手册随判据表)
- **增强 hst doctor = 编排补面**:hst doctor 管运行时诊断,agent-doctor 补静态度判据、修复手册、goal 与 loop 面(loop 归 Claude Code 原生 CronCreate 与 ScheduleWakeup 域,hst loop 已退役 2026-10-11)与网关面;hst 只认 PATH 不改其源;config-lint 判据族稳定后可回流 hst doctor(候选)
- overcast 网关面候实装:诊断三层(配置对齐、连通性、活性)框架先立,端点与鉴权形态实装后回填定稿(沿 s5 候首版实测标注先例)

## Consequences

- 好:四端环境治理从「封版清扫靠人眼」变「一命令体检加修复手册」;悬空引用与明文凭据两类高价值病灶全覆盖;goal 与 loop 有唯一查看口径;网关面预留 overcast 实装位
- 坏:五插件版图与市场清单全同步面加一;字段白名单与枚举集随四客户端版本手动跟(缓解:advisory 级加豁免变量加研究档权威入口);网关面在 overcast 实装前是框架不是成品
- 版图:evo-doc 二、evo-herdr 三、evo-distil 一、evo-lint 二、evo-agent 一,共九 skill;版本线 0.8.0 同线入列(ADR-0021 族版本纪律)
