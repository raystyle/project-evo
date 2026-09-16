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
| 契约注释 | `///`（missing_docs 可 deny） | docstring（interrogate 查覆盖） | TSDoc `/** */`（eslint-tsdoc 查语法） |
| agent 投影 | cargo-aidoc：llms.txt 索引 + 分模块 md | Griffe/MkDocStrings（弱,可自写 JSON） | API Extractor 的 .api.json + api-documenter markdown |
| 人看的站 | cargo doc（HTML） | MkDocs/Sphinx | TypeDoc（HTML） |
| 漂移门禁 | aidoc --check --strict | mkdocs --strict + 自写状态机校验 | api-extractor run（CI 无 --local） |
| 示例执行 | cargo test --doc | pytest --doctest-modules | Vitest（可选 doctest 插件） |

TS 侧管线（TypeScript 项目照此配，细节见 tool-typescript.md）：`/** TSDoc */` + tsc 出 .d.ts（勿 removeComments）,分流 TypeDoc 给人、api-extractor 出 etc/*.api.md（进 Git,PR 审公开面）与 .api.json,api-documenter 出 docs/api/（agent 面）。

Python 侧管线（Python 项目照此配，细节见 tool-python.md）：docstring 为源（做什么+何时用+边界）,Griffe/MkDocStrings 出分模块 md,`mkdocs build --strict` 兼作漂移门禁,示例执行 `pytest --doctest-modules`。

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
