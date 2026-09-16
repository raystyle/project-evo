# AGENTS 五节合同：项目的极简宪法

> AGENTS.md 只回答两件事：用哪条命令、先读哪份。保持短（<60 行为宜）；细则进 ADR/REQ/契约注释，不进本文件。CLAUDE.md 一行 `@AGENTS.md` 桥接，不重复维护。

## 五节结构（四硬一软）

| 节 | 回答 | 写法 |
| --- | --- | --- |
| `## Commands` | 构建/测试/检查/文档投影用什么命令 | 每行一条可复制命令 + 一句用途；含提交前必跑项注明 |
| `## Must` | 硬性义务 | 改公开项同步契约注释与测试；不可逆选择先立 ADR；新需求先立 REQ |
| `## Must not` | 硬性禁令 | 手改生成物、另写第二真相、把 why 写进函数注释 |
| `## Read first` | 检索阶梯 | 公开面投影 到 契约注释 到 源码；ADR 仅在改对应决策时读 |
| `## 环境` | 平台与运行时事实（软节） | Windows/PowerShell、端口、路径、日志位置等事实，无则省略 |

头部：`# 项目名` + 一句话定位 + 公开契约以什么为准（类型签名与契约注释）。

## 三栈写法要点

| 栈 | 头部定位句式 | Commands 特征 | Must not 特征 |
| --- | --- | --- | --- |
| Rust | 公开契约以 `///` 与类型签名为准 | fmt/clippy/test/doc/aidoc --check 全列 | 手改 docs/aidoc/、另写 API.md、把 ADR 正文贴进函数文档 |
| Python | 公开契约以 src 类型与 docstring 为准 | uv sync/pytest/ruff(D 规则)/投影校验 | 手写第二份 API.md、手改 ADR status、用 noqa 掩盖新增公开 API |
| TypeScript | 公开契约以导出、.d.ts 与 TSDoc 为准 | test/typecheck/lint/docs/api:check | 手改 etc/*.api.md、removeComments:true |

## 写作纪律

- 每节几行到十几行；超过一屏说明内容该下沉到 ADR/REQ/references
- 命令必须可复制执行；带平台差异时分行列出或注明 shell
- Must/Must not 用可判定的表述（「改 pub 项同步 doctest」可查；「保持优雅」不可查）
- 环境节只记事实（端口、默认路径、发现顺序），不记规范
- 改合同与改代码同一 PR；AGENTS 漂移即体系失真 [经验]

## 与其他层的关系

- why 不进 AGENTS（进 ADR）；需求不进 AGENTS（进 REQ）；API 不进 AGENTS（进投影与契约注释）
- AGENTS 是 agent 的第一入口：Read first 节就是渐进检索的起点（先投影后源码，不整读全量文档）
- 检查合规用 `check.py`（PE-01 查五节齐备）
