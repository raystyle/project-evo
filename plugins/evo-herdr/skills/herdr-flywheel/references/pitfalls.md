# herdr 飞轮治理操作坑

> 跨仓治理实操踩坑实录,按现象、根因、修法收录;新坑当场追加,二犯升格进 SKILL 正文纪律条目。

## 派单与回执面

| 坑 | 现象与根因 | 修法 |
|---|---|---|
| send-text 不是派单 | pane send-text 仅投草稿不提交,agent 不开始轮次 | 正式派单恒走 herdr agent prompt(原子文本加编码 Enter) |
| 工位编号漂移 | 合同或旧档写的编号与实况不符,凭记忆派单投错工位 | 派单前必 herdr agent list 实查,pane ID 从 JSON 响应取 |
| 备用屏读不全 | agent 跑在终端备用屏,加大 --lines 也读不到出屏行(出屏行不进宿主回滚缓冲) | 兜底:请对方把完整回执落临时 md 文件回路径,直读文件 |
| yolo 后落不追认 | agent 驻场在先、hst init --yolo 落盘在后,会话许可模式定格旧态,全会话审批阻塞 | 带起顺序恒 hst init --yolo 先于 agent 驻场;可提 hst doctor 加「会话活模式与盘上 yolo 一致性」检测项 |

## 仓级统一操作面

| 坑 | 现象与根因 | 修法 |
|---|---|---|
| checkout-index 假成功 | git checkout-index -f -a 对在场文件「强制重写」假成功,盘上 CRLF 原样不动;stat 缓存命中视为最新,-f 不真覆盖 | 清场再检出:git ls-files -z 加 xargs -0 rm -f 后 checkout-index -f -a |
| 整片 M 而 diff 空 | 工作树按索引重写后整片 M 但 diff 全空,似内容漂移实未变;索引条目 stat 陈旧的 racily-clean 形 | git add -u 刷索引条目即愈;收工前验 diff --cached 为零 |
| 管道吞门禁退出码 | 门禁命令接管道(tail/grep/head)后 `$?` 是末命令的,测试 FAILED 仍假绿;`&&` 链照走曾把红态提交直推远端,只能 forward 修 [实证: 2026-09-21 单仓评审轮两犯] | 门禁裸跑;要管道就显式取 `${PIPESTATUS[0]}` 或落盘 `CMD > f 2>&1; S=$?` 再按 S 分支,红态绝不进 commit 分支 |
| 评审格随 codex 退出被回收 | 常驻评审格里的 codex /quit 后整格被回收(remain-on-exit 关),pane ID 失效;旧格 cwd 还可能指向已删除目录(仓改名遗留),屏面 Ready 但相对路径全断 [实证: 2026-09-21 旧评审格驻已删目录] | 退出后 pane list 复查再派单;重驻 = 右分新格(仓内 cwd)加 agent start,命名沿用 live 名;勿信旧编号旧 cwd |
| --wait 撞已决态即时返回 | agent prompt --wait 对已处 idle/done 的工位即时返回,JSON 里 revision 与标题不动,似派单未落地;个别首轮粘贴还会被吞(update banner 期) [实证: 2026-09-22 browse-codex-review 首单丢、omc 派单静默] | 判落地看屏不看返回:pane read 实证 Context/回执在长;丢单用最小回显探针验通道后重发;派发后轮询 agent list 甄别真开工,--wait 只当提交回执不当完成回执 |

## 跨机器工位面

| 坑 | 现象与根因 | 修法 |
|---|---|---|
| --machine 叠加 --session | `herdr --machine lan-ubuntu --session agents agent list` 报 cannot be combined;--machine 走保存 profile 里记的会话,launch 选项互斥 | 只写 `--machine <label> <子命令>`,会话名已在 profile 里 |
| stalled 不等于没送到 | 跨机 agent prompt 报 agent_prompt_stalled,实读 pane 文本已送达且 agent 正常回执;CLI 观察窗短,慢热 agent 未在窗内起态 [实证: 2026-09-23 OfficeCLI 归属周知轮 lan-ubuntu] | 报 stalled 先 `herdr --machine X agent read` 实读确认送达与回执,确认前不重发防重复派单 |
| pane 编号不跨机唯一 | 远程机器自有工位编号体系,与本机 w1A/w1C 等并存;凭本机经验猜远程 pane 会投错 | 每台机器各跑 agent list 实查,pane ID 从该机 JSON 响应取 |
| 新工位开错形(两连错) | 先 pane split 右分格、再 tab create,均非工位单元;根因 = 原语层级未锚(评审格形与 tab 形先入为主),「工位 = workspace」缺带起配方 [实证: 2026-09-23 lan-ubuntu OfficeCLI 工位,用户两纠后 w7 归位] | 新工位恒走 workspace create 三步配方(SKILL 原语表);split = 评审格专用形,tab = 同工位多上下文,二者勿当工位开 |
| 远程机器全原语自成一套 | 跨机 workspace/pane 编号与本机并存互不相干(w6 在 lan-ubuntu 与本机 w1A 无关联),远程根格命名同为 p1 | 跨机操作恒 --machine 前缀;结构问询按机各查(workspace/tab/pane list 皆可路由),语义按原语表跨机一致解读 |
