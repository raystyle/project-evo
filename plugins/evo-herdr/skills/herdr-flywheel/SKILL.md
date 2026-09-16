---
name: herdr-flywheel
description: >-
  多仓 herdr 飞轮协作治理:一个总台协调多个单仓工位,派单、回执、断言、吸收四步循环。
  涵盖 herdr agent prompt 原子派单、agent read 收回执、独立复核断言、反馈吸收分流、
  工位带起顺序与治理操作坑。本 skill 是该协议唯一权威源;herdr 命令语法的活权威是本机直跑 herdr --skill。
  Use when 跨仓派发治理任务、收 herdr 工位回执、做总台轮次协调时;触发词 herdr、飞轮、
  派单、回执、工位、多仓治理。
compatibility: 需 herdr 管理的工位会话(HERDR_ENV=1);各工位侧仓自带门禁
---

# herdr 飞轮多仓协作

> 一个总台协调多个单仓 herdr 工位(仓加 workspace 加 pane 加常驻 agent 会话),派单、回执、断言、吸收四步循环。沉淀自 2026-09-16 六仓四轮实证(对齐、标准态、终态、扩编与讨论)与后续实践轮。

## 工位形态与带起

- 每仓一个 herdr 工位,总台自成工位;派单地址 = pane ID,从 herdr agent list 的 JSON 响应取,不猜不背;live 唯一的 agent 名亦可作地址
- **工位编号会漂移**:合同与旧档写的编号不可信,派单前必 herdr agent list 实查 [实证: 2026-09-16 合同写法与实况两轮不符]
- **带起顺序 = hst init --yolo 先于 agent 驻场**:会话许可模式在驻场时定格,后落盘的 yolo 不被追认,全会话停在旧审批态致阻塞 [实证: 2026-09-16 八工位驻场先于 yolo 落盘,全会话审批阻塞];可提 hst doctor 增加「会话活模式与盘上 yolo 一致性」检测项
- idle 与 done 皆可派;blocked 是等人裁,问用户不代答;working 可插队,回执甄别见派单节
- 勿关非自建工位(workspace、tab、pane、session)

## 四步协议

### 派单

- **prompt 自包含**:任务清单逐件可判(过/缺/不适用)加标准权威路径加回执格式;接收方没有派发方的上下文
- 正式派单恒走 `herdr agent prompt <pane> "<任务>" --wait --timeout <毫秒>`:原子提交文本加编码 Enter,--wait 等首个 settle 态(idle、done、blocked);对 blocked 工位拒收(agent_blocked),先查 UI 问用户再动
- pane send-text 仅草稿不提交,不用作派单通道
- 插队向 working 工位发单可以,但回执以 commit sha 加 diff 范围甄别,防混入在跑轮次
- 纯讨论轮(不改仓不提交)用于标准征求意见,结论按吸收即提炼回标准文本,不点名来源仓

### 回执

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

## 命令面要点

活权威 = 本机直跑 `herdr --skill`,安装版二进制是语法权威,不凭记忆写命令。常用面:herdr agent list 实查工位;herdr agent prompt 派单;herdr agent read 收回执;herdr agent get 查态;herdr agent send-keys 发逻辑键(esc、ctrl+c)。ID 与状态一律从 JSON 响应取,不从侧栏顺序或示例推导。

## 参考

- references/pitfalls.md:治理操作坑实录(send-text 草稿、工位编号漂移、checkout-index 假成功、racily-clean 整片 M、备用屏读不全、yolo 带起时序),按现象、根因、修法三段收录
- 推送前评审闸门(评审请求、F/G/CONFIRM 回执、轮次至终审放行、评审窗格检测带起)是飞轮协议的评审特化,见同插件 skill `evo-herdr:herdr-review`(ADR-0011)
