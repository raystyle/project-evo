# X 检索

> 本地收割库已随 bh 退役:`bh x-intel` 查本地 `x_tweets.db` 的通道不存在了(bh 时代库 1435 帖/666 作者,2026-09-08 实测,成历史)。现役 X 面走 Google `site:x.com` 与公开帖只读锚点,不碰现场收割。

## 命令

```bash
# 搜 X:走 Google(见 web.md 一)
browse --new-tab 'goto("https://www.google.com/search?q=site:x.com+<kw>&hl=en&gl=us&num=10", {waitIdle: true}); return await pageEval("JSON.stringify(Array.from(document.querySelectorAll(\"a h3\")).slice(0,5).map(h => ({t: h.innerText, u: h.closest(\"a\").href})))")'

# 公开帖锚点清点(匿名可渲染;见 web.md 三)
browse --new-tab 'goto("https://x.com/<handle>/status/<id>", {waitIdle: true}); return await pageEval("JSON.stringify(Array.from(document.querySelectorAll(\"article a\")).map(a => ({text: (a.innerText || \"\").trim(), href: a.href})).filter(x => x.href))")'
```

## 边界

- 不动宿主机浏览器是硬规则:先 `browse status`,浏览器腿只读导航加 `--new-tab`,不 up/down 默认实例 [用户裁定 2026-09-23]
- x.com 现场登录墙不绕:要凭据让用户自己输;Article 卡内文匿名跳登录是常态不是帖子私有的证据
- 一手源 = status 页与作者自控规范页(LinkedIn 外链解 `url` 参数拿规范页);评论区与搜索摘要只作旁证;恢复不出规范页就如实引公开 status 并标注正文不可达
- 现场收割(长驻抓推)不在本 skill 面:要做得用户明确要求并另开工位,不占宿主机引擎

## 与 Google / Medium

| | Google / Medium | X |
| --- | --- | --- |
| 命令 | `browse` fetch/goto 腿(web.md 一/二) | Google `site:x.com` 加公开帖锚点 |
| 对象 | 现场 SERP / 文章 JSON | 现场 SERP(本地库通道已退役) |
| 浏览器 | 硬规则约束下只读导航 | 同左 |
