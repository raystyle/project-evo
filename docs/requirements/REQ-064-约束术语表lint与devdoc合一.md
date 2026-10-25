---
id: REQ-064
title: 约束术语表 lint 与 dev-doc 合一(PE-13 面,批 175)
status: implemented
priority: must
trace: tests/test_project_evo.py
---

# REQ-064:约束术语表 lint 与 dev-doc 合一

## Scenario

总台令(2026-10-25,批 175):doc-gov 与 dev-lint 转换为 dev-doc,只专注项目文档结构与项目文档;参照 search-harness 先例(驻仓 grok 简报:取规则函数纯函数化骨架,lint 真源留本仓)与 ctxs 历史对话语料,定义中英文约束术语扫描 lint 脚本,专修不标准中文、英文黑话、俚语与短语。用户三答定制:语言面裁撤留结构面;进门禁分批收紧(摸基线、存量 PENDING、后批收紧);旧词表(zh-lint,git 9189048^ 复原)作底加语料挖词增补,单一权威规则模块。

语料实证(gw_logs,ClickHouse 只读道):13 天窗 client_request 5% 抽样 16.2 万块;种子词全验活(`收口` 4360、`缺省` 2160、`报错` 2124);高频黑话候选 `落地` 3753、`闭环` 3146、`兜底` 2284、`链路` 1143;英文 `magic` 591、`stuff` 426。仓内基线:ENFORCED 层零命中(45 项首跑全降 PENDING),PENDING 存量 `收口` 45、`沉淀` 39、`缺省` 31 等 18 词。方法与分流档案 S020。

## Criteria

- [x] dev-doc 合一(git mv 保史):router SKILL.md(80 行三句形,旧名 doc-gov/dev-lint 留触发词);references 10 篇(base/tool 五、md-faces 吸收 hook 面、term-rules 新、ls 三);语言面 lang-checks 裁撤退 git 史;templates 四 toml 随迁
- [x] termrules.py 词表唯一权威:zh-lint 词表复原作底 + 语料挖词增补;ENFORCED 四表(ZH_BANNED/ZH_CHOICE/EN_JARGON/TERM_VARIANTS)与 PENDING 两层;复用 mdrules 豁免机制(行内代码/围栏/frontmatter)
- [x] term-lint.py 三态门禁:位置参扫描、--staged 暂存挡板、--pending advisory;实证退出码 0/1/2 与 staged 挡提交
- [x] term-mine.py 研究道:reader.env 主道 + ssh 备道(SQL 走 stdin),截头 2000 字 + 5% 抽样 + LIMIT 限流(ORDER BY 爆内存判例入 S020);原文只落仓外
- [x] PE-13 接线:check.py PE-01 至 PE-13,PEVO_TERM_ALLOW 豁免(docs/ 档案,根三件永不受益);pre-commit 加 term-lint --staged
- [x] 测试守卫:SKILLS/PE 计数/plugin 脚本清单/pre-commit 挡板断言更新;新测 PE-13 豁免镜像、term-lint 退出码、termrules 表健全;test_repo_md_clean 加仓级 ENFORCED 零命中回归
- [x] 计数与守卫全同步:两插件十四 skill(dev 二加 evo 十二)全活面(AGENTS、根 README、docs 地图、gates、dev/evo README、双 manifest、市场清单三处)
- [x] S020 研究档案立档(方法、语料实测、基线分层、复现命令)与三索引登记(adr/requirements/research README)
- [x] 版本:dev 0.17.0、evo 0.19.1;门禁全绿(pytest、check PE-13、scan、term-lint、md-ref-scan 十四面)
