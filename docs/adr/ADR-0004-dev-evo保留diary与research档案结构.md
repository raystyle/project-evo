---
id: ADR-0004
title: dev-evo 保留 diary 与 research 档案结构
status: accepted
date: 2026-09-16
deciders:
  - raystyle
supersedes: []
superseded_by: null
tags:
  - doc-structure
---

# ADR-0004:dev-evo 保留 diary 与 research 档案结构

## Context

第五十批 dev-evo 重构把老体系 docs 六目录(proven/diary/research/references/guide/mistakes)收敛为五(adr/requirements/guides/diary/research):proven 语义由 implemented REQ 加关联 ADR 承接,mistakes 并入 ADR。base-init 裁剪原则曾将 guides/diary/research 并列为按需生长,存在后续收敛批把 diary 与 research 一并裁撤的解释空间。第五十三批飞轮实测中三仓 diary 承担存量豁免与过程留痕、research 承担 S008 对标落盘,两目录是体系运转的实证件。用户 2026-09-16 裁定红线。

## Decision

dev-evo 骨架五目录中 diary 与 research 是保留核心结构,不是可裁撤项:init 即建目录,diary 首日一笔,research 无真实研究可暂空(PE-09 SKIP 合法);后续任何收敛或裁剪批不得动这两目录的结构地位。guides 仍按需生长。

## Consequences

- 好:过程档案与证据档案的长线地位有决策锚,不再依赖文本解释
- 坏:极小项目也带两个低频目录;以目录在、内容渐进换结构稳定,代价可受 [实证: 三仓迁移后 diary 与 research 均在役]
