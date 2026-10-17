---
name: nodes
description: >-
  节点与窗格原语:herdr machine 机册管理(view/status/add/rename/remove/enable/disable/
  reconnect)、原始窗格操作(run/close/pane 直透)、agent 运行环境面(runtime,骑 ark)。
  Use when: node registry, run in a pane, runtime check, 注册或管理舰队节点、在指定节点
  窗格跑命令或关窗格、检查或对齐某仓 agent 运行环境时;触发词 nodes、机册、节点、窗格、
  pane、runtime、runtimes、ark、环境对齐。
  不要用于 agent 消息与工位操作(走 agents)。
---

# nodes - evo 节点与窗格域原语（第九原语）

| 动词 | 文法 | 何时用 |
| --- | --- | --- |
| view | `view` | 要看机册 + 各节点可达性(list 同面) |
| status | `status [名]` | 要查全量或单机可达态 |
| add | `add <ssh-target> [--label <名>]` | 要注册新节点(herdr 自动装远端并起 server) |
| rename | `rename <名> --label <新名>` | 要改机册标签 |
| remove | `remove <名>` | 要注销节点(远端会话不动) |
| enable/disable | `enable <名>` / `disable <名>` | 要启停某节点路由 |
| reconnect | `reconnect <名>` | 要重连失联节点 |
| run | `run <节点> <格> <命令...>` | 要在指定窗格内跑命令 |
| close | `close <节点> <格>` | 要直关窗格(agent 在跑先 agents close 走优雅退场) |
| pane | `pane <节点> <子面...>` | 要直透 herdr pane 子面(list/get/read/split 等) |
| runtime | `runtime [view|init|check|install|update|doctor|heal|config] [工具...]` | 要查或对齐 agent 运行环境;`--machine <节点>` 跨机经 ssh;`--repo <远端仓路径>` |

## 文法

- 裸调用 = view;全局旗标以 `nodes --llms` 为准
- 寻址:label 或 profile-id 皆收(label 优先);机册真源在 herdr
- 维度分职:nodes = 原始窗格面;agents = 在线 agent 面(启停/检测)
- runtime 栈真源 = 仓根 runtimes.toml(由工作台仓的 agent 自己定,init 出模板);骑 ark,三平台统一契约
- 空 pane = 异常态(所有 pane 须有 agent;agents view 会亮警示行)

## 示例

```bash
nodes view
nodes add ray@10.10.10.7 --label lan-pve
nodes run lan-pve w1:p1 claude
nodes close local w1A:p1
nodes disable lan-mac
nodes enable lan-mac
nodes reconnect lan-ubuntu
nodes pane lan-pve get w1:p1
nodes runtime check
nodes runtime --machine lan-pve --repo ~/repos/pve-harness
```

## 坑

| 错 | 对 |
| --- | --- |
| agent 会话操作走 nodes | agents = agent 面(启停/检测);nodes 只管窗格与机册 |
| `~` 路径跨机直传(被本地 shell 吸收) | 远端路径用绝对形或加引号 |
| 远端装环境手搓 apt | nodes runtime + ark(镜像道,pin 锁定) |
| 非交互面敲 reconnect 求自动重连 | reconnect 需交互终端(herdr 报 requires an interactive terminal);非交互态用 `nodes status <名>` 查可达 |

## 接着读

- `../agents/SKILL.md`:id 文法与信封协议总面(共享面单一权威源)
