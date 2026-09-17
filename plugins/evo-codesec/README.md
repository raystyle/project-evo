# evo-codesec

项目进化代码安全插件:两个 skill,`secret-scan` 密钥与隐私深扫(工作区、git 全历史、GitHub alerts 与 code search)与 `security-audit` 安全审计与漏洞审查(译自 Cloudflare security-audit-skill,MIT,目录内附 LICENSE)。

状态:active。插件面客户端:Claude Code、Codex、Grok;纯 skills 面:Kimi 等手拷子集。

## 前置

- skill 本体纯 Markdown;secret-scan 脚本为零依赖 PEP 723 标准 Python(>=3.12),`uv run` 或系统 `python` 均可
- GitHub 面需 gh 已登录;`--clone-history` 裸克隆远程历史需网络与磁盘
- security-audit 校验脚本为 Node `.cjs`,需 node 运行时(全平台命令分发由宿主工具链 omc 与 ark 统一维护)

## 安装

Claude Code:

```text
/plugin marketplace add raystyle/project-evo
/plugin install evo-codesec@project-evo
```

Codex:

```bash
codex plugin marketplace add raystyle/project-evo
```

Grok:

```bash
grok plugin marketplace add raystyle/project-evo
grok plugin install evo-codesec@project-evo --trust
```

Kimi(无市场):把 `skills/` 下两个 skill 目录一并拷至 `~/.kimi/skills/`;斜杠命令不随行。

## 用法

安装插件后两个 skill 按意图路由自动触发,客户端显示为 `evo-codesec:secret-scan` / `evo-codesec:security-audit`;斜杠命令(Claude Code 面):

- `/evo-codesec:secret-scan-cli [目标项目] [--github owner/repo] [--clone-history] [--pii] [--json]` 密钥与隐私深扫

脚本可独立调用(免插件):

```bash
uv run skills/secret-scan/scripts/scan.py [目标项目]
uv run skills/secret-scan/scripts/ab.py   # A/B 对照 secret-scan 与 evo-adr code-kit 的浅扫
```

示例提示词:「扫一下这个仓有没有密钥泄露」「对这个服务做一次聚焦的安全审查」。

## 输出与纪律

- 按严重级排序的发现清单(文件:行 + 脱敏片段 + 首见提交);命中片段一律脱敏
- HIGH(密钥疑似入库)先轮换凭据再清史(git filter-repo / BFG)
- 文档禁字与浅密钥门禁在 `evo-adr:scan`(code-kit);误报豁免走 `PEVO_SCAN_ALLOW` / `SECRET_SCAN_ALLOW`
- security-audit 产物走结构化报告(report-schema.json 与两个 validate 校验器)

## 支持与发布

- 支持:[raystyle/project-evo issues](https://github.com/raystyle/project-evo/issues)
- 当前发布:0.4.0
