# browse - 浏览器驾驶 CLI 操作指南

> 定位:**搜索引擎与网页抓取**。现役入口是 `browse`(browse_rs,0.21.0,给 agent 的浏览器驾驶 CLI,方言片段驱动 clean-chrome,常驻 daemon 跨命令存活)。普通 HTTP 能拿到的页面用 curl/aria2c/`browse fetch`,不必开浏览器腿。

## 零、硬规则(用户 2026-09-23 裁定)

1. **先确认浏览器状态**:任何浏览动作前 `browse status`(或 `--json`),看 daemon 宿主、引擎来源(origin 枚举 attached/managed-spawn/isolated-spawn)与活动 tab;跨宿主(CLI 与 daemon 不同机)会有显式告警,看清再动。
2. **不动宿主机浏览器**:不 `browse up/down` 默认实例(会重启或下线用户正在用的引擎),不附着用户 Chrome 做写操作。宿主机引擎在用时,任何会"换新引擎"的面都禁手。
3. **`browse fetch` 升级腿禁手边界**:正文空、墙词、少于 20 词三条件会升级引擎腿,升级即换新引擎,宿主机附着态下这会杀掉用户浏览器 [实证: 2026-09-23 fetch example.org,引擎 47312 被杀换 20208]。宿主机引擎在用时,正文抓取改走 curl/aria2c;必须 browse 抓取时先确认引擎是 isolated-spawn 或征得用户同意。
4. **研究优先隔离态**:必须起引擎时用 `BROWSE_NAME=<名> browse up --headless --isolated`(隔离 profile 退出即删,命名实例派生端口 9900-9999 不碰默认实例);本机无 Chrome 时报「找不到 chrome」,不要用宿主机的引擎顶上 [实证: 2026-09-23 命名实例 up,Linux 侧无 Chrome 如实报缺]。
5. **只读导航开新 tab**:宿主机引擎上做浏览器腿,用 `browse --new-tab '<片段>'`,只读求值,导航前看清 status 的活动 tab。

## 一、搜索(Google)

零浏览器腿(HTTP 直取,2026-09-21 基线可用):

```bash
browse fetch 'https://www.google.com/search?q=rust+cdp&hl=en&gl=us&num=50'
```

- 参数:`hl=en&gl=us` 钉英文美区;`num=50` 拉条数;`site:` 与 `-` 运算符照常
- **退化留痕**:2026-09-23 本网络实测零浏览器腿只回 redirect 占位页("Please click here..."),拿不到结果;遇此走浏览器腿
- 注意 fetch 的升级腿边界(硬规则 3):正文稀薄也可能触发升级,宿主机引擎在用时别用这条腿赌

浏览器腿(实证 2026-09-23,5 条标题加 URL):

```bash
browse --new-tab 'goto("https://www.google.com/search?q=<q>&hl=en&gl=us&num=10", {waitIdle: true}); return await pageEval("JSON.stringify(Array.from(document.querySelectorAll(\"a h3\")).slice(0,5).map(h => ({t: h.innerText, u: h.closest(\"a\").href})))")'
```

- 翻页免点击:URL 改 `&start=10`、`&start=20`
- EU 类出口可能先弹 consent 同意墙:让用户点一次再继续
- 高频自动化会触 429/验证码:批量检索降频,别硬闯
- 站点知识下钻:`browse workspace site google`(fetch/goto 回执自动点名 domain_skills)

## 二、Medium

只读任务恒先 HTTP 通道;medium.com search 页 403/坏 JSON,**搜索走 Google `site:medium.com`**。

```bash
browse fetch 'https://medium.com/@karpathy/software-2-0-a64152b37c35?format=json'
```

- 2026-09-21 实测:回执 403 但正文仍是完整 JSON(别当失败),剥 XSSI 前缀 `])}while(1);</x>` 再解析
- 关键字段:`payload.value`(title/firstPublishedAt/uniqueSlug)、`virtuals`(totalClapCount/readingTime/wordCount)、正文 `content.bodyModel.paragraphs`
- RSS:profile/publication 的 `/feed` 拉最近文章;GraphQL `POST /_/graphql` 免认证(post(id:)/user(username:)),POST 走 pageEval 同源 fetch 或门外 curl
- 站点知识:`browse workspace site medium`

## 三、X(无本地库通道)

`bh x-intel` 的本地收割库随 bh 退役,browse 无等价物。**X 检索改走 Google `site:x.com`**;x.com 现场登录墙不绕(要凭据让用户自己输)。

公开帖与 Article 卡片恢复的锚点清点(匿名可渲染帖子本体):

```bash
browse --new-tab 'goto("https://x.com/<handle>/status/<id>", {waitIdle: true}); return await pageEval("JSON.stringify(Array.from(document.querySelectorAll(\"article a\")).map(a => ({text: (a.innerText || \"\").trim(), href: a.href})).filter(x => x.href))")'
```

- Article 卡内文匿名跳登录是常态,不是帖子私有的证据;跨发兜底见 `browse workspace site x`(LinkedIn 外链解 `url` 参数拿规范页)
- 一手源 = status 页与作者自控规范页;恢复不出就如实引公开 status 并标注正文不可达

## 四、网页正文抓取

```bash
browse fetch <url>              # 一次性只读,HTTP 直取优先
browse fetch <url> --markdown   # markdown 形
```

- 回执 `{via, title, text, upgradedFrom}`:`via: http` 零浏览器成本;`upgradedFrom` 非空即走了引擎腿(硬规则 3 的边界)
- 能 curl/aria2c 拿到的不要走 fetch:宿主机引擎在用时,fetch 是 last resort 且先 status

## 五、引擎生命周期(默认不动,要动先问)

```bash
browse status [--json]   # daemon/引擎/实例/活动 tab 概览,引擎来源语义面
browse up --headless --isolated   # 隔离态引擎(须本机有 Chrome;默认实例不要 up/down)
browse down              # 退 daemon;只终结自己 spawn 的引擎
```

- 形态记忆是 daemon 进程态:最近一次 up 的意图生效,重启回环境缺省
- 附着优先是发现序默认:裸 `browse '<片段>'` 可能附着到用户 Chrome(硬规则 2),研究任务不走这条默认路

## 六、账本与生态

- `browse --llms [--full|--json]`:agent 手册直出,机制细节唯一权威
- `browse snippets list/show`:片段库,先查库再写新片段
- `browse workspace list/site/page`:站点与页面机制知识(google/medium/x/github 域段)
- `browse issue new --acceptance <验收>`:缺陷开单(账本只增;先 --dry-run)

## 七、复验命令

```bash
browse --version      # 0.21.0
browse status --json  # 引擎来源与宿主上下文
```
