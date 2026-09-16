# 生成投影与 agent 检索面：文档是投影，不是真相

> 公开契约的真相永远在源码（类型签名 + 契约注释）；API 文档是工具生成的投影。手改投影会被下次生成覆盖，另写手维护的 API.md 是第二真相，必漂移。公开面漂移靠 CI 门禁（必红），不靠自觉。

## 投影三问

| 问题 | 判据 |
| --- | --- |
| 谁生成 | 工具从源码注释生成（aidoc/Extract/MkDocStrings），不是手写 |
| 谁进 Git | diff 面进 Git（etc/*.api.md、docs/api/、docs/aidoc/），PR 里审公开面变化 |
| 谁门禁 | CI 重生成后与入库版 diff，不一致即红（api-extractor 无 --local、cargo aidoc --check --strict、mkdocs build --strict） |

## 三栈投影机制对照

| | Rust | Python | TypeScript |
| --- | --- | --- | --- |
| 契约注释 | `///`（missing_docs 可 deny） | docstring（ruff D 规则查覆盖） | TSDoc `/** */`（eslint-tsdoc 查语法） |
| agent 投影 | cargo-aidoc：llms.txt 索引 + 分模块 md | Griffe/MkDocStrings（弱,可自写 JSON） | API Extractor 的 .api.json + api-documenter markdown |
| 人看的站 | cargo doc（HTML） | MkDocs/Sphinx | TypeDoc（HTML） |
| 漂移门禁 | aidoc --check --strict | mkdocs --strict + 自写状态机校验 | api-extractor run（CI 无 --local） |
| 示例执行 | cargo test --doc | pytest --doctest-modules | Vitest（可选 doctest 插件） |

Rust 侧管线（Rust 项目照此配，细节见 code-kit 的 tool-rust）：`///` 契约注释为源,cargo aidoc 生成 `docs/aidoc/`（llms.txt 索引加 分模块 md 加 api JSON,全部生成物）,`cargo aidoc --check --strict` 作漂移门禁,示例执行 `cargo test --doc`。

TS 侧管线（TypeScript 项目照此配，细节见 code-kit 的 tool-typescript）：`/** TSDoc */` + tsc 出 .d.ts（勿 removeComments）,分流 TypeDoc 给人、api-extractor 出 etc/*.api.md（进 Git,PR 审公开面）与 .api.json,api-documenter 出 docs/api/（agent 面）。

Python 侧管线（Python 项目照此配，细节见 code-kit 的 tool-python）：docstring 为源（做什么+何时用+边界）,Griffe/MkDocStrings 出分模块 md,`mkdocs build --strict` 兼作漂移门禁,示例执行 `pytest --doctest-modules`。

## 契约注释通用准则（三栈共用）

- **公开项必写**：对外暴露的模块、函数、方法、类型、公开字段必须有契约注释,覆盖率由 lint 钉死（Rust `missing_docs`、Python ruff `D` 规则、TS jsdoc 规则）;私有实现复杂算法写「为什么」而非「是什么」
- **首句成句**：首段是一句可独立成句的简述（做什么加何时用加边界）,不以项名开头（rustdoc 自动加前缀,余栈同理防复读）;细节隔空行再写
- **不重复机器可推的信息**：类型、参数名、默认值只在签名里;文字只补语义（用途、前置条件、边界、示例）
- **示例必须真实可测**：禁止「仅供参考」假代码;断言收尾让示例兼回归测试;外部服务改内存实现或 mock 保 CI 可重复;不执行的块显式标注（`no_run`/`ignore`/`compile_fail`）并注明原因
- **失效即失败**：文档与代码行为不一致视为 bug,与功能 bug 同等对待;示例挂了是回归不是「文档问题」
- **风格单一**：每仓一种风格（Rust 原生 `///` 唯一、Python PEP 257 加 Google、TS TSDoc）禁混用;存量在改动时补齐,不推倒重写

## 无自有 API 面项目（构建树与补丁仓）

不是所有仓都有自有 API 面（外源构建树加补丁、纯构建定制等形态）。此类项目三栈投影整栈不适用，不立新栈篇；三件通用 [经验: 首个构建树仓用户反馈 2026-09-16]。**范围限定:Rust 仓不适用本范式,aidoc 投影一律强制（bin-only 不豁免,受众是维护者与 agent）**:

- 公开契约 = 字节确定性产物：补丁与生成物可重生成并 diff 等价（regenerate-and-diff）,作为公开面漂移门禁的对应物
- 构建门禁进 AGENTS Commands 在册：构建命令本身是文档的一部分
- 一句裁定入文档地图：明示三栈投影不适用、公开契约走什么，替代整栈工具篇

## agent 检索面（渐进披露）

读序（AGENTS 的 Read first 节引用）：

1. 入口索引（llms.txt / api.md 摘录）：一行一模块,拿候选
2. 对应模块投影页（docs/api/<module>.md 或 docs/aidoc/<crate>/<mod>.md）
3. 仍不确定再开源码契约注释与 .d.ts
4. 禁止整读全量投影（全量文件只检索不整读）[经验]

索引文件形态：`# 项目名` + `## <模块组> <版本>` + 每模块一行 `- [名](相对路径): 一句话职责`。

## 纪律清单

- 禁止手改生成物；投影文件头注明「生成物,勿手改」
- 禁止另写第二真相（API.md / 手维护的参考文档）；叙述性文档（guides）不算投影,可手写
- 覆盖率门禁：类型树 + 测试 + 投影报告锁的是「公开面没悄悄变」「导出项有注释」,锁不住「散文正确」「需求仍是意图」;散文正确靠审查,需求对齐靠 REQ [经验]
- 极小内部包可只开 diff 报告（apiReport）不上 documenter;公开库两者都要
- 投影与契约注释同一 PR 更新；先跑生成命令再提交（AGENTS Commands 节注明本地命令）
