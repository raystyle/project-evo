---
id: REQ-059
title: research 检索 skill 入真源(多通道路由)
status: implemented
priority: must
trace: tests/test_project_evo.py
---

# REQ-059:research 检索 skill 入真源

## Scenario

用户令(2026-10-17):evo 插件新增检索域 skill `research`,按指定研究目标路由多通道检索:gh 与 browse 搜 GitHub、browse 搜 Google/Bing、browse 搜 scholar.google.com 学术面。产出形态已拍板:纯检索原语+交棒,值得立档案的目标走 dev:doc-gov 研究档案面(单一权威源不破)。补充令:browse 面必须覆盖 rn 编排与油猴探针;gh 面自省命令帮助。

批中修正两令(同日):google 主搜索面易被挑战,出路由(实弹印证:本机判读机回执 verdict=challenged 落 /sorry);网页检索只用 bing 不设备胎,bing 与 github 无头即通。

定位:evo 出站检索域(与 mcps 同族)。无自有 CLI 动词面,B4 渐进知识库型(同 doc-gov 骨架);B3 非命令面例外(同 distil:入 SKILLS 清单,不入正典命令集)。判例底料:intelligence 工作台四问应答(2026-10-17,browse_rs 代转):三态判别、rn 编排五律、油猴探针判据、gh/browse 双轨分野;上游两注:rn 入口以 workspace 仓裸形为准(`-> Result` 旧形编译错)、verdict 术语对齐 google-search mech 族。B17 实证准入:写进 skill 的命令形均本机真跑(见 Criteria)。

## Criteria

- [x] REQ-059 skill 入真源(SKILL.md 渐进知识库型 58 行 + references 五篇,description 三句形 ≤400 过静检)
- [x] 实证准入全过:gh 五动词各真跑一条(repos --json/code/issues/prs/commits);bing fetch 直出(`via: http` 全 SERP)与无头引擎 goto+js 抽取;scholar fetch 直通(HTTP 200 满页 10 条);github 仓页 fetch;google-search 双探针实装(install --restart)、判读机 mech 真跑(challenged 判读正确);自写最小编排 .rn 裸形实跑(无头 bing 三条返回);google 主面 challenged 出路由即批中修正令的实证
- [x] 守卫有意识更新:SKILLS 清单增 research、B3 豁免集 {"distil"} 增 research(非命令面例外,注释注本 REQ)
- [x] 双 manifest 与市场清单计数同步(十四 skill),市场清单存量滞后顺批清账(两插件计数、evo 枚举补 mcps/nodes/research;连带根 README 表补 mcps/nodes 行、两插件 README 发布号、gates.md 计数)
- [x] 变更完整性:AGENTS/README/docs 地图/githooks 断链段同步;三敲法坑入 rulings.md(--vars 引号、userscript 绝对径、stdin 空串提示)
- [x] evo 独立升 0.17.0(新能力 minor);门禁全绿(pytest + check + scan + md-ref-scan 十四面)
