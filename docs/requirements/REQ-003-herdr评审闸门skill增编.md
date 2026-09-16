---
id: REQ-003
title: herdr 评审闸门 skill 增编
status: implemented
priority: must
trace: tests/test_project_evo.py
---

# REQ-003:herdr 评审闸门 skill 增编

## Scenario

工位侧评审闸门惯例(交付批经 herdr 右侧 codex 会话对齐后推 main)已有充分实证(十五条发现五轮复核链、D46 至 D53 请求回执原文、命名评审格实况),但散在各仓合同与 proven 档案,新工位接入靠口口相传。用户裁定沉淀为 evo-herdr 第二 skill herdr-review,并要求评审格具备「检测右侧、无格建格起 codex、有格直接对话」的自愈程序。

## Criteria

- [x] skill 落位 `plugins/evo-herdr/skills/herdr-review/`(SKILL.md + references 四篇加索引),frontmatter name 与目录一致,description 兼具做什么与何时用触发词
- [x] 内容按吸收即提炼自工位实证:请求五件模板、F/G/CONFIRM 三态回执与轮次、发现核实与交叉复核、窗格挂位命名与检测带起程序,纪律条目带实证标注
- [x] 命令块本会话实证:herdr pane neighbor/split、agent start(建格 evo-codex-review 于 project-evo 工位右侧)、agent list、hst trace sessions/search
- [x] evo-herdr 双 manifest 与双市场条目描述同步两 skill;守卫测试 SKILLS 断言 evo-herdr 双 skill 且全绿
- [x] herdr-flywheel 参考节加反向指针,协议面与评审特化边界互指;立 ADR-0011 修订 ADR-0010 七 skill 清单条款
- [x] uv run pytest 全绿;md-ref-scan 八 skill 零断链
