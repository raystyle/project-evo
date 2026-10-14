---
name: agents
description: >-
  agents 原语(prim v3 消息域)与六原语共享面枢纽;仅舰队窗格与消息操作域,读项目协作
  规则文件 AGENTS.md 时本 skill 不适用。全局 pane 操作器(隐式路由,任何端点同一
  文法),告诉或委派某 agent 干活、找格读屏等回话(read 自带忙候与超时)、按键、
  在场声明(mode)、开工作台起格调窗格邻居布局(ws/start/shell/dev/split/tab/zoom)、
  查在网机器;投递动词统一 to,投递与收件三反射(投递只看 status 与 CTA『下一步』、
  收件 agents read 自带忙候与超时、拒投自动代记 deferred 补收);门控 v2 = TUI 实况
  尾窗判标族(操作对话框拒投,busy 排队不拦);status 四态信封(delivered/
  engine_fail/deferred/stalled)与信封 v2 三行形(人话行 @收方、字段行 from/to 恒在
  带 v、取用行);id 三产生式与命名标准(工作台-类型-编号,编号即田字顺时针窗格位,
  满四开 tab)。共享面(id、门控、信封、命名标准、协作惯例、实装差异表)独家在本
  skill,shares/streams/tasks/pipes/ctx 五原语 skill 链至此。契约单一真源 = ai-ccoe 仓
  plugins/CONTRACT.md,本 skill 只路由不复述。
  Use when 要告诉或委派某 agent 干活、找格读屏等回话、读队友格、给某格发消息或按键、
  查在场改 presence、开工作台或 tab 调窗格邻居布局、查在网机器时;触发词 agents、
  原语、prim、告诉、委派、让干、找格、读屏、读格、窗格、邻居、tab、工作台、table、
  投递、派单、门控、拒投、deferred、代记、补收、force、四态、信封、status、收件、
  忙候、timeout-working、mode、presence、machines、id、命名标准、隐式路由、机:格、
  close、关格、reload、翻台、重载、wt、开视图、local:、舰队互操作。
---

# agents - evo 消息域原语与六原语共享面

**定位**:六原语的消息域原语,兼共享面枢纽:id 三产生式、命名标准、门控 v2、信封 v2、status 四态、协作惯例、实装差异表独家在本 skill 的 references,其余五原语 skill(shares/streams/tasks/pipes/ctx)以相对链至此。契约唯一真源 = ai-ccoe 仓 `plugins/CONTRACT.md`。

**版本对齐**:本机实装以 `agents --llms` 实查为准;残余差异面见 `references/commands.md` 差异表。

## 一、agents 域路由（何时用哪条）

| 我要… | 用哪条 |
| --- | --- |
| 告诉或委派某格 agent 干活(一句话指令) | `agents to <id> <文本>` |
| 找格读屏、等队友回话(自带忙候) | `agents read <id> [--lines N] [--timeout S]` |
| 给某格按键 | `agents keys <id> <键>` |
| 查全场格表、在场状态 | `agents view`;自声明 `agents mode <dnd|away|online> [until]` |
| 开工作台、起格、调布局 | `agents ws/start/shell/dev/split/tab/zoom` |
| 关格、翻台、开视图 | `agents close/reload/wt` |
| 查在网机器 | `agents machines` |
| 其余 herdr agent 动词 | 按允许表透传(trust、sync 等) |

- 传文件走 shares;往流交回执或广播走 streams;设持久任务走 tasks;实时字节走 pipes;查历史对话走 ctx(read 只管实时屏)(各域 skill 自持)

## 二、文法与全局旗标（六命令同构）

```
<命令> [全局旗标] <动词> [动词旗标] [位置参数...]      # 常规形;裸调用 = VIEW,exit 0
<命令> to <id> [域操作数...] [--force]                # DELIVER:定向传递(过门控,投信封)
```

- 全局七旗标任意槽:`--help -h --llms --json --format --full-output --filter-output --schema`;`--` 逃生口;未知词 usage 退 2
- 投递动词统一 `to`(`prompt` 为别名);`--force` 任意参数位识别
- 保留动词首词命中即非目标:view read keys list mode put get append set open close to prompt machines start ws shell dev split tab zoom close wt trust sync reload show search

## 三、id 三产生式（目标文法）

| 产生式 | 义 | 例 |
| --- | --- | --- |
| 无冒号 | 全局名:按 name 寻址,本机先,后在册机逐台 | `agents to evo-claude-1 "评审已递"` |
| `机:余段` | 显式跨机;首冒号前 = 机标签(在册或 local) | `agents read lan-win:w13:p1` |
| `local:余段` | 本机显式形 | `agents keys local:w8:p1 Enter` |

