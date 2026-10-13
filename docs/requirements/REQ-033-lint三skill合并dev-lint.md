---
id: REQ-033
title: lint 三 skill 合并为 dev-lint
status: implemented
priority: must
trace: tests/test_project_evo.py
---

# REQ-033:lint 三 skill 合并为 dev-lint

## Scenario

用户令(2026-10-13,市场重构续令):三个 lint 应该合成一个 dev-lint skill。md-lint、ls-lint、zh-lint 三 skill 并一,归 dev 插件;结构决策补入 ADR-0025。

## Criteria

- [x] dev-lint 落形:SKILL.md 意图路由四类面(md 面、语言面、结构面、中文面)加门禁速览;references 八篇扁平前缀分组(md-faces、lang-checks、hook-face、ls-types、ls-rules、ls-evals、zh-stc-rules、zh-reporting)加索引;scripts/zh-lint.py 与 templates 四类型模板随迁
- [x] 三原目录退出;description 触发词三合一(md-lint、ls-lint、zh-lint 旧名保留为触发词)
- [x] 守卫与路由面随形:SKILLS 清单、pre-commit 断链段(九目标)、双 manifest 与市场清单(dev 三 skill 描述)、AGENTS 与根 README 与 docs 地图、dev README;版本载体 0.13.0 进 0.13.1;四门禁全绿 + fleet 回执
