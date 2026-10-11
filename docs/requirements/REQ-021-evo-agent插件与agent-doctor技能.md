---
id: REQ-021
title: 第五插件 evo-agent:agent-doctor 四端环境诊断修复
status: implemented
priority: must
trace: tests/test_project_evo.py
---

# REQ-021:第五插件 evo-agent 与 agent-doctor 技能

## Scenario

用户令经三轮收敛(2026-10-12):增 config-lint 检查 claude 与 codex 配置,扩四端(claude、codex、grok、kimi),裁独立技能且单列第五插件 evo-agent,技能名 agent-doctor;专注配置诊断修复、hook 诊断修复,特别是 hst goal 与默认 goal、loop 的状态;再加 overcast API 网关诊断(候实装,现状配置端在 lan-mac 工作台)。研究格两轮支撑:cfg-01 官方文档对照与判据分档,cfg-02 网关先例与定时域权威(并行吸收)。裁定判据两级、只报不改、增强 hst doctor 编排补面(ADR-0023)。

## Criteria

- [x] ADR-0023 与 REQ-021 立档(第五插件单 skill、判据两级 error 与 advisory、只报不改、增强 hst doctor 编排、overcast 候实装框架)
- [x] `plugins/evo-agent/skills/agent-doctor/scripts/config-lint.py`:四端面(claude settings 两件、codex config.toml、grok config.toml、kimi config.toml 加 skills 面),PEP 723 零依赖,退出码 0/1,`--json` 机读,`--kimi-source` 漂移对账,网关键组配对检查
- [x] error 判据族:解析失败、枚举非法(doctor 实测枚举集)、绝对路径缺失(kimi 双 OS 形只查当前 OS)、高置信秘密形态、grok 悬空引用、kimi 形态与漂移、项目面明文凭据;advisory:claude 悬空引用(文档容忍态)、用户面明文凭据、未知字段、codex 配置残留候选、网关键组不齐
- [x] 四参考面:config-face(判据表加修复手册加权威入口)、hooks-face(hst doctor 诊断、hst init 修复、trusted_hash、kimi 双 OS 形)、goal-loop(hst goal 四命令与缺省态;loop 归 Claude Code 原生域)、gateway-face(overcast 三层框架候实装)
- [x] 版图全同步:双 manifest、双市场清单、插件 README、AGENTS、根 README(五插件九 skill)、docs 地图、ADR/REQ 索引、pre-commit(九 skill 断链段)、CI
- [x] 测试:config-lint 行为测试(四端坏配置夹具逐面报、好配置零错零警、豁免变量生效、网关配对)加清单一致性守卫不回归;四门禁全绿加提交挡板过推远端
