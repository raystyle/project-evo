# 目标文法与全局寻址

> 蒸馏自契约一、五a、五d 节。目标 = 五命令共用的寻址面;解析唯一实现处在 primlib(契约边界)。v3 定形:id 单类型三分产生式,机不再占位置参数。

## id 三产生式

| 产生式 | 义 | 例 |
| --- | --- | --- |
| 无冒号 | 全局名:按 name 寻址,本机先,后在册机逐台查 | `tasks to hst_rs "收束后发版"` |
| `机:余段` | 显式跨机;首冒号前 = 机标签,余段整段 = 名或格(格 id 自带冒号不冲突,按首冒号切) | `agents read lan-win:w13:p1` |
| `local:余段` | 本机显式形 | `agents keys local:w8:p1 Enter` |

- 裸 pane id 非法(契约文法):无冒号只按名查。[实证] 3.0.0a1 名字解析同时命中 pane_id,属实现偏离,勿依赖
- 机标签合法性 = 在册机表(`agents machines` 查)或 `local`;不在册报 not_found,CTA 指 `agents machines` [实证:实测「机器不在册」]
- 机标签 = herdr 机名(`hostname -s` 部署约定);`hostname -s` 因部署约定视为合法形

## 解析算法（primlib resolve）

1. 带冒号:机标签在册(或 local)则直取余段
2. 无冒号:本机 agent 表按 name 精确匹配
3. 未中:遍历在册机(enabled)逐台查
4. 全未中:not_found,CTA 指 `agents view`;**多名命中 = not_found**(信息注多名),契约规定不取先命中

## 命名纪律

- 起格必带名:`agent start --name <名>`;无名格在裸名寻址里不可达,只能 `local:<格>` 或 `<机>:<格>` 显式形
- 名字稳定复用:跨机递件、dm 流名、deferred 流名(shell 形)都拿名字做键;改名 = 换身份
- 查名面:`agents view`(全局格表:HOST、NAME、PANE、STATUS、KIND、CWD)

## 隐式路由（各端一致）

- 调用方只给名字或 `机:格`;local 与 `--machine` 由 primlib resolve 与 herdr 调用层自适,调用方零感知
- 同一文法在任何端点可用;远端解析走 `herdr --machine` 转发,零 ssh 零旁路
- 本机名取 `hostname -s`;与机册注册名不合时可 `PRIM_HOST_LABEL` 覆写(如 win 机)

## 回信地址与 src 核验

- 投递方自动附 `src=<host>:<pane>`(以 cwd 匹配本机格得出;匹配不中退化为仅 host);你在仓目录里投的件,回信地址就指向你那格
- **src 是提示非签名**:收方回信前以 `agents view` 核对 host:pane 仍是活格;取用行是唯一协议面(见 deliver-gate.md 信封节)

## 坑簿

- 无名格别裸写:`to w8:p1` 首冒号先当机标签,报「机器 w8 不在册」;要打该格用 `local:w8:p1` [实证]
- 裸名先本机后远程:同名本机远程都有时,本机优先;要打远程格用 `机:名` 显式形
- 远端机不可达时逐台查会慢;知道机就写 `机:名` 一次命中
- `hostname -s` 与 herdr 机标签不一致的机,裸名跨机查不到;用 `机:名` 并报给总台对齐标签
