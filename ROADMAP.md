# Roadmap

阶段与里程碑状态。四态：未开始 / 进行中 / 已完成 / 挂起。随进展翻转，详细历史见 `CHANGELOG.md`。

## 阶段一：skill 成型（进行中）

| 里程碑 | 状态 | 说明 |
|--------|------|------|
| 三仓文档体系提炼（家族骨架） | 已完成 | reader 仓 / PVE 仓 / browser-harness 调研归纳 [实证： 2026-09-03 三仓实地核对] |
| skill 单文件版（project-docs） | 已完成 | 已被三层布局版取代 |
| skill 规范仓 结构重构（project-evo） | 已完成 | 初版 SKILL + references/{howto,pitfalls} + verification + evals；后续演进为意图路由 SKILL + 分类扁平 references（前缀分组）并移除 evals（见 CHANGELOG 第六/七批） [实证： 2026-09-03] |
| verification 命令自验全绿 | 已完成 | PowerShell 用例集 + Python check 双实现，脚手架产物 11 PASS/0 FAIL 实测 |
| uv Python 工具成型 | 已完成 | project-evo init/check/llms/skill；7 测全绿；v0.1.0 定版 |
| 真实项目试跑（第一个用户） | 未开始 | 找一个新项目按 skill 初始化，回填 pitfalls |

## 阶段二：打磨与安装（进行中，主体已完成）

