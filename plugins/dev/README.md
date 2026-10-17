# dev

> project-evo 市场开发治理面插件:三 skill。客户端显示 `dev:<skill>`。

## skill 清单

| skill | 面 |
| --- | --- |
| doc-gov | 文档治理知识库:ADR 架构决策、REQ 需求登记、代码 doc 注释契约、文档即代码、研究档案、工具链范式 |
| dev-cli | Agent 原生友好开发:--llms 手册面、类型化 CTA 协议、命令自省、发现通道与 token 经济学(原 doc-cli 改名) |
| dev-lint | 静态检查(原 md-lint、ls-lint):md 五面与 rs/py/ts 语言面、类型化结构 init 与 check(四类型模板) |

插件级资产:scripts(md-guard.py 提交挡板、mdrules.py 禁字唯一权威、lint-hook.py 写后静检)与 hooks(PostToolUse,段名 dev file-check)。

结构沿革:由原 evo-doc 与 evo-lint 两插件域合成;中文面 zh-lint 经拆出后于批 145 删除(ADR-0025)。

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

## 翻台与清理(重载铁律)

- **旧进程 = 旧技能**:装/更新插件后必须翻台才生效,恒 `agents reload <id>`(同格同 session 重进)
- 全端序:每端 `/plugin marketplace update project-evo` 再到 卸旧插件(evo-doc、evo-herdr、evo-distil、evo-lint、evo-agent 五件)再到 装 dev 与 evo 再到 全格 `agents reload`
- Kimi 端:清 `~/.kimi/skills` 旧目录后重拷,重启会话

当前发布:0.15.0。
