# 2026-10-02:herdr-review 对话状态门控

> 当日主线:用户令 herdr-review 的对话状态判断方式参考飞轮第八十五批同款改进;第八十六批把状态门控、事件驱动收件、超时兜底套上评审闸门工作流。

## 第八十六批:评审对话四步配方

- 改造点定位:herdr-review 的对话状态面在三处,panes.md 第二节 4(直接对话两步形 prompt 加 read)、检测分派行(缺 unknown 路径)、receipt.md 收件行(idle 才收件,无机制);request.md 与 findings.md 无状态面不动
- 落位:对话配方升四步(get 判态五路、prompt --wait 同请求等待、wait 收束事件兜底、read 备读);分派行补 unknown 走 explain;收件纪律挂机制(wait 返回后再 read,idle 与 done 皆可收);SKILL 命令块加 get 与 wait 两形,路由表加判忙闲行;特化不重述原则保留(细则全部指回 herdr-flywheel)
- 实证准入:本轮零新命令形,get 与 wait 形即第八十五批本机实跑记录(herdr 0.9.1),panes.md 篇头实证注随写实情(挂位带起 2026-09-16,对话状态件 2026-10-02)
- 同步面:herdr-review 括号描述三处逐字同加「对话状态门控与事件驱动收件」、codex 长描述、evo-herdr README、docs 地图;版本线四插件 0.4.2 齐 0.4.3
- 留档:评审格 blocked 等审批加 send-keys 处置形、评审轮逐轮 wait 收件形尚无实战,首跑回填(沿飞轮同款中转态口径)
- 二犯追正(用户令):「skill 内容不带历史轨迹」为第二次提示;实查 skill 正文零批号,违规处是 panes.md 篇头被我写成两代年代分割形(挂位带起某日,对话状态件某日),已收敛为「命令均本机实证」无年代形;批号与年代轨迹只落 diary 与 CHANGELOG,六态实证标记(单点 [实证: 日期] 形)不属轨迹,保留
