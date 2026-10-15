# Requirements 索引

> 需求登记:新需求先立 REQ 再实现,实现后回填 trace(测试或验收命令)。新建拷 skill 模板(code-kit assets/templates/docs/requirements/0000-template.md),编号接当前最大号。

| id | 状态 | 优先级 | 标题 | trace |
|---|---|---|---|---|
| REQ-001 | implemented | must | check 输出 --json 机器读面与全量违规报告 | tests/test_project_evo.py |
| REQ-002 | implemented | must | 市场更名 project-evo 与四插件重组落地 | tests/test_project_evo.py |
| REQ-003 | implemented | must | herdr 评审闸门 skill 增编 | tests/test_project_evo.py |
| REQ-004 | implemented | must | 命令出错自动上报 issue 的 gh-issue 增编 | tests/test_project_evo.py |
| REQ-005 | implemented | must | build-release 流水线标准指导 skill 增编 | tests/test_project_evo.py |
| REQ-006 | implemented | must | cli-docs 对外面双标准 skill 增编 | tests/test_project_evo.py |
| REQ-007 | implemented | must | report skill 移除,evo-research 收敛为单 skill | tests/test_project_evo.py |
| REQ-008 | implemented | must | gh-issue 与 build-release 与 evo-research 移除,四插件收敛三插件七 skill | tests/test_project_evo.py |
| REQ-009 | implemented | must | evo-codesec 插件下线与 md-guard 挡板限仓内 md | tests/test_project_evo.py |
| REQ-010 | implemented | must | 三 skill 合一为 doc-gov,evo-adr 改名 evo-doc,skill 与 hook 解耦 | tests/test_project_evo.py |
| REQ-011 | implemented | must | herdr 委派与窗格布局轻吸收(lane 分发、四窗格定式、py 脚本评估) | tests/test_project_evo.py |
| REQ-012 | implemented | must | herdr 双模式定形:herdr-dev 开发模式含 review 窗格,herdr-flywheel 跨仓模式 | tests/test_project_evo.py |
| REQ-013 | implemented | must | herdr-flywheel 跨机器 machine 原语语义补强 | tests/test_project_evo.py |
| REQ-014 | implemented | must | 挪移后挂接面回归测试补强 | tests/test_project_evo.py |
| REQ-015 | implemented | must | herdr 集成 py 脚本重评估:总台运维面翻转建 fleet-exec,lane 与插件面维持零脚本 | tests/test_project_evo.py |
| REQ-016 | implemented | must | doc-gov 研究形态与工具链范式 | tests/test_project_evo.py |
| REQ-017 | implemented | must | herdr 飞轮产物契约与共享文件 | tests/test_project_evo.py |
| REQ-018 | implemented | must | 三插件五 skill 版图与 distil-skill 技能自进化 | tests/test_project_evo.py |
| REQ-019 | implemented | must | 四仓三层聚合标准合流与两 skill 终态 | tests/test_project_evo.py |
| REQ-020 | implemented | must | 类型化项目结构标准:struct 技能(init 与 check 双面) | tests/test_project_evo.py |
| REQ-021 | implemented | must | 第五插件 evo-agent:agent-doctor 四端环境诊断修复 | tests/test_project_evo.py |
| REQ-022 | implemented | must | evo-agent 第二技能 agent-s5:全局看板与频道操作面 | tests/test_project_evo.py |
| REQ-023 | implemented | must | herdr:s5 删除并入 agent-s5,s5 归一为全 agent 共享看板与实时流 | tests/test_project_evo.py |
| REQ-024 | implemented | must | evo-lint 第三技能 zh-lint:简明技术中文静检 | tests/test_project_evo.py |
| REQ-025 | implemented | must | evo-agent 第四技能 agent-prim:舰队互操作五原语操作面 | tests/test_project_evo.py |
| REQ-026 | implemented | must | zh-lint 汇报面吸收(结构律与状态词与验证状态与五模板) | tests/test_project_evo.py |
| REQ-027 | implemented | must | agent-prim 升格 prim v3 契约对齐(to 统一投递与 id 三产生式与 status 四态) | tests/test_project_evo.py |
| REQ-028 | implemented | must | agent-prim R0 三反射收编(门控 v2 与 read 隐式收件与拒投代记) | tests/test_project_evo.py |
| REQ-029 | implemented | must | herdr 技能淘汰序与 agent-prim 唯一操作面(附 R1 三件复核收编) | tests/test_project_evo.py |
| REQ-030 | implemented | must | agent-prim 信封 v2 对齐与 agent 命名标准(工作台-类型-编号) | tests/test_project_evo.py |
| REQ-031 | implemented | must | R2 复核收编:命名起名校验与取用行降级 | tests/test_project_evo.py |
| REQ-032 | implemented | must | 市场重构:两插件 dev 与 evo,裁四 skill 与五原语拆分 | tests/test_project_evo.py |
| REQ-033 | implemented | must | lint 三 skill 合并为 dev-lint | tests/test_project_evo.py |
| REQ-034 | implemented | must | grok 业界先例评审吸收(收口、独立 semver、命名细节、distil 压缩、环境变量) | tests/test_project_evo.py |
| REQ-035 | implemented | must | 拆中文面:zh-lint 复独立 skill | tests/test_project_evo.py |
| REQ-036 | implemented | must | zh-lint 删除(中文面退出 skill 面) | tests/test_project_evo.py |
| REQ-037 | implemented | must | 对抗 review 协议单收编(三新动词、重载铁律、sha 反射、rollout 段) | tests/test_project_evo.py |
| REQ-038 | implemented | must | 差异表对 ef8fca6 全刷(互审 CONFIRM 家庭作业) | tests/test_project_evo.py |
| REQ-039 | implemented | must | 改面收编:tasks 实时任务面与 herdr_run 容错 | tests/test_project_evo.py |
| REQ-040 | implemented | must | 六原语收编:ctx 对话历史域 skill | tests/test_project_evo.py |
| REQ-041 | implemented | must | ctx skill 对齐 prim v3.1.3(直连双闸与 --around 与多词 snip) | tests/test_project_evo.py |
| REQ-042 | implemented | must | evo 插件 skill 减熵批(正文只留正确用法) | tests/test_project_evo.py |
| REQ-043 | implemented | must | 命令指导 SKILL 写作标准采纳与六域过标 | tests/test_project_evo.py |
| REQ-044 | implemented | must | 信封 from 机器段目标感知同步(v3.1.7) | tests/test_project_evo.py |
| REQ-045 | implemented | must | 信封取用行全原语化同步(v3.1.8) | tests/test_project_evo.py |
| REQ-046 | implemented | must | skill 对抗审核 F 项修复(grok 审单) | tests/test_project_evo.py |
| REQ-047 | implemented | must | 双轨制信封与房间面收编(核验单 F1-F4) | tests/test_project_evo.py |
| REQ-048 | implemented | must | 命名标准六裁定对齐(v3.2.4) | tests/test_project_evo.py |
| REQ-049 | implemented | must | 英文面自查与 hst 2.15.0 台对齐(批159续) | tests/test_project_evo.py |
