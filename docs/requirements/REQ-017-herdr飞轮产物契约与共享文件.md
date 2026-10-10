---
id: REQ-017
title: herdr 飞轮产物契约与共享文件
status: implemented
priority: must
trace: tests/test_project_evo.py
---

# REQ-017:herdr 飞轮产物契约与共享文件

## Scenario

用户立单(2026-10-10):跨窗格飞轮对话的产物应写到临时目录统一标准路径的 md 文件进行共享;任务型与委托型交流由提示词生成文件产物,验收按文件对账达成一致。裁定一:发起方不限总台,任何窗格 agent 都可发起委托与同步。裁定二:状态 md 文件与产物 md 文件分职,状态检测看状态档、产物验收看产物笺;所有状态与产物由 agent 自己写盘产生确定稳态,herdr 生命周期态只是干预检查的信号,不是稳态。回归实测在邻居窗格做。

## Criteria

- [x] SKILL.md 落「交流分型与产物契约」节(三型文件化、讨论型不文件化、盘上稳态与 herdr 信号分治),派单、回执、断言、吸收四节同步条文,description 触发词补产物契约面
- [x] references 落 artifacts.md(统一标准路径、三件套 brief/state/receipt 模板、状态档四检查点、干预矩阵、跨机细则、与官方仅兜底口径的分野)
- [x] references/README.md 索引、pitfalls.md 两坑修法(done 假象、备用屏读不全)、parallel.md 条件归约挂接同步
- [x] 邻居窗格回归实测走通 brief 至 state 至 receipt 至对账断言全链(ADR-0010 命令实证;flywheel-01 委托轮,kimi 验证工位)
- [x] 版本载体 0.5.2 升 0.5.3,双 manifest 加市场清单加两插件 README 一致(两插件同版本线)
- [x] 门禁全绿:pytest、md-ref-scan、check、scan;CHANGELOG 第九十九批
