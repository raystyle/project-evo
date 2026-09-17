# evo-adr

项目进化文档治理插件:五个 skill,`doc-gov` 文档即代码治理知识(AGENTS 合同、ADR、REQ、投影纪律、六态)、`code-kit` 骨架与门禁工具(init/check/scan/md-guard/mdrules 零依赖脚本、模板、PE-01 至 PE-12 诊断、md 禁字挡板)、`gh-issue` 命令出错自动上报 GitHub issue(定位仓、双通道去重、模板正文、自动发单、三态回执)与 `build-release` 编译打包发布流水线指导(六型配方、公共契约、可拷改模板)与 `cli-docs` CLI 对外面双标准(README 四节骨架、agent 五件:--llms 手册、旗标全家与 CTA 协议、默认帮助面、自省、裸调用面)。

状态:active。插件面客户端:Claude Code、Codex、Grok;纯 skills 面:Kimi 等手拷子集。

## 前置

- 无硬性运行时依赖;skill 本体纯 Markdown
- 脚本为零依赖 PEP 723 标准 Python(>=3.12),`uv run <脚本>` 或系统 `python` 均可
- `scan.py` 的 git 历史扫描需目标项目是 git 仓

## 安装

Claude Code:

```text
/plugin marketplace add raystyle/project-evo
/plugin install evo-adr@project-evo
```

Codex:

```bash
codex plugin marketplace add raystyle/project-evo
```

Grok:

```bash
grok plugin marketplace add raystyle/project-evo
grok plugin install evo-adr@project-evo --trust
```

Kimi(无市场):把 `skills/` 下五个 skill 目录一并拷至 `~/.kimi/skills/`;斜杠命令与 hook 不随行。

本地开发(三客户端同款,路径换本地仓根)。

## 用法

安装插件后五个 skill 按意图路由自动触发,客户端显示为 `evo-adr:doc-gov` / `evo-adr:code-kit` / `evo-adr:gh-issue` / `evo-adr:build-release` / `evo-adr:cli-docs`;也可用斜杠命令(Claude Code 面):

- `/evo-adr:init <目标项目> [--name 项目名]` 安装文档骨架(幂等,不覆盖已有)
- `/evo-adr:check [目标项目]` 诊断骨架合规 PE-01 至 PE-12(只读,--json 出机器读面,退出码 0/1/2)
- `/evo-adr:scan [目标项目] [--no-history]` 安全与规范扫描(浅密钥 + markdown 禁字)

脚本可独立调用(免插件):

```bash
uv run skills/code-kit/scripts/init.py <目标项目> --name <项目名>
uv run skills/code-kit/scripts/check.py [目标项目]
uv run skills/code-kit/scripts/scan.py [目标项目] --no-history
```

示例提示词:「用 evo-adr 为这个项目初始化文档骨架」「帮我立一条 ADR 记录这个决策」「这条命令报错了,用 gh-issue 查重后给上游发个 issue」。

## 架构

五个 skill 都是渐进知识库:SKILL.md 只做意图路由与速览,完整知识在各自 `references/`(分类扁平,rg 定位渐进检索)。可执行面在 `skills/code-kit/scripts/`(规则唯一权威 `mdrules.py`,check 的 PE-12 与 scan、md-guard 三面同源),模板在 `skills/code-kit/assets/templates/`。PostToolUse hook(`hooks/hooks.json`)对编辑中的 markdown 做四类禁字会话内提醒。

## 敏感产物

scan 的白名单走目标项目环境变量 `PEVO_SCAN_ALLOW`(分号分隔正则,匹配 文件:行 规则);测试夹具等已知误报在此豁免,不改动扫描规则本身。

## 支持与发布

- 支持:[raystyle/project-evo issues](https://github.com/raystyle/project-evo/issues)
- 当前发布:0.3.0
