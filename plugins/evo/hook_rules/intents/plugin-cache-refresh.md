---
patterns: [插件更新, 更新插件, marketplace update, plugin update, 缓存不刷, 旧文, 同版本, 重装]
---

## 插件更新坑判例(同版本内容修正)

- 同版本内容修正(版本号未动的 content fix)Claude 端 `plugin update` 不刷缓存;且 **marketplace 快照本身也可能陈旧**——光删插件缓存目录重装仍得旧文
- 正序三步:`/plugin marketplace update project-evo` 先 -> 删 `~/.claude/plugins/cache/project-evo/<插件>/<版本>` -> `/plugin install <插件>@project-evo`;三步齐才得新文(2026-10-26 五端实录:linux/ubuntu/win 三端踩全坑翻过来,pve/mac 第一轮即对)
- 验收锚:抽验 description 首句新旧文即可判缓存新鲜度(不重读全树)
- 更新后翻台重载恒 `agents reload <id>`(旧进程 = 旧技能)
- 判例来源:批 176 续 78a45c6 distil 壳 description 修正五端拉齐战役,总台编排回执
