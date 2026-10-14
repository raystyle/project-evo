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
- 分层原则:references/ 每篇一主题自包含完整参考;实现代码放插件级 `scripts/`(如 dev 的 md-guard 加 mdrules,hook 与 skill 解耦)或仓自用 `.tools/`(PEP 723 零依赖;禁字规则唯一权威在 dev 的 `scripts/mdrules.py`,check PE-11/scan/md-guard 三面同源)

## 命令指导类 skill 写作标准（舰队规范）

> 出处 = fleet room/gateway-logging 流「命令指导 SKILL 写作标准 · 草案」;参照 [agentskills spec](https://agentskills.io/specification) 与 [Anthropic skill best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)。

- **description ≤400 字符**(硬顶 1024):一句职责第三人称 + 触发场景与触发词;旗标、端口、路径、凭据、版本、分工不进
- **正文节序**:动词表(动词、文法、何时用;何时用写任务不写同义词)到 文法(三至六条会改变敲法的;共享规则一行指属主)到 示例(一块,每动词恰一条,块下不讲解)到 坑表(列只有「错」与「对」,对 = 下一步动作或判定句)到 接着读(至多三条带何时读);定位段删除,分工一行
- **旗标全集与默认值不进正文**:一行「以 <cmd> --llms 为准」;与 --llms 冲突时改技能不改命令
- **行量**:正文 80 至 120 行(硬顶 150);单份 reference 至多 150 行(过 100 行顶上写目录);动词超 8 个时族细节下放 references/<族>.md
- **references 三档**:pitfalls.md(现行坑反例,80 行)/rulings.md(日期现象结论档案,正文不链)/obsolete.md(废止敲法,正文不链);批号不进这三档,进 git
- **验收八条**:description 无旗标路径版本批号;正文首节是动词表;每动词示例恰一次;坑行可独立执行或判定;全文检索不到批号实证根修定谳;同一事实只出现一处;正文无指向 reference 的 reference;抽三命令对 --llms 文法一致

## 写作约束

- 禁止 emoji;流程图用 mermaid,禁止 box-drawing 手拼伪流程图
- 事实性断言标六态:`[实证]/[推断]/[经验]/[记忆]/[假设]/[直觉]`
- 中文为主;命令/代码/专有名词保原文
- 吸收即提炼:外部经验进库前剔除冗余,只留最准确精练的可复用表达;成品不点名外部仓库,吸收后都是本仓知识
