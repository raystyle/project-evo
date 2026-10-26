---
patterns: [双端加载, 项目级技能, 隔离轮, 验证轮, CLAUDE_CONFIG_DIR, CODEX_HOME, transcript 过滤, 挂接]
---

## distil 双端执行面指导

- 标准件的家在项目仓(唯一权威源);Claude Code 项目级 `.claude/` 面挂接(仓内 .claude 整体 ignore 的存量仓先以忽略登记划界);Codex 走 `.codex-plugin/plugin.json` skills 挂接或 `$CODEX_HOME/skills` 符号链接(链接只是视图)
- 批 176 形:Claude Code 端标准 hook rule 件挂 hook_rules 树(加载器自动扫,加件即生效);同一份 md 双端可读(非 hook 端直读文件)
- 验证轮隔离:闸门只对候选标准集评分,agent 恰好看见候选集不带用户级技能与记忆,私有 `CLAUDE_CONFIG_DIR` / `CODEX_HOME`;凭据副本不进项目 git;每回合按当前候选集重建挂接
- transcript 资格过滤:回合收束先归一(首行记 backend/tool_call_count/message_count),零工具调用回合是假证据
- 命令面活权威是本机实查,不照抄外部文档句子
