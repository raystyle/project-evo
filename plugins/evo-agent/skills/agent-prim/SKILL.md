---
name: agent-prim
description: >-
  舰队互操作五原语操作面(prim v3),代理操作唯一面(herdr 技能已进淘汰序,herdr CLI
  退役为引擎):五命令 agents/shares/streams/tasks/pipes,文法 = 全局旗标加动词加位置
  参数,投递动词统一 to;id 三产生式(裸名全局寻址、机:名或格、local: 前缀,裸 pane
  id 非法);隐式路由 local 与 --machine 零感知,任何端点同一文法;投递与收件三反射
  (投递只看 status 与 CTA、收件 agents read 自带忙候与超时、拒投自动代记 deferred
  补收);门控 v2 = TUI 实况判标族(操作对话框拒投,busy 排队不拦);status 四态信封
  (delivered/engine_fail/deferred/stalled);协作惯例(流即房间、DELIVER 即 @、dm/
  与 room/ 前缀、agents view 即 presence、mode 自声明、回执走 streams append fleet、
  --from/--resume 回放)。契约单一真源 = ai-ccoe 仓 plugins/CONTRACT.md,本 skill 只
  路由不复述;与 agent-s5 分工 = s5 是引擎命令面,五原语是骑在其上的协议面。
  Use when 要跨机找格读屏发提示、读队友格等回话、把文件交给指定 agent、往流交回执或
  播报、设别的格所在项目的持久任务、开实时管道、开工作台起格调布局时;触发词
  agent-prim、五原语、原语、prim、agents、shares、streams、tasks、pipes、to、投递、
  门控、拒投、deferred、代记、force、强投、四态、信封、status、收件、忙候、
  timeout-working、判标、mode、presence、隐式路由、machine、房间、room、dm、取用行、
  回执、回放、cursor、from、resume、舰队互操作、唯一操作面。
---

# agent-prim - evo-agent 舰队互操作五原语

**定位**:舰队(多机多格 agent)互操作协议的操作面,代理操作唯一面(用户令 2026-10-13:既有 herdr 技能进淘汰序,herdr CLI 退役为引擎,窗格、工位、投递、读屏操作面一律本 skill)。五命令各管一域,同构文法;DELIVER 自带门控与代记,消息不静默丢失。契约唯一真源 = ai-ccoe 仓 `plugins/CONTRACT.md`,本 skill 蒸馏速览加路由,不复述契约全文;契约演进以真源为准,本 skill 随批对齐。

**版本对齐**:契约五节加五a/b/c/d(2026-10-13 参数规范批,v3.0 蓝图);本机实装 prim 3.0.0a1 R1 修件后实态(2026-10-13:R0 四件加 R1 三件 = 斜杠流名 cursor 崩修、手册补 -n、mode 实装;ai-ccoe main d524d7c) [实证:本机 uv 工具重装自仓源,五命令 --llms 与行为实测]。残余差异面(force 审计、VIEW --json、layout 挂账等)见 `references/commands.md` 差异表,用前实查。

## 一、五域路由（何时用哪条）

| 我要… | 用哪条 |
| --- | --- |
| 给某格发一句话、读某格屏幕等回话(自带忙候)、按键、查在网机器、工位管理(start/ws/shell/dev) | `agents` |
| 把文件交给指定 agent(自动上架加知会取用键) | `shares` |
| 播报、留痕、交回执、房间消息(append 落流,tail 取阅) | `streams` |
| 设别的格所在项目的持久任务(跨机 hst task,事件入流) | `tasks` |
| 要对方实时往我这里发字节(日志、进度,本机收对方发) | `pipes` |

- 与 evo-agent:agent-s5 分工:s5 是引擎命令面(put/get/ls/del/append/tail 直用);五原语是骑在 s5 与 herdr 与 hst 之上的协议面(寻址、门控、模板、状态信封)。裸引擎够用走 agent-s5;要投给人走本 skill。
- herdr 分工(淘汰序后):herdr CLI 退役为引擎(同 s5),窗格、工位、投递、读屏操作面一律本 skill(`agents start/ws/shell/dev/split/tab/zoom`);既有 herdr 技能(herdr-orch 等)已进淘汰序,指路至此。

## 二、文法与全局旗标（五命令同构）

```
<命令> [全局旗标] <动词> [动词旗标] [位置参数...]      # 常规形;裸调用 = VIEW,exit 0
<命令> to <id> [域操作数...] [--force]                # DELIVER:定向传递(过门控,投信封)
```

- 全局七旗标任意槽:`--help -h --llms --json --format --full-output --filter-output --schema`;`--` 逃生口;未知词 usage 退 2,禁静默吞
- 投递动词统一 `to`(v3.0 收口;`prompt` 在 agents 域为 to 别名);`--force` 任意参数位识别
- 保留动词首词命中即非目标:view read keys list mode put get append set open close to prompt machines start ws shell dev split tab zoom trust sync
- 逐命令动词表、输出契约与错误码表见 `references/commands.md`

## 三、id 三产生式（目标文法）

| 产生式 | 义 | 例 |
| --- | --- | --- |
| 无冒号 | 全局名:按 name 寻址,本机先,后在册机逐台 | `streams to hst_rs fleet "回执…"` |
| `机:余段` | 显式跨机;首冒号前 = 机标签(在册或 local),余段整段 = 名或格 | `agents read lan-win:w13:p1` |
| `local:余段` | 本机显式形 | `agents keys local:w8:p1 Enter` |

