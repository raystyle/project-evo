---
patterns: [tell, ask, ping, reply, inbox, 等回话, 等回信, 读屏, 按键, 派单, 私信, 回执, 在场, to, wait, read, keys, mode, reload, trust, yolo, 起格, run, shell, dev]
---

## agents 消息域操作指导(prim v5 十五动词)

- 消息面:`to <id> <文本> [--force]`(自由文投递,门控拒投代记 room/deferred);`wait [--from <id>] [--timeout S]`(阻塞等新入站信封,事件道);`inbox [--from <id>]`(非阻塞收件单);`read <id> [--lines N] [--timeout S]`(读屏,working 时内候到闲)
- 生命周期:`start <名> --kind <类> [--cwd DIR] [--machine 机]`(命名标准形 台名-类型-编号,字母开头禁下划线,全舰队唯一扫);`close <id>`(优雅退:/exit 后 shell exit,格自消);`reload <id>`(同格同 session 重进,插件更新后必做)
- 开台面:`shell <机> <仓路径>` 起该机 shell 格;`dev <机> <仓路径> [--kind 类]` 起 agent 于该仓;`workbenches [机]` 工作台清点(home 加 ~/repos/* 仓加 origin)
- 在场与杂项:`mode <dnd|away|online> [until]`(presence 走 shares 键);`trust`(信任屏放行);`yolo [--audit] | yolo <id> [--yes]`(四家 CLI 检测与冷翻);`run <id> <命令...>`(格内跑命令);`keys <id> <键>...`(按键一次多发)
- id 三产生式:裸别名(消息面唯一推荐)> `机:别名` > `机:格`;`local:格` 仅本机调试
- 已退役(调用回 usage 退 2 指新道):list(并入 view --json)、machines(machines view)、sync(hc machine add --install)、split、tab、zoom、wt(拓扑归 mod GUI)
- 不要用于:文件(shares)、房间留痕(streams)、工位拓扑查看(desks)
