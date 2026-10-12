# 工位形态与带起、跨机器路由、信号命令速查

> 批 128 由 herdr-flywheel 归并迁入(工位怎么带起、跨机怎么路由、herdr 信号命令怎么用);目标循环协议本体在 evo-agent:agent-rloop。命令语法活权威 = 本机直跑 `herdr --skill`。

## 原语四级(每台机器同名同义;编号只在机内唯一,跨机不通用)

| 原语 | herdr 单元 | 舰队语义 | 误用黑名单 |
| --- | --- | --- | --- |
| 机器 | machine(label 加独立 server) | 远程一等公民,workspace/tab/pane 全套自成一套 | 假设 pane 编号跨机唯一 |
| 工作台(工位) | workspace(w 号) | 一仓一台(仓工位)或一任务一台(临时会话);用户惯称「窗台」 | 新工位误开 split pane 或 tab [实证: 2026-09-23 lan-ubuntu 两连错形后归位] |
| TAB 页 | tab(t 号) | 同工位内多上下文页,舰队罕用 | 新工位 = 开新 tab(错形) |
| 窗格 | pane(p 号) | agent 驻留位;工位主格 = workspace 根格;右分格 = 评审格专用形 | 评审格形态当成工位 |

## 新工位带起配方(本机三步;跨机各步前置 `--machine <label>`,仓先在该机备好)

```bash
herdr workspace create --cwd <仓路径>                 # 返回 workspace 与 root_pane(如 w7:p1)
herdr agent start <工位名> --kind claude --pane <root_pane>   # 工位名即派单地址(编号会漂,名不漂)
# 仓内 cwd 首启弹目录信任或确认选择屏:pane read 实证后替答(裁定归用户;本 fleet 仓默认可信);
# claude 2.x 随后再弹外部导入问屏,按需选答。零信任屏复启 = 该 cwd 信任已录。
```

- 每仓一个 herdr 工位,总台自成工位;派单地址 = pane ID,从 herdr agent list 的 JSON 响应取,不猜不背;live 唯一的 agent 名亦可作地址
- **多 agent kind 工位**:`--kind` 随委派对象定(codex、grok、kimi 等);pane 内先跑 `<cli> --version` 探真解析;启动特化见 lane-dispatch.md
- **工位编号会漂移**:合同与旧档写的编号不可信,派单前必 herdr agent list 实查 [实证: 2026-09-16 两轮不符];关闭的 pane ID 不复用,活清单缺号打不中任何人;`--machine` 下 `--current` 解析为远端当前格,不带本地调用方
- **带起顺序 = hst init --yolo 先于 agent 驻场**:会话许可模式在驻场时定格,后落盘的 yolo 不被追认 [实证: 2026-09-16 八工位审批阻塞]
- idle 与 done 皆可派(差别仅 seen 标记);blocked 等人裁不代答;working 可插队(甄别见 agent-rloop);unknown 不判死,`herdr agent explain` 后处置;实时态只作门控与干预信号,完成判定用盘上稳态
- 勿关非自建工位(workspace、tab、pane、session)

## 跨机器工位

远程机器是 herdr 一等公民,总台经保存的 SSH profile 直接路由命令,不需要自己 ssh [实证: 2026-09-23 lan-ubuntu 归属周知轮]。

- **机器面实查**:`herdr machine list` 取 label、ssh target 与会话名;profile 增删启停仅用户明令,删 profile 只断客户端不断远端会话
- **命令路由**:`herdr --machine <label-or-id> <agent|pane 子命令>` 原样路由;selector 必须是 enabled profile 的 ID 或唯一(大小写敏感)label;不与 `--session`、`--remote` 组合
- **ID 与名都 scoped 单机**:两台机可各有 `w1:p1` 或同名 agent;跨机派单地址 = 机器 label 加该机 agent list 实查的 pane ID
- **转发前提与边界**:双侧安装都要支持 machine API 转发,远端 server 必须在跑且 API 兼容;转发不安装不起不重启远端 server;本地配置、会话管理、交互附着不转发
- **派单前双查**:本机与 `herdr --machine X` 的 agent list 各跑一次,两侧清册都从 JSON 取
- **stalled 误报处置**:跨机 prompt 报 `agent_prompt_stalled` 时文本往往已送达;先 `herdr --machine X agent read` 实读确认,确认前不重发
- **TUI 选机不重定命令向**:无 `--machine` 前缀的命令恒走本地 session,别被 TUI 选择态误导

## 信号命令速查

活权威 = 本机直跑 `herdr --skill`,不凭记忆写命令。常用面:`herdr agent list` 实查工位;`agent get` 查态;`agent prompt` 派单;`agent wait` 等状态事件(`--until` 逐态重复旗标加 `--timeout` 兜底);`agent read` 收回执;`agent send-keys` 发逻辑键;普通进程与文本事件不走生命周期,用 `herdr pane wait-output <pane> --match <文本>`(或 `--regex`)。ID 与状态一律从 JSON 响应取。

## 驻场与跨机坑实录(现象、根因、修法)

| 坑 | 现象与根因 | 修法 |
|---|---|---|
| 确认选择屏未替答 | 驻场后 idle、interactive_ready 真,屏面实为目录确认屏 [实证: 2026-10-10] | 驻场后必 pane read 实证 CLI 输入框稳态;见确认屏按策略替答后再派 |
| 冷启动竞态吞派单 | agent start 返回成功后立即派单报 stalled,欢迎屏渲染期键入被吞 [实证: 2026-10-07/08 双工位] | 先实读 pane 见输入框稳态再派;stalled 后必实读判送达才重发 |
| yolo 后落不追认 | 驻场先于 yolo 落盘,会话定格旧审批态 | 带起顺序恒 hst init --yolo 先于驻场 |
| --machine 叠加 --session | 报 cannot be combined;会话名已在 profile 里 | 只写 `--machine <label> <子命令>` |
| pane 编号不跨机唯一 | 凭本机经验猜远程 pane 投错 | 每台机器各跑 agent list 实查 |
| 新工位开错形 | split 或 tab 均非工位单元 | 新工位恒走 workspace create 三步配方 |
| 远程全原语自成一套 | 跨机编号与本机并存互不相干 | 跨机操作恒 --machine 前缀,结构问询按机各查 |
| 评审格随 codex 退出被回收 | /quit 后整格被回收,pane ID 失效;旧格 cwd 可能指向已删目录 [实证: 2026-09-21] | 退出后 pane list 复查再派;重驻 = 右分新格加 agent start |
| checkout-index 假成功 | 对在场文件强制重写假成功,CRLF 原样不动 | 清场再检出:git ls-files -z 加 xargs -0 rm -f 后 checkout-index -f -a |
| 整片 M 而 diff 空 | racily-clean 形,索引条目 stat 陈旧 | git add -u 刷索引即愈;收工前验 diff --cached 为零 |
| 管道吞门禁退出码 | 管道后 `$?` 是末命令的,红态假绿直推远端 [实证: 2026-09-21 两犯] | 门禁裸跑;要管道显式取 PIPESTATUS[0] 或落盘分支 |
