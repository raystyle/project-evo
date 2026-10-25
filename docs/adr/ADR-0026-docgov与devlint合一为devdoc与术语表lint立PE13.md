---
id: ADR-0026
title: doc-gov 与 dev-lint 合一为 dev-doc,语言面裁撤与约束术语表 lint 立 PE-13
status: accepted
date: 2026-10-26
---

# ADR-0026:dev-doc 合一与术语表 lint PE-13

## 背景

用户令(2026-10-25):doc-gov 与 dev-lint 应转换为一个 dev-doc,只专注项目文档结构与项目文档;参照 search-harness 先例与 ctxs 历史对话语料,定义一个中英文约束术语扫描的 lint 脚本,专修不标准中文、英文黑话、俚语与短语。先例结论(search-harness 驻仓 grok 简报):该仓非 lint 先例,取「规则函数纯函数化 + 单测锁阈值 + 夹具可重放」骨架;lint 规则真源留本仓 mdrules 形;语料走 ctxs/gw_logs。三项执行决策经用户选定制:语言面裁撤(留结构面)、进门禁分批收紧、旧词表作底加语料增补。

## 决策

1. **合一**:doc-gov 与 dev-lint 合并为 `dev-doc`(git mv 保史)。router 形 SKILL.md(80 行),references 10 篇扁平前缀分组(base/tool 五篇 + md-faces + term-rules 新术语面 + ls 三篇);计数两插件十四 skill(dev 二加 evo 十二)。
2. **语言面裁撤**:cargo fmt/clippy/ruff/tsc/eslint 语言三面检查知识退出 skill(lang-checks.md 删,git 史可复,同 zh-lint 批 145 先例);结构面(四类型模板卡、声明式规则件)保留;hook 面残余知识(md-guard/lint-hook 手动道、行量表)并入 md-faces。
3. **约束术语表 lint**:词表唯一权威 `plugins/dev/scripts/termrules.py`(term-lint/term-mine sibling);zh-lint 词表(git 9189048^ 复原)作底加 gw_logs 语料挖词(S020,16.2 万块实证);两层政策 ENFORCED(零基线命中强制)与 PENDING(存量待清,迁入即收紧)。
4. **门禁接线**:check.py PE-13(root 三件 + docs/,PEVO_TERM_ALLOW 同 PEVO_CHECK_ALLOW 惯例豁免 docs/ 档案,根三件永不受益);pre-commit 加 term-lint --staged;仓级回归测试锁 ENFORCED 零命中契约。
5. **版本**:dev 0.16.1 至 0.17.0(skill 集变更);evo 0.19.0 至 0.19.1(跨插件引用改)。

## 后果

- doc-gov 与 dev-lint 名从市场消失,旧名作 dev-doc 触发词保留;装端须翻台重载,卸旧 skill 目录。
- 语言面知识只在 git 历史;新仓语言面门禁不再由本仓 skill 覆盖。
- 术语表收紧通道:PENDING 存量词清完存量后迁 ENFORCED(如 `收口` 45 处、`沉淀` 39 处、`缺省` 31 处),迁移即收紧,回归测试守底;「进行中」状态形须排除。
- 历史档案不回写:CHANGELOG、既有 ADR/REQ、research 中旧名为当时事实,不回写;映射以本 ADR 为准。
