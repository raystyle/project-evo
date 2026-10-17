# S016:SKILL 双规范业界先例对照

> 三人组合稿研究轮:研究方 grok(w13:pB)业界先例调研,原文键 `share/lan-win/ca5de0e026/skill-spec-precedent.txt`(2026-10-16 实查);真源方(evo-claude-1)校准与计数勘误;产物 = `../guides/skill-spec.md` 规范 A/B。本文是信源与分流档案,规范条目以 guides 为准,不在此重复全文。

## 信源

- [agentskills.io specification](https://agentskills.io/specification)(2026-10-16 实查)[实证]
- [Claude Code 产品页](https://code.claude.com/docs/en/skills) 与 [发布公告](https://claude.com/blog/equipping-agents-for-the-real-world-with-agent-skills)(2026-10-16 实查)[实证]
- [Cursor rules](https://cursor.com/docs/rules)、[Aider conventions](https://aider.chat/docs/usage/conventions.html) 与 [conventions 示例仓](https://github.com/Aider-AI/conventions)[实证]
- [OpenAI Custom Instructions](https://help.openai.com/en/articles/8096356-custom-instructions-for-chatgpt) 与 [自定义 GPT 指南](https://help.openai.com/en/articles/9358033-key-guidelines-for-writing-instructions-for-custom-gpts)[实证]
- 本仓 dev-lint md 面(references/md-faces.md)与现役十一面 SKILL.md 实测点数(2026-10-17,真源 0.16.7)[实证]

## 关键口径（实查结论）

- **description 双口径**:规范硬顶 1024 字符;Claude Code 列表层把 description 与 when_to_use 拼条、每条截 1536 字符、从尾部切;溢出先拿掉最少调用技能的描述。触发词放最尾会被截掉。[实证]
- **渐进三层加载**:启动层只装 name 与 description(规范说法约 100 token 每技能,是预算指导语不是门禁数);命中层装整份 SKILL.md(建议 <5000 token、<500 行);scripts/references/assets 用到才读。[实证]
- **name 硬标准**:1-64,小写字母数字连字符,不首尾连字符不连续连字符,等于父目录名。[实证]
- **可选字段全集**:license、compatibility(≤500)、metadata(字符串映射)、allowed-tools(实验,空格分隔);产品页多出字段(when_to_use、argument-hint、paths、disable-model-invocation)非规范字段,Claude 端静默忽略、校验器可能拒。[实证]
- **正文无强制节序**:规范建议正文含步骤、输入输出示例、常见边界;任何固定节序属治理层追加。[实证]
- **引用一层**:从 SKILL.md 相对路径只走一层,引用不套引用(第二层模型经常不到)。[实证]
- **Cursor 对照**:rules 四触发面(alwaysApply 每会话注入/globs/description/手动点名),单文件 <500 行,大规则拆组合文件;AGENTS.md 通道自动注入无按需开关。任务技能不该走每会话注入通道。[实证]
- **Aider 对照**:CONVENTIONS.md 无 schema 无渐进加载,列入即每会话在场;只读可吃提示缓存。[实证]
- **OpenAI 对照**:Custom Instructions 上限 1500 字符(帮助中心原文);触发与指令成对、分隔符分段;技能正文落开发者或用户层,压不过根与系统层。[实证]

## 对照分流（吸收与不吸收）

| 先例要点 | 分流 | 落点 |
| --- | --- | --- |
| 触发面只写 description | 吸收 | 规范 A1 |
| 排除面(不要用于)进 description 防误唤起 | 吸收 | 规范 A2 三句形第三句 |
| 关键用例前置、触发词不放最尾 | 吸收 | 规范 A3 |
| 命令引用完整参数行、不写转述 | 吸收 | 规范 A5 |
| 一事实一处、引用不套引用 | 吸收 | 规范 A6/B12 |
| 渐进三层与 5000 token 建议 | 吸收 | 规范 B5 |
| 产品页扩展字段禁入跨端技能 | 吸收 | 规范 B1 |
| 反模式:无点数不写分布、禁句只打一次 | 吸收 | 规范 A12 |
| 正文加「何时用」节 | 不吸收:与 description 触发面重复,违反一事实一处 | 无落点 |
| 动词表加「是否改状态」列 | 不吸收:七域实测动词 3-6 个,增列 token 成本大于判别收益 | 无落点 |
| 坑表三列(现象/原因/下一步) | 不吸收:两列「错/对」实测够用,对列自带动作 | 规范 B10 维持两列 |
| tasks 类技能走 alwaysApply 式常注入 | 不吸收:与本仓渐进加载立场相反 | 无落点 |
| Cursor alwaysApply 通道与本仓门控纪律互文 | 互文不吸收:本仓同问题的解是门控与知会而非常注入:agents 门控 v2 只拒操作对话框、拒投代记不丢件、tasks set 只写不扰(to 加知会才扰)、nodes yolo 属执行侧豁免不是注入侧开关;共同底色 = 注入面最小化,代价承担面不同(Cursor 付上下文,本仓付一次知会握手) | 规范 B5/B15 侧记 |

## 计数勘误

- 研究方原文称本仓「SKILL.md 共 10 份,description 最小 113、中位 190、最大 550」;真源 0.16.7 实测 = **11 份**(dev 3 + evo 8),description 最小 99(shares)、中位 173(streams 按字符序取第 6 位)、最大 563(doc-gov)。差异判定 = 研究方在总台侧旧市场缓存(0.15.13,十 skill 时代)点数,非真源。[实证]
- evo 八面 description 全部 ≤400;dev 三面 393/540/563,两面超 400,dev 批收口在案(REQ-058 修批清单)。[实证]

## 六态声明

本文事实断言以 2026-10-16/17 实查与实测为底,全部 [实证];未实测社区仓行数分布,不写分布结论。
