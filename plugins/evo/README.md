# evo

> project-evo 市场 agent 操作面插件:五 skill 五入口(prim v5 五入口收敛批 180;动词对齐 hc = 清单 ls、留痕 send、生命周期 start)。客户端显示 `evo:<skill>`。

## skill 清单

| skill | 面 |
| --- | --- |
| shares | 文件域原语:ls/put/get/send,内容哈希键,拒投不丢件 |
| streams | 流域原语:增量消息(裸 ls 房间清单、room/dm、ls 读流、append、send),fleet 回执主频道 |
| ctxs | 对话历史域原语:agent 请求全链检索(ls 头行与单请求、search,引擎 ClickHouse gw_logs;与 hc read 分工 = 实时屏对历史档案) |
| ports | 端口映射域原语:ls/start/close/fwd/send,tailcat serve 面板端口与服务映射 |
| pipes | 实时字节域原语:ls/start/close/send,管道收发,stdin 字节直通(send = 字节写,留痕知会归 streams send) |

结构沿革:由旧多插件形态收敛重构而来(ADR-0025):herdr-orch、agent-s5、agent-rloop、agent-doctor 裁撤;agent-prim 拆原语 skill;doc-gov 与 doc-cli 及 lint 三 skill 归 dev 插件(批 175 前两者合一 dev-doc,ADR-0026);批 176 知识面翻 hook_rules 薄壳指针(ADR-0027,批 180 二段令知识树删、知识面并回 SKILL.md 自含);2026-11-09 注入面剔除(壳直读),批 178 distil 退役(ADR-0028);批 179 六入口对齐 prim v5.0.0,tasks/pipes/ports/mcps 四域退役(ADR-0029);批 180 五入口收敛:agents/desks/machines/research 四 skill 退役(消息与生命周期归 hc 与 herdr-app 原生面),pipes/ports 直入复活,动词对齐 hc,dev 插件整目录退役,hook_rules 知识树删除(ADR-0030)。旧名映射以 ADR-0025 为准。

## 前置

- skill 本体纯 Markdown,知识面自含于各 SKILL.md(批 180 二段令:hook_rules 知识树删除)
- 五入口实操需本机 PATH 上的 prim v5 或更高(五入口形;CLI 真源与维护在 herdr-ccoe 仓,本插件不涉及 prim 代码与封装;全平台分发由宿主工具链 omc 与 ark 统一维护)

## 安装

Claude Code:

```text
/plugin marketplace add raystyle/project-evo
/plugin install evo@project-evo
```

Codex:`codex plugin marketplace add raystyle/project-evo` 后 `codex plugin add evo@project-evo`

Grok:`grok plugin install evo@project-evo --trust`

Kimi:无市场,拷 `plugins/evo/skills/*` 至 `~/.kimi/skills`

## 翻台与清理(重载铁律)

- **旧进程 = 旧技能**:装/更新插件后必须翻台才生效,走 hc 原生面(`hc send <t> '/exit'` 后重进,或重启该格 agent;批 180 起 agents 域退役)
- 全端序:每端 `/plugin marketplace update project-evo` 再到 卸旧插件(dev 与 evo 的 agents/desks/machines/research 面)再到 装 evo 再到 全格翻台重载
- Kimi 端:清 `~/.kimi/skills` 旧目录后重拷,重启会话

当前发布:0.23.0。
