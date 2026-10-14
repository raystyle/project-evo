---
name: ctx
description: >-
  对话历史检索原语:查任何 agent 跑过的请求(最近请求头行、单请求原文、跨请求全文搜词)。
  Use when 查历史对话、回溯对话细节、按 request_id 调单次请求原文、跨请求搜关键词、看某
  agent 最近请求开销时;触发词 ctx、历史对话、对话历史、回溯、检索、全链、档案、
  request_id、snip、gw_logs、gwlogs。
---

# ctx - evo 对话历史域原语

| 动词 | 文法 | 何时用 |
| --- | --- | --- |
| view | `view [agent] [--limit N]` | 要最近请求的头行(时间/模型/token/耗时/request_id) |
| show | `show <request_id> [--around <词>] [--window N]` | 要单请求原文;`--around` 只看命中块±N 邻块 |
| search | `search <词> [--term <词>]... [--limit N]` | 跨请求全文搜词,多词 OR,行带 snip 片段 |

## 文法

- 裸调用 = view;窗口:head 365 天,正文 180 天
- 词至少 2 字符(UTF-8 计)
- 旗标全集与默认值以 `ctx --llms` 为准

## 示例

```bash
ctx view --limit 3
ctx view <agent> --limit 5
ctx show <request_id> --around <词> --window 1
ctx search --term <中文词> --term <ascii词> --limit 5
```

## 坑

| 错 | 对 |
| --- | --- |
| 嵌套一把梭取 rid | 先 `search --limit 1` 或 `view` 取 rid:rid = view 头行末列,search 行首列 |
| show 报「头行:未落」当 not_found | 头行未落正文已在属正常降级,接着读正文块;双无记录才 not_found |
| 表空当链路断 | 零行但表头出即链路通,数据候采集入库 |

## 分工

实时屏用 agents read,本命令只查历史。

## 接着读

- 共享规则与实装差异表:`../agents/references/commands.md`,跨 skill 投递或协作时
