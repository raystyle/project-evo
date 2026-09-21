# Changelog

本文件记录 project-evo skill 及本仓库的所有可交付变更。格式：新增/变更/修复/移除 + 日期；先写 `[Unreleased]`，发布时转版本（git tag）。

## [Unreleased]

### 新增(2026-09-21,第八十批:评审闸门轮工位实踩吸收)

- herdr-flywheel references/pitfalls.md 增两坑(三段式):一为管道吞门禁退出码(门禁接 tail/grep 后 `$?` 为末命令,红态假绿,曾致红提交直推远端只能 forward 修;修法为门禁裸跑或显式取 `${PIPESTATUS[0]}`,红态绝不进 commit 分支);二为评审格随 codex 退出被回收(/quit 后整格回收、pane ID 失效,旧格 cwd 可指向已删目录而屏面仍 Ready;修法为退出后 pane list 复查,重驻走右分新格加仓内 cwd)。实证标注留日期不留仓名,吸收即提炼。

## [0.10.0] - 2026-09-17

> 第七十七至七十八批合并发布:cli-docs 对外面双标准 skill 与 Prove2Me DAG 协作模型吸收进飞轮,四插件十一 skill 形态。

### 新增（2026-09-17，第七十八批:Prove2Me DAG 协作模型吸收进飞轮）

- 用户立单:Notion 核验笔记(Prove2Me 多 agent DAG 协作模型,笔记一手依据 Anthropic FLT 形式化材料)研究落点裁定 S009 档案加 herdr-flywheel 吸收,不新建 skill(触发面与飞轮重合,协议唯一权威源不切分;材料一半原则飞轮已有等价物)
- **S009 研究档案**:模型十二则核验留档(六态标注,信源点名止于档案面),与飞轮对照定分流:四则已有等价不重复吸收(验证器独立、产量非完成、幂等甄别、依赖变化雏形),五则真新增加依赖变化升格共压六纪律,两则留档不吸收(deprecated 两事区分、检索子串匹配)另产量数字一件留档;分流口径注随评审 G1/G2 补(S009 分流段)
- **herdr-flywheel 吸收**:SKILL.md 新节「并行派单与义务图」六纪律(台账只记还欠什么、条件归约先接线含闭包清账推论、租约与改派、依赖变化必重评估、扩容前瓶颈三判、任务与尝试分开记),references/parallel.md 操作细化(台账五字段、条件断言派单写法、失联改派、重评估三选一、瓶颈三判判据、四步协议映射);纪律标 [经验] 中转态,本飞轮未整轮实测,首跑回填
- 同步面:SKILL frontmatter 触发词加并行派单与义务图、双 manifest 与市场条目描述逐字同、根 README 意图表、evo-herdr README、docs 地图 herdr 行、references 索引与头注、research 登记、ROADMAP、diary;顺手正一条:docs 地图补 S008 漏行
- 收尾补笔(用户令,挂账清零):parallel.md 任务与尝试独立小节当批落位(尝试五元、先过验收记账、旧产物不覆盖完成态),头注回填义务只剩实证标记,S009 口径注与 SKILL 参考行同步

### 新增（2026-09-17，第七十七批:cli-docs 对外面双标准 skill 增编）

- 总台立单(用户令):为 evo-adr 立仓无关通用 SKILL(照 build-release 形,私有名零出现,归口裁定新立并与 doc-gov、code-kit 的 tool-cli-agents 分工互引);ADR-0014 修订 ADR-0010 清单为十一 skill,REQ-006
- **甲面 README 标准**(references/readme-standard.md):四业界标杆(ripgrep、fzf、bat、fd)README 实读研究,共性表提炼;四节主骨架定稿:项目介绍(徽章加定位加特性加演示加何时不用)、部署(全平台安装加升级加校验)、配置(配置文件样例加环境变量表)、使用(教程式渐进示例加集成配方加选项指 help 与手册);可选尾节排障开发许可;写法纪律(示例驱动、渐进、alert 提示块、配置给完整样例、全集不内联)与反面清单;README 骨架模板可拷改
- **乙面 agent 三件起步**(references/agent-face.md,二号补单时点口径,三号补单定四件见末条;总台细则补单定为旗标七件加类型化 CTA,双语言参考 incur 形):一 --llms 手册面(旗标恒 --llms,裸 markdown 紧凑手册至多 120 行,--llms --json 机器形,活命令树渲染禁手维护,全派生或 curated 加漂移守卫两形,stdout 退出 0 禁交互);二 输出协议:旗标七件(--filter-output 键路径含数组索引、--format toon/json/yaml/md、--full-output 全信封、--help/-h、--llms、--json 简写互斥、--schema 三面 JSON Schema)加信封 ok/data|error/meta/commands;commands 即类型化 CTA(command,args,description),ok 与 error 回执都可携带,人读形渲染(初稿 Next: 块,终形 Suggested commands 见末条),错误 stderr 单行 JSON,退出码 0/1/2,字段序保插入序;三 自省(活命令树唯一真源,help 与手册与 schema 三面同源,漂移守卫锁全旗标覆盖,版本从载体注入)
- 模板五节可拷改:README 骨架、手册骨架、信封与旗标七件、双语言实现模板(TS 加 Rust 各一份:信封结构加 ok/error 构造加 CTA 折算与 Suggested commands 渲染)、自省核对清单;tool-cli-agents 第二节加互引注
- 同步面:双 manifest 与市场条目描述、守卫 SKILLS 十一 skill、pre-commit 第十一段、AGENTS 与根 README 与 docs 地图与 gates 计数、evo-adr README 五 skill 化、ADR-0014 与 REQ-006 与索引、ROADMAP、diary
- 总台四号补单(裸调用面):增第五件,无参进入不弹交互不纯报错(导航事件非错误),紧凑形(一行定位加指 --llms 与 --help,agent 首荐)或全貌形(帮助体),退出码恒 0,管道模式显式分离;templates 补裸调用示例紧凑与全貌各一;乙面口径全量刷五件
- 总台三号补单复入(默认帮助说明标准):乙面四件定形,新增默认帮助面(节序:头行 name@version、Usage synopsis、Arguments、Options、Examples、Global Options 字典序枚举全值默认后缀弃用前缀、Environment Variables 脱敏;描述与 schema 同源单一真源;组与叶双形);CTA 契约按参考实形(字符串或 command/args/options/description 折算、CLI 名自动前缀、Suggested commands 渲染、进信封 meta 人机同源);旗标全家(七件必选加可选扩展:llms-full、mcp、token 三件、update、version、config,裁剪显式);mcp 与 http api 裁为可选附录章(默认不做);双语言模板各带帮助输出示例一份(TS 叶形加 Rust 组形)

## [0.9.0] - 2026-09-17

> 第七十五批合并发布:build-release 流水线标准指导 skill,四插件十 skill 形态。

### 新增（2026-09-17，第七十五批:build-release 流水线标准指导 skill 增编）

- ohmycloud 总台派单(用户令),六轮追正定形:全仓编译打包发布流程标准落位 **仓无关指导 SKILL** `build-release`(evo-adr 第四 skill,ADR-0013 修订 ADR-0010 清单为十,REQ-005;herdr-flywheel 同形态先例:SKILL.md 加 references,任何仓可套用);起草期的 doc-gov references 草稿篇 flow-build.md 退役并入,doc-gov 三面回退 9 篇
- **类型路由制**:「什么样的项目,怎么做」,六型配方(go 交叉六目标、rust 本地三目标(主开发机交叉加 mac 实机)、npm pack 离线包、py wheel、native 自含静态加跨宿主容器闸、manifest 纯文档仓),每型七要素(构建矩阵、测试闸、打包与边车、发布、播种、自升级判据、元数据对齐);CI 不可产的大件分发不属本面,边界一句注记
- **三段式正源(用户终裁)**:本地编译和打包(主开发机交叉加实机矩阵,npm pack 与 python -m build 本地出离线包,测试闸与版本闸与解包冒烟先行)到 GitHub 产物发布(gh release 直发 --latest 禁 draft)到 CI/CD Action 自动播种 R2(Release published 触发拉资产 rclone 推段,零上传红灯三段报数,dispatch 补推带 tag 入参;CI 面不编译不打包,测试岗随仓裁);模板形态取自家族仓实测实践参数化去私有名(env-remote r2: 配置形、三目标矩阵、单顶层目录包形 win zip 他 tar.gz、逐包边车、段制三段)
- **可拷改模板**(references/templates.md 四节),形态取自家族仓实测工作流(git 历史在档)参数化去私有名:本地编译与发布命令面(版本闸、测试闸、交叉编译、包形与逐包边车、解包冒烟、gh 直发与 dev prerelease 滚动)、各型本地编译片段、CI/CD 播种 workflow(release published 触发、拉资产、env-remote r2:、版本段 immutable copy-only 加 stable sync delete-excluded、零上传红灯三段报数、dispatch 带 tag 入参)、自升级契约核对清单
- **通用性终约束(最高优先)**:标准通用件,私有名称与私有信息零出现(正文、注脚、示例、模板默认值全禁);契约全部抽象参数化(镜像域 `<mirror-host>/<tool>/<version>/`、安装管理器元数据抽象化、Secrets 通用 R2 族);实证引一律不进 SKILL,留档仓内 diary
- 同步面:双 manifest 与市场条目描述、守卫 SKILLS 十 skill、pre-commit 第十段、AGENTS 与根 README 与 docs 地图与 gates 计数、evo-adr README 四 skill 化、CHANGELOG、ROADMAP、diary
- 总台追正一笔:补上游追新专节(fork 维护仓配方:upstream merge、冲突面纪律、版本 bump、回跑矩阵)

## [0.8.0] - 2026-09-16

> 第六十五至七十三批合并发布:四插件重组定形、评审闸门实战与 gh-issue,九 skill 形态成军。

### 变更（2026-09-16，第七十三批:发现通道收敛 llms 入库）

- 舰队裁定吸收:skill 面退役,agent 发现通道收敛 llms,`--llms` 定位为紧凑版 CLI 使用说明书(stdout 可管道,markdown 加 `--json` 双形态,按需零常驻);七仓对账后入库(hst 库投影型 ADR-0005、ark D50 在途、reader 与 browse 与 omc 旗标型已落地,OfficeCLI 与 clean-chrome 未动)
- code-kit tool-cli-agents.md:发现契约三通道改双通道(--llms 默认推荐,mcp add 需编排时用);skill 通道老记录按用户裁定直接剔除不留退役说明(通道表行、拆分要点与落地判据行、多面渲染与弃用同步与派生面枚举中的 skill 面);fleet --llms 先例与漂移门禁实证入文
- research references/reader.md:reader skill 双入口记录剔除,索引与命令契约统一 `--llms` 与 `--help` 口径;web.md 双入口改单入口(快核 F1)
- doc-gov base-projection.md:agent 检索面补 CLI 工具双形态(CLI 面 --llms 说明书加库面投影)与漂移守卫三型(旗标全覆盖断言、surface 同源锁、--check --strict);SKILL.md 路由行同步

### 新增（2026-09-16，第七十二批:gh-issue skill 增编）

- 新增第九 skill `gh-issue`(evo-adr 第三 skill,ADR-0012 修订 ADR-0010 八 skill 清单为九):命令出错自动上报 GitHub issue 工作流。两条用户裁定入文:无草稿确认闸直接 gh issue create 自动发;发前双通道去重(gh search issues 加 gh issue list,open 实质同一票否决,回执附既有链接)
- 五步成文:定位目标仓(git remote 与 gh repo view 自取,禁硬编码映射表)、四格判定矩阵、六段模板正文(截断保首尾标中段、脱敏对齐 secret-scan)、label 与 viewerPermission 预检后发单、三态回执(已发加查重摘要、命中未发、未能发);references 三篇:gh-ops(仓解析序、去重矩阵、预检、坑表)、issue-body(标题公式、模板、回执)、README 索引
- 命令面九条本会话实证:remote/repo view/label list/双通道搜索实跑;create 与 close 以本仓自发实证单走通验后即关;label 硬带不存在的 422 整单失败路径实证(预检必要性的依据)
- 同步面:REQ-004 走全流程(implemented 加 trace)、ADR-0012 与两处索引(ADR-0010 替代列回指)、双 manifest 与市场条目描述逐字同、守卫 SKILLS 九 skill、pre-commit 第九段断链、AGENTS 与根 README 与 docs 地图与 gates 计数八改九、evo-adr README 三 skill 化、ROADMAP 里程碑、diary

