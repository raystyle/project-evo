---
patterns: [回执, 群聊, 广播, 私信, 回放, replay, broadcast, dm, streams, 留痕, 房间, 大厅]
---

## streams 流域操作指导(prim v5)

- 裸 `view` = 房间清单(fleet 为回执主频道);`view <流名> [-n N] [-f] [--from <seq>|--resume]` 读流,`-f` 活跟随(Ctrl+C 退 130)
- `room <房名>` 读房(-f 活跟随)/ `room <房名> <消息>` 说房 / `room <房名> <消息> --file <文件> [--lines N:M]` 带日志切片;`dm <对方别名> <消息>` 私信(流名按双别名排序自动定)
- `append <流> <一行>` 追加可回放行(stdin 管道形:cat x | streams append <流>,不加 host 前缀,append 自动加 `<host>|`);`to <id> <流> <消息> [--force]` = 先入流再叫人(留痕加知会一道,免 room 加 agents to 双发)
- 礼仪:append-only 不撤回,更正 = 追加新行注明;大内容走 shares 上键流里放键引用;频道不做请求应答
- 已退役(调用回 usage 退 2 指新道):rooms 动词(清单即裸 view,命名与 agents view 对齐)、tasks 子面(钉任务走 agents to)
- 不要用于:搬运文件本体(走 shares)
