# 五命令文法与输出契约

> 蒸馏自契约二、三、四、五d 节(真源 ai-ccoe plugins/CONTRACT.md,v3.0 蓝图);标注 [实证] 的行为以本机 wrapper 实读为准(prim 3.0.0a1,R1 修件后实态:ai-ccoe main d524d7c)。

## 通则（文法与输出契约）

- **文法模板**:`<命令> [全局旗标] <动词> [动词旗标] [位置参数...]`;全局七旗标(`--help -h --llms --json --format --full-output --filter-output --schema`)任意槽;`--format` 与 `--filter-output` 带值;`--` 逃生口;未知词 usage 退 2 禁静默 shift
- **两形同源**:`--json` 出机器形(DELIVER 出单行信封 `{"ok":true,"data":{...},"meta":{"command":"<名>"}}`,data 恒带 status 四态);缺省人读形;两形字段序一致
- **错误分道**:错误一律 stderr;`--json` 时 stderr 单行 `{"code":"...","message":"...","cta":[{"command":"...","description":"..."}]}`;stdout 永纯数据 [实证:not_found 实测形]
- **CTA 专业标准**:错误必带下一步,统一『下一步:』前缀与 target= 键值形,俚语清零(『开吃/候/强投』不再出);例 `目标存在操作对话框,已拒投并代记;下一步:--force 跳过门控重发`
- **退出码**:0 成功;1 业务未命中(目标无、拒投、键不存在);2 用法错;禁其他码。拒投时 stdout 仍出 ok:true 信封 + exit 1,判定看退出码与 data.status 勿单信 ok [实证]
- **裸调用**:无参 = VIEW,exit 0,不进交互(agent 可放心探测)

## 错误码表

| code | 义 | cta |
| --- | --- | --- |
| not_found | 目标名或机器全局未命中(同名多格也走此码,信息注多名) | agents view 查名 / agents machines 列机 |
| gate_refused | 目标格有操作对话框(门控 v2:TUI 实况判标) | --force 重发 / 消息改走 OPERATE 记流 |
| engine_fail | s5/hst/tailcat/herdr 引擎失败(原文透传不吞不裁) | 看引擎输出(data 带 engine_error) |
| usage | 参数形不合法或未知词 | --llms 看手册 |

## 五域速查表（v3 动词面）

| 命令 | VIEW | OPERATE | DELIVER |
| --- | --- | --- | --- |
| agents | `view [机]`;`machines`;`list [机]` | `read <id> [--lines N] [--timeout S]`(收件面);`keys <id> <键>`;`mode <dnd|away|online> [until]`;`start <名> --kind <类>`;`ws <label>`/`ws list`/`ws close`;`shell <机> <仓>`;`dev <机> <仓> [--kind]`;`split <id> [--direction]`;`tab list/create/close`;`zoom <id>`;`trust`;`sync` | `to <id> <文本> [--force]`(prompt = 别名) |
| shares | `view`(share/ 键表) | `put <文件>`;`get <键> [-o|--output 名]` | `to <id> <文件> [--force]` |
| streams | `view [流名] [--from <seq>|--resume]`(流表加尾读) | `append <流> <消息>` | `to <id> <流> <消息> [--force]` |
| tasks | `view`(tasks/shared 最近事件) | `set <id> <文本>` | `to <id> <文本> [--force]`(= set 加事件加知会) |
| pipes | `view [机]` | `open [--keep]`;`close <addr|pid>` | `to <id> [--force]` |

## agents（消息域）

- **收件面(隐式等待)**:`agents read <id> [--lines N] [--timeout S]`(默认 20 行、90 秒);目标 working 则内候(5s 轮询)到闲/完成或超时;status 随信封出(闲 = idle/done,超时未闲 = timeout-working,内容仍全量附上,exit 0);无内容才 engine_fail 加 CTA `--timeout 加长重试` [实证:本机 working 格与闲格双实测]
- 读屏即收件:等队友回话就用 read,勿手写轮询
- 全局面:`agents view` 跨全部在册机出格表(HOST、NAME、PANE、STATUS、KIND、CWD);`agents machines` 出机表与可达性 [实证:实测本机外四机在册]
- 投递:`agents to <id> <文本>` 过门控 v2 投信封 v2 三行形;成功面 `已投递,目标已开始处理(target=…)`,拒投自动代记 room/deferred(含原文截 80 字)并 stderr `下一步:--force 跳过门控重发` [实证:包源直读]
- 工位管理:`agents start <名> --kind <类>` 起格、`ws`/`shell <机> <仓>`/`dev <机> <仓>` 开台起 agent、`split`/`tab`/`zoom` 布局、`trust` 信任屏放行、`sync` 机册面;tab id 解析 = `机:tabid`
- 在场声明:`agents mode <dnd|away|online> [until]`(自声明,写 shares 键 `share/presence/<host>/<格>` 覆盖,正文 mode 与 until;勿扰与离开建议短窗,过期自动回落) [实证:mode online 实测落键]
- 按键:`agents keys <id> <键>`;跨机 = usage 拒,CTA 指本机 keys 或 mesh trust(契约面)

