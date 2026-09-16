# code-kit 参考知识体系(渐进索引)

> `references/` 是**分类 + 扁平**目录:文件名 = 类别前缀 + 主题词(base/flow/env/tool),目录与命名以 rg 检索为先,`rg --files references | rg <主题词>` 直接命中;每篇一个主题、自包含完整参考。本 README 是唯一路由入口。合同/ADR/REQ/投影/六态等体系知识在同插件 doc-gov。

## 一、快速路由(高频场景 到 文档)

| 我要… | 看哪篇 |
| --- | --- |
| 在新项目落地骨架 / 存量迁移 | [base-init.md](base-init.md) |
| 写测试 / 定测试分层与门禁 | [flow-testing.md](flow-testing.md) |
| 定平台矩阵 / CI 三系统 / 换机接管 | [env-platform.md](env-platform.md) |
| 建项目脚本工具(.tools / uv / PEP 723) | [tool-project.md](tool-project.md) |
| 给 CLI 增加 agent 用户面 | [tool-cli-agents.md](tool-cli-agents.md) |
| 建 Rust 仓 / aidoc / doctest | [tool-rust.md](tool-rust.md) |
| 建 TypeScript/Node 仓 / TSDoc / API Extractor | [tool-typescript.md](tool-typescript.md) |
| 建 Python 仓 / docstring / MkDocs 投影 | [tool-python.md](tool-python.md) |

## 二、场景索引(按工作维度)

### 骨架与流程

- [base-init.md](base-init.md) - 初始化五步、关键问题清单、裁剪原则、验收清单、存量迁移路径与旧体系映射
- [flow-testing.md](flow-testing.md) - 测试流程规范:双轴分层(地基层/意图层)、五层正名(单元/集成/冒烟/回归/验收)、断言纪律、跨栈载体速查、门禁时机谱、特色机制(黄金文件/快照/防漂移/DryRun/假绿防线)

### 平台与环境

- [env-platform.md](env-platform.md) - 平台适配:shell 分平台、编码行尾、文档路径两制、脚本载体、CI 三系统门禁、接管验收清单

### 工具

- [tool-project.md](tool-project.md) - 项目工具:`.tools/` uv 运行时 Python 脚本约定(PEP 723)、归档规则、沉淀铁律、外部工具路由
- [tool-rust.md](tool-rust.md) - Rust 工程合同:workspace 与工具链、`///` 契约注释(missing_docs deny)、门禁命令、aidoc 投影、daemon 与 E2E 工程要点
- [tool-cli-agents.md](tool-cli-agents.md) - agent-native CLI 设计:双用户公理与 token 经济学、发现双通道(--llms 默认推荐,mcp add 需编排时)、市场分发协议(双客户端 add 形态、git 双协议、简写默认协议相反、钉版、source 七型)、TOON 紧凑输出与 CTA、四面 schema、管道代码逃生舱(零 import 集成运行时)、脚本 workspace 集中归档(同 exec 运行时、apps 即命令、domain-skills 知识层)、定义一次多面暴露(Agent Plugins 三层)、行为 oracle 对齐、落地清单
- [tool-typescript.md](tool-typescript.md) - TypeScript/Node 工程合同:Node >=22 ESM、tsc 严选项、runtime 依赖白名单、node:test(引号 glob)、checkJs 管 .mjs、npm pack 验收(禁 link)、空串不走 ??、fnm 下 spawn npm-cli.js;文档即代码面(TSDoc、API Extractor、TypeDoc、test-d)
- [tool-python.md](tool-python.md) - Python 工程合同:uv 运行时与 PEP 723 零依赖、docstring 契约(做什么+何时用+边界)、MkDocs/Griffe 投影、pytest 与 doctest 门禁

另有姊妹件:`../verification/command-test-cases.md`(骨架规范检查命令)。

## 三、全量清单(8 篇)

| 文件 | 主题 |
| --- | --- |
| base-init.md | 初始化流程与存量迁移 |
| flow-testing.md | 测试流程规范(双轴分层与五层正名) |
| env-platform.md | 三平台适配 |
| tool-project.md | 项目工具约定与路由 |
| tool-rust.md | Rust 工程合同(workspace、契约注释、aidoc) |
| tool-cli-agents.md | agent-native CLI 设计(双用户契约与自由代码面) |
| tool-typescript.md | TypeScript/Node 工程合同(tsc、node:test、TSDoc、API Extractor) |
| tool-python.md | Python 工程合同(uv、PEP 723、docstring、MkDocs 投影) |

## 检索方法

目录与文件名为 rg 检索设计(前缀=类别词、主干=主题词);文档结构为 mq 提取设计(h2=节、code=命令、表格=键值)。

```powershell
rg --files . | rg 关键词                    # 1 文件名定位(类别词/主题词)
rg -n "关键词" README.md                    # 2 索引导航
rg -n "关键词" . --glob "!README.md"        # 3 全文搜
reader query <文件> ".h2"                    # 4 结构化提取节目录
```