- 裸 pane id 非法;无名格用 `local:<格>` 或 `<机>:<格>` 显式形
- 命名标准 = `<工作台标签>-<agent类型>-<编号>`(台标签 = 仓别名;编号 = 田字顺时针窗格位,满四开 tab 续编);起名带校验(非标准形提示不拦截)
- 解析算法、多名命中、from 核验见 `references/addressing.md`

## 四、投递与收件反射（三律）

| 反射 | 律 |
| --- | --- |
| 投递 | 只看退出码与 `data.status` 与 CTA;门控判标全隐藏命令内 |
| 收件 | `agents read <id>` 自带等待:目标忙则内候到闲或完成(默认 90s,`--timeout` 调) |
| 拒投 | 自动代记 `deferred`(全域含 agents to);补收看 `room/deferred/` 流 |

- 门控 v2 = TUI 实况尾窗检测:只拒操作对话框(信任屏/权限屏/模式选择),空 TUI 可投,busy 排队不拦,误拒优于误投
- read 忙候超时未闲出 `status:"timeout-working"`(内容仍附,exit 0);无内容才 engine_fail;历史档案走 ctx
- 拒投自动代记 `room/deferred/<目标格>`(agents 域含原文截 80 字),退出码仍 1;`--force` 跳门控强投
- **status 四态信封**(DELIVER 的 `--json` data 恒带 `status`):

| status | 义 | data 伴生 |
| --- | --- | --- |
| `delivered` | 已投出且目标开始处理(等到 working,15s 窗口) | target 与域字段 |
| `engine_fail` | 引擎写败,引擎 stderr 不吞不裁 | `engine_error` 摘要 |
| `deferred` | 门控拒投,已代记 | target 与代记落点 |
| `stalled` | 写入但 15s 未开始处理 | target |

- 判成败先看退出码(0/1/2),再看 `data.status` 与 CTA(『下一步:』前缀);拒投时信封仍 `"ok":true`,勿单信 ok
- 信封 v2 三行形:人话行 `[<域>] @<收方> <一句话>`、字段行 `from=<host>:<pane> to=<id> 域字段 v=1`、取用行;细节见 `references/deliver-gate.md`

## 五、agents 专属动词面

- 收件:`agents read <id> [--lines N] [--timeout S]`(默认 20 行、90 秒)
- 在场:`agents mode <dnd|away|online> [until]`(写 shares 键 `share/presence/<host>/<格>`)
- 工位:`start <名> --kind <类>`(命名校验)、`ws`/`ws list`/`ws close`、`shell <机> <仓>`、`dev <机> <仓> [--kind]`、`split`、`tab list/create/close`、`zoom`
- 关格:`close <id>`(优雅退 /exit 后 shell exit,零击杀;末格收台)
- 翻台:`reload <id>`(同格同 session 重进;存量名保名,非法名自修正披露 old-name)
- 视图:`wt [机|wsl] [--title 名]`(win 专属:本窗开 tab 显该机 herdr 视图)
- 机器:`machines`;跨机隐式路由零感知
- 按键:`keys <id> <键>`(仅本机与 local: 目标)

## 六、常见坑

| 坑 | 正确姿势 |
| --- | --- |
| 裸格直写格 id(如 `to w8:p1`) | 无名格必须 `local:<格>` 或 `<机>:<格>` |
| 目标 working 就不敢投 | 门控只拒操作对话框,busy 排队不拦;等回话用 `agents read` 忙候 |
| 拒投信封 ok:true | 判定看退出码与 data.status,勿单信 ok |
| 旧进程 = 旧技能 | 装/更插件后必 `agents reload <id>` 翻台;回滚裸形时上下文弃(信封 resume 字段披露) |
| 目标机离线 | view 跳过不可达机单行告警;投递面按引擎错原文报 |

## 七、协作惯例（速览,IM 映射）

| IM 概念 | 协议形 |
| --- | --- |
| 聊天室/房间 | 流(stream),`room/` 前缀表房间,如 room/deferred |
| @某人 | DELIVER(门控加信封加提示词落格) |
| 私信 | `dm/<a>/<b>` 双方名专线流 |
| 在场状态 | `agents view` 看全场;`agents mode` 自声明 |
| 离线消息补收 | room/deferred 代记流 |

- **回执惯例**:批次完工交回执走 `streams append fleet "<一句话>"`(host 前缀自动带,勿手写裸 s5 append);收方 tail 取阅,取阅不回写
- 回放、消息礼仪、ack 惯例见 `references/collab.md`

## 八、契约真源与演进

- 唯一真源:ai-ccoe 仓 `plugins/CONTRACT.md`;细语义冲突以真源为准
- 契约升版本 skill 随批对齐;本机 wrapper 与契约不一致时,以 `--llms` 实查为准并回填差异表
