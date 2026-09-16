---
id: ADR-0006
title: Rust 栈 aidoc 投影强制化,bin-only 不再豁免
status: accepted
date: 2026-09-16
deciders:
  - raystyle
supersedes: []
superseded_by: null
tags:
  - projection
  - rust
---

# ADR-0006:Rust 栈 aidoc 投影强制化

## Context

第五十七批的「无自有 API 面项目」范式出台后,ark_rs、hst_rs、reader_rs 三仓以 bin-only 无公开库面为由裁定 aidoc 投影不适用,只留一句裁定句。用户 2026-09-16 裁定推翻此口径:Rust 仓一律强制使用 aidoc 投影并重构落位。理由:bin-only 仓的投影受众是维护者与 agent 而非外部用户,agent 检索面(分模块 md 加 llms.txt)对自家仓同样成立;browse-rs 已实证全量投影加漂移门禁加渲染格式豁免的完整闭环可行。

## Decision

Rust 栈 aidoc 投影是强制标配,不是可裁定项:「无自有 API 面项目」范式不覆盖 Rust 仓(该范式限构建树与补丁仓等非三栈形态)。Rust 仓对齐面:`///` 契约注释覆盖公开项、missing_docs 策略落地或显式分级、cargo aidoc 生成投影进 Git、`cargo aidoc --check --strict` 入 AGENTS Commands 作漂移门禁;工具渲染格式禁字按 tool-rust 豁免实务路径级登记。既有「不适用」裁定句由各仓重构时撤换,引用本 ADR。

## Consequences

- 好:六仓 Rust 面 agent 检索面统一,契约注释纪律由投影门禁反向强制;aidoc 工具本身获得三仓新实证场
- 坏:三仓需一轮真实重构(补 /// 注释、开 missing_docs、生成投影),存量仓首次跑有成本;非家族第三方 Rust 仓采用 dev-evo 时该强制项门槛变高,后续若反馈强烈可评估分级(家族内先行全强制) [假设]
