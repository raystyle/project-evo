---
id: REQ-062
title: desk 析出与 nodes 更名 machines(prim 3.10 命名三分同步)
status: implemented
priority: must
trace: tests/test_project_evo.py
---

# REQ-062:desk 析出与 nodes 更名 machines

## Scenario

总台令(2026-10-24,回归单批 173):prim 3.10.0 命名三分落地(ai-ccoe ADR-0007,main ab34298/8130fc4),desk 新命令收工位/窗格拓扑面(start/close/split/tab/zoom/ws/shell/dev/wt/yolo/trust,与 agents 同实现 alias 期 1 至 2 大版本),machines 收原 nodes 整包(nodes 留 deprecated 别名),agents 收敛消息面(to/wait/inbox/read/keys/mode/reload 加 view)。project-evo 仓同步:desk 新 skill、nodes 改名 machines、agents 瘦身指 desk、行话对齐(工位 = desk、格 = pane、邻格 = 邻 agent)。

本台实弹核对(prim v3.10.0 editable 实装):desk view/tab list/ws/trust 帮助面真跑;machines view/list/status 真跑;agents 面 alias 期拓扑动词仍在(设计内);两笔真坑入档(ws list 旧形被当机标签、machines llms 头仍印 nodes@v3 字样属 prim 侧残留已随回执上报)。顺手件:ctxs --around 真聚焦根修(命中点居中 3000 字加邻块窗,27KB 非全量)实证收讫并记 diary。

点名义务:skill 面与 prim 3.10 命名三分脱节(拓扑动词挂在 agents 面、nodes 旧名当正身、无 desk 载面),候选下全部翻正。

## Criteria

- [x] desk skill 入真源(SKILL.md 45 行级:动词表 12 行、文法含 alias 期与行话对齐、坑表含 ws list 实测坑、references/workspace.md 自 agents 迁入并去 mode/reload 行、references 索引)
- [x] nodes 更名 machines(git mv 保史;frontmatter name/description 换新,触发词 machines 机册节点,nodes 留 deprecated 别名说明;维度分职工句更新;示例命令形实证)
- [x] agents 瘦身:动词表删 start/close,文法行拓扑动词指 desk、mode/reload 留域内联,示例去拓扑行;description 收敛消息面(to/wait/inbox、在场翻台)
- [x] 计数与守卫全同步:两插件十五 skill(dev 三加 evo 十二)、SKILLS 表与 SINGLE_FILE_SKILLS、githooks 断链段十五面、AGENTS/根 README/docs 地图/gates 计数/evo README/双 manifest 与市场清单四面描述、版本 0.18.0
- [x] 顺手件:--around 真聚焦实证(intel tick 命中 3 块加邻窗 27KB);prim 侧残留上报(machines llms 头印 nodes@v3、ws list 旧形)
- [x] 门禁全绿(pytest、check、scan、md-ref-scan 十五面)