### 修复（2026-09-16，第七十一批:第七十批评审回执处置）

- codex 全量回执 4F 加 8G(任务协议产物 /tmp/project-evo-review/findings-70.md,增量面自洽零新患),总台逐条独立核实全真后全修:F1 至 F3 三处「四插件七 skill」陈旧计数刷正(marketplace 元数据、docs 地图、gates 门禁表;第六十八批 ADR-0011 扩八 skill 时同步面漏改,git blame 落 e32d1ab);F4 code-kit SKILL 的 md-guard 四类禁字自述对齐 mdrules.py 权威(box-drawing 移出机检类,补 emoji 与全角字母数字)
- G 批八项同批结清:G1 tool-typescript 十二/十三/十四节号倒置重排(flow-release「第十节」指针经核实不受牵连);G2 exp-sedimentation 两条链 box-drawing 伪流程图改 mermaid(围栏内机检盲区实抓,Must not 违例);G3 AGENTS scan 豁免句删「本文件 Commands 节自举示例的 AWS 公开样值」无据指代(全历史无 AKIA);G4 ADR-0005 索引标题对齐 frontmatter title;G5 ROADMAP 阶段二/三头状态翻正(与表内已完成行矛盾);G6 flow-release 空表格行清除;G7 pyproject 维护环境版本钉齐 0.7.0;G8 security-audit 补 references/README 索引(14 篇与 SKILL 意图路由同序,守卫断言仍留积压并同步措辞)

### 变更（2026-09-16，第七十批:评审格仓内 cwd 变体与信任屏处理序沉淀）

- herdr-review panes.md:评审格 cwd 定形为两形态按评审范围裁定:跨仓收件用用户级 home(原形态),单仓专属用该仓 cwd(用户裁定本仓 review 只针对本仓,evo-codex-review 驻 project-evo 仓内实建);带起节补 3a 处理序:仓内 cwd 首启弹 codex 目录信任屏,agent start 的 interactive_ready 是假阳,pane read 实证后 pane send-keys enter 替答,信任裁定归用户(本仓与自建仓默认可信,陌生仓先问);坑节补信任屏假阳条目;SKILL.md 形态节同步;yolo 与信任态以 hst doctor 只读复核入顺序纪律
- 修复:docs/diary/2026-09-16-飞轮批与封版v0.6.0.md 第六十九批标题 ASCII 括号触发 PE-10(第六十九批日记钩子补引入,改「与」并入主题),check 门禁恢复 12 PASS

### 变更（2026-09-16，计数原语对齐:env-platform 五端四机刷正）

- env-platform.md 第十节「四平台测试矩阵」计数原语按用户 2026-09-16 裁定刷正为「五端四机」:五端 = wsl、lan-win、lan-ubuntu、lan-linux、lan-mac 跨四机(wsl 与 lan-win 同机两面,Linux 面与 Windows 面各自成端),lan-linux2 不在矩阵;与 reader_rs 侧 AGENTS 同口径(总台转单,reader_rs 已落 c0a99b9);同文件 103/105 行既有「五端」表述核对一致零改动

### 修复（2026-09-16，第六十九批:第六十七批评审回执处置）

- 评审闸门首次实战:命名评审格 evo-codex-review 实建于 project-evo 工位右侧(herdr pane neighbor/split 加 agent start),按 herdr-review 请求模板实发第六十七批评审单;codex 回执五面全过(清单一致、守卫与实况、七 skill 零死链、跨插件前缀、吸收件可跑加 interop 五份真样例复跑),四项定夺处置如下
- S005/S006 活文档旧路径复跑命令修活(夹具与 ab.py 改指 plugins/evo-codesec,加迁移注记);README 钉版示例改现存 tag v0.7.0;report SKILL 实证数字改区间(130 KB 至评审轮五份 306 至 420 KB)
- Linux 面 CJK 字体静默丢字坑入档:triple-output 加字体前提节,SKILL compatibility 与坑节同记,render.py 检测 typst 未知字体告警并显式提示(退出码不动,字体族参数化列 ROADMAP 积压);守卫断言扩展与机检盲区(市场描述一致性、references README 存在性、md-ref-scan 多根、散文指针)同入积压
- 快核轮两处必修同批结清:report SKILL 节号指针悬挂(插字体节后 docx 管线第四改第五);ADR-0011 标题括号触发 PE-10(第六十八批引入,评审修复轮门禁跑漏骨架自检所致,教训入 herdr-review receipt 纪律:门禁跑全集);S006 头部补旧称沿革注记;节号引用入机检盲区积压行

### 新增（2026-09-16，第六十八批:herdr 评审闸门 skill 增编）

- 新增第八 skill `herdr-review`(evo-herdr 第二 skill,ADR-0011 修订 ADR-0010 七 skill 清单为八):推送前评审闸门工作流,沉淀自 hst_rs 等工位实证(十五条发现五轮交叉复核链、D46 至 D53 推送前门禁请求回执原文、命名评审格 hst-codex-review 实况);内容按吸收即提炼:评审请求五件模板(编号门禁语句/提交面/改动面逐条/背景已验证据/分级指令)、F 必修/G 建议/CONFIRM 三态回执与轮次至终审放行、发现逐条核实再修(高也可能部分真)与修复本身过二轮复核、多 agent 交叉互补、评审窗格挂位命名与查看、hst trace 对话检索
- 评审格检测带起自愈程序入 panes.md:查工位格右侧有无可用格(neighbor),无则右分 40% 建格起 codex 命名驻场,有则直接对话;全流程命令本机实证(project-evo 工位右侧实建 evo-codex-review 并按请求模板实发第六十七批评审单);立 REQ-003
- 同步面:evo-herdr 双 manifest 与市场条目描述改两 skill、守卫测试 SKILLS 断言八 skill、pre-commit 补 herdr-review 断链行、AGENTS 定位行与 Commands 节、根 README 与插件 README、docs 地图;herdr-flywheel 参考节加反向指针(协议面与评审特化互指)

### 变更（2026-09-16，第六十七批:市场更名 project-evo 与四插件重组）

- **破坏性**:市场名 `projectevo` 改 `project-evo`,GitHub 仓同步改名 `raystyle/project-evo`(旧地址重定向);单插件 `project-evo` 重组为四插件 `evo-adr` / `evo-codesec` / `evo-research` / `evo-herdr`(四插件同版本线,自 0.1.0 起);斜杠前缀 `/project-evo:*` 全部变为 `/evo-adr:*`、`/evo-codesec:*`;旧市场消费者须卸旧装新(旧缓存 `cache/projectevo/` 整目录可删)
- dev-evo 按意图路由拆细为 `doc-gov`(治理知识面,references 9 篇)与 `code-kit`(骨架与门禁工具箱,references 8 篇加五脚本加模板加 verification),17 篇参考总量不变构成重分;立 ADR-0010(supersede ADR-0001,修订 0007/0009 形态条款,0004 档案条款由 doc-gov 承载)
- super-research 拆 `research`(发现/获取/研读管线)与 `report`(研究成文三件套):report 吸收家族研究仓报告生成实践(断言式骨架、md/pdf/docx 三件套、Typst 渲染、版式复检口径、信源分级存档与登记),按「吸收即提炼」入库;docx 渲染与版式复检带外部依赖以 references 知识形态承载,脚本面仅收零依赖 render.py(参数化项目根、--check 编译门禁、risky-bold lint;修复吸收件「无二级标题时 cmarker 报 Markdown must be a string」缺陷);render 实证过(WSL interop 调 typst,130 KB 样例)
- 清单与合同同步:双 marketplace 四条、四插件双 manifest 各四份共十份 JSON 重写,AGENTS 定位/Commands/Must/Must-not/Read first/部署节、根 README 与四份插件 README、docs 地图、gates.md、skill-spec.md 分层原则、githooks pre-commit(顺手补 herdr-flywheel 断链扫描既有缺口)、.tools 默认根、.claude 两份 settings、CI 冒烟面、三个测试文件路径常量同步;清单守卫测试重写为四插件/七 skill/同版断言(立 REQ-002 走全流程)
- 构造纪律入合同(ADR-0010):新写与改写 SKILL.md 命令块实证准入(写进去的命令当会真跑过)、脚本即交付物、一条活路、坑出实碰;skill 依赖的外部命令(gh、bh、reader、aria2c、typst 等)全平台分发安装由宿主工具链 omc 与 ark 统一维护,skill 只认 PATH

### 新增（2026-09-16，第六十五批:check --json 机器读面与全量报告）

- `check.py` 新增 `--json`:stdout 出 JSON 机器读面取代人读逐项表,schema 为 `{"ok","counts"(pass/fail/skip),"results"[{id,status,note,violations}]}`,violations 是该检查全部违规项(file:line 或路径串);退出码 0/1/2 不变,出错仍 stderr 文本;立 REQ-001(本仓首件,requirements 体系首次走全流程)
- 全量报告:PE-05/06/07/08/10/11/12 去前 5 与前 4 截断;PE-11 由每文件只报首行改逐行全列(ark_rs 修一轮冒一轮三轮才清的根因之一);check() 返回值扩四元组,既有下标消费不破
- 文档面同步:commands/check.md、SKILL 第四节、verification/command-test-cases.md、gates.md check 节、tool-python 退出码行;ROADMAP 两待定行翻已完成;本仓自检 PE-07 由 SKIP 转 PASS(首件 REQ 落地)

### 修复（2026-09-16，第六十五批:commands/check.md PE-13 笔误）

- `commands/check.md` 描述「PE-01 至 PE-13」为笔误,脚本检查面实为 PE-01 至 PE-12;CHANGELOG 历史条目按当时事实保留不改

### 新增（2026-09-16，第六十六批:herdr 飞轮 skill 增编与 flow-flywheel 退役）

- 新增第五 skill `herdr-flywheel`(多仓 herdr 工位飞轮协作:派单/回执/断言/吸收四步协议,吸收原 dev-evo flow-flywheel.md 全量、herdr 命令面要点与家族实践坑;工位带起顺序纪律入正文:hst init --yolo 先于 agent 驻场);立 ADR-0009(supersede ADR-0008,ADR-0007 四 skill 形态条款扩为五)
- `flow-flywheel.md` 从 dev-evo references 退役删除(18 篇回落 17 篇):SKILL 路由、references 三层索引、env-platform 交叉引用全量改指新 skill,全仓 grep 零死链
- 清单与合同同步:双 marketplace、双 plugin.json 描述与 Codex 接口描述四 skill 改五,AGENTS 定位与 Commands 节、docs 地图、清单守卫测试同步;新 skill 配 references/pitfalls.md 坑实录(六坑三段式)

### 移除（2026-09-16，第六十六批:flow-flywheel.md 退役）

- `plugins/project-evo/skills/dev-evo/references/flow-flywheel.md`:内容全量并入 herdr-flywheel skill(补令裁定二择一为老的清除,单一真相不留双份);CHANGELOG 历史条目按当时事实保留

## [0.7.0] - 2026-09-16

> 第五十七至六十四批合并发布:治理基建八批(总台统一封版令)。

### 新增（2026-09-16，第六十四批:pwsh 统一载体、多仓版本标准与统一分发体系）

