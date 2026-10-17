---
name: research
description: >-
  检索域知识面:按研究目标路由通道,gh 搜 GitHub(API 面)、browse 搜 Bing(网页主通道,
  无头即通)与 scholar.google.com 学术面(fetch 直通)、rn 编排与油猴探针过重采集面。
  Use when: 调研某主题、找库选型、学术检索、跨源对照搜索、GitHub 找仓找码找 issue、
  要引擎采集或写采集编排时;触发词 research、检索、调研、搜索、找库、选型、学术、
  scholar、文献、找仓。
  不要用于检索结论的档案沉淀(走 dev:doc-gov 研究档案面)与 agent 消息操作(走 evo 原语域)。
---

# research - evo 检索域知识面

**渐进知识库型 skill**:本文件只做意图路由与通道速览;通道细节与判例在 `references/` 分类扁平目录,按「先路由、再读对应篇」渐进检索,不要求一次读完。

核心思想:**研究目标定通道,通道按成本递增**:fetch 直抓、无头引擎方言、rn 编排与油猴探针,三级递进(零引擎、单页、多页重采集)。网页检索主通道只有 bing;google 主搜索面易被挑战,不在通道内(判例 `references/rulings.md`)。产出是对照后的信源清单;结论断言与立档案走 `dev:doc-gov` 研究档案面(S 编号、六态)。

## 一、意图路由（按目标直达通道）

> 表未覆盖的目标:先想它是不是检索问题;是则按最接近行选通道,再查 `references/README.md` 索引。

| 目标 / 你要找的东西 | 通道与首击 |
| --- | --- |
| GitHub 仓选型、找码、issue、pr、commit | `gh search repos/code/issues/prs/commits`(API 面,机读;`references/channels.md`) |
| GitHub 网页面:discussions、topics、渲染 README | `browse fetch <url> --markdown`(零引擎;详情 `references/channels.md`) |
| 通用网页、技术调研、新闻面 | `browse fetch 'https://www.bing.com/search?q=<词>' --markdown`(唯一网页引擎;无头引擎形同篇) |
| 学术、文献、论文 | `browse fetch 'https://scholar.google.com/scholar?q=<词>&hl=en' --markdown`(直通实测;锚点抽取 `references/channels.md`) |
| 多页采集、批量关键词、重反爬面、Rune 语法疑问 | rn 编排 + 油猴探针(`references/browse-rn.md`、`references/probes.md`) |
| 页级/域级坑与选择器 | `browse workspace site <域名段>` / `browse workspace page <slug>`(活知识仓,git 更新) |

## 二、速览（每通道一条实跑锚形）

```bash
gh search repos "claude code plugin marketplace" --limit 3 --sort stars --json fullName,stargazersCount,description
gh search code "skill_description_violations" --language python --limit 3
browse fetch 'https://www.bing.com/search?q=rust+cdp' --markdown
browse fetch 'https://scholar.google.com/scholar?q=agent+skills&hl=en' --markdown
browse rune ~/.browse-rs/workspace/page-skills/google-search/mech.rn --vars 'q=rust cdp' --vars top=3 --timeout 180
```

> 锚形皆 2026-10-17 本机实跑过(B17);第五条是判读机消费例(挑战判读 verdict 族),自写最小编排完整件在 `references/browse-rn.md`。

## 三、硬规则

- 网页检索只用 bing,不设备胎;google 主搜索面 `/sorry` 挑战高发(实测 verdict=challenged),出现在结果里即弃走,不重试不硬闯
- 旗标全集不进本 skill:gh 以 `gh search --help` 自省,browse 以 `browse --llms` 自省;与手册冲突时改本 skill 不改命令
- 同一研究目标至少两源对照(如 gh 面 + bing 面),单源结论标注未对照;事实断言六态走 `dev:doc-gov`
- 写进本 skill 与 references 的命令形当会真跑过再写(ADR-0010);`--vars` 含空格必须整体引号(裂参退出 2)
- 引擎只在 fetch 塌(空正文/墙页)后起,缺省无头;探针只在结构高频漂移面装,稳定静态站用 `--js`
- 退出码三态判定:0 成功 / 1 执行失败 / 2 用法错;fetch 回执看 `via` 字段区分 http 与引擎

## 四、接着读

- `references/channels.md`:四通道完整形与坑,选通道或首击失败时
- `references/browse-rn.md`:rn 编排五律与裸形入口,写多页采集时
- `references/probes.md`:油猴探针骨架与装法,页面结构漂移采集失稳时
