# doc-gov 参考索引

> 渐进索引:一、快速路由;二、全量清单(5 篇);三、检索方法。目录与文件名以 rg 检索为先,进文件先抽 h2 目录再定点读。

## 一、快速路由

| 意图 | 首选参考 |
| --- | --- |
| 立决策 / 写 ADR / 立需求 / 写 REQ | base-adr.md、base-req.md |
| 代码 doc 注释 / 契约注释 / 文档即代码 / 投影守卫 | base-code-doc.md |
| 立研究档案 / S 编号一题一篇与对照分流 | base-research.md |
| 建项目工具链 / uv 与 PEP 723、门禁与发布 | tool-project-kit.md |

## 二、全量清单(5 篇)

| 文件 | 主题 |
| --- | --- |
| base-adr.md | ADR 架构决策记录(状态机、supersede 流、索引) |
| base-req.md | REQ 需求登记(状态机、trace 回填、索引) |
| base-code-doc.md | 代码 doc 注释(契约注释、what 与 why 分层)与文档即代码(单一权威源、投影再生成) |
| base-research.md | 研究档案(S 编号一题一篇、信源与六态结论、对照分流、择要升格) |
| tool-project-kit.md | 项目工具链范式(工具归档、PEP 723 零依赖 uv 直跑、门禁三态与提交挡板、发布三段式) |

## 三、检索方法

```powershell
rg --files references | rg 关键词          # 文件名直达
rg -n "关键词" references/README.md        # 索引定位
rg -n "关键词" references/                 # 全文直搜
```

跨插件分流:三层聚合与技能自进化(轨迹总结、模式页、标准 skill)见 `evo-skills:distil-skill`;Agent 原生友好开发(--llms 手册、CTA 协议、自省)见同插件 `native-design`;多仓飞轮协作见 `evo-herdr:herdr-flywheel`。
