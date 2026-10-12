# 配置诊断修复面:四端 agent 配置静检

> 检查对象是宿主四客户端配置面(claude 的 settings.json 与 settings.local.json、codex 与 grok 的 config.toml、kimi 的 config.toml 与 skills 安装面),按端手跑,不进仓 CI。判据分档依据研究档 cfg-01(2026-10-12,官方文档对照):error = 客户端不可能成功或写错载体的硬伤;advisory = 客户端容忍但值得治理的残留与演进面。纪律:只报不改,修复走人;判定取退出码,不接吞退出码管道。

## 命令

```bash
uv run <技能根>/scripts/config-lint.py [--claude P] [--codex P] [--grok P] [--kimi-config P] [--kimi P] [--kimi-source P] [--json]
```

- 单面异常走内部异常兜底转 error(`_safe`),不吞其余面的发现
- 缺省路径:`~/.claude/settings.json`(连同 `settings.local.json`)、`~/.codex/config.toml`、`~/.grok/config.toml`、`~/.kimi-code/config.toml`、`~/.kimi/skills`;文件不在即跳过该面(note 行,不算错)
- `--claude` 指向非用户面文件(如仓内 `.claude/settings.json`)时,凭证判据升 error(会进库的文件)
- 退出码:0 无 error(advisory 不挡)、1 有 error;`--json` 出机读形
- 豁免:`PEVO_CONFIG_LINT_ALLOW=字段a;字段b`(白名单与枚举值),留因由登记

## error 判据族

| 面 | 检查 | 判据 | 修法 |
| --- | --- | --- | --- |
| claude | JSON 解析 | 两 settings 文件可解析;顶层是对象 | 修语法 |
| 全端 | 形态非法 | 各键取值类型不符(env 与 enabledPlugins 与 permissions 与 hooks 须对象、hooks 数组表、枚举须字符串)报形态非法 error,不崩溃 | 修形态 |
| claude | defaultMode 非法值 | 限 doctor 2.1.296 实测枚举:`default`/`acceptEdits`/`auto`/`plan`/`bypassPermissions`/`dontAsk` | 改合法值 |
| claude | 命令绝对路径缺失 | hooks 与 statusLine 命令的绝对路径 token(引号段含空格可解)须存在 | 修路径或改 PATH 相对 |
| claude | 项目面明文凭据 | 非用户面文件的 env 键族 `*TOKEN`/`*API_KEY`/`*SECRET`/`*PASSWORD`/`*KEY`(词边界)/`*CREDENTIAL`/`*BEARER` 大小写不敏感持字面量(`${VAR}`、`$VAR`、`%VAR%`、`$env:VAR` 占位形放行) | 凭证移出会进库文件 |
| codex | TOML 解析 | config.toml 可解析 | 修语法 |
| codex | mcp_servers 形态 | 每服务 command 字符串、args 字符串列表 | 修形态 |
| codex | 枚举非法 | approval_policy 与 sandbox_mode 限官方值集 | 改合法值 |
| codex | 高置信秘密形态 | 值含 PEM 私钥块、AWS 键(AKIA)、sk- 长令牌(config.toml 不是凭证载体,契约是 auth.json 或 keyring) | 移到凭证载体 |
| grok | TOML 解析 | config.toml 可解析 | 修语法 |
| grok | plugins.enabled 悬空引用 | 每 enabled 名须在 `~/.grok/marketplace-cache/*/plugins/` 在位 | 清残留名(grok 卸载不自动清配置,判例 2026-10-12 本机四个) |
| grok | status_line 路径缺失 | ui.status_line.command 绝对路径 token 须存在 | 修路径 |
| kimi | TOML 解析 | config.toml 可解析 | 修语法 |
| kimi | providers api_key 明文非空 | 凭证应走 oauth 或环境注入 | 改 oauth |
| kimi | 高置信秘密形态 | 同 codex 行 | 同上 |
| kimi | SKILL.md 形态 | 每 skill 目录有 SKILL.md 且 frontmatter name 同目录名 | 重拷该 skill |
| kimi | 漂移对账 | 给 `--kimi-source` 时安装面与源完全一致 | 按源重镜像 |

## advisory 判据族

| 面 | 检查 | 依据 |
| --- | --- | --- |
| claude | enabledPlugins 悬空引用 | 文档容忍态:项目文件指向未装插件是稳态,客户端上报未安装不拒配置;治理价值在清卸载残留 |
| claude | 用户面明文凭据 | 网关页允许凭证写用户 settings(更优是 apiKeyHelper 或环境注入),提示迁移不阻断 |
| claude | 未知顶层字段 | 官方 schema 落后索引 45 键且根上放行额外属性;doctor 不报未知键,lint 不做闭合白名单 |
| codex | 未知顶层键 | 默认忽略并 warning,仅 exec 路径 `--strict-config` 报错;升档须另开 strict 档 |
| codex | plugins 配置残留候选 | `plugins."名@市场"` 键指向 cache 无目录(卸载不清配置,判例 2026-10-12 wsl 三条) |
| grok | 未知节 | 白名单先验,随版本演进 |
| kimi | 未知顶层键 | 同上 |
| 策略偏好 | 不判 | bypassPermissions、permission_mode 取值属用户裁量;`auto` 与 `bypassPermissions` 自 v2.1.257 起项目与本地文件不生效,可另提示 scope 不生效,不判非法 |

## 权威入口

| 客户端 | 入口 | 查什么 |
| --- | --- | --- |
| claude | `https://code.claude.com/docs/en/settings-reference`(Settings index) | 字段全集与 scope;活清单,不抄成冻结白名单 |
| claude | `https://code.claude.com/docs/en/env-vars` | env 变量全集 |
| claude | `https://code.claude.com/docs/en/llm-gateway-connect` | 网关凭证的正确载体 |
| claude | `https://json.schemastore.org/claude-code-settings.json` | 编辑器补全用;落后索引,不做门禁 |
| codex | `https://developers.openai.com/codex/config-reference` 加本机 `codex --strict-config` 在 exec 上的拒绝集 | 键全集;schema URL 取回前不当门禁 |
| grok | 本机 `~/.grok/README.md`(随发行内置)与 `grok plugin --help` | 节键与 plugins 语义 |
| kimi | 本机 `~/.kimi-code/config.toml` 实形与 `https://agentskills.io/specification` | 键形与 SKILL.md 形态 |

## 修复手册

- 悬空引用(claude enabledPlugins):确认插件确已撤 -> 删键;应保留 -> 重装该插件
- 悬空引用(grok plugins.enabled):卸载残留 -> 从 enabled 数组删名(grok uninstall 不回写,手清)
- codex plugins 配置残留:删 config.toml 对应 `[plugins."名@市场"]` 表
- 明文凭据:用户面 -> apiKeyHelper 或环境注入(vault env);项目面 -> 立即移出并轮换
- 路径缺失:statusline 指向 debug 构建是高发位(cargo clean 即断),改安装版路径或重建
- kimi 漂移:按源重镜像(rsync `--delete` 自仓 `plugins/*/skills/*`)

## 舰队用法

- 五端各跑本端 config-lint;装卸插件后必跑一次(安装面操作不同步清理配置引用)
- WSL 查宿主 Windows 面走 interop pwsh 直跑同脚本
- 结果进端检清单,不进仓 CI:配置面属宿主资产
