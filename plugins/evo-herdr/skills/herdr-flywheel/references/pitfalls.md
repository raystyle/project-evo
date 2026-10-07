# herdr 飞轮治理操作坑

> 跨仓治理实操踩坑实录,按现象、根因、修法收录;新坑当场追加,二犯升格进 SKILL 正文纪律条目。

## 派单与回执面

| 坑 | 现象与根因 | 修法 |
|---|---|---|
| send-text 不是派单 | pane send-text 仅投草稿不提交,agent 不开始轮次 | 正式派单恒走 herdr agent prompt(原子文本加编码 Enter) |
| 工位编号漂移 | 合同或旧档写的编号与实况不符,凭记忆派单投错工位 | 派单前必 herdr agent list 实查,pane ID 从 JSON 响应取 |
| agent 名被回收复用 | 工位名随退出即释放,后来者(另一 run 或用户手起)可复用同名,凭名 steer 投错对象 | steer 前对 session id:herdr agent get 与台账记录比对,不一致停手诊断 |
| done 假象多源 | agent_status 读 done 与提示被吞、冻结、modal 误分类同形;goal 型轮次间隙也读 done | done 不作完成判据;以验收判据(diff、测试、commit sha)与盘上记录对账 |
| TUI 未就绪悬输入框 | 新会话 agent 未就绪时 send-text 悬在输入框不生效 | 先 pane wait-output 等就绪标志(banner 类锚文本)再派;普通脚本 send-text 加 send-keys enter 两步起 |
| 冷启动竞态吞派单 | agent start 返回成功(idle、interactive_ready)后立即 agent prompt 派单,双工位(grok 与 kimi)齐报 agent_prompt_stalled(5 秒活动窗无 working);实读 pane 见欢迎屏仍占屏、输入框空、context 0%,文本未送达。根因 = 检测就绪不等于 CLI 输入面就绪,欢迎屏渲染期键入被吞 [实证: 2026-10-07/08 pve-harness 评审轮双工位] | 驻场后先实读 pane 见 CLI 输入框稳态再派单;stalled 后必实读 pane 判送达,确认输入框空且无在跑轮才重发(防重复派单);确认后重发即中 |
| prompt --wait 提交即返 | 带 --wait 提交后立即成功返回 agent_prompted,agent_status 仍 idle,未等 working 与收束。根因 [推断] = 收束判定的现态命中与轮次启动竞态:提交后首查落在 idle 窗即命中收束返回;对照实证:0.9.1 热会话未复现(探针 2.6 秒正常等收束,终态 done),冷启动慢起 agent 高危 | 刚提交的单不依赖 prompt --wait 收束,改两段式:先 wait --until working 开工探针(短超时,短轮漏 working 属正常),再 wait --until idle/done/blocked 独立收束;超时均不证未送达 |
| 备用屏读不全 | agent 跑在终端备用屏,加大 --lines 也读不到出屏行(出屏行不进宿主回滚缓冲) | 兜底:请对方把完整回执落临时 md 文件回路径,直读文件 |
| yolo 后落不追认 | agent 驻场在先、hst init --yolo 落盘在后,会话许可模式定格旧态,全会话审批阻塞 | 带起顺序恒 hst init --yolo 先于 agent 驻场;可提 hst doctor 加「会话活模式与盘上 yolo 一致性」检测项 |

## 仓级统一操作面

| 坑 | 现象与根因 | 修法 |
|---|---|---|
| checkout-index 假成功 | git checkout-index -f -a 对在场文件「强制重写」假成功,盘上 CRLF 原样不动;stat 缓存命中视为最新,-f 不真覆盖 | 清场再检出:git ls-files -z 加 xargs -0 rm -f 后 checkout-index -f -a |
| 整片 M 而 diff 空 | 工作树按索引重写后整片 M 但 diff 全空,似内容漂移实未变;索引条目 stat 陈旧的 racily-clean 形 | git add -u 刷索引条目即愈;收工前验 diff --cached 为零 |
| 管道吞门禁退出码 | 门禁命令接管道(tail/grep/head)后 `$?` 是末命令的,测试 FAILED 仍假绿;`&&` 链照走曾把红态提交直推远端,只能 forward 修 [实证: 2026-09-21 单仓评审轮两犯] | 门禁裸跑;要管道就显式取 `${PIPESTATUS[0]}` 或落盘 `CMD > f 2>&1; S=$?` 再按 S 分支,红态绝不进 commit 分支 |
| 评审格随 codex 退出被回收 | 常驻评审格里的 codex /quit 后整格被回收(remain-on-exit 关),pane ID 失效;旧格 cwd 还可能指向已删除目录(仓改名遗留),屏面 Ready 但相对路径全断 [实证: 2026-09-21 旧评审格驻已删目录] | 退出后 pane list 复查再派单;重驻 = 右分新格(仓内 cwd)加 agent start,命名沿用 live 名;勿信旧编号旧 cwd |
| --wait 撞已决态即时返回 | agent prompt --wait 对已处 idle/done 的工位即时返回,JSON 里 revision 与标题不动,似派单未落地;个别首轮粘贴还会被吞(update banner 期) [实证: 2026-09-22 browse-codex-review 首单丢、omc 派单静默] | 判落地看屏不看返回:pane read 实证 Context/回执在长;丢单用最小回显探针验通道后重发;甄别真开工用开工探针 `agent wait --until working`(已在跑即返,探针超时不证未送达);完成甄别以 commit sha 加 read 为准,重投前必实读防跑两遍 |

## 跨机器工位面

| 坑 | 现象与根因 | 修法 |
|---|---|---|
| --machine 叠加 --session | `herdr --machine lan-ubuntu --session agents agent list` 报 cannot be combined;--machine 走保存 profile 里记的会话,launch 选项互斥 | 只写 `--machine <label> <子命令>`,会话名已在 profile 里 |
| stalled 不等于没送到 | 跨机 agent prompt 报 agent_prompt_stalled,实读 pane 文本已送达且 agent 正常回执;CLI 观察窗短,慢热 agent 未在窗内起态 [实证: 2026-09-23 OfficeCLI 归属周知轮 lan-ubuntu] | 报 stalled 先 `herdr --machine X agent read` 实读确认送达与回执,确认前不重发防重复派单 |
| pane 编号不跨机唯一 | 远程机器自有工位编号体系,与本机 w1A/w1C 等并存;凭本机经验猜远程 pane 会投错 | 每台机器各跑 agent list 实查,pane ID 从该机 JSON 响应取 |
| 新工位开错形(两连错) | 先 pane split 右分格、再 tab create,均非工位单元;根因 = 原语层级未锚(评审格形与 tab 形先入为主),「工位 = workspace」缺带起配方 [实证: 2026-09-23 lan-ubuntu OfficeCLI 工位,用户两纠后 w7 归位] | 新工位恒走 workspace create 三步配方(SKILL 原语表);split = 评审格专用形,tab = 同工位多上下文,二者勿当工位开 |
| 远程机器全原语自成一套 | 跨机 workspace/pane 编号与本机并存互不相干(w6 在 lan-ubuntu 与本机 w1A 无关联),远程根格命名同为 p1 | 跨机操作恒 --machine 前缀;结构问询按机各查(workspace/tab/pane list 皆可路由),语义按原语表跨机一致解读 |
