---
id: ADR-0012
title: gh-issue skill 增编,evo-adr 双 skill 二扩三
status: accepted
date: 2026-09-16
deciders:
  - raystyle
supersedes: []
superseded_by: null
tags:
  - governance
  - gh
  - issue
---

# ADR-0012:gh-issue skill 增编,evo-adr 双 skill 二扩三

## Context

四插件八 skill 形态(ADR-0010 立,ADR-0011 扩八)运行中,本机命令/工具出错向上游 GitHub 仓报 bug 仍是手工路径:找仓、搜重复、手写正文、网页发单,口径散。用户裁定(2026-09-16)沉淀为 evo-adr 第三 skill gh-issue:经 gh 自动发 bug issue,无草稿确认闸直接发,发前双通道去重(命中 open 重复不发,回执附链接)。

## Decision

- evo-adr 增编第三 skill `gh-issue`(命令出错自动上报工作流:目标仓解析序、双通道去重与四格判定、正文模板与截断脱敏纪律、label 与权限预检、三态回执);修订 ADR-0010 的八 skill 清单条款为九 skill,四插件形态与分域不变
- 目标仓解析不建硬编码映射表:git remote 与 gh repo view 自取,举列 owner/repo 占位;与 evo-research:research 的 gh 篇分界单向指针(research 管通用 gh 面,gh-issue 只管 issue 上报纪律)
- 命令块实证纪律(ADR-0010 构造纪律)沿用:写进 SKILL.md 的命令本会话真跑;gh issue create 无 dry-run,以本仓自发实证单验后即关

## Consequences

- 好:命令出错上报从手工路径变五步纪律,自动发单零等待;去重先行防撞单;正文模板保报错原文与版本事实
- 坏:evo-adr 三 skill 后清单面与守卫同步成本微增;自动发单无人工闸,误判重复或脱敏漏检的风险由去重与脱敏纪律承担
- 无破坏性:新增能力,既有安装不受影响;版本线随四插件同版前进
