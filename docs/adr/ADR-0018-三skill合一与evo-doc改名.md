---
id: ADR-0018
title: 三 skill 合一为 doc-gov,evo-adr 改名 evo-doc,skill 与 hook 解耦
status: accepted
date: 2026-10-07
deciders:
  - raystyle
supersedes: []
superseded_by: null
tags:
  - skill-scope
---

# ADR-0018:三 skill 合一为 doc-gov,evo-adr 改名 evo-doc,skill 与 hook 解耦

## Context

用户立单(2026-10-07,整理重构批,五令):①doc-gov、code-kit、cli-docs 三 skill 合一;②evo-adr 改名 evo-doc;③插件内 skill 与 hook 解耦;④code-kit 工具面只带 md-guard 的 hook,init/check/scan 脚本与骨架模板移本仓 `.tools/`,斜杠命令三件删除;⑤知识面收敛:文档结构只有 ADR(需求决策)与 COE(三层聚合和双向链接图)两种形态,补项目日记形态(ADR 之外可增强),另留 Agent 友好 CLI 架构标准,其余复杂面(投影纪律、三栈工程合同、测试分层、封版流程、经验篇、平台矩阵等 15 篇参考)不再需要。市场收敛为两插件三 skill。

## Decision

合并为单 skill `doc-gov`(references 收敛 7 篇:base-adr、base-req、base-diary 新写、base-coe 新写、agent-face、tool-cli-agents、templates);插件改名 evo-doc,md-guard.py 与 mdrules.py 上移插件级 `scripts/`(hooks.json 指插件级路径,skill 目录纯知识,skill 与 hook 解耦);init/check/scan、骨架模板与 verification 用例移本仓 `.tools/`(check 与 scan 经插件路径 import mdrules,三面同源单源);commands/ 斜杠命令删除;SKILL 定位句落「指导 ADR、COE、项目日记三形态加 Agent 友好 CLI 架构标准」;manifest 版本线不动(两插件同版本线 0.4.3 不变,统一打版随后批)。

## Consequences

- 好:插件面聚焦(纯知识 skill 加插件级 hook);知识面与三形态定位对齐,检索面从 20 篇收敛 7 篇;仓工具归仓自用,插件分发面最小。
- 坏:evo-adr 改名属市场破坏性变更,已装者须卸载换装 evo-doc;骨架安装命令、投影纪律与三栈工程合同知识退出插件面(git 历史与旧版本缓存可恢复)。
