# evo-skills

项目进化技能自进化插件:单 skill `distil-skill`。项目把自己的执行经验变成可持续迭代的项目级标准 skill 集:三层聚合(sources = 带时间的历史轨迹总结、knowledge = 带版本的双向链接关联结构化知识、operations = 产物为 Claude Code 与 Codex 双端支持的标准项目级 SKILL),四步环(执行产痕、蒸馏模式、一案提案、合取闸门),no_action 合法出口,知识层永不回滚、标准层拒绝即回滚,生成维护环默认无头边界内跑、接受与发布停在人裁。

状态:active。插件面客户端:Claude Code、Codex、Grok;纯 skills 面:Kimi 等手拷子集。

## 前置

- skill 本体纯 Markdown,无脚本
- 跑环需项目 git 与既有门禁;双端执行面需 claude 或 codex CLI(命令面活权威是本机 --help 实查)

## 安装

Claude Code:

```text
/plugin marketplace add raystyle/project-evo
/plugin install evo-skills@project-evo
```

Codex:

```bash
codex plugin marketplace add raystyle/project-evo
```

Grok:

```bash
grok plugin marketplace add raystyle/project-evo
grok plugin install evo-skills@project-evo --trust
```

Kimi(无市场):把 `skills/distil-skill/` 拷至 `~/.kimi/skills/`。

## 用法

安装插件后按意图路由自动触发,客户端显示为 `evo-skills:distil-skill`。

示例提示词:「用 distil-skill 把这轮项目执行轨迹蒸馏成模式页,并提一案标准 skill 变更」「用 distil-skill 给这个项目建三层聚合与双端标准项目级技能集」。

## 架构

skill 是渐进知识库:SKILL.md 只做意图路由与环速览,完整机制在 `skills/distil-skill/references/` 五篇(layers、trajectories、loop、gate、backends)。无脚本无 hook;市场源仓的自用骨架工具在仓根 `.tools/`,不随插件分发。

## 支持与发布

- 支持:[raystyle/project-evo issues](https://github.com/raystyle/project-evo/issues)
- 当前发布:0.6.0
