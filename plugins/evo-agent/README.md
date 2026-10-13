# evo-agent

> project-evo 治理插件市场第五插件:agent 客户端环境与共享能力。市场 `raystyle/project-evo`,客户端显示 `evo-agent:agent-doctor`、`evo-agent:agent-s5`、`evo-agent:agent-rloop`、`evo-agent:agent-prim`。

第一 skill **agent-doctor** 三面:

- **配置诊断修复面**:`scripts/config-lint.py` 静检四端配置(claude 的 settings.json 与 settings.local.json、codex 与 grok 的 config.toml、kimi 的 config.toml 与 skills 安装面),判据两级(error = 解析失败、枚举非法、绝对路径缺失、高置信秘密形态、grok 悬空引用;advisory = 文档容忍态的 claude 悬空引用、未知字段、用户面明文凭证、卸载配置残留),只报不改,`--json` 机读,`--kimi-source` 漂移对账,豁免 `PEVO_CONFIG_LINT_ALLOW`;修复手册随判据表
- **hook 诊断修复面**:hst doctor 的 hooks.form 与 trust.hooks 诊断、hst init 幂等重部署(dead 或 absolute shim 即重跑)、codex trusted_hash 时效核对、kimi 双 OS 形共存判读
- **goal 与 loop 状态面**:hst goal 项目级 set/show/clear/heal 与缺省态(present=false)、Stop 每轮提醒 rounds、状态栏 goal 段同源;loop 归 Claude Code 原生域(CronList、`~/.claude/scheduled_tasks.json` durable、ScheduleWakeup 动态态;hst loop 已退役)

定位 = **增强 hst doctor**:hst doctor 管运行时诊断(yolo、trust、binary、state、登录态、hook 形态、状态栏),本 skill 补静态度判据与修复手册与 goal/loop 面;hst 只认 PATH,不改其源。判例源:2026-10-12 五端插件清扫病灶族加研究档 cfg-01 官方文档对照。ADR-0023 与 REQ-021 在册。

第二 skill **agent-s5**:工作台 agent 的 s5 全局看板与频道操作面:文件道(S3 形 put/get/ls/del)当全局文件看板,流道(S2 形 append/tail/streams)当全局流消息频道;命令面活权威 `s5 --llms`(装位为舰队惯例注记(win 与 linux 各一位,本机以 command -v s5 实查为准),零感知凭据,agent 永不接触钥);看板 `board/<工作台>/<主题>/` 与频道 `channel/<频道>` 命名约定、跨台读写规约(写者拥有、del 不越权、append-only、tail 取阅不回写);与 herdr 分工:herdr 管信号与消息,共享内容一律走本 skill(含飞轮轮次三件套上云,rounds 与 research 与 streams 键空间随并入)。REQ-022 在册,批 124 并入 herdr:s5。

第三 skill **agent-rloop**:目标驱动的多角色循环进化任务:herdr 定窗格角色后钉 hst goal,按轮派单回执断言吸收,循环到达成或显式停机;防停双层与停机条件入协议,状态在盘上三件套。REQ-023 在册(批 128 迁入,原 herdr-flywheel)。

第四 skill **agent-prim**:舰队互操作五原语操作面:五命令 agents/shares/streams/tasks/pipes 同构文法(全局旗标加动词加位置参数,投递动词统一 `to`),id 三产生式(裸名全局寻址、机:名或格、local: 前缀),隐式路由 local 与 --machine 零感知各端一致;投递与收件三反射(投递只看 status 与 CTA、收件 agents read 自带忙候与超时、拒投自动代记 deferred 补收),门控 v2 = TUI 实况判标族四家(操作对话框拒投、busy 排队不拦)与 status 四态信封(delivered/engine_fail/deferred/stalled),信封三行形取用行纪律,IM 映射(流即房间、DELIVER 即 @、dm/ 与 room/ 前缀、agents view 即 presence)与回执走 streams append fleet;契约单一真源 = ai-ccoe 仓 plugins/CONTRACT.md(对齐 v3:五节加五a/b/c/d;本机实装 prim 3.0.0a1 R0 修件后实态,残余差异表随 skill),本 skill 只路由不复述;与 agent-s5 分工 = s5 是引擎命令面,五原语是骑在其上的协议面。REQ-025 与 REQ-027 与 REQ-028 在册。

## 安装

- Claude Code:`/plugin marketplace add raystyle/project-evo` 后 `/plugin install evo-agent@project-evo`
- Codex:`codex plugin marketplace add raystyle/project-evo` 后 `codex plugin add evo-agent@project-evo`
- Grok:`grok plugin install evo-agent@project-evo --trust`
- Kimi:无市场,拷 `plugins/evo-agent/skills/*` 至 `~/.kimi/skills`

当前发布:0.11.1。版本线随市场五插件同线(ADR-0021 族版本纪律)。
