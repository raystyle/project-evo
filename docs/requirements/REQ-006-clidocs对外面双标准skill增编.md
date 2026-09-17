---
id: REQ-006
title: cli-docs 对外面双标准 skill 增编
status: implemented
priority: must
trace: tests/test_project_evo.py
---

# REQ-006:cli-docs 对外面双标准 skill 增编

## Scenario

总台立单(2026-09-17):CLI 项目需要仓无关双标准:甲面 README 标准(四标杆研究定稿,人类阅读优先)与乙面 agent 友好三件(--llms 手册、JSON 协议、自省)。归口裁定新立 skill(照 build-release 形),与 doc-gov、code-kit 的 tool-cli-agents 分工互引,私有名零出现。

## Criteria

- [x] skill 落位 `plugins/evo-adr/skills/cli-docs/`(SKILL.md 加 references 四篇含索引),frontmatter name 与目录一致,description 兼做什么与何时用并含触发词
- [x] 甲面 readme-standard:四标杆(ripgrep、fzf、bat、fd)README 实读研究,共性表、四节主骨架定稿(项目介绍、部署、配置、使用加可选尾节)、写法纪律与反面清单;README 骨架模板可拷改
- [x] 乙面 agent-face 四件:--llms 手册面(裸 markdown 至多 120 行加 --llms --json 机器形加 --llms-full 可选,活命令树渲染禁手维护);输出协议(必选旗标七件 --filter-output/--format/--full-output/--help/-h/--llms/--json/--schema 加可选扩展件显式裁剪,信封 ok/data|error/meta,类型化 CTA 进 meta 折算与 Suggested commands 渲染,jsonl 无信封,错误 stderr 单行 JSON,退出码 0/1/2,字段序稳定);默认帮助面(节序定稿、对齐规则、描述 schema 同源、组与叶双形);自省(活命令树唯一真源,三面同源,漂移守卫锁全旗标覆盖);mcp 与 http api 可选附录
- [x] 模板五节可拷改(README 骨架、手册骨架、信封与旗标、双语言实现模板各带帮助输出示例、自省核对清单),零私有名
- [x] 同步面全改:ADR-0014 与索引、双 manifest 与市场条目描述、守卫 SKILLS 十一 skill、pre-commit 第十一段、AGENTS 与根 README 与 docs 地图与 gates 计数、evo-adr README 五 skill 化、tool-cli-agents 互引、CHANGELOG、ROADMAP、diary;pytest 全绿加 md-ref-scan 十一 skill 零断链
