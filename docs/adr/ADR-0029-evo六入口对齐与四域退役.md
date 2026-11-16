---
id: ADR-0029
title: evo 六入口对齐与四域退役,tasks/pipes/ports/mcps 出面
status: accepted
date: 2026-11-16
---

# ADR-0029:evo 六入口对齐与四域退役

## Context

上游 prim 原语层放开重构(herdr-ccoe ADR-0003,2026-11-13 用户裁定:消费方可断,
按优化空间重塑;evo skills 随新面重写),v5.0.0 六入口定形(4e5006c,2026-11-16):
agents/desks/machines/streams/shares/ctxs。连带裁定:carry 三合一入口弃(先立后撤),
pipes(实时字节)与 ports(端口映射)随退;tasks 域退役(streams 收纯增量消息,
钉任务走 agents to);mcps 整域退役(MCP 边缘化,连通用 MCP 客户端腿也不留);
动词标准全域统一(view = 清单与读、to = 留痕知会、start/close = 生命周期),
machines list/runtimes 别名退役、ctxs show 并入 view <id>、streams rooms 并入裸 view。
本仓 evo 插件原十一 skill(十原语加 research)面向 prim 命令面,必须随形。

## Decision

1. 六 skill 按 prim v5.0.0 六面手册重写(壳 description 与 hook_rules 知识件同源
   manual.py 与金样):agents 收十五动词(view/workbenches/read/to/wait/inbox/mode/
   start/close/reload/trust/yolo/run/shell/dev/keys);desks 收三动词兜底
   (view/start/close,树形拓扑归 herdr-app mod GUI);machines 收
   view/add/reconnect/run/close/runtime;shares 复活(view/put/get/to);streams 收
   增量消息(裸 view = 房间清单、room、dm、view 读流、append、to);ctxs 收
   view/search(view <id> 并法,--around/--window 保留)。
2. 四域退役:tasks、pipes、ports、mcps 四 skill 目录与同名 intents 知识件删除,
   不留 deprecated 壳(上游为整域消亡,无后继道可指;退役 stub 可见化是 prim CLI
   面的事,skill 面不仿);research 非命令面,保留。版图:两插件九 skill
   (dev 二加 evo 七 = 六原语加 research)。
3. 动词标准与退役可见化口径入知识件:各域 intents 载明已退役动词与指新道
   (list、runtimes、status、rooms、show、split、tab、zoom、wt、desk 别名),
   仿 kubectl 废弃可见化纪律;共享面单一权威源不变(agents 契约件承载文法、
   信封、门控、命名标准)。
4. 版本与分发:evo 0.22.0(破坏性:四 skill 消费方卸载重装);dev 0.19.1
   (顺手修:市场清单描述残留「双 bun 注入加载器」与「按意图与路径注入」,
   批 178 注入面剔除后已失实)。

## Consequences

- evo 消费方破坏性:调用名 evo:tasks、evo:pipes、evo:ports、evo:mcps 失效;
  老版本技能文教旧动词,更新前旧屏照旧可用,更新走三步正序判例(批 176 续)
  加全格 agents reload。
- 实时字节与端口映射能力在 skill 面无后继(上游域消亡):还在长的日志走
  streams --file 切片,写完的文件走 shares;钉跨回合目标改 agents to 投递
  加 streams 留痕。需求再现属上游命运表翻案,不在本仓复活。
- 守卫同步:SKILLS 清单(evo 七)、HOOK_RULES 计数(evo intents 21 减 17)、
  正典原语集(六)、pre-commit 断链段、活面计数(九 skill)。
- 上游缺陷记档(已闭环):prim/src/prim/ctx.py 并法行漏传 g,ctxs view <request_id>
  实弹 TypeError(批 179 滚装实弹揪出,回执 fleet);上游已修(herdr-ccoe 6ca7baa
  补参),本端重装后实弹复验详情道全链返回与头行面、退役 stub 面均正常,
  六入口 skills 验收通过(总台 2026-11-16)。
- 六入口动词面以本机 PATH 上 prim --llms 为准(滚装 v5.0.0 实证);
  prim 分发由宿主工具链统一维护,skill 只认 PATH。
