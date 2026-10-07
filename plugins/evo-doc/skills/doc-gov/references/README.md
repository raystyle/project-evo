# doc-gov 参考索引

> 渐进索引:一、快速路由;二、全量清单(7 篇);三、检索方法。目录与文件名以 rg 检索为先,进文件先抽 h2 目录再定点读。

## 一、快速路由

| 意图 | 首选参考 |
| --- | --- |
| 立决策 / 写 ADR / 立需求 / 写 REQ | base-adr.md、base-req.md |
| 写项目日记 / 过程留痕与升格 | base-diary.md |
| 建 COE 知识库 / 三层与双链图 | base-coe.md |
| CLI agent 面(手册、协议、帮助面、自省、裸调用) | agent-face.md、templates.md |
| agent CLI 发现通道与脚本 workspace | tool-cli-agents.md |

## 二、全量清单(7 篇)

| 文件 | 主题 |
| --- | --- |
| base-adr.md | ADR 架构决策记录(状态机、supersede 流、索引) |
| base-req.md | REQ 需求登记(状态机、trace 回填、索引) |
| base-diary.md | 项目日记(一天一篇活轨迹、裁定与坑留痕、择要升格) |
| base-coe.md | COE 形态(三层聚合、双向链接图、指挥总纲路由、建仓五步) |
| agent-face.md | Agent 友好 CLI 五件(--llms 手册面、类型化 CTA 协议、默认帮助面、自省、裸调用面) |
| tool-cli-agents.md | agent-native CLI 设计(发现通道选型、token 经济学、任务脚本 workspace) |
| templates.md | CLI 双面可拷模板(README 骨架、--llms 手册、信封 schema、TS 与 Rust 实现、自省守卫清单) |

## 三、检索方法

```powershell
rg --files references | rg 关键词          # 文件名直达
rg -n "关键词" references\README.md        # 索引定位
rg -n "关键词" references\                 # 全文直搜
reader query references\base-coe.md ".h2"  # 结构化提取
```

多仓飞轮协作(herdr 派单、回执、断言、吸收)见 `evo-herdr:herdr-flywheel`(协议唯一权威源)。
