---
id: REQ-058
title: mcps/nodes skill 入真源与 dev description 收口(挂起)
status: implemented
priority: must
trace: tests/test_project_evo.py
---

# REQ-058:mcps/nodes skill 入真源与 dev 收口

## Scenario

总台令(2026-10-17):mcps(第八原语,MCP 域,出站,引擎 mcp2cli)与 nodes(第九原语,run/close/pane 直透加 ws/yolo/runtime 三子面)两 skill 以总台侧 0.15.13 缓存手建件为底正式入 evo 真源,按 REQ-057 双规范校准(B3 目录-命令对齐、A2 三句形、B4-B11 命令指导型骨架)。前置条件:总台缓存件尚在上架(键表未见),nodes 命令本机(lan-ubuntu)未装、B17 实证准入待装机或总台侧实弹回执。顺批:dev 两面 description 超 400 收口(dev-lint 540、doc-gov 563);md-faces 升静检三件(A2 三句形句法、≤400 上限、B9 废形示例自洽)。

## Criteria

- [x] mcps skill 入真源(缓存件为底 + 本机 view/tools 错径/add/remove 回环实弹;设计稿键 share/lan-win/bc42cd3cbf)
- [x] nodes skill 入真源(总台新写件为底微校;总台全动词实弹回执在单;enable/disable/reconnect/pane 四例已补,总台 2026-10-17 四动词实跑回文:disable/enable lan-mac 状态翻转、reconnect 非交互面限制入坑表、pane get JSON 面出,批 169续)
- [x] 双 manifest 与市场清单计数同步(十三 skill),守卫 SKILLS 清单与 B3 正典集增两 skill
- [x] dev 三面 description 压 400 内(dev-cli 380/dev-lint 399/doc-gov 400,连带补三句形)
- [x] md-faces 静检升两件(三句形、≤400,mdrules+md-guard+pytest 三面接线);废形自洽延后:需逐域废旗标登记表,另批立项
- [x] evo 升 0.16.9、dev 升 0.15.0;门禁全绿 + fleet 回执
