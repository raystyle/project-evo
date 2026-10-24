# 2026-10-24 agents 与 streams 3.9.1 判例蒸馏

> 当日用户令(总台 lan-win:lan-win-claude-1 蒸馏单):prim 3.9.1 刚落(寻址 canonical 化、engine_fail 定向诊断、流发现去截断),ctxs 实查挖判例蒸馏入 evo:agents 与 evo:streams。另:前日事件驱动改造设计+实现单(10-23)总台侧自做,本台未开工即撤,无产出。闭环概览:ctxs 实查窗口缺口实证(正文窗宣称 180 天实测不出当日),真源改本机实弹探针七发七中;两 SKILL 与三 references 判例入档;evo 0.17.2,REQ-061,批 172 提交推送。

## 裁定

1. ctxs 窗口缺口定性:gwlog 正文窗宣称 180 天,view 10000 行不出当日(search 深页 3000 同),10-21 至 10-23 判例不可达;本批真源改实弹探针,缺口随回执报 ctxs 域(采集入库滞后或裁剪待域方裁定)。
2. 判例入档口径:skill 面只收可执行判读(rc、json 形、canonical 形、照单改投),域叙述留 references;prim 版本号入档钉 v3.9.1。
3. dm 劈叉治理边界:canonical 归一只管新写,存量旧形流(dm/lan-pve/local:w1:p1 等 34 条)不迁移,按名 view 显式读;记入 streams 坑表。

## 坑

1. 无名格第二轮:wY 又无名(10-21 正名后 10-24 复丢),且 inbox 直接以旧键(机:格)出蒸馏单全文、正名后归零,事件道键随名迁移,旧键消息孤儿;开机先正名,旧 dm 显式 view。已入两 skill 坑表。
2. ctxs 自噪:search 首搜命中的全是本会话刚装载的 skill 文本与派单原文回声(当日活窗),历史判例要靠专名加日期滤;本批实证专名加深页也翻不过当日,判窗口缺口。
3. 深页翻页无时间旗标:ctxs view/search 无 --since/--before,海量日(舰队全天并发)里 limit 翻页翻不出当日圈;记 ctxs 域改进候选(随缺口一并上报)。
4. 仓被外来批推进(f848d8c wait/inbox 动词行)未同步版本账:evo 版本仍 0.17.1;本批补齐账目并续改(判据:manifest 与 CHANGELOG 均无该笔对应条目)。

## 门禁退出码

- `uv run pytest`:34 passed,exit 0
- `uv run .tools/check.py .`:PASS 12 / FAIL 0 / SKIP 0,exit 0
- `PEVO_SCAN_ALLOW="tests/.*;docs/research/S006.*" uv run .tools/scan.py . --no-history`:共 0 项发现,exit 0
- `uv run .tools/md-ref-scan.py plugins/<插件>/skills/<skill>` 十四面:断链 0,exit 0

## 终态

- evo 插件 0.17.1 至 0.17.2(双 manifest加市场清单三处同步);批 172 提交推送(REQ-061 implemented)
- 实弹判例七发七中(prim v3.9.1):错名定向清单、wait rc=1 加 status=timeout、inbox 两态、dm canonical 键、流列表 73 条无截断、rooms 净退、无名格退化
- 上报件:ctxs 正文窗缺口加时间旗标缺(随批回执报 ctxs 域);prim 侧无待办(A1/A2 已修实证入档)
