# Rust 工程合同：workspace、契约注释与 aidoc

> Rust 栈的文档即代码落地。项目从零起步照此配；投影与状态机总纲见 base-projection.md 与 base-adr.md。

## 工作区与工具链

- workspace 成员 `crates/*`；`rust-toolchain.toml` 钉版本
- 生成物与部署产物 .gitignore；协议清单类生成物（如 methods.txt）源头 refs 不入库,改协议版本重跑生成脚本再提交

## 契约注释（L1）

- 公开契约以 `///` 与类型签名为准；`missing_docs` 设 deny（CI 必红）,配 `#![warn(rustdoc::broken_intra_doc_links)]`
- 章节纪律（固定用词,rustdoc 与 clippy 识别）：`# Examples` 公开函数强制;`# Panics` 可能 panic 时强制;`# Errors` 返 `Result` 时强制（clippy `missing_errors_doc`）;`# Safety` 用于 `unsafe` 项,必须列全不满足即 UB 的前置条件（clippy `missing_safety_doc`）;参数语义非自明时 `# Arguments`
- clippy 开 `missing_errors_doc` 与 `missing_panics_doc` 与 `missing_safety_doc`
- 文档链接只用 intra-doc（`` [`Session::call`] ``）,不手写会死的外部 URL
- I/O 类示例标 `no_run`,不标 `ignore`（保持可编译验证）;错误示例用 `compile_fail` 并注明预期
- doctest 即示例冒烟：`cargo test --doc --workspace`（`cargo test` 默认已含）;错误矩阵进 tests

## 门禁命令（AGENTS Commands 节候选）

```text
cargo fmt --all
cargo clippy --workspace --all-targets -- -D warnings
cargo test --workspace
cargo test --doc --workspace
cargo doc --no-deps --workspace
cargo aidoc --check --strict      # 投影漂移门禁(改 pub/文档后先 cargo aidoc 再提交 docs/aidoc)
```

## 投影（agent 面）

- **aidoc 是 Rust 仓强制标配,不是可裁定项**（bin-only 仓不豁免:投影受众是维护者与 agent,不是外部用户）;「无自有 API 面」范式不覆盖 Rust 仓
- `docs/aidoc/`：llms.txt（入口索引）+ 分 crate 分模块 md + api JSON；全部生成物,手改被覆盖
- 改 pub 项流程：同步 `///` 与 doctest,跑 `cargo aidoc` 生成,`git add docs/aidoc` 同 PR 提交
- 工具渲染格式的禁字（如条目分隔符）无开关可改时：路径级豁免登记在册（`PEVO_CHECK_ALLOW` 指 `docs/aidoc/`）,漂移真门禁仍是 `aidoc --check --strict`；源头能改的一律改源头,不为生成物开口子 [经验: 首个 aidoc 全量投影仓 2026-09-16]

## ADR 与运维事实

- 不可逆选择进 docs/adr（引擎策略、daemon 形态、通道选型等,每篇一决策）
- 环境类事实（端口默认值、进程发现顺序、域策略环境变量、日志与 profile 路径）记 AGENTS 环境节,不散落 README

## 工程要点

- daemon 常驻 + 双通道（HTTP/WebSocket）时,守护类逻辑（如「不许关用户浏览器」）放 Session 调用层拦截,「绕不过是特性不是 bug」写进 Must not [经验]
- E2E 共享浏览器 profile 须互斥串行（浏览器单实例锁,并发必挂）,tests 里用全局序约束 [实证]
- spawn 浏览器引擎的平台特例（沙箱策略与部署形态冲突等）在 ADR 记因,在 AGENTS Must 钉行为
- 本机装 CLI 用 `cargo install --path crates/<cli> --force` 进 PATH
