# evo-doc

项目进化文档治理插件:单 skill `doc-gov` 文档框架治理知识,指导项目的 ADR(需求决策)、COE(三层聚合与双向链接图)、项目日记三类文档形态与 Agent 友好 CLI 架构标准。插件级 PostToolUse hook 提供 md 禁字挡板(四类禁字,辖域限仓内 md,规则唯一权威 `scripts/mdrules.py`,与 skill 解耦)。

状态:active。插件面客户端:Claude Code、Codex、Grok;纯 skills 面:Kimi 等手拷子集。

## 前置

- 无硬性运行时依赖;skill 本体纯 Markdown
- hook 脚本为零依赖 PEP 723 标准 Python(>=3.12),`uv run` 或系统 `python` 均可

## 安装

Claude Code:

```text
/plugin marketplace add raystyle/project-evo
/plugin install evo-doc@project-evo
```

Codex:

```bash
codex plugin marketplace add raystyle/project-evo
```

Grok:

```bash
grok plugin marketplace add raystyle/project-evo
grok plugin install evo-doc@project-evo --trust
```

Kimi(无市场):把 `skills/doc-gov/` 拷至 `~/.kimi/skills/`;hook 不随行。

本地开发(三客户端同款,路径换本地仓根)。

## 用法

安装插件后单 skill 按意图路由自动触发,客户端显示为 `evo-doc:doc-gov`;装插件即得 md 禁字挡板(编辑仓内 markdown 时 PostToolUse 提醒,无需配置)。

示例提示词:「用 doc-gov 给这个项目立 ADR 与 REQ 需求决策体系」「用 doc-gov 建一个 COE 知识库操作台,三层聚合加双向链接图」「用 doc-gov 写今天的项目日记」「用 doc-gov 给这个 CLI 配 --llms 手册与 agent 友好输出协议」。

## 架构

skill 是渐进知识库:SKILL.md 只做意图路由与形态速览,完整知识在 `skills/doc-gov/references/`(7 篇,rg 定位渐进检索)。可执行面只有插件级 `scripts/md-guard.py` 与 `scripts/mdrules.py`(hook 专用,skill 目录纯知识,skill 与 hook 解耦)。市场源仓的自用骨架工具(init/check/scan 与模板)在仓根 `.tools/`,不随插件分发。

## 支持与发布

- 支持:[raystyle/project-evo issues](https://github.com/raystyle/project-evo/issues)
- 当前发布:0.4.3
