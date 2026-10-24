---
name: agents
description: >-
  给格发指令并事件等回信(to/wait/inbox)、读屏按键、在场与翻台管理。
  Use when: tell, ask, ping, reply, read the screen, wait for a reply, 等回话、读屏、按键、
  派单、私信回执、翻台、在场声明。
  不要用于文件、房间留痕、跨回合任务或工位开格分屏(开格分屏走 desk)。
---

# agents - evo 消息域原语与七原语共享面

| 动词 | 文法 | 何时用 |
| --- | --- | --- |
| view | `view [机]`(族:`machines` 机表、`list [机]` 机读形) | 要全局格表与机册 |
| read | `read <id> [--lines N] [--timeout S]` | 要读某格屏幕或等队友回话(忙则内候) |
| to | `to <id> <文本> [--force]`(prompt 为别名) | 要给某格发一句话指令;投递即镜像 dm 流(回信事件道) |
| wait | `wait [--from <id>] [--timeout S]` | 要事件驱动等回信:阻塞到本格 dm 流新入站即返全文,不再 sleep 盲等;到件 rc=0,超时 rc=1 非 failure(`--json` status=timeout 带监视流键) |
| inbox | `inbox [--from <id>]` | 非阻塞收件单:dm 流入站消息清单(幂等,读不消费) |
| keys | `keys <id> <键>` | 要给某格按键(仅本机与 local: 目标) |

## 文法

- 裸调用 = view;全局旗标任意槽,以 `agents --llms` 为准
- 投递动词统一 `to`;`--force` 任意参数位,跳门控强投
- id 三产生式:`<名>`(全局寻址,本机先) / `<机>:<名或格>` / `local:<格>`;裸 pane id 非法;投递与回信用裸别名,格 id 只用于窗格操作
- 命名标准:`<台名>-<类型>-<编号>`,字母开头禁下划线;编号 = 出生序号,该台该类型不复用(田字只约束创建顺序,非格位)
- 投递判成败:先退出码(0/1/2),再看 `--json` 的 `data.status`(delivered/engine_fail/deferred/stalled)与 CTA;engine_fail 时 stderr 定向清单直出该机在册命名格,照单改投;拒投时信封仍 ok:true
- 事件道:`to` 投递即镜像 dm 流(流名双端 canonical `机:别名` 段),等回信用 `wait` 阻塞或 `inbox` 非阻塞查;看屏才 `read`
- 门控只拒操作对话框(信任屏/权限屏/模式选择)
- 拓扑动词(start/close/split/tab/zoom/ws/shell/dev/wt/yolo/trust)走 `desk` skill(prim 3.10 命名三分,alias 期 agents 暂兼容,新写 desk);`mode <dnd|away|online> [until]`(在场声明,走 shares 键)与 `reload <id>`(翻台重载技能与插件,idle/done 皆可翻,working/blocked 拒 --force 过)仍本域
- 文件走 shares,流走 streams,持久任务走 tasks,实时字节走 pipes,端口映射走 ports,历史对话走 ctxs;共享细语义见本 skill references

## 示例

```bash
agents view
agents read evo-claude --lines 40 --timeout 30
agents to evo-claude "评审请求已递" --json
agents wait --from lan-win:lan-win-claude-1 --timeout 300
agents inbox --from evo-claude
agents keys local:w13:p1 Enter
agents mode dnd 2h
agents reload evo-claude
```

## 坑

| 错 | 对 |
| --- | --- |
| 裸格直写格 id(如 `to w8:p1`) | 无名格用 `local:<格>` 或 `<机>:<格>` |
| 目标 working 就不敢投 | busy 排队不拦,照投;等回信用 `wait` 事件道,要看屏才 `read` |
| 判成败单看信封 ok 字段 | 先看退出码,再看 `data.status` |
| engine_fail 当笼统链路坏,翻 view 逐格找 | stderr 定向清单直出该机在册命名格,照单改用 `机:别名` 再投(错名实测:`lan-mac:lan-mac-claude-1` 即提示 `ray-claude-1`) |
| dm 用 `local:别名` 与 `机:别名` 两写法各开一条流 | dm 流名 canonical 双端 `机:别名` 段,与写法无关(3.9.1 治);跨机一律 `机:别名` 显式 |
| 无名格上 wait/inbox 等回信 | 事件道键退化 `机:格`,正名后旧键消息成孤儿;开机先正名,旧 dm 按 `streams view <旧键>` 显式读 |
| `to` 后 sleep 盲等回信 | `wait --from <别名> --timeout S` 阻塞到件(rc=0 返全文;超时 rc=1、status=timeout,续等即可) |
| 装更插件后不翻台 | `reload <id>` 翻台才生效(旧进程 = 旧技能);回滚裸形时上下文弃,信封 resume 字段披露 |
| 同 cwd 多格投递按格猜发话方 | caller_addr 歧义不猜,退化机名加告警;按名寻址 |
| grok 面信封见单行拍扁 | 收方 TUI 显示怪癖,定稿四行形不降协议(见 deliver-gate 信封节) |

## 接着读

- `references/addressing.md`:id 解析算法、命名标准细则、from 核验,跨机寻址出错时
- `references/deliver-gate.md`:门控判据、status 四态、信封 v2 定稿四行形、代记补收,投递被拒或读信封时
- `references/collab.md`:IM 映射、回执与 ack 惯例、回放与保留策略,交回执或发房间消息时
