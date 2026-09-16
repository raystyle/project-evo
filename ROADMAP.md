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

## 阶段二：打磨与安装（未开始）

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

## 阶段三：延伸（未开始）

| 里程碑 | 状态 | 说明 |
|--------|------|------|
| scripts/ 沉淀 | 未开始 | 骨架生成若手拼 ≥2 次，升级为可执行脚手架脚本（沉淀铁律） |
| 断链扫描工具适配 | 已完成 | 2026-09-04 落地 `.tools/md-ref-scan.py`(PEP 723 零依赖,断链检查手拼二犯升格,pre-commit 接入);第二十五批 |
