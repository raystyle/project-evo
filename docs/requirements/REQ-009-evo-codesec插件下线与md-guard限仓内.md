---
id: REQ-009
title: evo-codesec 插件下线与 md-guard 挡板限仓内 md
status: implemented
priority: must
trace: tests/test_project_evo.py
---

# REQ-009:evo-codesec 插件下线与 md-guard 挡板限仓内 md

## Scenario

用户立单(2026-10-07,同日两令):移除 evo-codesec 的 `secret-scan` skill,再下线 evo-codesec 整插件(`security-audit` 一并移除),三插件七 skill 收敛两插件五 skill;md 插件与扫描只针对(仓内)md 文档。核实 md 规则五面(hook、--staged、scan、PE-11、md-ref-scan)已全部只认 .md,唯一改动面为挡板辖域限仓内。

## Criteria

- [x] `plugins/evo-codesec/` 整插件移除(双 skill、双 manifest、README、secret-scan-cli 命令);tests/test_secret_scan.py 退役
- [x] 双市场清单去 evo-codesec 条目;两插件 manifest 版本线不动
- [x] 守卫 PLUGIN_NAMES/SKILLS 与断言同步;pre-commit 断链段余五;gates 与 AGENTS 豁免面去 secret-scan 夹具
- [x] doc-gov 与 code-kit 互引改指 code-kit scan,不留死链
- [x] md-guard hook 带 cwd 辖域限定(仓外 md 放行),无 cwd 载荷宽容不回退,新增用例
- [x] ADR-0017 与两索引、CHANGELOG 第八十八批、ROADMAP、计数刷齐
- [x] pytest 全绿加 md-ref-scan 五 skill 零断链
