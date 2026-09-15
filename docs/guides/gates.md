# 仓门禁全集

> 本仓五道门禁的标准命令。scan 的豁免正则完整权威在此（`AGENTS.md` Commands 节只留指针），跑者零记忆复制即用。夹具假密钥是公开示例值，路径级豁免可评审进库。[实证: 全部命令 2026-09-15 治理批实跑]

| 门禁 | 命令 | 时机 |
|------|------|------|
| 全测试 | `uv run pytest` | 每次提交前 |
| 骨架自检 | `uv run plugins/project-evo/skills/dev-evo/scripts/check.py .` | 改文档结构或 skill 后 |
| 禁字与密钥扫描 | 见下方带豁免标准命令 | 每次提交前 |
| 断链扫描 | `uv run .tools/md-ref-scan.py plugins/project-evo/skills/<skill>`（四 skill 各跑） | 改 skill 与文档后 |
| 提交挡板 | `git config core.hooksPath githooks`（md 禁字加断链，一次配置） | 换机后 |

## scan 标准命令与豁免正则

```powershell
$env:PEVO_SCAN_ALLOW = "tests/.*;plugins/project-evo/skills/secret-scan/scripts/ab.py;plugins/project-evo/skills/secret-scan/verification/.*;docs/research/S006.*"
uv run plugins/project-evo/skills/dev-evo/scripts/scan.py . --no-history
```

豁免面按路径（评审进库的可复现清单，新增夹具假密钥时同步扩这里）：

- `tests/.*`：pytest 夹具的公开示例 token
- `plugins/project-evo/skills/secret-scan/scripts/ab.py` 与 `verification/.*`：secret-scan 自身 A/B 用例样值
- `docs/research/S006.*`：AB 对照研究档案的公开示例值

期望输出为 `共 0 项发现`；出现真命中先轮换凭据再清史，禁止靠扩豁免消红。
