# ProjectEvo

> 一句话定位：项目治理插件仓。一个插件 `project-evo`，四个治理面 skill：`dev-evo`（文档体系治理）、`super-research`（资料检索治理）、`secret-scan`（密钥隐私治理）、`security-audit`（安全审计治理）。客户端显示 `project-evo:<skill>`。

## 安装

市场名 `projectevo`，源 `raystyle/projectevo`；市场内只有一个插件 `project-evo`，装它即得四个 skill。

| 客户端 | 命令 |
|--------|------|
| Claude Code | `/plugin marketplace add raystyle/projectevo`，再 `/plugin install project-evo@projectevo` |
| Codex | `codex plugin marketplace add raystyle/projectevo`，再 `codex plugin add project-evo@projectevo` |
| Grok | `grok plugin marketplace add raystyle/projectevo`，再 `grok plugin install project-evo@projectevo --trust` |
| Kimi | 无插件市场：按 `~/.kimi-code/config.toml` 的 `extra_skill_dirs`（默认 `~/.kimi/skills`）拷 `plugins/project-evo/skills/*` 四个目录；斜杠命令与 hook 不随行 |

开发态（指向工作树，改动即生效，免推送）：把 `marketplace add` 的源换成仓根路径，如 `/plugin marketplace add D:\ProjectEvo`。

## 升级

升级 = 刷新市场快照再更新插件；插件按 manifest 版本号归位缓存，版本号不变则不刷新。

```text
Claude Code   /plugin marketplace update projectevo   /plugin update project-evo@projectevo     (重启会话生效)
Codex         codex plugin marketplace upgrade        codex plugin add project-evo@projectevo
Grok          grok plugin marketplace update          grok plugin update
Kimi          重新拷 plugins/project-evo/skills/*
```

旧版本缓存不自动清，按目录手动删：`~/.claude/plugins/cache/projectevo/project-evo/<版本>`、`~/.codex/plugins/cache/projectevo/project-evo/<版本>`。

## 配置

- 市场源与协议：HTTPS 与 SSH git URL 都收；GitHub 简写默认协议相反，Claude Code 走 SSH（`CLAUDE_CODE_PLUGIN_PREFER_HTTPS=1` 切 HTTPS），Codex 走 HTTPS；Grok 另收本地路径与 `@ref`、`#subdir`
- 私有仓认证：标准 git 凭据（credential helper 或 ssh-agent），与终端 git 行为一致
- 钉版：Claude Code `raystyle/projectevo@v0.6.0`（或 URL 尾 `#v0.6.0`）；Codex `--ref v0.6.0`
- md 禁字挡板：装插件后编辑 markdown 触发 PostToolUse 提醒（四类禁字，规则唯一权威是 skill 内 `mdrules.py`）
- 扫描豁免：secret-scan 的误报走目标项目环境变量 `PEVO_SCAN_ALLOW`（分号分隔正则，匹配 文件:行）

## SKILL 介绍

| skill | 做什么 | 何时用 |
|-------|--------|--------|
| `dev-evo` | 文档即代码体系：契约在代码、文档是投影；AGENTS 极简五节合同、ADR 架构决策记录、REQ 需求登记与 trace 回填、生成投影纪律、三栈机制对照（Rust/Python/TypeScript）、diary 与 research 档案、六态标记；附 init/check/scan 零依赖脚本 | 新项目建文档即代码体系、存量迁移、写 AGENTS 合同、立 ADR/REQ、配 API 文档工具链 |
| `super-research` | 资料检索管线：gh 搜代码与仓库、bh 搜 Google/Medium/X、aria2c 取件、reader 研读；结论落 `docs/research` 并标六态 | 找论文与文章、查 X 与 GitHub、下大文件、读电子书 |
| `secret-scan` | 密钥与隐私扫描：工作区、git 全历史、GitHub alerts 与 code search；命中一律脱敏 | 查泄露、凭据轮换前体检 |
| `security-audit` | 安全审计与漏洞审查（译自 Cloudflare security-audit-skill，MIT）：防御性源码优先，双模式（指导/全量审计），信任边界、覆盖账本、猎手波次、独立验证、结构化报告 | 安全问题、聚焦安全审查、渗透测试、漏洞研究、需要审计报告产物时 |

斜杠命令（Claude Code 面）：`/project-evo:init`、`/project-evo:check`、`/project-evo:scan`、`/project-evo:secret-scan-cli`。脚本可免插件直跑，具体命令见各 skill 的 SKILL.md 与 `plugins/project-evo/README.md`。

## 环境前提

- skill 本体纯 Markdown；脚本零第三方依赖（PEP 723，>=3.12，`uv run` 或系统 python）
- 检索与验证命令按 PowerShell 7、ripgrep、reader 实测
- 平台：Windows 主开发；文档与用例按三平台适配撰写（`plugins/project-evo/skills/dev-evo/references/env-platform.md`）

## 文档导航

| 文档 | 讲什么 | 何时看 |
|------|--------|--------|
| `AGENTS.md` | 开发协作规则唯一权威源 | 写/改任何文件前 |
| `plugins/project-evo/README.md` | 插件说明（前置、安装、三 skill 用法、敏感产物） | 用插件面时 |
| `plugins/project-evo/skills/dev-evo/SKILL.md` | dev-evo skill 本体（意图路由） | 使用/修改 skill 前 |
| `docs/README.md` | 全仓文档地图 | 找任何文档时 |
| `ROADMAP.md` | 阶段与里程碑状态 | 看进度时 |
| `CHANGELOG.md` | 变更日志 | 查历史时 |
