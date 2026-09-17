# ProjectEvo 开发协作规则

> 唯一权威源。`CLAUDE.md` 仅一行 `@AGENTS.md` 桥接,不重复维护。
> 定位:项目治理插件市场仓(四插件十一 skill 同属项目治理面,非业务工具面):evo-adr(文档治理:doc-gov 知识面、code-kit 工具面、gh-issue 错报上报、build-release 流水线标准、cli-docs 对外面双标准)、evo-codesec(代码安全:secret-scan、security-audit,后者译自 Cloudflare security-audit-skill,MIT,skill 目录内附 LICENSE)、evo-research(研究检索:research、report)、evo-herdr(多仓协作:herdr-flywheel 飞轮协议、herdr-review 评审闸门),市场名 project-evo,客户端显示 `<插件>:<skill>`。skill 硬性规范以 [agentskills 官方 spec](https://agentskills.io/specification) 为硬标准,细则见 `docs/guides/skill-spec.md`。

## Commands

- `uv run pytest` 全测试(脚本行为 + 清单一致性守卫 + 仓内禁字回归)
- `uv run .tools/md-ref-scan.py plugins/<插件>/skills/<skill>` 断链扫描(四插件十一 skill 各跑一次;pre-commit 自动)
- `uv run plugins/evo-adr/skills/code-kit/scripts/check.py` 本仓骨架自检(PE-01 至 PE-12;下游仓 PE-11 历史档案豁免走 PEVO_CHECK_ALLOW,正则见 docs/guides/gates.md)
- `uv run plugins/evo-adr/skills/code-kit/scripts/scan.py . --no-history` 禁字与密钥扫描(测试夹具与 A/B 用例的公开示例假密钥走 `PEVO_SCAN_ALLOW` 豁免:tests/test_project_evo.py 的 ghp_ 假 token 与 secret-scan ab 夹具及 docs/research/S006 的公开示例样值;标准命令与完整豁免正则见 docs/guides/gates.md)
- 提交挡板:`git config core.hooksPath githooks`(md 禁字 + 断链,不过不进库)

## Must

- skill 目录名与 frontmatter `name` 一致;`description`「做什么+何时用」兼具且含触发词
- 变更完整性:只改 skill 不同步 SKILL 索引/references/CHANGELOG = 变更不完整
- 事实性断言标六态;操作前先查 references/ 索引,禁止凭记忆重写删减版
- 吸收即提炼:外部信源与家族实践进库只留最准确精练的可复用表达;成品不点名外部仓库
- 四插件各持双 manifest(Claude/Codex 面)字段同步改;四插件同版本线,市场条目与双 manifest 版本三处一致(守卫测试断言)
- 不可逆技术选择先立 `docs/adr/`;新需求先立 `docs/requirements/REQ` 再实现
- 新写与改写 SKILL.md 命令块实证准入:写进去的命令当会真跑过(ADR-0010 构造纪律)
- skill 依赖的外部命令(gh、bh、reader、aria2c、typst 等)全平台分发安装由宿主工具链 omc 与 ark 统一维护:skill 只认 PATH(或等价显式指定),不内置安装路径

## Must not

- 禁止 emoji;流程图用 mermaid,禁止 box-drawing 手拼伪流程图
- frontmatter 禁 `version`/`argument-hint` 等非官方字段
- 生成物手改、双份并行维护(单一权威源:skill 只在 `plugins/<插件>/skills/` 下,插件共四个:evo-adr、evo-codesec、evo-research、evo-herdr)
- 中文 md 用 PowerShell 管道批量改写(塌行/截断,用编辑工具逐处改)

## Read first

- 本文件(合同)
- `docs/README.md`(全仓文档地图 + skill references 索引)
- `plugins/evo-adr/skills/doc-gov/SKILL.md`(治理知识面意图路由)
- `docs/adr/` 仅在改对应决策时;`CHANGELOG.md`/`ROADMAP.md` 查历史与阶段

## 环境

- 平台:Windows + PowerShell 7(禁 powershell.exe 5.1 与 cmd);uv 运行时,脚本 PEP 723 零依赖(>=3.12);WSL 到宿主恒走 127.0.0.1 回环加 interop 直调,不走宿主 mesh IP(口径见 code-kit references/env-platform.md 第十节);验收运维脚本载体统一 pwsh(见同篇第十一节)
- 当前阶段:v0.10.0 已封版(2026-09-17,第七十七至七十八批:cli-docs 对外面双标准 skill(ADR-0014 十一 skill 形态)与 Prove2Me DAG 协作模型吸收进 herdr-flywheel;沿革:v0.9.0 build-release 流水线标准、v0.8.0 四插件重组与评审闸门与 gh-issue)
- 部署:Claude Code `/plugin marketplace add raystyle/project-evo` 后按插件装(如 `/plugin install evo-adr@project-evo`);Codex `codex plugin marketplace add raystyle/project-evo`;Grok `grok plugin install <插件>@project-evo --trust`;Kimi 无市场,拷 `plugins/*/skills/*` 至 `~/.kimi/skills`
- 工作根:`~/repos/ProjectEvo`(WSL 独立 VHDX 挂载 /mnt/wsl/repos 快捷 ~/repos;2026-09-16 迁移,旧位 /mnt/d/ProjectEvo 过渡后裁)
- 项目状态与待办见 `ROADMAP.md`,不在本文件维护
