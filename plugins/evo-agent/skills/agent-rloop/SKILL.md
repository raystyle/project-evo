---
name: agent-rloop
description: >-
  目标驱动的多角色循环进化任务:herdr 把多个窗格的 agent 角色放好后,本 skill 给这一组角色钉一个
  目标(hst goal),按轮派单、回执、断言、吸收,循环到达成或显式停机。防停双层:轮内 Stop 事件
  goal 提醒驱动再来一轮,轮外 hst goal heal 静默窗唤醒;停机条件入协议(达成即 clear、人裁
  blocked 不 heal、风暴闸、角色数与轮深上限),缺省不无限转。多角色协同的消息与产物走 s5
  (任务发布 put 上键、结果 get 文本或 tail 实时流,命令面 evo-agent:agent-s5);信号命令活权威
  = 本机 herdr --skill,goal 动词活权威 = hst goal --help。并行轮按义务图运转,状态在盘上
  (三件套 brief/state/receipt 加义务台账),不在模型上下文里。
  Use when 给一组窗格角色立目标开循环、按轮派单收执断言、防停与停机裁定、多工位并行义务图
  对账时;触发词 agent-rloop、rloop、目标循环、角色循环、循环进化、防停、goal、heal、轮次、
  派单、回执、断言、吸收、义务图、并行派单、三件套、brief、receipt、任务上云、键指针、
  实时流取回。
compatibility: 需 herdr 管理的工位会话(HERDR_ENV=1)与各工位侧仓自带门禁;目标循环依赖 hst goal(hook 注册面见 agent-doctor)
---

# agent-rloop - evo-agent 目标驱动的多角色循环

> 闸门记录(批 128,2026-10-12,用户令):由 herdr-flywheel 升格迁入(rloop-01 研究映射,批 111 至 127 沿革见 CHANGELOG);工位带起与跨机器面归并 herdr-orch,s5 命令面在 evo-agent:agent-s5,goal 健康诊断在 evo-agent:agent-doctor。

**核心判据**(rloop-01 先例研究提炼):一项目一个 hst goal,角色分工写进派单笺不各设存储;总台委派、角色回执回总台,对等交接不作默认;**主时钟 = Stop 的「目标未满再来一轮」**,heal 与 Claude /loop 只做停摆回扫不并列第二主循环;停机条件写进协议,缺省不无限转;状态在盘上,压缩或换会话后重读台账。

## 一、角色定式

- 窗格布局(谁在哪个格、什么 kind)不重写,见 `evo-herdr:herdr-orch` 第一节;本 skill 只加一张**角色卡**:格、kind、本轮义务、验收句,落本轮笺内
- 角色数与轮深设上限(沿 AutoGPT 硬顶思路):开工前在笺里写明上限数字,超限拒绝不跑;未定前不开循环
- 工位带起、跨机器路由、信号命令速查归 `evo-herdr:herdr-orch` 的工位面篇

## 二、目标与防停

goal 动词活权威 = `hst goal --help`;诊断条文(判病)在 `evo-agent:agent-doctor` 的 goal-loop 面,本节只管设与清:

1. **开循环**:`hst goal set "<本轮目标>"`(覆盖即重计 rounds,中途改目标等于新开一轮)
2. **轮内防停**:Claude Code Stop 事件 goal 提醒注入,目标未满 decision block 再来一轮;`stop_hook_active` 防环放行
3. **轮外防停**:格位掉进 idle 且 Stop 没拉回来,`hst goal heal`(可先 `--dry-run`;15 分钟静默窗,working 与 blocked 豁免,连续 3 次唤醒无 rounds 增长风暴闸转人工)
4. **收循环**:`hst goal clear`(达成、人裁停、或风暴闸后)
5. 候 hst 发布批:goal 腿注册面扩四事件双挂(Stop 加 SessionEnd 加 Notification 加 PermissionRequest,REQ-047,2026-10-12 落地候推),Stop 后即时循环检测防 idle;落定前防停判据以 `hst goal heal --help` 为准

## 三、循环轮次协议(派单、回执、断言、吸收)

- **交流先分型**:任务型(要产出有验收判据)、委托型(核查调研要结论)、同步型(周知要留痕)三型文件化;讨论型不文件化屏读吸收
- **任务发布走 s5,消息递指针**:任务清单逐件可判落 brief 后 put 上键(`rounds/<YYYY-MM-DD>-<主题短名>/<单号>-brief.md` 形,键空间见 evo-agent:agent-s5 的 naming);herdr prompt 只递单号、键与一句接单指令;本机无 s5 二进制时退回全文内联并记注(兜底)
- **派单门控**:先 `herdr agent get` 判态(idle 与 done 直派、working 排队候位或插队、blocked 问用户、unknown 先 explain);正式派单恒 `herdr agent prompt <工位> "<任务>" --wait --timeout <毫秒>`;开工探针 `--until working`;插队单回执以 commit sha 加 diff 范围甄别;pane send-text 禁作派单
- **回执**:事件驱动收执(--wait 收束即 `herdr agent read`);**结果获取走 s5**:文本结果 get receipt 键逐件对账,实时进展接收方 append 轮次流发起方 tail;三型恒文件回执,会话只回键或路径加一句摘要;屏读收窄到讨论型与兜底
- **断言**:对账以 brief 为基准,盘上是权威、s5 是信道、会话只递指针;对方陈述不作数(commit sha 自取、门禁自跑、断言带原文证据);复核不过打回重证
- **吸收**:标准反馈当场分流(文案直改、机制进 ROADMAP、不可逆立 ADR);轮次收尾共享档择要吸收进仓

三件套模板、状态档检查点、干预矩阵、派单回执坑实录见 `references/rounds.md`。

## 四、多角色义务图

并行轮按义务图运转(纪律源自外部多 agent 协作系统核验对照,本循环尚未整轮实测,首跑回填):台账只记还欠什么;条件归约先接线(连接证明与子结果分开验收);租约即收执 wait 的 timeout 上限,失联改派、证据落仓不落工位;依赖变化必重评估(三选一);扩容前瓶颈三判;任务与尝试分开记,先过验收者记账。操作细化见 `references/parallel.md`。

## 五、停机条件

达成并 clear;人裁 blocked 不 heal 等人;风暴闸转人工;角色数或轮深超笺内上限即停。Claude /loop 的 7 天到期不自动套用到本循环,循环寿命由 goal 与停机条件管。

## 六、参考

| 我要… | 看哪篇 |
| --- | --- |
| 三件套与检查点、干预矩阵、派单回执坑 | `references/rounds.md` |
| 义务图操作细化(台账、条件归约、租约改派、重评估) | `references/parallel.md` |
| s5 命令与键空间 | `evo-agent:agent-s5` |
| goal 健康诊断、loop 原生域 | `evo-agent:agent-doctor` |
| 窗格布局、工位带起、跨机器路由 | `evo-herdr:herdr-orch` |