- env-platform 新增第十一节「统一验收脚本载体 pwsh」:五端一份不再三套、非登录 shell PATH 兜底、五端版本对齐判据、既有跨平台载体不强制迁移;flow-testing 跨栈载体节加指针,本仓 AGENTS 环境节引用
- flow-release 新增第七节「多仓版本标准」:semver 触发判据、各仓版本载体唯一权威、统一封版协调(总台令加 conclusion 自验加 catalog 镜像滚动)、版本对齐表模板
- flow-release 新增第八节「统一分发体系」:种子发布链(catalog pin 加签名加对象桶加定时)、镜像域版本段分发(sha256 边车加双通道回退)、自升级三通道(dev 加 stable 加 git,镜像回退腿,digest 判新);职责分工入节(omc 分发运维与版本管理,ark 落地执行验收,用户裁定)

### 新增（2026-09-16，第六十三批:全平台连接姿势与多仓飞轮协作篇,ADR-0008 边界修订）

- env-platform 新增第十节「全平台连接姿势」:WSL 到宿主恒走 127.0.0.1 回环 ssh 加 interop 直调不走宿主 mesh IP(mirrored 共享节点身份自连被 RST 属结构性)、lan 三端 mesh 随时随地、四平台测试矩阵与端点支撑;各仓 AGENTS 环境节引用此口径
- 新增 references/flow-flywheel.md(多仓飞轮协作:工位形态、派发自包含、回执 conclusion 自取、端点测试支撑、吸收纠错分流;六仓四轮实证提炼);references 17 到 18 篇,立 ADR-0008 按 ADR-0007 边界纪律显式修订(首例)
- 本仓 AGENTS 环境节补连接姿势引用句

### 新增（2026-09-16，第六十二批:项目治理终态定形与四技能治理面定调）

- 立 ADR-0007:治理终态五件套(ADR/REQ 体系、diary 与 research 档案、三栈文档即代码标准与工具、agent CLI 三栈标准、AGENTS 五节合同与 17 篇边界)冻结,动终态面须立新 ADR 显式 supersede
- 用户定调入定位口径:ProjectEvo 四 skill 同属项目治理面非业务工具面(dev-evo 文档体系治理、super-research 资料检索治理、secret-scan 密钥隐私治理、security-audit 安全审计治理),AGENTS 与 README 定位句同步

### 变更（2026-09-16，第六十一批:agent CLI 三栈标准落位与终态清理）

- tool-cli-agents 新增第十一节「三栈落位与输出面增量」:token 计量与分页(cl100k_base)、输出过滤点路径、{ok,data,meta} 信封与 retryability、agent 探测与输出策略;三栈落位表(Rust=incur-rs 模型 clap derive 派生、TS=incur 模型 Zod、Python=argparse 加 pydantic,hst 的 format 信封为活例);源仓深读吸收(wevm/incur 与 gakonst/incur-rs,克隆本地分析)
- 终态清理(用户裁定 dev-evo 终态=ADR+研究日记+三栈文档即代码标准工具+agent CLI 标准):退役 env-environment.md(ome 家族工具索引)、flow-events.md(事件执行模型)、tool-selection.md(依赖选型),references 20 到 17 篇,SKILL 路由与索引同步,残留交叉引用(含 SKILL 六层表 interrogate 旧值换 ruff D)清理

### 新增（2026-09-16，第六十批:三栈契约注释格式纪律吸收）

- base-projection 新增「契约注释通用准则」六条跨栈共用:公开项必写加覆盖率 lint 钉死、首句成句、不重复机器可推信息、示例必须真实可测(断言收尾兼回归、外部服务 mock 保 CI 可重复)、失效即失败(文档与行为不一致视同功能 bug)、风格单一存量改动时补齐
- tool-rust 补章节纪律与 clippy 三 lint:# Examples/# Panics/# Errors/# Safety 固定用词加 missing_errors_doc/missing_panics_doc/missing_safety_doc,compile_fail 错误示例口径
- tool-python 补格式基准:PEP 257 加 Google 风格、章节顺序 Args 到 Returns 到 Raises 到 Examples、doctest 限定格式、覆盖率机检由 interrogate 改 ruff D 规则集(对照表与 base-agents-contract 同步)
- tool-typescript 补标签白名单与禁 JSDoc 类型声明语法,@example 用 fenced block 标语言
- 来源:外部三栈内嵌文档标准参考件,按吸收即提炼入册,不点名来源

### 变更（2026-09-16，第五十九批:Rust 栈 aidoc 投影强制化,ADR-0006）

- 用户裁定推翻 bin-only 豁免口径:Rust 仓 aidoc 投影为强制标配,「无自有 API 面项目」范式范围限定为构建树与补丁仓等非三栈形态,Rust 仓不适用
- tool-rust 投影节改强制口径(受众是维护者与 agent);base-projection 无自有 API 面节加范围限定;各仓既有「不适用」裁定句随重构撤换

### 新增（2026-09-16，第五十八批:aidoc 集成补全）

