---
id: S014
title: wikiskill 对照:三层聚合成技能自进化
state: 已完成
date: 2026-10-10
sources:
  - ashutoshsinghpr7/wikiskill main 快照 cdc291c4296e30488a5922860dc596763704ede4(2026-09-16;经 proxy.ohmygh.com 反代抓取 README、docs/RUNS.md、skills/wikiskill-evolve)
  - grok 工位 wiki-01 研究委托轮产物笺(/tmp/herdr-flywheel/2026-10-10-wikiskill对照/,含浅克隆 52 文件源码级证据)
related:
  - REQ-018
  - ADR-0020
  - REQ-017
---

# S014:wikiskill 对照:三层聚合成技能自进化

## 背景

用户立单(2026-10-10):把 doc-gov 的 COE 三层聚合剥离成「项目级标准 skill 自产生自迭代」技能(distil-skill,新插件 evo-skills),支持 Claude Code 与 Codex 双端;与 grok 邻格对照研究 wikiskill 供料。研究轮走 REQ-017 产物契约协议(brief、state、receipt 三件套,grok 工位 wiki-grok)。

## 过程

- 我方直读:README(进化环、三层布局、双端 backend 表)、docs/RUNS.md 六轮实跑记录(含诚实负结果)、wikiskill-evolve 元技能
- grok 委托轮:浅克隆快照源码级解构(Algorithm 1 四步、wiki 四件、claude/codex 隔离与 transfer、对照 COE 三清单、负结果根因),产物笺逐件带文件路径与行号证据
- 双端命令面本机实查:claude(-p、--output-format stream-json、--permission-mode、--allowedTools、--model)与 codex(exec、--approve-for-me、--skip-git-repo-check、--json、-c)在位
- 后续三轮同日:wiki-02 草案评审(三建议全收)、wiki-03 全库业界对照评估(agentskills spec、Anthropic 写作实践、双市场惯例、agents.md、MADR、Diátaxis;必改二应改三全吸收)、wiki-04 四端无头模式研究(claude、codex、grok、kimi 三档对照,四端推荐形入 backends.md;kimi 无边界内档按全开处置)
- 无头模式业界材料(用户供):claude 权限三态与 --dangerously-skip-permissions 风险面、codex workspace-write 加 on-request 的 Auto 形与 --yolo 边界、分级权限先例;吸收为三档纪律与四端推荐形,成品不点名外部产品

## 结果

对照分流三清单(可吸收、不适用、风险)全量在 wiki-01 产物笺;入 skill 的吸收面:

- 可吸收:三层分目录且 knowledge 与 operations 各自 git、拒绝只回滚技能层;一轮一案(create/patch/no_action);失败为主有限样本蒸馏;被拒提案全文防重提页(对蒸馏者只读);隔离配置目录每回合重建技能链接;transcript 首行计数资格过滤;模式页短结论、标准页分适用与不适用
- 不适用(替身):均值闸门换合取三条(门禁无回归、点名义务翻转、知识链接成立);合成 bench 换项目真实失败义务;满分 early-stop 换「无未覆盖义务或连续 no_action 停机」;跨端转移 = 未提交一案重过闸(不拷完即 commit)
- 风险面入条文:幻觉蒸馏(模式页无引文标 unverified)、闸门假阳(单题回归即拒、单次会话不当分数)、成本(无新义务不跑)、凭据副本不进 git、未过闸蒸馏不进安装路径、文档与实现漂移(命令面活权威 = 本机 --help)

## 关键结论

- [实证] 该实现六轮 live gate 全部为拒绝或 no_action,接受路径仅测试证明;根因 = 验证集无上升空间、失败模式被写成通用技能被闸门正确拒绝、原料层无行为。蒸馏文本不是标准 skill 是本对照最重结论
- [实证] 蒸馏器曾抓到框架自身 bug(死会话对陈旧沙箱打分):资格过滤必须在环前接通,零工具调用回合不进样本与分母
- [推断] 项目治理类任务无自动评分基准,均值闸不可移植;合取闸门(变好而非不变坏)是替身形态
- [经验] prompt --wait 提交即返报 done 而盘上状态档已交:herdr 信号与盘上稳态分治(REQ-017)在本研究轮再次实证

## 参考

- wiki-01 三件套:/tmp/herdr-flywheel/2026-10-10-wikiskill对照/(brief、state、receipt;临时目录,择要已吸收进本档与 skill)
- 落地:plugins/evo-skills/skills/distil-skill/(ADR-0020、REQ-018)
