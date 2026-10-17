---
id: REQ-058
title: mcps/nodes skill 入真源与 dev description 收口(挂起)
status: draft
priority: must
trace: tests/test_project_evo.py
---

# REQ-058:mcps/nodes skill 入真源与 dev 收口

## Scenario

总台令(2026-10-17):mcps(第八原语,MCP 域,出站,引擎 mcp2cli)与 nodes(第九原语,run/close/pane 直透加 ws/yolo/runtime 三子面)两 skill 以总台侧 0.15.13 缓存手建件为底正式入 evo 真源,按 REQ-057 双规范校准(B3 目录-命令对齐、A2 三句形、B4-B11 命令指导型骨架)。前置条件:总台缓存件尚在上架(键表未见),nodes 命令本机(lan-ubuntu)未装、B17 实证准入待装机或总台侧实弹回执。顺批:dev 两面 description 超 400 收口(dev-lint 540、doc-gov 563);md-faces 升静检三件(A2 三句形句法、≤400 上限、B9 废形示例自洽)。

## Criteria

- [ ] mcps skill 入真源(缓存件为底 + 本机 `mcps --llms` v3 实况校准;设计稿键 share/lan-win/bc42cd3cbf)
- [ ] nodes skill 入真源(缓存件为底;命令实证待 nodes 装机或总台侧实弹回执)
- [ ] 双 manifest 与市场清单计数同步(十一 skill 增至十三 skill),守卫 SKILLS 清单增两 skill
- [ ] dev 两面 description 压 400 内(dev-lint、doc-gov)
- [ ] md-faces 静检升三件(三句形、≤400、废形自洽)
- [ ] evo 与 dev 升版;门禁全绿 + fleet 回执