- base-projection 对照表下补 Rust 侧管线段(/// 为源、cargo aidoc 生成 docs/aidoc、--check --strict 漂移门禁),与 TS/Python 两段对称
- tool-rust 投影节补工具渲染格式豁免实务:无开关可改的分隔符类禁字走路径级豁免在册,漂移真门禁仍是 aidoc --check,源头能改就改不为生成物开口子(首个 aidoc 全量投影仓实战提炼)

### 新增（2026-09-16，第五十七批:无自有 API 面项目范式入册与三机制反馈登记）

- base-projection 新增「无自有 API 面项目」小节(构建树与补丁仓):公开契约等于字节确定性产物 regenerate-and-diff 门禁、构建门禁进 Commands、一句裁定入地图;来自首个构建树仓用户讨论轮,提炼为通用表达
- ROADMAP 登记三机制反馈:check.py 下游拷贝哈希锁、仓本地路径排除标记 .evoignore、C/C++ 第四栈裁定已拒绝(通用件入册替代)

## [0.6.0] - 2026-09-16

### 新增（2026-09-16，第五十六批:三栈工具篇补齐与档案机制入册,ADR-0005）

- 新 reference `tool-python.md`:Python 工程合同(uv 与 PEP 723 零依赖、docstring 契约、MkDocs/Griffe 投影、pytest 与 doctest 门禁);三栈工具篇齐(Rust/Python/TypeScript)
- 新 reference `flow-archive.md`:diary 一天一篇与裁定留痕、research SNNN 编号与六态与索引登记、择要升 ADR、结构保留红线、旧 proven 与 mistakes 承接
- base-projection 对照表下补 Python 侧管线段;SKILL 意图路由两行、references README 三层索引同步(18 篇到 20 篇);立 ADR-0005

### 变更（2026-09-16，第五十五批:check PE-10 报错改相对路径）

- omc 飞轮实踩:报错只给文件名,重名 README.md(根加 docs 各一)定位错文件;PE-10 违规项改输出仓库相对路径(PE-11 本批前已改,PE-12 原生相对)

### 新增（2026-09-16，第五十四批:dev-evo 保留 diary 与 research 档案结构红线固化）

- 用户裁定:diary 与 research 是 dev-evo 骨架保留核心结构,不是可裁撤项;后续收敛或裁剪批不得动两目录结构地位,guides 仍按需生长
- 立 ADR-0004(仓侧决策锚);base-init 两处口径同步:Step 2 的 research 缓建问法改结构保留暂空合法,Step 4 裁剪原则拆分 guides 按需与 diary/research 保留

### 新增（2026-09-16，第五十三批:check 的 PE-11 豁免通道与仓名小写对齐）

- `check.py` 新增 `PEVO_CHECK_ALLOW` 路径级豁免（分号分隔正则，只作用 `docs/` 下档案的 相对路径:行，命中报 SKIP 留审计处数；根三件 AGENTS/README/CHANGELOG 是活跃面，机制上永不受益，全域正则也吞不掉）。经 security-audit 指导模式聚焦审查后的加固项
- `docs/guides/gates.md` 补 check 标准命令与豁免正则节；base-init 存量迁移路径接入门禁豁免口径；AGENTS Commands 的 check 行加指针；tests 增豁免三分支用例（未设 FAIL/命中 SKIP/全域正则不掩护根三件）
- GitHub 仓名已改小写 `projectevo`，活面全仓对齐：根与插件 README 安装命令、AGENTS 部署行、双 manifest homepage/repository、ROADMAP 指针、dev-evo SKILL 安装通道、git remote；CHANGELOG 历史条目按当时事实保留
- `.gitignore` 增智能体配置类四目录（.agents/skills/、.grok/、.hst/、.kimi-code/，hst init 部署产物不入库）

### 新增（2026-09-15，第五十一批:security-audit skill 中文化集成）

> 源:Cloudflare security-audit-skill(MIT,skill 目录内附 LICENSE);用户裁定转换为中文并集成,技能名 security-audit 不变。

- 新 skill `plugins/project-evo/skills/security-audit/`:SKILL.md 中文版(双模式/六阶段工作流/覆盖账本/写隔离/预算闸门/核心原则/反模式);14 篇领域专题全量中文化进 references/(前缀 audit-:recon/hunting/attack-classes/web-auth/client-side/ai-llm/data-lifecycle/cloud-deploy/memory-binary/ipc/protocols-rpc/resource-exhaustion/supply-chain/reporting),交叉引用同步新文件名
- 校验脚本随行(scripts/,Node .cjs 原样):validate-findings 与 validate-coverage-ledger(含 .test.cjs)、report-schema.json;注记:validate-findings.test.cjs 在本机 Node 24.20.0 下 34 测 22 过 7 挂,源仓同环境同结果(上游自带,与拷贝无关;校验器本体行为正常)
- 翻译纪律裁定:正文中文、agent 提示词围栏块保留英文原文(源 skill 设计为逐字复制进 hunter/verifier prompt 的模板,保真优先);md-ref-scan SKIP 增补审计运行时产物名(REPORT.md 等 5 个)
- 六件套同步:三清单四 skill 化并升版 0.6.0、AGENTS 定位、根 README 与插件 README(SKILL 表/用法/发布)、githooks 断链扫描加第四路、tests 守卫四 skill 断言与 security-audit 脚本在位、docs/README 索引
- 版本 0.5.0 未及发布,与第五十、四十九批合并以 0.6.0 发布

### 变更（2026-09-15，第五十批:docs-evo 改名 dev-evo,知识体系转文档即代码）

> 用户裁定:吸收三份经验(Rust workspace 实证、Python 数据管线实证、TypeScript 方案)重构为「文档即代码」体系;三栈机制对照;保留 diary 与 research;本仓自身 docs 一起迁移。旧体系(根原语 PRD/GOAL/PLAN/TODO/INDEX、docs 六目录、五步工作流、双向问答、P/S/R/G/M/D 编号)全面退役。

- 改名:skills/docs-evo git mv 至 skills/dev-evo,frontmatter 同步;全仓 88 处引用同步(清单 4 份、hooks 3 处、CI、.tools、commands、AGENTS/README、双 skill 交叉引用、tests、docs 索引);历史记载(CHANGELOG/ROADMAP/S 档案)保留原样
- SKILL.md 重写:新定位文档即代码;意图路由新体系问题前置;速览换六层模型(L0 形态到 L5 索引)、新文件地图、三栈机制对照、ADR/REQ 状态机(mermaid)
- references 重组 17 到 18 篇:新增 base-agents-contract/base-adr/base-req/base-projection/tool-rust 五篇;改写 base-init/base-writing-standards/tool-typescript(融合 TSDoc 与 API Extractor)/exp-pitfalls(十八条);退役 base-primitives/base-docs-directories/flow-workflow/flow-inquiry 四篇;保留九篇清理旧体系引用与外部仓名(吸收即提炼:成品不点名外部仓库)
- scripts 重写:init.py 新骨架(AGENTS 五节合同 + docs 五目录 adr/requirements/guides/diary/research,模板 10 件;渲染改 replace 防花括号冲突);check.py 新规则 PE-01 至 PE-12(五节合同、ADR/REQ 状态机与 trace、索引一致、六态、禁字、断链);mdrules/scan/md-guard 不动
- md-ref-scan:SKIP 集合更新为新体系占位名,NNN 占位通配
- 本仓迁移:新增 docs/adr/(README + 补录 ADR-0001 市场形态/0002 uv 退役/0003 office-pro 移除,日期用原裁定日)与 docs/requirements/(空表起步);AGENTS 五节化改造(97 行到 40 行,细则下沉 docs/guides/skill-spec.md,地图在 docs/README.md);本仓首次跑自家 check 自检
- 版本:三清单 0.3.1 直升 0.5.0,后因第五十一批同日并入,合并以 0.6.0 一个 tag 发布
- 已装用户:更新插件后 skill 显示 project-evo:dev-evo;旧骨架项目按 base-init.md 存量迁移路径走(PRD 条目对应 REQ、proven 对应 implemented REQ 加关联 ADR);Kimi 面重拷并删旧 docs-evo 目录

### 移除（2026-09-15，第四十九批:office-pro skill 下线）

- 删除 `skills/office-pro/` 全目录、斜杠命令 `commands/office-cli.md`、专属测试 `tests/test_office_pro.py`
- 引用全量同步:AGENTS(地图/索引/硬规则1/环境事实)、根 README(定位/安装/SKILL表/命令行/钉版)、插件 README(描述/用法/输出/架构/发布版本)、双市场清单与双 manifest(描述改三 skill、keywords 去 office、版本 0.3.1 升 0.4.0)、githooks 去 office-pro 断链段、tests 清单守卫改三 skill、docs-evo SKILL 与 references 去交叉引用、docs/README 去索引行、S007 登记注记移除沿革
- 研究档案 S007 保留(编号不复用,历史沿革在案)
- 已装用户:更新插件后 office-pro 与 /project-evo:office-cli 随之下线;Kimi 面手动删 `~/.kimi/skills/office-pro`

## [0.3.1] - 2026-09-11

### 变更（2026-09-11，第四十八批:aria2c 下载必关 IPv6 入库）

- super-research `references/aria2c.md` 三处落地:标准下载命令带上 `--disable-ipv6=true`、参数表补该行、坑表补「本机网络 IPv6 到镜像站有坑」条目(用户裁定;实证:TUNA 镜像 Ubuntu ISO 关后 16 连接 21MiB/s)

### 变更（2026-09-10，第四十七批:四插件收敛为单插件四 skill）

> 用户裁定:市场应是一个前缀下挂不同 skill 名,而不是四个前缀各挂一个同名域词的 skill。显示目标:`project-evo:docs-evo`、`project-evo:super-research`、`project-evo:secret-scan`、`project-evo:office-pro`。

- 目录:三插件 skill 迁入唯一插件 `plugins/project-evo/skills/`(research 到 super-research、secrets 到 secret-scan、office 到 office-pro,均 git mv 保沿革);`plugins/{super-research,secret-scan,office-pro}` 目录下线
- skill 名与 frontmatter 同步目录名(硬规则);测试新增守卫:四 skill 目录齐备且每个 frontmatter `name` 与目录名一致
- 命令面并入 project-evo:secret-scan 的 `scan` 与原 docs `scan` 同名,按避让规则改 `secret-scan-cli`;office-cli 原名保留(避开与 skill 同名)
- 清单面:双市场清单只留 `project-evo` 一条;插件双 manifest 版本 0.3.0,description 覆盖四 skill;Codex 面 interface 长描述与默认提示词同步
- 引用全量同步:AGENTS 地图与索引与硬规则、README 定位与安装节(Kimi 拷贝路径)、docs/README 索引、S005/S006/S007 底稿、插件 README、四个 skill 内交叉引用(原「市场另一插件」改「同插件 skill」)、githooks 断链三路并一路、tests 两处脚本根
- README 精简重写:收成安装(四客户端一表)、升级(命令面与缓存归位)、配置(协议与钉版与禁字挡板与扫描豁免)、SKILL 介绍(四 skill 表)四节,115 行到 65 行;删掉的裸脚本示例由各 skill 的 SKILL.md 与插件 README 承担
- 已装用户:市场更新后卸旧三个插件、装 project-evo 即得四 skill;Kimi 面重拷 `plugins/project-evo/skills/*`

### 修复（2026-09-10，第四十六批:Codex 面 hook 的 Windows 修法纠错,改用花括号变量）

> 现象:第四十二批发版后,Codex 会话编辑 markdown 仍报 `PostToolUse hook (failed) error: hook exited with code 1`。第四十二批的根因判断有误,本轮纠正。

- 正确根因 [实证: 2026-09-10 codex 源码 rust-v0.149.1 与 main 实取 + 本机 cmd 实跑]:Codex 在 Windows 用 `cmd.exe /C`(取 COMSPEC)执行 hook 命令行(codex-rs/hooks/src/engine/command_runner.rs),且只把命令里的 `${VAR}` 花括号形态按插件环境变量展开(codex-rs/hooks/src/engine/discovery.rs:`command.replace("${key}", value)`,插件 env 含 `CLAUDE_PLUGIN_ROOT` 与 `PLUGIN_ROOT`;Windows 面取 `command_windows.unwrap_or(command)`)
- 纠错:第四十二批的 `commandWindows` 写了 PowerShell 语法 `$env:CLAUDE_PLUGIN_ROOT`,cmd 不认这一形态,路径原样传给 uv,仍退出 1;并非当时判定的"PowerShell 把变量展开成空串"
- 修法:`command` 与 `commandWindows` 统一改 `${CLAUDE_PLUGIN_ROOT}`(Windows 面用反斜杠拼路径);本机 cmd `/C` 跑展开后的命令行退出 0
- 测试:tests 守卫改为"两字段都须含 `${CLAUDE_PLUGIN_ROOT}` 且禁 `$env:`",判据来源写进 docstring
- 教训:跨 shell 的命令面不许按一面的语法臆测,判据要落到被执行方(此处 cmd)的实跑

### 变更（2026-09-10，第四十五批:三兄弟插件补版 0.1.1,同步改名引用）

> 缘由:第四十四批改名动了 secret-scan、super-research、office-pro 三插件内的引用文字(A/B 脚本路径、SKILL 与 README 交叉引用、office 六态措辞),但三插件版本未动,市场按版本号判定无更新,Claude 面装到的仍是改名前的文本。

- 版本面:`.claude-plugin/marketplace.json` 三插件条目与六份双 manifest 同步 0.1.0 到 0.1.1
- 内容:本轮刷新即第四十四批同步后的文本(secret-scan `DOCS_EVO_SCAN` 路径与用例表、super-research SKILL 与 README 交叉引用、office facts 六态措辞)
- 已装用户:`/plugin marketplace update projectevo` 后重装对应插件即得;Codex 与 Grok 面市场升级会整体重拷,但版本号仍须前进才触发刷新

## [0.2.2] - 2026-09-10

### 变更（2026-09-10，第四十四批:skill 改名 docs-evo,消除指代含糊）

> 用户裁定(2026-09-10):skill 名 `evo` 指代含糊,改为 `docs-evo`,与插件 `project-evo` 并读为「文档进化」。同第三十一批口径:插件名与市场安装标识不动,客户端显示收敛为 `project-evo:docs-evo`。

- 目录:`plugins/project-evo/skills/evo` git mv 至 `plugins/project-evo/skills/docs-evo`;SKILL.md frontmatter `name` 与标题同步(硬规则:name 与目录名一致)
- 仓内引用全量同步:仓根 `.claude/settings.json` 钩子、`.github/workflows/test.yml` 冒烟、`githooks/pre-commit`、`.tools/md-ref-scan.py` 默认根与 `.tools/README.md`、AGENTS 地图与索引、README、docs/README、S005/S006/S007 研究底稿、project-evo 插件 README 与三斜杠命令、`hooks/hooks.json` 双面路径、super-research 与 office 交叉引用、secret-scan A/B 脚本(`DOCS_EVO_SCAN`、`_docs_evo_has`、`B_docs_evo`)、tests 两处脚本根;CHANGELOG 历史批次记载保留原样
- 已装用户:`/plugin marketplace update projectevo` 后重装 project-evo 即得新 skill 名(0.2.1 缓存按版本归位);Kimi 面无市场,重拷 `plugins/project-evo/skills/docs-evo/` 整目录

## [0.2.1] - 2026-09-10

### 修复（2026-09-10，第四十三批:secret-scan A/B 对照测试在 Windows 必红）

> 现象:本机 Windows + PowerShell 7 下 `uv run pytest` 必红一例,`test_ab_matches_oracle` 抛 `TypeError: the JSON object must be str, bytes or bytearray, not NoneType`。

- 根因 [实证: 2026-09-10 本机 pytest 实跑与探针复现]:`ab.py` 以 `ensure_ascii=False` 打含中文的 JSON,Windows 下子进程 stdout 接管道时默认用 ANSI 代码页(cp936)编码,测试按 utf-8 解码失败,读取线程抛 UnicodeDecodeError,`r.stdout` 落成 `None`
- 修复:`tests/test_secret_scan.py` 该例子进程补 `PYTHONIOENCODING=utf-8`,与 `test_project_evo.py` 的 `_run_md_guard` 既有口径一致;脚本产物形态不动,Linux 与 CI 行为不变
- 影响面:该例自第三十七批引入起在 Windows 上从未真绿,属长期潜伏,非本轮改动引入

### 修复（2026-09-10，第四十二批：Codex 面 PostToolUse 钩子在 Windows 起不来）

> 现象：Codex 会话里每次编辑 markdown 都报 `PostToolUse hook (failed) error: hook exited with code 1`，会话被打断。定位到本插件 `hooks/hooks.json` 的 md 禁字挡板，与 oma 无关。

- 根因 [实证：2026-09-10 本机 codex 0.149.1 探针实跑]：Codex 在 Windows 用会话 shell(PowerShell)执行 hook 命令行，`$CLAUDE_PLUGIN_ROOT` 被 PowerShell 当普通变量解析，展开为空串，实际执行 `uv run --no-project "/skills/evo/scripts/md-guard.py"`，uv 找不到脚本，钩子进程退出码 1
- 修复：`hooks/hooks.json` 补 `commandWindows` 字段，Windows 面改用 `$env:CLAUDE_PLUGIN_ROOT`（非 Windows 面保持原 `$CLAUDE_PLUGIN_ROOT`，Claude 面 bash 语义不变）
- 加固：`md-guard.py` 载荷宽容，`tool_input` 不是对象（Codex 的 apply_patch 面是 patch 文本）或整条事件不是对象时直接放行退出 0，不再抛 `AttributeError` 退出 1
- 测试：`tests/test_project_evo.py` 加三例，hooks.json Windows 形态守卫、载荷宽容、禁字判据不回退

### 变更（2026-09-09，第四十一批：Grok/Kimi 部署通道入册与 README 精练）

> 本机四 agent 面装齐（claude/codex/grok/kimi）后把实测通道写回文档；用户裁定 README 面向人类读者精练，专注全平台安装部署与使用示例。

- README 重写：安装节按客户端分面（Claude Code/Codex/Grok 插件 + Kimi skills 手拷 + 本地市场 + 裸脚本），新增四插件使用示例节；删目录树与理论概念节（权威在 AGENTS 仓库地图与 evo SKILL）
- AGENTS 环境事实、evo SKILL 安装通道、四插件 README 安装节、tool-cli-agents 市场分发要点同步 Grok/Kimi
- 实测口径：grok 1.0.13 走 plugin marketplace（install/update/details 通）；kimi 0.41.0 无市场，`extra_skill_dirs` 指 `~/.kimi/skills`，命令与 hooks 不随行

### 变更（2026-09-09，第四十批：office-pro skill 改名 office,消除双名重叠）

> 用户指出市场安装后显示 Skill(office-pro:office-pro) 双名重叠;同第三十一批裁定:插件名、市场安装标识不动,skill 目录与 name 改为 office,显示收敛为 office-pro:office;斜杠命令同名避让,office 改 office-cli。

- 目录:plugins/office-pro/skills/office-pro git mv 至 plugins/office-pro/skills/office;SKILL.md frontmatter name 同步 office
- 斜杠命令 commands/office.md 改名 office-cli.md,避免与 skill `/office-pro:office` 同名再重叠
- 仓内路径引用全量同步:README、docs/README、AGENTS、插件 README、命令、install/smoke 参考、S007、evo SKILL 交叉引用、tests;CHANGELOG 历史批次记载保留原样
- 已安装用户 `/plugin marketplace update projectevo` 后卸载重装 office-pro 即得

### 新增（2026-09-08，第三十九批：office-pro 插件）

> 信源：S007 烟测 + 既有 pptx 纠偏/换文案/事实核查实弹。用户裁定把该过程沉淀为市场插件。钉资产，不跑 `install.ps1`，不 `officecli install`。

- 新插件 `plugins/office-pro`（skill `office-pro`）：意图路由 + install/cli/edit/facts 四篇参考；PEP 723 `which.py`/`smoke.py`；斜杠命令 `/office-pro:office`
- 硬规则：钉 GitHub 资产、备份与锁文件、PowerShell 禁 `$args`、稿面数字须对官方页、native 截图核、图片保纵横比
- 双 manifest 0.1.0；双市场清单收录；pytest 覆盖清单与 which/smoke
- 研究底稿仍是 `docs/research/S007-OfficeCLI-agent原生Office套件.md`，本轮标明已沉淀

### 新增（2026-09-08，第三十八批：OfficeCLI 研究与本机烟测）

> 信源：https://github.com/iOfficeAI/OfficeCLI 。钉 release 资产，不跑官方 `install.ps1`、不 `officecli install`。

- 研究：`docs/research/S007-OfficeCLI-agent原生Office套件.md`
- 本机 `%LOCALAPPDATA%\OfficeCLI\officecli.exe` v1.0.148，SHA256 与 `SHA256SUMS` 一致
- 烟测 pptx/docx/xlsx 的 create/add/view/get/validate/close 与 `--json` 信封通过；坏路径 `not_found` 退出 1

### 新增（2026-09-08，第三十七批：secret-scan A/B 对照）

> A/B 是对比不是门禁。同夹具实跑 A=`secret-scan` 对 B=`evo scan` secrets 部分，结论回填 S006。

- `scripts/ab.py` + `verification/ab-cases.md`：九条伪造夹具（工作区/已删历史/占位/AWS 文档示例/.env/--pii）
- 本机九条期望全中；A 独有 Stripe/GitLab/pii；共有 GitHub token 历史能力与 AWS 示例假阳；gitleaks 未装 SKIP
- 研究：`docs/research/S006-secret-scan-AB对照.md`

### 新增（2026-09-08，第三十六批：密钥隐私扫描插件 secret-scan）

> 信源：超级研究对照 gitleaks/trufflehog/detect-secrets/akaihola secrets-scan/GitGuardian 技能与本仓 evo scan.py。用户要 uv Python 扫本地仓与 GitHub 历史，不绑 Go 二进制。

- 新插件 `plugins/secret-scan`（skill `secrets`）：PEP 723 零依赖 `scan.py` 扫工作区、`git log -p` 全历史、`gh` Secret Scanning alerts 与 code search；完整远程历史须显式 `--clone-history`
- 报告脱敏；不做活密钥探测；白名单 `SECRET_SCAN_ALLOW`
- 双 manifest 0.1.0；双市场清单收录；pytest 覆盖历史命中与 CLI 校验
- 研究落 `docs/research/S005-git密钥隐私扫描skill选型.md`

### 变更（2026-09-08，第三十五批：bh 0.6.0 无头引擎写入 research）

> 信源：https://github.com/raystyle/browser-harness README + CHANGELOG 0.6.0（D37）+ 本机 `bh engine` 实弹。仓已是 TS `bh`，不是旧 Python CLI。

- web.md 第七节改写：研究优先 `bh engine start/status/stop` 与 `web-fetch --engine`；用户 Chrome 仍工位复用
- SKILL.md / pipeline.md 硬规则同步；本机实证 engine pid 15448、`--headless=new`、抓 example.org 后 stop 干净

### 新增（2026-09-08，第三十四批：超级研究技能拆出市场；论文与种子下载实证）

> 用户裁定：reader / X / Google / Medium / gh 集成进市场独立技能；evo 专注项目文档，去掉多余 CLI 工具介绍。同日实测论文检索下载与官方种子文件下载。

- 新插件 `plugins/super-research`（skill `research`，显示 super-research:research）：管线 pipeline + gh/web/x/reader/aria2c/git 参考；双 manifest 0.1.0；双市场清单收录
- evo 迁出五工具篇（git mv 保沿革）；SKILL 意图路由改指 research 技能；references 全量 17 篇正文 + 本索引
- 论文实证：Google `site:arxiv.org` + arxiv API + `aria2c` 下 `arxiv.org/pdf/2104.00142`（108268 字节）+ reader 抽出 NodeSRT 摘要
- 种子实证：官方 Ubuntu 24.04.4 `.torrent` 508158 字节；**必须 `--follow-torrent=false`**，否则预分配 6.1GiB ISO（已中止删除）

### 新增（2026-09-08，第三十三批：记录 bh 与 reader 使用过程技巧）

> 信源：本会话对 `bh` 0.5.2 与 `reader` 0.6.0 实弹（Google/Medium/web-fetch、`E:\研究资料` 电子书）。用户裁定：只复用 1 到 2 个 tab，禁止重复附着。研究收尾 `[实证]` 抽进现役工具篇。

- 本仓研究：`docs/research/S001-bh与reader使用过程技巧.md`（工位复用、HTTP 优先、pluck 对现场、坏 EPUB、扫描 OCR、大盘禁递归）+ `docs/research/README.md` 登记；diary `docs/diary/2026-09-08-bh与reader使用过程.md`
- tool-browser-harness 脚本纪律补工位复用硬规则；新增第八节 TypeScript 端口 `bh`（与 Python 0.6.12 分 oracle）
- tool-reader 版本快照 0.5.0 到 0.6.0；坑表补 PowerShell filter、mq exit 2、malformed EPUB、`--pages` 位置、整盘递归挂死
- 接线：docs/README、references/README 条目描述、env-environment reader 快照

### 新增（2026-09-08，第三十二批：吸收 browser-harness-ts 的 TypeScript 工程经验）

> 信源：D:\browser-harness-ts 对照 package.json、tsconfig、R001、G002、M101 至 M103、P0001。吸收即提炼：只入库跨项目可复用的工程合同，不搬 CDP/站点应用产品细节（产品面仍在 tool-browser-harness.md；脚本 workspace 仍在 tool-cli-agents.md）。

- 新增 `references/tool-typescript.md`（第 22 篇）：Node >=22 ESM、tsc 严选项、runtime 依赖白名单（commander/zod）、构建分面（tsc 对核心、esbuild 仅 IIFE）、node:test 引号 glob、checkJs 管 .mjs、两套家（npm pack 验收禁 link）、空串不走 ??、fnm 下 spawn npm-cli.js、无内核锁只认 pid 死亡、CI 矩阵 Node 22/24 乘三系统
- 反哺：flow-testing TS 行改为 node:test 家族默认；tool-selection 标准库档补 Node 内置、稳妥梯队改 commander/zod；env-platform 补 node:path 与 npm/fnm/glob 坑；flow-release 衔接 npm pack；base-init 跨项目样本增 browser-harness-ts；env-environment 依赖路由补 Node/TS 不进 ome
- 接线：SKILL.md 意图路由加行、compatibility 四类仓、篇数 21 改 22；references/README 三层同步（全量 23 篇含本索引）；AGENTS 地图与提炼源；docs/README 与仓 README 篇数

### 变更（2026-09-04，第三十一批：skill 改名 evo,消除插件名与 skill 名重叠）

> 用户指出市场安装后显示 Skill(project-evo:project-evo) 双名重叠;裁定:插件名、市场安装标识、`/project-evo:*` 斜杠命令前缀不动(品牌与安装兼容优先),skill 目录与 name 改为 evo,显示收敛为 project-evo:evo。

- 目录:plugins/project-evo/skills/project-evo git mv 至 plugins/project-evo/skills/evo;SKILL.md frontmatter name 同步 evo(硬规则:name 与目录名一致)
- 仓内路径引用全量同步:README(含反斜杠命令示例)、docs/README、AGENTS(规范导语/name 规则/地图/分层原则/硬规则 1)、插件 README 与三斜杠命令、hooks.json($CLAUDE_PLUGIN_ROOT 面)、.claude/settings.json、githooks/pre-commit、.tools/md-ref-scan 默认根、CI 冒烟、tests 两处路径;CHANGELOG 历史批次记载保留原路径不改
- verification 引言措辞修正:project-evo 定位为文档体系插件,核心 skill 为 evo
- 插件名、双市场清单、双 manifest、安装通道均不变;已安装用户插件更新即得新路径,无需重装

### 新增（2026-09-04，第三十批:市场分发协议沉淀,tool-cli-agents 第二节增补）

> 信源:Claude Code 官方文档原文取回(code.claude.com/docs 插件市场页)+ Codex 本机实弹(codex-cli 0.149.1:简写/SSH/HTTPS+钉版三形态逐一如实跑通)。用户问「marketplace add 应该支持 https 和 ssh 两种?」触发调研,裁定沉淀。

- tool-cli-agents.md 第二节新增「市场分发:add 形态与 git 协议(双客户端)」小节:双客户端 add 形态/简写默认协议(SSH vs HTTPS,相反)/私库认证(标准 git 机制,Claude 后台更新禁 helper)/钉版(@ref、#ref、--ref)/marketplace.json 插件级 source 七型(./、github、url、git-subdir、npm、archive、command;url 双协议;marketplace 级只 ref 无 sha)/裸 json 不可作分发载体
- 方法论一条:同一简写跨客户端解析不同,分发文档按客户端分别给实证 [经验]
- 同文件第八节同构表修正:双漂移守卫已在第二十八批随单源化消亡,该行改指清单一致性守卫
- README「快速开始」重写为「安装与部署」:四通道矩阵(Claude Code 插件/Codex 插件/本地市场开发态/裸脚本)+ 协议与钉版通用事实
- references/README 条目描述同步

### 修复（2026-09-04，第二十九批:init 脚手架语义,目标目录不存在则创建）

> 同日两犯升格:本地 e2e 与 CI 三系统冒烟(ubuntu/macos)各踩一次「目标目录不存在 exit 2」。裁定:init 是脚手架,建目标目录属其本性;check/scan 为只读诊断,保留存在性保护。

- scripts/init.py:目标目录 mkdir(parents) 替代报错退出;docstring 同步
- tests 增 test_init_creates_missing_target(嵌套不存在路径,期望 0 且 PRD.md 生成)
- CI 冒烟步无需预建目录,顺带即测新语义

## [0.2.0] - 2026-09-04

### 变更（2026-09-04，第二十八批：插件市场转型,uv CLI 分发通道退役）

> 信源:SpecterOps/skills 市场仓组织维护形式实地调研(README/CONTRIBUTING/justfile/根双市场清单/插件双 manifest/catalog 机制原文取回核对)。用户裁定:放弃 uv CLI 分发,转插件市场仓,保留 git 历史原地重构;Codex 双面纳入;命令面全量(斜杠命令+hook)。六命令归宿:skill 安装与 update 随分发模式消亡(插件通道原生替代),init/check/scan 等价迁出,llms 降为 CI 冒烟。

- 目录:skills/project-evo 迁至 plugins/project-evo/skills/project-evo,模板迁至 skills/project-evo/assets/templates(均 git mv 保沿革)
- 双市场清单(.claude-plugin/marketplace.json 与 .agents/plugins/marketplace.json)+ 插件双 manifest(.claude-plugin/.codex-plugin,name/version/description 同步受测试守卫;Codex 面实弹验收:codex-cli 0.149.1 本机 `marketplace add` + `plugin add` 成功,缓存按 manifest 版本 0.2.0 归位,51 文件全树随装 [实证])
- 三脚本下沉 skill:scripts/{init,check,scan}.py(PEP 723 零依赖,逻辑原味迁自 CLI 模块);mdrules.py 立为禁字规则唯一权威(check PE-12/scan/md-guard 三面同源);md-guard.py 自包含化(PEP 723)随 skill 分发,plugin hook、.claude/settings.json、githooks 三处共用一份
- Claude 面:commands/{init,check,scan}.md 斜杠命令 + hooks/hooks.json PostToolUse 挡板($CLAUDE_PLUGIN_ROOT);Codex 面走 skill 本体与双 manifest
- 移除:src/project_evo 全树(六命令 CLI;update 自升级闭环、skill 双落位安装随分发模式消亡)、data/skill 内嵌副本(双漂移守卫随之取消,单源化)、.tools/md-guard.py(并入 plugin scripts)
- tests 重写:脚本按路径加载(无安装态包);新增市场清单一致性守卫(双市场收录一致/source 可达/双 manifest 字段与版本同步/命令面与脚本在位);仓内禁字回归改指 mdrules.py;10 测全绿
- 接线:AGENTS(地图/分层原则/硬规则 1/环境事实)、README(安装与结构全重写)、SKILL.md 配套面、base-writing-standards 与 tool-cli-agents 措辞、verification 引言、docs/README 路径、CI 冒烟(init+check 实跑 + 五 JSON 解析)、.tools/README、md-ref-scan 默认根、pyproject(package=false 降维护栈)
- 安装通道变化:uv tool install git+ 退役;新通道 Claude Code `/plugin marketplace add raystyle/ProjectEvo` + `/plugin install project-evo@projectevo`,Codex `codex plugin marketplace add raystyle/ProjectEvo`

### 新增（2026-09-04，第二十七批：agent-native CLI 设计指南,双用户契约、自由代码面与脚本 workspace 吸收）

> 信源:wevm/incur(TS 原作)与 douglance/incurs(Rust 移植)两仓 README 原文取回核对;叠加家族 browser-harness 与云 CLI 仓 管道代码逃生舱、browser-harness browser-workspace 脚本归档设计实证(用户裁定纳入)。契约方法论框架无关,两仓为样本实现。

- 新增 `references/tool-cli-agents.md`(第 21 篇),十节:双用户公理与 token 经济学(MCP/单 skill/agent-native 三形态会话成本对照,数字为信源建模未本仓复验);发现契约三通道(skills add/mcp add/--llms,skill 按命令组拆分,发现层 11489 到 387);输出契约(TOON 紧凑格式/--format 面/CTA/输出策略两档);输入契约(四面 schema/类型即文档一份多渲染/弃用全通道同步);**自由代码面**(管道代码逃生舱:here-string/heredoc 喂代码、内置库函数零 import 直集成运行时、helper 双通道;incurs Code Mode 为产品化形态,审批生命周期);人机分叉(agent 检测/全局 flag 契约);定义一次多面暴露(共享命令图 + Agent Plugins 1.0 三层:Prompt Artifact/Tool Binding/Tool Runtime);行为 oracle 对齐法(1062 测试 parity gate,映射黄金文件/双漂移守卫/llms 冒烟);**脚本 workspace**(browser-workspace 实证:agent 拥有的运行时目录非包源码、钉数据根与代码根解耦、两类产物两个口(browser_helpers.py merge 覆写 + apps/<名>.py 即成一级命令 APP_ARGS)、apps 与管道代码同一 exec 运行时零 import 互见、包薄核 + 插件增量供给本地永不删、domain-skills 站点知识层、包管稳定内核 workspace 管长尾演化);落地清单九问(含逃生舱与归档两问)
- 接线:SKILL.md 意图路由加行、description 加触发词、篇数 20 改 21;references/README 三层同步(全量 22 篇);AGENTS 仓库地图 references 篇数 17 改 21(滞后校正)
- data/skill 副本同步(双漂移守卫)

### 变更（2026-09-04，第二十六批：browser-harness 0.6.12 复验与事实刷新）

> 上游 D:\browser-harness 更新至 v0.6.12(装态同版本);实弹复验搜索与抓取全过(google_search 3 条、example.com 抓取、维基 Feedback 78KB 正文一次过,此前四度超时的同页,新版导航 30s 预算生效)。

- tool-browser-harness.md:版本 0.6.9 到 0.6.12;helper 面补 `wait_for_render`(渲染态判官);连接模型补任务级浏览器隔离;坑表首行按 Issue #3 修复改写(三档超时 env 可配:BH_IPC_TIMEOUT 5s/BH_NAVIGATE_TIMEOUT 30s/BH_SCREENSHOT_TIMEOUT 60s;导航三态事件判定,unknown 如实上报不伪装)
- 注记:上游修复原则「事件驱动判状态(成功/失败/未知),超时只做无事件时的死锁兜底」与本仓第二十批事件驱动模型同构 [实证: 上游 CHANGELOG 0.6.10]
- env-environment.md 版本快照同步;data/skill 副本同步

### 变更（2026-09-04，第二十五批：环环相扣收口,体系骨架显式化 + 断链工具沉淀）

> 用户验收标准:skill 要形成环环相扣的框架体系。机械层:交叉引用断链扫描 0;结构层:骨架显式化为 SKILL.md 七层环扣表。

- SKILL.md 体系速览新增「体系骨架(七层环扣)」表:认知(六态+知行合一)/对话(双向问答)/流程(五步+阶梯)/探查(选型+工具管线)/执行(事件+超时)/验证(测试门禁+PE)/沉淀(分治+集成约束),与传动句「执行产事件、验证产反馈,沉淀转资产,资产生复利;吸收即提炼是入库口径」;核心思想补代谢链一句
- exp-sedimentation 集成约束节挂 flow-testing 交叉引用(约束与门禁同源)
- 新增 `.tools/md-ref-scan.py`(PEP 723 零依赖断链扫描,断链检查手拼二犯升格,沉淀铁律);pre-commit 接入(git 提交挡板 = md-guard --staged + md-ref-scan);.tools/README 登记
- ROADMAP 阶段三「断链扫描工具适配」翻已完成
- data/skill 副本同步

### 变更（2026-09-04，第二十四批：tool-selection 增发现层,awesome 清单与官方库搜索）

> 用户裁定:补各开发环境各领域的 awesome 清单与各语言官方库、GitHub 搜索方法,即「不知道叫什么」的发现层。

- tool-selection.md 新增「三、发现层」:awesome 清单用法(总索引 sindresorhus/awesome,领域清单 gh search 拿;**扫清单拿候选名再回三通道核稳度,清单是发现不是裁决**,清单自身也看 pushedAt)与官方库搜索表(Rust docs.rs/Python docs/Node api+MDN/pwsh Get-Command+Learn/Go pkg.go.dev);原三至五节顺延,决策树首行改走 awesome 入口
- references/README 条目描述同步;data/skill 副本同步

### 新增（2026-09-04，第二十三批：依赖选型探查手册,阶梯的落地方法）

> 用户裁定:阶梯是知,「怎么查到每一档」是行,没有探查方法阶梯空转;五栈(rust/python/powershell/node/typescript)大量库与仓可搜索研究。提炼自家族选型手册四篇:结构源仓 R005(Rust crates.io+GitHub 双通道)、R008(PyPI)、R009(PowerShell Gallery)、云 CLI 仓 R004(npm),骨架同构。

- 新增 `references/tool-selection.md`(第 20 篇):阶梯 2 到 5 档数据源表(本仓 rg/标准库文档/平台原生/已装清单);五栈三通道能力对照(差异即方法:PyPI 关键词仅网页、Gallery CLI 恒带显式仓、cargo search 镜像须 --registry);稳度四信号(下载/发版/维护者/License,启发式非门禁);GitHub 通道四步;防仿冒与单锁纪律;结论落 S 文档双通道各一条证据、装后跑最小用例(反馈)
- 接线:flow-workflow 阶梯 bullet 挂指针;tool-gh 选型双通道挂指针;SKILL.md 意图路由加行、篇数 20;references/README 三层同步(全量 21 篇);data/skill 副本同步

### 变更（2026-09-04，第二十二批：吸收 ponytail 最小实现阶梯）

> 信源:DietrichGebert/ponytail README 全文(raw 取回)。其基准数字经一次社区纠偏(#126,单发基线虚高)后自我修正为诚实口径(均值 54% 减码、安全 100%),与六态实证纪律同气。

- flow-workflow.md 拆步骤标准加两行:**最小实现阶梯**(不需要就跳过/本仓已有就复用/标准库、平台原生、已装依赖有就用/一行就一行/皆否才写够用的最小;小因为必要不是高尔夫)+ **阶梯两护栏**(懒于解不懒于读=反冥行妄作;最小不削安全,验证/错误处理/安全/无障碍不上砧板)
- 与既有体系映射确认:阶梯是「验证过的直接复用」的执行形态,未新增文件;references/README flow-workflow 条目描述同步
- data/skill 副本同步

### 变更（2026-09-04，第二十一批：全库自省,残留清剿与事实复验）

> 执行第二十批「吸收即提炼」裁定的自省后续:全 20 篇参考 + SKILL 通读复查,四查(冗余/啰嗦/跨文件重复/事实过时)。

- 扁平化残留三处:tool-project「references/tools/」与 flow-release 两处「tools/tool-*」改为扁平路径(第六批扁平化漏网)
- 版本事实复验(五工具实测):browser-harness 0.6.8 到 0.6.9、reader 0.4.0 到 0.5.0 刷新;gh 2.98.0/git 2.55.0/aria2 1.37.0/ome 0.1.0 复验无变化;tool-reader 篇内细节断言按六态诚实标注「0.4.0 版实证,待复验」
- tool-browser-harness 坑表补一行:web-fetch 子命令输出过 PowerShell 管道中文塌码,处理=管道脚本写 UTF-8 文件再读(本日两踩)
- 指针补齐:base-init 追问链指向 flow-inquiry;flow-workflow「先读文档再执行」改「纪律」(硬规则编号是本仓语境,对目标项目读者悬空)
- 通读结论:base-init/base-docs-directories/base-primitives/env-platform/flow-release/exp-pitfalls 及五工具篇密度合格,不动

### 新增（2026-09-04，第二十批：事件驱动模型吸收 + 吸收即提炼裁定与全库自省）

> 用户裁定(2026-09-04):吸收是提炼,大量无用与冗余信息须剔除,保最准确精练的上下文表达;立为硬规则并对全部文档自省。信源:熔断器维基全文、let-it-crash 原文(支付服务三返回态例证);EDP 维基与超时专文四度撞冷启动超时未取正文(题录级)。

- 新增 `references/flow-events.md`(第 19 篇):三态事件(成功/失败/未知,未知最危险且不等于失败);let it crash 监督者模式(未知态处理从业务代码剥离到监督层);超时兜底三选(幂等重试一次/换路径/放弃并记录);熔断三态(Closed/Open/Half-open,防重试风暴);与六态接口(成功=实证渠道、失败=错误路径、未知=中转态)
- 接线:flow-workflow 拆步骤标准加「等待有上限」;SKILL.md 意图路由加行、篇数 19;references/README 三层同步(全量 20 篇);data/skill 副本同步
- 硬规则 7「吸收即提炼」立规(AGENTS.md);base-writing-standards 写完自查加第 6 条;全库自省瘦身(flow-events/flow-testing/base-writing-standards 四节等剔除重复表述)

### 新增（2026-09-04，第十九批：测试流程规范吸收,双轴分层与五层正名）

> 提炼源:本地九仓实测(reader 仓 G006 六层体系、ome 源仓 R004 黄金文件与真机对齐、结构源仓 R004 双轴雏形、浏览器工具仓 R003 四层、云 CLI 仓冒烟矩阵与真钥验收、虚拟化仓 Pester 结构冒烟与 DryRun、主机环境仓 verify/heal 闭环与假绿防线、PVE 仓 dryrun 闸门、远端接入仓 doctor 哨兵);四路并行调研,文档引句与测试实盘双核对。

- 新增 `references/flow-testing.md`(第 18 篇):**双轴模型**(地基层=框架原生单元/集成/文档测试,意图层=冒烟/回归/验收/A-B 目的流程,两轴正交);五层正名表(每层归属轴、回答的问题、载体、时机);断言纪律七条(期望值独立来源禁重言式、只断稳定字段、正负例成对、错误路径覆盖等,家族各仓 AGENTS 逐字一致);跨栈载体速查(Rust/Python/TS/PowerShell 四栈);门禁时机谱(本地三件到批次到 CI 三系统到发版三路到 verify/heal 收尾,含假绿防线);特色机制八项(黄金文件 oracle、快照纪律、回归生长律、防漂移、DryRun 沙箱、A-B、验收即对照、六态衔接);AGENTS「写测试时」摘要条款
- 接线:flow-workflow 验收口径加测试分层调度行;base-primitives 义务表「写测试」行指向;SKILL.md 意图路由加行、篇数 18;references/README 三层同步(全量 19 篇)
- data/skill 内嵌副本同步(双漂移守卫)

### 新增（2026-09-04，第十八批：集成约束四形态落地,禁字二犯升格）

> 用户裁定(2026-09-04):重复犯的错误除规则与文档记录外必须有集成约束:Agent 的各种 HOOK 阻断或提醒、项目强制执行的 uv 运行时 python 脚本工具、git 提交事件的 HOOK 提醒、转换的回归测试用例。规则是知,约束是行。触发案:第十六/十七批新增文本连犯破折号禁字(各被 scan 当场抓住)。

- 教义:exp-sedimentation.md 升格节加「集成约束(二犯以上必配)」四形态与验收清单第 5 条;SKILL.md 意图路由、references/README 条目同步;data/skill 副本同步
- 形态一(agent hook):`.claude/settings.json` PostToolUse hook(Edit|Write|MultiEdit 到 `.tools/md-guard.py`,违规 exit 2 回传提醒);本会话实弹验证触发;.gitignore 改为忽略 `.claude/*` 但放行 `settings.json`(约束资产入库,其余仍为运行时状态)
- 形态二(uv 脚本门禁):`.tools/md-guard.py`(stdin hook 模式与 --staged 挡板模式;规则唯一权威在 `project_evo.mdfix`,与 scan/check PE-12 同源)+ `.tools/README.md` 清单
- 形态三(git 钩子):`githooks/pre-commit` 调 md-guard --staged,不过不进库;`git config core.hooksPath githooks` 已设;实测违规模板被挡(exit 1)、干净放行
- 形态四(回归测试):`tests/test_repo_md_clean.py` 仓内全量 md 禁字清零回归,CI 常驻;安装态自动跳过
- AGENTS.md 仓库地图补 `.tools/` 与 `githooks/` 两行;提交时 githooks/pre-commit 需 `git update-index --chmod=+x`(Windows 下保 exec 位)

### 变更（2026-09-04，第十七批：双向问答协议定型,吸收 grilling 拷问机制）

> 用户裁定(2026-09-04):对话模式定型为两式:你问我答(agent 拷问用户,收敛决策)与我问你答(用户咨询 agent,以问为种子扩充整理)。信源:mattpocock/skills 的 grilling SKILL.md(raw 取回,模板占位符经 blob 渲染页核对)。

- 新增 `references/flow-inquiry.md`(第 17 篇):你问我答四机制(设计树、前沿轮次=前置已定问题整轮齐问附推荐答案、事实/决策/实验三分流、无静默假设终止判据)+ 我问你答扩充式整理(用户裁定:以问为种子不断扩充追加所有关联详情,整理三步=种子扩散/人类组织/落位回写;自检三条=先读文档再答/答必六态/信源核实)+ 闭环 mermaid(两通道汇于方案,实验类走 PoC);实验三分与落位义务为超出 grilling 原文的扩展(原文只有事实/决策二分)
- flow-workflow.md:登记步追问链挂接拷问模式;base-primitives.md:文档义务表「追问链澄清」行注记(你问我答+轮次算法指向)
- SKILL.md:description 加双向问答触发词、意图路由加行、篇数 16 改 17;references/README.md:快速路由+场景索引+全量清单 18 篇同步
- data/templates/AGENTS.md:对话节补「对话分两式」摘要行(细则唯一权威在 skill)
- data/skill 内嵌副本同步(双漂移守卫)

### 变更（2026-09-04，第十六批：知行合一植入,六态理论升级与工作纪律落地）

> 理论裁定（用户 2026-09-04）:六态是知行合一的工程化,实证=知行合一态;五态为中转态,为进入实证服务;实证与经验循环,迭代复利;阳明术语（冥行妄作/悬空思索/着实去做/事上磨炼）进正式词汇。信源:王阳明知行合一双源核对（光明日报/人民网理论频道 + 中文维基,后者参考节引前者,独立性部分打折;核心引句双源吻合）。

- base-writing-standards.md:六态节重构为「知行合一的工程化」;两级结构（实证态一/中转态五）+ mermaid 六态流转图;用法升红线级:中转态标注义务（假设/推断附验证动作、记忆附复核点,不写即未完成）与收尾处置纪律（悬空升实证/留 research/注销,禁止滞留）;写完自查同步
- flow-workflow.md:新增「三、知行合一工作纪律」（反冥行妄作=不查不验就动手、反悬空思索=研究做完不落地（PoC 必落 poc\ 目录）、着实去做、事上磨炼）,原三至八节顺延重编号;验收通用口径补两条（悬空中转态处置、研究类目标验收看 PoC 产物）
- exp-sedimentation.md:成功经验链下新增「实证与经验的循环（迭代复利）」小节（mermaid + references 为循环固化形态）
- exp-pitfalls.md:P6 六态标记滥用补第三误读（中转态长期滞留）与正解同步
- SKILL.md:description 加知行合一触发词;意图路由与体系速览同步;references/README.md 三条目描述同步;verification PE-10 加手检注记（验证路径属语义判断,机检不做）
- data/skill 内嵌副本同步（双漂移守卫）;G001 模板六态节补一行
- 不动:checker/cli 不加新 PE 检查;AGENTS 硬规则与 ROADMAP 无涉

## [0.1.1] - 2026-09-03

### 实测（2026-09-03,v0.1.0 后）

- 真实项目首装（remotex，已有部分体系的存量仓）：init 建 6 跳 5（幂等含 Windows 大小写碰撞保护）、check 诊断 8 PASS / 4 FAIL（均为存量文档真实差距：references 未登记新 INDEX、AGENTS 缺义务表、research 无六态、存量文档含 emoji）、skill 双落位安装 + gitignore 追加幂等；未触碰既有内容文件、未提交（目标仓自主裁决）

## [0.1.0] - 2026-09-03

首个版本，双形态交付：

- **渐进知识库 skill**:SKILL.md 意图路由 + references 分类扁平 17 篇 + verification 检查命令 13 条；吸收家族七仓 1148 提交的演化实践（经验分治、封版模式、平台适配、环境索引、17 条误区），全量六态标注并隐私脱敏
- **uv Python 工具**（project-evo，零运行时依赖）：init 骨架安装（幂等）/ check 诊断 PE-01 至 PE-13 / skill 项目级安装（.claude/skills 与通用 .agents/skills 双落位，内嵌全树 + 双漂移守卫 + agent 目录 gitignore 惯例）/ llms 索引；pytest 8 测全绿，端到端冒烟通过

### 开发批次明细（POC 期）

### 新增（2026-09-03，第十五批：update 自更新，参考 browser-harness 方式）

- `project-evo update [-y] [--repo o/r]`：双安装模式分派，git 模式（仓内 checkout）要求工作区干净后 `git pull --ff-only`；installed 模式走 `uv tool install --upgrade`（PEVO_GIT 环境变量切 git 源）
- 版本探测：GitHub Releases API（匿名，GH_TOKEN/GITHUB_TOKEN 可注入，超时离线返回 None 不阻塞）；semver 近似比较含 a/b/rc 预发布序
- 升级后 realign 提示：对已装项目重跑 `project-evo skill` 同步最新 skill 树
- pytest 增 3 测（版本序比较、离线容错、update 冒烟）至 11 测全绿；README/SKILL.md/llms 同步

### 修复（2026-09-03，第十四批：README 同步与 checker 围栏误判）

- README 四处同步：快速开始第 3 步改为 uv CLI 主入口（init/check,PowerShell 用例集降为等价）、目录树补 src/tests/pyproject、常用命令诊断组补 uv check、环境前提补 uv 运行时说明；清除全部 gh skill 表述
- checker 修复真 bug：PE-11 标题检查现**跳过围栏代码块内 # 注释行**（本仓 README 的 powershell 注释曾被误判）；新增回归测试
- AGENTS 三个真违规标题去括号（解释移标题下 > 引用行）；自家仓复诊 FAIL 6 降到 5，余项均为设计内（骨架仓检查项不适用于 skill 开发仓，verification 已注记 PE-01/02/03/08/09)
- pytest 9 测全绿

### 变更（2026-09-03，第十三批：README 按规范重写）

- 按标准 README 七段式重写：一句话定位（引用块）、快速开始 4 步（安装通道说明，替换过时 Copy-Item）、目录树（不含工作产物）、核心概念 6 术语、常用命令三分组（检索/验证/安装，标注副作用）、文档导航表（与 docs/README.md 同源）、环境前提（全部实测版本）
- 2.9KB，8KB 门禁内；快速开始与常用命令抽查实跑通过

### 变更（2026-09-03，第十二批：隐私脱敏）

- 用户裁定：skill 内不保留被吸收仓的名称与本机目录信息（隐私）
- 全仓脱敏：七个来源仓名替换为角色称谓（源头仓/结构源仓/ome 源仓/发布工程仓/云 CLI 仓/虚拟化仓/运行存储根等），本机路径替换为通用表述（环境根 EnvRoot/参照仓），外部调查 skill 引用去路径化
- 保留：公开工具名与接口（ome/OHMYENV_ROOT/browser-harness/reader/gh/git/aria2c）、提交哈希、日期与事实
- 经验标注降维：来源由「仓名+编号」改为「角色称谓」，六态语义不变

### 变更（2026-09-03，第十一批：家族三仓补读）

> 研究对象：云 CLI 仓（09-02 立项，TS/Node,omc CLI，最新完整形态）、虚拟化仓（08-03 生，家族最老祖先，先有工程后有体系，后期反向接入）、运行存储根（非 git 仓，运行存储数据根）。至此家族七仓全读。

- base-init.md 增 **agent-native CLI 的 SKILL.md 模式**（何时用 + 命令表指向 R 文档 + 管道代码逃生舱 + helper 双通道；bh/两仓同款）与 **存量仓接入迁移路径**（plans到proven 改名、补编号、AGENTS 四段重写、六态补标、引用替换、门禁接入；虚拟化仓实证序列）
- base-docs-directories.md:mistakes 单文件形态补最新仓实证（云 CLI 仓 09-02 仍单文件）；编号规则增**跨仓不对齐是常态**（G004 三义漂移实证，稳定的是类别语义非绝对号码）
- env-environment.md 增**代码根与数据根解耦**模式（ome EnvRoot / 运行存储根 StoreRoot / bh BH_HOME 三例）

### 变更（2026-09-03，第十批：源头仓 溯源吸收）

> 研究对象：源头仓（体系总源头，458 提交，2026-08-19 至 09-03；现行体系多数发明诞生于 08-29「文档体系重构：从流水账到状态驱动的统一标准」）。另发现家族未读仓：云 CLI 仓、虚拟化仓、运行存储根。

- base-primitives.md 增 AGENTS **8KB 大小软门禁**（超限下沉 references；家族实测 8.9-16.7KB，两仓被迫瘦身重构）与 **CHANGELOG/ROADMAP 粒度纪律**（只留版本级里程碑，源头曾细碎堆积后全删收敛）
- base-docs-directories.md mistakes 节增**演化路径**（单文件 MISTAKES.md 起步合法到膨胀拆 M1xx，源头实证）与 **diary/proven 出身注记**（08-29 一个 history 拆成两目录，分界即「流水 vs 方案」）
- flow-workflow.md 验收口径增**多轮独立 review**实践（多家 agent 无头轮换至缺陷清零，缺陷家族沉淀；源头三轮 kimi/codex/claude 实证）
- exp-pitfalls.md 增 P16（CHANGELOG 记流水）、P17（AGENTS 无限膨胀）

### 变更（2026-09-03，第九批：ome 源仓 对照优化）

> 研究对象：ome 源仓（ome CLI 源码仓，103 提交，08-31 从 源头仓 结构平移；轻量变体：三原语无 PRD、无 proven、编号平移留洞）。其 AGENTS 四段与 结构源仓 一致，印证第八批模板升级。

- base-docs-directories.md diary 节升级：概貌级口径纪律（防单文件膨胀）+ **收工自省五段模板**（概貌/关键裁决/得失/明日入口/环境）
- exp-pitfalls.md 增 P13-P15:PowerShell 批改中文 md 塌行（一律编辑工具）、口径类裁决先展示再落码（taxonomy 四轮返工）、对环境想当然（runner 预装/正则先验证）
- env-platform.md CI 节增「CI 文档门禁」：四件套同口径进 CI + 上岗三坑（uv 预装/GITHUB_PATH export 语义/Windows stdout cp1252)
- flow-release.md 增「门禁与实跑互补」纪律（首跑实整抓逻辑缺口，门禁全绿下的漏网实证）
- flow-workflow.md 增「八、跨仓协作」：姊妹仓校准、ISSUE 矩阵四形态（通报/依赖/提议/上报）、对齐清单、探查先行、规范跨仓统一
- base-init.md 裁剪原则增「轻量变体合法」（ome 源仓 实证样本）

### 新增（2026-09-03，第八批：三仓 git 史对照优化）

> 研究对象：结构源仓（203 提交，体系源头，09-03 文档体系重构）、reader 仓（97 提交）、PVE 仓（2 提交）；谱系 源头仓 到 结构源仓 到 reader 仓 到 PVE 仓/browser-harness，姊妹仓交替演化互相校准。

- 新增 `references/exp-sedimentation.md`（经验沉淀分治，源仓 G004 提炼）：成功/错误经验两条链、产生时机与检索路径、**二犯升格工作流**（错误经验的终点是变成正确工作流）、一条知识一个权威落位、[推断]/[假设] 禁止跳级进 references
- base-primitives.md AGENTS 模板三段 到 **四段**（加意图路由节）+ 摘要层铁律（一行摘要、细则唯一权威在 R 文档，双份并行必漂移，源仓 5 处失守实证）
- base-primitives.md INDEX 节增维护硬规则：**以磁盘为唯一事实源**、登记缺陷高发区（diary/.tools/src/编号段/断号）、断号注记、TODO 残表清退
- exp-pitfalls.md 增 P9-P12：双份并行膨胀、规范文件自违规（豁免态全绿是假象）、豁免退出顺序纪律、旧索引当重写底稿
- flow-workflow.md 归档步挂经验分治落位；SKILL.md 意图路由表增「经验沉淀/升格」行；references/README 增经验组（17 篇）

### 变更（2026-09-03，第七批：渐进知识库定型）

- 用户裁定三原则落地：**目录与文件名为 rg 检索设计；文档结构为 mq 提取设计；SKILL.md 只做意图路由与速览**
- 移除 `evals/` 层：本 skill 为渐进知识库型，不做用例评估；AGENTS 布局/索引/硬规则、README、docs/README、references/README、ROADMAP 同步
- SKILL.md 重写为「意图路由前置」：18 行意图到参考路由表、rg 定位 + mq 提取四层检索法、体系速览压缩；frontmatter description 改为渐进知识库语义
- references 分类 + 扁平化：文件名加类别前缀（base-/flow-/env-/tool-/exp-），16 篇前缀分组自然排序；全部交叉引用同步
- base-writing-standards.md 重构为「命名三层标准」：定位模型（目录名到文件名到标题三层检索接口，定位内容不需要读全文）、文件名标准、标题结构标准（mq 自检）、反模式清单
- 硬规则更新：「双层机器可读」（rg 检索 + mq 提取）替换原两类评估规则

### 变更（2026-09-03，第六批：references 扁平化）

- 用户裁定：去掉 howto/pitfalls/tools 分类子目录，`references/` 为扁平目录，README 即渐进索引路由
- `references/` 扁平为 16 篇（9 howto + 5 工具指南 + pitfalls.md + README);pitfalls/README.md 改 pitfalls.md,tools/ 索引并入主 README
- references/README.md 重写为三层渐进索引：快速路由（高频场景）到 场景索引（四维度分组）到 全量清单；含五工具定位与研究管线、检索方法
- 全部交叉引用同步（SKILL.md 详细参考、AGENTS.md 布局与索引、docs/README.md、project-tools/environment/pitfalls 内链）；代码调查 skill 外部路径保持原样
- 新参考文件登记义务改为「登记进 README 第三层全量清单」

