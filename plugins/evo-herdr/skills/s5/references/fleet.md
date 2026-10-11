# 与 herdr 飞轮协同:跨机路径规范

> 分工裁定:herdr 管信号与消息(派单、回执通知、状态门控),s5 管共享内容(档、工件、流)。同机轮次走本地共享目录(herdr-flywheel 产物契约篇),**跨机轮次**才上 s5。

## 一、跨机轮次三件套(对象道)

键空间规范:`rounds/<YYYY-MM-DD>-<主题短名>/<单号>-{brief,state,receipt}.md`

- 发起方:写 brief 后 `s5 put` 上键;prompt 里给远端键(接收方 `s5 get` 到本地轮次目录再走三件套纪律)
- 接收方:state 与 receipt 先写本地(盘上稳态),每检查点后 `s5 put` 同步远端键(覆盖同键,终态形)
- 断言方:从远端键 get 回执对账;凭据与路径问题走 herdr 消息道问,不走 s5
- 原则:本地是稳态、s5 是跨机共享层;同键覆盖(终态件),不追加

## 二、研究档与工件(对象道)

键空间:`research/<仓名>/<S 编号或档名>`;工件:`artifacts/<仓名>/<工件路径形>`

跨仓研究档交换:出方 put 收方 get,收方入自己 sources/external(verbatim 留底纪律,relation 记 cited_source)

## 三、轨迹流与事件流(流道)

键空间:`streams/<仓名>/diary`(日轨迹流)、`streams/<仓名>/events`(事件流)

- 跨机协同期各仓 agent 把轨迹要点 `s5 append` 到本仓流;总台或协查方 `s5 tail -n` 取最近态
- 流不替代 diary 文件:日终 diary 篇(文件)是权威,流是跨机实时面;流内容可蒸馏进 diary 时标 derived_from 指流名
- 环 1000 条与单条 32KB 量级(设计值,候实测回填),超限走对象道分片

## 四、边界与协同律

- s5 不传 herdr 消息:派单、状态、通知走 herdr(不混道);s5 只走内容
- 一次性跨机传文件给对方就用,不留档不留流,直接 s5 put 临时键 + 消息道告键,用毕 del
- 生产桶键规范变更走本仓治理(REQ),不私改键空间
