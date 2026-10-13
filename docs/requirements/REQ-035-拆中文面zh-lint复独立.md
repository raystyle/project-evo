---
id: REQ-035
title: 拆中文面:zh-lint 复独立 skill
status: implemented
priority: must
trace: tests/test_project_evo.py
---

# REQ-035:拆中文面（zh-lint 复独立）

## Scenario

用户裁定(2026-10-13,批 144):dev-lint 拆中文面(grok 评审 2 触发竞争论获采纳:约 711 字跨域 description 发现阶段互相抢激活,对照 agentskills 只常驻 name 与 description、VS Code 分扩展)。dev-lint 留 md 面、语言面、结构面;zh-lint 复独立 skill 归 dev。

## Criteria

- [x] zh-lint 复形:SKILL.md 与 references 索引自 git 史恢复(题注与分工行随新形改:与 dev-lint 分工 = 格式禁字断链结构对语言清晰度),stc-rules 与 reporting 复原名名,scripts/zh-lint.py 随迁回
- [x] dev-lint 瘦身:description 与路由与速览去中文面,触发词去 zh 域(结构、脚手架、md、语言留),六篇 references;zh-lint.py 指路姊妹 skill
- [x] 守卫与路由面随形:SKILLS 清单(dev 四 skill)、pre-commit 断链段(十目标)、双 manifest 与市场清单(dev 0.14.1 独立升,evo 0.14.1 不动)、AGENTS 与根 README 与 docs 地图与 dev README(两插件十 skill);ADR-0025 决策一与后果补裁定
- [x] 四门禁全绿 + fleet 回执 + 知会 grok(其评审 2 获裁定采纳)