### 新增（2026-09-03，第五批：环境索引与封版模式）

- `references/howto/environment.md`：环境依赖索引，ome（Oh My Env，全平台 Agent 依赖环境管理 CLI，v0.1.0 未封板）三态模型（locked/installed/path）、七域分组、命令面速查（query/pin/install/deploy/update/status/daily/verify/heal/doctor）、环境根布局、项目依赖路由规则（status 盘点到AGENTS 环境事实登记到verify/doctor 进门禁）、browser-harness 走 uv tool 的例外说明
- `references/howto/release.md`：封版发布模式，提炼自 reader 仓 R008 四轮发布实证：前置裁定（版本必前进/Unreleased 有货才封/semver 取舍）、三路全平台门禁（主开发机+各平台实机+CI，含阶段标记串与吞退出码纪律）、封版件五步一次提交、tag 触发（一致性闸）、发布验收（资产件数/sha256 抽查/self update 首验/收尾义务）
- workflow.md 归档步挂接 release.md;SKILL.md、references/README、docs/README 索引同步

### 新增（2026-09-03，第四批：平台适配维度）

- `references/howto/platform.md`：平台适配规范九节，shell 分平台约定（pwsh7/bash/zsh 与禁项）、编码与行尾（UTF-8/BOM/.gitattributes 钉 LF/禁手拼分隔符）、文档路径写法两制（Windows 主场反斜杠 vs 跨平台正斜杠，全仓统一）、脚本载体跨平台优先级（uv Python 默认）、命令双形态写法、CI 三系统门禁、接管开发验收清单（R004/R005 模式）、八工具平台速查、立项平台决策
- init.md:Step 2 增「目标平台矩阵」必问项；Step 5 验收清单增平台决策落地检查
- primitives.md:AGENTS 模板操作规则段补分平台 shell 约定（reader 仓 规则 2 口径）
- writing-standards.md：路径写法规则由 Windows 单制改为两制全仓统一
- git.md：「Windows 专项坑」扩为「平台坑」八条（补 macOS 大小写不敏感、exec bit、文件锁、二进制行尾误伤）
- browser-harness.md：脚本模式补 Linux/macOS heredoc 形态
- verification：复验前提注明 pwsh 7 跨平台 + bash 转写口径
- SKILL.md、references/README、docs/README 索引同步

