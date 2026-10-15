---
id: REQ-054
title: v3.4.3 批收编:send/fwd 收方动词与 token 英文化(批165)
status: implemented
priority: must
trace: tests/test_project_evo.py
---

# REQ-054:v3.4.3 批收编

## Scenario

总台 v3.4.3 批令(2026-10-15,真源 412cfef/归档 ba7c65f):pipes send 与 ports fwd 收方动词入列(引擎名退出取用行)、win 防火墙检测 CTA(规则名 tailcat-in,默认入站 Block 提醒)、指令 token 全英(host:pane/host:alias/recipient)。本批:pipes/ports SKILL 各加 send/fwd 动词行与 win 坑行、取用行改 pipes send/ports fwd(deliver-gate/collab/commands 同步,send 原语缺口记档出清)、token 英文化扫全 skill 面(host:pane/host:alias/@recipient/view [host]);lan-ubuntu 翻台 v3.4.3。

## Criteria

- [x] pipes SKILL:send 动词行、取用行改 pipes send、win 防火墙坑行
- [x] ports SKILL:fwd 动词行、取用行改 ports fwd、win 防火墙坑行
- [x] deliver-gate/collab/commands:取用行族同步,缺口记档出清,七域速查 send/fwd 行
- [x] token 英文化全扫:机:格/机:别名/机:agent别名/@收方 改 host:pane/host:alias/@recipient;view [机] ; view [host]
- [x] lan-ubuntu 翻台 prim v3.4.3
- [x] evo 独立升 0.16.3;门禁全绿 + fleet 回执
