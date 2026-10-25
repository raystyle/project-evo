---
id: REQ-063
title: desk 更名 desks 复数对齐与拓扑真视图入面(prim 3.11.0 同步)
status: implemented
priority: must
trace: tests/test_project_evo.py
---

# REQ-063:desk 更名 desks 复数对齐与拓扑真视图入面

## Scenario

总台令(2026-10-25,批 174):prim 3.11.0 复数对齐落地(desks@v3.11 实装,主名 desks、desk 留旧名单字别名,四端在役),project-evo 仓 skill 面同步。用户同日定谳术语:工位/窗格 = pane;工作台/窗台 = workspace(w 编号,一个终端窗);tab = 窗台内页。desks view 升拓扑真视图(窗台 w -> tab -> 工位 pane 三层分组,▍ 焦点工位,活动列 = 终端标题,含非 agent 工位),与 agents view 消息面分职。用户补令:skill 面补命名契约节(四层命名律,含 pane id 尾缀字母无规则实态披露)与空间语义节,作为原语缺陷审查最终版提案的 skill 侧输入。

本台实弹核对(prim v3.11.0 本机实装):`desks --llms` 头行确认 desks@v3.11 主名与 desk 别名注记;`desks view` 真跑确认三层分组输出(w8 窗台 1 tab 2 工位形,▍ 焦点行,pT/p1W 尾缀字母实态);`desks ws` 裸调用列台面、`desks ws list` 仍翻车(list 被当机标签,3.11 未修)、`desks reload` 已收面(帮助文案直出)。

顺手收口:HEAD 77a6599(dev 0.16.1 撤 hook 批)遗留 dev codex manifest 版本漂移(0.16.0)与三个 hook 守卫用例红灯(hooks.json 清空后 KeyError),按该批已落地用户令补齐 manifest 面与空面守卫,门禁复绿。

点名义务:仓库活面(desk 字样与九原语计数)残留陈旧引用,候选下全部翻正;agents/machines skill 批 173 面已到位只核对,仅改 desk 指路词。

## Criteria

- [x] desk 更名 desks(git mv 保史):frontmatter name/description、文内命令前缀全 desks 化;desk 留单字别名注记(prim 3.11.0 主名 desks、别名 desk、四端在役);references 两件同步
- [x] desks view 拓扑真视图入面:窗台 w -> tab -> 工位 pane 三层分组、▍ 焦点工位、活动列 = 终端标题、含非 agent 工位;与 agents view 消息面分职(动词行加坑表双记)
- [x] 术语行入册(用户定谳 2026-10-25):工位/窗格 = pane;工作台/窗台 = workspace(w 编号,一个终端窗);tab = 窗台内页
- [x] 命名契约节与空间语义节入 desks skill:四层命名律(machine/workspace/tab/pane 加 agent 层指路)、pane id 尾缀字母无规则实态披露、方向寻址仅分裂时、邻格与布局查询实态限制
- [x] 守卫与活面全同步:SKILLS 表与正典集(B3 复数律全量成立,desk 单数豁免撤销)、githooks 断链段、AGENTS、根 README 与 evo README(九原语翻十原语)、docs 地图、双 manifest(十一 skill 翻十二)与市场清单四面描述
- [x] 顺手收口:dev codex manifest 同步 0.16.1 与新描述;市场 dev 条目同步;三 hook 用例翻空面守卫(批 105 加批 174 双裁撤不回潮)
- [x] evo 升 0.19.0(改名加新面,minor);门禁全绿(pytest、check、scan、md-ref-scan 十五面)
