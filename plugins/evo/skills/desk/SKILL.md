---
name: desk
description: >-
  工位与窗格拓扑原语:开工作台(仓即台)、起停格与分屏切tab、聚焦翻台、信任放行。
  Use when: open workbench, split pane, start agent, 工位、工作台、开台、开格、起格、
  分屏、切tab、关格、聚焦、翻台、信任屏、win 窗口视图。
  不要用于发消息与等回信(走 agents)或机册管理(走 machines)。
---

# desk - evo 工位与窗格域原语

| 动词 | 文法 | 何时用 |
| --- | --- | --- |
| view | `view [机]` | 要看某机格表(裸调用即面) |
| start | `start <名> --kind <类> [--pane 格] [--cwd DIR] [--machine 机]` | 要起带名新格(非标形拒 rc=2;起名全局扫,撞名拒 rc=2) |
| close | `close <id>` | 要关格(优雅退后 shell exit,零击杀) |
| split | `split <id> [--direction right\|down]` | 要在格旁分裂新格 |
| tab | `tab list [机]` / `tab create <机>` / `tab close <机:tab>` | 要管理 tab |
| zoom | `zoom <id>` | 要聚焦某格 |
| ws | `ws <label> [--cwd DIR] [--machine 机]` | 要开工作台(仓即台);裸 `ws` 列本机台面;`ws close <台> [机]` 收台 |
| shell | `shell <机> <仓路径>` | 要在某机某仓开台 shell 格 |
| dev | `dev <机> <仓路径> [--kind 类]` | 要开台并起 agent |
| wt | `wt [机\|wsl] [--title 名]` | win 专属:本窗开 tab 显该机窗格视图 |
| yolo | `yolo [--audit]` / `yolo <id> [--yes]` | 要检测或冷翻四家 CLI 的权限模式 |
| trust | `trust` | 要放行信任屏(全机扫屏按键) |

## 文法

- 裸调用 = view;全局旗标任意槽,以 `desk --llms` 为准
- 与 agents 同实现 alias 期(prim 3.10 起 1 至 2 大版本):两入口等价,新写统一 desk;消息面动词(to/wait/read/keys/mode/inbox)恒在 agents
- 格寻址:`<名>` / `<机>:<名或格>` / `local:<格>`;格操作用格 id,消息用别名(id 三产生式细语义见 `../agents/SKILL.md`)
- 行话(ADR-0007):工位 = 本命令域;格 = pane;邻格 = 同机邻 agent
- reload(同格同 session 重进,重载技能与插件)与 mode(在场声明)仍在 agents 面

## 示例

```bash
desk view
desk start hst-kimi-2 --kind kimi --cwd ~/repos/hst_rs
desk close local:w13:p1
desk split local:w13:p1 --direction down
desk tab list
desk ws
desk shell lan-ubuntu ~/repos/ai-ccoe
desk dev lan-ubuntu ~/repos/pi-rs --kind grok
desk wt wsl --title 台面
desk trust
```

## 坑

| 错 | 对 |
| --- | --- |
| 去 agents 找起格与分屏写法 | 拓扑动词正身在 desk(agents alias 期暂兼容,新写走 desk) |
| start 起名随手敲 | 命名标准 `<台名>-<类型>-<编号>`(细则见 agents skill) |
| reload 找 desk | reload 与 mode 是会话面动词,仍在 agents |
| 空 pane 出现不管 | 空 pane = 异常态(所有 pane 须有 agent);补 agent 或 close 收格 |
| `ws list` 旧形列台 | 3.10 起 `ws` 裸调用即列台;`ws list` 的 list 会被当机标签(报 unknown machine,实测) |

## 接着读

- `../agents/SKILL.md`:id 三产生式、命名标准、信封协议(共享面单一权威源)
- `../machines/SKILL.md`:机册与跨机直透面
