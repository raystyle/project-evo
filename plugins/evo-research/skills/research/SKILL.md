---
name: research
description: >-
  资料检索管线:把发现、获取、研读做成一条可复用管线。发现用 gh 搜代码与仓库、bh google-search / medium-search 搜网页与文章、
  bh x-intel search 查 X 本地库;获取用 aria2c 下论文 PDF、官方种子文件与大资产;研读用 reader 抽 PDF/EPUB。
  工位复用、HTTP 优先、研究优先无头。轻量结论落目标项目 docs/research/SNNN 标六态;正式报告成文走同插件 report。
  Use when 搜索论文、arxiv、google、medium、X/twitter、GitHub 代码、电子书、种子 torrent、aria2c 下载、调研、文献检索。
compatibility: 需本机 PATH 上的 gh、reader、aria2c、bh(可选);全平台命令分发安装由宿主工具链 omc 与 ark 统一维护
---

# research - 资料检索管线

本文件只做**意图路由 + 管线速览**。命令细节在 `references/`。落盘两分:轻量结论写目标项目 `docs/research/SNNN` 并标六态;深度分析成正式报告(md/pdf/docx 三件套)走同插件 skill `report`。文档体系与骨架知识在 `evo-adr:doc-gov` 与 `evo-adr:code-kit`,本技能不替代。

## 一、意图路由

| 你要做的事 | 入口 |
| --- | --- |
| 整条调研怎么串 | `references/pipeline.md` |
| 搜 GitHub 代码/仓库 | `references/gh.md` |
| 搜 Google / Medium、抓网页 | `references/web.md` |
| 查 X 帖(本地收割库) | `references/x.md` |
| 读 PDF / EPUB / 电子书 | `references/reader.md` |
| 下论文、大文件、种子 | `references/aria2c.md` |
| clone 外来仓深读 | `references/git.md` |
| 检索结论写成正式报告 | 同插件 skill `evo-research:report` |

## 二、管线(发现到研读)

```text
发现  gh search / bh google-search / bh medium-search / bh x-intel search
获取  aria2c(HTTP PDF、官方 .torrent);git clone 仅在要深读源码时
研读  reader extract/search/query;扫描页加 --ocr
落盘  轻量:目标项目 docs/research/SNNN 标六态;成文:同插件 report 出三件套
```

硬规则(用户 2026-09-08 裁定,S001 实证;0.6.0 无头增补):

- **研究优先无头**:`bh engine start` 自起隔离 Chrome(`--headless=new`,临时 profile,用完 `bh engine stop`)。不弹 Allow,不碰用户浏览器。[实证: 2026-09-08 engine start/fetch --engine/stop]
- **用户 Chrome 才工位复用**:已附着时钉 1 到 2 个 tab,`switch_tab`,禁止 `--new-tab` / 为自愈 `bh --restart`
- **HTTP 优先**:能直链就 `aria2c` 或 `bh web-fetch`;要 JS 且不碰用户面时用 `--engine`
- **X 不是现场 SERP**:`bh x-intel search` 查本地库;`bh x-search` 会被当成 JS 片段
- **种子只下官方种子文件或 metadata**,ISO 等大体量须用户明确要求再下
- 登录墙停下问用户,不代点 Chrome Allow

## 三、最小命令面

```powershell
gh search repos "pdf extraction rust" --limit 10 --json fullName,stargazersCount,updatedAt
gh search code "<kw>" --repo <o/r> --json path,repository,sha,url
bh engine start
bh web-fetch "https://example.org/" --text --engine
bh engine stop
bh google-search "site:arxiv.org <题>" --top 5
bh google-search pluck gs_search
bh medium-search "<题>" --top 5
bh medium-search pluck ms_search
bh x-intel search "<kw>" --limit 5
bh x-intel search --stats
aria2c -x 8 -s 8 -c -d <dir> -o <name>.pdf "https://arxiv.org/pdf/<id>"
aria2c -x 8 -s 8 -c -d <dir> -o name.torrent "https://releases.ubuntu.com/.../*.iso.torrent"
aria2c -S <file>.torrent
reader extract <pdf> --pages 1-2
```

论文 PDF 直链形态:`https://arxiv.org/pdf/<id>`(Google 命中若是 `/html/` 把路径改 `/pdf/`)。

细节与坑见对应 reference;过程实证见仓内 `docs/research/S001-bh与reader使用过程技巧.md`。
