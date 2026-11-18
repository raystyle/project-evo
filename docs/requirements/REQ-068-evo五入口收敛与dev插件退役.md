---
id: REQ-068
title: evo skills 五入口收敛与 dev 插件退役与 hook_rules 知识树删(批 180)
status: implemented
priority: must
date: 2026-11-18
trace: tests/test_project_evo.py(test_skill_manifests_and_marketplace、test_hook_rules_tree_stays_removed、test_pre_commit_matches_current_skills、test_live_surfaces_count_matches_reality、test_dev_plugin_and_hooks_stay_removed、test_evo_primitive_skill_dirs_align_with_commands)
---

# REQ-068:evo skills 五入口收敛与 dev 插件退役

## Scenario

prim v5 五入口收敛(herdr-ccoe ce5dd93,2026-11-18 用户裁定;总台令):入口收敛为
shares/streams/ctxs/ports/pipes;agents/desks/machines 三域退役(归 hc 与 herdr-app
原生面);动词对齐 hc = 清单 ls(原 view)、留痕 send(原 to)、生命周期 start
(原 open),旧名不留别名;pipes send = 字节写,留痕知会归 streams send。
连带裁定:dev 插件整目录退役;本仓职责收缩为只维护 skill 面,不维护 prim(真源在
herdr-ccoe 仓)。用户续令(二段):hook_rules 知识树整删,只保留 evo 插件的原语
命令 skill,知识面并回各 SKILL.md 自含。消费方 evo skills 按新面重写。

## Criteria

- [x] 五 skill 壳按 prim v5 五面手册(manual.py 与金样)重写且知识面自含:shares
  (ls/put/get/send)、streams(裸 ls 房间清单/room/dm/append/send,吸收 fleet 回执
  道与 dm 专线与 append-only 礼仪)、ctxs(ls 头行与 ls <request_id> 单请求并法/
  search)、ports(ls/start/close/fwd/send)、pipes(ls/start/close/send)
- [x] 退役面:agents/desks/machines/research 四 skill 目录删;hook_rules 知识树整删
  (二段令,知识面并回 SKILL.md);dev 插件整目录删(门禁脚本五枚迁 .tools,lint-hook
  随退役删);evo hooks 目录删;SKILLS 清单同步;正典原语集收敛为五
- [x] 活面同步:AGENTS 定位与阶段行、根 README(含职责声明:只维护 skill 面,不维护
  prim)、evo README、docs 地图、gates、skill-spec B3/B14/B15/B16、双 manifest 与
  双市场清单(evo 0.23.0;Codex 删 dev 条目)、pre-commit 断链段、pyproject 描述
- [x] 实证准入(ADR-0010):本端 prim 先滚装五入口形(herdr-ccoe 源临时装验),
  五域 --llms 与金样逐字一致、五域 ls 实跑、shares put 实弹往返成功
- [x] 门禁全绿:pytest 34、check、scan(带豁免)、term-lint、md-ref-scan(pre-commit
  挡板实跑)
