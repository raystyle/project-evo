---
name: agents
description: >-
  消息域原语与六原语共享面:告诉或委派 agent 干活、读屏等回话、按键、在场声明、工位
  管理、查机器(项目协作规则文件 AGENTS.md 不属本面)。Use when 委派某格干活、找格读屏、
  发消息或按键、查在场、开工作台调窗格布局、翻台重载、查在网机器时;触发词 agents、
  告诉、委派、让干、找格、读屏、窗格、邻居、工作台、tab、table、翻台、reload、关格、
  派单、门控、信封、deferred、命名标准、presence、machines。
---

# agents - evo 消息域原语与六原语共享面

| 动词 | 文法 | 何时用 |
| --- | --- | --- |
| view | `view [机]` | 要全局格表(HOST、NAME、PANE、STATUS、KIND、CWD) |
| machines | `machines` | 要在网机表与可达性 |
| list | `list [机]` | 要格表机读形 |
| read | `read <id> [--lines N] [--timeout S]` | 要读某格屏幕或等队友回话(忙则内候) |
| to | `to <id> <文本> [--force]` | 要给某格发一句话指令(prompt 为别名) |
| keys | `keys <id> <键>` | 要给某格按键(仅本机与 local: 目标) |
| mode | `mode <dnd|away|online> [until]` | 要声明本机在场状态 |
| start | `start <名> --kind <类> [--pane 格] [--cwd DIR] [--machine 机]` | 要起一个带名新格 |
| ws | `ws <label> [--cwd DIR] [--machine 机]` | 要开工作台;`ws list [机]` 列台;`ws close <台> [机]` 收台 |
| shell | `shell <机> <仓路径>` | 要在某机某仓开台 shell 格 |
| dev | `dev <机> <仓路径> [--kind 类]` | 要开台并起 agent |
| split | `split <id> [--direction right\|down]` | 要在格旁分裂新格 |
| tab | `tab list [机]` / `tab create <机>` / `tab close <机:tab>` | 要管理 tab |
| zoom | `zoom <id>` | 要聚焦某格 |
| close | `close <id>` | 要关格(优雅退后 shell exit,零击杀;末格收台) |
| reload | `reload <id>` | 要翻台重载技能与插件(同格同 session 重进) |
| wt | `wt [机\|wsl] [--title 名]` | 要在 win 本窗开 tab 显该机 herdr 视图 |
| trust | `trust` | 要放行信任屏(全机扫屏按键) |
| sync | `sync [机]` | 要补注册机册 |
| prompt | `prompt` = `to` 别名 | 同 to |

## 文法

- 裸调用 = view;全局旗标任意槽,以 `agents --llms` 为准
- 投递动词统一 `to`;`--force` 任意参数位,跳门控强投
- id 三产生式:`<名>`(全局寻址,本机先) / `<机>:<名或格>` / `local:<格>`;裸 pane id 非法
- 命名标准:`<工作台标签>-<agent类型>-<编号>`,编号即田字顺时针窗格位,满四开 tab 续编;起名带校验
- 投递判成败:先退出码(0/1/2),再看 `--json` 的 `data.status`(delivered/engine_fail/deferred/stalled)与 CTA;拒投时信封仍 ok:true
- 门控只拒操作对话框(信任屏/权限屏/模式选择);busy 排队不拦

## 示例

```bash
agents view
agents machines
agents list lan-win
agents read evo-claude-1 --lines 40 --timeout 30
agents to evo-claude-1 "评审请求已递" --json
agents keys local:w8:p1 Enter
agents mode dnd 2h
agents start hst-kimi-2 --kind kimi --cwd ~/repos/hst_rs
agents ws evo
agents ws list
agents ws close evo
agents shell lan-win "D:\\repos\\ai-ccoe"
agents dev lan-ubuntu ~/repos/pi-rs --kind grok
agents split local:w8:p1 --direction down
agents tab list
agents tab create lan-win
agents tab close lan-win:2
agents zoom local:w8:p1
agents close local:w9:p4
agents reload evo-claude-1
agents wt wsl --title herdr
agents trust
agents sync
```

## 坑

| 错 | 对 |
| --- | --- |
| 裸格直写格 id(如 `to w8:p1`) | 无名格用 `local:<格>` 或 `<机>:<格>` |
| 目标 working 就不敢投 | busy 排队不拦,照投;等回话用 `read` 忙候 |
| 判成败单看信封 ok 字段 | 先看退出码,再看 `data.status` |
| 装更插件后不翻台 | `reload <id>` 翻台才生效(旧进程 = 旧技能);回滚裸形时上下文弃,信封 resume 字段披露 |
| 同 cwd 多格投递按格猜发话方 | caller_addr 歧义不猜,退化机名加告警;按名寻址 |

## 分工

文件走 shares,流走 streams,持久任务走 tasks,实时字节走 pipes,历史对话走 ctx;共享细语义见本 skill references。

## 接着读

- `references/addressing.md`:id 解析算法、命名标准细则、from 核验,跨机寻址出错时
- `references/deliver-gate.md`:门控判据、status 四态、信封 v2 三行形、代记补收,投递被拒或读信封时
- `references/collab.md`:IM 映射、回执与 ack 惯例、回放与保留策略,交回执或发房间消息时
