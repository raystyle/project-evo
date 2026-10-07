# ProjectEvo

> 一句话定位:项目治理插件市场仓。市场名 `project-evo`,源 `raystyle/project-evo`,两插件三 skill:`evo-doc`(文档治理:doc-gov)、`evo-herdr`(双模式协作:herdr-dev 开发模式、herdr-flywheel 跨仓模式)。客户端显示 `<插件>:<skill>`。

## 安装

市场名 `project-evo`,源 `raystyle/project-evo`;按域装插件,两插件同版本线(ADR-0010)。

| 客户端 | 命令 |
|--------|------|
| Claude Code | `/plugin marketplace add raystyle/project-evo`,再 `/plugin install <插件>@project-evo`(如 `evo-doc@project-evo`) |
| Codex | `codex plugin marketplace add raystyle/project-evo`,再 `codex plugin add <插件>@project-evo` |
| Grok | `grok plugin marketplace add raystyle/project-evo`,再 `grok plugin install <插件>@project-evo --trust` |
| Kimi | 无插件市场:按 `~/.kimi-code/config.toml` 的 `extra_skill_dirs`(默认 `~/.kimi/skills`)拷 `plugins/<插件>/skills/*`;斜杠命令与 hook 不随行 |

开发态(指向工作树,改动即生效,免推送):把 `marketplace add` 的源换成仓根路径,如 `/plugin marketplace add /mnt/wsl/repos/project-evo`。

## 升级

升级 = 刷新市场快照再更新插件;插件按 manifest 版本号归位缓存,版本号不变则不刷新。两插件同版本线,升级时逐插件 update。

```text
Claude Code   /plugin marketplace update project-evo   /plugin update <插件>@project-evo     (重启会话生效)
Codex         codex plugin marketplace upgrade         codex plugin add <插件>@project-evo
Grok          grok plugin marketplace update           grok plugin update
Kimi          重新拷 plugins/<插件>/skills/*
```

旧版本缓存不自动清,按目录手动删:`~/.claude/plugins/cache/<市场>/<插件>/<版本>`、`~/.codex/plugins/cache/<市场>/<插件>/<版本>`。

**从旧市场 projectevo 迁移(破坏性)**:先卸载旧市场(`/plugin marketplace remove projectevo`)再按上方命令加 `project-evo` 装插件;旧缓存目录 `cache/projectevo/` 与已下线插件的缓存目录可整目录删除。

## 配置

- 市场源与协议:HTTPS 与 SSH git URL 都收;GitHub 简写默认协议相反,Claude Code 走 SSH(`CLAUDE_CODE_PLUGIN_PREFER_HTTPS=1` 切 HTTPS),Codex 走 HTTPS;Grok 另收本地路径与 `@ref`、`#subdir`
- 私有仓认证:标准 git 凭据(credential helper 或 ssh-agent),与终端 git 行为一致
- 钉版:Claude Code `raystyle/project-evo@v0.10.0`(或 URL 尾 `#v0.10.0`);Codex `--ref v0.10.0`(下一封版 v0.11.0 后同理)
- md 禁字挡板:装 evo-doc 后编辑仓内 markdown 触发 PostToolUse 提醒(四类禁字,仓外 md 不管;规则唯一权威是插件级 `scripts/mdrules.py`,与 skill 解耦)
- 扫描豁免:本仓 `.tools/scan.py` 的误报走环境变量 `PEVO_SCAN_ALLOW`(分号分隔正则,匹配 文件:行)

## 插件与 SKILL 介绍

| 插件 | skill | 做什么 | 何时用 |
|------|-------|--------|--------|
| evo-doc | `doc-gov` | 文档框架治理知识:ADR(需求决策:ADR 与 REQ)、COE(三层聚合与双向链接图)、项目日记三类文档形态;Agent 友好 CLI 架构标准(--llms 手册、CTA 协议、帮助面、自省、裸调用面、发现通道) | 立 ADR/REQ、写项目日记、建 COE 知识库操作台、配 CLI agent 面 |
| evo-herdr | `herdr-dev` | 开发模式:通用四窗格与 PI 五窗格布局定式(主开发、研究、review、自省回归;PI 加实战验收);评审闸门加自省验收双闸门;任务分发 lane(worktree 分支加总台独占发布) | 定开发窗格布局、发评审请求、终审放行、自省验收、多 agent 任务分发 |
| evo-herdr | `herdr-flywheel` | 跨仓模式:不同仓库 agent 工作台对话交流,四步协议派单、回执、断言、吸收;跨机器工位、并行派单义务图 | 跨仓派发治理任务、总台轮次协调、多工位并行派单 |

装 evo-doc 即得 md 禁字挡板(插件级 hook,与 skill 解耦);本仓自用骨架工具(init/check/scan 与模板)在仓根 `.tools/`,不随插件分发。

## 环境前提

- skill 本体纯 Markdown;脚本零第三方依赖(PEP 723,>=3.12,`uv run` 或系统 python)
- 外部命令(gh、reader 等)全平台分发安装由宿主工具链 omc 与 ark 统一维护,skill 只认 PATH
- 检索与验证命令按 PowerShell 7、ripgrep、reader 实测
- 平台:Windows 主开发;文档与用例按三平台适配撰写

## 文档导航

| 文档 | 讲什么 | 何时看 |
|------|--------|--------|
| `AGENTS.md` | 开发协作规则唯一权威源 | 写/改任何文件前 |
| `plugins/<插件>/README.md` | 各插件说明(前置、安装、用法、敏感产物) | 用插件面时 |
| `plugins/evo-doc/skills/doc-gov/SKILL.md` | 治理知识面 skill 本体(意图路由) | 使用/修改 skill 前 |
| `docs/README.md` | 全仓文档地图 | 找任何文档时 |
| `ROADMAP.md` | 阶段与里程碑状态 | 看进度时 |
| `CHANGELOG.md` | 变更日志 | 查历史时 |
