---
id: ADR-0027
title: 十四 skill 知识面翻 hook_rules,薄壳指针与双 bun 注入加载器
status: accepted
date: 2026-10-26
---

# ADR-0027:知识面翻 hook_rules 与薄壳指针

## 背景

总台裁定(2026-10-26,用户令,蒸馏体系转向):蒸馏技能的产出物不再是 skill,而是 hook rule。总台已建成 hook_rules 注入体系实弹验证(结构化 md 树:frontmatter patterns/match 加正文即注入内容;加载器两枚 bun 脚本:UserPromptSubmit 意图识别 + PreToolUse Edit/Write 路径规则)。知识沉淀从 SKILL.md 常驻文档改按意图/路径即时注入,token 经济学更好(常驻 description 占上下文对按需注入)。

追加裁定:全部 skill 转 hook rule 无一保留;唯一例外 = 带 tools/scripts 的可执行件面保留。三落地裁定:① 双层树,插件 hook_rules 留插件目录(CLAUDE_PLUGIN_ROOT,单一真源随装随卸零残留),不落全局树;加载器搜项目树先插件树后,项目优先。② 薄指针壳:SKILL.md 留 name + description + 指路句,非 hook 端(Kimi 等)靠壳直读 md,知识零失效。③ 守卫全翻 hook_rules 树扫描。分型:TS 走 bun 主道(node 备道 tsx)、python 走 uv、rust hook 归 pi-rs-plugins。

## 决策

1. **结构**:每插件 `hook_rules/intents/*.md`(patterns 词表)+ `hook_rules/dev-rules/*.md`(match 字面或 /regex/);加载器双拷贝(dev 正源 evo 拷贝,守卫测字节等一);hooks.json 挂 UserPromptSubmit + PreToolUse(Edit|Write matcher),`${CLAUDE_PLUGIN_ROOT}` 花括号形;PostToolUse 禁令不破(批 105/174 裁撤律只禁 PostToolUse)。
2. **薄壳**:十四 SKILL.md 留 frontmatter(name + 原 description,三句形守卫仍过)+ 一句指路;skill 目录计数不变;references 目录全撤;dev 结构模板四 toml 迁插件级 tools/。
3. **件粒度**:evo intents 26 件(十二域主件 + agents 七拆件 + desks 一拆件 + research 四拆件 + distil 五拆件);dev intents 六件 + dev-rules 四件。
4. **distil 环翻转**:产出物由标准 skill 集改标准 hook rule 集;闸门加 pattern 实弹验证判据(词表每词应触发样本至少一命中、近失零误命中;pattern 无效即提案失败)。
5. **守卫**:hooks 形态守卫重写(恰挂两事件、花括号形、statusMessage 英文短形带插件前缀);hook_rules 树扫描测(frontmatter 非空、正文非空、禁字与术语清零、计数断言);pre-commit 断链段加 hook_rules 两子树;加载器实弹测(bun 子进程,缺 bun skip)。
6. **版本**:dev 0.17.0 至 0.18.0、evo 0.19.1 至 0.20.0。

## 后果

- 知识注入即所得:意图命中或路径命中才注入,常驻上下文只余薄壳 description;非 hook 端读同源 md,知识零失效。
- 双端加载差异:Claude Code 端自动注入;Kimi 端拷 skills 加 hook_rules 靠壳指路(additionalContext 已验不支持:源码 HookSpecificOutputSchema 不消费该字段,官方 issue #4255 open;若 kimi 端要注入须改道 UserPromptSubmit 纯文本 stdout 或 message 通道);codex/grok 支持面待舰队核验。
- SKILL.md 正文退出市场历史可溯(git 史);新知识面变更入口 = hook_rules 加件或改件,蒸馏闸门管辖。
- bun 依赖进插件前置(加载器 .ts 直跑);node 备道与 rust hook 面另属(pi-rs-plugins 承接)。
