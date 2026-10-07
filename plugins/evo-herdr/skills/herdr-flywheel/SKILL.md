---
name: herdr-flywheel
description: >-
  herdr 跨仓模式:不同仓库的 agent 工作台对话交流与治理协作。一个总台协调多个单仓工位,
  派单、回执、断言、吸收四步循环,并行轮按义务图运转。涵盖 herdr agent prompt 原子派单、
  agent get 状态门控、agent wait 事件驱动收执、agent read 收回执、独立复核断言、反馈吸收分流、
  工位带起顺序与多 agent kind、跨机器工位路由、并行派单义务图纪律、治理操作坑。
  本 skill 是该协议唯一权威源;herdr 命令语法的活权威是本机直跑 herdr --skill;
  开发模式(窗格布局、评审闸门、自省验收、lane 任务分发)在同插件 herdr-dev。
  Use when 跨仓派发治理任务、收 herdr 工位回执、做总台轮次协调、多工位并行派单时;触发词 herdr、
  飞轮、跨仓、派单、回执、工位、多仓治理、并行派单、义务图、跨机器工位、--machine、状态门控、
  事件驱动、agent wait、codex、grok、kimi。
compatibility: 需 herdr 管理的工位会话(HERDR_ENV=1);各工位侧仓自带门禁
---

# herdr 飞轮跨仓协作

> 跨仓模式:一个总台协调多个单仓 herdr 工位(仓加 workspace 加 pane 加常驻 agent 会话)对话交流与治理协作,派单、回执、断言、吸收四步循环。沉淀自 2026-09-16 六仓四轮实证(对齐、标准态、终态、扩编与讨论)与后续实践轮。开发模式(窗格布局、评审闸门、自省验收、lane 任务分发)在同插件 herdr-dev。

## 工位形态与带起

### 原语四级(每台机器同名同义;编号只在机内唯一,跨机不通用)

| 原语 | herdr 单元 | 舰队语义 | 误用黑名单 |
| --- | --- | --- | --- |
| 机器 | machine(label 加独立 server) | 远程一等公民,workspace/tab/pane 全套自成一套 | 假设 pane 编号跨机唯一 |
| 工作台(工位) | workspace(w 号) | **一仓一台**(仓工位)或一任务一台(临时会话);用户惯称「窗台」 | 新工位误开 split pane 或 tab [实证: 2026-09-23 lan-ubuntu OfficeCLI 工位两连错形后归位] |
| TAB 页 | tab(t 号) | 同工位内多上下文页,舰队罕用 | 新工位 = 开新 tab(错形) |
| 窗格 | pane(p 号) | agent 驻留位;工位主格 = workspace 根格;右分格 = 评审格专用形(开发模式布局见 herdr-dev) | 评审格形态当成工位 |

### 新工位带起配方(本机三步;跨机各步前置 `--machine <label>`,仓先在该机备好)

```bash
herdr workspace create --cwd <仓路径>                 # 返回 workspace 与 root_pane(如 w7:p1)
herdr agent start <工位名> --kind claude --pane <root_pane>   # 工位名即派单地址(编号会漂,名不漂)
# 仓内 cwd 首启弹目录信任屏:pane read 实证后替答(裁定归用户;本 fleet 仓默认可信);
# claude 2.x 随后再弹外部导入问屏,按需选答。零信任屏复启 = 该 cwd 信任已录。
```

- 每仓一个 herdr 工位,总台自成工位;派单地址 = pane ID,从 herdr agent list 的 JSON 响应取,不猜不背;live 唯一的 agent 名亦可作地址
- **多 agent kind 工位**:`--kind` 随委派对象定(codex、grok、kimi 等);pane 内先跑 `<cli> --version` 探真解析(command -v 会踩版本管理 shim 假解析);启动特化与环境预检见同插件 herdr-dev 的 lane-dispatch 篇
- **工位编号会漂移**:合同与旧档写的编号不可信,派单前必 herdr agent list 实查 [实证: 2026-09-16 合同写法与实况两轮不符]
- **带起顺序 = hst init --yolo 先于 agent 驻场**:会话许可模式在驻场时定格,后落盘的 yolo 不被追认,全会话停在旧审批态致阻塞 [实证: 2026-09-16 八工位驻场先于 yolo 落盘,全会话审批阻塞];可提 hst doctor 增加「会话活模式与盘上 yolo 一致性」检测项
- idle 与 done 皆可派,差别仅 seen 标记(pane 与 agent focus 标 seen,agent read 不标);blocked 是等人裁,问用户不代答;working 可插队,回执甄别见派单节;unknown 不判死,`herdr agent explain <工位>` 看检测规则与证据后处置;状态优先来自集成上报,无上报退回屏幕检测
- 勿关非自建工位(workspace、tab、pane、session)

## 跨机器工位

远程机器是 herdr 的一等公民(machine 原语),工位可以驻在别的机器上;总台经保存的 SSH profile 直接路由命令,不需要自己 ssh 过去 [实证: 2026-09-23 OfficeCLI 维护归属周知轮 lan-ubuntu]。

