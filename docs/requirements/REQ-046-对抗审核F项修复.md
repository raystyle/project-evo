---
id: REQ-046
title: skill 对抗审核 F 项修复(grok 审单)
status: implemented
priority: must
trace: tests/test_project_evo.py
---

# REQ-046:skill 对抗审核 F 项修复

## Scenario

总台派单(2026-10-15,批156):grok 对抗审出 F13/G7/CONFIRM7(审单 share/lan-win/6cf96633fd/evo-skill-adv-review-2026-10-15.md,对象 evo 0.15.5 对 prim v3.1.8)。skill 面修 F1-F13 加 G1/G2/G7;代码面 G3/G5/G4/G6 总台已修在 prim v3.1.9(0895c67),本端拉装后核对 skill 与新 --llms 零漂移。要害 = 取用行与正文还教引擎命令(批155 已修 F1/F3/F5 主体)、agents 二十动词不下放、触发词漏词误开、分工节未收一行、示例不可复制。

## Criteria

- [x] F1/F3/F5:取用行三 SKILL 原语形(批155 主体;F1 坑表按审单改法、F5 坑表错列去 s5 字样)
- [x] F2:tasks view 声称改「本机各仓直读,远机经 agents read」(动词表与 commands 差异表同步)
- [x] F4/F9:示例可复制化(shares 换手册两行加 view 加 get 键;五域 view 各留一条带参形)
- [x] F6:streams 旗标 | 形对齐 --llms,文法只留 resume 覆盖 from 一句,100 行默认只留坑表
- [x] F7:collab 取用行贴审单形;commands 标题六原语、tasks 行分实现与取用行、表头 v3.1.9
- [x] F8:agents 正文六主动词,工位与在场族(ws/shell/dev/split/tab/zoom/wt/trust/sync/reload/mode)下放 references/workspace.md 加索引行,示例每动词恰一次,活名 evo-claude,busy 与 reload 只留坑表
- [x] F10:ctx 示例换 --llms 四行可复制形,坑行改可判定,接着读改 --llms 指针(删 commands.md 两级跳)
- [x] F11:pipes 触发词删引擎名(tailcat/addr/open/close),取用行缺口挪文法
- [x] F12:六域触发词删引擎名与撞车裸词、补漏词;agents 去 AGENTS.md 路径词(G2)
- [x] F13:六域分工节收文法末一行;pipes 方向留文法一条加坑表一行
- [x] G7:插件 README 五原语、tasks 事件入流、tailcat 旧语清,codex interface 同步
- [x] 零漂移核对:六域动词表文法对 prim v3.1.9 --llms 逐面一致(G3 tasks 远机注、G5 七旗标、G4 -o 别名、G6 wt 窗格视图)
- [x] evo 独立升 0.15.7;四门禁全绿 + fleet 回执
