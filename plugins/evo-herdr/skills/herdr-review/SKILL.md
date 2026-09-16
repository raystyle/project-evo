---
name: herdr-review
description: >-
  推送前评审闸门工作流:交付批经 herdr 窗格里的 codex 评审会话对齐后才推 main。
  评审请求模板(批次与基线、提交清单、改动面逐条、背景与已验证据、门禁语句)、
  回执三态(F 必修/G 建议/CONFIRM,逐条修复对照,采纳评审方实证)、
  轮次循环(修订回执、二轮快核至终审放行)、发现核实(逐条核实再修、修复本身过复核、多 agent 交叉互补)、
  评审窗格挂位与命名、窗格查看与对话历史检索。
  Use when 评审请求、推送前门禁、codex review、对线回执、评审轮次、终审放行、看窗格收评审时。
compatibility: 需 herdr 管理的评审窗格(codex 常驻会话)与 PATH 上的 hst;派单协议面见同插件 herdr-flywheel(全平台命令分发由宿主工具链 omc 与 ark 统一维护)
---

# herdr-review - 推送前评审闸门工作流

> 沉淀自 hst_rs 等工位实证(2026-08-31 至 09-16 六轮:整文件 review 十五条发现、五轮交叉复核链、D46 至 D53 推送前门禁请求与回执):**交付批经 herdr 右侧 codex 评审会话对齐后推 main**。派单、回执、断言、吸收四步协议的唯一权威源在同插件 `herdr-flywheel`;本 skill 是评审闸门的特化工作流,不复述派单命令细节。

## 一、形态

- 评审会话 = herdr 窗格里的常驻 codex,用户级 cwd 跨仓收件(同一评审格先后收 hst_rs、ark_rs、OfficeCLI、oxvg 的评审) [实证: hst trace 会话史 2026-09-14/16]
- 挂位 = 工位 tab 内右侧格,与开发格同 tab 同屏;命名评审格(如 hst-codex-review),live 名可作派单地址,仍以 herdr agent list 实查为准 [实证: 2026-09-16 agent list 见 wT:p2 命名格]
- 带起 = 检测到自愈:查工位格右侧有无可用格(neighbor),无则右分建格起 codex,有则直接对话;全流程命令实证见 `references/panes.md` 第二节
- 两种规模:**快核**(单提交或小批,评审请求直发会话)与**全量 code review**(整文件集,走任务协议:委派即产物落任务目录,收件人模式收件)

## 二、工作流(请求 到 放行)

```text
评审请求(批次/基线/改动面/证据/门禁语句)
到 codex 评审(逐行核 diff,产出发现)
到 回执三态(F 必修 / G 建议 / CONFIRM)
到 工位修复并回执(逐条对照,采纳评审方实证)
到 二轮快核(修复本身也过复核)
到 终审放行后推 main
```

纪律:达成一致前不推 main;AI review 的发现逐条核实再修(高严重度也可能部分真);每轮修复可能引入新缺陷,轮次到 CONFIRM 为止。

## 三、命令面(本节命令本会话实证可跑)

```bash
herdr agent list                                   # 实查评审格(命名、pane_id、状态、cwd)
herdr pane list                                    # 全窗格布局(评审格与开发格同 tab 关系)
herdr pane read <pane_id>                          # 直接看某窗格输出
hst trace sessions --project <仓路径>               # 该仓各 agent 会话史
hst trace search "review" --agent codex --project <仓路径>   # 按正则检索评审对话
```

派单与收件走 `herdr agent prompt` / `herdr agent read`,命令细节与坑见同插件 herdr-flywheel(唯一权威源,活权威 `herdr --skill`)。

## 四、意图路由

| 你要做的事 | 入口 |
| --- | --- |
| 发一份评审请求 | `references/request.md`(模板与实例) |
| 写回执 / 修订回执 / 快核 | `references/receipt.md`(三态与轮次) |
| 核实评审发现 / 分级处置 / 交叉复核 | `references/findings.md` |
| 评审窗格检测右侧、无格建格起 codex、有格直接对话、怎么查看 | `references/panes.md` |
| 派单/收件/断言/吸收协议面 | 同插件 skill `evo-herdr:herdr-flywheel` |
