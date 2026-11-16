---
patterns: [工位, 工位表, 拓扑, 看拓扑, 起格, 关格, 空格, desks, 分屏, 切tab, 聚焦, wt]
---

## desks 工位拓扑操作指导(prim v5 三动词)

- 三动词:`view [host]`(全量工位表:机/格/类/态/活动,裸调用同,--json 出行形)/ `start <名> --kind <类> [--cwd DIR] [--machine 机]`(起 agent,命名标准形校验)/ `close <id>`(优雅退场)
- 空 pane = 异常态,须 `start` 补 agent 或 `close` 收格
- 已退役(调用回 usage 退 2 指新道):split、tab、zoom、wt(树形拓扑归 herdr-app mod GUI);desk 单字别名删除;shell/dev/workbenches 等开台面走 agents 面(见 desks-workspace)
- 寻址:裸别名 > `机:别名` > `机:格`;空间关系从 view 人读
- 消息与等回信走 agents;机册管理走 machines
