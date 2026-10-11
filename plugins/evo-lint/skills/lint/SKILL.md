---
name: lint
description: >-
  项目静态检查报错:skill markdown、agents markdown、claude markdown、Rust、Python、TypeScript
  五面静检的命令、判据与门禁接线。md 面(skill 格式标准:frontmatter 官方字段、name 同目录名、
  description 形态与上限、行数上限;agents 与 claude markdown 长度限制与结构合同;禁字四类;
  断链扫描)、rs 面(cargo fmt --check 加 clippy -D warnings 加 missing_docs deny)、py 面
  (ruff 含 D 系 docstring 纪律与按仓 ignore 裁剪)、ts 面(tsc --noEmit 加 eslint 随仓配置);
  门禁三态退出码与提交挡板 pre-commit 挂接。
  Use when 给项目配静态检查门禁、排查 md 或代码静检报错、把 lint 挂进 pre-commit 或 CI、
  修禁字断链 clippy ruff tsc 红时;触发词 lint、静态检查、静态分析、禁字、断链、clippy、
  ruff、tsc、eslint、fmt、missing_docs、docstring 检查、门禁、退出码、pre-commit、md-guard。
---

# lint - evo-lint 项目静态检查报错

**渐进知识库型 skill**:本文件只做意图路由与纪律速览,五面细则在 `references/` 两篇,按需定点读。

核心思想:**静态检查是可判定的报错面,不是风格建议**。每面给命令、退出码判据、常见报错修法;判定纪律沿市场技能 `evo-distil:distil-skill` 族(gate-verdict 判例):判定取进程退出码,不接吞退出码管道,报错逐条修不豁免凑绿。

## 一、意图路由

| 意图 / 你要做的事 | 参考 |
| --- | --- |
| md 三面(skill markdown、agents markdown、claude markdown)静检:格式标准、长度限制、禁字、断链、结构 | `references/md-faces.md` |
| rs、py、ts 三语言静检:cargo fmt 与 clippy、ruff 与 D 系、tsc 与 eslint | `references/lang-checks.md` |
| 写后自动静检 hook:Edit/Write 落盘按后缀即查,报错信息回传(Claude Code 与 Codex 双端) | `references/hook-face.md` |
| 门禁接线与 pre-commit 挂接 | 两篇末节互补,三态退出码纪律见下 |

## 二、五面速览

| 面 | 主命令(以本机 --help 实查为准) | 判据 |
| --- | --- | --- |
| skill markdown | 断链扫描 + 格式标准核(frontmatter 仅官方字段、name 同目录名、description 做什么加何时用且不超限、行数上限) | 断链 0、spec 形合规 |
| agents / claude markdown | 禁字扫描(--staged 形)+ 结构合同 + **长度限制**(行数上限,仓可裁登记) | 禁字 0、结构齐、行数在限 |
| rs | `cargo fmt --check`;`cargo clippy -- -D warnings` | 退出码 0;missing_docs 按仓 deny |
| py | `ruff check .`(select 按仓裁剪,E/F/W/I/B/UP 起步,D 系为 docstring 纪律) | 退出码 0 |
| ts | `tsc --noEmit`;eslint 随仓配置 | 退出码 0 |

## 三、hook 面:写后自动静检

- 插件带 PostToolUse hook:Edit/Write/MultiEdit 落盘后按后缀自动静检(.md 禁字与长度、.py ruff、.rs rustfmt、.ts eslint),报错信息回传给 agent 逐条修
- **快检查通道**:秒级为界,重检查(clippy 全量、tsc 全量、断链全树)进门禁与 CI;工具缺位放行(分发归 omc 与 ark,只认 PATH)
- 双端:Claude Code 直查;Codex 的 apply_patch 载荷无 file_path 宽容放行,靠 pre-commit 兜底
- 限额可裁:AGENTS/CLAUDE/SKILL 行数上限走环境变量(见 references/hook-face.md)

## 四、纪律速览

- **退出码三态**:0 过、非 0 败、缺工具按仓裁定(装或记不适用);判定命令一律 `cmd > log 2>&1; echo $?` 形,禁尾管吞红
- **提交挡板**:pre-commit 挂静态检查,红不进库;门禁清单固定成文于 AGENTS 或 README(命令原文加退出码口径)
- **逐条修不凑绿**:豁免要留因由注释与范围(行级或文件级),整目录豁免须登记在册
- 命令面以本机 `cargo --help`、`ruff --help`、`tsc --help` 实查为准,参数随版本演进不写死
