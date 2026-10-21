# S017:rust 交流波业界先例对照

> 交流波研究轮:研究方 lan-win:lan-win-grok-1(search-harness 业界先例调研),原档键 `share/lan-win/6af7e2216d/rust-cli-fleet-research-brief.md`,本仓 verbatim 留底 `../sources/external/2026-10-21-rust-cli-fleet-research-brief.md`(2026-10-21 取回);受件与转发 lan-win:w19:p1(总台)。本页是信源与分流档案:舰队最小公约数五条与按仓采纳建议是研究方结论,跨仓互鉴判定落 S018,agent 原生 CLI 公约聚合落 S019,入标准面走 REQ-060,条目定稿以彼为准。

## 信源（cited_source）

- 研究件原档:本仓 sources/external 留底件(字节原样)[实证: 2026-10-21 shares get 取回后 diff 验证]
- 原档所引公开源:cargo-nextest 官方文档(design/partitioning)、proptest crates.io、insta 与 insta-cmd 官方、termlens lib.rs、testcontainers-rs 官方与仓、cargo-dist 与 release-please 官方书、tracing 与 tracing-subscriber EnvFilter 惯例[实证: 原档 2026-10-21 实查,本台未重开,结论归 cited_source 级]

## 关键口径（研究方结论）

- **舰队最小公约数五条**(原档第 4 节,建议交流波先立):CI 跑测统一 cargo nextest(profile ci,fail-fast=false);PR 硬闸 fmt 加 clippy -D warnings 加 nextest;对外 CLI 用 cargo-dist 或等价出多平台产物;人机可读面(help/llms/信封)用 insta 加 insta-cmd 加 redact 锁快照;跨 agent 故障走 tracing 字段加 shares 最小复现包[实证: 原档结论,2026-10-21]
- **工具适用判读**:nextest 全 Rust 仓默认跑测器,自定义 harness 需适配、serial 在其下无效;proptest 打 argv/配置解析/协议编解码/纯函数不变量,勿测整段 TUI 交互;insta 锁 --help/--llms/JSON 信封/CTA 文案,路径时间戳必须 redact,CI 用 INSTA_UPDATE=no 防静默改金;termlens 真 PTY 只给交互非平凡 TUI;testcontainers 无 Docker 工位会挂,CLI 纯测勿引入[实证: 原档判读,2026-10-21]
- **项目管理面**:release-please 多包同仓或统一发版叙事时上;cargo-dist 对外发二进制 CLI 强烈建议,可与 release-please 串联;clippy 分级门禁全仓统一硬闸;多 crate 必须 workspace,单 bin 可暂缓;发版组合舰队统一一种避免每仓手搓[实证: 原档判读,2026-10-21]
- **多 agent 调试理念**:tracing 分层加 EnvFilter,靠 span 字段(request_id/pane/tool)过滤;关键 id 禁拼进字符串;JSON 层生产 CI 与本地 pretty 分离;最小复现件(命令行原文加环境加自检输出)跨格交接用 shares 一包复现;根 span 带相关 id 贯穿[实证: 原档判读,2026-10-21]

## 对照分流（吸收与不吸收）

| 原档要点 | 分流 | 落点 |
| --- | --- | --- |
| 最小公约数五条(工具链面) | 吸收为互鉴判定底料 | S018 表判列;工具链属各仓面,不入本仓标准 skill |
| 按仓采纳建议(ark/pi/browse/haoxun/ai-ccoe/search-harness 六分) | 吸收为互鉴表行 | S018 |
| 测试工具选型判读(nextest/proptest/insta/termlens/testcontainers) | 吸收 | S018;各仓按需采纳,本仓不锁死工具名进标准页 |
| insta 锁人机可读面加 redact | 吸收进 CLI 公约 | S019 快照守卫条;REQ-060 |
| tracing 字段加最小复现包 | 吸收为跨 agent 故障公约 | S019 机器面文本纪律邻近条;REQ-060 酌情 |
| cargo-dist/release-please 发版组合 | 不吸收进本仓标准页:发版属各仓工具链面,S010 已有四样板对照,不重复立标准 | S018 判定列 |
| 仓规模板化(ai-ccoe 条) | 不吸收:本仓是治理市场仓不是 Rust 实践仓,仓规模板归实践仓自持 | 无落点 |
