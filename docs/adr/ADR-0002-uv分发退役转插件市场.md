---
id: ADR-0002
title: uv tool 分发通道退役,全走插件市场
status: accepted
date: 2026-09-04
deciders:
  - raystyle
supersedes: []
superseded_by: null
tags:
  - distribution
---

# ADR-0002:uv tool 分发通道退役,全走插件市场

## Context

早期以 uv tool install 分发 CLI 工具,与插件市场双通道并行:两套安装面、两套版本探测、两套更新语义,漂移成本高;脚本本体已 PEP 723 化,uv run 直跑不需要安装态。

## Decision

分发只走插件市场(Claude Code / Codex / Grok 市场清单 + 双 manifest;Kimi 无市场走手拷 skills),脚本保留 PEP 723 零依赖形态可免插件直跑,uv tool install 通道退役。

## Consequences

- 好:单一分发真相;市场版本号即更新探测锚;脚本面零安装即可用。
- 坏:无市场客户端的用户要手拷或直跑脚本 [实证: CHANGELOG 第二十八批转型实录]
