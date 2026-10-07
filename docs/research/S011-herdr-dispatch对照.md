# S011:herdr-dispatch 任务分发编排对照

> 信源:bestony/herdr-dispatch(Claude Code 加 Codex 插件,2026-10-02 快照;四 skill:dispatch-codex、dispatch-grok、dispatch-opencode、dispatch-antigravity)。对照对象:本仓 evo-herdr:herdr-flywheel 与 herdr-review。结论六态标注,信源点名止于本档案。

## 上游形态

- 纯 skill 插件(全 md,零脚本文件):编排程序以纪律条文呈现,python3 与 jq 只作内联探针(状态 JSON 读写、rollout JSONL 解析);skills.sh 单 skill 拷装,共享 halves(_shared/plan 与 supervise)经 symlink 单源
- 编排分工三句:Claude 计划(每 lane 计划与验收判据,用户确认后开建)、agent 执行、Claude 发布(lane 恒禁 push/merge/PR,发布是总台验收后的独占动作,只做可加可逆的事)
- lane 模型:每任务一 git linked worktree 加独立分支加独立 herdr workspace/pane 加一个 agent(codex、grok、opencode、agy 四驱动);基线取 origin/<branch> 先 fetch
- 状态文件唯一真相:`~/.claude/<skill>/<run-id>/state.json`,开工先记 run id 与 orchestrator_pane($HERDR_PANE_ID);原子写(.tmp 加 mv);每 sweep 开头重读(抗会话 compaction)
- 探针契约:driver 每 lane 必报 session、turn_state、used_pct、compactions、mtime、probe 六字段;缺字段报 null 不猜;盘上记录(codex rollout JSONL)优先,屏幕是回退
- 身份核验:agent 名可被回收复用(退出即释放),steer 前必对 session id;名对不上停手诊断
- done 假象:agent_status 的 done 与吞 prompt、冻结、modal 误分类同形;active goal 的 turn 间隙也读 done;完成判据 = 验收过、分支推、PR 开
- 扫描循环:全队探查、答 help ring(先答后分类)、逐 lane 分类行动、收尾写状态;定时器兜底回铃
- agent 启动特化:codex goal 模式(/goal 不能随 argv,先启动后经 agent prompt 下)、--no-alt-screen 保 scrollback、status_line 强制 context-remaining、--timeout 120000 冷启动、审批旁路默认开;grok 有 doctor 与本机 user-guide 文档面
- 版本探针:pane 里跑 `<cli> --version` 而非 command -v(asdf shim 可解析而真二进制不在,agent start 从 pane 登录 shell 解析,args 不能重定向);pane 无 run 子命令,send-text 加 send-keys enter 两步

## 对照分流

- 等价不吸收:JSON 判据优先、勿动非自建、超时不证未送达、blocked 问用户、命令语法活权威(本仓 herdr --skill 口径同源)
- 真新增吸收(进 herdr-flywheel):lane 分发模型(worktree 加分支加独占发布)、状态台账纪律(唯一真相加原子写加 sweep 重读加探针契约)、身份核验(session 对账)、done 假象细分、help ring 先答后催、多 agent kind 启动特化与版本探针、HERDR_PANE_ID 总台坐标
- 留档不吸收:skills.sh 分发通道、symlink 单源形(本仓用市场双 manifest 面)、antigravity 与 opencode 驱动细节(本 fleet 未用,布局定式篇记品类即可)
- kimi 委派:上游无 kimi 驱动,无成熟参照 [实证: 上游仓库树全量核对];kimi 委派待专项研究其 CLI 非交互能力后再定,不臆造

## py 脚本评估结论:是否针对性开发集成 herdr 的 py 脚本

**不开发** [经验: 上游同场景实证纯 skill 够用]。理由:上游零 .py 文件跑通全链(探针与状态机是 python3/jq 单行);本仓沉淀铁律(手拼二犯才升格脚本)未触发;py 包装层会藏住 herdr CLI 活权威语义(herdr --skill);插件面刚收敛为纯知识加 hook,引入脚本面与解耦方向相反。触发重评估的条件:探针/扫描循环手拼二犯,或 state 台账复杂到单行不可读。