### 变更（2026-09-03，第三批：工具指南实证深化）

- reader.md 新增「环境变量」节：全量 env 面源码实证（READER_OCR_CACHE_DIR 含三平台默认值逻辑、READER_OCR_MODEL_SIZE 只认 tiny/small、GH_TOKEN for self update;ocr.rs/selfupdate.rs 逐行核对），消除上一批遗留的 [经验] 待验项
- gh.md 零节重写：吸收 代码调查 skill 五轮实测速查表（定位决策表、两级 sha 链机制、六条搜索陷阱），标注经验来源
- git.md 零节重写：吸收 git-forensics-guide(pickaxe -S/-G 分工、blame -L/log -L、bisect、ls-remote 与浅/稀疏克隆、五工具搜索边界表）
- aria2c.md 参数表全部实证重写（`aria2c --help=#all` 1767 行核对，含默认值）；新增帮助命令技巧（裸 --help 只出第一页）
- browser-harness.md 新增「零点五、脚本 helper 面」（源码 helpers.py def 清单实证）；定位改为搜索引擎与网页抓取优先
- 素材来源：代码调查 skill skill howto(gh-search-cheatsheet/git-forensics-guide）、D：\reader 仓 与 浏览器工具仓 源码、gh 与 aria2c 命令帮助

### 新增（2026-09-03，第二批：项目工具维度）

- `skills/project-evo/references/howto/project-tools.md`：项目工具约定，`.tools/` uv 运行时 Python 脚本（PEP 723 头、`uv run --script`、归档规则、沉淀铁律）+ 外部工具路由表
- `skills/project-evo/references/tools/`：外部标准工具指南五篇（gh 2.98.0 / git 2.55.0 / browser-harness 0.6.8 / reader 0.4.0 / aria2 1.37.0，版本均本机实证）+ README 索引与快速路由
- 五工具定位按用户裁定对齐：gh=搜索代码和项目仓库、git=本地 clone 研究代码仓库、browser-harness=搜索引擎和网页抓取、reader=读取本地文档电子书参考资料、aria2c=下载任意资料；gh/git/browser-harness 增设「零节」承载首要场景，README 与 project-tools 路由表增研究管线视角（发现到获取到研读）
- 自验修正：browser-harness.md 移除 emoji 违规（马形标记改文字描述）
- SKILL.md、references/README.md、docs/README.md 同步登记

### 新增（2026-09-03，第一批：骨架成型）

- `skills/project-evo/SKILL.md`:skill 概览层（定位与进化闭环、文件地图、编号体系、六目录、五步工作流、六态标记）
- `skills/project-evo/references/`:howto 五篇（primitives / docs-directories / workflow / writing-standards / init)+ pitfalls（已知误区）+ README 索引
- `skills/project-evo/verification/command-test-cases.md`：骨架规范检查命令（参数化 `$ProjectRoot`）
- `skills/project-evo/evals/evals.json`:skill 质量评估用例 4 条
- 仓库层：AGENTS.md（唯一权威源）、CLAUDE.md（一行桥接）、README.md、ROADMAP.md、.gitignore、docs/README.md（文档地图）

### 变更（2026-09-03)

- skill 由单文件 `SKILL.md` 重构为 skill 规范仓 三层布局（SKILL.md 概览 + references/howto 详参 + verification/evals 两类评估）
- skill 命名 `project-docs` 到 `project-evo`（项目进化），description 增加进化闭环触发词
- proven 语义修正：明确为**完全成功的 plan 方案归档**（立项建方案、完成回填），非里程碑/成果列表 [经验： 用户裁定]

### 移除（2026-09-03)

- 撤回用户级安装副本（`~/.claude/skills/project-evo`）与项目内 `.claude/skills/` 副本；源码唯一位置改为 `skills/project-evo/`
