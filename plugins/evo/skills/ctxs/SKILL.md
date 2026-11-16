---
name: ctxs
description: >-
  对话历史域原语:查已结束的请求与历史对话。view [agent] 看请求头行,
  view <request_id> 看单请求全链(--around/--window),
  search 跨请求全文检索。
  Use when: last request, request_id, transcript search, token cost, 上次请求、
  历史对话、查记录、单请求全文、跨请求搜索。
  不要用于当前屏幕(agents read)或房间历史(streams view)。
---

知识面在本插件 hook_rules(技能直读):按需直读 `plugins/evo/hook_rules/` 下同名与拆件(注入面 2026-11-09 用户令剔除)。
