# hook 面:写后自动静检

> 插件自带 PostToolUse hook(hooks/hooks.json 加 scripts/lint-hook.py):Edit、Write、MultiEdit 落盘后按后缀自动静检,报错信息回传。设计纪律沿市场仓 hook 判例:只做快检查,重检查进门禁与 CI。

## 触发与分派

- 载荷:stdin JSON,取 tool_input.file_path;无 file_path 或非对象整体放行(退出码 0)
- 后缀分派:.md 走内建检查(禁字四类、标题括号、按面行数上限);.py 走 ruff check --no-cache;.rs 走 rustfmt --check --edition 2024;.ts/.tsx/.mts/.cts 走 eslint(仓内有配置才有效,工具缺位放行)
- 报错回传:退出码 2 加 stderr 逐条(行号加规则加一句);修后重写即复检

## 行数上限(可裁)

| 面 | 缺省 | 环境变量 |
| --- | --- | --- |
| AGENTS.md | 200 行 | EVO_LINT_AGENTS_MAX |
| CLAUDE.md(单行桥接免检) | 50 行 | EVO_LINT_CLAUDE_MAX |
| SKILL.md | 500 行(spec) | EVO_LINT_SKILL_MAX |

裁值登记在仓 AGENTS 或 lint 配置在册,不静默超。

## 双端支持

- Claude Code:Edit/Write/MultiEdit 直查(hook 原生面)
- Codex:hooks.json 用花括号 `${CLAUDE_PLUGIN_ROOT}` 与 commandWindows(cmd.exe /C 形,Codex 只替换花括号形态);apply_patch 载荷无 file_path 宽容放行,静态检查兜底靠 pre-commit
- 生效时点:装插件或 update 后新会话起;hook 改动同插件版本线发版

## 纪律红线

- hook 内禁慢命令:cargo clippy 全量、tsc 全量、断链全树不进 hook(秒级为界)
- hook 报错不豁免凑绿:豁免留因由与范围;误拦上报插件仓修规则,不静默绕
- 判定纪律沿 lint SKILL 速览:退出码制,不接吞退出码管道
