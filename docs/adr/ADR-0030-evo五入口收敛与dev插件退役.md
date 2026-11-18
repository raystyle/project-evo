---
id: ADR-0030
title: evo 五入口收敛与 dev 插件退役,hook_rules 知识树删,动词对齐 hc
status: accepted
date: 2026-11-18
---

# ADR-0030:evo 五入口收敛与 dev 插件退役

## Context

上游 prim 原语层继续收敛(herdr-ccoe ce5dd93,2026-11-18 用户裁定):六入口收敛五入口
shares/streams/ctxs/ports/pipes;agents/desks/machines 三域退役(消息与工位与机册归
hc 与 herdr-app 原生面);动词对齐 hc 形态:清单 view 改 ls、留痕 to 改 send、生命周期
open 改 start,旧名不留别名;pipes 语义澄清:send = 字节写,留痕知会道归 streams send。
连带裁定(总台令,批 180):本仓 dev 插件整目录退役(hst 已退役,dev 治理知识面无消费
道);本仓职责收缩为只维护 skill 面,不维护 prim(真源与维护在 herdr-ccoe 仓)。
用户续令(批 180 二段):hook_rules 知识树整删,只保留 evo 插件的原语命令 skill,
知识面并回各 SKILL.md 自含。本仓 evo 插件原七 skill(六原语加 research)面向
prim 命令面,必须随形。

## Decision

1. evo 收敛五 skill:shares/streams/ctxs 三壳按 prim v5 五面手册重写(manual.py 与
   金样为源,动词 ls/send),pipes/ports 两 skill 直入复活(批 179 曾随 carry 退役,
   上游 2026-11-18 五入口直入);agents/desks/machines/research 四 skill 目录删除,
   不留 deprecated 壳(上游为整域消亡,归 hc 与 herdr-app 原生面,无后继道可指)。
   版图:单插件五 skill。二段令:hook_rules 知识树(六枚 intents)整删,五 skill
   的知识面(动词表、判读坑、礼仪、示例)并回各 SKILL.md 自含,薄壳指针形态终结。
2. dev 插件整目录退役:skills/hook_rules/hooks/manifests/README/tools 随目录消亡
   (治理知识面属插件产品面,本仓自用治理在 AGENTS.md 与 docs/guides);门禁脚本
   五枚(md-guard、mdrules、term-lint、termrules、term-mine)迁仓根 `.tools/` 保
   门禁(check PE-11/PE-13、scan、pre-commit 三面同源不破;先例 = 第八十九批
   init/check/scan 移 .tools、ADR-0018 工具与 skill 解耦);lint-hook.py 无消费方
   (live hook 批 174 裁撤)随插件退役删。evo hooks 目录整删(批 178 后空装配,
   hst 已退役)。
3. 动词面与职责声明:五域动词以 prim 手册为真源(`--llms` 为权威出口,各 SKILL.md
   一行回链);本仓 README 与 AGENTS 载明职责声明:只维护 skill 面,不维护 prim。
4. 版本与分发:evo 0.23.0(破坏性:四 skill 退役与动词更名,消费方卸载重装);
   Codex 市场清单删 dev 条目。

## Consequences

- evo 消费方破坏性:调用名 evo:agents、evo:desks、evo:machines、evo:research 失效;
  旧动词 view/to/open 不再可用(上游旧名不留别名);更新走三步正序判例(批 176 续)
  加翻台重载(hc 原生面,agents reload 已无)。
- dev 插件消费方破坏性:卸载 dev@project-evo;md 禁字与术语表挡板脚本不再随插件
  分发,下游仓用门禁走本仓 `.tools/` 拷贝或自备。
- 消息与生命周期操作从 skill 面归 hc 与 herdr-app 原生面:投递走 hc send、读屏走
  hc read、起格走 hc run;需求再现属上游命运表翻案,不在本仓复活。
- 守卫同步:SKILLS 清单(evo 五)、正典原语集(五)、pre-commit 断链段、活面计数
  (单插件五 skill)、dev 与 hook_rules 退役防回潮守卫、SKILL.md 自含形(--llms
  权威行)断言。
- 实证准入(ADR-0010):本端 prim 先滚装五入口形(herdr-ccoe 源临时装验,五域
  --llms 与金样逐字一致;五域 ls 实跑;shares put 实弹往返成功);prim 分发由宿主
  工具链统一维护,skill 只认 PATH。
