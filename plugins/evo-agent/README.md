# evo-agent

> project-evo 治理插件市场第五插件:agent 客户端环境诊断与修复。市场 `raystyle/project-evo`,客户端显示 `evo-agent:agent-doctor` 与 `evo-agent:agent-s5`。

第一 skill **agent-doctor** 三面:

- **配置诊断修复面**:`scripts/config-lint.py` 静检四端配置(claude 的 settings.json 与 settings.local.json、codex 与 grok 的 config.toml、kimi 的 config.toml 与 skills 安装面),判据两级(error = 解析失败、枚举非法、绝对路径缺失、高置信秘密形态、grok 悬空引用;advisory = 文档容忍态的 claude 悬空引用、未知字段、用户面明文凭证、卸载配置残留),只报不改,`--json` 机读,`--kimi-source` 漂移对账,豁免 `PEVO_CONFIG_LINT_ALLOW`;修复手册随判据表
- **hook 诊断修复面**:hst doctor 的 hooks.form 与 trust.hooks 诊断、hst init 幂等重部署(dead 或 absolute shim 即重跑)、codex trusted_hash 时效核对、kimi 双 OS 形共存判读
- **goal 与 loop 状态面**:hst goal 项目级 set/show/clear/heal 与缺省态(present=false)、Stop 每轮提醒 rounds、状态栏 goal 段同源;loop 归 Claude Code 原生域(CronList、`~/.claude/scheduled_tasks.json` durable、ScheduleWakeup 动态态;hst loop 已退役)

定位 = **增强 hst doctor**:hst doctor 管运行时诊断(yolo、trust、binary、state、登录态、hook 形态、状态栏),本 skill 补静态度判据与修复手册与 goal/loop 面;hst 只认 PATH,不改其源。判例源:2026-10-12 五端插件清扫病灶族加研究档 cfg-01 官方文档对照。ADR-0023 与 REQ-021 在册。

第二 skill **agent-s5**:工作台 agent 的 s5 全局看板与频道操作面:文件道(S3 形 put/get/ls/del)当全局文件看板,流道(S2 形 append/tail/streams)当全局流消息频道;命令面活权威 `s5 --llms`(装位 win 的 `D:\ohmyenv\s5\s5.exe`、linux 的 `~/.local/bin/s5`,零感知凭据,agent 永不接触钥);看板 `board/<工作台>/<主题>/` 与频道 `channel/<频道>` 命名约定、跨台读写规约(写者拥有、del 不越权、append-only、tail 取阅不回写);与 evo-herdr:s5 分工(那管跨机治理轮次协议,本 skill 管通用日常读写)。REQ-022 在册。

## 安装

- Claude Code:`/plugin marketplace add raystyle/project-evo` 后 `/plugin install evo-agent@project-evo`
- Codex:`codex plugin marketplace add raystyle/project-evo` 后 `codex plugin add evo-agent@project-evo`
- Grok:`grok plugin install evo-agent@project-evo --trust`
- Kimi:无市场,拷 `plugins/evo-agent/skills/*` 至 `~/.kimi/skills`

当前发布:0.8.0。版本线随市场五插件同线(ADR-0021 族版本纪律)。
