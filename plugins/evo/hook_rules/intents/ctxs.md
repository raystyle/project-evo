---
patterns: [last request, request_id, transcript, token cost, 上次请求, 历史对话, 查记录, ctxs, 全链检索, 单请求全文, 跨请求搜索]
---

## ctxs 对话历史域操作指导(prim v5)

- `view [agent] [--limit N] [--since <ts>] [--before <ts>]` 请求头行(时间/模型/token/耗时/request_id;时间窗直裁分区,翻页找目标日用)
- `view <request_id> [--around <词>] [--window N]` 单请求全链(--around 只出命中块加邻块 N;show 动词已并入 view,2026-11-16)
- `search <词> [--term <词>]... [--limit N] [--days N] [--since <ts>] [--before <ts>]` 跨请求全文,多词 OR,每行带命中片段;--days 扫描窗默认 1 天(慢查询防护),宽窗用 --since/--before 分片
- 窗口:头行 365 天、正文 180 天;词至少 2 字符(UTF-8 计)
- request_id 从 view 尾列或 search 首列取;「头行:未落」是正常降级非 not_found;空表带表头即连接通
- 引擎 ClickHouse gw_logs(head 表索引加 gwlog 表正文);实时屏走 agents read,ctxs 只管已结束请求
- 语料批量导出不走 ctxs(片段面),走 ClickHouse 直连(reader.env 只读道)
