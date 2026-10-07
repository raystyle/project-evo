---
id: ADR-0017
title: evo-codesec 插件下线,市场收敛两插件五 skill
status: accepted
date: 2026-10-07
deciders:
  - raystyle
supersedes: []
superseded_by: null
tags:
  - skill-scope
---

# ADR-0017:evo-codesec 插件下线,市场收敛两插件五 skill

## Context

用户立单(2026-10-07,同日两令):先移除 evo-codesec 的 `secret-scan` 密钥深扫 skill,再令整个 evo-codesec 插件下线(`security-audit` 一并移除)。密钥浅扫(工作区、git 全历史、敏感文件)已在同市场 code-kit 的 scan 命令;security-audit 为 Cloudflare security-audit-skill 中文化译本。市场收敛为两插件五 skill(evo-adr: doc-gov、code-kit、cli-docs;evo-herdr: herdr-flywheel、herdr-review),同批用户另令 md 挡板辖域限仓内 md。

## Decision

移除 `plugins/evo-codesec/` 整插件(secret-scan 与 security-audit 双 skill、双 manifest、README 与 secret-scan-cli 斜杠命令),双市场清单条目删除;守卫测试、pre-commit 断链段、gates 豁免面、幸存 skill 互引同步去 evo-codesec 化,密钥浅扫路由改指 code-kit scan;manifest 版本线不动(两插件同版本线 0.4.3 不变,统一打版留待整理重构批)。同批裁定:md-guard hook 辖域限仓内 md(事件带 cwd 时 file_path 须在其内,无 cwd 载荷保持宽容),属可逆行为细化,不另立 ADR。

## Consequences

- 好:插件面聚焦两插件五 skill;豁免面缩小(secret-scan ab 夹具正则退役);挡板不再触发仓外 md(如意向笔记与 plan 文件);node 运行时依赖面随 security-audit 校验脚本退出。
- 坏:安全审计面(Cloudflare 译本)与密钥深扫面(GitHub alerts 与 code search、裸克隆深历史、PII)失去,属市场破坏性变更,已装者须卸载(git 历史与 ~/.kimi 备份仍在,可按历史版本自行恢复);密钥自查只剩 code-kit scan 浅规则。
