# evo

> project-evo 市场 agent 操作面插件:七 skill(六原语加 distil)。客户端显示 `evo:<skill>`。

## skill 清单

| skill | 面 |
| --- | --- |
| agents | 五原语消息域原语与共享面枢纽(to 投递、id 三产生式、命名标准 工作台-类型-编号、门控 v2 尾窗、信封 v2、status 四态、read 收件、mode、工位管理 start/ws/shell/dev/split/tab/zoom) |
| shares | 文件域原语:S3 形中转看板(put/get/to,内容哈希键) |
| streams | 流域原语:S2 形持久流(append/view/to,流即房间,fleet 回执主频道) |
| tasks | 持久任务域原语:hst task 全局遥控(set/to,事件入流,远机零 ssh) |
| pipes | 实时字节域原语:tailcat 管道(open/close/to,本机收对方发) |
| ctx | 对话历史域原语:agent 请求全链检索(view/show/search,引擎 ClickHouse gw_logs;与 agents read 分工 = 实时屏对历史档案) |
| distil | 技能自进化:三层聚合(sources/knowledge/operations)、一案提案、合取闸门、双端分发 |

结构沿革:由旧多插件形态收敛重构而来(ADR-0025):herdr-orch、agent-s5、agent-rloop、agent-doctor 裁撤;agent-prim 拆五原语 skill,共享面在 agents;distil-skill 改名 distil;doc-gov 与 doc-cli(改名 dev-cli)及 lint 三 skill 归 dev 插件。旧名映射以 ADR-0025 为准。

## 前置

- skill 本体纯 Markdown
- 五原语实操需本机 PATH 上的 prim(uv 工具 `prim`,全平台分发由宿主工具链 omc 与 ark 统一维护)

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

当前发布:0.15.5(独立 semver,dev 独立号)。
