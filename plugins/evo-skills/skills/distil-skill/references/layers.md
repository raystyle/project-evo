# 三层聚合:轨迹总结、双链知识与标准 skill

> 原语沿知识库三层聚合(sources、knowledge、operations 单向支撑),在技能自进化语境下各层收窄定形:sources = 带时间的历史轨迹总结,knowledge = 带版本的双向链接关联结构化知识,operations = 项目级标准 skill。本篇管三层结构、写法与流转;环与闸门见 loop.md 与 gate.md,双端加载见 backends.md。

## 三层结构(单向支撑)

| 层 | 承载 | 回答 | 形态 |
| --- | --- | --- | --- |
| `sources/` | 带时间的历史轨迹总结(会话、日记、回执、门禁输出、评审记录按时间收束) | 发生过什么、出处是什么 | 带时点的轨迹总结件,只增不改 |
| `knowledge/` | 带版本、双向链接关联的结构化知识(模式页、防重提页、索引与流水) | 是什么、为什么 | 版本化知识页,[[双链]] 关联 |
| `operations/` | 项目级标准 skill(Claude Code 与 Codex 双端支持的标准 SKILL.md) | 怎么做、验收什么 | 标准 SKILL.md 集,过闸才进 |

- 单向支撑:knowledge 页靠 sources 撑,标准 skill 靠 knowledge 撑,反向不成立
- 硬规则:模式页无 trace 引文标 unverified,不得当提案依据;标准 skill 无 knowledge 链接不得当规范执行;原理不进标准页,步骤不进知识页,正文不进索引
- 流转:新轨迹入库 = 新建或追加 sources 件加更新对应 knowledge 页并链接;模式已稳要落地 = 提案进 operations(走闸门);标准页与知识冲突 = 带 sources 的 knowledge 页为准

## sources 轨迹总结层

- 每条轨迹总结带时点(日期加场景标识),一段收束一个执行片段:做了什么、结果、证据指针(会话文件路径、commit sha、门禁退出码);不贴原始长转录,留指针
- **资格过滤在前**:零工具调用、空输出、启动失败的回合不进样本也不进分母;死会话对陈旧交付物的打分是假证据,资格检查没接通前不开蒸馏
- 只增不改:轨迹是历史,修正走新条目,不回写旧条;一天一篇的轨迹总结写法与升格分流见 trajectories.md

## knowledge 双链知识层

- **模式页**(patterns):PROBLEM、ROOT CAUSE、FIX 三段,10 至 30 行;FIX 只许一句非步骤结论(不含命令与步骤,可执行步骤只出现在标准 skill 页);写行动模式不抄报错;对照成功轨迹保留有效行为;必带 trace 引文(sources 路径加时点或片段),无引文标 unverified;合并重复,不发明轨迹不支持的模式
- **防重提页**(skill-impact):收被拒提案全文与 diff,只由闸门追加;蒸馏与提案角色对它只读,丢失或改写即本轮蒸馏失败;提案前必读,防重复已拒路线
- **索引与流水**:索引是可再生成的导出物(不是唯一入口,漏行不能让磁盘上的模式页不可见);流水按轮次记蒸馏、提案、闸门三行结论
- **双链与版本**:知识页 frontmatter 登记 `links`(target 加 relation)与版本;正文 `[[路径去 .md]]` 双链,单独成行挂主题、句中作参见;检索跟双链展开默认最多 2 跳,要出处再进 sources

## operations 标准 skill 层

- 产物是 Claude Code 与 Codex 双端支持的标准项目级 SKILL.md:frontmatter 只留官方字段(name、description 等,禁 version 等非官方字段);正文含 When to Apply 与 When NOT to Apply(不适用面是防「一个失败模式写成通用技能」的槽)与步骤;正文不点名外部仓库
- **git 协议**:候选先落未提交工作区;接受才 commit;拒绝即 reset 回基线提交;knowledge 是独立 git,永不随标准集回滚
- 唯一权威源在项目仓;双端按各自项目级面加载(见 backends.md),不分发第二份

## 建仓五步

1. 立三层目录与各自索引,git 各自独立(knowledge 与 operations 分仓或分目录分 git)
2. 首批轨迹总结带时点入库,既有项目经验先收口
3. 蒸馏首批模式页,带 trace 引文与 links
4. 立防重提页与流水,空态也要立(见gate.md)
5. 标准 skill 集从空态起步,一切进集走闸门
