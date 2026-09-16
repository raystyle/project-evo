# ProjectEvo 开发协作规则

> 唯一权威源。`CLAUDE.md` 仅一行 `@AGENTS.md` 桥接,不重复维护。
> 定位:项目治理插件市场仓(四 skill 同属项目治理面,非业务工具面):dev-evo(文档体系治理)、super-research(资料检索治理)、secret-scan(密钥隐私治理)、security-audit(安全审计治理,译自 Cloudflare security-audit-skill,MIT,skill 目录内附 LICENSE),客户端显示 `project-evo:<skill>`。skill 硬性规范以 [agentskills 官方 spec](https://agentskills.io/specification) 为硬标准,细则见 `docs/guides/skill-spec.md`。

## Commands

- `uv run pytest` 全测试(脚本行为 + 清单一致性守卫 + 仓内禁字回归)
- `uv run .tools/md-ref-scan.py plugins/project-evo/skills/<skill>` 断链扫描(四 skill 各跑一次;pre-commit 自动)
- `uv run plugins/project-evo/skills/dev-evo/scripts/check.py` 本仓骨架自检(PE-01 至 PE-12;下游仓 PE-11 历史档案豁免走 PEVO_CHECK_ALLOW,正则见 docs/guides/gates.md)
- `uv run plugins/project-evo/skills/dev-evo/scripts/scan.py . --no-history` 禁字与密钥扫描(测试夹具与 A/B 用例的公开示例假密钥走 `PEVO_SCAN_ALLOW` 豁免:tests/test_project_evo.py 的 ghp_ 假 token、secret-scan ab 夹具与 S006 与本文件 Commands 节自举示例的 AWS 公开样值;标准命令与完整豁免正则见 docs/guides/gates.md)
- 提交挡板:`git config core.hooksPath githooks`(md 禁字 + 断链,不过不进库)

## Must

- skill 目录名与 frontmatter `name` 一致;`description`「做什么+何时用」兼具且含触发词
- 变更完整性:只改 skill 不同步 SKILL 索引/references/CHANGELOG = 变更不完整
- 事实性断言标六态;操作前先查 references/ 索引,禁止凭记忆重写删减版
- 吸收即提炼:外部信源与家族实践进库只留最准确精练的可复用表达;成品不点名外部仓库
- 双 manifest(Claude/Codex 面)字段同步改;版本号三清单一致
- 不可逆技术选择先立 `docs/adr/`;新需求先立 `docs/requirements/REQ` 再实现

## Must not

- 禁止 emoji;流程图用 mermaid,禁止 box-drawing 手拼伪流程图
- frontmatter 禁 `version`/`argument-hint` 等非官方字段
- 生成物手改、双份并行维护(单一权威源:skill 只在 `plugins/project-evo/skills/` 下,插件只有 `project-evo` 一个)
- 中文 md 用 PowerShell 管道批量改写(塌行/截断,用编辑工具逐处改)

## Read first

- 本文件(合同)
- `docs/README.md`(全仓文档地图 + skill references 索引)
- `plugins/project-evo/skills/dev-evo/SKILL.md`(核心 skill 意图路由)
- `docs/adr/` 仅在改对应决策时;`CHANGELOG.md`/`ROADMAP.md` 查历史与阶段

## 环境

- 平台:Windows + PowerShell 7(禁 powershell.exe 5.1 与 cmd);uv 运行时,脚本 PEP 723 零依赖(>=3.12)
- 当前阶段:v0.6.0 已封版发布(2026-09-16 tag 加 Release;第五十六批三栈工具篇与档案机制入册;沿革:第五十一批 security-audit、第五十批 dev-evo 文档即代码、第四十七批四插件收敛、第四十九批 office-pro 移除)
- 部署:Claude Code `/plugin marketplace add raystyle/projectevo`;Codex `codex plugin marketplace add raystyle/projectevo`;Grok `grok plugin install project-evo@projectevo`;Kimi 无市场,拷 `plugins/project-evo/skills/*` 至 `~/.kimi/skills`
- 项目状态与待办见 `ROADMAP.md`,不在本文件维护
