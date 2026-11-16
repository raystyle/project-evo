---
patterns: [机册, 机器, 节点, 注册节点, 重连, pane 直透, runtime, ark, 环境对齐, machines]
---

## machines 机册域操作指导(prim v5)

- 册表:`machines view`(机/态/靶/版本四列,state 字段即可达性;裸调用同);`add <ssh-target> [--name <名>] [--install]`(注册节点,--install 远端缺 hc 即装);`reconnect <机名>`(hc machine login 直通)
- 直透:`run <节点> <格> <命令...>`(格内跑命令,hc send)/ `close <节点> <格>`(直关格;agent 在跑先 agents close 优雅退)
- 运行环境:`runtime [view|init|check|install|update|doctor|heal|config] [工具...]`,骑 ark;栈真源 = 仓根 runtimes.toml;`--machine <节点>` 跨机经 hc exec --on
- 已退役(调用回 usage 退 2 指新道):status(并入 view,state 字段)/ list(清单即 view)/ runtimes(复数别名删,单数 runtime)/ rename、remove(直令 hc machine)/ enable、disable(机册无启停态)/ pane(拓扑归 mod GUI)
- 机册裁定:常驻 hc 节点进册,机册外节点不进册,ssh 行为不变
- 坑:远端路径用绝对形或加引号(`~` 被本地 shell 吸收);reconnect 需交互终端,非交互态用 `machines view` 看 state;装环境走 runtime 加 ark 镜像道,不手搓 apt
- agent 消息走 agents;工位拓扑查看走 desks