| 里程碑 | 状态 | 说明 |
|--------|------|------|
| git init + 首版 tag + 远端发布 | 已完成 | 2026-09-03：公开仓 raystyle/projectevo,main + v0.1.0 tag 已推，Release 已发；update 版本探测闭环实测（已是最新，exit 0）[实证] |
| 插件市场转型(v0.2.0) | 已完成 | 2026-09-04 第二十八批:SpecterOps/skills 既证形态(双市场清单+双 manifest+commands/hooks);三脚本 PEP 723 化下沉 skill,uv CLI 分发通道退役;双漂移守卫随单源化取消,清单一致性守卫接棒;Codex 面实弹验收(codex-cli 0.149.1 本机:marketplace add + plugin add 成功,缓存按 manifest 版本 0.2.0 归位,51 文件全树随装)[实证] |
| 封版 v0.2.1(Windows 钩子修复) | 已完成 | 2026-09-10 第四十二至四十三批:Codex 面 PostToolUse md 挡板在 Windows 的变量展开修复(`commandWindows` 用 `$env:` 前缀 + 载荷宽容);secret-scan A/B 对照测试 Windows 编码修复;本机 pytest 全绿 [实证: 2026-09-10 本机实跑] |
| 封版 v0.2.2(skill 改名 docs-evo) | 已完成 | 2026-09-10 第四十四批:skill 目录与 frontmatter 改名 docs-evo,仓内外引用全量同步;补发 v0.2.0 GitHub Release(此前只有 tag 无 Release) [实证: 2026-09-10 本机实跑] |
| 单插件四 skill 形态(v0.3.0) | 已完成 | 2026-09-10 第四十七批:四插件收敛为唯一插件 project-evo,skills/ 下 docs-evo 与 super-research、secret-scan、office-pro 同装同版;市场清单与 manifest 单条化;客户端显示 project-evo:<skill> [实证: 2026-09-10 本机实跑] |
| 封版 v0.3.1(aria2c 下载关 IPv6) | 已完成 | 2026-09-11 第四十八批:super-research aria2c 参考三处落地 `--disable-ipv6=true`(标准命令/参数表/坑表);用户裁定本机网络 IPv6 到镜像站有坑 [实证: 关后 TUNA 镜像 16 连接 21MiB/s] |
| office-pro skill 移除(v0.6.0) | 已完成 | 2026-09-15 第四十九批:office-pro 全目录与 office-cli 命令下线,仓内外引用全量同步,清单面改三 skill;S007 研究档案保留;与第五十、五十一批合并发 v0.6.0 |
| dev-evo 文档即代码重构(v0.6.0) | 已完成 | 2026-09-15 第五十批:docs-evo 改名 dev-evo,知识体系全面替换为文档即代码(AGENTS 五节合同/ADR/REQ/投影纪律/三栈对照),init/check 重写,references 17 到 18 篇,本仓 docs 迁移(adr/requirements 落地,AGENTS 五节化) [实证: 本机 pytest 全绿 + 自家 check 自检] |
| security-audit skill 集成(v0.6.0) | 已完成 | 2026-09-15 第五十一批:Cloudflare security-audit-skill(MIT)全量中文化集成,四 skill 形态:SKILL.md 中文版 + 14 篇 audit- 前缀 references + validate .cjs 校验脚本随行;三清单与六件套同步,版本 0.6.0(与四十九、五十批合并发布) |
| 项目级安装通道验证 | 已完成 | 2026-09-03 remotex 首装实测：init 补 6 件跳 5 件（含 AGENTS.MD 大写碰撞安全跳过）、check 8 PASS/4 FAIL（FAIL 均为存量文档真实差距）、skill 双落位 + gitignore 幂等；全程未改既有内容文件 [实证] |
| 与其他 skill 的分工说明 | 已拒绝 | 用户裁定（2026-09-03):project-evo 是独立项目，不与其他 skill 划分边界 |
| PE-11 历史档案豁免通道 | 已完成 | 2026-09-16 第五十三批:`PEVO_CHECK_ALLOW` 落地(docs/ 下路径级豁免报 SKIP,根三件永不受益;ark_rs 首批用户同款诉求,先于反馈已交付) [实证: pytest 豁免三分支用例] |
| 三栈工具篇补齐与档案机制入册 | 已完成 | 2026-09-16 第五十六批:tool-python.md 补齐三栈、flow-archive.md 固化 diary 与 research 机制、ADR-0005;references 18 到 20 篇 [实证: 三仓落地性回执支撑] |
| 封版 v0.7.0 | 已完成 | 2026-09-16 总台统一封版令:第五十七至六十四批治理基建八批(PE-11 豁免通道、aidoc 补全与强制、契约注释纪律、agent CLI 三栈、终态清理定形 ADR-0007 与 0008、连接姿势与飞轮篇、pwsh 与版本与分发标准);tag v0.7.0 加 Release |
| 封版 v0.6.0 | 已完成 | 2026-09-16 第四十七至五十六批合并发布:单插件四 skill 形态(dev-evo/super-research/secret-scan/security-audit)、dev-evo 文档即代码体系、PE-11 豁免通道、diary 与 research 红线、三栈与档案机制;tag v0.6.0 加 GitHub Release |
| check 全量报告(去前 5 截断) | 已完成 | 2026-09-16 第六十五批:PE-05/06/07/08/10/11/12 违规清单去截断全量输出,PE-11 由每文件首行改逐行全列 [实证: pytest test_check_reports_all_violations 七处全列] |
| PE-12 扫描面扩散到检索面 | 待定 | 2026-09-16 首批用户反馈(ark_rs):断链扫描现只盖 AGENTS 与 docs 各 README,llms.txt 等新检索面是盲区 |
| 存量迁移映射表生成物 | 待定 | 2026-09-16 首批用户反馈(ohmycloud):旧编号到新编号对照宜机器生成落盘,人写注记即漂移面,生成物可进门禁 |
| check 一次性迁移修复子命令 | 待定 | 2026-09-16 首批用户反馈(ohmycloud):PE-10 标题括号批量转冒号形,存量首对齐手搓约 25 文件,收尾成本落在用户侧 |
| ADR/REQ frontmatter 字段表显式化 | 待定 | 2026-09-16 首批用户反馈(ohmycloud):base-adr/base-req 正文状态体态与 PE-06/07 frontmatter 判式不对应,被打回两轮才定位契约差 |
| check 输出 --json 机器读面 | 已完成 | 2026-09-16 第六十五批:JSON 载荷 ok/counts/results 含结构化 violations,退出码 0/1/2 不变,回执读 counts.skip 不再正则抓 stdout [实证: pytest JSON 三用例] |
| init 模板 rumdl 撞规预防 | 待定 | 2026-09-16 飞轮批反馈(hst_rs):ADR/REQ 模板 YAML title 与 rumdl MD025 默认规则必撞,init 宜检测并自动落 front_matter_title 空串 |
| 整文件豁免形态官方示例 | 待定 | 2026-09-16 飞轮批反馈(hst_rs):路径前缀正则不带冒号即整文件豁免(hst_rs 以 ^docs/proven/ 实证),gates.md 补官方示例,免各仓自造前缀式 |
| skill-spec 对表 agentskills 新字段 | 待定 | 2026-09-16 S008:allowed-tools(Experimental)与 metadata 可选字段是否引入待评估,skill-spec.md 对表现行 spec |
| PE-12 同目录裸文件名误报 | 待定 | 2026-09-16 终态对齐批反馈(hst_rs):断链检查只认根相对路径,README 同目录裸文件名(中文 S 件名)误报,被迫去反引号规避;建议支持 README 相对解析或明示根相对口径 |
| check.py 下游拷贝哈希锁 | 待定 | 2026-09-16 构建树仓用户反馈(clean-chrome):仓内 tools/check.py 拷贝静默落后权威版照旧 12/12 绿,双份漂移靠 diff 才暴露;机制化为拷贝头内嵌版本或内容哈希,门禁自检不匹配即 FAIL 提示自插件重同步,飞轮对齐轮顺手刷新锁;强制引用权威路径不取(破仓自包含,换机即断) |
| 仓本地路径排除标记(.evoignore) | 待定 | 2026-09-16 构建树仓用户反馈(clean-chrome):树遍历类工具对超大仓(约 100GB 构建树,上游字节含禁字绝不许改)是性能与误报双坑;标准固化双规则:门禁类工具一律候选列表式(显式包含域),必须走树的工具统一认仓根 ignore 标记文件进 mdrules 同源;env 豁免管内容、ignore 管路径,两层不混;仓本地文件优于环境变量(随仓走不随机器走) |
| C/C++ 第四栈工具篇 | 已拒绝 | 2026-09-16 构建树仓用户反馈(clean-chrome):三栈加通用裁定出口现状够用,通用件(确定性产物门禁、构建门禁在册、裁定句)已提炼入 base-projection 无自有 API 面小节;整栈篇会引入用不到的面,出现第二个有自有 C/C++ 代码的项目再议 |
| herdr 飞轮 skill 增编与 flow-flywheel 退役 | 已完成 | 2026-09-16 第六十六批:总台派单 A/B/C/D 全件;第五 skill herdr-flywheel 落地(协议全量吸收、老参考清除),ADR-0009 supersede ADR-0008,四 skill 形态扩五;两仓实践轮真派单真回执 [实证: check 12 PASS 加 grep 零死链加实践轮对账] |
| 市场更名 project-evo 与四插件重组 | 已完成 | 2026-09-16 第六十七批:市场名与 GitHub 仓统一 project-evo;四插件 evo-adr/evo-codesec/evo-research/evo-herdr 七 skill;dev-evo 拆 doc-gov 与 code-kit,super-research 拆 research 与 report(吸收家族研究仓报告生成实践);ADR-0010 supersede ADR-0001;REQ-002 落地 [实证: pytest 26 全绿加 md-ref-scan 七 skill 零断链加 render 130 KB 样例] |
| herdr 评审闸门 skill 增编 | 已完成 | 2026-09-16 第六十八批:evo-herdr 第二 skill herdr-review(评审请求五件模板、F/G/CONFIRM 回执轮次、发现核实与交叉复核、评审窗格检测带起);ADR-0011 修订 ADR-0010 清单为八 skill;REQ-003 落地 [实证: 命名评审格实建 evo-codex-review 加第六十七批评审单实发加 pytest 全绿] |
| gh-issue skill 增编 | 已完成 | 2026-09-16 第七十二批:evo-adr 第三 skill,命令出错自动上报 GitHub issue(定位仓、双通道去重、模板正文、自动发单、三态回执);ADR-0012 修订 ADR-0010 清单为九 skill,REQ-004 落地 [实证: 命令面本会话实跑加自发实证单验后即关加 pytest 全绿] |
| 封版 v0.8.0 | 已完成 | 2026-09-16 第六十五至七十三批九批合并发布:check --json 机器读面、herdr-flywheel、市场更名 project-evo 与四插件重组(ADR-0010)、herdr-review 评审闸门(ADR-0011)、gh-issue 第九 skill(ADR-0012)、发现通道收敛 llms;四插件 0.1.0 升 0.2.0;tag v0.8.0 加 Release |
| build-release 指导 skill 增编 | 已完成 | 2026-09-17 第七十五批:evo-adr 第四 skill,仓无关编译打包发布流水线标准(六型配方七要素、公共契约、可拷改模板四件);总台六轮追正定形,通用性终约束私有名零出现;ADR-0013 修订清单为十 skill,REQ-005 落地 [实证: pytest 全绿加 md-ref-scan 十 skill 零断链] |
| 封版 v0.9.0 | 已完成 | 2026-09-17 第七十五批合并发布:build-release 流水线标准指导 skill(含上游追新追正一笔);四插件 0.2.0 升 0.3.0;tag v0.9.0 加 Release;三端更新铺开随封版走 |
| cli-docs 对外面双标准 skill 增编 | 已完成 | 2026-09-17 第七十七批:总台立单,evo-adr 第五 skill(甲面 README 四节骨架标杆研究定稿、乙面 agent 五件 --llms 手册加旗标全家 CTA 协议加默认帮助面加自省加裸调用面);ADR-0014 修订清单为十一 skill,REQ-006;私有名零出现 [实证: 四标杆 README 实读加 hst 与 omc 契约实读加 pytest 全绿] |
| Prove2Me DAG 协作模型吸收进飞轮 | 已完成 | 2026-09-17 第七十八批:S009 研究档案(十二则核验与飞轮对照分流);herdr-flywheel 增并行派单与义务图节六纪律与 references/parallel.md 操作细化,纪律标 [经验] 待首跑回填;描述触发词双 manifest 与市场三处同步 [实证: pytest 全绿加 md-ref-scan 零断链加 check 12 PASS] |
| 封版 v0.10.0 | 已完成 | 2026-09-17 第七十七至七十八批合并发布:cli-docs 对外面双标准 skill(ADR-0014 十一 skill)与 Prove2Me DAG 协作模型吸收进飞轮;四插件 0.3.0 升 0.4.0;tag v0.10.0 加 Release;五端铺开随封版走 |
| 守卫断言扩展与机检盲区 | 待定 | 2026-09-16 评审批(codex):守卫未断言「市场描述 == manifest 描述」与 references/README.md 存在(security-audit 索引已补,守卫断言仍缺)与插件 README「当前发布」行对齐 manifest 版本(两轮封版靠人工核;第七十八批双 manifest 漂移再实证此缺口,靠纪律补位);md-ref-scan 只认首个 root 实参(多根静默忽略,现靠逐次调用规避);跨 skill 散文式指针(无 .md 后缀)与节号引用(如「triple-output 第五节」)不在机检范围(快核轮实抓节号悬挂一处);PE-10 标题括号扫描面不含 plugins/,插件面存量同形标题 109 处(第七十八批评审 G3 记档) |
| gh-issue 与 build-release 与 evo-research 移除 | 已完成 | 2026-10-07 第八十七批:四插件十 skill 收敛三插件七 skill;evo-adr 收敛 doc-gov/code-kit/cli-docs,evo-research 整插件下线(破坏性,消费者卸载);ADR-0016 与 REQ-008 落地;版本线 0.4.3 不动待整理重构批统一打版 |
| evo-codesec 插件下线与 md 挡板限仓内 | 已完成 | 2026-10-07 第八十八批:evo-codesec 整插件移除(secret-scan 与 security-audit 双 skill,破坏性,消费者卸载),test_secret_scan.py 退役;md-guard hook 辖域限仓内 md(md 五面核实已只认 .md);ADR-0017 与 REQ-009 落地;市场收敛两插件五 skill,版本线 0.4.3 不动待整理重构批统一打版 |
| doc-gov 三合一与 evo-doc 改名 | 已完成 | 2026-10-07 第八十九批:三 skill 合一为 doc-gov(知识面收敛 ADR 加 COE 加项目日记三形态与 Agent 友好 CLI 架构标准,references 20 篇收敛 7 篇,base-diary 与 base-coe 新写);evo-adr 改名 evo-doc(破坏性,卸旧装新);skill 与 hook 解耦(md-guard 加 mdrules 上插件级 scripts);init/check/scan 与模板移本仓 .tools;ADR-0018 与 REQ-010 落地;市场收敛两插件三 skill,版本线 0.4.3 不动待打版批 |
| herdr 委派与窗格布局轻吸收 | 已完成 | 2026-10-07 第九十批:S011(herdr-dispatch 对照,py 脚本评估结论不开发)加 S012(四窗格通用定式与 PI 五窗格特化,用户裁定);herdr-flywheel 增布局定式与双闸门节、任务分发 lane 模型节、references/lane-dispatch.md、pitfalls 三坑;REQ-011 落地 |
| herdr 双模式定形 | 已完成 | 2026-10-07 第九十一批:herdr-review 并入重组为 herdr-dev 开发模式(布局定式、评审闸门、自省验收、lane 分发,references 五篇);herdr-flywheel 收敛跨仓模式(多仓工作台对话交流);ADR-0019 与 REQ-012 落地;版本线 0.4.3 不动待打版批 |
| 挂接面回归测试补强 | 已完成 | 2026-10-07 第九十三批:hooks.json 与 settings.json 挂接路径、pre-commit 断链段对 SKILLS 一致性、CI 引用存在性三用例(REQ-014);套件 25 绿 |
| 封版 v0.11.0 | 已完成 | 2026-10-07 第九十四批:第八十七至九十三批合并发布(两插件三 skill 形态、版本线 0.4.3 齐 0.5.0);tag v0.11.0 加 GitHub Release;破坏性通告三插件卸载与 evo-doc 换装 |
| herdr 集成 py 脚本重评估 | 已完成 | 2026-10-08 第九十六批(REQ-015):部分翻转;S011 原写触发(lane 探针/扫描)未 fired,但舰队运维轮普通进程通道手拼十余次,沉淀铁律在总台面成立,建本仓 .tools/fleet-exec.py 运维薄封装(逐条回显 herdr 命令);插件面维持纯知识(ADR-0018 不动);lane 实跑二犯再议插件面与更重脚本;kimi 委派驱动仍待专项研究 |
| 封版 v0.11.2 | 已完成 | 2026-10-09 第九十八批:doc-gov 四形态定形(增研究档案 base-research)与项目工具链范式(tool-project-kit),references 7 至 9 篇,裁定形态跟项目形态走只有合适的没有硬性;REQ-016 与 S013 落地;版本载体 0.5.1 齐 0.5.2;tag v0.11.2 加 GitHub Release |
| 封版 v0.12.0 | 已完成 | 2026-10-10 第九十九至一百批:herdr-flywheel 产物契约三件套 brief/state/receipt 与盘上稳态信号分治(REQ-017,邻居窗格回归实测);三插件五 skill 版图(ADR-0020):evo-skills 立项 distil-skill 技能自进化(三层聚合加合取闸门,S014 wikiskill 对照)、doc-gov 三向拆分(native-design 抽离)、herdr-dev 更名 herdr-orch;版本载体齐 0.6.0;tag v0.12.0 加 GitHub Release;业界对照评估与四端无头模式研究吸收(wiki-03/04) |
| 四仓三层聚合标准合流 | 已完成 | 2026-10-10 第一百零一批:ADR-0021(sources 唯一出处层、git 边界三选一含单仓纪律形、归档统一字母表八元组、doc-gov 工件归层、operations 两类与加载视图、闸门证据形态扩、supersede 否证流、CoALA 映射、业界负对照排除);distil-skill 与 doc-gov 文本随 22 项修订清单落地;三实践仓施工单回执断言收口(ai-ccoe 正名五动作加 R1 至 R3 小修、browse_rs 三层从零建加首技能 gate-verdict 人裁入集与触发对实证、pve-harness 归档统一加 Python 代码即文档;其间会话中断盘上续派一次,租约纪律实证);REQ-019 与 S015 落地;check PE-02/03 扩双形;终态判据六条全仓验收过;版本线 0.6.0 不动待封版批 |
| md-guard 按仓豁免配置 | 待定 | 2026-10-10 pve-harness 施工报备:插件 md-guard 钩子对下游仓自有豁免路径与 external 第三方原文三度误拦;钩子豁免按仓配置机制待立(积压) |

## 阶段三：延伸（进行中）

| 里程碑 | 状态 | 说明 |
|--------|------|------|
| scripts/ 沉淀 | 未开始 | 骨架生成若手拼 ≥2 次，升级为可执行脚手架脚本（沉淀铁律） |
| 断链扫描工具适配 | 已完成 | 2026-09-04 落地 `.tools/md-ref-scan.py`(PEP 723 零依赖,断链检查手拼二犯升格,pre-commit 接入);第二十五批 |
