# evo

> project-evo 市场 agent 操作面插件:七 skill(六原语加 research;prim v5.0.0 六入口对齐,批 179)。客户端显示 `evo:<skill>`。

## skill 清单

| skill | 面 |
| --- | --- |
| agents | 消息域原语与六入口共享面枢纽(to 投递、wait 事件道、inbox 收件、read 读屏、start/close/reload 生命周期、mode 在场、trust/yolo、run/keys、shell/dev 开台、workbenches 清点) |
| desks | 工位拓扑兜底原语:view 工位表、start 起格、close 优雅退;树形拓扑归 mod GUI |
| machines | 机册域原语:册表与注册(view/add/reconnect)、窗格直透(run/close)、runtime 环境面(骑 ark) |
| streams | 流域原语:增量消息(裸 view 房间清单、room/dm、view 读流、append、to),fleet 回执主频道 |
| shares | 文件域原语:put/get/to,内容哈希键,拒投不丢件 |
| ctxs | 对话历史域原语:agent 请求全链检索(view 头行与单请求、search,引擎 ClickHouse gw_logs;与 agents read 分工 = 实时屏对历史档案) |
| research | 检索域知识面:按研究目标路由通道(gh 搜 GitHub、browse 搜 Bing 与 Scholar、rn 编排与油猴探针;产出交棒 dev-doc 研究档案) |

结构沿革:由旧多插件形态收敛重构而来(ADR-0025):herdr-orch、agent-s5、agent-rloop、agent-doctor 裁撤;agent-prim 拆原语 skill,共享面在 agents;distil-skill 改名 distil;doc-gov 与 doc-cli(改名 dev-cli)及 lint 三 skill 归 dev 插件(批 175 前两者合一 dev-doc,ADR-0026);批 176 知识面翻 hook_rules 薄壳指针(ADR-0027);2026-11-09 注入面剔除(壳直读),批 178 distil 退役(ADR-0028);批 179 六入口对齐 prim v5.0.0,tasks/pipes/ports/mcps 四域退役(ADR-0029)。旧名映射以 ADR-0025 为准。

## 前置

- skill 本体纯 Markdown
- 六原语实操需本机 PATH 上的 prim v5.0.0 或更高(uv 工具 `prim`,全平台分发由宿主工具链 omc 与 ark 统一维护;v5 为六入口形,旧版 prim 无 shares 直入面)

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

- **旧进程 = 旧技能**:装/更新插件后必须翻台才生效,恒 `agents reload <id>`(同格同 session 重进)
- 全端序:每端 `/plugin marketplace update project-evo` 再到 卸旧插件(evo-doc、evo-herdr、evo-distil、evo-lint、evo-agent 五件)再到 装 dev 与 evo 再到 全格 `agents reload`
- Kimi 端:清 `~/.kimi/skills` 旧目录后重拷,重启会话

当前发布:0.22.0(独立 semver,dev 独立号)。
