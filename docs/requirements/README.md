# Requirements 索引

> 需求登记:新需求先立 REQ 再实现,实现后回填 trace(测试或验收命令)。新建拷 skill 模板(code-kit assets/templates/docs/requirements/0000-template.md),编号接当前最大号。

| id | 状态 | 优先级 | 标题 | trace |
|---|---|---|---|---|
| REQ-001 | implemented | must | check 输出 --json 机器读面与全量违规报告 | tests/test_project_evo.py |
| REQ-002 | implemented | must | 市场更名 project-evo 与四插件重组落地 | tests/test_project_evo.py |
| REQ-003 | implemented | must | herdr 评审闸门 skill 增编 | tests/test_project_evo.py |
| REQ-004 | implemented | must | 命令出错自动上报 issue 的 gh-issue 增编 | tests/test_project_evo.py |
| REQ-005 | implemented | must | build-release 流水线标准指导 skill 增编 | tests/test_project_evo.py |
| REQ-006 | implemented | must | cli-docs 对外面双标准 skill 增编 | tests/test_project_evo.py |
| REQ-007 | implemented | must | report skill 移除,evo-research 收敛为单 skill | tests/test_project_evo.py |
| REQ-008 | implemented | must | gh-issue 与 build-release 与 evo-research 移除,四插件收敛三插件七 skill | tests/test_project_evo.py |
| REQ-009 | implemented | must | evo-codesec 插件下线与 md-guard 挡板限仓内 md | tests/test_project_evo.py |
| REQ-010 | implemented | must | 三 skill 合一为 doc-gov,evo-adr 改名 evo-doc,skill 与 hook 解耦 | tests/test_project_evo.py |
| REQ-011 | implemented | must | herdr 委派与窗格布局轻吸收(lane 分发、四窗格定式、py 脚本评估) | tests/test_project_evo.py |
| REQ-012 | implemented | must | herdr 双模式定形:herdr-dev 开发模式含 review 窗格,herdr-flywheel 跨仓模式 | tests/test_project_evo.py |
| REQ-013 | implemented | must | herdr-flywheel 跨机器 machine 原语语义补强 | tests/test_project_evo.py |
