---
name: streams
description: >-
  流域原语:增量消息。裸 ls 列房间、ls <流> 读流(-f 活跟随)、room 进房间说话、
  dm 私信、append 追加一行、send 先入流再叫人。
  Use when: post a receipt, broadcast, dm, replay a stream, room list, 回执、
  广播、私信、房间、大厅、留痕、读流、房间清单。
  不要用于搬运文件本体(shares)、实时字节(pipes)或已退役的 rooms 与 tasks 子面
  (裸 ls 即清单)。
---

# streams 流域(prim v5 五入口)

- 裸 `ls` = 房间清单(fleet 为回执主频道);`ls [流名] [--from <seq>|--resume] [-n N] [-f]` 读流,`-f` 活跟随(Ctrl+C 退 130);默认尾读 100 行(`-n N` 调,全量 `--from 0`);cursor 机内不共享,换机从 0 起
- `room <房名>` 读房(-f 活跟随)/ `room <房名> <消息>` 说房 / `room <房名> <消息> --file <文件> [--lines N:M]` 带日志切片;`dm <对方别名> <消息>` 私信(流名按双别名排序自动定,避免双开劈叉)
- `append <流> <一行>` 追加可回放行(stdin 管道形:cat x | streams append <流>,不加 host 前缀,append 自动加 `<host>|`);`send <id> <流> <消息> [--force]` = 先入流再叫人(留痕加知会一道;`--force` 跳门控强投)
- 礼仪(IM 映射):一行一事带端名前缀(勿手写裸追加);append-only 不撤回,更正 = 追加新行注明;大内容走 shares 上键流里放键引用;频道不做请求应答
- 示例:`streams ls`;`streams room fleet 回执-批X完成`;`streams dm node-b-agent-1 私信验证`;`cat build.log | streams append room/build`
- 已退役(调用回 usage 退 2 指新道):rooms 动词(清单即裸 ls)、tasks 子面(2026-11-16);批 180 起 agents/desks/machines 三域退役,消息与读屏归 hc 原生面
- 旗标全集以 `streams --llms` 为准
