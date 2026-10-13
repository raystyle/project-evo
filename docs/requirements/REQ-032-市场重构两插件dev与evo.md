---
id: REQ-032
title: 市场重构:两插件 dev 与 evo,裁四 skill 与五原语拆分
status: implemented
priority: must
trace: tests/test_project_evo.py
---

# REQ-032:市场重构（两插件 dev 与 evo）

## Scenario

用户令(2026-10-13,数条渐进定形):project-evo 是市场名,不需要那么多插件(非唯一,后续还会有);不需要 herdr-orch、agent-s5、agent-rloop;agent-prim 拆五原语 skill;再开 dev 插件收 doc-gov 与改名 dev-cli 的 doc-cli;lint 三 skill 进 dev;distil-skill 改名 distil(触发 = 蒸馏);agent-doctor 去掉。结构决策见 ADR-0025。

## Criteria

- [x] 两插件十一 skill:dev(doc-gov、dev-cli、md-lint、ls-lint、zh-lint)与 evo(agents、shares、streams、tasks、pipes、distil);双 manifest 与两市场清单两条目,同版本线 0.13.0
- [x] 裁撤四 skill(herdr-orch、agent-s5、agent-rloop、agent-doctor),存活面引用清零或改注历史
- [x] agent-prim 拆五原语 skill,共享面归 agents 独家 references,四域 skill 单文件自持加相对链接触发词按域自然语化
- [x] 两改名落地:doc-cli 改 dev-cli、distil-skill 改 distil(全树同步含自引)
- [x] 插件级资产随域走:md-guard、mdrules、lint-hook 与写后 hook(段名 dev file-check)归 dev;守卫随形(测试 PLUGIN/SKILLS/市场一致性/断链段/段名/计数守卫,pre-commit,check.py;config-lint 测试族随 agent-doctor 退役)
- [x] AGENTS 与根 README 与 docs 地图路由面全同步;四门禁全绿 + fleet 回执
