---
name: dev-lint
description: >-
  开发治理静态检查三合一:md 面、语言面、结构面、中文面与门禁接线。md 面 = skill/agents/
  claude markdown 五面静检(frontmatter 官方字段、name 同目录名、description 形态与上限、
  行数上限、禁字四类、断链扫描);语言面 = cargo fmt 与 clippy 加 missing_docs、ruff 含
  D 系 docstring、tsc 与 eslint;结构面 = 类型化项目结构标准(四类型模板卡与声明式规则件,
  init 脚手架加结构 check);中文面 = 简明技术中文 STC 静检(禁用词、选词表、句长机检)
  与汇报面(结论先行、状态词、五模板);门禁三态退出码、提交挡板 pre-commit 与写后自动
  静检 hook 双端。
  Use when 给项目配静态检查门禁、排查 md 或代码静检报错、把 lint 挂进 pre-commit 或 CI、
  新仓脚手架或存量仓结构 lint、写改中文技术文档要无歧义、写汇报或回执时;触发词
  dev-lint、lint、静态检查、静态分析、禁字、断链、clippy、ruff、tsc、eslint、fmt、
  missing_docs、docstring 检查、门禁、退出码、pre-commit、md-guard、结构、脚手架、
  scaffold、目录树、ls-lint、md-lint、zh-lint、简明技术中文、STC、受控中文、句长、
  技术写作、汇报、回执、结论先行。
---

# dev-lint - dev 静态检查三合一（md、语言、结构、中文）

**渐进知识库型 skill**:本文件只做意图路由与纪律速览,四类细则在 `references/` 八篇,按需定点读。原 md-lint、ls-lint、zh-lint 三 skill 合并而来(ADR-0025 市场重构续令)。

## 一、意图路由

| 我要… | 看哪篇 |
| --- | --- |
| md 三面(skill markdown、agents markdown、claude markdown)静检:格式标准、长度限制、禁字、断链、结构 | `references/md-faces.md` |
| rs、py、ts 三语言静检:cargo fmt 与 clippy、ruff 与 D 系、tsc 与 eslint | `references/lang-checks.md` |
| 写后自动静检 hook:Edit/Write 落盘按后缀即查,报错信息回传(Claude Code 与 Codex 双端) | `references/hook-face.md` |
| 看四类型标准结构卡(TS CLI、知识三层、worker 服务、Python 工具) | `references/ls-types.md` |
| 新仓脚手架 init 或存量仓结构 check:声明式规则件(toml)与豁免登记 | `references/ls-rules.md` |
| 结构判定触发用例与边界(脚手架或咨询分流) | `references/ls-evals.md` |
| 简明技术中文四十条与判例(禁用词、选词、句长) | `references/zh-stc-rules.md` |
| 汇报面:结构律、状态词十词表、验证状态、五模板、发前自检 | `references/zh-reporting.md` |

工具:`scripts/zh-lint.py`(PEP 723 零依赖,内置先验核,`--wordlist` 外接上游词表,只报不改);结构模板 `templates/*.toml` 四类型。

## 二、三面速览

- **md 面**:静态检查是可判定的报错面,不是风格建议;判定取进程退出码,不接吞退出码管道;禁字四类与断链零容忍,豁免走环境变量登记(PEVO_*_ALLOW)不手改生成物
- **语言面**:rs = cargo fmt --check 加 clippy -D warnings 加 missing_docs deny;py = ruff 含 D 系 docstring 纪律按仓 ignore 裁剪;ts = tsc --noEmit 加 eslint 随仓配置
- **结构面**:按项目类型(TS CLI 仓、知识三层聚合仓、worker 服务仓、Python 工具仓)做初始脚手架与声明式结构比对;每仓豁免与本地覆盖登记在册;三层聚合类型联动 distil 建仓
- **中文面**:技术文档与 AI 解释性回答的受控中文,目标 = 读者读一遍就不会读错;与 md 面分工 = md 管格式与禁字与断链,中文面管语言清晰度

## 三、门禁与挡板

- 门禁三态退出码(0 过、1 业务、2 用法);提交挡板 pre-commit 挂 md-guard --staged 与断链扫描;写后静检 hook 双端(hook 段名 dev file-check)
- 限额可裁:AGENTS/CLAUDE/SKILL 行数上限走环境变量(见 references/hook-face.md)
