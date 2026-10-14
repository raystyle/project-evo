---
id: REQ-040
title: 六原语收编:ctx 对话历史域 skill
status: implemented
priority: must
trace: tests/test_project_evo.py
---

# REQ-040:六原语收编（ctx 对话历史域）

## Scenario

总台派单(2026-10-14,prim v3.1.0,GitHub main e98e4af 起实装):第六原语 ctx = agent 对话历史检索(引擎 ClickHouse gw_logs,lan-linux2 gwlogs 实例,ssh 道进容器内 client 免证书面);动词 view/show/search,窗口 head 365 天正文 180 天;与 agents read 分工 = read 实时屏,ctx 历史档案;保留动词表增 show/search;CONTRACT 真源已更新(二节动词表与七节批次记)。任务 = skill 面收编、本端滚装、实弹验证、回执贴 fleet。

## Criteria

- [x] 新 skill evo:ctx(单文件域面,链 ../agents/ 共享面):三动词表、窗口与分工、坑(ssh 凭据按端、request_id 取自 view、采集端未起检索面空属正常)
- [x] agents 枢纽升六原语:定位与 description、路由行(查历史对话走 ctx)、保留动词表增 show/search、read 分工注;commands.md 六域速查加 ctx 行与共享面注
- [x] 守卫与路由面随形:SKILLS(evo 七 skill)、SINGLE_FILE 增 ctx、pre-commit(十目标)、双 manifest 与市场清单(evo 0.15.0,十 skill 形)、AGENTS 与根 README 与 docs 地图与 evo README
- [x] 本端滚装 prim v3.1.0(本仓道重装,六命令入口含 ctx,ctx --llms 实测);实弹 = ctx view 与 ctx search 各一发,本机 ssh 道无 lan-linux2 凭据(engine_fail 退 1,错误原文 stderr,退出码实测)如实报件,链路全通待总台侧或配钥后验
