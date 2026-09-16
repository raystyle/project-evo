---
id: REQ-001
title: check 输出 --json 机器读面与全量违规报告
status: implemented
priority: must
trace: tests/test_project_evo.py
---

# REQ-001:check 输出 --json 机器读面与全量违规报告

## Scenario

check 的消费方(飞轮回执、下游仓门禁脚本)需要机器可读结果:退出码只带得过/不过,SKIP 处数与逐项违规明细此前只能正则抓人读 stdout(hst_rs 飞轮回执实证);同时人读面违规清单只报前 5 处,PE-11 还只报每文件第一处(ark_rs 修一轮冒一轮,三轮才清)。

## Criteria

- [x] check.py 提供 --json:stdout 只出 JSON 取代人读逐项表,schema 为 ok(bool)、counts(pass/fail/skip 三计数)、results 逐项(id/status/note/violations),violations 恒在、无为空列表
- [x] 退出码契约不变:0 全过(含 SKIP)/ 1 有 FAIL / 2 出错;出错仍 stderr 文本,不包 JSON
- [x] 违规清单全量:PE-05/06/07/08/10/11/12 去前 5 与前 4 截断,PE-11 逐行列出同文件全部违规行
- [x] 人读面逐项表与结论行格式不变,仅去截断
- [x] 测试覆盖:干净脚手架 JSON 形状与计数、注错后 violations 非空加退出码 1、豁免面 counts.skip 直读、单检查超 5 处全量列出
