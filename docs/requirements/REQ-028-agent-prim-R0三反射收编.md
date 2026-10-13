---
id: REQ-028
title: agent-prim R0 三反射收编(门控 v2 与 read 隐式收件与拒投代记)
status: implemented
priority: must
trace: tests/test_project_evo.py
---

# REQ-028:agent-prim R0 三反射收编

## Scenario

总台令(2026-10-13,R0 修件已全推至 ai-ccoe main 5f7b48c):门控 v2 四家 TUI 判标族(16ae19e:不看状态字段看 TUI 实况,操作对话框拒投、空 TUI 可投、busy 排队不拦;5f7b48c:判标族扩 claude/codex/grok/kimi)、read 隐式收件(忙则内候到闲/完成或超时,status 随信封,--timeout 调)、agents to 拒投代记补齐(3a2435d,含原文截 80 字);另动词面补齐(afb8e02:start/ws/shell/dev/split/tab/zoom/keys/trust/sync)与 pipes 域铸齐(16a2e1c)。本仓 agent-prim skill 反射节按三件收编,总台候首稿与 R1 攻击单。

## Criteria

- [x] SKILL.md 四节重铸为投递与收件反射三律(投递只看 status 与 CTA、收件 agents read 自带忙候与超时、拒投自动代记 deferred);门控 v2 判据与 busy 排队不拦入律;常见坑随改(streams 拒投不含原文、busy 误区、-n 调量;pipes 铸齐坑撤)
- [x] references 同步:commands.md(agents 收件面与工位动词、pipes 铸齐、streams -n、差异表收缩至 R0 后残余十一行)、deliver-gate.md(门控 v2、代记全域、read 收件信封)、collab.md(-n);description 与 evo-agent README 随改
- [x] 实证准入:本机 uv 工具重装自 ai-ccoe main 5f7b48c 后实测(read working 格 timeout-working 信封、read 闲格 idle 信封、streams -n、pipes view exit 0、斜杠流名 cursor 崩复测仍在)
- [x] 版本线 0.11.0 进 0.11.1(五插件双 manifest、市场清单、五插件 README 发行行);四门禁全绿 + 回执走 streams append fleet
