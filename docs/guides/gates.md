# 仓门禁全集

> 本仓五道门禁的标准命令。scan 与 check 的豁免正则完整权威在此（`AGENTS.md` Commands 节只留指针），跑者零记忆复制即用。夹具假密钥是公开示例值，路径级豁免可评审进库。[实证: 命令 2026-09-15 治理批实跑;四插件路径 2026-09-16 第六十七批实跑]

| 门禁 | 命令 | 时机 |
|------|------|------|
| 全测试 | `uv run pytest` | 每次提交前 |
| 骨架自检 | `uv run plugins/evo-adr/skills/code-kit/scripts/check.py .` | 改文档结构或 skill 后 |
| 禁字与密钥扫描 | 见下方带豁免标准命令 | 每次提交前 |
| 断链扫描 | `uv run .tools/md-ref-scan.py plugins/<插件>/skills/<skill>`（四插件八 skill 各跑） | 改 skill 与文档后 |
| 提交挡板 | `git config core.hooksPath githooks`（md 禁字加断链，一次配置） | 换机后 |

## scan 标准命令与豁免正则

```powershell
$env:PEVO_SCAN_ALLOW = "tests/.*;plugins/evo-codesec/skills/secret-scan/scripts/ab.py;plugins/evo-codesec/skills/secret-scan/verification/.*;docs/research/S006.*"
uv run plugins/evo-adr/skills/code-kit/scripts/scan.py . --no-history
```

豁免面按路径（评审进库的可复现清单，新增夹具假密钥时同步扩这里）：

- `tests/.*`：pytest 夹具的公开示例 token
- `plugins/evo-codesec/skills/secret-scan/scripts/ab.py` 与 `verification/.*`：secret-scan 自身 A/B 用例样值
- `docs/research/S006.*`：AB 对照研究档案的公开示例值

期望输出为 `共 0 项发现`；出现真命中先轮换凭据再清史，禁止靠扩豁免消红。

## check 标准命令与豁免正则

```powershell
uv run plugins/evo-adr/skills/code-kit/scripts/check.py .
```

机器读面(第六十五批起):加 `--json` 输出 `{"ok","counts"(pass/fail/skip),"results"[{id,status,note,violations}]}` 到 stdout,violations 为全量违规项(file:line 或路径串);退出码 0/1/2 不变,出错仍 stderr 文本。飞轮回执与门禁脚本读 `counts.skip` 与 `violations`,不再正则抓结论行。

本仓活跃面零禁字，自检无需豁免。下游仓迁移骨架后(第六十七批起入口是 evo-adr 的 code-kit)的历史档案存量禁字，用环境变量
`PEVO_CHECK_ALLOW="正则;正则"` 豁免（只作用于 `docs/` 下档案的 `相对路径:行`，命中报 SKIP
留审计痕迹；根三件 AGENTS/README/CHANGELOG 是活跃面，机制上永不受益，全域正则也吞不掉；
与 scan 的 `PEVO_SCAN_ALLOW` 同一惯例，活跃面零容忍）。存量仓示例：

```powershell
$env:PEVO_CHECK_ALLOW = "docs/diary/2026-08-.*;docs/research/P00.*"
uv run plugins/evo-adr/skills/code-kit/scripts/check.py .
```

豁免清单在下游仓自己的 gates 或 docs/README 评审进库；出现新禁字先修文，禁止靠扩豁免消红。