- **机器面实查**:`herdr machine list` 取 label、ssh target 与会话名(它是连接 profile 清册,不是跨机 pane 清单,`--json` 供脚本取);profile 的增删启停仅在用户明令时做,删 profile 只断客户端不断远端会话
- **ID 与名都 scoped 单机**:两台保存机可各有 `w1:p1` 或同名 agent;跨机派单地址 = 机器 label 加**该机** agent list 实查的 pane ID,继承的本地 ID 与 `--current` 不识别远程 pane [实证: herdr 0.9.1 --skill 直读]
- **TUI 选机不重定命令向**:TUI 里选了机器,不改变 pane 内命令的目标;无 `--machine` 前缀的 herdr 命令恒走继承的本地 session 与 socket 语境,别被 TUI 选择态误导 [实证: herdr 0.9.1 --skill 直读]
- **命令路由**:`herdr --machine <label-or-id> <agent|pane 子命令>` 把 list/prompt/read/get/wait 原样路由到远程机器,四步协议与状态门控同形跨机;selector 必须是 enabled 保存 profile 的 ID 或唯一(大小写敏感)label,不是任意 SSH 主机名;**不与 `--session`、`--remote` 组合**(报 cannot be combined,勿试);add 默认接远端默认会话,显式 `--remote-session` 才覆盖
- **转发前提与边界**:双侧安装都要支持 machine API 转发,远端 server 必须已在跑且 API 兼容;转发不安装、不起、不重启远端 server,不回落本地;本地配置、会话管理、安装命令、交互附着不转发;跨机 workspace 的远端 worktree 路径必须绝对或 `~` 起,插件链接路径必须绝对 [实证: herdr 0.9.1 --skill 直读]
- **派单前双查**:归属轮或跨机协作轮开工前,本机 `herdr agent list` 与 `herdr --machine X agent list` 各跑一次,两侧工位清册都从 JSON 响应取,不假设编号全局唯一、不凭旧档
- **跨机周知**:维护归属、标准变更这类全 fleet 周知,收件人 = 本机全部在职工位加每台远程机器的工位,双侧都要留回执;给远程工位的 prompt 必须自包含其够不到的路径(如远程机器上的仓库路径要写清在哪台机、怎么到达)
- **失败不证未应用**:跨机连接失败不证变更未落远端(同 prompt 超时族),重试前先查远端实态;setup 遇不兼容 server 先问用户,默认 No,不经同意不批准替换 [实证: herdr 0.9.1 --skill 直读]
- **stalled 误报处置**:跨机 prompt 可能报 `agent_prompt_stalled`(CLI 观察窗内未见 working/blocked 态),文本往往已送达且 agent 正常回执;处置 = `herdr --machine X agent read` 实读 pane 确认送达与回执,确认前不重发,防重复派单

## 四步协议

### 派单

- **prompt 自包含**:任务清单逐件可判(过/缺/不适用)加标准权威路径加回执格式;接收方没有派发方的上下文
- **状态门控先行**:派单前 `herdr agent get <工位>`(跨机 `herdr --machine <label> agent get`)判 agent_status:idle 与 done 直派;working 不硬注入,先 `herdr agent wait <工位> --until idle --until done --until blocked --timeout <租约余量毫秒>` 排队候位或走插队条;blocked 被拒收(agent_blocked)属常态,查 UI 问用户再动;unknown 不派,`herdr agent explain <工位>` 排查检测态
- 正式派单恒走 `herdr agent prompt <pane> "<任务>" --wait --timeout <毫秒>`:原子提交文本加编码 Enter,**提交与等待同一请求**(避开先 prompt 后 wait 的空窗);--wait 自带活动闸门,非 working 态提交后 5 秒内未见 working 或 blocked 活动即 `agent_prompt_stalled`,见到活动后才等收束态(默认 idle、done、blocked);提交时对方已在 working,其在跑轮收束即可满足等待,插队完成甄别见插队条;对 blocked 工位拒收(agent_blocked),先查 UI 问用户再动;超时与 stalled 都不证未送达 [经验: 2026-10-02 官方 Agent automation 与 Socket API 语义,首跑回填]
- **开工探针**:甄别真开工用 `herdr agent wait <工位> --until working --timeout <毫秒>`,已在跑立即返回;turn 短于探针启动则探针必超时,失败不证任务失败、不证上一句未送达;本地热工位秒级即可,冷启动与远程放宽(活动闸门窗为 5 秒级)
- pane send-text 仅草稿不提交,不用作派单通道
- 插队向 working 工位发单可以,但回执以 commit sha 加 diff 范围甄别,防混入在跑轮次
- 纯讨论轮(不改仓不提交)用于标准征求意见,结论按吸收即提炼回标准文本,不点名来源仓

### 回执

