# ADR 架构决策记录：锁住不可逆选择的 why

> 不可逆技术选择（选库、存储、协议、公开面形态）先立 ADR 再动手；每篇只答「为什么选这个」。why 不写进函数注释、不写进 AGENTS，进 ADR。

## 文件与索引

- 位置 `docs/adr/ADR-NNNN-slug.md`，编号四位接当前最大号，退役不复用
- `docs/adr/README.md` 索引表：`| id | 状态 | 标题 | 替代 |`，每篇必登记（check.py PE-08 查一致）
- 新建拷 `0000-template.md`（init 产物）；状态机合法性由本 skill 的 check.py 校验（PE-06），不依赖外部工具

## frontmatter 契约

```yaml
---
id: ADR-0007
title: 一句话标题
status: accepted        # proposed 或 accepted 或 superseded
date: 2026-09-14
deciders: [ray]
supersedes: []          # 本篇替代了谁
superseded_by: null     # 谁替代了本篇(被替代时填)
tags: [hashing]
---
```

## 正文三段（Nygard 式）

| 段 | 写什么 | 不写什么 |
| --- | --- | --- |
| Context | 背景与约束、当时的备选项、量化的痛点（如:单线程 170 文件/秒,全盘数小时） | 决策本身 |
| Decision | 一句话可执行的决定 + 为什么是它而不是备选 | 实现细节(那是代码与契约注释的事) |
| Consequences | 好/坏两面;坏面写清后续要跟的事 | 只写好话(坏面才是 ADR 的价值) |

示例节选（哈希算法替换）：Context 给实测数字（单线程 SHA-256 约 170 文件/秒,blake3 实测 3.8 GB/s），Decision 一句「本地消重管线全面改用 blake3,云端路径保留 MD5(协议约束)」，Consequences 明写两套哈希并存的代价。数字进 Context、一句话决定进 Decision、代价不隐瞒进 Consequences。

## 状态机与 supersede 流

- proposed 到 accepted 到 superseded；只进不退（回滚 = 新立 ADR 替代，不改旧文）
- supersede 双向互指：新篇 `supersedes: [ADR-0007]`，旧篇 `superseded_by: ADR-0008`；悬空指向被 check.py PE-06 抓住
- status 与 superseded_by 属流程字段，走工具子命令或谨慎手改，改完跑 check
- accepted 不等于永久：环境变了就 supersede，历史都在案

## 何时写、何时不写

- 写：选存储/选库/换算法/改协议/公开面破坏性变更/「为什么不用 X」会被反复问的选择
- 不写：可逆实现细节（测试与重构可改）、需求（进 REQ）、操作规范（进 guides）
- 判据：**撤销成本高到需要留案**才写;一天能改回的不写 [经验]

## 门禁

- check.py PE-05（文件名）、PE-06（状态机与悬空）、PE-08（索引登记）
- 与代码同 PR：先写或改 ADR 再合代码（两仓 AGENTS Must 节同款要求）
