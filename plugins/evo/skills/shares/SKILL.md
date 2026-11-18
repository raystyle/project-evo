---
name: shares
description: >-
  文件域原语:交付或取回一份已写完的文件。ls 清点本机搬运面,
  put 推送上桌回内容哈希键,get 按键取回落盘,
  send 留痕加知会(入流 + hc send 一发)。
  Use when: send the file, attach, fetch a share key, 传文件、取文件、交付产物、
  上架、取回、搬运面清点。
  不要用于还在长的字节(走 pipes 或 streams --file 日志切片)
  或只发一条消息(走 streams send)。
---

# shares 文件域(prim v5 五入口)

- `ls`(本机搬运面清点,share/ 前缀);`put <path>` 推送上架回内容哈希键(键形 share/<机>/<hash>/<名>);`get <key> [到目录]` 取回落盘(默认落当前目录按键尾名);`send <id> <key>` 留痕加知会一道(入流 + hc send 一发;拒投不丢件,目标门控拒收时代记,收方自取)
- 示例:`shares put report.md`;`shares get 3fa9 report/`;`shares send node-a-claude-1 3fa9 交付评审`
- 动词沿革:ls 原 view、send 原 to(2026-11-18 动词对齐 hc,旧名不留别名)
- 还在长的日志走 `streams room <房> <消息> --file <文件> [--lines N:M]` 切片或 `pipes send` 字节道
- 旗标全集以 `shares --llms` 为准
