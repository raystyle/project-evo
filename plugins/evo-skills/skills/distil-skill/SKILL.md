---
name: distil-skill
description: >-
  项目技能自进化:把项目自身执行经验蒸馏成模式,经一案提案与合取闸门,持续产生并迭代
  Claude Code 与 Codex 双端支持的标准项目级 SKILL。三层聚合:sources 层收带时间的历史轨迹
  总结(执行痕迹按时间收束、资格过滤),knowledge 层收带版本、双向链接关联的结构化知识
  (模式页必带 trace 引文、防重提页只读),operations 层产物即项目级标准 skill(agentskills
  官方 spec 形态,过闸才进)。四步环:执行产痕、蒸馏模式、一案提案(create/patch/no_action
  三选一)、合取闸门(既有门禁无回归、点名失败义务翻转、标准页链到有 sources 的知识页)。
  知识层永不回滚,标准层拒绝即回滚,no_action 是合法出口;无人值守接受停待审;双端项目级
  加载与跨端转移重过闸。
  Use when 把项目执行经验沉淀成 skill、迭代项目标准技能集、建三层聚合知识库与双链图、蒸馏
  执行轨迹、给标准技能改动设闸验收、双端分发项目级 skill 时;触发词 技能自进化、distil、
  蒸馏、三层聚合、sources、knowledge、operations、轨迹总结、模式页、标准 skill、项目级
  skill、提案、合取闸门、no_action、防重提、CLAUDE_CONFIG_DIR、CODEX_HOME、双端、跨端
  转移、双链图、日记、活轨迹。
compatibility: 通用;跑环需项目 git 与既有门禁;双端执行面需 claude 或 codex CLI(命令面活权威是本机 --help 实查)
---

# distil-skill - evo-skills 项目技能自进化

**渐进知识库型 skill**:本文件只做意图路由与环速览,完整机制在 `references/` 五篇,按需定点读,不要求一次读完。

核心思想:**项目技能集是被治理的活资产**。执行经验先落带时间的历史轨迹总结(sources),蒸馏成带版本、双向链接的结构化知识(knowledge),一案提案过合取闸门才进标准 skill 集(operations);知识层永不回滚,标准层拒绝即回滚;证据不足走 no_action,不硬造产出。

## 一、意图路由

> 表未覆盖的意图:用文件名或关键字直搜 references/,或查 `references/README.md` 索引。

| 意图 / 你要做的事 | 参考 |
| --- | --- |
| 建或看三层聚合 / 轨迹总结与资格过滤 / 模式页与防重提页 / 双链与版本 | `references/layers.md` |
| 记执行轨迹 / 一天一篇活轨迹 / 坑与裁定留痕 / 升格分流 | `references/trajectories.md` |
| 跑一轮进化环 / 蒸馏取样与纪律 / 提案一案 schema / 停机条件 | `references/loop.md` |
| 给提案设闸验收 / 接受谓词 / 发布纪律 / 跨端转移 | `references/gate.md` |
| 双端执行面 / 项目级加载 / 隔离验证轮 / transcript 过滤 / 命令面 | `references/backends.md` |

## 二、四步环速览

```mermaid
flowchart LR
    A[执行产痕<br/>项目正常工作] --> B[蒸馏<br/>轨迹总结取样]
    B --> C[提案<br/>一轮一案]
    C --> D{合取闸门}
    D -- 三条全过 --> E[标准 skill 集提交<br/>operations]
    D -- 任一不过 --> F[标准集回滚<br/>提案全文进防重提页]
    B --> K[knowledge<br/>带版本双链知识]
    K --> C
    F --> K
    K -. 永不回滚 .-> K
```

- 三层单向支撑:sources 撑 knowledge,knowledge 撑标准 skill,反向不成立;原理不进标准页,步骤不进知识页
- 闸门合取三条:既有门禁无回归;至少一条点名失败义务翻转为过;标准页链到有 sources 的知识页
- 停机:无未覆盖的失败义务,或连续 no_action;没有满分短路

## 三、硬规则(速览)

- 标准面只收过闸产物;knowledge 可读但不进技能安装路径,蒸馏文本不是标准 skill
- 模式页无 trace 引文标 unverified,不得当提案依据;防重提页只由闸门追加,蒸馏角色只读
- 零工具调用、空输出的回合不进样本也不进分母;单次随机会话不得当分数
- 无人值守只批蒸馏与提案;接受停在待审提案,人不裁不发布
- 命令面以本机 `claude --help` 与 `codex exec --help` 实查为准,不照抄外部文档句子
