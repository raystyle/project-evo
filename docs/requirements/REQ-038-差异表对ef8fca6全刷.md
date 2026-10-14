---
id: REQ-038
title: 差异表对 ef8fca6 全刷(互审 CONFIRM 家庭作业)
status: implemented
priority: must
trace: tests/test_project_evo.py
---

# REQ-038:差异表对 ef8fca6 全刷

## Scenario

总台互审 CONFIRM(2026-10-13):五答全收,四件攻单两修两关落账(reload 保名与 caller_addr 歧义在 ef8fca6 修,wt 早拒与 close 零击杀实测已在位);指令 = 差异表十行对 ef8fca6 全刷入下批。

## Criteria

- [x] 本机重装 prim(ef8fca6)实证:caller_addr 同 cwd 多格歧义不猜告警 + 退化取用行(自探针回环双落地);close 零击杀与 reload 保名包源直读
- [x] commands.md 差异表全刷:caller_addr 行改「歧义已修」;新入「手册 close 语义滞后于零击杀码」漂移行(报总台);表头实态升至 ef8fca6
- [x] agents SKILL:close 行改零击杀形;reload 行补名字保真(存量名保名,非法名自修正披露 old-name);addressing.md 同 cwd 判例更新
- [x] evo 独立升 0.14.3(dev 不动);四门禁全绿 + 回执贴台 + fleet 回执;总台走 rollout 序(装毕其贴回执,六端 reload 归其辖)
