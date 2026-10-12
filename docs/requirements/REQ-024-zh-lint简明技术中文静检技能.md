---
id: REQ-024
title: evo-lint 第三技能 zh-lint:简明技术中文静检
status: implemented
priority: must
trace: tests/test_project_evo.py
---

# REQ-024:zh-lint 简明技术中文静检技能

## Scenario

用户令(2026-10-12):给 lint 面增加一个 SKILL 和工具,参考 mzopedia/simplified-technical-chinese(简明技术中文规范 0.2:六节四十条 + 词表三张表,CC-BY 4.0,自带 check.py 示范)。裁定挂 evo-lint 第三 skill zh-lint(客户端 evo-lint:zh-lint):蒸馏规则页不 vendor 全文,工具内置先验核 + --wordlist 外接上游词表全表(沿 ADR-0022 自研不引依赖判例,上游仓为活权威)。

## Criteria

- [x] REQ-024 立档;版图五插件十 skill(evo-lint 三 skill)
- [x] `scripts/zh-lint.py`(PEP 723 零依赖):内置先验核(无条件禁用词 + 选词)+ --wordlist 外接词表三张表(自动检查列、编号项内条件)+ 句长机检(操作句 30 描述句 40,汉字 1 英文词数字串 1 行内代码 1 标点不计),退出码 0/1,只报不改,行内代码不参检
- [x] SKILL.md(适用面、写前分类、六节必须条速览、工具用法、模式与分工)+ references/stc-rules.md(四十条蒸馏带判例)+ 索引
- [x] 与 md-lint 分工句(md-lint 管格式禁字断链,zh-lint 管语言清晰度);权威入口指上游规范与词表
- [x] 双 manifest、市场清单、插件 README、AGENTS、根 README、docs 地图、pre-commit、测试清单(SKILLS + 行为测试)全同步;四门禁全绿
