---
id: REQ-060
title: agent 原生 CLI 舰队公约入 dev-cli(交流波聚合)
status: implemented
priority: must
trace: tests/test_project_evo.py
---

# REQ-060:agent 原生 CLI 舰队公约入 dev-cli

## Scenario

总台令(2026-10-21,交流波加办与用户裁):Rust 交流波开 agent 原生 CLI 标准专题,六仓四点晒(现状、痛点、公约提案、测试锁面),产出交本台升级 dev-cli 技能为舰队标准;用户裁定交流波全部讨论成果走 evo distil 机制沉淀,不散落聊天。distil 流水:sources 层归档(rust-exchange 流全文留底、研究件留底、sources 索引),knowledge 层两页(S018 跨仓互鉴、S019 公约聚合),operations 层一案(本 REQ 的 dev-cli 公约面补丁)过合取闸门后总台转各仓采纳。

聚合定稿:S019 六仓票去重,必须 10 条(C1 三面同源派生、C2 机器形统一信封、C3 错误机器化、C4 退出码契约三态文档化、C5 写级动词预览缺省、C6 版本单源注入、C7 生成物进仓与投影守卫、C8 安全面、C9 快照守卫标配、C10 多端味实机冒烟)加应该 3 条(C11 agent 检测机器形默认、C12 成功面 next-step 结构化、C13 类型化 CTA 分级);pi-rs-agent 票到后增量定稿,不回写。

定位:dev-cli 五件(渐进知识库型)上增公约面,agent-face.md 第六节分级表落文,SKILL.md 速览与意图路由补行;实现形与模板细节不重复造,公约条均映射回五件锚点。点名义务(现行标准盖不住的失败义务,闸门谓词二对象):hst 双解析(clap 解析级错误不走机器形)、s5 CTA 无独立字段与字段名分裂(next_step 与 guidance 两形)、dctl 裸调用退出码 2 与外插子进程文本裸进机器面;三条在现行 dev-cli 五件无载面。

## Criteria

- [x] sources 层归档:裸流 rust-exchange 与 room 劈叉支流全文留底、研究件 verbatim 留底(diff 验证字节一致)、`docs/sources/README.md` 索引(ADR-0021 external 根首建)
- [x] knowledge 层:S017 业界先例对照(cited_source 级信源)、S018 跨仓互鉴表、S019 六仓票聚合页(10 必须 3 应该,票源 seq 号可回查)
- [x] dev-cli 公约面落文:agent-face.md 第六节分级表(必须 10 应该 3,各条映射五件锚点,不点名仓库)、SKILL.md 五件速览补公约行与意图路由行、description 增公约触发词(三句形折叠 386 过静检);顺清 templates 与 agent-face 存量半角标题账,信封载体定名 next_step(cta 兼容别名)三面同步(agent-face、templates、第六节)
- [x] 合取闸门三谓词:门禁全绿(pytest 34 passed、check 12 PASS 0 FAIL、scan 0 发现、md-ref-scan 十四面断链 0);点名义务翻转(hst 双解析载 C3、s5 字段分裂载 C2 与定名、dctl 裸调用 2 与外插文本载 C4 与 C8,现行五件均无载面、候选公约面有);知识链接成立(agent-face 第六节背注 S019 与 sources 留底件)
- [x] 变更完整性:docs 地图与 research 索引与 requirements 索引登记、CHANGELOG 批次条、dev 双 manifest 与市场清单同步升 0.16.0(新能力 minor)
- [x] 首令任务一并行交割:原语 skill 优化清单(shares 键 share/lan-ubuntu/2fa1cd5487/ 交总台,活证据含 streams rooms 崩、流劈叉、列表截断、寻址退化、shares 键生命周期、lint-hook 围栏不感知)
- [ ] pi-rs-agent 票到后 S018 与 S019 增量定稿(dctl、pi-rs 晒单同补;定稿判点 next_step 终裁);提案工作区待总台与人裁后提交
