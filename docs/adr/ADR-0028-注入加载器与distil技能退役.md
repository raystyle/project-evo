---
id: ADR-0028
title: 注入加载器与 distil 技能退役,知识面壳直读定形
status: accepted
date: 2026-11-09
---

# ADR-0028:注入加载器与 distil 技能退役

## Context

批 176(ADR-0027)把十四 skill 知识面翻进 hook_rules 树,并挂两枚 bun 注入加载器
(intent-guidance.ts 走 UserPromptSubmit、dev-rules.ts 走 PreToolUse Edit|Write),按意图
与路径即时注入,SKILL.md 留薄壳指针。实弹一周期后暴露两面问题:

- 注入面重复注入:多路消息同块指导文一回合内重复三到四次,上下文占用反超常驻面,
  token 经济学初衷落空;加载器双拷贝维护与 bun 依赖也是持续成本。
- distil 技能(三层聚合与合取闸门)使用停歇:规则件演进改走总台直接裁定与门禁验收,
  技能面长期无调用,知识件六枚随之闲置。

## Decision

1. 注入面剔除(与总台 3d0fb88、43fea40 两批合流):两插件 hooks.json 留空装配
   {"hooks": {}},两枚 bun 加载器删除,不再走 UserPromptSubmit 与 PreToolUse 注入;
   PostToolUse 禁令(批 105/174 裁撤律)不破。
2. hook_rules 知识树保留,加载路径唯一化为壳直读:SKILL.md 薄壳指针直读
   插件 hook_rules/ 下同名与拆件,与 Kimi 端同道,各端行为一致。
3. distil 技能退役:skill 目录与六枚 hook_rules 知识件(distil、distil-loop、
   distil-gate、distil-layers、distil-trajectories、distil-backends)删除;
   三层聚合方法论存档于 docs/research(S014、S015)与 git 史,需要时再启。
4. 版图:两插件十三 skill(dev 二加 evo 十一);dev 升 0.19.0、evo 升 0.21.0。

## Consequences

- 上下文注入归零:客户端不再收到 hook 注入块,知识按需由 agent 读壳指路后直取;
  各端(含 Kimi)加载行为统一,无双端分叉。
- 守卫:装配守卫改两插件 hooks.json 均须空、加载器均须删(总台批);本批同步
  SKILLS 与 HOOK_RULES 计数断言(evo intents 27 减 21);pre-commit 断链段去 distil 树。
- distil 退役后,标准规则件变更不再有合取闸门机检面,改由门禁(pytest、check、
  scan、term-lint、md-ref-scan)与评审承担;后续若重启技能自进化,须新 REQ 立项。
- 插件更新走同版本内容修正三步正序判例(marketplace update 先于缓存删)。
