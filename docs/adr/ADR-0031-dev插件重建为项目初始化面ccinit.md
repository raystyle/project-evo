---
id: ADR-0031
title: dev 插件重建为项目初始化面 ccinit,单 skill 知识面自含
status: accepted
date: 2026-11-19
---

# ADR-0031:dev 插件重建为项目初始化面 ccinit

## Context

批 180(ADR-0030)dev 插件整目录退役(开发治理面无消费道)。总台次日重建裁定
(2026-11-19,lan-win/t3v 执行素材,本仓收件落地):dev 以新义回归 = 项目初始化面,
ccinit 单 skill:按六件资产分工(CLAUDE.md/rules/skills/agents/memory/hooks)加
.reference 参考仓规范,为项目铺设 Claude 配置基线。本仓只维护 skill 面(批 180 补充
裁定)不变,重建体不含 prim 代码、不含 hook_rules 知识树、不含门禁脚本。

## Decision

1. dev 插件重建为项目初始化面:plugins/dev/ 只含 .claude-plugin 与 .codex-plugin
   双 manifest、README、skills/ccinit/ 单 skill;version 0.1.0(重建后独立 semver,
   不继承旧 dev 治理面版本线)。
2. ccinit skill 知识面自含于 SKILL.md(与批 180 二段令形态一致):六件资产分工表、
   初始化流程(勘察、铺资产、验证)、CLAUDE.md/rules/hooks 骨架模板、.reference/
   参考仓规范(放外部参考的项目仓库与文档,只读纪律、出处链、片段优先、索引)、
   双仓判例沉淀(去出处点名,守成品不点名外部仓库纪律)。
3. 旧面不随重建回潮(守卫断言):dev-doc/dev-cli 双 skill、hook_rules 树、hooks、
   scripts、tools 目录均不得回;门禁脚本留仓根 .tools(批 180 迁入,不回插件)。
4. 市场:Claude 与 Codex 双清单恢复 dev 条目;两插件六 skill 版图(dev 一加 evo 五)。

## Consequences

- 旧 dev 消费方(批 180 已卸载)按需新装 dev@project-evo(0.1.0,新义);调用名
  dev:ccinit;旧 dev:dev-doc、dev:dev-cli 不复活。
- 守卫同步:PLUGIN_NAMES 与 SKILLS 恢复双插件、semver 起步线分插件(dev 0.1 与
  evo 0.23)、pre-commit 断链段收 ccinit 树、活面计数(两插件六 skill)、dev 重建
  洁面守卫(只收 ccinit,旧四目录不得回)。
- md-ref-scan SKIP 补目标项目示例文件名(MEMORY.md、NOTES.md、precedent-researcher.md):
  ccinit 铺到目标仓的产物名,非本仓静态文件,沿报告类产物名兜底先例。
- ADR-0030 的 dev 退役裁定由本决策翻页(其 evo 五入口收敛与门禁脚本迁 .tools 部分
  不变);evo 消费方不受影响。
