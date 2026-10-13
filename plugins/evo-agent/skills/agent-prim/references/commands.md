# 五命令文法与输出契约

> 蒸馏自契约二、三、四、五d 节(真源 ai-ccoe plugins/CONTRACT.md,v3.0 蓝图);标注 [实证] 的行为以本机 wrapper 实读为准(prim 3.0.0a1,python 形)。

## 通则（文法与输出契约）

- **文法模板**:`<命令> [全局旗标] <动词> [动词旗标] [位置参数...]`;全局七旗标(`--help -h --llms --json --format --full-output --filter-output --schema`)任意槽;`--format` 与 `--filter-output` 带值;`--` 逃生口;未知词 usage 退 2 禁静默 shift
- **两形同源**:`--json` 出机器形(DELIVER 出单行信封 `{"ok":true,"data":{...},"meta":{"command":"<名>"}}`,data 恒带 status 四态);缺省人读形;两形字段序一致
- **错误分道**:错误一律 stderr;`--json` 时 stderr 单行 `{"code":"...","message":"...","cta":[{"command":"...","description":"..."}]}`;stdout 永纯数据 [实证:not_found 实测形]
- **退出码**:0 成功;1 业务未命中(目标无、拒投、键不存在);2 用法错;禁其他码。拒投时 stdout 仍出 ok:true 信封 + exit 1,判定看退出码与 data.status 勿单信 ok [实证]
- **裸调用**:无参 = VIEW,exit 0,不进交互(agent 可放心探测)

## 错误码表

| code | 义 | cta |
| --- | --- | --- |
| not_found | 目标名或机器全局未命中(同名多格也走此码,信息注多名) | agents view 查名 / agents machines 列机 |
| gate_refused | 目标 working/blocked | --force 重发 / 改走 OPERATE 记流 |
| engine_fail | s5/hst/tailcat/herdr 引擎失败(原文透传不吞不裁) | 看引擎输出(data 带 engine_error) |
| usage | 参数形不合法或未知词 | --llms 看手册 |

## 五域速查表（v3 动词面）

| 命令 | VIEW | OPERATE | DELIVER |
| --- | --- | --- | --- |
| agents | `view [机]`;`machines`;`list [机]` | `read <id> [--lines N]`;`keys <id> <键>`;`mode <dnd|away|online> [until]`;herdr agent 透传(允许表) | `to <id> <文本> [--force]`(prompt = 别名) |
| shares | `view`(share/ 键表) | `put <文件>`;`get <键> [-o|--output 名]` | `to <id> <文件> [--force]` |
| streams | `view [流名] [--from <seq>|--resume]`(流表加尾读) | `append <流> <消息>` | `to <id> <流> <消息> [--force]` |
| tasks | `view`(tasks/shared 最近事件) | `set <id> <文本>` | `to <id> <文本> [--force]`(= set 加事件加知会) |
| pipes | `view [机]` | `open [--keep]`;`close <addr|pid>` | `to <id> [--force]` |

## agents（消息域）

- 读屏:`agents read <id> --lines 80` [实证:--lines 3 实测];默认 20 行;`--source recent-unwrapped` 由 wrapper 内带
- 全局面:`agents view` 跨全部在册机出格表(HOST、NAME、PANE、STATUS、KIND、CWD);`agents machines` 出机表与可达性 [实证:实测本机外四机在册]
- 投递:`agents to <id> <文本>` 过门控投自由文(无信封模板);拒投 stderr 指 `--force 强投,或改走 streams append 记流` [实证]
- 按键:`agents keys <id> <键>`;跨机 = usage 拒,CTA 指本机 keys 或 mesh trust(契约面)
- 透传:其余 herdr agent 动词按允许表透传(如 rename、kill、trust、sync)

## shares（文件域）

- 键形:`share/<src 机>/<内容短哈希>/<文件名>`;同内容命中同键(哈希取前 64KB md5 前 10 位)
- 上架:`shares put <文件>` 回显键;取回:`shares get <键> -o <本地名>` [实证:实测取回]
- DELIVER:先上架再投信封,取用行 = `s5 get -o <文件名> <键>`;拒投时文件已在键上、代记注明待达,人不丢件

## streams（流域）

- 播报:`streams append <流> <消息>` 自动加 `<host>|` 前缀(勿手写裸 `s5 append` 漏前缀,判例 = 批 132)
- 读:`streams view <流>` 默认尾读最近 100 行(s5 tail -n 100);全量回放 `--from 0`;`--resume` 从机内 cursor 续读;每次具名 view 后 cursor 落 `~/.local/state/prim/cursor/<流名>`(机内不共享)
- DELIVER:先 append 入流再投信封,取用行 = `s5 tail <流>`;拒投时不写流不保原文,要留消息改走 append

## tasks（持久任务域）

- 底座 = hst task(goal 命令族已正名 task,hst v2.12.0);本地直设,远机零 ssh:pending 流 `tasks/pending/<机>` 加 apply 受体唤醒
- 事件流:每次 set 追加事件行入 `tasks/shared`(ts、node、cwd、by、task)
- DELIVER:set 加事件加知会,取用行 = `cd <cwd> && hst task show`

## pipes（实时字节域,契约面）

- 底座 = tailcat;`pipes open` 本机起收听,字节方向 = 本机收对方发;`close <addr|pid>` 关;本机 30 分钟超时自关,`open --keep` 长 transport
- 跨机 VIEW 走只读流 `room/pipe-live`(src、pid、opened,分钟级保留)
- [实证] v3.0.0a1 此域铸造中:任意动词 die usage 退 2,提示 shell 版仍在役;实时字节面暂走旧道

## 本机实装差异表（v3.0 契约面 vs prim 3.0.0a1 实装）

[实证:2026-10-13 lan-ubuntu 实测;prim = python 形 uv 工具,`--llms` 与包源直读]

| 契约 v3.0 面 | 3.0.0a1 实装 |
| --- | --- |
| pipes 域全动词面 | 铸造中,任意动词 die usage 退 2 |
| agents 工作台面(ws/shell/dev/split/layout/tab/zoom)与 mode | 未落 case 分支,透传先按 id 解析,首参非 id 即 not_found [实证:ws list 实测] |
| VIEW 与 OPERATE 的 --json 两形 | 未落(--json 仅 DELIVER 信封与错误 stderr 生效) |
| tasks view [机|id] 带参面 | 忽略参数,恒出 tasks/shared 最近 8 事件 |
| 拒投代记流键 = 收方名 | 用目标格 pane id(如 room/deferred/w8:p1);shell 形旧流按名(room/deferred/hst_rs)仍在,补收两边都看 |
| streams 拒投代记含原文 | 只记意图行(流名加待递),不含消息体;须 --force 重发或改走 append |
| --force 审计 room/force-audit | 未落(python 形;shell 形曾落) |
| 幂等 id、v=1 字段、tasks 事件 prev | 未落 |
| 裸 pane id = usage | 偏离:名字解析同时命中 pane_id,勿依赖此偏离 |
| --help = 手册加节序展开 | --help 与 --llms 同面(无节序展开) |
| --llms 动词表 = case 分支(漂移守卫) | 手册列 ws 族等超集于 case 分支,守卫未挂,以差异表为准 |
| cursor 任意流名可写 | 斜杠流名(room/、dm/、channel/ 族)view 尾段 cursor 写崩(子目录不建):数据行已全打印,退出码 1 加栈 [实证] |

- 用前实查:`command -v agents` 等五命令在不在、`<命令> --llms` 看手册面;差异面如实报,不猜不代装(分发归宿主工具链 omc 与 ark)
