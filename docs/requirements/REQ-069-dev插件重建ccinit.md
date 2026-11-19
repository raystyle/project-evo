---
id: REQ-069
title: dev 插件重建为项目初始化面 ccinit(批 181)
status: implemented
priority: must
date: 2026-11-19
trace: tests/test_project_evo.py(test_skill_manifests_and_marketplace、test_pre_commit_matches_current_skills、test_live_surfaces_count_matches_reality、test_dev_plugin_rebuilt_clean_and_hooks_stay_removed、test_skill_description_form_repo_wide)
---

# REQ-069:dev 插件重建为项目初始化面 ccinit

## Scenario

总台裁定(2026-11-19):dev 以新义重建 = 项目初始化面,ccinit 单 skill(素材经
shares 通道推送,本仓收件落地后按仓规收口)。核心内容:六件资产分工表
(CLAUDE.md/rules/skills/agents/memory/hooks 各自职责、写入者、载入时机、判据)、
初始化流程(勘察、铺资产、验证清单)、CLAUDE.md 与 rules 与 hooks 骨架模板、
.reference/ 参考仓规范(放外部参考的项目仓库与文档;只读纪律、_provenance.yaml
出处链、片段优先、索引表)、判例(memory 不复制 docs 等)。

## Criteria

- [x] dev 插件重建:双 manifest(.claude-plugin 与 .codex-plugin)、README、
  skills/ccinit/SKILL.md,version 0.1.0
- [x] 内容修正(用户裁定):去外部仓出处点名(herdr-ccoe/hvperv-harness 双仓实践
  等历史轨迹噪音,守成品不点名外部仓库纪律);补 .reference 用途说明(放外部参考
  的项目仓库与文档)
- [x] 仓规收口:SKILL.md description 三句形(Use when 与不要用于)、禁字与约束术语
  清零(md-guard 与 term-lint 实跑)、双市场清单恢复 dev 条目、pre-commit 断链段收
  ccinit 树、守卫恢复双插件形且 dev 重建洁面断言(旧 skill/hook_rules/hooks/scripts/
  tools 不得回潮)
- [x] 门禁全绿:pytest 34、check、scan(带豁免)、term-lint、md-ref-scan
