---
name: research
description: >-
  资料检索管线:把发现、获取、研读做成一条可复用管线。发现用 gh 搜代码与仓库、browse 驾浏览器搜
  Google 与 Medium、site: 检索查 X;获取用 aria2c 下论文 PDF、官方种子文件与大资产;研读用 reader 抽 PDF/EPUB。
  先确认浏览器态、不动宿主机浏览器、HTTP 优先、研究优先隔离态。轻量结论落目标项目 docs/research/SNNN 标六态。
  Use when 搜索论文、arxiv、google、medium、X/twitter、GitHub 代码、电子书、种子 torrent、aria2c 下载、调研、文献检索。
compatibility: 需本机 PATH 上的 gh、reader、aria2c、browse(可选;全平台命令分发安装由宿主工具链 omc 与 ark 统一维护)
---

# research - 资料检索管线

本文件只做**意图路由 + 管线速览**。命令细节在 `references/`。落盘两分:轻量结论写目标项目 `docs/research/SNNN` 并标六态;需要正式成文的深度分析按 doc-gov 投影纪律成文(ADR-0015 起本插件不再带 report skill)。文档体系与骨架知识在 `evo-adr:doc-gov` 与 `evo-adr:code-kit`,本技能不替代。

## 一、意图路由

| 你要做的事 | 入口 |
| --- | --- |
| 整条调研怎么串 | `references/pipeline.md` |
| 搜 GitHub 代码/仓库 | `references/gh.md` |
| 搜 Google / Medium、抓网页 | `references/web.md` |
| 查 X 帖(Google site: 与公开帖锚点) | `references/x.md` |
| 读 PDF / EPUB / 电子书 | `references/reader.md` |
| 下论文、大文件、种子 | `references/aria2c.md` |
| clone 外来仓深读 | `references/git.md` |
| 检索结论需要正式成文 | 按 doc-gov 投影纪律成文落 `docs/research/`(本插件不替代) |

## 二、管线(发现到研读)

```text
发现  gh search / browse Google 腿 / aria2c arxiv API
获取  aria2c(HTTP PDF、官方 .torrent);git clone 仅在要深读源码时
研读  reader extract/search/query;扫描页加 --ocr
落盘  轻量:目标项目 docs/research/SNNN 标六态;成文:按 doc-gov 投影纪律出 md
```

硬规则(用户 2026-09-23 裁定,替代 2026-09-08 bh 时代口径;S001 仅作历史):

- **先确认浏览器态**:任何浏览动作前 `browse status`,看 daemon 宿主、引擎来源(attached/managed-spawn/isolated-spawn)与活动 tab;跨宿主告警看清再动。[实证: 2026-09-23 status 显示 daemon 在 windows/AI-LAB、引擎 managed-spawn]
- **不动宿主机浏览器**(用户 2026-09-23 裁定):不 `browse up/down` 默认实例,不附着用户 Chrome 做写操作;浏览器腿只读导航加 `--new-tab`。[实证: 2026-09-23 fetch 升级腿杀宿主机引擎 47312 换 20208,用户裁定入硬规则]
- **研究优先隔离态**:必须起引擎时 `BROWSE_NAME=<名> browse up --headless --isolated`(隔离 profile 退出即删,命名实例派生端口 9900-9999);本机无 Chrome 如实报缺,不用宿主机引擎顶上。[实证: 2026-09-23 命名实例 up,Linux 侧报「找不到 chrome」]
- **HTTP 优先**:能直链就 `aria2c` 或 curl;`browse fetch` 是 HTTP 直取优先但正文稀薄会升级引擎腿(换引擎),宿主机引擎在用时禁手,改走 curl/aria2c。[实证: 2026-09-23]
- **X 无本地库通道**:`bh x-intel` 本地收割库随 bh 退役;X 检索走 Google `site:x.com` 加公开帖锚点,x.com 登录墙不绕。[实证: 2026-09-23 web.md 重写]
- **种子只下官方种子文件或 metadata**,ISO 等大体量须用户明确要求再下
- 登录墙停下问用户,不代点同意/允许

## 三、最小命令面

```powershell
gh search repos "pdf extraction rust" --limit 10 --json fullName,stargazersCount,updatedAt
gh search code "<kw>" --repo <o/r> --json path,repository,sha,url
browse status                                          # 先确认浏览器态(硬规则 1)
browse fetch 'https://www.google.com/search?q=site:arxiv.org+<题>&hl=en&gl=us&num=10'
browse --new-tab 'goto("https://www.google.com/search?q=<题>&hl=en&gl=us&num=10", {waitIdle: true}); return await pageEval("JSON.stringify(Array.from(document.querySelectorAll(\"a h3\")).slice(0,5).map(h => ({t: h.innerText, u: h.closest(\"a\").href})))")'
aria2c -x 8 -s 8 -c -d <dir> -o <name>.pdf "https://arxiv.org/pdf/<id>"
reader extract <pdf> --pages 1-2
```

论文 PDF 直链形态:`https://arxiv.org/pdf/<id>`(Google 命中若是 `/html/` 把路径改 `/pdf/`)。

细节与坑见对应 reference;过程实证见仓内 `docs/research/S001-bh与reader使用过程技巧.md`。
