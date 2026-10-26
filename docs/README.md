# docs 地图

> 本仓自身的文档。体系为文档即代码形态:ADR 管不可逆决策、requirements 管需求登记、research 存研究档案;skill 知识面批 176 起在插件 `hook_rules/`(薄壳指路,ADR-0027)。

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
| `research/S014-wikiskill对照.md` | wikiskill 对照,三层聚合成技能自进化(吸收进 distil;档案) | 复核 distil 三层口径时 |
| `research/S015-四仓三层聚合标准合流.md` | 四仓三层聚合标准合流:实践判例与业界对照(档案) | 复核三层聚合与 distil 终态口径时 |
| `research/S016-skill双规范业界先例对照.md` | SKILL 双规范业界先例对照(grok 研究轮,计数勘误;吸收进 skill-spec 规范 A/B) | 对表 skill 双规范口径与业界先例时 |
| `research/S017-rust交流波业界先例对照.md` | rust 交流波业界先例对照(grok 研究轮;最小公约数五条与按仓建议分流) | 复核交流波工具链判读口径时 |
| `research/S018-rust交流波跨仓互鉴.md` | rust 交流波跨仓互鉴:谁偷谁什么表(七仓晒单档案) | 复核互鉴判定与采纳去向时 |
| `research/S019-agent原生CLI标准聚合.md` | agent 原生 CLI 标准聚合(六仓票去重定稿;吸收进 dev-cli 公约面) | 对表 CLI 公约口径与票源时 |
| `research/S020-gwlogs术语挖词与词表基线.md` | gw_logs 对话语料术语挖词与仓内基线(termrules 两层词表与 term-lint 出处) | 复核术语表口径或再挖词时 |
| `sources/README.md` | sources 唯一出处层索引(diary 与 external 两根,ADR-0021) | 查出处件留底与 trace 引文时 |
| `diary/2026-09-08-bh与reader使用过程.md` | 轨迹样例(写法权威在 distil 轨迹篇) | 写轨迹前对照格式时 |
| `../plugins/dev/hook_rules/intents/` | dev 意图注入件六枚(dev-cli 面、ADR/REQ、研究档案、doc 注释、工具链) | 改治理与静检知识时 |
| `../plugins/dev/hook_rules/dev-rules/` | dev 路径注入件四枚(md 纪律、术语纪律、结构面、骨架治理) | 改写 md/toml/合同时 |
| `../plugins/evo/hook_rules/intents/` | evo 意图注入件 26 枚(十二域主件加拆件:坑、协作、契约、闸门、层结构、判例) | 改 evo 操作知识时 |
| `../.tools/README.md` | 本仓自用脚本工具登记(md-ref-scan、init、check、scan) | 跑仓门禁或维护骨架模板时 |
| `../.tools/verification/command-test-cases.md` | check 的等价 PowerShell 用例集(参数化 ProjectRoot) | 验证骨架合规时 |
| `guides/gates.md` | 本仓门禁全集标准命令（含 scan 豁免完整正则） | 跑门禁或被 scan 假红卡住时 |