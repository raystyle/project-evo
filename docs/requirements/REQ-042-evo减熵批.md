---
id: REQ-042
title: evo 插件 skill 减熵批(正文只留正确用法)
status: implemented
priority: must
trace: tests/test_project_evo.py
---

# REQ-042:evo 插件 skill 减熵批

## Scenario

总台派单(2026-10-14,用户令):evo 全套 skill 内容减熵,「废话和历史轨迹和解释太多,应该聚焦于正确的」。裁定:正文只留动词表、文法、示例最小集、坑的一句话正确姿势;批号引用、根修来龙去脉、误判轨迹撤出正文(出处与演变史归 changelog,不混正文);commit 与 REQ 台账照旧不改史;下批起 commit 标题一行减熵。

## Criteria

- [x] 六域 SKILL 正文减熵(ctx 先行):叙事、批号、实证标签与根修史清除,坑表一行正确姿势;frontmatter description 不动(发现面)
- [x] references 知识面同尺:[实证:批 X] 收敛为 [实证],commit 哈希沿革注记收简,判例叙事去轨迹留规则
- [x] 功能描述零漂移:ctx search 多词实弹自验绿(退 0 出 snip);动词、旗标、语义、窗口、分工全保
- [x] evo 独立升 0.15.3;四门禁全绿 + fleet 回执带前后行数对比;本批 commit 标题起一行形
