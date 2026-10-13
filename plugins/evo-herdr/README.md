# evo-herdr

项目进化主开发台插件。单 skill **herdr-orch**:主开发台工作流(通用四窗格与 PI 五窗格布局定式、评审闸门加自省验收双闸门、先推后审与会话纪律、任务分发 lane 模型)加工位面(工位形态与带起配方、跨机器路由、信号命令速查、驻场坑,references/workstations.md)。目标循环与跨仓派单协议(派单、回执、断言、吸收、义务图)在同市场 `evo-agent:agent-rloop`(批 128 由原第二 skill herdr-flywheel 升格迁出)。通用原则:herdr 生命周期态只是检测信号,md 文件才是状态与产物,消息与产物传递内置 s5。

状态:active。插件面客户端:Claude Code、Codex、Grok;纯 skills 面:Kimi 等手拷子集。

## 前置

- skill 本体纯 Markdown,无脚本
- 实操需本机 PATH 上的 herdr(命令语法活权威是本机直跑 `herdr --skill`;全平台命令分发安装由宿主工具链 omc 与 ark 统一维护);对话检索需 hst

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

Kimi(无市场):把 `skills/` 下 skill 目录拷至 `~/.kimi/skills/`。

## 用法

安装插件后按意图路由自动触发,客户端显示为 `evo-herdr:herdr-orch`。协议、命令面与坑见 SKILL.md 与 references;目标循环协议见 evo-agent:agent-rloop。

示例提示词:「检测工位右侧有没有评审格,没有就建一个起 codex 然后发这份 review 请求」「把 lan-ubuntu 上的工位带起来」。

## 支持与发布

- 支持:[raystyle/project-evo issues](https://github.com/raystyle/project-evo/issues)
- 当前发布:0.11.0
