# doc-gov 参考知识体系(渐进索引)

> `references/` 是**分类 + 扁平**目录:文件名 = 类别前缀 + 主题词(base/flow/exp),目录与命名以 rg 检索为先,`rg --files references | rg <主题词>` 直接命中;每篇一个主题、自包含完整参考。本 README 是唯一路由入口,三层渐进:快速路由 到 场景索引 到 全量清单;新参考文件建成后登记进第三层。骨架安装、门禁与工程合同类参考(base-init、flow-testing、env-platform、tool-*)在同插件 code-kit。

## 一、快速路由(高频场景 到 文档)

| 我要… | 看哪篇 |
| --- | --- |
| 写或改 AGENTS 五节合同 | [base-agents-contract.md](base-agents-contract.md) |
| 立一条 ADR / 替代旧决策 | [base-adr.md](base-adr.md) |
| 立需求 REQ / 回填 trace | [base-req.md](base-req.md) |
| 配 API 文档投影 / 公开面漂移门禁 | [base-projection.md](base-projection.md) |
| 写日记 / 研究档案 / SNNN 编号 / 沉淀升 ADR | [flow-archive.md](flow-archive.md) |
| 写任何文档前 | [base-writing-standards.md](base-writing-standards.md) |
| 发一个版本 | [flow-release.md](flow-release.md) |
| 落地前预警 / 踩坑对照 | [exp-pitfalls.md](exp-pitfalls.md) |

## 二、场景索引(按工作维度)

### 体系骨架与规范

- [base-agents-contract.md](base-agents-contract.md) - AGENTS 五节合同(Commands/Must/Must not/Read first/环境;三栈写法要点;写作纪律)
- [base-adr.md](base-adr.md) - ADR 架构决策记录:frontmatter 契约、Nygard 三段、状态机与 supersede 流、何时写何时不写
- [base-req.md](base-req.md) - REQ 需求登记:frontmatter 契约(status/priority/trace)、Scenario/Criteria、状态机、旧体系迁移映射
- [base-projection.md](base-projection.md) - 生成投影与 agent 检索面:投影三问、三栈机制对照、llms 式索引(CLI 旗标与库投影)、纪律清单(禁止第二真相)
- [base-writing-standards.md](base-writing-standards.md) - 写作规范(文件名即标题、标题干净、六态完整定义(知行合一:五态为实证服务)、路径两制、门禁选配)

### 工作流与发布

- [flow-release.md](flow-release.md) - 封版发布模式:前置裁定、三路全平台门禁、封版件、tag 触发、发布验收
- [flow-archive.md](flow-archive.md) - 日记与研究档案机制:diary 一天一篇与裁定留痕、research SNNN 编号六态索引、择要升 ADR、结构保留红线

### 经验

- [exp-pitfalls.md](exp-pitfalls.md) - 已知误区十八条(ADR/REQ 混淆、手改投影、静默假设、双份漂移、豁免退出、索引底稿、批改塌行、口径返工、环境想当然、CHANGELOG 流水、AGENTS 膨胀、supersede 单边指等)
- [exp-sedimentation.md](exp-sedimentation.md) - 经验沉淀分治:成功/错误两条链、实证与经验循环复利、产生时机与检索路径、二犯升格工作流与集成约束四形态(agent hook/uv 脚本门禁/git 钩子/回归测试)

骨架初始化、测试分层、平台适配与三栈工程合同见同插件 code-kit 的 references/。资料检索(gh / Google / Medium / X / reader / aria2c)见同市场 skill `evo-research:research`,研究成文见 `evo-research:report`。密钥深扫见 `evo-codesec:secret-scan`。多仓飞轮协作(herdr 派单、回执、断言、吸收)见 `evo-herdr:herdr-flywheel`(ADR-0009 起,原 flow-flywheel 参考篇已全量并入退役)。

## 三、全量清单(9 篇)

| 文件 | 主题 |
| --- | --- |
| base-agents-contract.md | AGENTS 五节合同 |
| base-adr.md | ADR 架构决策记录 |
| base-req.md | REQ 需求登记 |
| base-projection.md | 生成投影与 agent 检索面 |
| base-writing-standards.md | 写作规范与六态(知行合一) |
| flow-release.md | 封版发布模式 |
| flow-archive.md | 日记与研究档案机制(SNNN 与沉淀升 ADR) |
| exp-pitfalls.md | 已知误区十八条 |
| exp-sedimentation.md | 经验沉淀分治细则 |

## 检索方法

目录与文件名为 rg 检索设计(前缀=类别词、主干=主题词);文档结构为 mq 提取设计(h2=节、code=命令、表格=键值)。

```powershell
rg --files . | rg 关键词                    # 1 文件名定位(类别词/主题词)
rg -n "关键词" README.md                    # 2 索引导航
rg -n "关键词" . --glob "!README.md"        # 3 全文搜
reader query <文件> ".h2"                    # 4 结构化提取节目录
reader query <文件> ".code"                  #    只抽命令
```
