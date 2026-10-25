# S020:gw_logs 术语挖词与词表基线

> 约束术语表 lint(PE-13)的语料方法与基线档案。表源 = zh-lint 词表(批 145 裁撤,git 9189048^ 复原)加 gw_logs 对话语料挖词;产物 = `plugins/dev/scripts/termrules.py`(唯一权威,ENFORCED 与 PENDING 两层);方法面 = dev-doc 技能 term-rules.md。原始语料不进仓(落 /tmp,快照指标见下)。需求线 REQ-064,决策线 ADR-0026。

## 方法

- 引擎:ClickHouse `gw_logs.gwlog`(ctxs 同源;head 表无正文,只用 gwlog);本机只读凭据 `~/.ctx/reader.env`
- 通道:HTTP 8123 主道(客户端证书强制,Basic 道实测被拒 TLS 层)落 ssh 备道(`ssh lan-linux2` + docker clickhouse-client,SQL 走 stdin)[实证: 2026-10-26 两道实跑]
- 切片纪律:全表 5300 万块;`ORDER BY ts` 全序爆内存(ClickHouse memory limit 13 GiB 实测红),去排序;`substringUTF8(payload,1,2000)` 截头 + `rand() % 100 < 5` 抽样 + `LIMIT` 三重限流 [实证: 7 天片首跑 7.8 GiB 未竟,改三板后 13 天片 405 MiB 16.2 万块 90 秒]
- kind 实测:`sse` 4925 万、`client_request` 355 万、`upstream_attempt`、`request_end`;对话正文走 `client_request` [实证: DISTINCT kind 查询]
- 候选提取:种子词频扫(表内词验活)+ CJK 二字组离群(粗筛,需停用词后人工)+ 英文俚语种子表词边界扫 [经验: 三法互补,二字组原始 top 全为常用词(用户、文件、失败),无停用词不可直用]

## 语料实测 2026-10-12 至 2026-10-25 · client_request 5% 抽样 16.2 万块

- 种子词命中(验活):`收口` 4360、`缺省` 2160、`报错` 2124、`进行` 1629、`沉淀` 755、`的话` 375、`拉齐` 249、`入参` 245、`对标` 189、`赛道` 97、`痛点` 64、`出参` 56、`打法` 48、`登陆` 40、`尽快` 37 [实证: 频次扫描]
- 高频黑话候选(仓外活、仓内基线见下):`落地` 3753、`闭环` 3146、`兜底` 2284、`链路` 1143、`打通` 269、`反哺` 185、`串联` 56、`贯穿` 25、`咬合` 21 [实证: 频次扫描]
- 英文黑话:`magic` 591(多为 CLI 旗标名与同名技术惯用语半技术用)、`stuff` 426、`synergy` 71、`hacky` 44、`leverage` 5 [实证: 词边界扫描]

## 仓内基线与分层 · term-lint 首跑 2026-10-26

| 层 | 词(基线命中数) |
| --- | --- |
| ENFORCED zh 禁用 | `加以`、`予以`、`作出`、`做出`、`的话`、`一下`、`尽快`、`众所周知`、`不难看出`、`赋能`、`抓手`、`拉通`、`赛道`、`颗粒度`、`打法`、`组合拳`、`牵头`、`倒逼`、`体感`、`拉齐`、`打通`、`顶层设计`、`底层逻辑`、`出参`、`登陆`、`帐号`、`阀值`、`布署`(均 0 命中) |
| ENFORCED zh 选词 | `单击`、`点选`、`摁`(均 0) |
| ENFORCED en 黑话 | `leverage`、`utilize`、`synergy`、`basically`、`obviously`、`stuff`、`hacky`、`magic`(均 0) |
| PENDING 存量 | `收口` 45、`沉淀` 39、`缺省` 31、`报错` 21、`进行` 10、`对标` 5、`入参` 4、`删掉` 2、`痛点` 2、`点按` 1、`心智` 1、`若干` 1、`闭环` 19、`串联` 2、`反哺` 2、`落地` 0、`兜底` 0、`链路` 0 |
| 弃 | `贯穿`、`咬合`(语料低频且仓内 0,不足立据;`magic` 半技术用留观,命中处多为旗标名,误报风险记档) |

- PENDING 含语料高频但仓基线 0 的 `落地`、`兜底`、`链路`:直接 ENFORCED 不伤本仓,但下游仓活文大概率有存量,按两层政策先 PENDING 示警,收存量后迁 [假设: 分层判定,后批收紧验证]
- `进行` 迁入须排除「进行中/进行后」状态形(仓内 10 命中全为此形待核) [假设: 待逐条核]

## 复现

```bash
uv run plugins/dev/scripts/term-mine.py --since 2026-10-12 --slice 14d \
  --kind client_request --sample 5 --out-dir /tmp/term-mine-2026-10/
uv run plugins/dev/scripts/term-lint.py .            # ENFORCED 层(退出码 1 = 有违规)
uv run plugins/dev/scripts/term-lint.py . --pending  # 加列 PENDING 存量
```
