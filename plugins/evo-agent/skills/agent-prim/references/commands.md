# 五命令文法与输出契约

> 蒸馏自契约二、三、四节(真源 ai-ccoe plugins/CONTRACT.md v2.3);标注 [实证] 的行为以本机 wrapper 实读为准。

## 通则（输出契约）

- **两形同源**:`--json` 出机器形(JSONL 逐行数据;DELIVER 出单行信封 `{"ok":true,"data":{...},"meta":{"command":"<名>"}}`),缺省人读形;两形字段序一致
- **错误分道**:错误一律 stderr,形 `<命令>: <信息>`;`--json` 时 stderr 单行 `{"code":"<码>","message":"...","cta":[...]}`;stdout 永纯数据
- **类型化 CTA**:拒投与未命中错误必带下一步(`--force 强投` / `改走 OPERATE` / `agents view 查名`)
- **退出码**:0 成功;1 业务未命中(目标无、拒投、键不存在);2 用法错;禁其他码
- **裸调用**:无参 = VIEW,exit 0,不进交互(agent 可放心探测)

## 错误码表

| code | 义 | cta |
| --- | --- | --- |
| not_found | 目标名全局未命中(同名多格也走此码,信息注多名) | agents view 查名 |
| gate_refused | 目标 working/blocked | --force 重发 / OPERATE 记流 |
| engine_fail | s5/hst/tailcat/herdr 引擎失败 | 看引擎输出 |
| usage | 参数形不合法 | --llms 看手册 |

## 五域速查表

| 命令 | VIEW | OPERATE | DELIVER |
| --- | --- | --- | --- |
| agents | `[view [机]]`;`list [机]` | `read <目标> [--lines N]`;`keys <目标> <键...>`;herdr agent 动词透传 | `prompt <目标> <文本> [--force]` |
| shares | `[view]`(格表 + share/ 键表) | `put <文件>`;`get <键> -o <名>` | `<目标> <文件> [--force]` |
| streams | `[view [流名]]`(格表 + 流表/尾读) | `append <流> <消息>` | `<目标> <流> <消息> [--force]` |
| tasks | `[view [机|目标]]`(格表 + tasks/shared 事件 + 该机任务) | `set <目标> <文本>` | `<目标> <文本> [--force]` |
| pipes | `[view]`(格表 + 本机活动管道) | `open`;`close <addr|pid>` | `<目标> [--force]` |

## agents（格操作域）

- 读屏:`agents read <目标> --lines 80`;跨机自动路由 `herdr --machine <机> agent read`
- 发提示词:`agents prompt <目标> <文本>`(过门控,无信封模板,自由文)
- 按键:`agents keys <目标> <键...>`(仅本机与 local: 目标;跨机 = usage 拒,CTA 指本机 keys 或 mesh trust)
- 透传:其余 herdr agent 动词原样透传(如 rename、kill)
- [实证] v2.0.0 的 prompt 分支拒投即退,不写代记流也不记 force 审计;要代记改走 streams DELIVER

## shares（文件域）

- 键形:`share/<src 机>/<内容短哈希>/<文件名>`;同内容命中同键,不同内容不互覆
- 上架:`shares put <文件>` 回显键;取回:`shares get <键> -o <本地名>`
- DELIVER:上架后向目标投信封,取用行 = `s5 get -o <文件名> <键>`;写入失败时文件已在键上,回执会注明
- [实证] 首航判例(2026-10-12):share/lan-linux/primitive-first-flight.txt 与 pi-rs 回执 ack

## streams（流域）

- 播报:`streams append <流> <消息>`(自动加 `<host>|` 前缀;勿手写裸 `s5 append` 漏前缀,判例 = 批 132 回执手写前缀写错机名)
- 读:`streams view <流>`(最近 100 行);回放:`--from <seq>` 从序号读、`--resume` 从机内 cursor 续读;cursor 落 `~/.local/state/prim/cursor/<流名>`,机内不共享
- 全量回放 = `--from 0`;保留策略(契约面):room/ 与 dm/ 14 天、tasks/shared 30 天
- DELIVER:先 append 入流再向目标投信封,取用行 = `s5 tail <流>`

## tasks（目标域）

- 底座 = hst goal(项目态);`tasks set <目标> <文本>` 在目标格 cwd 上执行,远端走 `ssh mesh-<机>`
- 事件流:每次 set 追加 JSON 事件行入 `tasks/shared`(ts/node/cwd/by/goal;契约 v2.3 补 prev 字段)
- VIEW 带目标时附显该格 cwd 的 goal
- DELIVER:set 加知会,取用行 = `cd <cwd> && hst goal show`

## pipes（实时字节域）

- 底座 = tailcat;`pipes open` 本机起收听(后台),地址与日志落 `~/.local/state/pipe/`;字节方向 = 本机收、对方发
- `pipes close <addr|pid>` 关管道地址作废;本机管道 30 分钟超时自关(契约面:`open --keep` 长 transport)
- DELIVER:开管道后向目标投信封,取用行 = `tailcat <addr>`
- 契约 v2.3 面:跨机 VIEW 走只读流 room/pipe-live(src/pid/opened,分钟级保留)

## 本机实装差异表（v2.3 契约面 vs v2.0.0 实装）

| 契约 v2.3 面 | v2.0.0 实装 [实证:lan-ubuntu wrapper 实读] |
| --- | --- |
| `--json` 两形与信封 | 未落(仅人读形) |
| `--llms` 手册面 | 未落 |
| stderr 错误码结构(CTA json 块) | 部分(人读错误有指路,无 json 形) |
| 幂等 id、v=1 字段 | 未落 |
| presence 声明键 share/presence | 未落(仅 agents view 展示列) |
| pipes 跨机 VIEW(room/pipe-live)、open --keep | 未落 |
| tasks 事件 prev 字段 | 未落 |
| 裸 pane id 非法 | 偏离:v2.0.0 寻址同时认 name 与 pane_id |
| agents prompt 代记与 force 审计 | 未落(拒投即退) |
| streams --from/--resume、拒投代记、force 审计、取用: 前缀、host| 前缀 | 已落 |

- 用前实查:`command -v agents` 等五命令在不在、`head -3 $(command -v streams)` 看头注版本;差异面如实报,不猜不代装(分发归宿主工具链 omc 与 ark)
