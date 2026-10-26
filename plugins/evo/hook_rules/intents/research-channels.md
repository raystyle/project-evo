---
patterns: [gh search, bing, browse fetch, SERP, 通道, 无头, headless, gh 面, 检索通道]
---

## research 四通道路由指导

- gh 面(GitHub API):`gh search repos/code/issues/prs/commits`,机读 `--json`;qualifier 直进查询串(如 `topic:claude-code stars:>100`);排除 qualifier 用 `--` 隔离;已知 owner/repo 的元数据与 README raw 走 gh
- bing 面(网页主通道,唯一引擎):`browse fetch 'https://www.bing.com/search?q=词+词' --markdown` 直抓 SERP;翻页 URL 加 `&first=10`;时间过滤 `&filters=ex1:"ez1"`;google 主搜索面易被挑战不在通道内
- fetch 塌(空正文/墙页)再起无头引擎方言抽取(`browse up --headless`);成本递增三级:fetch 零引擎 > 无头单页 > rn 编排多页
- scholar 面:`fetch` 直通 scholar.google.com
- 页级选择器与域级配方活在 browse workspace(`browse workspace site/page`),不重抄
