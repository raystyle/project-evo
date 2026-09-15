# {name}

一句话定位:<这是什么、给谁用>;公开契约以代码里的类型签名与契约注释为准,文档只是投影。

## Commands

- <构建>:<按栈填,如 uv run pytest / cargo test --workspace / npm test>
- <检查>:<如 ruff check / cargo clippy / npm run typecheck>
- <文档投影>:<如 mkdocs build --strict / cargo aidoc / npm run api:check>

## Must

- 改公开项:同步契约注释与测试,同一次提交
- 不可逆技术选择:先写 docs/adr/ 新 ADR 或改旧 ADR 状态
- 新需求先在 docs/requirements/ 立 REQ 再实现;实现后回填 trace
- 事实性断言标六态:[实证]/[推断]/[经验]/[记忆]/[假设]/[直觉]

## Must not

- 手改生成物投影或另写第二份 API 文档当真相
- 把 why 写进函数注释(进 ADR)
- 未登记的需求直接写码

## Read first

- 本文件(合同)与 docs/requirements/ 对应 REQ
- 公开契约:源码契约注释(类型签名 + docstring/文档注释)
- docs/adr/ 仅在改对应决策时
- docs/diary/ 过程留痕;docs/research/ 研究档案(六态)

## 环境

- 平台与运行时事实:<如 Windows + PowerShell 7,Python 3.12,uv>
