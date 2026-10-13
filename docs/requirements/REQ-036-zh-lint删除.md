---
id: REQ-036
title: zh-lint 删除(中文面退出 skill 面)
status: implemented
priority: must
trace: tests/test_project_evo.py
---

# REQ-036:zh-lint 删除

## Scenario

用户令(2026-10-13,批 145):zh-lint 还是删除。沿革:批 141 lint 三合一 dev-lint,批 144 依用户裁定拆中文面复独立(采纳 grok 评审 2),批 145 用户终裁删除,中文语言纪律不设 skill 面;工具与判例史存 git 档案。终形回两插件九 skill = dev 三加 evo 六。

## Criteria

- [x] plugins/dev/skills/zh-lint 全目录删除(SKILL、stc-rules、reporting、zh-lint.py)
- [x] dev-lint 去姊妹指路与沿革改写(中文面经拆出后删除,中文语言纪律不设 skill 面);触发词无 zh 域残留
- [x] 守卫与路由面随形:SKILLS(dev 三)、test_zh_lint_tool 退役、pre-commit(九目标)、双 manifest 与市场清单(dev 0.14.2 独立升,evo 不动)、AGENTS 与根 README 与 docs 地图与 dev README(两插件九 skill);ADR-0025 终形改九
- [x] 四门禁全绿 + fleet 回执 + 知会 grok(评审 2 终局 = 删除)
