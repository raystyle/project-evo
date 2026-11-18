---
name: ctxs
description: >-
  对话历史域原语:查已结束的请求与历史对话。ls [agent] 看请求头行,
  ls <request_id> 看单请求全链(--around/--window),
  search 跨请求全文检索。
  Use when: last request, request_id, transcript search, token cost, 上次请求、
  历史对话、查记录、单请求全文、跨请求搜索。
  不要用于当前屏幕(hc read)或房间历史(streams ls)。
---

# ctxs 对话历史域(prim v5 五入口)

- `ls [agent] [--limit N] [--since <ts>] [--before <ts>]` 请求头行(时间/模型/token/耗时/request_id;时间窗直裁分区,翻页找目标日用)
- `ls <request_id> [--around <词>] [--window N]` 单请求全链(--around 只出命中块加邻块 N;show 与 view 已并入 ls,2026-11-16/11-18)
- `search <词> [--term <词>]... [--limit N] [--days N] [--since <ts>] [--before <ts>]` 跨请求全文,多词 OR,每行带命中片段;--days 扫描窗默认 1 天(慢查询防护),宽窗用 --since/--before 分片
- 窗口:头行 365 天、正文 180 天;词至少 2 字符(UTF-8 计);request_id 从 ls 尾列或 search 首列取
- 判读:「头行:未落」是正常降级非 not_found;空表带表头即连接通
- 引擎 ClickHouse gw_logs(head 表索引加 gwlog 表正文);实时屏走 hc read(agents 域已退役),ctxs 只管已结束请求;语料批量导出走 ClickHouse 直连(片段面不管)
- 示例:`ctxs ls`;`ctxs ls 0192a0f0-xxxx --around "挂死" --window 1`;`ctxs search "panic"`
- 旗标全集以 `ctxs --llms` 为准
