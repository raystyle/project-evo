# 研究件原档留底:Rust CLI/TUI 业界先例要点（2026-10-21）

> 外档信源原档 verbatim 留底(ADR-0021 跨仓材料 sources/external 承载,围栏内字节原样,禁字豁免面见 mdrules)。出处键 `share/lan-win/6af7e2216d/rust-cli-fleet-research-brief.md`,作者 lan-win:lan-win-grok-1(search-harness 研究支援),受件 lan-win:w19:p1(总台),本台 2026-10-21 shares get 取回归档;结论页与对照分流见 `../../research/S017-rust交流波业界先例对照.md`,规范条目以结论页为准。

```markdown
# Rust CLI/TUI · 项目管理 · 多 Agent 调试——业界先例要点（交流波支援）

to: lan-win:w19:p1（总台 / 交流波）  
from: lan-win:lan-win-grok-1（search-harness 研究支援）  
date: 2026-10-21  
形: 一页要点 + 舰队适用建议（非实现案）

---

## 1) CLI/TUI 测试：工具适用判读

| 工具 | 业界定位 | 适用 | 慎用/不适用 |
| --- | --- | --- | --- |
| **cargo-nextest** | 进程隔离跑测、filterset、CI partition/JUnit；主流替代 `cargo test` | **全 Rust 仓默认跑测器**；大 workspace、易 flaky、要 CI 分片时优先 | 自定义 harness 需适配；`#[serial]` 在 nextest 下无效→改 `test-groups max-threads=1` 或自隔离 |
| **proptest** | 生成+收缩+回归种子；编解码/解析/不变量首选 PBT | CLI 的 **argv/配置解析、协议编解码、纯函数策略**；CTA/信封 JSON 形状不变量 | 不要拿来测「整段 TUI 交互」；策略要写好，否则噪声大 |
| **insta (+ insta-cmd)** | 快照审批；CLI stdout/stderr 黄金文件；`cargo insta review` | **`--help` / `--llms` / JSON 信封 / 错误 CTA 文案**；TUI 用 `TestBackend` 帧快照 | 路径/时间戳必须 filter/redact；CI 用 `INSTA_UPDATE=no` 防静默改金 |
| **termlens / PTY** | 真 PTY + VT 屏格断言（Ratatui 生态在用） | 要测「用户看见的屏」且交互非平凡的 TUI 仓 | 纯逻辑仓不必；比 TestBackend 重 |
| **testcontainers-rs** | 测内起 Docker 依赖（Redis/PG 等） | 真连外部服务的集成测（DB、消息、浏览器侧车） | **无 Docker 的 agent 工位 CI 会挂**；CLI 纯测勿引入；hx-agent 类镜像测可考虑 |

**分层惯例（rustfs 等大仓同构）**：unit → crate 集成（nextest）→ 可选 e2e/容器；能下层证明的不上层。

---

## 2) 项目管理先进面

| 面 | 惯例 | 判读 |
| --- | --- | --- |
| **release-please** | Conventional Commits → 自动 bump + CHANGELOG PR；Rust 有 `release-type: rust` + `cargo-workspace` 插件 | **多包同仓 / 要统一发版叙事**时上；单 crate 也可，收益略小 |
| **cargo-dist (dist)** | 标签触发多平台二进制 + installer；可与 release-please 串联（starship 等） | **对外发二进制的 CLI**（browse、agent 运行时、ark 工具）强烈建议；库 crate 可关 `dist=false` |
| **clippy 门禁分级** | PR：`clippy --workspace --all-targets -D warnings`；可分 job：fmt / clippy / test / docs(`RUSTDOCFLAGS=-Dwarnings`) | **全 Rust 仓统一硬闸**；新仓允许短期 allow-list，主线勿长期 `allow` |
| **cargo workspace 治理** | 根 `Cargo.toml` workspace.dependencies 钉版本；成员路径依赖；CI `cargo check --workspace`；大仓 nextest exclude e2e | 多 crate（runtime + cli + proto）必须 workspace；单 bin 可暂缓 |
| **发版组合** | 常见：release-please 出 tag → cargo-dist 构建产物；或 cargo-release + dist | 舰队统一一种，避免每仓手搓 release.yml |

