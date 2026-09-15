# project-evo

项目进化插件:一个插件四个 skill,即 `dev-evo` 文档即代码体系、`super-research` 资料检索管线、`secret-scan` 密钥与隐私扫描、`security-audit` 安全审计与漏洞审查(译自 Cloudflare security-audit-skill,MIT,目录内附 LICENSE)。

状态:active。插件面客户端:Claude Code、Codex、Grok;纯 skills 面:Kimi 等手拷子集。

## 前置

- 无硬性运行时依赖;skill 本体纯 Markdown
- 脚本(`scripts/init.py`、`check.py`、`scan.py`)为零依赖 PEP 723 标准 Python(>=3.12),`uv run <脚本>` 或系统 `python` 均可
- `scan.py` 的 git 历史扫描需目标项目是 git 仓

## 安装

Claude Code:

```text
/plugin marketplace add raystyle/projectevo
/plugin install project-evo@projectevo
```

Codex:

```bash
codex plugin marketplace add raystyle/projectevo
```

Grok:

```bash
grok plugin marketplace add raystyle/projectevo
grok plugin install project-evo@projectevo --trust
```

Kimi(无市场):把 `skills/` 下四个 skill 目录一并拷至 `~/.kimi/skills/`;斜杠命令与 hook 不随行。

本地开发(三客户端同款,路径换本地仓根)。

## 用法

安装插件后,四个 skill 按意图路由自动触发,客户端显示为 `project-evo:dev-evo` / `project-evo:super-research` / `project-evo:secret-scan` / `project-evo:security-audit`;也可用斜杠命令(Claude Code 面):

- `/project-evo:init <目标项目> [--name 项目名]` 安装文档骨架(幂等,不覆盖已有)
- `/project-evo:check [目标项目]` 诊断骨架合规 PE-01 至 PE-12(只读,退出码 0/1/2)
- `/project-evo:scan [目标项目] [--no-history]` 安全与规范扫描(token/密钥/隐私 + markdown 禁字)
- `/project-evo:secret-scan-cli [目标项目]` 密钥与隐私深扫(工作区 + git 全历史,GitHub 面加 `--github owner/repo`)

脚本可独立调用(免插件):

```bash
uv run skills/dev-evo/scripts/init.py <目标项目> --name <项目名>
uv run skills/dev-evo/scripts/check.py [目标项目]
uv run skills/dev-evo/scripts/scan.py [目标项目] --no-history
uv run skills/secret-scan/scripts/scan.py [目标项目]
```

示例提示词:「用 project-evo 为这个项目初始化文档骨架」「搜一下 agent skills 规范的论文和近期文章」「扫一下这个仓有没有密钥泄露」。

## 输出

- init:目标项目根下 AGENTS 五节合同 + CLAUDE/CHANGELOG + docs 五目录(adr/requirements/guides/diary/research)与 ADR/REQ 模板(已有文件跳过)
- check:PE-01 至 PE-12 逐项 PASS/FAIL/SKIP 与结论行(AGENTS 五节、ADR/REQ 状态机与索引、六态、禁字、断链)
- scan:按严重级排序的发现清单(文件:行 + 脱敏片段 + 首见提交)
- secret-scan:同上口径的独立深扫(工作区 + git 全历史;GitHub alerts 与 code search),误报豁免走 `PEVO_SCAN_ALLOW`

## 架构

三个 skill 都是渐进知识库:SKILL.md 只做意图路由与速览,完整知识在各自 `references/`(分类扁平,前缀 base/flow/env/tool/exp 分组,rg 定位 + 结构提取渐进检索)。可执行面:`skills/dev-evo/scripts/`(规则唯一权威 `mdrules.py`,check 的 PE-12 与 scan、md-guard 同源)、`skills/secret-scan/scripts/`;模板在 `skills/dev-evo/assets/templates/`。PostToolUse hook(`hooks/hooks.json`)对编辑中的 markdown 做四类禁字会话内提醒。

## 敏感产物

scan 的白名单走目标项目环境变量 `PEVO_SCAN_ALLOW`(分号分隔正则,匹配 文件:行 规则);测试夹具等已知误报在此豁免,不改动扫描规则本身。

## 支持与发布

- 支持:[raystyle/projectevo issues](https://github.com/raystyle/projectevo/issues)
- 当前发布:0.6.0
