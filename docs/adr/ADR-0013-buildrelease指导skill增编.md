---
id: ADR-0013
title: build-release 指导 skill 增编,evo-adr 三 skill 三扩四
status: accepted
date: 2026-09-17
deciders:
  - raystyle
supersedes: []
superseded_by: null
tags:
  - governance
  - ci
  - release
---

# ADR-0013:build-release 指导 skill 增编,evo-adr 三 skill 三扩四

## Context

各仓编译打包发布形态经多轮实战收敛(自含静态构建、双段镜像、自升级双通道、护栏三件),但散在各仓工作流与 REQ,新仓接入靠逐仓考古。2026-09-17 总台派单起草全仓标准,外部 CI/CD 通稿作基底,总台六轮追正定形:产出为仓无关指导 SKILL(herdr-flywheel 同形态先例),类型路由「什么样的项目,怎么做」,references 必带可拷改参数化模板;**通用性终约束(最高优先)**:标准为通用件,私有名称与私有信息零出现,契约全部抽象参数化,实证引一律不进 SKILL 留仓内 diary;边界只辖仓侧 GitHub CI/CD 自建流,CI 不可产的大件分发不属本面。起草期的 doc-gov references 草稿篇(flow-build.md)随定形退役并入本 skill。

## Decision

- evo-adr 增编第四 skill `build-release`(仓无关编译打包发布流水线指导:六型配方 go/rust/npm/py/native/manifest,每型七要素;三段式正源 本地编译和打包 到 GitHub 产物发布 到 CI/CD Action 自动播种;公共契约节管边界与产地、rclone 恒形与段制、Release 直发、护栏三件、自升级与元数据对齐;references 含可拷改模板:本地编译与发布命令面、各型片段、CI/CD 播种 workflow、自升级核对清单);修订 ADR-0010 的九 skill 清单条款为十 skill,四插件形态与分域不变
- 类型路由制:按仓根清单形态分型给配方,先定型号再取七要素;公共契约型号无关,型号差异只写型差异
- 通用性纪律入正文与模板:镜像域写 `<mirror-host>/<tool>/<version>/`,安装管理器元数据写「安装管理器的工具级状态」,Secrets 名保持通用 R2 族;仓名与私有基础设施名正文注脚示例模板默认值全禁,实证留档只进仓内 diary

## Consequences

- 好:流水线标准从逐仓考古变成对号入座,新仓接入零记忆;模板参数化空壳拷改即用;通用件可对外分发不受私有信息泄漏面约束
- 坏:evo-adr 四 skill 后清单面与守卫同步成本微增;通用化抽象使具体环境的镜像域与安装管理器对接须各仓自行填参
- 无破坏性:新增能力,既有安装不受影响;版本线随四插件同版前进
