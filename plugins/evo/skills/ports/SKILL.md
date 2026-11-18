---
name: ports
description: >-
  端口映射域原语:tailcat serve 面板端口与服务映射。ls 列映射面,
  start 起映射(端口表或服务侧映射或 all/exit-node),close 停映射,
  fwd 本地起听转发,send 留痕知会。
  Use when: port forward, port mapping, expose port, 端口映射、端口转发、
  起端口、开面板端口、服务映射。
  不要用于实时字节管道(走 pipes)或留痕消息(走 streams send)。
---

# ports 端口映射域(prim v5 五入口)

- `ls [host]`(映射面清单);`start <spec>`(起映射:8080,8443 端口表 / 5555:IP:5555 服务侧映射 / all / exit-node;原 open 更名);`close <地址或pid>`(停映射);`fwd <addr> <local>:<remote-port>`(本地起听转发,0 = 空口);`send <id> <spec>`(留痕知会:入流 + hc send 一发;原 to 更名)
- spec 形:纯端口 = serve 面板端口;`端口:IP:端口` = 服务侧映射(被服务端口,非客户端监听);`all` 全量;`exit-node` 出口节点
- 示例:`ports ls`;`ports start 8123`;`ports close tcADDR`;`ports fwd tcADDR 15555:5555`
- 沿革:carry 域退役(2026-11-16);ports 直入五入口(2026-11-18,原 carry 域显式道)
- 旗标全集以 `ports --llms` 为准
