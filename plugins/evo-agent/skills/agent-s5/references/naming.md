# 看板与频道命名约定

> 键空间是跨台共享的地基:名对了,任何端任何 agent 零沟通即可定位。约定沿舰队端名与 kebab 短名,判例随用随记。

## 看板键空间

形:`board/<工作台>/<主题>/<文件名>`

| 段 | 取值 | 判例 |
| --- | --- | --- |
| 工作台 | 舰队端名:wsl、lan-win、lan-mac、lan-ubuntu、lan-linux | board/wsl/... |
| 主题 | kebab 短名,一主题一目录:config-lint、research、ops、release | board/lan-mac/research/... |
| 文件名 | 带日期或单号,排序即时间线:2026-10-12-cfg-01、batch-113.patch | .../2026-10-12-cfg-01 |

规约:

- 看板对象是**文件级交换**:报告、补丁、工件包、对账单;不是数据库,不建深层级(主题下直接放文件,不再嵌目录)
- 写者拥有:哪台放哪台管;要改他人对象 = 取回自己工作台前缀下改完重放,原对象由 owner 处置
- `del` 只清自己工作台前缀(board/<本端>/...)下的对象;清他人前缀属越权,不做
- 放前 `ls` 同主题目录防重名覆盖;覆盖自己旧版是合法迭代(同 key 重 put)

## 频道键空间

形:`channel/<频道>`

| 段 | 取值 | 判例 |
| --- | --- | --- |
| 频道 | 全局 kebab 短名:舰队运维 fleet-ops、项目研究 <项目>-research、告警 <域>-alert | channel/fleet-ops |

规约:

- 频道是 **append-only 流**:播报、周知、留痕;一条消息一行,端名前缀打头(如 `[wsl] 批117 已推 2f174b2`)
- 开新频道前 `streams` 或 `ls` 查重;新频道首条消息自述用途一句(如 `[wsl] 本频道播 project-evo 封版动态`)
- 消费 = `tail` 取阅;取阅不回写、不 ack 到频道(要回应走对话或派单域)
- 大内容(超数行)走看板文件,频道消息里放 key 引用:`[lan-mac] 研究笺已上看板 board/lan-mac/research/ 下 2026-10-12-gw 件`
- 频道不做请求-应答、不做派单收执(那是 herdr 飞轮域);只做单向播报

## 双道选型三问

对象道后端 garage(path-style),流道 streamstore 记录(候 s5 首版实测定稿)。

1. 要的是**文件**(有版本、要取回、给后续用)还是**消息**(一句话、流过去就完)?文件走看板,消息走频道
2. 读者是**指定的对端**(要回执、要对账)还是**谁在谁捞**?指定对端走 herdr 派单与产物契约,广播走频道
3. 内容是**轮次档或研究档**(三件套、研究笺、轨迹流)?走下节 rounds 与 research 与 streams 键空间,不进 board/ 与 channel/

## 跨机轮次与研究档键空间

键空间规范(源 herdr:s5 批 124 并入,语义原样):

- `rounds/<YYYY-MM-DD>-<主题短名>/<单号>-{brief,state,receipt}.md`:跨机轮次三件套;发起方写 brief 后 put 上键(prompt 给远端键,接收方 get 回本地轮次目录),接收方 state 与 receipt 先写本地、每检查点后 put 同步远端(同键覆盖终态形),断言方 get 回执对账
- `research/<仓名>/<S 编号或档名>`:跨仓研究档交换(收方入自己 sources/external,verbatim 留底);`artifacts/<仓名>/<工件路径形>`:工件包
- `streams/<仓名>/diary` 与 `streams/<仓名>/events`:轨迹流与事件流(append 追加、tail 尾随);流不替代 diary 文件(日终 diary 篇是权威,流是跨机实时面,蒸馏进 diary 时标 derived_from);环 1000 条与单条 32KB 量级为设计值(候实测回填),超限走对象道分片

协同律:同机轮次走本地共享目录不上 s5;一次性跨机传文件 = 临时键加消息道告键加用毕 del(传输即弃);键空间规范变更走本仓 REQ,不私改

## 判例簿

- 2026-10-12:本 skill 立项(总台用户令);同日用户令删 herdr:s5 并入本 skill(s5 = 所有 agent 共享的看板与实时流,唯一技能面,轮次与研究键空间随迁);命令面以各台 `s5 --llms` 实查为准,wsl 当日尚无 s5 二进制(分发归 omc 与 ark),skill 只认 PATH
