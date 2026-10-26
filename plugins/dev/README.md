# dev

> project-evo 市场开发治理面插件:两 skill。客户端显示 `dev:<skill>`。

## skill 清单

| skill | 面 |
| --- | --- |
| dev-doc | 文档治理与静态检查薄壳(原 doc-gov 与 dev-lint 合一;知识面在插件 hook_rules):ADR 决策、REQ 登记、doc 注释契约、文档即代码、研究档案、工具链、md 静检、约束术语表、结构面与门禁接线 |
| dev-cli | Agent 原生友好开发薄壳(知识面在插件 hook_rules):--llms 手册面、类型化 CTA 协议、命令自省、发现通道与 token 经济学(原 doc-cli 改名) |

插件级资产:scripts(md-guard、mdrules、termrules、term-lint、term-mine、lint-hook)加 hooks(双 bun 注入加载器 intent-guidance/dev-rules,批 176)加 hook_rules(意图件六加路径件四)加 tools(四结构模板 toml)。PostToolUse 禁令不破(批 105/174 裁撤;注入面只挂 UserPromptSubmit 与 PreToolUse)。

结构沿革:由原 evo-doc 与 evo-lint 两插件域合成;中文面 zh-lint 经拆出后于批 145 删除(ADR-0025);批 175 doc-gov 与 dev-lint 合一 dev-doc、语言面退 git 史、术语表 lint 立 PE-13(ADR-0026);批 176 知识面翻 hook_rules 薄壳指针(ADR-0027)。

## 前置

- skill 本体纯 Markdown;门禁脚本需 uv
- md 禁字与术语表挡板走仓 githooks pre-commit(md-guard.py 与 term-lint.py 的 --staged);注入面需 bun(加载器 .ts 直跑)

## 安装

Claude Code:

```text
/plugin marketplace add raystyle/project-evo
/plugin install dev@project-evo
```

Codex:`codex plugin marketplace add raystyle/project-evo` 后 `codex plugin add dev@project-evo`

Grok:`grok plugin install dev@project-evo --trust`

Kimi:无市场,拷 `plugins/dev/skills/*` 与 `plugins/dev/hook_rules/*`(壳指路直读)至 `~/.kimi/skills`

## 翻台与清理（重载铁律）

- **旧进程 = 旧技能**:装/更新插件后必须翻台才生效,恒 `agents reload <id>`(同格同 session 重进)
- 全端序:每端 `/plugin marketplace update project-evo` 再到 卸旧插件(evo-doc、evo-herdr、evo-distil、evo-lint、evo-agent 五件)再到 装 dev 与 evo 再到 全格 `agents reload`
- Kimi 端:清 `~/.kimi/skills` 旧目录(含 doc-gov、dev-lint)后重拷,重启会话

当前发布:0.18.0。
