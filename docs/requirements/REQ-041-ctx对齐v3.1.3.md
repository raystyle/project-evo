---
id: REQ-041
title: ctx skill 对齐 prim v3.1.3(直连双闸与 --around 与多词 snip)
status: implemented
priority: must
trace: tests/test_project_evo.py
---

# REQ-041:ctx skill 对齐 prim v3.1.3

## Scenario

总台交流单(2026-10-14):ctx 三连升(v3.1.2 检索道换直连 https 8123 双闸 = client 证书 + ctx_reader SELECT-only,~/.ctx/reader.env 六键 600;v3.1.3 吸收三姿势),我 evo:ctx 按 v3.1.0 写有漂移,令核面更新加三发实弹加回执。ai-ccoe 本机克隆中间版污染经总台复位至 5b43650。

## Criteria

- [x] skill 面全刷:检索道(直连主道双闸 + CTX_* 环境变量 + reader.env 六键 + ssh 兜底)、动词面(show --around/--window 命中点居中 3000 字、search --term 多词 OR + snip)、坑表三入(词 2 字符下限、嵌套抓 rid --limit 1 与切列 f8/f1、块命中无头行属管道时滞);commands.md 六域速查 ctx 行随改
- [x] 三发实弹全绿:search 多词出 snip 退 0;show --around --window 1 出命中块 ±1 带居中标注退 0;view --limit 3 退 0;列位两踩入坑表;时滞观察一件报总台
- [x] 本端 prim 滚 v3.1.3(force 重装六入口);evo 独立升 0.15.1;四门禁全绿 + fleet 回执
