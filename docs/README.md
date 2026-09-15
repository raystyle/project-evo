# docs 地图

> 本仓自身的文档。体系为文档即代码形态:ADR 管不可逆决策、requirements 管需求登记、diary 留过程痕、research 存研究档案;skill 知识库在 `plugins/project-evo/skills/` 下。

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
| `research/S006-secret-scan-AB对照.md` | secret-scan 对 docs-evo scan 的 A/B 实跑 | 裁决规则面差异时 |
| `research/S007-OfficeCLI-agent原生Office套件.md` | OfficeCLI 是什么、怎么给 agent 用、本机钉资产安装与烟测 | 选型或本机安装 Office 自动化 CLI 时 |
| `diary/2026-09-08-bh与reader使用过程.md` | 过程日记样例 | 写 diary 前对照格式 |
| `../plugins/project-evo/skills/super-research/SKILL.md` | 资料检索管线命令面（gh/bh/aria2c/reader 工位复用） | 搜代码/论文/文章/下载大资产时 |
| `../plugins/project-evo/skills/secret-scan/SKILL.md` | 密钥与隐私扫描命令面 | 扫 git/GitHub 泄露时 |
| `../plugins/project-evo/skills/security-audit/SKILL.md` | 安全审计与漏洞审查(双模式、六阶段、覆盖账本;译自 Cloudflare security-audit-skill) | 安全审计/渗透测试/漏洞审查时 |
| `../plugins/project-evo/skills/dev-evo/SKILL.md` | skill 本体概览层 | 使用/修改 skill 前 |
| `../plugins/project-evo/skills/dev-evo/references/README.md` | 参考知识体系渐进索引（快速路由到场景到全量） | 找任何参考时先看 |
| `../plugins/project-evo/skills/dev-evo/references/base-agents-contract.md` | AGENTS 五节合同（Commands/Must/Must not/Read first/环境） | 写目标项目 AGENTS 时 |
| `../plugins/project-evo/skills/dev-evo/references/base-adr.md` | ADR 模板、状态机、supersede 流 | 立 ADR 时 |
| `../plugins/project-evo/skills/dev-evo/references/base-req.md` | REQ 状态机与 trace 回填 | 立需求时 |
| `../plugins/project-evo/skills/dev-evo/references/base-projection.md` | 生成投影纪律与三栈机制对照 | 配 API 文档工具链时 |
| `../plugins/project-evo/skills/dev-evo/references/base-init.md` | 初始化流程、裁剪原则、存量迁移 | 在目标项目落地骨架时 |
| `../plugins/project-evo/skills/dev-evo/references/tool-rust.md` | Rust 工程合同（workspace、契约注释、aidoc） | 建 Rust 仓时 |
| `../plugins/project-evo/skills/dev-evo/references/tool-typescript.md` | TypeScript/Node 工程合同（tsc、node:test、TSDoc、API Extractor） | 建或治理 Node/TS 仓时 |
| `../plugins/project-evo/skills/dev-evo/references/env-platform.md` | 平台适配：shell 分平台、编码行尾、脚本载体、CI 三系统、接管验收 | 定平台矩阵/跨平台协作时 |
| `../plugins/project-evo/skills/dev-evo/references/flow-release.md` | 封版发布模式：三路门禁验收、封版件、tag 触发、发布验收 | 发版本时 |
| `../plugins/project-evo/skills/dev-evo/references/exp-pitfalls.md` | 已知误区十八条 | 落地前预警 / 踩坑后对照 |
| `../plugins/project-evo/skills/dev-evo/verification/command-test-cases.md` | 规范检查命令（参数化 ProjectRoot） | 验证骨架合规时 |
| `guides/gates.md` | 本仓门禁全集标准命令（含 scan 豁免完整正则） | 跑门禁或被 scan 假红卡住时 |
