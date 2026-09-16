---
id: REQ-004
title: 命令出错自动上报 issue 的 gh-issue 增编
status: implemented
priority: must
trace: tests/test_project_evo.py
---

# REQ-004:命令出错自动上报 issue 的 gh-issue 增编

## Scenario

本机命令/工具出错时(如 CLI 报错),向对应程序的上游 GitHub 仓报 bug 仍是手工路径:找仓、搜重复、手写正文、网页发单,口径散且慢。用户裁定(2026-09-16)沉淀为 evo-adr 第三 skill gh-issue:经 gh 自动发 bug issue,无草稿确认闸,组装完直接 gh issue create;发前必去重,命中 open 重复则不发并回执附既有链接。

## Criteria

- [x] skill 落位 `plugins/evo-adr/skills/gh-issue/`(SKILL.md 加 references 三篇含索引),frontmatter name 与目录一致,description 兼具做什么与何时用并含触发词
- [x] 工作流五步成文:定位目标仓(git remote 与 gh repo view 自取,禁硬编码映射表)、双通道去重与四格判定、模板化组装(截断与脱敏纪律)、label 与权限预检后 gh issue create、三态回执
- [x] 无草稿确认闸(用户裁定明写入文);唯一停点为信息缺失,非人工确认
- [x] 命令块本会话实证:git remote get-url、gh repo view、gh search issues、gh issue list --search、gh label list、gh issue create(本仓自发实证单,验后即关)、gh issue view、gh issue close、gh auth status
- [x] 同步面全改:双 manifest 与市场条目描述、守卫 SKILLS 九 skill、pre-commit 第九段、AGENTS 与根 README 与 docs 地图与 gates 计数、evo-adr README、CHANGELOG、ROADMAP、diary;立 ADR-0012 修订 ADR-0010 八 skill 清单条款
- [x] uv run pytest 全绿;md-ref-scan 九 skill 零断链
