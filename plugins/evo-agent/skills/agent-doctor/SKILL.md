---
name: agent-doctor
description: >-
  agent 客户端环境诊断与修复:四端(claude、codex、grok、kimi)配置诊断修复、hook 诊断修复、goal
  与 loop 状态三面。配置面 config-lint 脚本(悬空引用、明文凭据、路径缺失、枚举非法、卸载配置残留、
  kimi skills 形态与漂移对账;判据两级 error 与 advisory;只报不改);hook 面(hst doctor 的
  hooks.form 与 trust.hooks 诊断、hst init 幂等修复、codex trusted_hash 时效、kimi 双 OS 形);
  goal 面(hst goal 项目级 set/show/clear/heal 与缺省态)与 loop 面(Claude Code 原生 CronCreate
  与 ScheduleWakeup 与 durable 件);网关诊断面(overcast API 网关候实装:配置对齐、连通性、
  hst diagnose 活性)。定位 = 增强 hst doctor:编排补面,hst 只认 PATH 不改其源。
  Use when 四端 agent 配置例行体检或出错排查、装卸插件后清配置残留、修 hook 与 trusted_hash、
  查 statusline 路径悬空、设看清项目 goal、查 loop 定时任务状态、配诊断 API 网关时;触发词
  agent-doctor、配置诊断、config-lint、修 hook、trusted_hash、悬空引用、明文凭据、配置残留、
  hst doctor、hst init、hst goal、loop 状态、CronList、scheduled_tasks、kimi skills 漂移、
  网关诊断、overcast、base_url、模型映射。
---

# agent-doctor - evo-agent 四端 agent 环境诊断修复

**渐进知识库型 skill**:本文件只做意图路由与纪律速览,四面细则在 `references/` 四篇,按需定点读。核心思想:**诊断取双源(hst doctor 的运行时诊断加本 skill config-lint 的静态度判据),修复走幂等重部署(hst init)与逐条手修,只报不改**。判例源:2026-10-12 五端插件清扫实证病灶族(enabledPlugins 与 plugins.enabled 悬空、明文 token、debug 构建路径、卸载后配置与缓存残留)加研究档 cfg-01(官方文档对照,判据分档依据)。

## 一、意图路由

| 意图 / 你要做的事 | 参考 |
| --- | --- |
| 四端配置诊断(跑 config-lint、读 error 与 advisory、逐条修) | `references/config-face.md` |
| hook 诊断修复(hst doctor hooks 面、hst init 重部署、codex trusted_hash、kimi 双 OS 形) | `references/hooks-face.md` |
| goal 与 loop 状态(hst goal 项目级面、缺省态、loop 原生域与 durable 件) | `references/goal-loop.md` |
| 网关诊断(overcast 候实装:配置对齐、连通性、活性三层) | `references/gateway-face.md` |

## 二、三面速览

| 面 | 主命令 | 判据 |
| --- | --- | --- |
| 配置诊断 | `uv run <技能根>/scripts/config-lint.py`(四端缺省路径;`--json` 机读;`--kimi-source` 漂移对账;`--claude` 指项目面文件则凭证升 error) | error 0;advisory 不挡 |
| 运行时诊断 | `hst doctor`(yolo、trust、binary、state、登录态、hook 形态、状态栏) | 逐 agent 逐 check 过 |
| hook 修复 | `hst init`(幂等:hook 注册、shim 落位、状态栏)、`hst hook init`、`hst hook verify` | 重部署后再 doctor 全过 |
| goal 状态 | `hst goal show / set / clear / heal` | show 出 present 与 rounds;heal 风暴闸在册 |
| loop 状态 | Claude Code 原生:CronList、`~/.claude/scheduled_tasks.json`、ScheduleWakeup 动态态 | 在册任务全可解释 |
| 网关诊断 | config-lint 网关键组配对 + curl health(候实装)+ `hst diagnose`(活性烧最小 token) | 三层各自判 |

## 三、纪律速览

- **只报不改**:config-lint 输出 findings 与退出码(0 无 error、1 有 error),修复动作走人;hst init 是幂等重部署,重复跑安全
- **判据两级**:error = 客户端不可能成功或写错载体的硬伤(解析失败、枚举非法、绝对路径缺失、高置信秘密形态、grok 悬空引用);advisory = 客户端容忍但值得治理(claude 悬空引用是文档容忍态、未知字段白名单、用户面明文凭证、卸载配置残留);依据与权威入口在 references/config-face.md,不凭记忆升档
- **豁免留因由**:`PEVO_CONFIG_LINT_ALLOW=字段a;字段b`(白名单与枚举值),登记在册不静默
- **hst 只认 PATH**:分发归宿主工具链 omc 与 ark;本 skill 不改 hst 源,增强 = 编排(hst doctor 加 config-lint 加修复手册)
- 按端跑:各端 PATH 里的 uv 直跑;装卸插件后各跑一次,安装面操作不同步清理配置引用(判例 2026-10-12)
