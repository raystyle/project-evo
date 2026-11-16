---
id: REQ-067
title: evo skills 六入口重写与四域退役(批 179)
status: implemented
priority: must
date: 2026-11-16
trace: tests/test_project_evo.py(test_skill_manifests_and_marketplace、test_hook_rules_tree_valid、test_pre_commit_matches_current_skills、test_live_surfaces_count_matches_reality、test_evo_primitive_skill_dirs_align_with_commands)
---

# REQ-067:evo skills 六入口重写与四域退役

## Scenario

prim v5.0.0 六入口定形(herdr-ccoe 4e5006c,2026-11-16;总台令):入口收敛为
agents/desks/machines/streams/shares/ctxs;carry 三合一入口弃,pipes/ports 随退,
shares 复活直入第六入口;tasks 域退役(streams 只做增量消息,钉任务走 agents to);
mcps 整域退役(MCP 边缘化,2026-11-13 用户裁定);动词标准全域统一(view = 清单与读、
to = 留痕知会、start/close = 生命周期),machines list/runtimes 别名退役、ctxs show
并入 view <id>。消费方 evo skills 按新面重写(ADR-0003 放开重构裁定,可断重写)。

## Criteria

- [x] 六 skill 壳与知识件按 prim v5.0.0 六面手册(manual.py)重写:agents 十五动词
  (view/workbenches/read/to/wait/inbox/mode/start/close/reload/trust/yolo/run/shell/
  dev/keys)、desks 三动词兜底(view/start/close,树形拓扑归 mod GUI)、machines
  (view/add/reconnect/run/close/runtime)、shares(view/put/get/to)、streams
  (裸 view 房间清单/room/dm/view 读流/append/to)、ctxs(view 头行/view <id> 全链/
  search;show 并入);退役动词以 stub 可见化口径入知识件(usage 退 2 指新道)
- [x] 四域退役:plugins/evo/skills/{tasks,pipes,ports,mcps}/ 与同名 intents 四枚删;
  SKILLS 清单与 HOOK_RULES 计数同步(evo intents 21 减 17);正典原语集收敛为六
- [x] 动词标准统一与文法契约随形:agents-contract 七原语共享面改六入口共享面,
  六域速查行重写;desks-workspace 开台细则改 agents 面(workbenches/shell/dev)
- [x] 活面同步:AGENTS 定位与阶段行、根 README 定位与 skill 表、evo README、
  docs 地图计数、skill-spec B15、双 manifest 与市场清单(dev 描述注入残影顺手修)、
  pre-commit 断链段;版本 evo 0.22.0(破坏性:四 skill 退役)、dev 0.19.1(描述修正)
- [x] 实证准入(ADR-0010):本端 prim 先滚装 v5.0.0,六入口核心动词逐面实跑
  (view 族、shares put/get 往返、streams 裸 view 清单与读流、退役 stub 退 2);
  上游缺陷如实报:ctxs view <request_id> 并法行漏传 g(TypeError),已回执 fleet
  修向,知识件按契约面书写
- [x] 五道门禁全绿:pytest、check.py、scan.py、term-lint、md-ref-scan
