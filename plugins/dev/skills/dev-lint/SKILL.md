---
name: dev-lint
description: >-
  开发治理静态检查(md、语言、结构三面)与门禁接线。md 面 = skill/agents/claude markdown
  五面静检;语言面 = cargo fmt 与 clippy 加 missing_docs、ruff、tsc 与 eslint;
  结构面 = 四类型模板卡与声明式规则件;门禁三态退出码与 pre-commit 挡板。
  Use when: lint gate, 配静态检查门禁、把 lint 挂进 pre-commit 或 CI、
  新仓脚手架或存量仓结构 lint 时;触发词 dev-lint、lint、静态检查、禁字、断链、clippy、
  ruff、tsc、eslint、fmt、missing_docs、docstring、门禁、pre-commit、md-guard、
  脚手架、ls-lint、md-lint。
  不要用于运行时行为验证或业务逻辑调试。
---

# dev-lint - dev 静态检查（md、语言、结构）

**渐进知识库型 skill**:本文件只做意图路由与纪律速览,细则在 `references/` 六篇,按需定点读。原 md-lint、ls-lint 合并而来(ADR-0025 市场重构续令;中文面 zh-lint 经拆出后于批 145 删除,中文语言纪律不设 skill 面)。

## 一、意图路由

| 我要… | 看哪篇 |
| --- | --- |
| md 三面(skill markdown、agents markdown、claude markdown)静检:格式标准、长度限制、禁字、断链、结构 | `references/md-faces.md` |
| rs、py、ts 三语言静检:cargo fmt 与 clippy、ruff 与 D 系、tsc 与 eslint | `references/lang-checks.md` |
| 写后自动静检 hook:Edit/Write 落盘按后缀即查,报错信息回传(Claude Code 与 Codex 双端) | `references/hook-face.md` |
| 看四类型标准结构卡(TS CLI、知识三层、worker 服务、Python 工具) | `references/ls-types.md` |
| 新仓脚手架 init 或存量仓结构 check:声明式规则件(toml)与豁免登记 | `references/ls-rules.md` |
| 结构判定触发用例与边界(脚手架或咨询分流) | `references/ls-evals.md` |

结构模板 `templates/*.toml` 四类型。

## 二、三面速览

- **md 面**:静态检查是可判定的报错面,不是风格建议;判定取进程退出码,不接吞退出码管道;禁字四类与断链零容忍,豁免走环境变量登记(PEVO_*_ALLOW)不手改生成物
- **语言面**:rs = cargo fmt --check 加 clippy -D warnings 加 missing_docs deny;py = ruff 含 D 系 docstring 纪律按仓 ignore 裁剪;ts = tsc --noEmit 加 eslint 随仓配置
- **结构面**:按项目类型(TS CLI 仓、知识三层聚合仓、worker 服务仓、Python 工具仓)做初始脚手架与声明式结构比对;每仓豁免与本地覆盖登记在册;三层聚合类型联动 distil 建仓

## 三、门禁与挡板

- 门禁三态退出码(0 过、1 业务、2 用法);提交挡板 pre-commit 挂 md-guard --staged 与断链扫描;写后静检 hook 双端(hook 段名 dev file-check)
- 限额可裁:AGENTS/CLAUDE/SKILL 行数上限走环境变量(见 references/hook-face.md)
