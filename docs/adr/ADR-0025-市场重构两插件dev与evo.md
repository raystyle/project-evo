---
id: ADR-0025
title: 市场重构:两插件 dev 与 evo,裁四 skill,五原语拆分与两改名
status: accepted
date: 2026-10-13
---

# ADR-0025:市场重构（两插件 dev 与 evo）

## 背景

用户令(2026-10-13,数条渐进定形):project-evo 是市场名,不需要那么多插件,装一个 evo 插件就可以(非市场唯一插件,以后还会有);不需要 herdr-orch、agent-s5、agent-rloop;agent-prim 拆分成五个原语 skill;再开 dev 插件,doc-gov 进去,doc-cli 改名 dev-cli 进去;lint 三 skill 也进 dev;distil-skill 改名 distil(触发 = 蒸馏);agent-doctor 去掉。此前形态 = 五插件十一 skill,插件层过碎。

## 决策

1. **市场终形 = 两插件十 skill**:dev(开发治理面:doc-gov、dev-cli、dev-lint、zh-lint)与 evo(agent 操作面:agents、shares、streams、tasks、pipes、distil)。市场后续按域可再添插件;本轮由单插件 evo 中途定形为两插件;lint 三 skill 先并一 dev-lint(用户令续令),中文面经用户裁定拆回 zh-lint 独立(批 144,采纳 grok 评审 2 触发竞争论)。
2. **裁撤四 skill**:herdr-orch(淘汰序由留档改删除,推翻批 137 过渡安排)、agent-s5(s5 引擎面,取用行所需 s5 知识内嵌五原语 skill)、agent-rloop(循环协议,hst task 引擎面自持)、agent-doctor(四端配置诊断)。
3. **agent-prim 拆分**:五原语 skill = `agents`/`shares`/`streams`/`tasks`/`pipes`(skill 名即命令名,触发词直配);共享面(id 三产生式、命名标准、门控 v2 尾窗、信封 v2、status 四态、协作惯例、差异表)归 `agents` 独家 references,四域 skill 单文件自持加相对链接,守单一权威源。
4. **两改名与一合并**:doc-cli 改名 `dev-cli` 随 doc-gov 归 dev;distil-skill 改名 `distil`(触发词蒸馏);md-lint、ls-lint、zh-lint 合并为 `dev-lint`(references 扁平前缀分组,工具与模板随迁)。
5. **插件级资产随域走**:md-guard、mdrules、lint-hook 与写后静检 hook(statusMessage 段名 dev file-check)归 dev;evo 纯 skill 面。
6. **版本与部署**:版本线 0.12.2 进 0.13.0(两插件同线);旧五插件市场条目移除,各端重装 dev 与 evo。
7. **历史档案不回写**:CHANGELOG、既有 ADR/REQ、research 沿革中旧名为当时事实,不回写;映射以本 ADR 为准。

## 后果

- 当前版图 = dev 四 skill 加 evo 六 skill;守卫与挡板(测试 PLUGIN/SKILLS/市场一致性/断链段/段名断言/计数守卫,pre-commit,check.py)随形改;「五插件同版本线」律改两插件同线。
- herdr-orch 教学内容与 agent-doctor 诊断面随删退出市场;回溯走 git 历史与本 ADR。
- 先例回环:v0.3.0 曾单插件形态(批 47),后拆五,今回环再分域。