- **事件驱动收执**:正式派单的 --wait 已含收束等待(见派单节);插队单与补等走独立 `herdr agent wait <工位> --until idle --until done --until blocked --timeout <毫秒>` 阻塞等收束事件(现态已命中即返不空等;`--until` 逐态重复给旗标、或关系,逗号串无效;不要审批提前收束就只给 `--until idle --until done`;prompt 上的 --until 须搭配 --wait),返回即 `herdr agent read` 收回执,不靠人工记挂与轮询清册
- **超时兜底**:wait 必带 timeout(省略即无限期;超时是调用方租约,不改写 agent 状态);超时与服务器错误 JSON 走 stderr、退出码 1(语法错误退出码 2),成功时当前 agent 在 `.result.agent`;处置 = 看 error.code 加 `agent get` 判现态加 `agent read` 实读判送达,确认送达前不重发(超时不证未送达,重投可能跑两遍;与 stalled 处置同源);timeout 不超租约余量,连续超时即失联判据成立,按租约改派走(references/parallel.md);wait 钉住解析时的窗格占用者,窗格中途移走以 `agent_not_running` 结束,改用新 pane_id 或 agent 名重等 [经验: 2026-10-02 官方口径,首跑回填]
- **审批与提问面**:等审批用 `herdr agent wait <工位> --until blocked --timeout <毫秒>`,`agent read` 实读界面后 send-keys 送键处置或问用户,不代答
- `herdr agent read <pane> --source recent-unwrapped --lines <N>` 收回执;长响应在备用屏读不全时,兜底请对方落临时 md 文件回路径再直读(仅兜底,初版派单不预设文件回执)
- **对方陈述不作数**:commit sha 自取 git log、门禁自跑取退出码(落盘直跑,不接吞退出码管道)、CI 自取 gh run conclusion
- 断言带原文证据:说某文本「仍是旧口径」必须引读到的行,grep 反证优先于口头回执 [实证: 六仓轮中一次旧文误报被 grep 反证]
- 零改动回执合法,不强制造提交;不适用面一句裁定留痕即可

### 断言

- 总台对回执逐项独立复核:工位自证加总台实查对账(如行尾统一轮:工位自证三项,总台独立复核吻合)
- 复核不过打回重证,不采信口头补述

### 吸收

- 每轮回执中的标准反馈当场分流:文案缺口直改、机制缺口进 ROADMAP 积压、不可逆裁定立 ADR
- 工位实踩提炼成纪律条目回写本 skill(references/pitfalls.md),复利即在此

## 并行派单与义务图

多工位并行轮按义务图运转;纪律沉淀自外部多 agent 协作系统的核验对照,本飞轮尚未整轮实测 [经验: 2026-09-17 外部系统技术手册核验],首跑后回填实证。操作细化见 references/parallel.md。

- **台账只记还欠什么**:并行轮总台账记义务与验收判据,不记谁在干;工位每轮收尾重读台账取最新态,不依据开工时的旧图工作,防过期依赖
- **条件归约先接线**:上层义务不等下层完工,先交「只要 A、B 成立则 G 成立」的条件断言;连接正确性与子结果正确性分开验收,上下层真并行。推论:父件无缺不等于依赖闭包无缺,工位局部过门禁不等于全图义务清账,并行轮收尾按闭包清点
- **租约与改派**:工位会话死掉不等于任务作废;约定时限内无心跳即失联改派他位,时限即收执 wait 的 timeout 上限,连续超时加无回执无 commit 判据成立。已交证据与失败记录落仓不落工位,工位消失账不丢
- **依赖变化必重评估**:上游义务变更后,依赖它的下游断言要么附兼容证据复用、要么重跑、要么作废;禁止只改台账链接沿用旧断言
- **扩容前先判瓶颈**:并行度受依赖关键路径封顶;加工位前先判瓶颈是独立任务不够、验证资源不够、还是接口频繁变化致返工,三类对策不同;产量数据(agent 数、提交数、token 数)不是完成证据
- **任务与尝试分开记**:同一义务允许多工位多路线并行攻坚,不靠禁并行避冲突;完成归属以验收判据甄别,先过验收者记账,后到者不覆盖已成立的完成态

## 命令面要点

活权威 = 本机直跑 `herdr --skill`,安装版二进制是语法权威,不凭记忆写命令。常用面:herdr agent list 实查工位;herdr agent get 查态;herdr agent prompt 派单;herdr agent wait 等状态事件(--until 逐态重复旗标加 --timeout 兜底);herdr agent read 收回执;herdr agent send-keys 发逻辑键(esc、ctrl+c)。普通进程与文本事件不走生命周期,用 `herdr pane wait-output <pane> --match <文本> --timeout <毫秒>`(或 `--regex`,即时搜最近约 80 行展开快照,已有文本也命中)。ID 与状态一律从 JSON 响应取,不从侧栏顺序或示例推导。

## 参考

- references/pitfalls.md:治理操作坑实录(send-text 草稿、工位编号漂移、checkout-index 假成功、racily-clean 整片 M、备用屏读不全、yolo 带起时序、跨机器 stalled 误报与编号不全局唯一),按现象、根因、修法三段收录
- references/parallel.md:并行派单与义务图操作细化(台账五字段、条件归约派单写法、租约改派、任务与尝试记账、重评估三选一、瓶颈三判、四步协议映射)
- 开发模式(窗格布局定式、评审闸门、自省验收、lane 任务分发)是跨仓协议的开发特化,见同插件 skill `evo-herdr:herdr-dev`(ADR-0011 起,ADR-0019 双模式定形)
