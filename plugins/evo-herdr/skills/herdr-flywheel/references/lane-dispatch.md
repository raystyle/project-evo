# 任务分发 lane 模型(多 agent 并行产出)

> 一次把多个实现任务分发给多 agent 并行产出(分支加 PR 收尾)时的飞轮特化。四步协议(派单、回执、断言、吸收)与状态门控同形;本篇管 lane 专属面:worktree 与分支、状态台账、探针契约、身份核验、agent 启动特化、发布纪律。多 agent 并行治理协作(非产出分支)仍走 parallel.md 义务图。

## lane 结构

- 每 lane = 一任务:git linked worktree 加独立分支加独立工位(workspace 加 pane 加 agent);从主检出建,不在 linked worktree 里再开
- 基线先 `git fetch origin` 取 `origin/<分支>`,无远端用本地分支并在计划里说明
- 总台自居一格,坐标取 `$HERDR_PANE_ID` 记进台账;lane 回铃指名总台格,不让 lane 自己找

## 状态台账(唯一真相)

- run 级台账:`~/.claude/<skill 名>/<run id>/state.json`;开工先记 skill、agent kind、repo、基线、总台格坐标、每 lane 的名与 session
- **原子写**:写 .tmp 再 mv;每轮 sweep 开头重读台账再动手(会话记忆可能已被压缩,台账是唯一真相)
- 同仓已有非终态 lane 的旧 run 不静默开新 run,问用户续跑、归档还是废弃

## 探针契约

每 lane 探针必报六字段,缺字段报 null 不猜:

| 字段 | 含义 |
| --- | --- |
| session | agent 自己的会话 id(台账记录值) |
| turn_state | working(轮次在飞)/ complete(末轮已收)/ unknown |
| used_pct | 上下文窗占用百分比,不发布则 null |
| compactions | 该线程已压缩次数 |
| mtime | lane 盘上记录的末次写入(停滞检测) |
| probe | ok / unavailable 加原因 |

盘上记录优先(agent 自己的会话 JSONL:token 用量、轮次边界、压缩记录),屏幕输出是回退不是主信号。

## 身份核验与完成判据

- **名可回收**:agent 退出即释放名,后来者可复用;steer(prompt、send-keys、compact)前必 `herdr agent get` 对 session id 与台账一致,不一致停手诊断
- **done 不证完成**:吞单、冻结、modal 误分类、goal 型轮次间隙都读 done;lane 完成 = 验收判据过、分支已推、PR 已开
- **help ring 先答后催**:lane 求助铃先答(答案出自总台写的计划),再进分类处置

## agent 启动特化

- **版本探针**:pane 内跑 `<cli> --version`(不是 command -v:asdf shim 可解析而真二进制缺位,agent start 会超时);agent start 从 pane 登录 shell 解析可执行,命令参数不能重定向解析路径
- **环境预检**:新 worktree 无 node_modules、.env、.venv;依赖缺失先在 pane 跑安装并等收;secrets 缺失问用户是否 symlink,绝不拷贝
- codex 类 goal 驱动:无位置参数启动,goal 走斜杠命令不能随 argv;`--no-alt-screen` 保 scrollback 可读;status_line 强制 context-remaining 形;冷启动超时放宽(120 秒级);审批旁路默认开(无人值守轮审批浮层会卡 lane),用户明令保守时才继承用户审批配置
- grok 类:有 doctor 体检命令,首格终端异常时跑一次;新会话先 pane wait-output 等就绪标志再派
- pane 无 run 子命令:send-text 加 send-keys enter 两步,pane read 读果

## 发布纪律

- **lane 恒禁 push/merge/开 PR**:发布是总台在验收后的独占动作,只做可加可逆的事(推 lane 自己的分支、开它的 PR)
- 永不 force-push、永不推基线分支与台账外的分支、永不 merge、永不 worktree remove(杀进程删未提交改动);这些命令打印给用户自己跑
- **发布预检开工时定**:origin 与 gh 可用性在开建任何 workspace 前查清记台账;缺 gh 则推分支后把开 PR 命令打印给用户;缺 origin 则 lane 留本地如实报告;绝不代装代认证
