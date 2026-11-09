---
id: REQ-066
title: 注入加载器与 distil 技能退役(批 178)
status: implemented
priority: must
date: 2026-11-09
trace: tests/test_project_evo.py(test_hook_loaders_wired_and_isolated 装配守卫、test_hook_rules_tree_valid、test_pre_commit_matches_current_skills)
---

# REQ-066:注入加载器与 distil 技能退役

## Scenario

用户令(2026-11-09):evo 插件仍挂的 2 个 hook 已不需要,剔除 hook_rules 的注入设置;
随后追加 distil 技能删除。合并为批 178:双插件 hooks/ 整段退役、distil 技能与其
hook_rules 知识件六枚退役,hook_rules 知识树保留,加载路径唯一化为壳直读。

## Criteria

- 双插件 hooks.json 空装配、intent-guidance.ts 与 dev-rules.ts 删(注入面剔除由
  总台批 3d0fb88、43fea40 先行);装配守卫断言两插件均须空。
- plugins/evo/skills/distil/ 与 hook_rules/intents/distil*.md 六枚不存在;
  SKILLS 清单与 HOOK_RULES 计数断言同步(evo intents 27 减 21)。
- 十三枚存活 skill 壳指路句改为壳直读措辞,不再提注入。
- 活面同步:AGENTS、根 README、双插件 README、双 manifest 与市场清单、
  docs/README、skill-spec(闸门条目退役注记)、pre-commit 断链段、ADR-0028、
  CHANGELOG;版本 dev 0.19.0、evo 0.21.0。
- 五道门禁全绿:pytest、check.py、scan.py、term-lint、md-ref-scan。
