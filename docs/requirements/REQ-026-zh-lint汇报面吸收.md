---
id: REQ-026
title: zh-lint 汇报面增编:ASD-STE100 中文家族实践吸收
status: implemented
priority: must
trace: tests/test_project_evo.py
---

# REQ-026:zh-lint 汇报面吸收

## Scenario

用户令(2026-10-13,会话中插单):参考外部 ASD-STE100 中文汇报 skill(25 规则、术语表、五模板)提炼进本仓技能体系。一案提案三选一裁定:**patch**(否 create:与 zh-lint 同域,受控中文拆两 skill 伤意图路由;否 no_action:zh-lint 适用面虽含「AI 解释性回答」,但六节四十条是文档面规则,汇报面(结论先行、状态词、验证状态、询问律、模板)是真空)。吸收进 evo-lint:zh-lint,增 references/reporting.md 一页;吸收即提炼,不点名外部仓库,标注家族来源(ASD-STE100 中文家族实践);文档面与上游 0.2 冲突时上游优先,汇报面以新页为准。

## Criteria

- [x] references/reporting.md:结构律(结论先行)、状态词十词表、验证状态(与本仓六态呼应)、询问律、语言律增量、五模板、发前自检
- [x] SKILL.md:适用面加工作汇报与任务回执;新增汇报面速览节;description 补触发词(汇报、回执、结论先行、状态词、已验证、未验证、选项、模板)
- [x] references/README.md 索引行同步
- [x] 不改 zh-lint.py 机检面(情态近义词与缓冲开头入先验核属工具行为变更,候另批)
- [x] 版图计数不变(patch 不加 skill);四门禁全绿
