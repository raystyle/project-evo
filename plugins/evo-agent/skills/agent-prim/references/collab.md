# 协作惯例与 IM 映射

> 五原语之上的舰队社交层:房间、私信、在场、回执、回放。命名即路由,流即载体。

## IM 映射表

| IM 概念 | 协议形 | 说明 |
| --- | --- | --- |
| 聊天室/房间 | 流名带 `room/` 前缀 | room/deferred(代记)、room/force-audit(审计)、room/pipe-live(跨机管道,契约面) |
| 全舰队大厅 | `fleet` 流 | 播报与回执主频道;append 落消息,tail 取阅 |
| @某人 | DELIVER | 门控加信封加提示词落格;比房间消息重,要人看见才用 |
| 私信 | `dm/<a>/<b>` 流 | 双方名专线;命名 = 两名按固定序(字典序)排,避免双开 |
| 在场状态 | `agents view` | presence 展示列;契约面另有声明键 share/presence(勿扰等,带 until) |
| 离线消息 | room/deferred | 拒投代记,收方补收(落点两形见 deliver-gate.md) |

## 消息礼仪（沿 agent-s5 同律）

- 一行一事,带端名前缀(`streams append` 自动加 `<host>|`;勿手写裸 `s5 append`)
- append-only:发出去不撤回不改写;更正 = 追加新行注明更正对象 [判例:批 132 回执前缀写错机名,以新行更正,不改旧行]
- 大内容走 shares 上键,流里只放键引用;频道不做请求应答(那是 agent-rloop 轮次域)
- 取阅 = tail,不回写、不 re-put

## 回执与 ack 惯例

- 批次完工回执:`streams append fleet "<一句话:批次、改面要点、去向>"`;总台 tail 取阅 [实证:批 132 首例]
- ack:收到要紧件(交付、周知)回执到来源流或 dm,一行确认;文件件可回执 ack 键(shares 上 share/<名>/…-ack.txt 判例)
- 停机与阻塞:持久任务域走 tasks;消息域回执说明原因,不静默消失

## 回放与续读

- `streams view <流> --from <seq>`:从序号回放;全量 = `--from 0`
- `--resume`:从机内 cursor 续读(cursor 落 `~/.local/state/prim/cursor/<流名>`,机内不共享;换机从 0 或显式 seq 起)
- 默认尾读最近 100 行(s5 tail -n 100);要更多用 `-n N` 调量或 `--from` 回放
- [实证] 3.0.0a1 斜杠流名(room/、dm/、channel/ 族)view 尾段 cursor 写崩:数据行已全打印,退出码 1 加栈;读 stdout 即得,要净退出码走 s5 tail(agent-s5 面)
- 保留策略(契约面):room/ 与 dm/ 14 天、tasks/shared 30 天;要长留的内容上 shares 看板

## 与邻 skill 分工

- evo-agent:agent-s5 = s5 引擎命令面(put/get/ls/del/append/tail 直用,看板与频道命名);本 skill = 五原语协议面(寻址、门控、信封、状态回调)。裸引擎够用走 agent-s5,要投给人走本 skill
- evo-agent:agent-rloop = 轮次协议(派单、三件套、义务图);消息与产物信道仍走本 skill 与 agent-s5
- evo-herdr:herdr-orch = 本台窗格与信号;跨机跨格投递走本 skill
- hst task = 持久任务存储与 Stop 提醒(goal 命令族已正名 task);跨机设任务走本 skill tasks 域
