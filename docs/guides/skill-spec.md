# skill 规范细则（agentskills 硬标准）

> 本仓 skill 目录的硬性规范细则,从 AGENTS 下沉至此;AGENTS 只留合同速查。以 [agentskills 官方 spec](https://agentskills.io/specification) 为硬标准。

## frontmatter 字段

| 字段 | 是否必填 | 约束 |
|------|------|------|
| `name` | 必填 | ≤64 字符;小写字母/数字/连字符;**必须与目录名一致** |
| `description` | 必填 | 1-1024 字符;「做什么 + 何时用」兼具;含触发关键词 |
| `license` / `compatibility` / `metadata` / `allowed-tools` | 可选 | 见官方 spec |
| `version` / `argument-hint` 等非官方字段 | **禁止** | 版本由 git tag / release 管理 |

## 正文与目录

- `SKILL.md` ≤500 行;只留意图路由 + 体系速览;详细操作移 `references/`
- 标准布局:`SKILL.md`(意图路由+速览) + `references/`(分类+扁平,前缀 base/flow/env/tool/exp 分组) + `verification/`(命令行为);无 evals 层(渐进知识库型 skill,不做用例评估)
- 分层原则:references/ 每篇一主题自包含完整参考;实现代码唯一来源是插件内 `skills/<skill>/scripts/`(如 code-kit 五脚本、secret-scan 的 scan.py,PEP 723 零依赖;禁字规则唯一权威在 code-kit 的 `mdrules.py`,check PE-11/scan/md-guard 三面同源)

## 写作约束

- 禁止 emoji;流程图用 mermaid,禁止 box-drawing 手拼伪流程图
- 事实性断言标六态:`[实证]/[推断]/[经验]/[记忆]/[假设]/[直觉]`
- 中文为主;命令/代码/专有名词保原文
- 吸收即提炼:外部经验进库前剔除冗余,只留最准确精练的可复用表达;成品不点名外部仓库,吸收后都是本仓知识
