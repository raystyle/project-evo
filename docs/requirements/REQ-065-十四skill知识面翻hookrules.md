---
id: REQ-065
title: 十四 skill 知识面翻 hook_rules(薄壳指针与双加载器,批 176)
status: implemented
priority: must
trace: tests/test_project_evo.py
---

# REQ-065:十四 skill 知识面翻 hook_rules

## Scenario

总台令(2026-10-26,批 176,用户裁定蒸馏体系转向):蒸馏产出物从 skill 翻转为 hook rule;全部 skill 转 hook rule 无一保留(可执行件面例外)。转换清单先报后动:十四 skill 映射表(意图件与拆件粒度、patterns 词表来源、dev-rules 路由)、三裁定(双层树插件随装优先、薄指针壳、守卫翻树扫描)获总台放行后动工。真源(两样例件 + 两加载器)s5 取得并本机实弹(bun 1.3.14 注入通过)。

## Criteria

- [x] 双加载器落地:intent-guidance.ts(UserPromptSubmit)与 dev-rules.ts(PreToolUse Edit|Write),双层树(项目 .claude/hook_rules 先、插件 CLAUDE_PLUGIN_ROOT/hook_rules 后,项目优先);dev 正源 evo 拷贝,守卫测字节等一;本机实弹注入与静默退出验证
- [x] hooks.json 双插件各挂两事件,`${CLAUDE_PLUGIN_ROOT}` 花括号形,statusMessage 插件前缀英文短形;PostToolUse 禁令不破(批 105/174 律)
- [x] hook_rules 树:evo intents 26 件(十二域主件加 agents 七、desks 一、research 四、distil 五拆件)、dev intents 六件加 dev-rules 四件;词表取自原 description 触发词与 Use when 行
- [x] 薄壳:十四 SKILL.md 留 name + 原 description + 指路句;references 目录全撤;dev 模板四 toml 迁插件级 tools/
- [x] distil 环翻转:产出物 = 标准 hook rule 件(create/patch/retire 语义、闸门加 pattern 实弹验证判据:应触发至少一命中、近失零误命中、含糊独立判)
- [x] 守卫翻新:hooks 形态守卫重写、hook_rules 树扫描测(frontmatter/正文/禁字/术语/计数)、pre-commit 断链段加 hook_rules 两子树、加载器实弹测(bun 缺则 skip);38 测全绿
- [x] 活面同步:AGENTS 定位与断链行、根 README 配置节与表行与 Kimi 节、docs 地图、gates、双插件 README、双 manifest 与市场清单描述、版本(dev 0.18.0、evo 0.20.0)
- [x] 治理:ADR-0027 立档、REQ-065 本单、CHANGELOG 批 176 入册、索引登记
