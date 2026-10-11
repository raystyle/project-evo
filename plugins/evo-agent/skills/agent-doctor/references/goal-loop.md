# goal 与 loop 状态面

> goal 归 hst 自治面(项目级自有存储);loop 已从 hst 退役(2026-10-11 用户令「hst 不再关联 goal 和 loop」),归 Claude Code 原生 CronCreate 与 ScheduleWakeup 域。本面是查看与管理手册。

## goal 面

```bash
hst goal show          # 查看本项目 goal(无 goal 给 goal.present=false,即缺省默认态)
hst goal set "<目标>"   # 设置:自有存储覆盖旧 goal,rounds 重计
hst goal clear         # 清空:Stop 提醒与状态栏段随撤;无 goal 零改动退 0
hst goal heal          # 自愈唤醒扫描(goal-01):须在 herdr 会话格内跑
```

- 提醒机制:claude Stop 事件每轮提醒(rounds 计数落盘、自然停一轮 decision block、stop_hook_active 防环放行)
- 同源显示:状态栏 goal 段与 show 同源;doctor 的 goal check 报 stop goal-hook registered 与 project goal 有无
- 缺省默认态:`goal.present=false` 是合法稳态,不是病;要不要设 goal 属人裁
- heal 纪律:goal 在册而格位停摆未被 Stop 唤醒过 15 分钟静默窗才唤醒(经 herdr agent prompt 附用法);working 与 blocked 等人裁态豁免;连续 3 次唤醒无 rounds 增长即风暴闸转人工

## loop 面

> Claude Code 原生域:会话内 cron(CronCreate/CronList/CronDelete)、durable 件(`~/.claude/scheduled_tasks.json`,跨会话存活)、动态自调度(ScheduleWakeup,-dynamic 变体)。hst 无 loop 面,别去 hst 找。

- 查看现状:会话内 `CronList`;盘上读 durable 件(无件 = 无跨会话任务)
- 会话内任务随会话死;durable 任务跨会话,改用 CronDelete 清
- 动态 loop(ScheduleWakeup)状态在会话内,盘上无痕;判定看会话输出与 `/loop` 状态
- recurring 任务 7 天自动到期(末次触达后清),长期任务要续期登记
- 诊断问题三连:任务没火 = 会话是否 idle(任务只在空闲时入队)+ durable 是否落盘 + cron 表达式本地时区对不对

## 与诊断面的合流

- `hst doctor` 的 goal check 与本面 show 同源,doctor 过 + show 可解释即 goal 面健康
- loop 面无 doctor 位:判定只靠 CronList 与 durable 件双查;发现孤儿 durable 任务(对应会话已死)即清
