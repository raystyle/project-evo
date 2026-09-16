---
id: ADR-0011
title: herdr 评审闸门 skill 增编,evo-herdr 双 skill 七扩八
status: accepted
date: 2026-09-16
deciders:
  - raystyle
supersedes: []
superseded_by: null
tags:
  - governance
  - herdr
  - review
---

# ADR-0011:herdr 评审闸门 skill 增编,evo-herdr 双 skill 七扩八

## Context

四插件重组(ADR-0010)落定后 evo-herdr 单 skill。飞轮实践中工位侧演化出稳定的评审闸门惯例:交付批经 herdr 右侧 codex 评审会话对齐后推 main(hst_rs AGENTS 合同环境节明载)。实证链充分:2026-08-31 整文件 code review 十五条发现与五轮交叉复核链(codex、codex、grok、kimi、codex,每轮抓出上轮新引入缺陷);D46 至 D53 推送前门禁的评审请求与回执原文(hst trace 会话史可溯);评审格实况(命名 hst-codex-review、用户级 cwd 跨仓收件、与开发格同 tab 右侧位)。用户裁定沉淀为标准工作流 skill,并补评审格「检测右侧、无格建格起 codex、有格直接对话」的自愈程序(2026-09-16 于 project-evo 工位全流程实证)。

## Decision

- evo-herdr 增编第二 skill `herdr-review`(推送前评审闸门工作流:评审请求五件模板、F 必修/G 建议/CONFIRM 三态回执与轮次至终审放行、发现逐条核实与交叉复核纪律、评审窗格挂位命名与检测带起程序、hst trace 对话检索);修订 ADR-0010 的七 skill 清单条款为八 skill,四插件形态与分域不变
- herdr-flywheel 仍是派单/回执/断言/吸收四步协议唯一权威源;herdr-review 不复述派单命令细节只指路,-flywheel 参考节加反向指针
- 按「吸收即提炼」入库:请求与回执句式取自工位实证原文,纪律条目带实证标注;skill 命令块本会话实证(herdr pane neighbor/split、agent start/list、hst trace sessions/search)

## Consequences

- 好:评审闸门从各工位惯例变成可复用标准,跨仓请求与回执格式统一;评审格检测带起自愈,新工位零记忆接入
- 坏:evo-herdr 双 skill 后清单面与守卫同步成本微增;两 skill 边界(协议面与评审特化)须靠互指维护,漂移即双份
- 无破坏性:新增能力,既有安装不受影响;版本线随四插件同版前进
