---
patterns: [ADR, REQ, 立决策, 立需求, 需求登记, supersede, trace 回填, 状态机, 不可逆]
---

## ADR 与 REQ 治理指导

- ADR 管不可逆技术选择;REQ 先立单再实现;编号接当前最大号,退役不复用
- ADR 状态机:proposed > accepted > superseded(互指,frontmatter superseded_by 可达);正文三段 Context/Decision/Consequences(Nygard 形)
- REQ 状态机:draft > implemented(必带 trace 回填)/ rejected;正文 Scenario/Criteria;trace 指验收证据位(测试文件等)
- 各自 README 索引表必登记(门禁 PE-06/07/08 断言);历史档案不回写,旧名为当时事实
- 判据:改公共契约、裁撤既有面、换技术栈先立 ADR;新功能需求先立 REQ 再动代码
