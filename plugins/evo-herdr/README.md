# evo-herdr

项目进化多仓协作插件:一个 skill,`herdr-flywheel` 多仓 herdr 工位飞轮协作治理(派单、回执、断言、吸收四步协议,附命令面要点与治理操作坑)。本 skill 是该协议唯一权威源。

状态:active。插件面客户端:Claude Code、Codex、Grok;纯 skills 面:Kimi 等手拷子集。

## 前置

- skill 本体纯 Markdown,无脚本
- 实操需本机 PATH 上的 herdr(命令语法活权威是本机直跑 `herdr --skill`;全平台命令分发安装由宿主工具链 omc 与 ark 统一维护)

## 安装

Claude Code:

```text
/plugin marketplace add raystyle/project-evo
/plugin install evo-herdr@project-evo
```

Codex:

```bash
codex plugin marketplace add raystyle/project-evo
```

Grok:

```bash
grok plugin marketplace add raystyle/project-evo
grok plugin install evo-herdr@project-evo --trust
```

Kimi(无市场):把 `skills/herdr-flywheel/` 拷至 `~/.kimi/skills/`。

## 用法

安装插件后按意图路由自动触发,客户端显示为 `evo-herdr:herdr-flywheel`。协议、命令面与坑见 skill 的 SKILL.md 与 references。

示例提示词:「给 ark_rs 工位派这轮治理单」「收一下各工位回执并做独立断言」。

## 支持与发布

- 支持:[raystyle/project-evo issues](https://github.com/raystyle/project-evo/issues)
- 当前发布:0.1.0
