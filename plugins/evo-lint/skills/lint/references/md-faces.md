# md 三面静检:格式标准、长度限制、禁字、断链、结构

> skill markdown、agents markdown、claude markdown 三面的可判定检查。硬标准:skill 面以 [agentskills 官方 spec](https://agentskills.io/specification) 为准;禁字与结构沿本市场仓惯例(AGENTS 写作规范)。

## skill markdown(格式标准)

- **frontmatter 仅官方字段**:必填 name 与 description;禁 version、argument-hint 等非官方字段
- **name 同目录名**:目录名与 frontmatter name 一致,客户端按 `<插件>:<name>` 显示
- **description 形态**:「做什么 + 何时用」兼具,含触发词;上限 1024 字符(spec 数值,以官方 spec 实查为准)
- **行数上限**:SKILL.md 少于 500 行、正文建议低于 5000 token(spec 建议;渐进披露,细节下放 references)
- **断链**:references 与正文相对链接全部可达(断链扫描器各仓自备或引 market 仓工具形)
- 检查形态:脚本逐项断言退出码制(示例判据:非官方字段命中即红、name 与目录名不等即红、超行即红)

## agents markdown(长度限制与结构)

- **长度限制**:行数上限缺省 200 行(上下文成本纪律:agent 每轮装载,越长越贵越易漏);仓可裁,裁值登记在 AGENTS 或 lint 配置在册,不静默超
- **结构合同**:节齐(定位、Commands、Must、Must not、Read first、环境,按仓裁剪);命令块可实证(写进去的当真跑过)
- **禁字四类**:emoji、box-drawing 手拼伪流程图、破折号/连接号、标题括号(本市场写作规范;扫描器 md-guard 形,--staged 挂 pre-commit)

## claude markdown(长度限制与桥接)

- **单行桥接形**(本家族):CLAUDE.md 仅一行 `@AGENTS.md`,不重复维护
- **长度限制**:非桥接形上限缺省 50 行(同上下文成本纪律;仓可裁登记)
- 检查形态:行数断言加桥接形态断言,退出码制

## 门禁接线(md 面)

- pre-commit 挂禁字与断链(--staged 形,只查当批);结构合同与长度限制进门禁清单(AGENTS 或 README 固定成文)
- 豁免纪律:整文件或目录豁免须登记在册带因由;历史档案面(旧轨迹、verbatim 外档)按只增不改豁免,不追改
