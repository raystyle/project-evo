---
patterns: [开工作台, ws, shell 开台, dev 开台, wt, 旗标, 工位族, zoom, sync, trust 放行]
---

## desks 工位族动词细则

- `ws <label> [--cwd DIR] [--machine 机]` 开台;裸 `ws` 列本机台面;`ws close <台> [机]` 收台
- `shell <机> <仓路径>` 某机某仓开 shell 格;`dev <机> <仓路径> [--kind 类]` 开台并起 agent
- `split <id> [--direction right|down]` 分裂新格;`tab list/create/close` 管 tab;`zoom <id>` 聚焦
- `wt [机|wsl] [--title 名]` win 专属窗格视图;`trust` 放行信任屏(全机扫屏按键);`sync [机]` 补注册机册
- mode 与 reload 在 agents 面;旗标全集以 `desks --llms` 为准
- 示例:`desks shell lan-ubuntu ~/repos/ai-ccoe`;`desks dev lan-ubuntu ~/repos/pi-rs --kind grok`;`desks split local:w13:p1 --direction down`;`desks wt wsl --title 台面`
