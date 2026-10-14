---
name: pipes
description: >-
  pipes 原语(prim v3 实时字节域):tailcat 实时管道(本机收对方发)。open [--keep]
  本机起收听(地址与日志落 ~/.local/state/pipe/),close <addr|pid> 关闭,view [机]
  看本机活动管道或跨机只读(room/pipe-live 流),to <id> 开管道并知会对方(取用行 = tailcat <addr>)。字节方向恒 = 本机收、对方发;本机 30 分钟超时自关,
  --keep 长 transport。共享规则(id、门控、信封)见 evo:agents skill(相对链 ../agents/)。契约单一真源 = ai-ccoe 仓 plugins/CONTRACT.md。
  Use when 要让对方实时往我这里发字节(日志尾随、进度流、实时输出)、开实时管道、看
  活动管道、跨机看管道在册时;触发词 pipes、管道、实时发、实时流、日志尾随、tailcat、
  open、close、addr。
---

# pipes - evo 实时字节域原语

**定位**:五原语的实时字节域:tailcat 实时管道。要对方持续往我这里发字节(日志、进度)时用;字节方向恒 = 本机收、对方发。共享面在 `../agents/references/`,本篇只持域面。

## 动词面

| 动词 | 义 |
| --- | --- |
| `view [机]` | 本机活动管道;带机 = 跨机只读(room/pipe-live 流) |
| `open [--keep]` | 本机起收听,回地址与日志位 |
| `close <addr\|pid>` | 关管道,地址作废 |
| `to <id> [--force]` | 开管道并知会对方 |

- 裸调用 = view,exit 0;全局旗标与文法见 `../agents/SKILL.md` 二节

## 语义

- 地址与日志落 `~/.local/state/pipe/`;本机管道 30 分钟超时自关,`open --keep` 长 transport
- DELIVER:域字段 addr,取用行 = `tailcat <addr>`;拒投自动代记(管道待达,地址已在手)
- 跨机 VIEW 走只读流 `room/pipe-live`(src、pid、opened,分钟级保留)
- Windows 端活性探测走 OpenProcess

## 坑

- 方向不可换:想让对方收你的字节,由对方 open、你被 to
- 长传输记得 `--keep`,或对端重连前先 close 旧地址
