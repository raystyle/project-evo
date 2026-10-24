---
id: REQ-061
title: agents 与 streams skill 3.9.1 判例蒸馏(wait 事件道与 canonical 寻址)
status: implemented
priority: must
trace: tests/test_project_evo.py
---

# REQ-061:agents 与 streams skill 3.9.1 判例蒸馏

## Scenario

总台令(2026-10-24,用户令蒸馏单):prim 3.9.1 落地(agents 寻址 canonical 化:dm pair 与信封 to= 统一 机:别名 形、engine_fail 定向诊断、流发现去截断;3.9.0 已落 to 镜像 dm 流与 wait/inbox 事件道,f848d8c 入动词行),evo:agents 与 evo:streams 两 skill 需按 3.9.1 判例入档。蒸馏真源要求 ctxs 实查;实测 ctxs 正文窗仅覆盖当日(view 10000 行不出当日,10-23 判例不可达,窗口缺口另报),故真源改为本机实弹探针(全部真跑)加总台侧判例对照:错名定向清单(`lan-mac:lan-mac-claude-1` stderr 直出 `ray-claude-1`)、dm 劈叉归一、wait rc 与 json 形、无名格事件道退化与正名键迁移、流列表 73 条全量无截断、rooms 不崩(10-21 A1/A2 已修实证)。

点名义务(现行 skill 盖不住):wait/inbox 行无 rc 与 json 形;engine_fail 定向清单判读无载面(坑表只有「先看退出码再看 status」);dm canonical 流名与劈叉判例无载面;无名格事件道退化与正名致旧键消息孤儿无载面。

## Criteria

- [x] agents SKILL.md:wait/inbox 行按实弹精化(到件 rc=0 超时 rc=1、status=timeout 带监视流键、inbox 幂等);文法节补事件道与 engine_fail 定向清单句;坑表增四行(定向清单照单改投、dm canonical 两写法劈叉、无名格事件道退化、sleep 盲等对 wait);示例 wait 行改 canonical 寻址形
- [x] streams SKILL.md:dm 行 canonical 流名形;文法节 dm canonical 与流列表无截断句;坑表增劈叉判例行
- [x] references 同步:addressing.md 解析算法第五条(机在册名错定向清单)与坑簿两行;collab.md 私信行 canonical 加「等回信」速判;deliver-gate.md engine_fail 行定向清单与收件面事件道句
- [x] 实证准入:全部新句本机实跑(prim v3.9.1:错名投递、wait 超时 rc=1 与 --json 形、inbox 两态、dm 流名清单、流列表 73 条、rooms 净退)
- [x] 变更完整性:docs 地图 agents 行与 AGENTS 描述行补 wait 事件道、CHANGELOG 批 172、evo 升 0.17.2(双 manifest加市场清单三处同步)
- [x] ctxs 窗口缺口上报:正文窗宣称 180 天,实测 view 10000 行不出当日,10-21 至 10-23 判例不可达,随回执报 ctxs 域
- [x] 批 172 续(总台复后认账修正):ctxs 数据面无缺(head 27k 行全在),「不可达」为慢道翻页超时假象;prim 3.9.2 增 --since/--before 时间旗标,--since 重挖 10-21 至 23 秒圈;增量判例一条入档(engine_fail 双败 fleet 兜底回执,collab.md 回执节);--around 聚焦不生效(show 全量转储)续报 ctxs 域;evo 0.17.3
