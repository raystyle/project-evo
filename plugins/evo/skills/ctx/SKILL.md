---
name: ctx
description: >-
  ctx 原语(prim v3.1.3 对话历史域):agent 请求全链检索的历史档案面(引擎 ClickHouse
  gw_logs,lan-linux2 gwlogs 实例)。检索道 = 直连 https 8123 主道(双闸 = client 证书
  TLS 层加 basic ctx_reader SELECT-only;凭据环境变量 CTX_URL/CTX_USER/CTX_PASSWORD
  优先,缺省读 ~/.ctx/reader.env 六键 600),ssh 道兜底(无凭据或直连败自动落,容器内
  client)。动词三枚:view [agent] [--limit N] 出最近请求头行(时间/模型/token/耗时/
  request_id);show <request_id> [--around <词>] [--window N] 出单请求全档,--around
  只出命中块±N 邻块(命中块为命中点居中 3000 字,SQL 侧全文匹配突破块截断);search
  <词> [--term <词>]... [--limit N] 跨请求全文多词 OR,每行带命中片段 snip 列。窗口:
  head 365 天,正文 180 天;词至少 2 字符(UTF-8 计)。与 agents read 分工 = read 实时屏,
  ctx 历史档案。共享规则见 evo:agents skill(相对链 ../agents/)。契约单一真源 =
  ai-ccoe 仓 plugins/CONTRACT.md(七节批次记)。
  Use when 要查历史对话、回溯任何 agent 对话细节、按 request_id 调单次请求原文、跨请求
  全文搜关键词、看某 agent 最近请求开销(token、耗时、模型)时;触发词 ctx、历史对话、
  对话历史、回溯、检索、全链、档案、请求、request_id、正文、view、show、search、
  ClickHouse、gw_logs、gwlogs。
---

# ctx - evo 对话历史域原语

**定位**:agent 请求全链检索的历史档案。引擎 ClickHouse gw_logs(lan-linux2 gwlogs 实例);检索道 = 直连 https 8123 主道(双闸:client 证书 TLS 层加 basic ctx_reader SELECT-only;凭据 `CTX_URL/CTX_USER/CTX_PASSWORD` 优先,缺省读 `~/.ctx/reader.env` 六键 600),ssh 道兜底(直连败自动落)。共享面在 `../agents/references/`。

## 动词面

| 动词 | 义 |
| --- | --- |
| `view [agent] [--limit N]` | 最近请求头行:时间、模型、token、耗时、request_id |
| `show <request_id> [--around <词>] [--window N]` | 单请求全档;`--around` 只出命中块±N 邻块,命中点居中 3000 字 |
| `search <词> [--term <词>]... [--limit N]` | 跨请求全文多词 OR,每行带命中片段 snip |

- 裸调用 = view,exit 0;窗口:head 365 天,正文 180 天
- 与 agents read 分工:read = 实时屏,ctx = 历史档案
- 示例:`ctx search --term 挂死 --term ensure_ascii`;`ctx show <rid> --around "挂死" --window 1`

## 坑

- 词至少 2 字符(UTF-8 计),单字词 usage 拒
- 嵌套取 rid:先 `--limit 1` 再 show;rid = view 头行末列(f8)或 search 行首列(f1)
- 在途请求 show 出「头行:未落」加正文块属正常降级;双无记录才 not_found
