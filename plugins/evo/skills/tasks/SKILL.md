---
name: tasks
description: >-
  tasks 原语(prim v3 持久任务域):hst task 全局遥控(引擎 hst;goal 命令族已正名
  task)。set <id> <文本> 设别的格所在项目的持久任务(本地直设;远机零 ssh = pending
  流加 apply 受体),to <id> <文本> 定向委派(= set 加事件入 tasks/shared 加信封 v2
  知会,取用行 = cd <cwd> && hst task show),view 看 tasks/shared 最近事件。id 文法、
  门控 v2、信封 v2 等共享面在 evo:agents skill(相对链 ../agents/)。契约单一真源 =
  ai-ccoe 仓 plugins/CONTRACT.md。
  Use when 要设别的格所在项目的持久任务、跨机委派目标、查任务事件流时;触发词 tasks、
  持久任务、任务、goal、委派目标、设任务、task set、事件流。
---

# tasks - evo 持久任务域原语

**定位**:五原语的持久任务域:hst task 全局遥控,引擎 hst。给别的格(或本机格)所在项目钉持久任务,事件入流全舰队可见。共享面(id 三产生式、门控 v2、信封 v2、status 四态、差异表)在 `../agents/references/`,本篇只持域面。

## 动词面

| 动词 | 义 |
| --- | --- |
| `view` | tasks/shared 最近事件(当前实装忽略参数) |
| `set <id> <文本>` | 设目标格 cwd 的持久任务 |
| `to <id> <文本> [--force]` | 定向委派 = set 加事件加信封知会 |

- 裸调用 = view,exit 0;全局旗标与文法见 `../agents/SKILL.md` 二节

## 语义

- 底座 = hst task(hst v2.12.0 起 goal 命令族正名 task;旧 goal 面仅作回退)
- 本地直设;**远机零 ssh**:pending 流 `tasks/pending/<机>` 加 apply 受体唤醒(herdr plugin action)
- 事件流:每次 set 追加事件行入 `tasks/shared`(ts、node、cwd、by、task)
- DELIVER:域字段 cwd,取用行 = `cd <cwd> && hst task show`;拒投自动代记(任务文本待设)

## 坑

- 取用行是 `hst task show`,别再写 `hst goal show`(正名后旧面只作回退)
- 任务设在目标格 cwd 上:目标格换目录后任务仍指原仓,以取用行 cwd 为准