- 裸 pane id 非法:无冒号只按名查;含冒号先当机标签解析。**无名格必须 `local:<格>` 或 `<机>:<格>` 显式形**
- 机不占位置参数;机标签合法性 = 在册机表,查表用 `agents machines`
- 解析算法、多名命中、命名纪律、src 核验见 `references/addressing.md`

## 四、投递与收件反射（三律）

| 反射 | 律 |
| --- | --- |
| 投递 | 只看退出码与 `data.status` 与 CTA;门控判标全隐藏命令内,调用方零感知 |
| 收件 | `agents read <id>` 自带等待:目标忙则内候到闲或完成(默认 90s,`--timeout` 调),status 随信封出 |
| 拒投 | 自动代记 `deferred`(全域含 agents to);勿手补投,补收看 `room/deferred/` 流 |

- **门控 v2 = TUI 实况检测**:不看状态字段,读格可见内容对四家 TUI 判标族(claude/codex/grok/kimi 实测文案);有操作对话框(信任屏/权限屏/模式选择)即拒,空 TUI 可投,**busy 排队不拦**(各家 TUI 自带消息排队);保守清单,误拒优于误投 [实证:包源直读]
- **read 收件面**:忙候到闲/完成或超时;超时未闲出 `status:"timeout-working"`(内容仍全量附上,exit 0);无内容才 engine_fail 加 CTA `--timeout 加长重试` [实证:本机 working 格与闲格双实测]
- **拒投自动代记**:拒投时意图自动记入 `room/deferred/<目标格>` 流,退出码仍 1;agents 域代记含原文截 80 字,streams 域只记意图不含原文(要留原文走 `streams append`,见六坑)
- **--force**:跳门控强投(契约面追记 `room/force-audit` 审计;实装未落见差异表,强投前自问必要性)
- **status 四态信封**(DELIVER 的 `--json` data 恒带 `status`):

| status | 义 | data 伴生 |
| --- | --- | --- |
| `delivered` | 已投出且目标 agent 开吃(等到 working,15s 窗口) | target 与域字段 |
| `engine_fail` | 引擎写败,引擎 stderr 不吞不裁 | `engine_error` 摘要 |
| `deferred` | 门控拒投,已代记 | target 与代记落点 |
| `stalled` | 写入但 15s 未开吃 | target |

- 判成败先看退出码(0/1/2),再看 `data.status`;拒投时信封仍 `"ok":true`,勿单信 ok 字段 [实证]
- 信封三行形(字段行与取用行逐字稳定)与幂等 id、v 字段见 `references/deliver-gate.md`

## 五、隐式路由（各端一致）

- 调用方只给名字或 `机:格`;local 与 `--machine` 由 primlib 自适,调用方零感知,同一文法在任何端点可用
- 各端同构:linux/mac 直跑;Windows 无本地 s5 时顺 WSL 代役(wsl -e 直 exec,stdin/stdout 直通);本机名可 `PRIM_HOST_LABEL` 覆写
- 跨机零 ssh:herdr 族走 `--machine` 转发;tasks 远机走 pending 流加 apply 受体(见 commands.md tasks 域)

## 六、常见坑

| 坑 | 正确姿势 |
| --- | --- |
| 裸格直写格 id(如 `to w8:p1`) | 首冒号先当机标签解析,报「机器不在册」;无名格必须 `local:<格>` 或 `<机>:<格>` |
| `streams view` 只见最近一段 | 默认尾读最近 100 行(s5 tail -n 100);`-n`/`--lines` 调量,全量回放 `--from 0`,续读 `--resume` |
| streams 拒投后找消息原文 | 代记通知自动落 `room/deferred/` 但不含消息体、消息也不进流;要留原文改走 `streams append`(OPERATE 无门控)记流 |
| 目标 working 就不敢投 | 门控 v2 busy 排队不拦,只拒操作对话框;要等人回话用 `agents read` 忙候语义 |
| tasks 面沿用 goal 旧名 | hst 已正名 task;取用行 = `hst task show`,旧 goal 面仅作回退 |

## 七、协作惯例（速览,IM 映射）

| IM 概念 | 协议形 |
| --- | --- |
| 聊天室/房间 | 流(stream),`room/` 前缀表房间,如 room/deferred、room/force-audit |
| @某人 | DELIVER(门控加信封加提示词落格) |
| 私信 | `dm/<a>/<b>` 双方名专线流 |
| 在场状态 | `agents view` 看全场(presence 展示列);`agents mode <dnd|away|online> [until]` 自声明 |
| 离线消息补收 | room/deferred 代记流 |

- **回执惯例**:批次完工交回执走 `streams append fleet "<一句话>"`(host 前缀自动带,勿手写裸 s5 append;判例:批 132 首例回执手写前缀写错机名);收方 tail 取阅,取阅不回写
- 回放:`streams view <流> --from <seq>` 或 `--resume`;消息礼仪与 ack 惯例见 `references/collab.md`

## 八、契约真源与演进

- 唯一真源:ai-ccoe 仓 `plugins/CONTRACT.md`(五节加五a/b/c/d,v3.0 蓝图);细语义冲突以真源为准
- 演进纪律:契约升版,本 skill 随批对齐版本标注并回填差异表;本机 wrapper 与契约不一致时,以本机 `--llms` 与头注实查为准并如实报差异 [六态]
