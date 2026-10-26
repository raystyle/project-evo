---
patterns: [三层聚合结构, sources 层, knowledge 层, operations 层, 双链, 单向支撑, 出处层, 标准面]
---

## distil 三层聚合结构指导

- 三层单向支撑:sources(唯一出处层:自产轨迹/自产证据/外档原档,只增不改)> knowledge(带版本双链结构化知识:模式页/防重提页/索引流水)> operations(标准面:标准 hook rule 件与 how-to 手册,过闸才进);反向不成立
- 硬规则:模式页无 trace 引文标 unverified 不得当提案依据;标准件无 knowledge 链接不得当规范执行;原理不进标准面,步骤不进知识页,正文不进索引
- 记忆映射(CoALA):sources 约 episodic、knowledge 约 semantic、operations 约 procedural;工作记忆不进三层
- sources 三类出处分根收口(轨迹/证据件/外档原档),一层一索引;证据分级靠 relation(derived_from 自产撑模式页,cited_source 外档撑综述)
- 资格过滤在前:零工具调用、空输出、启动失败回合不进样本不进分母;每条样本带可回查指针(git sha 或会话文件路径)
- 冲突裁决:标准页与知识冲突,带 sources 的 knowledge 页为准
