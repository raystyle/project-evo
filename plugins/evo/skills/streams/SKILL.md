---
name: streams
description: >-
  streams 原语(prim v3 流域):S2 形持久流(引擎 s5,流即房间),播报、留痕、交回执、
  房间消息。append <流> <消息> 落流(自动带 host 前缀,勿手写裸 s5 append),view
  读流(-n 调量、--from <seq> 回放、--resume 从机内 cursor 续读),to <id> <流>
  <消息> 定向递流(先入流再知会,取用行 = s5 tail;拒投不写流不保原文,要留消息改走
  append 或 --force 重发)。room/ 与 dm/ 保留 14 天,tasks/shared 30 天;
  fleet 流 = 全舰队回执主频道。共享规则(id、门控、信封)见 evo:agents skill(相对链 ../agents/)。契约单一真源 = ai-ccoe 仓 plugins/CONTRACT.md。
  Use when 要往流交回执或广播、播报进展、留痕、发房间消息、私信(dm/ 专线)、回放或
  续读历史消息、查流列表时;触发词 streams、流、回执、房间、广播、播报、留痕、私信、
  dm、频道、append、tail、view、cursor、回放、from、resume、S2。
---

# streams - evo 流域原语

**定位**:五原语的流域:S2 形持久流,引擎 s5,流即房间。播报、回执、留痕、房间消息的主载体。共享面(id 三产生式、门控 v2、信封 v2、status 四态、差异表)在 `../agents/references/`,本篇只持域面。

## 动词面

| 动词 | 义 |
| --- | --- |
| `view [流名]` | 流表;具名时尾读(默认最近 100 行) |
| `append <流> <消息>` | 落流,自动加 `<host>\|` 前缀 |
| `to <id> <流> <消息> [--force]` | 定向递流 = 先入流再投信封知会 |

- 读控制:`-n N`/`--lines N` 调量;`--from <seq>` 从序号回放(全量 = `--from 0`);`--resume` 从机内 cursor 续读(cursor 落 `~/.local/state/prim/cursor/<流名>`,机内不共享) [实证]
- 裸调用 = view,exit 0;全局旗标与文法见 `../agents/SKILL.md` 二节

## DELIVER 语义

- `to` = 先 append 入流再向目标投信封 v2,域字段 stream,取用行 = `s5 tail <流>`
- **拒投(操作对话框)不写流不保原文**:代记只记流名与待递;要留消息改走 `streams append`(OPERATE 无门控)或 `--force` 重发 [实证]

## 惯例与坑

- **回执主频道 = fleet 流**:批次完工交回执走 `streams append fleet "<一句话>"`(host 前缀自动带;判例:批 132 手写裸 s5 append 前缀误书机名,以新行更正);收方 tail 取阅,取阅不回写
- 一行一事;append-only:发出去不撤回,更正 = 追加新行注明对象
- 私信 = `dm/<a>/<b>` 双方名字典序专线;房间 = `room/` 前缀(room/deferred 代记、room/pipe-live 管道在册)
- 保留策略(契约面):room/ 与 dm/ 14 天、tasks/shared 30 天;要长留的内容上 shares 键
- 默认尾读只最近 100 行,要全量记得 `--from 0`
