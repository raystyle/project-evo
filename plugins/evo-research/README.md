# evo-research

项目进化研究检索插件:两个 skill,`research` 资料检索管线(gh/bh 发现、aria2c 获取、reader 研读,无头优先与 HTTP 优先)与 `report` 研究成文(断言式报告骨架、md/pdf/docx 三件套、Typst 渲染、版式复检口径、信源存档与登记)。

状态:active。插件面客户端:Claude Code、Codex、Grok;纯 skills 面:Kimi 等手拷子集。

## 前置

- research 需本机 PATH 上的 gh、reader、aria2c、bh(可选;全平台命令分发安装由宿主工具链 omc 与 ark 统一维护)
- report 渲染需 PATH 上的 typst(或 `TYPST` 环境变量、`--typst` 显式指定);首次编译联网拉取 `@preview/cmarker` 包
- 脚本为零依赖 PEP 723 标准 Python(>=3.12)

## 安装

Claude Code:

```text
/plugin marketplace add raystyle/project-evo
/plugin install evo-research@project-evo
```

Codex:

```bash
codex plugin marketplace add raystyle/project-evo
```

Grok:

```bash
grok plugin marketplace add raystyle/project-evo
grok plugin install evo-research@project-evo --trust
```

Kimi(无市场):把 `skills/` 下两个 skill 目录一并拷至 `~/.kimi/skills/`。

## 用法

安装插件后两个 skill 按意图路由自动触发,客户端显示为 `evo-research:research` / `evo-research:report`。research 无斜杠命令,report 脚本可独立调用(免插件):

```bash
uv run skills/report/scripts/render.py <报告.md>          # md 渲同名 PDF
uv run skills/report/scripts/render.py <报告.md> --check  # 编译门禁,不覆盖产物
```

示例提示词:「搜一下 agent skills 规范的论文和近期文章」「把这份调研写成正式报告并渲染三件套」。

## 输出

- research:检索命中清单与获取产物;轻量结论落目标项目 `docs/research/SNNN` 标六态
- report:三件套 `reports/YYYY-MM-DD-短名.md` 与同名 `.pdf`、`.docx`(缺一不算完成,md 是唯一真源,生成物禁手改);docx 管线与版式复检口径见 skill references(知识面,下游自建)

## 支持与发布

- 支持:[raystyle/project-evo issues](https://github.com/raystyle/project-evo/issues)
- 当前发布:0.3.0
