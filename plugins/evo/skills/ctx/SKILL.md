---
name: ctx
description: >-
  ctx 原语(prim v3.1.0 对话历史域):agent 请求全链检索的历史档案面(引擎 ClickHouse
  gw_logs,lan-linux2 gwlogs 实例;查询走 ssh 道进容器内 client,免证书面)。动词三枚:
  view [agent] [--limit N] 出最近请求头行(时间/模型/token/耗时/request_id),show
  <request_id> 出单请求头行加正文块(每块截 4000 字),search <关键词> [--limit N] 跨请求
  全文检索。窗口:head 365 天,正文 180 天。与 agents read 分工 = read 实时屏,ctx 历史
  档案。共享规则(id、门控、信封)见 evo:agents skill(相对链 ../agents/)。契约单一
  真源 = ai-ccoe 仓 plugins/CONTRACT.md(v3.1.0,七节批次记)。
  Use when 要查历史对话、回溯任何 agent 对话细节、按 request_id 调单次请求原文、跨请求
  全文搜关键词、看某 agent 最近请求开销(token、耗时、模型)时;触发词 ctx、历史对话、
  对话历史、回溯、检索、全链、档案、请求、request_id、正文、view、show、search、
  ClickHouse、gw_logs、gwlogs。
---

# ctx - evo 对话历史域原语

**定位**:六原语的对话历史域:agent 请求全链检索的历史档案。引擎 ClickHouse gw_logs(lan-linux2 gwlogs 实例),查询走 ssh 道进容器内 client,免证书面。共享面(id 三产生式、门控 v2、信封 v2、status 四态、差异表)在 `../agents/references/`,本篇只持域面。

## 动词面

| 动词 | 义 |
| --- | --- |
| `view [agent] [--limit N]` | 最近请求头行:时间、模型、token、耗时、request_id;带 agent 名即过滤该 agent |
| `show <request_id>` | 单请求全档:头行加正文块,每块截 4000 字 |
| `search <关键词> [--limit N]` | 跨请求全文检索 |

- 裸调用 = view,exit 0;保留动词 show 与 search 由本域引入(全局保留表见 `../agents/SKILL.md` 二节)
- 窗口:head 365 天,正文(gwlog)180 天;更早档案已过期不在检索面

## 分工与链路

- 与 agents read 分工:read = 实时屏(对方现在在跑什么),ctx = 历史档案(对方跑过什么)
- 数据源 = vector 采集入库;采集端未起或未入库的时段,检索面为空属正常(表头出即链路通)

## 坑

- ssh 凭据按端配:查询走 ssh 道进 lan-linux2 容器,端上无该机凭据即 engine_fail 退 1(错误原文 stderr) [实证:批 149 本机实测,lan-ubuntu 无 lan-linux2 凭据拒 publickey]
- request_id 形如 `0192a0f0-xxxx`,取自 view 头行再喂 show;手拼无效
