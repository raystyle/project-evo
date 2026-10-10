---
id: REQ-018
title: 三插件五 skill 版图与 distil-skill 技能自进化
status: implemented
priority: must
trace: tests/test_project_evo.py
---

# REQ-018:三插件五 skill 版图与 distil-skill 技能自进化

## Scenario

用户立单(2026-10-10):与 grok 邻格对照研究 wikiskill(arXiv 2608.27454 实现,快照 cdc291c,研究轮 wiki-01 走产物契约协议)后,把 doc-gov 的三层聚合剥离,立第三插件 evo-skills 承载新技能 distil-skill:项目基于自身执行经验自动产生并迭代项目级标准 skill,支持 Claude Code 与 Codex 双端。裁定:sources = 带时间的历史轨迹总结,knowledge = 带版本的双向链接关联结构化知识,operations = 双端标准项目级 SKILL;doc-gov 聚焦 ADR/REQ、代码 doc 注释、文档即代码,日记转 distil-skill,agent 原生面抽离 native-design;herdr-dev 更名 herdr-orch(主开发台初始各工作角色邻居窗格并开始配合工作,功能不变),herdr-flywheel 专注跨仓库跨项目跨机器交流,两 skill 通用「herdr 态是检测信号,md 文件是状态与产物」原则。

## Criteria

- [x] evo-skills 插件落地(双 manifest、README、四端安装面),distil-skill 含 SKILL 与 references 五篇(layers、trajectories、loop、gate、backends)加索引
- [x] 三层定义按裁定:operations 产物为双端支持的标准项目级 SKILL(agentskills 官方 spec 形态);合取闸门三条、no_action 合法出口、知识层永不回滚入条文;双端命令面以本机 --help 实查为准(ADR-0010 实证;无头模式三档入 backends)
- [x] doc-gov 三向拆分:base-coe 删(知识升级进 layers)、base-diary 迁为 trajectories、agent-face 与 tool-cli-agents 与 templates 迁入新 skill native-design;doc-gov references 收 5 篇并新立 base-code-doc;SKILL 意图路由与 description、evo-doc 双 manifest 与 README 同步
- [x] herdr-dev 更名 herdr-orch(目录、frontmatter、互引、测试清单、pre-commit、市场面全同步),定位改述主开发台初始角色邻居窗格配合工作;herdr-flywheel 定位收准跨仓库跨项目跨机器;通用跨窗格交流原则入两 skill
- [x] ADR-0020 立档登记;S014 研究档案落档登记;版本线三插件统一 0.6.0(双 manifest、市场清单、三 README);AGENTS.md、docs/README.md、根 README 同步
- [x] 门禁全绿:pytest 26 用例、md-ref-scan 五 skill、check 12 项、scan 带豁免;CHANGELOG 第一百批;wiki-02 评审轮三建议吸收、蒸馏环最小实测走通(确认选择屏坑入 pitfalls)
