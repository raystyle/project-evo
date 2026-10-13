---
id: REQ-027
title: agent-prim 升格 prim v3 契约对齐(to 统一投递与 id 三产生式与 status 四态)
status: implemented
priority: must
trace: tests/test_project_evo.py
---

# REQ-027:agent-prim 升格 prim v3 契约对齐

## Scenario

总台令(2026-10-13,发版部署批):ai-ccoe 契约演进至五节加五a/b/c/d(v3.0 蓝图:投递动词统一 to、id 三产生式、机不占位置参数、全局七旗标、status 四态信封、agents 工作台面),本机 prim v3(python 形 3.0.0a1)已装。本仓 agent-prim skill(REQ-025,对齐 v2.3)随批升格:按 doc-cli 纪律重铸意图路由与投递语义面,发版部署到各端。总台令原名 prim-ops,按本仓命名律落位既有 agent-prim(evo-agent 插件 agent- 前缀族),不另铸新 skill 免双份并行维护。

## Criteria

- [x] SKILL.md 重铸:五域路由表、文法与全局旗标(to 统一)、id 三产生式与例、投递语义(status 四态信封)、隐式路由(各端一致,local 与 --machine 零感知)、常见坑(裸格须 local: 前缀、streams 尾读 100 行限读、门控拒投走 streams append 记流)
- [x] references 四篇同步:commands.md(v3 动词面与输出契约与 3.0.0a1 实装差异表)、addressing.md(id 三产生式与隐式路由)、deliver-gate.md(status 四态与代记两形)、collab.md(hst task 正名与 cursor 崩坑);索引随改
- [x] 实证准入(ADR-0010):SKILL 与 references 所写命令形经本机实测(view、machines、read、shares get、to 拒投路径、streams 代记落点)或包源直读标注 [实证]
- [x] 版图与版本线:五插件 0.10.1 进 0.11.0(双 manifest、市场清单、五插件 README 发行行);顺手修批 133 遗漏的市场清单描述(十 skill 进十一,evo-lint 两进三、evo-agent 三进四);根 README 与 docs 地图 agent-prim 行随改
- [x] 四门禁全绿 + 回执走 streams append fleet;部署道建议候总台核
