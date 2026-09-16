# 初始化流程：在目标项目落地文档即代码骨架

> 五步执行指南 + 裁剪原则 + 验收清单 + 存量迁移。在目标项目执行 dev-evo 时照此走。

## Step 1：判断项目状态

- **空项目/新项目** 到 全量骨架（Step 3 最小集起步）
- **已有项目补文档** 到 先盘点现有文档（README/docs/wiki/issue），问清：哪些保留、哪些迁移、哪些废弃；现有内容按新目录归类安置，**不推倒重来**
- 判断依据：git 历史、现有文档规模、团队协作约定

## Step 2：问关键问题（禁止静默假设）

| 问题 | 用途 |
| --- | --- |
| 项目一句话定位是什么？ | 写进 AGENTS 头部定位句 |
| 技术栈与形态？（CLI/服务/库/前端） | 决定契约注释形态、投影工具链、测试分层 |
| **目标平台矩阵？**（仅 Windows / 三平台 / 特定 OS） | 决定 CI 矩阵、脚本载体、行尾策略（见 env-platform.md) |
| 交互对象是谁？（agent 工具？人？） | agent 面需要 llms.txt 式入口索引与稳定输出契约 |
| 有没有研究/选型场景？ | research 结构保留；无真实研究可暂空（PE-09 SKIP 合法），有则首篇即落 |
| 文档语言与 lint 工具偏好？ | 中文为主？rumdl/markdownlint? |

一次问清一批，逐条澄清后才动手；裁定记进 diary。

## Step 3：生成骨架（最小可用集）

用 skill 自带脚本（模板在 assets/templates/，幂等不覆盖已有）：

```powershell
uv run plugins/project-evo/skills/dev-evo/scripts/init.py <目标项目> --name <项目名>
```

产物（10 件 + 五目录）：

1. **根三件**：`AGENTS.md`（五节合同,填定位与 Commands）+ `CLAUDE.md`（一行桥接）+ `CHANGELOG.md`
2. **docs 五目录**：`adr\`（README 索引 + 0000 模板）、`requirements\`（README 索引 + 0000 模板）、`guides\`（getting-started 占位）、`diary\`、`research\`
3. 按项目类型追加：公开库配投影工具链（Rust aidoc / Python MkDocStrings / TS API Extractor,见 base-projection.md 与 tool-* 篇）；有脚本积累建 `.tools\` + README；README 缺则一并建
4. **首个 REQ 登记**（通常是「建立文档体系」本身）；首个不可逆选择立 ADR-0001

## Step 4：裁剪原则

- 最小集 = AGENTS + CLAUDE + CHANGELOG + adr + requirements（含各自 README 与模板）；**guides 按需生长，不一次建全**；**diary 与 research 结构保留（用户裁定 2026-09-16，不可裁撤）**：init 即建目录，diary 首日一笔，research 无真实研究暂空、PE-09 SKIP 合法
- **禁止为凑结构建空文档**：每个文件建立时必须有真实初始内容（哪怕是首条 REQ）
- 已有团队约定（如 CONTRIBUTING、既有 ADR 目录）保留原位，在 AGENTS 的 Read first 登记关系
- 单平台项目在 AGENTS 环境节注明,免跨平台开销

## Step 5：验收清单

- [ ] AGENTS 五节齐备且定位句是本项目自己的（禁止模板原文照抄）
- [ ] ADR/REQ README 索引与文件一致（跑 check.py PE-08）
- [ ] 文件名即标题,无括号/空格/冒号
- [ ] 仓内引用无断链（check.py PE-12；或 md-ref-scan 类脚本）
- [ ] 平台矩阵决策落地：跨平台项目 `.gitattributes` 钉行尾、CI 三系统矩阵起步（见 env-platform.md)
- [ ] diary 记录初始化当天一笔
- [ ] `check.py` 全 PASS（PE-06/07 空目录 SKIP 是合法起步态）
- [ ] （可选）`git init` + 首提交；`.gitignore` 三类齐全（智能体配置/密钥/衍生垃圾）

## 存量仓迁移路径

旧目录改名归位（如 plans 到 adr、历史方案择要转 ADR）到 需求清单转 REQ 到 AGENTS 重写为五节合同 到 六态补标 到 全仓引用字面替换 到 文档门禁接入。不推倒重来，逐件迁移逐件对账 [经验]。门禁接入时历史档案存量禁字用 `PEVO_CHECK_ALLOW` 路径级豁免（只作用 docs/ 下档案，命中报 SKIP 留审计痕迹，根三件活跃面永不受益），正则口径与 scan 的 `PEVO_SCAN_ALLOW` 同一惯例。

旧体系（根原语 PRD/GOAL/PLAN/TODO/INDEX + docs 六目录）迁移映射：PRD 条目 对应 REQ；PLAN/TODO 对应 REQ 的 Criteria 与 trace；GOAL 定位句并入 AGENTS 头部与 README；INDEX 职责由 AGENTS Read first + 各 README 索引承接；proven 语义由 implemented REQ + 关联 ADR 承接；mistakes 并入 ADR（被否决的选择也是决策）或 exp 沉淀链 [经验: 迁移不是搬运是重审]。

## 初始化之后（首次运转）

1. 第一个真实需求走完整链（立 REQ 到 实现 到 验收到回填 trace），验证体系转得动
2. 第一次踩坑当场记 diary 或立 ADR，这是体系可信度的第一块试金石
3. 一周后回看：哪些文档没人写、哪些规则守不住，裁剪或降级
