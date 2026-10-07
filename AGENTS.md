# ProjectEvo 开发协作规则

> 唯一权威源。`CLAUDE.md` 仅一行 `@AGENTS.md` 桥接,不重复维护。
> 定位:项目治理插件市场仓(两插件三 skill 同属项目治理面,非业务工具面):evo-doc(文档治理:doc-gov 文档框架知识,ADR 需求决策、COE 三层聚合与双向链接图、项目日记三形态,加 Agent 友好 CLI 架构标准;插件级 md 禁字 hook 与 skill 解耦)、evo-herdr(双模式协作:herdr-dev 开发模式含 review 窗格、herdr-flywheel 跨仓模式),市场名 project-evo,客户端显示 `<插件>:<skill>`。skill 硬性规范以 [agentskills 官方 spec](https://agentskills.io/specification) 为硬标准,细则见 `docs/guides/skill-spec.md`。

## Commands

- `uv run pytest` 全测试(脚本行为 + 清单一致性守卫 + 仓内禁字回归)
- `uv run .tools/md-ref-scan.py plugins/<插件>/skills/<skill>` 断链扫描(两插件三 skill 各跑一次;pre-commit 自动)
- `uv run .tools/check.py` 本仓骨架自检(PE-01 至 PE-12;下游仓 PE-11 历史档案豁免走 PEVO_CHECK_ALLOW,正则见 docs/guides/gates.md)
- `uv run .tools/scan.py . --no-history` 禁字与密钥扫描(测试夹具与研究档案的公开示例假密钥走 `PEVO_SCAN_ALLOW` 豁免:tests/test_project_evo.py 的 ghp_ 假 token 与 docs/research/S006 的公开示例样值;标准命令与完整豁免正则见 docs/guides/gates.md)
- 提交挡板:`git config core.hooksPath githooks`(md 禁字 + 断链,不过不进库)

## Must

- skill 目录名与 frontmatter `name` 一致;`description`「做什么+何时用」兼具且含触发词
- 变更完整性:只改 skill 不同步 SKILL 索引/references/CHANGELOG = 变更不完整
- 事实性断言标六态;操作前先查 references/ 索引,禁止凭记忆重写删减版
- 吸收即提炼:外部信源与家族实践进库只留最准确精练的可复用表达;成品不点名外部仓库
- 两插件各持双 manifest(Claude/Codex 面)字段同步改;两插件同版本线,市场条目与双 manifest 版本三处一致(守卫测试断言)
- 不可逆技术选择先立 `docs/adr/`;新需求先立 `docs/requirements/REQ` 再实现
- 新写与改写 SKILL.md 命令块实证准入:写进去的命令当会真跑过(ADR-0010 构造纪律)
- skill 依赖的外部命令(gh、reader 等)全平台分发安装由宿主工具链 omc 与 ark 统一维护:skill 只认 PATH(或等价显式指定),不内置安装路径

## Must not

- 禁止 emoji;流程图用 mermaid,禁止 box-drawing 手拼伪流程图
- frontmatter 禁 `version`/`argument-hint` 等非官方字段
- 生成物手改、双份并行维护(单一权威源:skill 只在 `plugins/<插件>/skills/` 下,插件共两个:evo-doc、evo-herdr)
- 中文 md 用 PowerShell 管道批量改写(塌行/截断,用编辑工具逐处改)

## Read first

- 本文件(合同)
- `docs/README.md`(全仓文档地图 + skill references 索引)
- `plugins/evo-doc/skills/doc-gov/SKILL.md`(治理知识面意图路由)
- `docs/adr/` 仅在改对应决策时;`CHANGELOG.md`/`ROADMAP.md` 查历史与阶段

## 环境

- 平台:Windows + PowerShell 7(禁 powershell.exe 5.1 与 cmd);uv 运行时,脚本 PEP 723 零依赖(>=3.12);WSL 到宿主恒走 127.0.0.1 回环加 interop 直调,不走宿主 mesh IP;验收运维脚本载体统一 pwsh
- 当前阶段:v0.11.0 已封版(2026-10-07,第八十七至九十四批:三插件下线与改名收敛两插件三 skill、知识面三形态收敛、herdr 双模式定形、挂接回归补强;两插件版本线 0.4.3 齐 0.5.0;沿革:v0.10.0 封版于 2026-09-17 第七十七至七十八批(cli-docs 对外面双标准 skill(ADR-0014)与 Prove2Me DAG 协作模型吸收进 herdr-flywheel);2026-09-23 第八十一批:report skill 移除(ADR-0015,REQ-007),四插件收敛十 skill;2026-10-07 第八十七批:gh-issue 与 build-release 与 evo-research 插件移除(ADR-0016,REQ-008),四插件收敛三插件七 skill,版本线 0.4.3 不动待整理重构批统一打版;同日第八十八批:evo-codesec 整插件下线(ADR-0017,REQ-009)与 md-guard 挡板限仓内 md,市场收敛两插件五 skill;同日第八十九批:三 skill 合一为 doc-gov、evo-adr 改名 evo-doc、skill 与 hook 解耦、知识面收敛 ADR 加 COE 加项目日记三形态与 Agent 友好 CLI 架构标准(ADR-0018,REQ-010),市场收敛两插件三 skill;同日第九十批:herdr 委派与窗格布局轻吸收(lane 分发、通用四窗格与 PI 五窗格定式,REQ-011,S011 加 S012,py 脚本评估不开发);同日第九十一批:herdr 双模式定形,herdr-review 并入 herdr-dev 开发模式(含 review 窗格),herdr-flywheel 收敛跨仓模式(ADR-0019,REQ-012);同日第九十二批:跨机器 machine 原语语义按活权威补强(REQ-013);同日第九十三批:挂接面回归测试补强三用例(REQ-014,套件 25 绿);沿革:v0.9.0 build-release 流水线标准、v0.8.0 四插件重组与评审闸门与 gh-issue)
- 部署:Claude Code `/plugin marketplace add raystyle/project-evo` 后按插件装(如 `/plugin install evo-doc@project-evo`);Codex `codex plugin marketplace add raystyle/project-evo`;Grok `grok plugin install <插件>@project-evo --trust`;Kimi 无市场,拷 `plugins/*/skills/*` 至 `~/.kimi/skills`
- 工作根:`~/repos/ProjectEvo`(WSL 独立 VHDX 挂载 /mnt/wsl/repos 快捷 ~/repos;2026-09-16 迁移,旧位 /mnt/d/ProjectEvo 过渡后裁)
- 项目状态与待办见 `ROADMAP.md`,不在本文件维护
