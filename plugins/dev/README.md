# dev

> project-evo 市场开发治理面插件:三 skill。客户端显示 `dev:<skill>`。

## skill 清单

| skill | 面 |
| --- | --- |
| doc-gov | 文档治理知识库:ADR 架构决策、REQ 需求登记、代码 doc 注释契约、文档即代码、研究档案、工具链范式 |
| dev-cli | Agent 原生友好开发:--llms 手册面、类型化 CTA 协议、命令自省、发现通道与 token 经济学(原 doc-cli 改名) |
| dev-lint | 静态检查三合一(原 md-lint、ls-lint、zh-lint):md 五面与 rs/py/ts 语言面、类型化结构 init 与 check(四类型模板)、简明技术中文与汇报面 |

插件级资产:scripts(md-guard.py 提交挡板、mdrules.py 禁字唯一权威、lint-hook.py 写后静检)与 hooks(PostToolUse,段名 dev file-check)。

结构沿革:由原 evo-doc 与 evo-lint 两插件域合成,lint 三 skill 并一 dev-lint(ADR-0025 市场重构续令)。

## 前置

- skill 本体纯 Markdown;写后静检 hook 需 uv
- md 禁字挡板走仓 githooks pre-commit(scripts/md-guard.py --staged)

## 安装

Claude Code:

```text
/plugin marketplace add raystyle/project-evo
/plugin install dev@project-evo
```

Codex:`codex plugin marketplace add raystyle/project-evo` 后 `codex plugin add dev@project-evo`

Grok:`grok plugin install dev@project-evo --trust`

Kimi:无市场,拷 `plugins/dev/skills/*` 至 `~/.kimi/skills`

当前发布:0.13.1。
