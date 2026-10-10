# evo-herdr

项目进化多仓协作插件:两个 skill 双模式。`herdr-orch` 主开发台(初始各工作角色邻居窗格并开始配合工作:通用四窗格与 PI 五窗格布局定式、评审闸门加自省验收双闸门、先推后审与会话纪律、任务分发 lane 模型)与 `herdr-flywheel` 跨仓库跨项目跨机器交流(派单、回执、断言、吸收四步协议,状态门控与事件驱动收执,产物契约与状态档统一标准路径三件套 brief/state/receipt 且盘上稳态与 herdr 干预信号分治,跨机器工位,并行派单义务图,附命令面要点与治理操作坑,该协议唯一权威源)。两 skill 通用原则:herdr 生命周期态只是检测信号,md 文件才是状态与产物。

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

Kimi(无市场):把 `skills/` 下两个 skill 目录一并拷至 `~/.kimi/skills/`。

## 用法

安装插件后按意图路由自动触发,客户端显示为 `evo-herdr:herdr-orch` / `evo-herdr:herdr-flywheel`。协议、命令面与坑见两个 skill 的 SKILL.md 与 references。

示例提示词:「给 ark_rs 工位派这轮治理单」「收一下各工位回执并做独立断言」「检测工位右侧有没有评审格,没有就建一个起 codex,然后发这份 review 请求」。

## 支持与发布

- 支持:[raystyle/project-evo issues](https://github.com/raystyle/project-evo/issues)
- 当前发布:0.7.0
