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

> Claude Code 原生域(hst loop 已退役 2026-10-11)。三套调度分立:云 Routines(机器可关,最短 1 小时)、Desktop 定时任务(本机开着即可,最短 1 分钟)、会话内 /loop(本机加会话都开着,最短 1 分钟);错过的触发不补跑。权威三页:scheduled-tasks、tools-reference、agent-sdk/typescript(code.claude.com/docs)。

- **创建**:`/loop 间隔 提示词` = 固定 cron;`/loop` 只给提示词 = Claude 自选延迟(1 分钟至 1 小时,工具 ScheduleWakeup);裸 `/loop` 读项目或用户 `.claude/` 目录下的 loop 提示件(超 25000 字节截断)。直接要求时用 CronCreate/CronList/CronDelete(8 字符 id),一会话至多 50 条,秒取整到分钟,本地时区
- **触发条件**:只在运行且空闲时触发;关终端或会话退出即停;长请求占点时空闲后只补一次;`CLAUDE_CODE_DISABLE_CRON=1` 全关
- **到期**:重复任务 7 天到期再触发一次后自删;要更长取消重建或改 Routines/Desktop
- **durable 落盘**:`durable: true` 请求写 `.claude/scheduled_tasks.json` 跨重启;以输出 `durable` 字段为准(true 落盘,false 仅会话);CronList 两类同列;`--resume/--continue` 恢复未过期任务(自节奏 loop 不恢复);符号链接 `.claude` 报错,拷到别的 worktree 能列出不会跑
- **ScheduleWakeup**:自节奏每轮末调,delaySeconds 夹 60 至 3600;`stop: true` 终止(须 v2.1.202+);待触发项出现在 Stop hook 输入 `session_crons`;既未重排也未 stop 约 20 分钟兜底再排一次,仍不排即结束;Esc 只清自节奏不清固定间隔
- **诊断三连**:任务没火 = 会话 idle 否 + durable 落盘否 + 本地时区 cron 对否

## 与诊断面的合流

- `hst doctor` 的 goal check 与本面 show 同源,doctor 过 + show 可解释即 goal 面健康
- loop 面无 doctor 位:判定只靠 CronList 与 durable 件双查;发现孤儿 durable 任务(对应会话已死)即清
