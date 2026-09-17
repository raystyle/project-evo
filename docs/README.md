# docs 地图

> 本仓自身的文档。体系为文档即代码形态:ADR 管不可逆决策、requirements 管需求登记、diary 留过程痕、research 存研究档案;skill 知识库在 `plugins/<插件>/skills/` 下(四插件九 skill,ADR-0010 与 ADR-0011 与 ADR-0012)。

| 文档 | 讲什么 | 何时看 |
|------|--------|--------|
| `../README.md` | 项目标准入口（定位、快速开始、目录、概念） | 第一次接触本仓 |
| `../CHANGELOG.md` | 可交付变更日志 | 查历史时 |
| `../ROADMAP.md` | 阶段与里程碑状态 | 看进度时 |
| `adr/README.md` | 本仓架构决策索引（ADR-NNNN） | 立不可逆技术选择前查先例 |
| `requirements/README.md` | 本仓需求登记索引（REQ-NNN） | 立需求或查验收判据时 |
| `research/README.md` | 本仓研究登记 | 找 S 文档时 |
| `research/S001-bh与reader使用过程技巧.md` | bh 工位复用与 reader 电子书阅读过程 | 再用搜索抓取或读电子书前 |
| `research/S005-git密钥隐私扫描skill选型.md` | 密钥扫描 skill 选型 | 改 secret-scan 规则或对照 gitleaks 前 |
| `research/S006-secret-scan-AB对照.md` | secret-scan 对 code-kit scan 的 A/B 实跑 | 裁决规则面差异时 |
| `research/S007-OfficeCLI-agent原生Office套件.md` | OfficeCLI 是什么、怎么给 agent 用、本机钉资产安装与烟测 | 选型或本机安装 Office 自动化 CLI 时 |
| `diary/2026-09-08-bh与reader使用过程.md` | 过程日记样例 | 写 diary 前对照格式 |
| `../plugins/evo-adr/skills/doc-gov/SKILL.md` | 文档治理知识面本体(合同/ADR/REQ/投影/六态) | 写 AGENTS、立 ADR/REQ 时 |
| `../plugins/evo-adr/skills/code-kit/SKILL.md` | 骨架与门禁工具箱命令面(init/check/scan/md-guard) | 初始化骨架、跑合规检查时 |
| `../plugins/evo-adr/skills/gh-issue/SKILL.md` | 命令出错自动上报 GitHub issue 工作流(定位仓、去重、组装、发单、回执) | 命令报错要给上游发 issue 时 |
| `../plugins/evo-adr/skills/doc-gov/references/README.md` | 治理知识渐进索引（快速路由到场景到全量） | 找治理参考时先看 |
| `../plugins/evo-adr/skills/code-kit/references/README.md` | 工具与工程合同渐进索引 | 找工程参考时先看 |
| `../plugins/evo-adr/skills/doc-gov/references/base-agents-contract.md` | AGENTS 五节合同（Commands/Must/Must not/Read first/环境） | 写目标项目 AGENTS 时 |
| `../plugins/evo-adr/skills/doc-gov/references/base-adr.md` | ADR 模板、状态机、supersede 流 | 立 ADR 时 |
| `../plugins/evo-adr/skills/doc-gov/references/base-req.md` | REQ 状态机与 trace 回填 | 立需求时 |
| `../plugins/evo-adr/skills/doc-gov/references/base-projection.md` | 生成投影纪律与三栈机制对照 | 配 API 文档工具链时 |
| `../plugins/evo-adr/skills/code-kit/references/base-init.md` | 初始化流程、裁剪原则、存量迁移 | 在目标项目落地骨架时 |
| `../plugins/evo-adr/skills/code-kit/references/tool-rust.md` | Rust 工程合同（workspace、契约注释、aidoc） | 建 Rust 仓时 |
| `../plugins/evo-adr/skills/code-kit/references/tool-typescript.md` | TypeScript/Node 工程合同（tsc、node:test、TSDoc、API Extractor） | 建或治理 Node/TS 仓时 |
| `../plugins/evo-adr/skills/code-kit/references/env-platform.md` | 平台适配：shell 分平台、编码行尾、脚本载体、CI 三系统、接管验收 | 定平台矩阵/跨平台协作时 |
| `../plugins/evo-adr/skills/doc-gov/references/flow-release.md` | 封版发布模式：三路门禁验收、封版件、tag 触发、发布验收 | 发版本时 |
| `../plugins/evo-adr/skills/doc-gov/references/flow-build.md` | 编译打包流水线：detect 清单、产地分工、rclone 双段镜像、护栏与自升级对齐 | 搭 CI/CD 流水线时 |
| `../plugins/evo-adr/skills/doc-gov/references/exp-pitfalls.md` | 已知误区十八条 | 落地前预警 / 踩坑后对照 |
| `../plugins/evo-adr/skills/code-kit/verification/command-test-cases.md` | 规范检查命令（参数化 ProjectRoot） | 验证骨架合规时 |
| `../plugins/evo-codesec/skills/secret-scan/SKILL.md` | 密钥与隐私扫描命令面 | 扫 git/GitHub 泄露时 |
| `../plugins/evo-codesec/skills/security-audit/SKILL.md` | 安全审计与漏洞审查(双模式、六阶段、覆盖账本;译自 Cloudflare security-audit-skill) | 安全审计/渗透测试/漏洞审查时 |
| `../plugins/evo-research/skills/research/SKILL.md` | 资料检索管线命令面（gh/bh/aria2c/reader 工位复用） | 搜代码/论文/文章/下载大资产时 |
| `../plugins/evo-research/skills/report/SKILL.md` | 研究成文与三件套(骨架、渲染、版式、信源) | 写研究报告或渲染 PDF 时 |
| `../plugins/evo-herdr/skills/herdr-flywheel/SKILL.md` | 多仓 herdr 飞轮协作(派单/回执/断言/吸收;协议唯一权威源,ADR-0009) | 跨仓派单或收回执时 |
| `../plugins/evo-herdr/skills/herdr-review/SKILL.md` | 推送前评审闸门(评审请求、F/G/CONFIRM 回执、轮次、窗格检测带起;ADR-0011) | 发评审请求或写对线回执时 |
| `guides/gates.md` | 本仓门禁全集标准命令（含 scan 豁免完整正则） | 跑门禁或被 scan 假红卡住时 |