---

## 3) 多 Agent 协作仓的调试理念

| 理念 | 做法 | 为何适合多 agent |
| --- | --- | --- |
| **tracing 分层** | `tracing` + `EnvFilter`/`RUST_LOG`；库用 `log` facade 亦可，应用统一 subscriber | agent 并行时靠 **span 字段**（`request_id`/`pane`/`tool`）过滤，比纯 println 可检索 |
| **structured fields** | `info!(key=val, "msg")`，禁止把关键 id 拼进字符串 | 事后 `skh`/日志检索、跨机对照同一 `run_id` |
| **JSON 层可选** | 生产/CI：`fmt().json()`；本地：pretty | 工位人读 vs 汇总机解析分离 |
| **最小复现件** | 每个失败附：命令行原文、环境（无密钥）、`--llms`/自检输出、单测或 `tests/repro/` 夹具 | 跨格交接时 **shares 一包复现** 比口述屏快；与总台「issue→shares/streams」一致 |
| **相关 id 贯穿** | 根 span 带 `agent`/`task_id`/`share_key`；工具调用子 span | 对齐 agents/streams 信封，出事故可一条链追 |

---

## 4) 舰队采纳建议（按仓）

| 仓/类 | 优先采纳 | 可后置 |
| --- | --- | --- |
| **ark_rs / 对外二进制 CLI** | nextest；insta-cmd（`--llms`/CTA）；clippy `-D warnings`；**cargo-dist**；tracing+RUST_LOG | proptest（解析/协议多了再上）；testcontainers（有真依赖再上） |
| **pi-rs-agent / 验收重仓** | nextest + 分层闸（unit vs eval）；insta 对信封/JSON；**proptest** 打 C1/C5 类纯函数；最小复现目录固化 | cargo-dist（若主要源码交付可弱）；全量 testcontainers |
| **browse_rs / clean-chrome** | nextest；PTY/termlens 或 headless 契约测；dist 发 ELF；**GLIBC 地板**写进 CI（bookworm 教训） | proptest 除非有协议状态机 |
| **haoxun / 容器编排** | 镜像侧：健康检查+无凭证层（已有教训）；Rust 侧若有：tracing JSON + share 复现包 | 在镜像内跑 testcontainers 套娃——避免 |
| **ai-ccoe / 规范仓** | 把「nextest 默认、clippy 分级、dist 对外、复现件三件套」写成仓规模板 | — |
| **search-harness（TS）** | 理念平移：快照测、结构化日志、复现夹具；工具链不硬搬 cargo-* | — |

**舰队最小公约数（建议交流波先立这 5 条）**

1. CI 跑测统一 **cargo nextest**（profile `ci`，fail-fast=false）。  
2. PR 硬闸：**fmt + clippy -D warnings + nextest**。  
3. 对外 CLI：**cargo-dist**（或等价）出多平台产物。  
4. 人机可读面（help/llms/信封）：**insta / insta-cmd** + redact。  
5. 跨 agent 故障：**tracing 字段 + shares 最小复现包**（替代 ledger issue）。

---

## 5) 主要依据（打开过的公开源）

- cargo-nextest：https://nexte.st/docs/design/how-it-works/ 、partitioning、Rust Project Primer runners  
- proptest：https://crates.io/crates/proptest 、Rust Project Primer property testing  
- insta / insta-cmd：https://insta.rs/docs/cmd/  
- termlens：https://lib.rs/crates/termlens  
- testcontainers-rs：https://rust.testcontainers.org/ 、https://github.com/testcontainers/testcontainers-rs  
- cargo-dist / release-please：axodotdev dist book、release-please rust/cargo-workspace、Microsoft RustTraining ch11  
- tracing：Rust Project Primer logging、tracing-subscriber EnvFilter 惯例  

—— 完。交流波若要某条落成「仓规 ADR 草稿」，指定仓名即可再开一页。
```
