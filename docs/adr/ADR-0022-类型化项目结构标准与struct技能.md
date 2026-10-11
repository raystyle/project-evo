---
id: ADR-0022
title: 类型化项目结构标准:struct 技能挂 evo-lint,声明式自研规则,四类型模板库
status: accepted
date: 2026-10-11
deciders:
  - raystyle
supersedes: []
superseded_by: null
tags:
  - skill-scope
  - structure
  - lint
---

# ADR-0022:类型化项目结构标准与 struct 技能

## Context

用户立项(2026-10-11):参考 ls-lint,为不同类型项目立最佳标准结构的初始与检查技能。舰队已有四实践仓实形与当日结构研究(单仓折中形:知识三层居仓根、产品代码归 src、可部署子工程与 Rust 子工程成员化、配置根件一工具一件、生成投影在发现位);既有 .tools/init.py 是本仓单形骨架生成,无类型面、无声明式规则。ls-lint(PHP 生态)是参考不是依赖:按仓纪律「skill 只认 PATH,外部工具分发归 omc 与 ark」,且规则需中文语境与三层聚合语义,自研声明形成本低于引依赖。

## Decision

- 挂 evo-lint 插件第二 skill **struct**(客户端 evo-lint:struct),init 面(按类型脚手架:既有件不动,缺件补位)加 check 面(结构 lint:声明式规则比对,ls-lint 同族)
- **规则自研声明式**:每类型一 toml 规则件(meta、required 必备、generated 生成物位、excluded 禁入源码树、config-root 配置根件位、optional 可选成员位),随技能入库 templates/;未来脚本化时同格式可直接吃
- **四类型起步**(数据源四仓实形加研究档,可扩):TS CLI 仓、知识三层聚合仓、worker 服务仓、Python 工具仓
- **豁免与本地覆盖**:每仓 `.struct-lint.toml`(或等位)可覆盖规则与豁免路径,豁免须带因由登记在册,不静默;沿 check.py PEVO_CHECK_ALLOW 判例
- 不施工实践仓:模板与规则先立标准,实践仓迁移各自走蒸馏环与施工单

## Consequences

- 好:结构标准从「本仓单形 init」升「类型化模板库加声明式检查」,新仓脚手架与存量仓结构 lint 有据;声明式规则件同时是文档与未来脚本输入,零重复
- 坏:类型模板需随实践演进迭代(四仓形态漂移时模板要跟,维护面加一);自研规则器脚本化前 check 面靠 agent 按规则件人工比对,机检留待判例(grok 条 6 同族回流候选)
