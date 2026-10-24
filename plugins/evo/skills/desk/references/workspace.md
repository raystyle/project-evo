# 工位族动词细则

> desk 正文动词表收主行;本篇收动词旗标与示例。mode 与 reload 在 agents 面;旗标全集以 `desk --llms` 为准。

| 动词 | 文法 | 何时用 |
| --- | --- | --- |
| ws | `ws <label> [--cwd DIR] [--machine 机]` | 要开工作台;裸 `ws` 列本机台面;`ws close <台> [机]` 收台 |
| shell | `shell <机> <仓路径>` | 要在某机某仓开台 shell 格 |
| dev | `dev <机> <仓路径> [--kind 类]` | 要开台并起 agent |
| split | `split <id> [--direction right\|down]` | 要在格旁分裂新格 |
| tab | `tab list [机]` / `tab create <机>` / `tab close <机:tab>` | 要管理 tab |
| zoom | `zoom <id>` | 要聚焦某格 |
| wt | `wt [机\|wsl] [--title 名]` | win 专属:本窗开 tab 显该机窗格视图 |
| trust | `trust` | 要放行信任屏(全机扫屏按键) |
| sync | `sync [机]` | 要补注册机册 |

## 示例

```bash
desk shell lan-ubuntu ~/repos/ai-ccoe
desk dev lan-ubuntu ~/repos/pi-rs --kind grok
desk split local:w13:p1 --direction down
desk zoom local:w13:p1
desk wt wsl --title 台面
desk trust
desk sync
```