## shares（文件域）

- 键形:`share/<src 机>/<内容短哈希>/<文件名>`;同内容命中同键(哈希取前 64KB md5 前 10 位)
- 上架:`shares put <文件>` 回显键;取回:`shares get <键> -o <本地名>` [实证:实测取回]
- DELIVER:先上架再投信封,取用行 = `s5 get -o <文件名> <键>`;拒投时文件已在键上、代记注明待达,人不丢件

## streams（流域）

- 播报:`streams append <流> <消息>` 自动加 `<host>|` 前缀(勿手写裸 `s5 append` 漏前缀,判例 = 批 132)
- 读:`streams view <流> [-n N|--lines N]` 默认尾读最近 100 行(s5 tail -n 100;`--seq` 与 -n 互斥时由 python 层切片兜底);全量回放 `--from 0`;`--resume` 从机内 cursor 续读;每次具名 view 后 cursor 落 `~/.local/state/prim/cursor/<流名>`(机内不共享)
- DELIVER:先 append 入流再投信封,取用行 = `s5 tail <流>`;拒投时不写流不保原文,要留消息改走 append

## tasks（持久任务域）

- 底座 = hst task(goal 命令族已正名 task,hst v2.12.0);本地直设,远机零 ssh:pending 流 `tasks/pending/<机>` 加 apply 受体唤醒
- 事件流:每次 set 追加事件行入 `tasks/shared`(ts、node、cwd、by、task)
- DELIVER:set 加事件加知会,取用行 = `cd <cwd> && hst task show`

## pipes（实时字节域）

- 底座 = tailcat;`pipes view [机]` 出本机活动管道或跨机只读(走 `room/pipe-live` 流);`pipes open [--keep]` 本机起收听,地址与日志落 `~/.local/state/pipe/`;字节方向 = 本机收对方发
- `pipes close <addr|pid>` 关管道地址作废;本机 30 分钟超时自关,`--keep` 长 transport;win 活性探测走 OpenProcess
- DELIVER:开管道后向目标投信封,取用行 = `tailcat <addr>`;拒投自动代记(管道待达)
- [实证] R0 已铸齐(view 实测 exit 0;win 五链实弹过,ai-ccoe 16a2e1c)

## 本机实装差异表（v3.0 契约面 vs prim 3.0.0a1 R1 后实装）

[实证:2026-10-13 lan-ubuntu 实测,ai-ccoe main d524d7c 重装后;`--llms` 与包源直读。R0 已收:pipes 域铸齐、agents 域动词面与 to 拒投代记、门控 v2 四家判标、read 隐式收件;R1 已收:斜杠流名 cursor 崩(父链全建,view room/deferred/w8:p1 净退 0)、streams 手册补 -n、mode 实装]

| 契约 v3.0 面 | R1 后实装 |
| --- | --- |
| VIEW 与 OPERATE 的 --json 两形 | 未落(--json 仅 DELIVER 信封与错误 stderr 生效) |
| tasks view [机|id] 带参面 | 忽略参数,恒出 tasks/shared 最近 8 事件 |
| --force 审计 room/force-audit | 未落(五域皆无;强投前自问必要性) |
| 幂等 id、tasks 事件 prev | 未落(v=1 已随信封 v2 落,from/to 恒在) |
| 拒投代记流键 = 收方名 | 用目标格 pane id;shell 形旧流按名仍在,补收两边都看 |
| presence 声明键 = share/presence/<机>/<名>(五a) | 实装用 <机>/<格> pane 形 [实证:mode online 落键] |
| streams 拒投代记含原文 | 只记意图行(流名加待递),不含消息体;须 --force 重发或改走 append |
| 裸 pane id = usage | 偏离:名字解析同时命中 pane_id,勿依赖此偏离 |
| --help = 手册加节序展开 | --help 与 --llms 同面(无节序展开) |
| layout 动词(契约八节) | 挂账:herdr 0.9.3 无 layout 子命令(preview 面,候 herdr 后续版) |

- 用前实查:`command -v agents` 等五命令在不在、`<命令> --llms` 看手册面;差异面如实报,不猜不代装(分发归宿主工具链 omc 与 ark)
