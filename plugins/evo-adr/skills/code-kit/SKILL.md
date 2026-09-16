---
name: code-kit
description: >-
  文档骨架与门禁工具箱:安装文档骨架(init.py 幂等不覆盖已有)、诊断骨架合规(check.py PE-01 至 PE-12,
  只读,--json 出机器读面)、安全与规范扫描(scan.py 浅密钥 + md 禁字)、会话内 md 禁字挡板(md-guard.py,
  规则唯一权威 mdrules.py);附文档骨架模板与骨架规范检查用例。工程合同参考:初始化五步与存量迁移、
  测试分层与门禁、平台矩阵(shell/编码/行尾/CI 三系统)、项目脚本工具约定、Rust/TypeScript/Python 三栈工程合同、
  agent-native CLI 设计。触发后先读本文件「意图路由」定位,命令细节见各节。
  Use when 初始化项目骨架、迁移旧项目到文档体系、跑合规检查、扫描禁字与浅密钥、
  建项目脚本工具、建 Rust/TypeScript/Python 工程、给 CLI 加 agent 用户面时。
compatibility: 通用;脚本为 PEP 723 零依赖 Python(>=3.12),uv run 或系统 python 直跑,无第三方依赖。
---

# code-kit - evo-adr 骨架与门禁工具箱

**工具型 skill**:`scripts/` 五脚本(init/check/scan/md-guard/mdrules)是交付物,本文件是它们的用法面与意图路由;骨架模板在 `assets/templates/`,骨架规范检查用例在 `verification/`。文档体系知识(合同/ADR/REQ/投影/六态)在同插件 `doc-gov`。

## 一、意图路由

| 你要做的事 | 入口 |
| --- | --- |
| 新项目初始化骨架 / 旧项目迁移到本体系 | `references/base-init.md` |
| 装骨架(命令) | 本文件「二、init」 |
| 验证某项目是否符合骨架 / PE-01 至 PE-12 判定语义 | `verification/command-test-cases.md` |
| 写测试 / 定测试分层与门禁(单元/集成/冒烟/回归/验收) | `references/flow-testing.md` |
| 定平台矩阵 / shell 行尾 / CI 三系统 / 换机接管 | `references/env-platform.md` |
| 建项目脚本工具(.tools / uv / PEP 723) | `references/tool-project.md` |
| 建 Rust 项目 / cargo 工作区 / missing_docs / doctest / aidoc | `references/tool-rust.md` |
| 建 TypeScript/Node 项目 / TSDoc / API Extractor / TypeDoc / Vitest | `references/tool-typescript.md` |
| 建 Python 项目 / docstring / MkDocs 投影 / PEP 723 脚本 | `references/tool-python.md` |
| 给 CLI 加 agent 用户面(agent-native 契约、管道逃生舱、脚本 workspace) | `references/tool-cli-agents.md` |
| 写 AGENTS 合同 / 立 ADR 或 REQ / 投影纪律 / 六态 | 同插件 skill `evo-adr:doc-gov` |

## 二、脚本用法(本节命令均实证可跑)

三脚本统一形态:PEP 723 零依赖(>=3.12),`uv run` 或系统 python 直跑;路径以本 skill 目录为根。

### init:安装文档骨架

```bash
uv run <skill>/scripts/init.py <目标项目> --name <项目名>
```

幂等:已有文件一律跳过不覆盖;装完按输出提示补 AGENTS 定位段与 GOAL 起点。骨架结构见 `references/base-init.md`。

### check:诊断骨架合规(PE-01 至 PE-12)

```bash
uv run <skill>/scripts/check.py <目标项目>          # 人读逐项表
uv run <skill>/scripts/check.py <目标项目> --json   # 机器读面(ok/counts/results)
```

只读;退出码 0 全过(含 SKIP)/ 1 有 FAIL / 2 出错;违规清单全量列出。逐项判定语义见 `verification/command-test-cases.md`;FAIL 项按对应参考修正后复跑,直到全绿。

### scan:安全与规范扫描(浅面)

```bash
uv run <skill>/scripts/scan.py <目标项目>                 # 工作区+git 历史+md 禁字
uv run <skill>/scripts/scan.py <目标项目> --no-history    # 只扫工作区
```

处置口径:HIGH(密钥疑似入库)先轮换凭据再清史;md 禁字按告警逐行修正;已知误报走目标项目环境变量 `PEVO_SCAN_ALLOW`(分号分隔正则,匹配 文件:行),不改规则。git 全历史与 GitHub 面深扫在同市场 `evo-codesec:secret-scan`。

### md-guard:会话内禁字挡板

`md-guard.py` 由插件 hook(`hooks/hooks.json`)与宿主仓 `.claude/settings.json` 调用,编辑 markdown 时提醒四类禁字(Unicode 箭头、破折号/连接号、emoji 与装饰符、智能引号与全角字母数字);规则唯一权威 `scripts/mdrules.py`,与 check 的 PE-11、scan 三面同源,围栏内整行豁免。box-drawing 手拼伪流程图是 AGENTS 的写法禁令,不在机检四类内。

## 三、骨架与模板

`assets/templates/` 持 AGENTS/CLAUDE/CHANGELOG 与 docs 五目录(adr/requirements/guides/diary/research)模板;init 按模板渲染,ADR/REQ 模板含 frontmatter 契约与状态机说明。

安装通道:Claude Code `/plugin marketplace add raystyle/project-evo` 后装 evo-adr 插件(`/evo-adr:init`、`/evo-adr:check`、`/evo-adr:scan` 斜杠命令与 PostToolUse 禁字挡板随插件生效);Codex `codex plugin marketplace add raystyle/project-evo`;Grok `grok plugin install evo-adr@project-evo --trust`;Kimi 无市场,拷 `skills/code-kit/` 至 `~/.kimi/skills`(命令与 hook 不随行,脚本可直跑)。
