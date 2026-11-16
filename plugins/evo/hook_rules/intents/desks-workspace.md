---
patterns: [开工作台, workbenches, shell 开台, dev 开台, 开台, 工作台清点]
---

## 开台与工作台细则(prim v5 归 agents 面)

- `agents workbenches [机]` 工作台清点:home 加 ~/repos/* 各 git 仓加 origin
- `agents shell <机> <仓路径>` 某机某仓起 shell 格回址;`agents dev <机> <仓路径> [--kind 类]` 起 agent 于该仓(启动后阻塞检测)
- `agents start <名> --kind <类> [--cwd DIR] [--machine 机]` 起格:命名标准形 台名-类型-编号(字母开头禁下划线),全舰队唯一扫;kind 面 = claude/codex/grok/kimi/pi
- 已退役:desks split/tab/zoom/wt 与 `ws` 开台动词(拓扑归 herdr-app mod GUI,调用回 usage 退 2 指新道)
- mode 与 reload 恒在 agents 面;旗标全集以 `agents --llms` 为准
- 示例:`agents dev lan-ubuntu ~/repos/ai-ccoe`;`agents shell lan-pve ~/repos/pi-rs`;`agents workbenches lan-win`
