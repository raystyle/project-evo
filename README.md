# ProjectEvo

> 一句话定位:项目治理插件市场仓。市场名 `project-evo`,源 `raystyle/project-evo`,两插件十四 skill:`dev`(开发治理面:dev-doc 文档治理与静态检查、dev-cli(原 doc-cli))、`evo`(agent 操作面:agents、desks、shares、streams、tasks、pipes、ports、ctxs、mcps、machines 十原语 skill 加 research 检索域与 distil;十原语 = 舰队互操作代理操作唯一面,herdr 技能已淘汰)。客户端显示 `<插件>:<skill>`。

## 安装

市场名 `project-evo`,源 `raystyle/project-evo`;按域装插件,两插件同版本线(ADR-0025)。

| 客户端 | 命令 |
|--------|------|
| Claude Code | `/plugin marketplace add raystyle/project-evo`,再 `/plugin install <插件>@project-evo`(如 `evo@project-evo`、`dev@project-evo`) |
| Codex | `codex plugin marketplace add raystyle/project-evo`,再 `codex plugin add <插件>@project-evo` |
| Grok | `grok plugin marketplace add raystyle/project-evo`,再 `grok plugin install <插件>@project-evo --trust` |
| Kimi | 无插件市场:按 `~/.kimi-code/config.toml` 的 `extra_skill_dirs`(默认 `~/.kimi/skills`)拷 `plugins/<插件>/skills/*` 与 `plugins/<插件>/hook_rules/*`(壳指路直读);斜杠命令不随行 |

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
- 钉版:Claude Code `raystyle/project-evo@v0.15.0`(或 URL 尾 `#v0.15.0`);Codex `--ref v0.15.0`(下一封版后同理)
- md 禁字与术语表挡板:提交挡板脚本在插件级 `scripts/`(md-guard 禁字、term-lint 约束术语;走 pre-commit --staged;规则唯一权威 `mdrules.py` 与 `termrules.py`,与 skill 解耦)
- hook_rules 注入面(批 176):知识本体在插件 `hook_rules/`(intents 意图注入 + dev-rules 路径注入),插件 hooks 挂两枚 bun 加载器(UserPromptSubmit + PreToolUse);SKILL.md 为薄壳指针,非 hook 端直读 hook_rules md
- 扫描豁免:本仓 `.tools/scan.py` 的误报走环境变量 `PEVO_SCAN_ALLOW`(分号分隔正则,匹配 文件:行)

## 插件与 SKILL 介绍

| 插件 | skill | 做什么 | 何时用 |
|------|-------|--------|--------|
| dev | `dev-doc` | 文档治理与静态检查(原 doc-gov 与 dev-lint 合一):ADR 与 REQ 需求决策、代码 doc 注释契约、文档即代码、研究档案、工具链;md 静检与约束术语表 term-lint、四类型结构模板卡、门禁接线 | 立 ADR/REQ、立代码契约注释与文档即代码守卫、配静态检查与术语门禁、新仓脚手架时 |
| dev | `dev-cli` | Agent 原生友好开发(原 doc-cli;批 176 知识面在插件 hook_rules,壳指路):--llms 手册面、类型化 CTA 输出协议、命令自省与漂移守卫、Rust CLI 舰队公约、发现通道与 token 经济学 | 配 CLI agent 面、为 agent 时代设计命令与工具面 |
| evo | `agents` | 五原语消息域原语与共享面枢纽:to 投递、id 三产生式、命名标准(工作台-类型-编号)、门控 v2 尾窗、信封 v2、status 四态、read 收件、工位管理 | 告诉或委派某 agent、找格读屏等回话、开工作台调窗格布局、查在场时 |
| evo | `shares` | 文件域原语:put/get/to,内容哈希键,拒投不丢件 | 传文件给指定 agent、交付产物、取回共享时 |
| evo | `streams` | 流域原语:append/view/to,流即房间,fleet 回执主频道 | 往流交回执或广播、私信、回放续读时 |
| evo | `tasks` | 持久任务域原语:set/to,事件入流,远机零 ssh | 设别的格的持久任务、跨机委派目标时 |
| evo | `pipes` | 实时字节域原语:open/close/to,本机收对方发 | 要对方实时发字节、开实时管道时 |
| evo | `ports` | 端口域原语:任意节点端口转发映射(view/open/close/to,引擎 tailcat serve;spec = 端口表/定点映射/all/exit-node;取用行 tailcat forward) | 开端口转发、映射远端端口、让对方接入端口服务时 |
| evo | `ctxs` | 对话历史域原语:agent 请求全链检索(ClickHouse gw_logs;view 头行、show 单请求、search 全文;head 365 天正文 180 天) | 查历史对话、回溯对话细节、跨请求搜关键词、看请求开销时 |
| evo | `mcps` | MCP 目标域原语:出站通用 MCP 客户端(view 健康、tools 面、call 调用、注册表管理),无门控 | 驱动任意 MCP server、查工具面、跨机调用工具时 |
| evo | `desks` | 工位与窗格拓扑域原语:开工作台、起停格、分屏切tab、聚焦、信任放行、拓扑真视图(prim 3.11 复数对齐,原 desk 留单字别名) | 开工作台、起格分屏、切 tab、聚焦格、放行信任屏、看窗台工位分组拓扑时 |
| evo | `machines` | 机册域原语(原 nodes):herdr 机册管理、原始窗格操作(run/close/pane 直透)、runtime 环境面(骑 ark) | 注册或管理舰队节点、在指定节点窗格跑命令、环境对齐时 |
| evo | `research` | 检索域知识面:按研究目标路由通道(gh 搜 GitHub、browse 搜 Bing 与 Scholar、rn 编排与油猴探针) | 调研主题、找库选型、学术检索、跨源对照搜索时 |
| evo | `distil` | 技能自进化(原 distil-skill):三层聚合、一案提案、合取闸门 | 把项目经验沉淀成 skill 时 |

装 dev 即得 md 禁字与术语表挡板脚本与 hook_rules 注入面(插件级,与 skill 解耦);本仓自用骨架工具(init/check/scan 与模板)在仓根 `.tools/`,不随插件分发。结构沿革(旧多插件形态收敛、裁撤与改名映射)见 ADR-0025、ADR-0026 与 ADR-0027。

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
| `plugins/dev/skills/dev-doc/SKILL.md` | 治理与静检知识面 skill 本体(意图路由) | 使用/修改 skill 前 |
| `docs/README.md` | 全仓文档地图 | 找任何文档时 |
| `ROADMAP.md` | 阶段与里程碑状态 | 看进度时 |
| `CHANGELOG.md` | 变更日志 | 查历史时 |
