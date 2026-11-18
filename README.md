# ProjectEvo

> 一句话定位:项目治理插件市场仓。市场名 `project-evo`,源 `raystyle/project-evo`,单插件五 skill:`evo`(agent 操作面:shares、streams、ctxs、ports、pipes 五入口,prim v5 五入口收敛批 180,动词对齐 hc = 清单 ls、留痕 send、生命周期 start;pipes send = 字节写,留痕知会归 streams send)。职责声明:本仓只维护 skill 面,不维护 prim(原语 CLI 真源与维护在 herdr-ccoe 仓)。客户端显示 `<插件>:<skill>`。

## 安装

市场名 `project-evo`,源 `raystyle/project-evo`;单插件 evo(批 180 起,dev 插件退役)。

| 客户端 | 命令 |
|--------|------|
| Claude Code | `/plugin marketplace add raystyle/project-evo`,再 `/plugin install evo@project-evo` |
| Codex | `codex plugin marketplace add raystyle/project-evo`,再 `codex plugin add evo@project-evo` |
| Grok | `grok plugin marketplace add raystyle/project-evo`,再 `grok plugin install evo@project-evo --trust` |
| Kimi | 无插件市场:按 `~/.kimi-code/config.toml` 的 `extra_skill_dirs`(默认 `~/.kimi/skills`)拷 `plugins/evo/skills/*`;斜杠命令不随行 |

开发态(指向工作树,改动即生效,免推送):把 `marketplace add` 的源换成仓根路径,如 `/plugin marketplace add /mnt/wsl/repos/project-evo`。

## 升级

升级 = 刷新市场快照再更新插件;插件按 manifest 版本号归位缓存,版本号不变则不刷新。

```text
Claude Code   /plugin marketplace update project-evo   /plugin update evo@project-evo     (重启会话生效)
Codex         codex plugin marketplace upgrade         codex plugin add evo@project-evo
Grok          grok plugin marketplace update           grok plugin update
Kimi          重新拷 plugins/evo/skills/*
```

旧版本缓存不自动清,按目录手动删:`~/.claude/plugins/cache/<市场>/<插件>/<版本>`、`~/.codex/plugins/cache/<市场>/<插件>/<版本>`。

**从旧市场 projectevo 迁移(破坏性)**:先卸载旧市场(`/plugin marketplace remove projectevo`)再按上方命令加 `project-evo` 装插件;旧缓存目录 `cache/projectevo/` 与已下线插件的缓存目录可整目录删除。

**批 180 迁移(破坏性)**:dev 插件退役,消费方卸载 `dev@project-evo`;evo 的 agents/desks/machines/research 四 skill 退役(消息与生命周期归 hc 与 herdr-app 原生面),消费方更新 evo 至 0.23.0。

## 配置

- 市场源与协议:HTTPS 与 SSH git URL 都收;GitHub 简写默认协议相反,Claude Code 走 SSH(`CLAUDE_CODE_PLUGIN_PREFER_HTTPS=1` 切 HTTPS),Codex 走 HTTPS;Grok 另收本地路径与 `@ref`、`#subdir`
- 私有仓认证:标准 git 凭据(credential helper 或 ssh-agent),与终端 git 行为一致
- 钉版:Claude Code `raystyle/project-evo@v0.15.0`(或 URL 尾 `#v0.15.0`);Codex `--ref v0.15.0`(下一封版后同理)
- md 禁字与术语表挡板:提交挡板脚本在仓根 `.tools/`(md-guard 禁字、term-lint 约束术语;走 pre-commit --staged;规则唯一权威 `mdrules.py` 与 `termrules.py`,批 180 随 dev 插件退役自插件级 scripts/ 迁入)
- skill 知识面自含(批 180 二段令:hook_rules 知识树删除,知识面并回各 SKILL.md;批 176 曾翻 hook_rules 薄壳指针、批 178 注入加载器裁撤,均已翻页)
- 扫描豁免:本仓 `.tools/scan.py` 的误报走环境变量 `PEVO_SCAN_ALLOW`(分号分隔正则,匹配 文件:行)

## 插件与 SKILL 介绍

| 插件 | skill | 做什么 | 何时用 |
|------|-------|--------|--------|
| evo | `shares` | 文件域原语:ls/put/get/send,内容哈希键,拒投不丢件 | 传文件给指定 agent、交付产物、取回共享时 |
| evo | `streams` | 流域原语:增量消息,裸 ls 房间清单、room/dm/ls 读流/append/send,fleet 回执主频道 | 往流交回执或广播、私信、回放续读、列房间时 |
| evo | `ctxs` | 对话历史域原语:agent 请求全链检索(ClickHouse gw_logs;ls 头行与单请求全链、search 全文;head 365 天正文 180 天) | 查历史对话、回溯对话细节、跨请求搜关键词、看请求开销时 |
| evo | `ports` | 端口映射域原语:ls/start/close/fwd/send,tailcat serve 面板端口与服务映射 | 起面板端口、服务侧映射、本地起听转发时 |
| evo | `pipes` | 实时字节域原语:ls/start/close/send,管道收发,stdin 字节直通 | 转发实时日志流、连对方管道灌字节时 |

五入口实操需本机 PATH 上的 prim v5(五入口形;CLI 真源与维护在 herdr-ccoe 仓,本仓不涉及 prim 代码与封装;全平台分发由宿主工具链 omc 与 ark 统一维护)。本仓自用骨架工具(init/check/scan 与模板)与门禁脚本(md-guard/term-lint 及规则源)在仓根 `.tools/`,不随插件分发。结构沿革(旧多插件形态收敛、裁撤与改名映射)见 ADR-0025、ADR-0026、ADR-0027、ADR-0028、ADR-0029 与 ADR-0030。

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
| `docs/README.md` | 全仓文档地图 | 找任何文档时 |
| `ROADMAP.md` | 阶段与里程碑状态 | 看进度时 |
| `CHANGELOG.md` | 变更日志 | 查历史时 |
