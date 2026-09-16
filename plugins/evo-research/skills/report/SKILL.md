---
name: report
description: >-
  研究成文与三件套产出:把研究成果写成正式报告。断言式标题与题名区骨架(编制/日期/分类/来源/摘要/关键词)、
  编号章节、附录信源清单与断言证据对照;Markdown 唯一真源,固定产出 md/pdf/docx 三件套,缺一不算完成;
  PDF 由 Typst(cmarker)渲染,附零依赖 render.py(支持 --check 编译门禁与加粗标签 lint);
  版式复检口径、信源分级存档与完成登记。触发后先读本文件「意图路由」。
  Use when 写研究报告、把调研成文、出正式报告、渲染 PDF、报告三件套、版式复检、信源存档登记时。
compatibility: 需 PATH 上的 typst(全平台命令分发安装由宿主工具链 omc 与 ark 统一维护;或 TYPST 环境变量、--typst 显式指定)与本侧 CJK 字体(Linux 面缺则静默丢中文字,装如 fonts-noto-cjk);脚本 PEP 723 零依赖(>=3.12)。
---

# report - 研究成文与三件套

**成文型 skill**:模板在 `assets/templates/report.md`(骨架)与 `assets/templates/report.typ`(渲染),渲染脚本 `scripts/render.py` 是交付物,本文件是它的用法面;写作规范、管线、版式、信源细节在 `references/`。检索与获取管线在同插件 research。

## 一、意图路由

| 你要做的事 | 入口 |
| --- | --- |
| 开写一篇新报告 | `references/skeleton.md` + 复制 `assets/templates/report.md` 起步 |
| 渲染 PDF / 编译门禁 | 本文件「二、命令」 + `references/triple-output.md` |
| 出 Word(docx) | `references/triple-output.md` 第四节(管线知识面) |
| 版式复检 | `references/layout-check.md` |
| 信源分级 / 原件存档 / 完成登记 | `references/sources-and-index.md` |
| 找论文、搜网页、下载原件 | 同插件 skill `evo-research:research` |
| 轻量结论落 docs/research | 同市场 skill `evo-adr:doc-gov`(flow-archive 口径) |

## 二、命令(本节命令本会话实证可跑)

```bash
# 渲染:生成同名 PDF(md 是唯一真源,生成物禁手改)
uv run <skill>/scripts/render.py <报告.md>

# 编译门禁:渲到临时目录只校验,不覆盖正式产物(退出码 0/非 0 可接 CI)
uv run <skill>/scripts/render.py <报告.md> --check
```

- typst 定位三选一:PATH(默认)、`TYPST=<路径>` 环境变量、`--typst <路径>` 显式指定;命令分发由宿主工具链 omc 与 ark 统一维护,本工具不内置安装路径
- 首次编译联网拉取 `@preview/cmarker` 包,之后走缓存
- lint 面:题头里 `**关键词:**内容` 形态会告警(加粗失效且星号印进 PDF),写成 `**关键词**:内容`

## 三、产出纪律

- 三件套 `reports/YYYY-MM-DD-短名.md` + 同名 `.pdf` + `.docx`,缺一不算完成;md 改动必重渲全部产物
- 版式复检按 `references/layout-check.md` 口径(逐页转图 + 行距度量),不靠猜
- 完成登记:INDEX 一行 + 日记钩子 + 立项状态流转

## 四、坑(实证)

- **报告须有二级标题**:模板以首个 `## ` 拆题头与正文,缺失时原家族模板会让 cmarker 报 Markdown must be a string(已修为空串兜底)
- **WSL 调 Windows typst.exe**:render.py 自动把路径参数转 Windows 形态;但 Windows exe 看不到 WSL 专属挂载,报告与根目录要放 Windows 盘路径(如 /mnt/d)一侧,或改用 Linux typst [实证: 2026-09-16 /mnt/d 样例 130 KB 渲染通过;评审轮五份真报告 306 至 420 KB 复跑全过]
- **Linux 面缺 CJK 字体会静默丢中文字**:typst 未知字体只告警不失败,退出码仍 0,产物文本层只剩 ASCII [实证: 评审轮最小复现];装 CJK 字体(如 fonts-noto-cjk)再渲,render.py 检测到未知字体告警会显式提示
- **PDF 同步校验比文本不比哈希**:typst 内嵌时间戳,同一 md 两次渲染哈希必不同

安装通道:Claude Code `/plugin marketplace add raystyle/project-evo` 后装 evo-research 插件;Codex `codex plugin marketplace add raystyle/project-evo`;Grok `grok plugin install evo-research@project-evo --trust`;Kimi 无市场,拷 `skills/report/` 至 `~/.kimi/skills`(脚本可直跑)。
