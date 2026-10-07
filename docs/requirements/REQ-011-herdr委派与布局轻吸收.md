---
id: REQ-011
title: herdr 委派与窗格布局轻吸收(lane 分发、四窗格定式、py 脚本评估)
status: implemented
priority: must
trace: tests/test_project_evo.py
---

# REQ-011:herdr 委派与窗格布局轻吸收:lane 分发、四窗格定式与 py 脚本评估

## Scenario

用户立单(2026-10-07,两单):①吸收蒸馏 herdr-dispatch 任务分发编排,改进 herdr skill,并评估是否针对 grok、kimi、codex 委派与窗格布局开发集成 herdr 的 py 脚本;②吸收 PI 智能体五窗格开发布局模式(用户裁定:五窗格仅 PI 开发模式,通用四窗格足够,自省位可由 codex 替代)。

## Criteria

- [x] S011 与 S012 研究档案落 docs/research(对照分流六态标注,信源点名止于档案面),docs 地图登记
- [x] herdr-flywheel 新增「窗格布局定式与双闸门」节(通用四窗格、PI 五窗格特化、先推后审、会话纪律、重载铁律、TUI 就绪探测)与「任务分发 lane 模型」节(lane 恒禁发布、状态台账唯一真相、身份核验)
- [x] references/lane-dispatch.md 新篇(lane 结构、探针契约六字段、codex 与 grok 启动特化、发布纪律与预检降级);pitfalls.md 增三坑(agent 名回收、done 假象多源、TUI 未就绪悬输入框)
- [x] frontmatter description 与触发词同步(窗格布局、lane、worktree、codex、grok、kimi)
- [x] py 脚本评估结论:不开发(纯 skill 加内联探针够用、沉淀铁律未触发、活权威是 herdr --skill),记 S011 与 ROADMAP 待定行;kimi 委派无上游参照,待专项研究不臆造
- [x] CHANGELOG 第九十批、ROADMAP 里程碑行;pytest 全绿加 md-ref-scan 零断链
