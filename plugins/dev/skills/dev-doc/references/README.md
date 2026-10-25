# dev-doc 参考索引

> 渐进索引:一、快速路由;二、全量清单(10 篇);三、检索方法。目录与文件名以 rg 检索为先,进文件先抽 h2 目录再定点读。

## 一、快速路由

| 意图 | 首选参考 |
| --- | --- |
| 立决策 / 写 ADR / 立需求 / 写 REQ | base-adr.md、base-req.md |
| 代码 doc 注释 / 契约注释 / 文档即代码 / 投影守卫 | base-code-doc.md |
| 立研究档案 / S 编号一题一篇与对照分流 | base-research.md |
| 建项目工具链 / uv 与 PEP 723、门禁与发布 | tool-project-kit.md |
| md 五面静检 / 禁字 / 断链 / 行量 | md-faces.md |
| 约束术语表 / term-lint / 挖词 / PENDING 收紧 | term-rules.md |
| 新仓选类型 / 四类型模板卡 | ls-types.md |
| 结构 lint 规则件 / toml 表式 | ls-rules.md |
| 结构 lint 触发场景 | ls-evals.md |

## 二、全量清单(10 篇)

| 文件 | 主题 |
| --- | --- |
| base-adr.md | ADR 架构决策记录(状态机、supersede 流、索引) |
| base-req.md | REQ 需求登记(状态机、trace 回填、索引) |
| base-code-doc.md | 代码 doc 注释(契约注释、what 与 why 分层)与文档即代码(单一权威源、投影再生成) |
| base-research.md | 研究档案(S 编号一题一篇、信源与六态结论、对照分流、择要升格) |
| tool-project-kit.md | 项目工具链范式(工具归档、PEP 723 零依赖 uv 直跑、门禁三态与提交挡板、发布三段式) |
| md-faces.md | md 五面静检(skill/agents/claude markdown、禁字、断链、行量与门禁接线) |
| term-rules.md | 约束术语表 lint(两层政策、term-lint 用法、豁免通道、挖词程序;词表权威在 termrules.py) |
| ls-types.md | 四类型结构模板卡(TS CLI、知识三层、worker 服务、Python 工具) |
| ls-rules.md | 结构 lint 声明式规则件(toml 六节表式、生成物与排除) |
| ls-evals.md | 结构 lint 触发场景(何时结构面、何时语言面) |

## 三、检索方法

```bash
rg --files references | rg 关键词          # 文件名直达
rg -n "关键词" references/README.md        # 索引定位
rg -n "关键词" references/                 # 全文直搜
```

跨插件分流:三层聚合与技能自进化(轨迹总结、模式页、标准 skill)见 `evo:distil`;Agent 原生友好开发(--llms 手册、CTA 协议、自省)见同插件 `dev-cli`;多仓协作与派单回执见 `evo:agents` 与 `evo:streams`(五原语操作面)。
