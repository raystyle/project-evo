# docs 地图

> 本仓自身的文档。体系为文档即代码形态:ADR 管不可逆决策、requirements 管需求登记、research 存研究档案;过程轨迹(日记)继续落 diary/,形态权威已迁 `../plugins/evo-skills/skills/distil-skill/references/trajectories.md`;skill 知识库在 `plugins/<插件>/skills/` 下(三插件五 skill)。

| 文档 | 讲什么 | 何时看 |
|------|--------|--------|
| `../README.md` | 项目标准入口（定位、快速开始、目录、概念） | 第一次接触本仓 |
| `../CHANGELOG.md` | 可交付变更日志 | 查历史时 |
| `../ROADMAP.md` | 阶段与里程碑状态 | 看进度时 |
| `adr/README.md` | 本仓架构决策索引（ADR-NNNN） | 立不可逆技术选择前查先例 |
| `requirements/README.md` | 本仓需求登记索引（REQ-NNN） | 立需求或查验收判据时 |
| `research/README.md` | 本仓研究登记 | 找 S 文档时 |
| `research/S001-bh与reader使用过程技巧.md` | bh 工位复用与 reader 电子书阅读过程 | 再用搜索抓取或读电子书前 |
| `research/S005-git密钥隐私扫描skill选型.md` | 密钥扫描 skill 选型(档案) | 查选型沿革或对照 gitleaks 前 |
| `research/S006-secret-scan-AB对照.md` | secret-scan 对 code-kit scan 的 A/B 实跑(档案) | 查扫描规则面差异沿革时 |
| `research/S007-OfficeCLI-agent原生Office套件.md` | OfficeCLI 是什么、怎么给 agent 用、本机钉资产安装与烟测 | 选型或本机安装 Office 自动化 CLI 时 |
| `research/S008-dev-evo标准外部对标.md` | agentskills 规范、AGENTS.md 生态、llms.txt 与 ADR 惯例对标,对照九条用后感定优先级 | 对表 skill 规范或定检索面积压时 |
| `research/S009-多agent并行DAG协作模型核验.md` | 多 agent DAG 协作模型核验与飞轮对照分流 | 做并行派单设计或复核该模型时 |
| `research/S010-clidocs四样板对照.md` | CLI 对外面标准四样板对照与吸收分流(gh、cf、incur 双实现;档案) | 复核 agent-face 与 templates 口径时 |
| `research/S011-herdr-dispatch对照.md` | herdr 任务分发编排对照分流(lane 模型、探针契约、py 脚本评估结论;档案) | 改 lane-dispatch 标准或复核委派口径时 |
| `research/S012-五窗格开发布局对照.md` | 窗格布局定式对照(通用四窗格与 PI 五窗格、双闸门、会话纪律;档案) | 改布局定式或自省验收口径时 |
| `research/S013-研究形态与工具链范式对照.md` | 研究形态与工具链范式对照分流(三仓研究形态、十仓工具链扫描;档案) | 复核四形态与工具范式口径时 |
| `diary/2026-09-08-bh与reader使用过程.md` | 轨迹样例(写法权威在 distil-skill 轨迹篇) | 写轨迹前对照格式时 |
| `../plugins/evo-doc/skills/doc-gov/SKILL.md` | 文档框架治理知识本体(意图路由与形态速览) | 使用/修改 skill 前 |
| `../plugins/evo-doc/skills/doc-gov/references/README.md` | 参考索引(5 篇全量与快速路由) | 找治理参考时先看 |
| `../plugins/evo-doc/skills/doc-gov/references/base-adr.md` | ADR 模板、状态机、supersede 流 | 立 ADR 时 |
| `../plugins/evo-doc/skills/doc-gov/references/base-req.md` | REQ 状态机与 trace 回填 | 立需求时 |
| `../plugins/evo-doc/skills/doc-gov/references/base-code-doc.md` | 代码 doc 注释契约与文档即代码(单一权威源、投影再生成) | 立代码契约注释或投影守卫时 |
| `../plugins/evo-doc/skills/doc-gov/references/base-research.md` | 研究档案形态(S 编号一题一篇、六态结论、对照分流) | 立研究档案时 |
| `../plugins/evo-doc/skills/doc-gov/references/tool-project-kit.md` | 项目工具链范式(工具归档、PEP 723 零依赖 uv 直跑、门禁与发布) | 建项目工具骨架时 |
| `../plugins/evo-doc/skills/native-design/SKILL.md` | Agent 原生友好开发指导(五件速览与意图路由) | 造或改 agent 友好 CLI 时 |
| `../plugins/evo-doc/skills/native-design/references/agent-face.md` | Agent 友好 CLI 五件(手册面、CTA 协议、帮助面、自省、裸调用) | 配 CLI agent 面时 |
| `../plugins/evo-doc/skills/native-design/references/tool-cli-agents.md` | agent-native CLI 设计(发现通道、token 经济学、脚本 workspace) | 定发现通道与 token 面时 |
| `../.tools/README.md` | 本仓自用脚本工具登记(md-ref-scan、init、check、scan) | 跑仓门禁或维护骨架模板时 |
| `../.tools/verification/command-test-cases.md` | check 的等价 PowerShell 用例集(参数化 ProjectRoot) | 验证骨架合规时 |
| `../plugins/evo-herdr/skills/herdr-orch/SKILL.md` | 主开发台:初始角色邻居窗格并配合工作(通用四窗格与 PI 五窗格布局定式)、评审闸门加自省验收双闸门、任务分发 lane;ADR-0011 起,ADR-0019 双模式定形 | 定开发布局、发评审请求或写对线回执时 |
| `../plugins/evo-herdr/skills/herdr-flywheel/SKILL.md` | 跨仓库跨项目跨机器交流(派单/回执/断言/吸收,状态门控与事件驱动收执,产物契约与状态档三件套、盘上稳态与干预信号分治,跨机器工位,并行派单义务图;协议唯一权威源,ADR-0009) | 跨仓派单、收回执或落产物契约验收对账时 |
| `../plugins/evo-skills/skills/distil-skill/SKILL.md` | 技能自进化:三层聚合(sources 唯一出处层、knowledge 带版本双链知识、operations 标准技能与 how-to 手册,git 边界三选一,归档统一字母表),四步环蒸馏提案与合取闸门 | 把项目经验沉淀成 skill、迭代标准技能集时 |
| `guides/gates.md` | 本仓门禁全集标准命令（含 scan 豁免完整正则） | 跑门禁或被 scan 假红卡住时 |
