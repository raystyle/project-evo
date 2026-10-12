# 目标文法与全局寻址

> 蒸馏自契约一、五a 节。目标 = 五命令共用的寻址面;解析唯一实现处在 primlib(契约边界)。

## 文法三形

| 形 | 义 | 例 |
| --- | --- | --- |
| 裸名字 | 全局按 name 寻址:先本机,后各在册机逐台查 | `streams orch 回执 …` |
| 机:名 | 显式跨机;第一个冒号前 = 机标签,其后整段 = 名或格 | `agents read lan-linux:s5_rs` |
| local:名 | 本机显式形(等价裸名先查本机) | `agents keys local:evo-claude Enter` |

- 裸 pane id 非法(契约文法);[实证] v2.0.0 实装同时认 pane_id 形,属实现偏离,勿依赖
- 机标签 = herdr 机名(`hostname -s` 部署约定);在册机表 = `herdr machine list`

## 解析算法（prim_lookup）

1. 带冒号:机标签在册(或 local)则直取,机不在册报错
2. 裸名:本机 `agent list` 按 name 精确匹配
3. 未中:遍历在册机逐台 `--machine` 查
4. 全未中:not_found,错误指路 `agents view`;同名多格 = not_found(信息注多名),契约规定不取先命中

## 命名纪律

- 起格必带名:`agent start --name <名>`;无名格在全局寻址里不可达(表里 PANE 列有名才寻得到)
- 名字稳定复用:跨机递件、dm 流名、deferred 流名都拿名字做键;改名 = 换身份
- 查名面:`agents view`(全局格表:HOST、PANE、STATUS、KIND、CWD)

## 回信地址与 src 核验

- 投递方自动附 `src=<host>:<pane>`(以 $PWD 匹配本机格得出);你在仓目录里投的件,回信地址就指向你那格
- **src 是提示非签名**:收方回信前以 `agents view` 核对 host:pane 仍是活格;取用行是唯一协议面(见 deliver-gate.md 信封节)
- agent 自助用法:在目标仓 cwd 里起格并命名,即可被全局寻址与回信 [实证:批 132 evo-claude 格经 fleet 流交回执]

## 坑簿

- 裸名先本机后远程:同名本机远程都有时,本机优先;要打远程格用 机:名 显式形
- 远端机 ssh 不通时逐台查会慢;知道机就写 机:名 一次命中
- `hostname -s` 与 herdr 机标签不一致的机,裸名跨机查不到;用 机:名 并报给总台对齐标签
