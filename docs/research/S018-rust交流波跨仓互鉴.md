# S018:rust 交流波跨仓互鉴

> 交流波知识页一:七仓晒单的谁偷谁什么表。信源 = rust-exchange 流全文留底 `../sources/external/2026-10-21-rust-exchange-stream.md`(derived_from,seq 号即引文位)加业界先例对照 S017;CLI 标准专题公约聚合另页 S019,标准面落点 REQ-060。发版互学与各自采纳属各仓面,本页只记互鉴判定。

## 互鉴表（谁偷谁什么）

| 偷方 | 偷什么 | 出让方 | 判定 |
| --- | --- | --- | --- |
| ark_rs | socket 常驻进程测试组织 | hst_rs、s5_rs | hst 点名件已答 ark[实证: 流 seq 7];s5 崩溃注入与断点续写在册 seq 5 |
| ark_rs | --llms 活树自省弃静态表手维护 | browse_rs、s5_rs | ark 自认静态表受教,活树更优[实证: 流 seq 14] |
| browse_rs | nextest 按测试进程隔离,解 Mutex 连坐 | 业界共识 | S017 最小公约数第 1 条背书,全仓默认跑测器方向[实证: 流 seq 2 加 S017] |
| s5_rs | 内网小舰队自愈式分发,musl 与 glibc 裁法、binstall 值不值 | reader_rs、业界 | reader musl 静态五平台一条流水是现成实践[实证: 流 seq 5 加 seq 6];binstall 引入属裁剪题,实测定值 |
| reader_rs | cargo-dist 声明式发布件 | 业界 | S017 判读:对外发二进制 CLI 强烈建议,可与 release-please 串联[实证: 流 seq 6 加 S017] |
| 各 CLI 仓 | 错误四元组 code、message、hint、exit_code 单点 | ark_rs | ark arerr.rs 单点冻结面,hst 与 s5 已在信封与枚举上同向[实证: 流 seq 4 加 seq 10 加 seq 11] |
| 各仓 | 多端味产物实机冒烟 | s5_rs | s5 自查缺口反向成条:win 味产物欠实机冒烟[实证: 流 seq 11] |
| haoxun 等非 Rust 仓 | 理念平移:快照测、结构化日志、复现夹具 | 业界 | 工具链不硬搬 cargo 系[实证: S017 第 4 节] |

## 晒单对照（优势面速览,全文见留底件）

| 仓 | 优势面关键词 | 管理与测试面关键词 |
| --- | --- | --- |
| browse_rs | 错误链 CTA 纪律、三层 crate 加 daemon 单点状态面、名实三验 | 文档即契约 missing_docs 加 clippy 全 deny;四层测试(arg_contract 真二进制、e2e 真 chrome SEQ 互斥、实弹 17 案双证) |
| ark_rs | lib 与 bin 分面 core 全可测、错误四元组、纯函数判定核 | md 四件套加投影守卫;本地三段式发布;golden 黄金文件加双环境闸,期望值独立来源 |
| s5_rs | --llms 活命令树、依赖克制同源、零凭据密档 | 穷尽对锁守卫;崩溃注入断点续写、契约反证 2500 条静默截断、缺件 SKIP 不红 |
| reader_rs | TextUnit 全格式统一、极简错误面 grep 语义、musl 静态五平台 | 六层测试(单测、域分 target、smoke、regress、cucumber BDD、insta 快照、corpus 真样本缺自动跳) |
| hst_rs | 原生渲染退役脚本载体、结构化 stderr 单行 JSON | 假二进制注入 PATH 测真子进程边界、kill -9 验锁接管、四线程 Barrier 并发锤 |
| dctl_rs | 待晒单(0.7.0 在途 ledger 全清,CLI 标准票已先到) | 见 S019 票面 |
| pi-rs-agent | 待晒单 | 见 S019 票面 |

## 判定注

- 互学后各自发版是本波目的,发版节拍与版本号属各仓终态,本页不记[经验: 交流波定位,流 seq 0]
- 工具链采纳(nextest、insta、proptest、cargo-dist、tracing)按 S017 判读走各仓 ADR,不进本仓标准页;本仓只收 agent 原生 CLI 公约面(S019)[经验: S017 分流表]
