---
name: desks
description: >-
  工位与窗格拓扑原语:开工作台(仓即台)、起停格与分屏切tab、聚焦翻台、信任放行、拓扑真视图。
  Use when: open workbench, split pane, start agent, 工位、工作台、窗台、开台、开格、起格、
  分屏、切tab、关格、聚焦、翻台、信任屏、win 窗口视图、看拓扑、窗台工位分组视图。
  不要用于发消息与等回信(走 agents)或机册管理(走 machines)。
---

# desks - evo 工位与窗格域原语

| 动词 | 文法 | 何时用 |
| --- | --- | --- |
| view | `view [机]` | 要看拓扑真视图:窗台 w -> tab -> 工位 pane 三层分组,▍ 焦点工位,活动列 = 终端标题,含非 agent 工位(裸调用即面) |
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

- 裸调用 = view;全局旗标任意槽,以 `desks --llms` 为准
- 主名 desks(prim 3.11.0 实装,ADR-0007+0008 复数对齐):desk 为旧名单字别名,四端在役仍可用,新写统一 desks
- 与 agents 同实现 alias 期(prim 3.10 起 1 至 2 大版本):两入口等价,新写统一 desks;消息面动词(to/wait/read/keys/mode/inbox)恒在 agents
- 术语行(用户定谳 2026-10-25):工位/窗格 = pane(p1、p1W);工作台/窗台 = workspace(w 编号,一个终端窗);tab = 窗台内页
- 格寻址:`<名>` / `<机>:<名或格>` / `local:<格>`;格操作用格 id,消息用别名(id 三产生式细语义见 `../agents/SKILL.md`)
- 行话(ADR-0007):工位 = 本命令域;格 = pane;邻格 = 同机邻 agent
- reload(同格同 session 重进,重载技能与插件)与 mode(在场声明)仍在 agents 面

## 命名契约(四层,实态披露)

- machine 层:机册 label(herdr 真源,如 local、lan-win、lan-mac);跨机窗台恒 `机:w13` 限定形
- workspace 层:机内 w 编号(终端窗序号,字母数字递增: w8、w13、w1G);人读名 = 仓即台(ws 按仓路径开台,view 台面列 WORKBENCH 路径)
- tab 层:窗台内页,t 编号(t1、t2),无独立人读名
- pane 层:p 加编号(p1、p2、p25);尾缀字母(p1W 的 W、pT 的 T)为窗格系统指派,**无词义规则**,勿猜语义、勿当稳定键引用
- agent 层:工位上的 agent 用 `<台名>-<类型>-<编号>` 命名标准(唯一权威源在 agents skill);工位 id 与 agent 名是两套键,操作格用 pane id、投递用别名

## 空间语义

- 方向寻址仅分裂时:`split <id> --direction right|down` 相对被分裂格;无绝对方位词
- 邻格 = 同机邻 agent(ADR-0007);布局真视图 = `view`(窗台 -> tab -> 工位三层分组即空间排布),聚焦单格 = `zoom <id>`
- 实态限制:无程序化邻格查询与布局变换命令(仅 split 单步分裂);空间关系只能从 view 人读,提案改进走 prim 域

## 示例

```bash
desks view
desks start hst-kimi-2 --kind kimi --cwd ~/repos/hst_rs
desks close local:w13:p1
desks split local:w13:p1 --direction down
desks tab list
desks ws
desks shell lan-ubuntu ~/repos/ai-ccoe
desks dev lan-ubuntu ~/repos/pi-rs --kind grok
desks wt wsl --title 台面
desks trust
```

## 坑

| 错 | 对 |
| --- | --- |
| 去 agents 找起格与分屏写法 | 拓扑动词正身在 desks(agents alias 期暂兼容,新写走 desks) |
| start 起名随手敲 | 命名标准 `<台名>-<类型>-<编号>`(细则见 agents skill) |
| reload 找 desks | reload 与 mode 是会话面动词,仍在 agents |
| 空 pane 出现不管 | 空 pane = 异常态(所有 pane 须有 agent);补 agent 或 close 收格 |
| `ws list` 旧形列台 | 3.10 起 `ws` 裸调用即列台;`ws list` 的 list 会被当机标签(报 unknown machine,实测) |
| 找 agents view 看拓扑分组 | `desks view` 是拓扑真视图(窗台 -> tab -> 工位三层);agents view 是消息面格表,分职不同 |

## 接着读

- `../agents/SKILL.md`:id 三产生式、命名标准、信封协议(共享面单一权威源)
- `../machines/SKILL.md`:机册与跨机直透面
