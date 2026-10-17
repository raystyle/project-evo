---
id: REQ-057
title: SKILL 双规范定稿与修批(批168)
status: implemented
priority: must
trace: tests/test_project_evo.py
---

# REQ-057:SKILL 双规范定稿与修批

## Scenario

总台三人组合稿单(2026-10-17):真源方起草 evo 约束侧、grok 业界先例(键 share/lan-win/ca5de0e026,档案 S016)、总台终审。两规范(语言约束 A1-A12、格式结构 B1-B18)定稿入 `docs/guides/skill-spec.md`,条目尾标执行面(静检/守卫/闸门/纪律);业界口径与治理层追加显式分流(声明节 + S016)。研究轮计数勘误入 S016(真源 11 面,研究方在总台侧旧缓存 0.15.13 点 10 面)。顺批修:pipes 示例废形出清与 send 例补实弹环;ports 补 fwd 例(数据面 HTTP 200 实证);distil 三句形补面;docs 地图回补(S014/S015/S016 行、agents 行五原语旧表述);守卫测试增目录-命令对齐断言;evo 升 0.16.8。dev 两面 description 超 400(540/563)收口与 mcps/nodes skill 正式入真源另立 REQ-058。

## Criteria

- [x] guides/skill-spec.md 双规范 A1-A12/B1-B18 条目化,治理层追加项标明非业界硬标准
- [x] S016 信源与对照分流档案立卷,计数勘误入档(10 vs 11 面差异判定)
- [x] pipes 示例废形出清(`open --keep` 删,补 `send` 例;open-send-close 实弹环)
- [x] ports 示例补 `fwd` 恰一条(fwd 隧道数据面 HTTP 200 实证)
- [x] distil frontmatter description 三句形补面(Use when 句式对齐 + 不要用于句)
- [x] docs/README.md 回补 S014/S015/S016 行与 agents 行七原语表述;research/README.md 回补 S015/S016 行
- [x] 守卫测试增目录-命令对齐断言(evo 域 skill 目录名 = 命令名复数形,非命令面例外)
- [x] evo 独立升 0.16.8;门禁全绿(pytest 33 过、check 12 面、断链 0、scan 净)+ fleet 回执
