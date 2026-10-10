---
id: ADR-0020
title: 三插件五 skill 版图:evo-skills 立项 distil-skill,doc-gov 三向拆分,herdr-dev 更名 herdr-orch
status: accepted
date: 2026-10-10
deciders:
  - raystyle
supersedes: []
superseded_by: null
tags:
  - skill-scope
---

# ADR-0020:三插件五 skill 版图:evo-skills 立项 distil-skill,doc-gov 三向拆分,herdr-dev 更名 herdr-orch

## Context

用户立单(2026-10-10,与 grok 邻格对照研究 wikiskill 后):把 doc-gov 的三层聚合剥离出来,形成让项目基于自身执行经验自动产生并迭代项目级标准 skill 的技能,支持 Claude Code 与 Codex 双端;裁定立第三插件 evo-skills 承载,技能名 distil-skill。同日追加裁定:doc-gov 聚焦 ADR/REQ 需求决策、代码 doc 注释、文档即代码,日记类文档转入 distil-skill,agent 原生面抽离为 native-design;evo-herdr 开发模式 skill 更名为 herdr-orch(主开发台初始各工作角色邻居窗格并开始配合工作,功能不变),herdr-flywheel 专注跨仓库、跨项目、跨机器交流;两 skill 通用「herdr 态是检测信号,md 文件是状态与产物」的跨窗格交流原则。

## Decision

市场收敛为三插件五 skill,版本线统一升 0.6.0:

- 新插件 `evo-skills` 立项,单 skill `distil-skill`:三层聚合(sources = 带时间的历史轨迹总结,knowledge = 带版本的双向链接关联结构化知识,operations = 产物为 Claude Code 与 Codex 双端支持的标准项目级 SKILL);四步环执行、蒸馏、提案、合取闸门;接受谓词 = 既有门禁无回归加至少一条点名失败义务翻转为过加标准页链到有 sources 的知识页(不搬均值闸与满分短路);no_action 合法出口;知识层永不回滚、标准层拒绝即回滚;标准面只收过闸产物
- `doc-gov` 三向拆分:COE 三层聚合与项目日记(轨迹总结形态)迁入 distil-skill;Agent 友好 CLI 面抽离为同插件新 skill `native-design`(agent-face、tool-cli-agents、templates 三篇随迁);自身聚焦 ADR/REQ 需求决策、代码 doc 注释契约、文档即代码、研究档案、项目工具链范式(references 9 篇收 5 篇,新立 base-code-doc)
- `herdr-dev` 更名 `herdr-orch`:定位改述为主开发台初始各工作角色邻居窗格并开始配合工作(内容主体不动);`herdr-flywheel` 定位收准为跨仓库、跨项目、跨机器交流;跨窗格交流原则(herdr 态是检测信号,md 文件是状态与产物)入两 skill,唯一权威源在 herdr-flywheel 产物契约篇

## Consequences

- 好:版图按治理域清分(文档决策与原生设计、开发台与跨机交流、技能自进化);三层聚合与自进化环同处一个 skill,轨迹总结(原日记)有了机制归宿;doc-gov 触发面收窄后与 distil-skill、native-design 无主讲重叠
- 坏:herdr-dev 与 doc-gov 旧触发词失效,依赖旧名的消费者需重学(git 历史可恢复);三插件版本线同步面从六处载体扩到八处(三插件双 manifest、市场清单、三 README);distil-skill 的合取闸门尚未整轮实测,首跑后回填实证
