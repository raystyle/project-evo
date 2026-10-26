---
patterns: [google 挑战, sorry 页, scholar 直通, bing 直出, 判例, 风控, 渲染等待, --vars 坑]
---

## research 检索判例指导

- google 主搜索面出路由:实测落 `/sorry` 挑战页,主通道定 bing,google 不进路由不设备胎,挑战即弃不重试
- scholar 与 google 主面风控独立:fetch 首击直出满页,学术通道零引擎直通
- bing fetch 零引擎直出(HTTP 200 全 SERP),引擎只在 fetch 塌后起;无头即通不需有头与 profile 养护
- SERP 渲染等待由 goto 默认提交等待覆盖,编排裸 sleep 退役(限速退避 sleep 保留)
- 敲法坑:`--vars` 值含空格须整体引号(否则 rune 退出 2);userscript install 路径按 CWD 解析用绝对径;管道跑 browse rune 的「stdin 为空串」提示是噪音不是错
