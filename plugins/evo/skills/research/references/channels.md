# channels:四通道完整形与坑

> 每通道给实跑锚形与判定坑;页级选择器与域级配方活在 browse workspace(`browse workspace site <域名段>` / `browse workspace page <slug>`,`browse workspace update` 更新),本篇不重抄。

## gh 面（GitHub API 通道）

五动词,机读优先 `--json`:

```bash
gh search repos "claude code plugin marketplace" --limit 3 --sort stars --json fullName,stargazersCount,description
gh search code "skill_description_violations" --language python --limit 3
gh search issues "plugin marketplace" --repo anthropics/claude-code --limit 3
gh search prs "skills" --repo anthropics/claude-code --limit 3
gh search commits --repo anthropics/claude-code "skills" --limit 3
```

- 常用旗标:`--limit`(缺省 30)、`--json <字段>`、`--sort`、`--repo`、`--language`、`--owner`;qualifier 直进查询串(如 `"topic:claude-code stars:>100"`)
- 排除 qualifier 带连字符时用 `--` 隔离:`gh search issues -- "query -label:bug"`
- 分野:已知 owner/repo 的元数据批采、README raw 走 gh;搜索面发现新仓 gh 也强,但 README 渲染后内容与 discussions、topics 页走 browse 引擎面
- `--web` 旗标开浏览器面,检索自动化里不用

## bing 面（网页主通道,唯一引擎）

fetch 直抓,零引擎成本,首击:

```bash
browse fetch 'https://www.bing.com/search?q=claude+code+plugin+marketplace' --markdown
```

- 实测 HTTP 200 直出全 SERP(结果在 `#b_results`,标题 `li.b_algo h2 a`);词间用 `+` 或 `%20`
- 翻页免点击:URL 追加 `&first=10`、`&first=20`;时间过滤 `&filters=ex1:"ez1"`(24 小时)等
- fetch 塌(空正文/墙页)再起无头引擎,方言抽取:

```bash
browse up --headless
browse rune <编排件.rn> --timeout 90
```

- 无头引擎 bing 实测即通;抽取锚 `#b_results > li.b_algo h2 a`,完整最小编排件见 `browse-rn.md`
- 引擎会话跨命令存活,批量检索循环放 shell 层,每页一条片段

## scholar 面（学术通道,fetch 直通）

```bash
browse fetch 'https://scholar.google.com/scholar?q=agent+skills+specification&hl=en' --markdown
```

- 实测直通:HTTP 200 满页 10 条,无挑战无验证码;锚点结果行 `#gs_res_ccl_mid .gs_r`、容器 `#gs_res_ccl`
- `&hl=en` 钉英文界面;年度过滤 `&as_ylo=2025`;排序 `&scisbd=1`(按日期);`&as_vis=1` 含引用
- 引用卡(`[PDF]`、`[CITATION]`、Cited by)在结果行内随行抽取
- 高频会触验证码:降频或换官方 API,别硬闯;scholar 与 google 主面风控独立,主面被挑战不影响本面

## github browse 面（网页渲染通道）

```bash
browse fetch 'https://github.com/anthropics/claude-code' --markdown
```

- 仓页、topics、README 渲染面 fetch 可直出(实测 200 大体);搜索结果页未登录态渲染不全,搜内容用 gh 面
- 深采逐仓限速约 8 秒/仓;批量走 gh API 建壳,引擎只跟进渲染面

## google 主搜索面（不在通道内）

- 易被挑战:本机实测 mech 判读 verdict=challenged(`/sorry` 页,IP 限流/反爬);网页检索一律走 bing
- 判读机与探针知识仍在 workspace(`browse workspace page google-search`),供重采集面参考;其 verdict 族 = ok / consent / challenged / empty / nav-stall / budget
