---
id: REQ-056
title: skill description 定稿三句形落地(批167)
status: implemented
priority: must
trace: tests/test_project_evo.py
---

# REQ-056:skill description 定稿三句形落地

## Scenario

总台终卷定稿单(2026-10-15,grok F1-F6 加 hst_rs T1-T3/A 族合流):七条 frontmatter description 按三句形重写(一句做什么、一句 Use when 中英触发词、一句不要用于),每条预算约 100 token 不顶满,删旧同义词串不追加;中文词只进 description(name 加 description 常驻命中)。顺批:commands.md agents 行 DELIVER 注「(prompt = 别名)」残清(F5 退役后残留,hst_rs 顺带审出);collab 补 A 族易混场景速判注记(在跑族/实时族/知会)。

## Criteria

- [x] 七域 description 三句形逐字落总台定稿文(agents/shares/streams/pipes/ports/tasks/ctxs,84 至 128 字符)
- [x] commands.md `(prompt = 别名)` 残清
- [x] collab 与邻面分工补 A 族速判注记(在跑族:agents view 或 tasks view;实时族:pipes 字节或 streams -f 消息;知会:to 直达或 streams 留痕或 tasks 记住)
- [x] evo 独立升 0.16.6;门禁全绿 + 镜像推 + fleet 回执
