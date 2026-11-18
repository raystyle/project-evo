---
name: pipes
description: >-
  实时字节域原语:管道收发与转发。ls 列管道面,start 起收听管道常驻至
  close,close 停管道,send 连对方管道 stdin 字节直通。
  Use when: pipe, byte stream, live bytes, 管道、字节流、实时字节、
  转发日志流、连管道。
  不要用于留痕知会(走 streams send)或写完的文件(走 shares)。
---

# pipes 实时字节域(prim v5 五入口)

- `ls [host]`(管道面清单);`start`(起收听管道,常驻至 close;原 open 更名);`close <地址或pid>`(杀进程收档广播);`send <addr>`(连对方管道,stdin 直通:字节写,非消息留痕)
- 语义澄清(2026-11-18):send = 字节写;留痕知会道归 `streams send`,不在本域
- 典型形:`cat x.log | pipes send tcADDR`(把本地日志字节流灌进对方管道);`pipes start` 起本机收听
- 沿革:carry 域退役(2026-11-16);pipes 直入五入口(2026-11-18,原 carry 域显式道)
- 旗标全集以 `pipes --llms` 为准
