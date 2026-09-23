# evo-research

项目进化研究检索插件:单 skill,`research` 资料检索管线(gh 发现、browse 驾浏览器搜索与抓取、aria2c 获取、reader 研读,先确认浏览器态、不动宿主机浏览器、HTTP 优先;轻量结论落目标项目 `docs/research/SNNN` 标六态)。

状态:active。插件面客户端:Claude Code、Codex、Grok;纯 skills 面:Kimi 等手拷子集。

## 前置

- research 需本机 PATH 上的 gh、reader、aria2c、browse(可选;全平台命令分发安装由宿主工具链 omc 与 ark 统一维护)
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

Kimi(无市场):把 `skills/` 下 skill 目录拷至 `~/.kimi/skills/`。

## 用法

安装插件后 skill 按意图路由自动触发,客户端显示为 `evo-research:research`。research 无斜杠命令。

示例提示词:「搜一下 agent skills 规范的论文和近期文章」。

## 输出

- research:检索命中清单与获取产物;轻量结论落目标项目 `docs/research/SNNN` 标六态;需正式成文的按 doc-gov 投影纪律出 md

## 支持与发布

- 支持:[raystyle/project-evo issues](https://github.com/raystyle/project-evo/issues)
- 当前发布:0.4.0
