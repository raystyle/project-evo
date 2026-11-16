---
patterns: [传文件, 取文件, 发文件, send the file, attach, fetch a share key, shares, share key, 上架, 取回]
---

## shares 文件域操作指导(prim v5)

- `put <path>` 推送上架回内容哈希键(键形 share/<机>/<hash>/<名>);`get <键> [-o|--output 名]` 取回落盘(默认落当前目录按键尾名);`view` 本机搬运面清点(share/ 前缀)
- `to <id> <文件> [--force]` = 上架加门控知会一道(先上架再判 blocked,文件已在,人可取);拒投不丢件:目标门控拒收时代记,收方自取
- 退役注记(prim v5 六入口定形):实时字节域(pipes)与端口映射域(ports)随 carry 退役;还在长的日志走 `streams room <房> <消息> --file <文件> [--lines N:M]` 切片
- 不要用于:只发一条消息(走 agents/streams)
