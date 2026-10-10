# evo-doc

项目进化文档治理插件:两个 skill。`doc-gov` 文档框架治理知识(ADR 与 REQ 需求决策、代码 doc 注释契约、文档即代码、研究档案、项目工具链范式)与 `native-design` Agent 原生友好开发指导(--llms 手册面、类型化 CTA 协议、命令自省、发现通道与 token 经济学)。插件级 PostToolUse hook 提供 md 禁字挡板(四类禁字,辖域限仓内 md,规则唯一权威 `scripts/mdrules.py`,与 skill 解耦)。三层聚合与技能自进化在同市场插件 evo-skills。

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

Kimi(无市场):把 `skills/` 下两个 skill 目录一并拷至 `~/.kimi/skills/`;hook 不随行。

本地开发(三客户端同款,路径换本地仓根)。

## 用法

安装插件后按意图路由自动触发,客户端显示为 `evo-doc:doc-gov` / `evo-doc:native-design`;装插件即得 md 禁字挡板(编辑仓内 markdown 时 PostToolUse 提醒,无需配置)。

示例提示词:「用 doc-gov 给这个项目立 ADR 与 REQ 需求决策体系」「用 doc-gov 给这个项目立代码契约注释与文档即代码守卫」「用 doc-gov 立研究档案做选型对照」「用 native-design 给这个 CLI 配 --llms 手册与 agent 友好输出协议」。

## 架构

skill 是渐进知识库:SKILL.md 只做意图路由与形态速览,完整知识在各自 `skills/<skill>/references/`(doc-gov 5 篇、native-design 3 篇,rg 定位渐进检索)。可执行面只有插件级 `scripts/md-guard.py` 与 `scripts/mdrules.py`(hook 专用,skill 目录纯知识,skill 与 hook 解耦)。市场源仓的自用骨架工具(init/check/scan 与模板)在仓根 `.tools/`,不随插件分发。

## 支持与发布

- 支持:[raystyle/project-evo issues](https://github.com/raystyle/project-evo/issues)
- 当前发布:0.7.0
