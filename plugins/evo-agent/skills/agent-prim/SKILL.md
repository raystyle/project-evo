---
name: agent-prim
description: >-
  舰队互操作五原语操作面:五命令 agents/shares/streams/tasks/pipes,三段式文法(VIEW 全局可视、
  OPERATE 只动资源、DELIVER 定向传递带门控);裸名全局寻址与命名纪律(agent start 带 --name);
  DELIVER 门控(working/blocked 拒投、--force 留审计、拒投代记 room/deferred 补收);协作惯例
  (流即房间、DELIVER 即 @、dm/ 与 room/ 前缀、agents view 即 presence、回执走 streams append
  fleet、--from/--resume 回放)。契约单一真源 = ai-ccoe 仓 plugins/CONTRACT.md,本 skill 只路由
  不复述;与 agent-s5 分工 = s5 是引擎命令面,五原语是骑在其上的协议面。
  Use when 要跨机找格读屏发提示、把文件交给指定 agent、往流交回执或播报、设别的格所在项目的
  goal、开实时管道时;触发词 agent-prim、五原语、原语、agents、shares、streams、tasks、pipes、
  投递、门控、拒投、deferred、代记、force、强投、房间、room、dm、presence、取用行、回执、
  回放、cursor、from、resume、舰队互操作。
---

# agent-prim - evo-agent 舰队互操作五原语

**定位**:舰队(多机多格 agent)互操作协议的操作面。五命令各管一域,三段式同构;DELIVER 自带门控与代记,消息永不静默丢失。契约唯一真源 = ai-ccoe 仓 `plugins/CONTRACT.md`,本 skill 蒸馏速览加路由,不复述契约全文;契约演进以真源为准,本 skill 随批对齐。

**版本对齐**:契约 v2.3(2026-10-12 契约化批)。本机实装以 `command -v agents` 等实查为准,wrapper 头注即版本 [实证:本节写作时 lan-ubuntu 实装 v2.0.0]。差异面(--json、--llms、幂等 id、v 字段等)见 `references/commands.md` 差异表。用前实查。

## 一、五域路由（何时用哪条）

| 我要… | 用哪条 |
| --- | --- |
| 给某格发一句话、读某格屏幕、按键、herdr agent 动词 | `agents` |
| 把文件交给指定 agent(自动上架加知会取用键) | `shares` |
| 播报、留痕、交回执、房间消息(append 落流,tail 取阅) | `streams` |
| 设别的格所在项目的 goal(跨机 hst goal,事件入流) | `tasks` |
| 要对方实时往我这里发字节(日志、进度,本机收对方发) | `pipes` |

- 与 evo-agent:agent-s5 分工:s5 是引擎命令面(put/get/ls/del/append/tail 直用);五原语是骑在 s5 与 herdr 与 hst 之上的协议面(寻址、门控、模板、审计)。裸引擎够用走 agent-s5;要投给人走本 skill。
- 与 evo-herdr:herdr-orch 分工:herdr 管本台窗格布局与信号;跨机跨格投递走本 skill。

## 二、三段式文法（五命令同构）

```
<命令> [view [参数]]              # VIEW:全局可视(格表 + 本域资源),裸调用同此,exit 0
<命令> <OPERATE 动词> [参数...]    # OPERATE:只动资源不投人
<命令> <目标> <资源...> [--force]  # DELIVER:定向传递(过门控,投信封模板加提示词)
```

- OPERATE 保留词:view read keys list prompt put get append set open close;保留词不进目标解析
- 五域速查(VIEW 与 OPERATE 与 DELIVER 逐命令动词表)见 `references/commands.md`

## 三、目标文法与命名纪律（速览）

- **裸名字** = 全局按 name 寻址(先本机,后各在册机);**机:名** = 显式跨机;`local:` 前缀 = 本机;裸 pane id 非法
- 命名纪律:起格必带名(`agent start --name <名>`);找不到目标时错误会指路 `agents view`
- 解析算法、回信地址(host:pane)、src 核验见 `references/addressing.md`

## 四、DELIVER 语义（速览）

- **门控**:投前查目标格状态;working/blocked 拒投(exit 1,CTA 指路);`--force` 强投并追记审计流
- **拒投代记**:拒投时原文意图记入 `room/deferred/<收方名>` 流;收方补收 = `streams view room/deferred/<自己的名字>`
- **信封三行形**(字段行与取用行逐字稳定,人话行可自由):

```
[<域>] <src> <一句话动作>
src=<host>:<pane> <域字段...>
取用:<可复制命令行>
```

- 门控判据细节、幂等 id、v 字段、agents prompt 的裸门控差异见 `references/deliver-gate.md`

## 五、协作惯例（速览,IM 映射）

| IM 概念 | 协议形 |
| --- | --- |
| 聊天室/房间 | 流(stream),`room/` 前缀表房间,如 room/deferred、room/force-audit |
| @某人 | DELIVER(门控加信封加提示词落格) |
| 私信 | `dm/<a>/<b>` 双方名专线流 |
| 在场状态 | `agents view`(presence 展示列) |
| 离线消息补收 | room/deferred 代记流 |

- **回执惯例**:批次完工交回执走 `streams append fleet "<host>|<回执一行>"`(host 前缀自动带,勿手写裸 s5 append;判例:批 132 首例回执手写前缀写错机名);收方 tail 取阅,取阅不回写
- 回放:`streams view <流> --from <seq>` 或 `--resume`(cursor 机内落 `~/.local/state/prim/cursor/`);消息礼仪与 ack 惯例见 `references/collab.md`

## 六、契约真源与演进

- 唯一真源:ai-ccoe 仓 `plugins/CONTRACT.md`(当前 v2.3);本 skill 不复述契约全文,细语义冲突时以真源为准
- 演进纪律:契约升版,本 skill 随批对齐版本标注并回填差异表;本机 wrapper 与契约版本不一致时,以本机 `--help` 与头注实查为准并如实报差异 [六态]
