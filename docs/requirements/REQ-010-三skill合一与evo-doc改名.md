---
id: REQ-010
title: 三 skill 合一为 doc-gov,evo-adr 改名 evo-doc,skill 与 hook 解耦
status: implemented
priority: must
trace: tests/test_project_evo.py
---

# REQ-010:三 skill 合一为 doc-gov,evo-adr 改名 evo-doc,skill 与 hook 解耦

## Scenario

用户立单(2026-10-07,五令):三 skill 合一为 doc-gov、插件改名 evo-doc、skill 与 hook 解耦(md-guard 上插件级 scripts)、init/check/scan 与模板移本仓 .tools 且斜杠命令删除、知识面收敛 ADR 加 COE 加项目日记三形态与 Agent 友好 CLI 架构标准(其余复杂面移除);市场收敛两插件三 skill,版本线 0.4.3 不动待打版。

## Criteria

- [x] `plugins/evo-adr` 改名 `plugins/evo-doc`;code-kit 与 cli-docs 目录消失,references 并入 doc-gov 后收敛 7 篇(base-diary 与 base-coe 新写,15 篇复杂面移除)
- [x] md-guard.py 与 mdrules.py 上移插件级 `scripts/`;hooks.json 与仓 settings.json 指新路径;skill 目录纯知识
- [x] init/check/scan 移 `.tools/`(路径锚点改);模板移 `.tools/templates/`;verification 移 `.tools/verification/`;commands/ 斜杠命令删除
- [x] 双市场清单与 evo-doc 双 manifest 同笔(name、homepage、单 skill 描述、codex interface),版本线不动
- [x] 守卫测试 PLUGIN_NAMES/SKILLS/工具断言/md-guard 路径同步;test_repo_md_clean 的 mdrules 路径同步;CI smoke 改 .tools 路径
- [x] AGENTS、根 README、docs 地图、gates、.tools/README 计数与路径刷齐「两插件三 skill」
- [x] ADR-0018 与两索引、CHANGELOG 第八十九批、ROADMAP;pytest 全绿加 md-ref-scan 三 skill 零断链
