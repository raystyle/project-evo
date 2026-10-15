# Changelog

本文件记录 project-evo skill 及本仓库的所有可交付变更。格式：新增/变更/修复/移除 + 日期；先写 `[Unreleased]`，发布时转版本（git tag）。

## [Unreleased]

### 变更 2026-10-15 第一百五十九批:命名标准六裁定对齐,总台对齐单

- **v3.2.4 同步**(REQ-048):命名标准定稿六裁定(别名活注册、编号 = 出生序号非格位、新标准形禁下划线、start 拒非标形、起名全局扫全舰队、台名 1-22)入 skill:addressing 命名标准节全刷(四概念开篇:节点名/工作台名/窗格名/agent 别名;正则标准形;起名两闸),agents SKILL start 动词行补两闸注(非标形 rc=2、撞名全局扫 rc=2)加文法命名标准行随刷;旧「编号即格位」「非标形提示不拦截」语义出清
- 验收实弹:非标形(下划线名)与撞名(在役名)两发各验,双 rc=2 正响
- evo 独立升 0.15.9;四门禁全绿 + fleet 回执

### 变更 2026-10-15 第一百五十八批:双轨制信封与房间面收编,总台令

- **核验单 F1-F4**(REQ-047;research-grok-1 核验单 share/lan-win/289df2185a,F5/F6/F7 总台已修 prim v3.2.2):信封文档改渲染函数实形(F1:deliver-gate 模板行 from=host_label:别名、双轨注、回信取用裸别名;addressing 回信节 session 直配三级退化全刷;collab 拆回信与取文件两句;agents id 行双轨句;shares/streams 交付取用行改裸别名,键与流名归字段行,取文件命令入坑表);streams 房间面整段收编(F2:rooms/room/dm 三动词照手册、view 带 -f、--file 整档上架语义、stdin 管道道、fleet 是房;commands 速查与 collab 尾读同步);commands 标头对 v3.2.2 加差异三行(F3);死例子换活名(F4:local:w13:p1、去 lan-win、ai-ccoe-claude-1、put 打印键指引形);G1/G4 顺带(collab 私信补 dm 动词、shares get 真键形)
- tasks 取用(tasks view)与 pipes 取用(tailcat)遵核验单 CONFIRM 1 未裁定不动,与 v3.2.2 代码对齐
- 终核:六面 --llms 对 v3.2.2 逐面零漂移;四门禁全绿
- evo 独立升 0.15.8;fleet 回执

### 变更 2026-10-15 第一百五十六批:skill 对抗审核 F 项修复,总台令

- **F1-F13 加 G1/G2/G7**(REQ-046;grok 审单 share/lan-win/6cf96633fd,对象 evo 0.15.5 对 prim v3.1.8;代码面 G3/G5/G4/G6 总台已修 prim v3.1.9,本端核对零漂移):取用行余量收口(F1 坑表按审单、F5 坑表去 s5 字样)、tasks view 远机声称修正(F2)、示例可复制化(F4/F9,五域 view 各留一条带参形,活名 evo-claude)、streams 旗标或形与复述收敛(F6)、agents 正文六主动词与工位在场族下放 references/workspace.md(F8)、ctx 示例换 --llms 四行加坑行可判定加接着读去两级跳(F10)、pipes 触发词去引擎名与缺口挪文法(F11)、六域触发词修漏误(F12)与 agents 去 AGENTS.md 路径词(G2)、六域分工节收文法一行(F13)、插件 README 与 codex interface 旧语清(G7)
- 验收:六域动词表文法对 prim v3.1.9 --llms 逐面核对一致;四门禁全绿
- evo 独立升 0.15.7;fleet 回执

### 变更 2026-10-15 第一百五十五批:信封取用行全原语化同步,总台令

- **v3.1.8 同步**(REQ-045):信封取用行全原语化(用户令:原语更抽象更直觉,引擎名不漏照抄面;win 面裸 s5 本不存在,旧取用行是照抄即炸死链,兼正确性修):shares 取用 `s5 get -o` 改 `shares get <键>`、tasks 取用 cd 加 hst 直读改 `tasks view`、streams 文法补 `streams view <流> -n 20`、collab 协议面注与 deliver-gate 取用行随域词汇表同步、obsolete 旧形归档;pipes 取用暂留 tailcat(send 原语缺口 CONTRACT 记档,勿改);commands 差异表重拼标题与 obsolete 标题括号全角顺手修
- 验收实弹:shares to 本地格,信封取用行 = `shares get <键>`;本端拉新装 prim v3.1.8
- evo 独立升 0.15.6;四门禁全绿 + fleet 回执

### 变更 2026-10-14 第一百五十四批:信封机器段目标感知同步,总台令

- **v3.1.7 同步**(REQ-044):信封 from 机器段目标感知 = 同机 local 形(本机别名不在自己机册)、跨机在册别名形,真 hostname 永不进路由位;deliver-gate 信封规范行补两形与回信直答注;commands 差异表 from 行改现行形;addressing 与 pitfalls 旧 hostname 判例出清,分叉史(AI-LAB 对 lan-win,机器改名注册挂起,重启合一)归档 rulings.md
- 验收实弹:local 到 local 投递回环,信封 from=local:w8:p1 to=local:w8:p1 v=1,local 形实证;本端拉新装 prim v3.1.7
- evo 独立升 0.15.5;四门禁全绿 + fleet 回执

### 变更 2026-10-14 第一百五十三批:写作标准采纳与六域过标,总台令

- **标准采纳**(REQ-043):「命令指导 SKILL 写作标准」入 docs/guides/skill-spec.md(命令指导类节,出处 = fleet room/gateway-logging 草案链保留);description 压 400 字符、正文五节序、--llms 指针、references 三档、验收八条俱为本仓 skill 写作长期依据
- **六域过标**:evo 六 skill 全套重写(ctx 先行样稿):description 前后(字符)= agents 904 到 230、shares 395 到 166、streams 529 到 182、tasks 421 到 125、pipes 436 到 130、ctx 839 到 175;正文五节序与坑表错|对形,定位段删除,分工一行;agents references 三档落盘(pitfalls、rulings、obsolete),存量知识件标签与哈希注记出清
- 验收自检过:四词全文零命中、抽三命令对 --llms 一致实弹退 0、回指修正;evo 独立升 0.15.4;四门禁全绿 + fleet 回执带字符对比

### 变更 2026-10-14 第一百五十二批:evo skill 减熵批,总台令（用户令）

- 六域 SKILL 正文与 references 知识面减熵(REQ-042):批号引用、根修来龙去脉、误判轨迹叙事撤出;坑与规则收敛一行正确姿势;description 发现面不动;功能零漂移(ctx search 多词实弹自验绿);evo 独立升 0.15.3;commit 标题自本批起一行形

### 变更 2026-10-14 第一百五十一批:ctx 在途降级判例收编（v3.1.4）,总台令

- 批 150 观察定谳根修落 v3.1.4:管道时序 = 正文块先入 gwlog、头行随 request_end 批后入(近 10 分钟在途差);show 对在途 rid 降级出「头行:未落」加正文块先行,双无记录才 not_found
- ctx skill 坑表改判例行(在途降级属正常非错误);本端重装 v3.1.4;evo 独立升 0.15.2;四门禁全绿 + fleet 回执

### 变更 2026-10-14 第一百五十批:ctx skill 对齐 prim v3.1.3,总台令

- **v3.1.3 面收编**(REQ-041;v3.1.0 稿漂移全刷):检索道 ssh 单道改直连 https 8123 主道(双闸 = client 证书 TLS 层加 basic ctx_reader SELECT-only;CTX_* 环境变量优先,~/.ctx/reader.env 六键 600)加 ssh 兜底;动词面增 show --around <词> --window N(命中块±N 邻块,命中点居中 3000 字,SQL 侧全文匹配)与 search --term 多词 OR 加 snip 片段列;坑表三入(词至少 2 字符、嵌套抓 rid 用 --limit 1 且切列认准 f8/f1、块命中 rid 无头行属管道时滞)
- 三发实弹全绿:search 多词(收编 OR ensure_ascii)出 snip 命中退 0;show --around 收编 --window 1 出命中块 [16] ±1 带命中点居中标注退 0;view --limit 3 表头加三行退 0;途中两踩列位坑(rid 取 f8/f1)入坑表;观察一件报总台 = search 命中 rid 而 show 无记录(块先入头后入时滞)
- 本端 prim 滚至 v3.1.3(ai-ccoe main 5b43650;中间版残差 stash 路弃用,总台已复位);evo 独立升 0.15.1;四门禁全绿 + fleet 回执

### 变更 2026-10-14 第一百四十九批:六原语收编 ctx 对话历史域,总台令

- **ctx 第六原语**(REQ-040;prim v3.1.0,e98e4af 起实装):新 skill evo:ctx = agent 请求全链检索历史档案面(引擎 ClickHouse gw_logs,ssh 道进容器内 client 免证书面);动词 view [agent] [--limit N] 与 show <request_id> 与 search <关键词>;窗口 head 365 天正文 180 天;与 agents read 分工 = read 实时屏对 ctx 历史档案
- agents 枢纽升六原语(定位、description、路由行、保留动词表增 show/search、read 分工注);commands.md 六域速查加 ctx;守卫与路由面全随形(evo 七 skill 共十,pre-commit 十目标,市场清单);evo 独立升 0.15.0
- 本端滚装 prim v3.1.0(六命令入口含 ctx,ctx --llms 实测);实弹两发如实报件 = 本机 ssh 道无 lan-linux2 凭据,ctx view 与 ctx search 均 engine_fail 退 1(错误原文 stderr,退出码实测),链路全通待总台侧或配钥后验;四门禁全绿 + fleet 回执

### 变更 2026-10-14 第一百四十八批:改面收编 tasks 实时任务面与引擎容错,总台令（顺手批）

- **tasks view 实时任务面**(REQ-039;prim 369e57b):fleet 各格状态总览(标记在跑)加各格仓内 hst task show 直读,tasks/shared 历史事件流弃用(set 不再写事件,旧档只读);tasks SKILL 与五域速查与差异表随改,tasks 事件 prev 差异行销账;streams 与 collab 保留策略去 tasks/shared 面
- **herdr_run 容错**:超时/离线机回 rc=124 不抛栈,view 跳过不可达机单行告警;tasks 坑表与 agents 坑表与 addressing 坑簿随改(离线不挂死)
- 实证:本机重装后 tasks view 实测(实时总览);evo 独立升 0.14.4(dev 不动);四门禁全绿 + fleet 回执;rollout 双到位闸门维持

### 变更 2026-10-13 第一百四十七批:差异表对 ef8fca6 全刷,总台令（互审 CONFIRM 家庭作业）

- **实证三修**(REQ-038;本机重装 ef8fca6):caller_addr 同 cwd 多格歧义不猜(自探针回环,告警加退化取用行双落地);close 零击杀(/exit 优雅退加 shell exit 末步);reload 名字保真(存量名保名,非法名自修正披露 old-name)
- 差异表全刷:caller_addr 行改歧义已修;**新入漂移行 = 手册 close 语义滞后于零击杀码**(手册仍书「分裂格杀 shell」,报总台);表头实态升至 ef8fca6;agents SKILL close 行改零击杀、reload 行补保名;addressing.md 同 cwd 判例更新
- evo 独立升 0.14.3(dev 不动);四门禁全绿 + 回执贴台;总台走 rollout 序,六端 reload 归其辖

### 变更 2026-10-13 第一百四十六批:对抗式 review 协议单收编,总台令

- **三新动词入 skill**(REQ-037;prim ai-ccoe main 04ba9bf):agents 补 close(关格三形)、reload(同格同 session 重进翻台,四家 resume 形,resume 失败自回滚裸形 fresh-session 披露)、wt(win 专属本窗开 tab 显任意机 herdr 视图);保留动词表与触发词随改
- **重载铁律入坑**(总台 Q5):旧进程 = 旧技能,装更插件后必 agents reload 翻台;shares 补版本链传 sha 反射(键取用面加 sha 验证面,总台 Q4 实操面);browse update 滚版注为外部工具自面不入五原语
- **rollout 段入两插件 README**:全端序 = 市场更新、卸旧五插件、装 dev 与 evo、全格 agents reload;Kimi 清目录重拷重启
- 实证:本机重装 prim 04ba9bf;evo 0.14.2 加 dev 0.14.3 独立升;四门禁全绿;回执贴台 = 五问答卷(触发歧义矩阵、hook 面核对、漂移全列、实操覆盖、安装序)加我方攻单(动词缺口、门控误判面、reload 误标、信封退化道)

### 变更 2026-10-13 第一百四十五批:zh-lint 删除,用户令

- **终裁**(REQ-036):zh-lint 删除,中文语言纪律不设 skill 面(沿革 = 批 141 三合一、批 144 拆出复独立、本批删除;工具与判例存 git 档案);终形回两插件九 skill = dev 三(doc-gov、dev-cli、dev-lint)加 evo 六
- dev-lint 去姊妹指路,沿革改写;test_zh_lint_tool 退役;守卫与路由面全随形(SKILLS、pre-commit 九目标、双 manifest 与市场清单、AGENTS 与根 README 与 docs 地图与 dev README);ADR-0025 终形改九
- dev 独立升 0.14.2(evo 0.14.1 不动);四门禁全绿 + fleet 回执 + 知会 grok(评审 2 终局 = 删除)

### 变更 2026-10-13 第一百四十四批:拆中文面 zh-lint 复独立,用户裁定

- **裁定落形**(REQ-035;grok 评审 2 触发竞争论获采纳):zh-lint 复独立 skill 归 dev,SKILL 与 references 索引自 git 史恢复(分工行随新形:dev-lint 管格式禁字断链结构,zh-lint 管语言清晰度),stc-rules 与 reporting 复原名,scripts/zh-lint.py 随迁回
- dev-lint 瘦身:description 与路由与速览去中文面(约 711 字跨域触发竞争解除),触发词去 zh 域,六篇 references,zh-lint.py 指路姊妹 skill
- 守卫与路由面随形:SKILLS(dev 四 skill)、pre-commit(十目标)、双 manifest 与市场清单、AGENTS 与根 README 与 docs 地图与 dev README(两插件十 skill);ADR-0025 补裁定;dev 独立升 0.14.1(evo 0.14.1 不动)
- 四门禁全绿 + fleet 回执 + 知会 grok 评审闭环;市场 tag v0.16.0 候打(裁后即备)

### 变更 2026-10-13 第一百四十三批:from 判例收编（grok 回信信道实弹）

- **判例**:grok 评审回信暴露 from=<host> 用 hostname 而非在册机标签,同机回信 hostname 形不可解析(本机 lan-ubuntu 对在册标签 local,`agents to lan-ubuntu:w8:p1` not_found),按名回信(evo-grok-4)成;同 cwd 多格时 caller_addr 首命中可能误指他格(w8:p4 的信写 w8:p1),以名为准 [实证:双向实弹]
- addressing.md from 核验节与 commands.md 差异表各落一行;evo 独立升 0.14.1(dev 不动,独立 semver 首例);报总台 prim 侧:from= 建议改用注册标签或同机 local
- 命名标准活例:evo-grok-4(工作台-类型-编号)自起名并按名寻址成

### 变更 2026-10-13 第一百四十二批:grok 业界先例评审吸收,总台令（收口与独立 semver 与命名细节）

- **评审来源**:邻居 grok(w8:p4)对照业界先例(Claude Code 插件市场、VS Code 扩展、npm scope 与 changesets、oh-my-zsh)六条;全文 /tmp/grok-evo-review.md;**裁定落五条,一条 hold**(拆 dev-lint 中文面与用户明令 lint 三合一相抵,候用户裁)
- **收口**(评审 1):根 README 安装例与挡板行与文档表残留 evo-doc 三处清零;doc-gov 路由行 evo:distil-skill 改 evo:distil、evo:dev-cli 改同插件 dev:dev-cli;dev 与 evo codex 面 shortDescription 与 defaultPrompt 随终形(zh-lint 改 dev-lint,evo 去诊断);AGENTS 当前阶段随批 141 与 142
- **独立 semver**(评审 3):两插件各自升版本(本批双改,dev 与 evo 各进 0.14.0),市场快照仍走 git tag(下一号 v0.16.0 候打);守卫改独立校验(0.13 起可混装,弃同号硬锁)
- **命名细节**(评审 4):keywords 分域(dev 去 fleet、evo 去 lint);agents description 加适用域句(读项目协作规则文件 AGENTS.md 时本 skill 不适用,防误触发);shares/streams/tasks/pipes 四域 description 瘦身(门控信封复述删除,共享规则只留 agents 一处)
- **distil 压缩**(评审 5 轻形,distil 归 dev 候下轮):description 约 767 字压至约 350 字,触发词蒸馏保留
- **hook 与环境变量**(评审 6):lint-hook、mdrules、md-guard 留 dev 插件根,zh-lint.py 留 skill scripts(现状确认);EVO_LINT_* 三环境变量新名 DEV_LINT_*(旧名再认一版,下版移除),hook-face 表随改
- 保持项(评审结论同向):不恢复五插件、五原语不并回、hook 不进 evo;REQ-034 在册;四门禁全绿 + fleet 回执 + 回信 grok

### 变更 2026-10-13 第一百四十一批:lint 三 skill 合并为 dev-lint,用户令

- **dev-lint 落形**(REQ-033;ADR-0025 续令):md-lint、ls-lint、zh-lint 三 skill 并一归 dev;SKILL.md 意图路由四类面(md 面、语言面、结构面、中文面)加门禁速览;references 八篇扁平前缀分组加索引;scripts/zh-lint.py 与四类型模板随迁;触发词三合一(旧名保留)
- 守卫与路由面随形:SKILLS 清单、pre-commit 断链段(九目标)、双 manifest 与市场清单、AGENTS 与根 README 与 docs 地图、dev README;版本载体 0.13.0 进 0.13.1(两插件同线);终形 = dev 三 skill(doc-gov、dev-cli、dev-lint)加 evo 六 skill;四门禁全绿 + fleet 回执

### 变更 2026-10-13 第一百四十批:市场重构两插件 dev 与 evo,用户令（五原语拆分与四裁撤与两改名）

- **市场终形**(REQ-032;ADR-0025,用户令数条渐进定形):两插件十一 skill = dev(开发治理面:doc-gov、dev-cli、md-lint、ls-lint、zh-lint)与 evo(agent 操作面:agents、shares、streams、tasks、pipes、distil);市场后续按域可再添插件
- **裁撤四 skill**:herdr-orch(淘汰序留档改删除)、agent-s5、agent-rloop、agent-doctor;config-lint 测试族随 agent-doctor 退役;存活面与路由面引用清零或改注历史
- **agent-prim 拆五原语 skill**:agents(消息域原语与共享面枢纽,持 id 三产生式、命名标准、门控 v2 尾窗、信封 v2、status 四态、协作惯例、差异表四 references)加 shares/streams/tasks/pipes 四单文件域面(相对链指共享面);触发词按域自然语化(fleet seq 44 延续)
- **两改名**:doc-cli 改 dev-cli 随 doc-gov 归 dev;distil-skill 改 distil(触发 = 蒸馏);lint 三 skill 与 md-guard、mdrules、lint-hook 及写后 hook(段名 dev file-check)归 dev;evo 纯 skill 面
- **守卫与路由面随形**:测试 PLUGIN/SKILLS/市场一致性/断链段/段名断言/活面计数守卫(两插件十一 skill),pre-commit 断链段(十一目标),check.py 路径;AGENTS 定位段与 Commands 与 Must 与 Read first、根 README 定位与 skill 表、docs 地图、双 manifest 与两市场清单、两插件 README;版本线 0.12.2 进 0.13.0(两插件同线)
- 四门禁全绿 + fleet 回执;部署道 = 各端卸旧五插件装 dev 与 evo(市场条目已换)

### 变更 2026-10-13 第一百三十九批:R2 复核收编（起名校验与取用行降级）,总台令

- **R2 两件实测过**(REQ-031;ai-ccoe main 6bb8a6b,本机重装后):起名校验 = `agents start` 非标准名 stderr 提示不拦截(正则 = 台标签-类型(-编号 可选),类型族 claude/codex/grok/kimi/pi)[实证:非标准名实测出提示];取用行降级 = cwd 无格匹配时 caller_addr 退化告警 [实证:/tmp 直调] 加取用行自动降级指 agents view 定位(总台来信取用行即在飞活证)
- addressing.md:命名标准节标已收编契约八,新增起名校验 bullet;from 核验节取用行降级 bullet 重写(告警加降级形判例);坑簿 hostname 行闭注(PRIM_HOST_LABEL=lan-win 已配 win 用户环境变量,旧投递属进程内 env 未续一次性,新会话起生效)
- commands.md agents 工位管理 bullet 补起名校验指引;版本线 0.12.1 进 0.12.2;四门禁全绿 + 回信总台与 fleet 回执

### 变更 2026-10-13 第一百三十八批:agent-prim 信封 v2 对齐与 agent 命名标准,总台令（与 R1 批合轮）

- **信封 v2 收编**(REQ-030;ai-ccoe main fb701a7+41ca290,pydantic 真源 prim/src/prim/msg.py):deliver-gate.md 信封节重写 = 人话行 @收方、字段行 `from=<host>:<pane> to=<id> 域字段 v=1`(from/to 恒在,v 恒带,收方 parse_fieldline 机读,旧形 src= 收旧拒);addressing.md src 核验改 from 核验加 host-only 判例;『开吃/候/强投』俚语清零(delivered 义 = 目标开始处理);差异表幂等行拆(v=1 已落,幂等 id 与 tasks prev 未落)
- **门控尾窗与 CTA 标准化**:门控判据补尾 12 行窗(对话框按钮与页脚区,正文文档引用如信任屏教学文不误判;evo 实弹案 = working 格读 skill 文档整屏扫描假阳性,尾窗后 delivered);CTA 通则补专业标准(『下一步:』前缀与 target= 键值形)
- **触发词自然语化**(fleet seq 44 全单):SKILL description 重写,意图词路由五原语(告诉、委派、让干、找格、读屏、窗格、邻居、tab、工作台、table 走 agents;流、回执、房间、广播走 streams;共享、给文件走 shares;管道、实时发走 pipes;持久任务走 tasks)
- **agent 命名标准(用户三令:名字不乱取,标准形定案,同步总台)**:addressing.md 命名纪律升命名标准,标准形 = `<工作台标签>-<agent类型>-<编号>`;台标签 = 仓别名(agents ws 以仓为单位),类型 = TUI 家族,**编号 = 工作台窗格位序号,名与格一一对应**;工作台默认至多四窗格田字布局顺时针开(TL-TR-BR-BL 即 1 至 4),第五格起自动开新 tab 编号续增;一格一名结构性全局唯一,存量名兼容在役新起一律标准形;AI-LAB 取用行断点(from 无格段,agents to AI-LAB not_found 实测)与机标签不合(AI-LAB 裸 hostname 对在册名 lan-win)入判例与报件
- 实证:本机重装 prim 后本地渲染信封 v2 与 parse_fieldline 双向过;版本线 0.12.0 进 0.12.1;四门禁全绿 + 回执走 streams append fleet + 回信总台(命名标准方案同步,候 CONTRACT 收编)

### 变更 2026-10-13 第一百三十七批:herdr 技能淘汰序与 agent-prim 唯一操作面,总台令（附 R1 三件复核）

- **R1 三件复核收编**(REQ-029;ai-ccoe main 实落 d524d7c,总台令引 9a6856c 仓内未寻得,回执注明):斜杠流名 cursor 崩修(父链全建,`streams view room/deferred/w8:p1 -n 3` 净退 0)、streams 手册补 -n/--lines、mode 动词实装(presence 走 shares 键,`agents mode online` 落键实测);agent-prim 差异表收缩至残余十行(cursor 崩与手册 -n 与 mode 三行撤;layout 挂账行入 = herdr 0.9.3 无 layout 子命令,preview 面),mode 入速查表与保留动词表与协作惯例
- **淘汰序(用户裁:herdr 退役出代理操作面,操作面唯一 = agent-prim)**:herdr-orch 标 deprecated(description 前缀加题下指路条,一条不删只指路,内容留档);evo-herdr README 与双 manifest 与市场条目同步淘汰序;agent-prim 定位与 description 升「代理操作唯一面」,herdr 分工行改「herdr CLI 退役为引擎(同 s5)」
- **裸命令教学节改五原语反射**:agent-rloop(派单门控改 agents to 内置门控 v2 与信封回执、登记簿核对改 agents view、回执收件改 agents read 忙候、跨机路由改机:名一次命中、herdr --skill 活权威改 agents --llms、参考路由)、agent-s5(分工行两处)、agent-rloop references/rounds.md(四处);裁定 = rloop 协议面存续不整 deprecated(其 herdr 操作面已反射化),候总台裁
- 路由面同步:AGENTS 定位段、根 README(定位行与 herdr-orch 及 agent-prim 两行)、docs 地图两行、evo-agent README;顺手修 herdr-orch 与 agent-rloop 既存标题半角括号三处(静检 hook 抓出)
- 版本线 0.11.1 进 0.12.0(淘汰序 = 面级变更;五插件双 manifest、市场清单、五插件 README 发行行);四门禁全绿 + 回执走 streams append fleet

### 变更 2026-10-13 第一百三十六批:agent-prim R0 三反射收编,总台令

- **反射节重铸**(REQ-028;R0 修件 = ai-ccoe main 5f7b48c):SKILL.md 四节改投递与收件反射三律(投递只看 status 与 CTA、收件 agents read 自带忙候与超时、拒投自动代记 deferred);门控 v2 入律 = TUI 实况检测替代状态字段,四家 TUI 判标族(claude/codex/grok/kimi 实测文案),操作对话框拒投、空 TUI 可投、busy 排队不拦,保守清单误拒优于误投
- R0 四件随收:read 隐式收件(忙则内候 5s 轮询到闲/完成或超时,默认 90s,`--timeout` 调,超时出 status timeout-working 内容仍全量附上 exit 0)、agents to 拒投代记补齐(含原文截 80 字)、agents 域动词面补齐(start/ws/shell/dev/split/tab/zoom/keys/trust/sync,layout 与 mode 契约面挂账)、pipes 域铸齐(view/open/close/to,win OpenProcess 活性探测);streams view 接 -n/--lines(批 135 报件之一已收)
- references 同步:commands.md(agents 收件面与工位动词、pipes 铸齐、差异表收缩至 R0 后残余十一行)、deliver-gate.md(门控 v2 判据、代记全域、read 收件信封与 DELIVER 四态分立)、collab.md(-n 调量);description 与 evo-agent README 随改;常见坑重排(streams 拒投不含原文、busy 误区两坑新入,pipes 铸造中坑撤)
- 实证准入:本机 uv 工具重装自 ai-ccoe main 5f7b48c 后实测(read working 格 timeout-working 信封与闲格 idle 信封双态、streams -n、pipes view exit 0、斜杠流名 cursor 崩复测仍在报在案);版本线 0.11.0 进 0.11.1(五插件双 manifest、市场清单、五插件 README 发行行);首稿呈总台,R1 攻击单候

### 变更 2026-10-13 第一百三十五批:agent-prim 升格 prim v3 契约对齐,总台令（发版批）

- **agent-prim 升格**(REQ-027;总台令原名 prim-ops,按仓命名律落位既有 agent-prim 免双份并行维护):契约真源演进至五节加五a/b/c/d(v3.0 蓝图),本机实装 prim 3.0.0a1(python 形 uv 工具)实查对齐;SKILL.md 重铸 = 五域路由、文法与全局七旗标、id 三产生式与例、投递语义(to 统一、--force、门控 deferred、status 四态信封 delivered/engine_fail/deferred/stalled)、隐式路由(local 与 --machine 零感知各端一致)、常见坑六条(裸格须 local: 前缀、streams 尾读 100 行限读、门控拒投走 streams append 记流、斜杠流名 cursor 崩、hst task 正名、pipes 铸造中)
- references 四篇同步:commands.md v3 动词面与输出契约与 3.0.0a1 实装差异表十三行(实证面:pipes 铸造中、ws/mode 族未落、VIEW --json 未落、代记键 pane 形、streams 代记不含原文、force 审计未落、斜杠流名 view cursor 崩等)、addressing.md id 三产生式与隐式路由、deliver-gate.md status 四态与代记两形、collab.md hst task 正名;索引随改;实证准入:所写命令形经本机实测或包源直读标 [实证](自探针:门控 deferred 路径打本机 working 格零扰他格)
- 版本线 0.10.1 进 0.11.0(五插件双 manifest、市场清单、五插件 README 发行行);顺手修批 133 遗漏(市场清单描述十 skill 进十一、evo-lint 两进三、evo-agent 三进四)与批 134 遗漏(REQ 索引缺 REQ-026 行);根 README 与 docs 地图 agent-prim 行随改(to 投递与 status 四态、goal 域正名 task);部署道建议候总台核
- 顺手报总台:prim 3.0.0a1 斜杠流名 view 尾段 cursor 写崩(子目录不建,数据行已全打印退 1 加栈,room/deferred 补收面受累)、--llms 手册列 ws 族动词超出 case 分支(漂移守卫未挂),建议随 prim 下一版收口

### 新增 2026-10-13 第一百三十四批:zh-lint 汇报面吸收,用户令

- **汇报面**(references/reporting.md 新页):ASD-STE100 中文家族实践蒸馏(一案提案 patch 形,否 create 因同域拆分伤意图路由);结构律(结论先行)、状态词十词表(已完成到未确认)、验证状态(方法与命令与输出摘要,六态的回复形)、询问律(选项编号)、语言律增量(情态词只必须不得可以、禁缓冲开头与比喻成语)、五模板(进度、结果、排查结论、请求决定、多项总结)、发前自检八问
- SKILL.md 适用面加工汇报与回执、新增汇报面速览节;description 补触发词(汇报、回执、结论先行、状态词、已验证、未验证、选项、模板);顺手修正标题半角括号漏网(批 131 遗留)
- zh-lint.py 机检面不动(情态近义词与缓冲开头入先验核属工具行为变更,候另批);REQ-026 立档

### 新增 2026-10-13 第一百三十三批:evo-agent 第四技能 agent-prim 五原语,总台令

- **agent-prim**(客户端 evo-agent:agent-prim):舰队互操作五原语操作面;五命令 agents/shares/streams/tasks/pipes 三段式(VIEW 全局可视、OPERATE 只动资源、DELIVER 定向传递带门控),裸名全局寻址与命名纪律,投递门控(working/blocked 拒投、--force 留审计、拒投代记 room/deferred 补收),信封三行形取用行纪律,IM 映射(流即房间、DELIVER 即 @、dm/ 与 room/ 前缀、agents view 即 presence)与回执走 streams append fleet
- 契约单一真源 = ai-ccoe 仓 plugins/CONTRACT.md,skill 只路由不复述;版本对齐 v2.3(2026-10-12 契约化批),本机实装 v2.0.0 差异面六态标注(--json、--llms、幂等 id、v 字段、presence 声明、pipes 跨机 view、tasks prev 未落,references/commands.md 差异表)
- SKILL.md 意图路由 + references 四篇(commands、addressing、deliver-gate、collab)加索引;与 agent-s5 分工定形(s5 引擎命令面,五原语协议面)
- md-ref-scan SKIP 增 CONTRACT.md(舰队契约外指针);版图全同步(五插件十一 skill):测试 SKILLS 守卫、pre-commit 断链段、AGENTS(含修正插件数既笔「共四个」)、根 README、docs 地图、evo-agent README(含补 rloop 段既漏)、REQ 索引;REQ-025 立档
- 回执走 streams append fleet(自吃狗粮);批 132 回执机名误书以新行更正

### 变更 2026-10-12 第一百三十二批:evo-lint hook 段名英文化,总台令

- hook statusMessage「evo-lint 后缀静检」改「evo-lint file-check」(herdr/hst 状态栏段名纯英文裁定,hst 面另单;statusrender 拼接形 evo-lint-{title});lint-hook.py 头注同步;版本线 0.10.0 进 0.10.1(五插件双 manifest、市场清单、五插件 README 当前发行行);守卫测试补段名纯英断言(test_evo_lint_hook_status_message_english)

### 新增 2026-10-12 第一百三十一批:evo-lint 第三技能 zh-lint 简明技术中文静检,用户令

- **zh-lint**(客户端 evo-lint:zh-lint):受控中文写技术文档与 AI 解释性回答,目标 = 读者读一遍就不会读错;判据源 = 简明技术中文规范 0.2(六节四十条 + 词表三张表,上游仓为活权威,CC-BY 4.0)
- 工具 `scripts/zh-lint.py`(PEP 723 零依赖):内置先验核(无条件禁用词与选词,不 vendor 全表)+ `--wordlist` 外接上游词表三张表(自动检查列、编号项内条件)+ 句长机检(操作句 30 描述句 40,汉字 1 英文词数字串 1 行内代码 1 标点不计);只报不改,行内代码不参检;沿 ADR-0022 自研不引依赖判例
- SKILL(适用面、写前分类、六节必须条速览、模式与 md-lint 分工)+ references/stc-rules.md(四十条蒸馏带判例)+ 索引;权威入口指上游规范与词表
- REQ-024 立档;版图五插件十 skill 全同步(双 manifest、市场清单、AGENTS、根 README、docs 地图、pre-commit 十一段断链、测试清单与行为测试)
- 同轮:ai-ccoe 与 hst_rs 双工位同步轮 sync-01 闭环(周知 v0.14.0 版图与信道翻转;自查旧技能名引用:ai-ccoe 零引用、hst_rs 零活引用且 REQ-047 知会闭环确认,双回执落档)

### 新增 2026-10-12 第一百三十批:dev-01 吸收,channels 危险旗标判据入 agent-doctor

- **机制结论**(dev-01,官方文档加本机 2.1.296 二进制实证):`--dangerously-load-development-channels` 为隐藏 CLI 旗标,加载研究预览 channel 服务器(MCP 入站推送)绕过批准允许名单,仅限本地 channel 开发;启动确认框无跳过法;与更新通道、实验 env、disableSideloadFlags 名单均无关;`-p` 与 Agent SDK 忽略;组织关闸 = `channelsEnabled` 保持未设置
- config-face error 族新增两行:**启动参数面**(该旗标出现在 rc、别名、herdr/hst 启动参数、脚本、skill 启动块、settings env 或 hooks 命令即 error;config-lint 现不扫 argv,标手跑判据)与**危险叠用**(舰队格或无人值守启动里与 bypassPermissions 或 --dangerously-skip-permissions 或 yolo 叠用即 error);策略偏好不判原则保持,叠用为例外;未知字段 advisory 面不动(它不是 settings 键)
- channels 机制速览节入 config-face(值形、八道注册门摘要、组织关闸口径,权威指向 channels 两页);舰队落点:五端都不开

### 新增 2026-10-12 第一百二十九批:rloop-02 吸收,s5 窗格登记簿与防漂移时序,总台令追补研究

- **窗格登记簿**落 agent-s5:`board/<工作台>/panes/registry` 一机一册、角色为行键、九字段表(role、machine、workspace_id、pane_id、agent_kind、agent_name、session_id、task_id、heartbeat);只由总台 sweep 覆盖写(整份 put,防多格互冲),与 herdr report-* 互补(那管实时身份,册管角色意图)
- **防漂移五步时序**(注册、查询、核验、漂移恢复、收单)进 naming 与 agent-rloop 派单纪律:按角色取行不按记的 pane 号;核 session(焦点格不参与);缺号或 session 不对重找(同 session 优先、次唯一 name、再次同 workspace 唯一 kind;多个对不上停手候裁);跨机先 --machine 再 list(--current 在远端解析为远端当前格);yolo-heal 重启后强制重写册
- 漂移四成因实证吸收(编号关闭不复用致缺号、agent 名释放复用、--current 与继承 ID 不指远程、TUI 焦点不改命令向);herdr-orch 身份核验升级为「登记册加 list」双源,workstations 补缺号与远端 --current 语义,lane 台账注明不覆盖无名格与缺号
- herdr 与 s5 结合律定形(rloop-02 件 3):herdr 管信号与窗格控制、s5 管内容与登记、hst goal 管目标;防混道(凭证与审批与 pane 控制绝不进 s5,登记簿正文与回执全文绝不进 prompt);REQ-047 四事件与 sweeper 维持候发布口径

### 变更 2026-10-12 第一百二十八批:herdr-flywheel 升格迁出为 evo-agent:agent-rloop,用户令

- **本版破坏性变更预告**:技能 evo-herdr:herdr-flywheel 删除,调用名失效,升格迁出为 **evo-agent:agent-rloop**(目标驱动的多角色循环进化任务);evo-herdr 收单 skill herdr-orch;版图五插件九 skill 不变(doc 2 加 herdr 1 加 distil 1 加 lint 2 加 agent 3)
- agent-rloop 定形(rloop-01 研究吸收):herdr 定多窗格角色后钉一个 hst goal,按轮派单回执断言吸收循环到达成或显式停机;防停双层(轮内 Stop 提醒、轮外 goal heal 静默窗唤醒,候 hst REQ-047 发布批 goal 腿扩四事件双挂);停机条件入协议(达成 clear、人裁 blocked 不 heal、风暴闸、角色数与轮深上限,缺省不无限转);核心判据六条(一项目一 goal、总台委派默认、Stop 主时钟、状态在盘上等)
- 迁移映射(rloop-01 件 1):轮次协议本体(分型、三件套、检查点、干预矩阵、四步、吸收、义务图、派单回执坑)随迁 agent-rloop(SKILL 加 rounds.md 加 parallel.md);工位带起、跨机器路由、信号命令速查、驻场与仓级坑归并 herdr-orch(新增 references/workstations.md);s5 命令面留 agent-s5;flywheel 目录删除
- 指针全翻:orch 路由与 panes/lane/receipt、doc-gov 路由、agent-s5 分工句、fleet-exec 注记;通用原则句落 orch(单 skill 形);AGENTS、根 README、双市场清单、双 manifest 双插件、docs 地图、pre-commit、测试清单全同步;agent-doctor 补 hst REQ-047 候发布注记(goal 腿四事件双挂知会)

### 变更 2026-10-12 第一百二十七批:herdr 飞轮与编排消息信道翻转内置 s5,用户令

- **协议变更通告**:herdr-flywheel 与 herdr-orch 的消息与产物传递不再走本地文档与 prompt 内联,内置 s5(命令面 evo-agent:agent-s5):派单 = 任务内容落 brief 后 put 上键(rounds 键空间),herdr prompt 只递单号、键与一句接单指令;结果获取 = get receipt 键(文本结果)或 tail 轮次流(实时进展);三件套仍为 md 文件稳态,本地临时目录降为底稿写作面
- 跨机细则同步翻转:跨机派单与周知走 s5 键(prompt 递指针),prompt 全文内联降为本机无 s5 二进制时的兜底形(记注);对账判据句改「盘上是权威、s5 是信道、会话只递指针」
- 通用原则句(orch 与 flywheel 同步):md 文件是状态与产物,消息与产物传递内置 s5(发布上键、结果文本或实时流取回);agent-s5 分工句对应更新(herdr 管信号与调度,传递面归 agent-s5)
- 双 manifest、市场清单、AGENTS 全同步;触发词补任务上云、键指针、实时流取回

### 变更 2026-10-12 第一百二十六批:agent-doctor 网关面 [1m] 剥离事实与 overcast 实测回填,总台优化单

- **[1m] 后缀剥离事实入判据**(用户口径加实证:Claude Code 发网关前剥模型名 [1m] 标记,网关 models 列表只有剥离形;raw curl 带后缀 400 unknown provider 不代表配置错,实证 zp-cc-glm53[1m] 400 与剥离形 200):拼接规范节立条,活性层「钉住 id 不在 models 列表」改先剥后缀再比对,错形三注剥后比对,手测验证一律用剥离形
- overcast 回填位两项落实测:models = GET /v1/models?limit=1000(Bearer,200 JSON 六模型),推理 = POST /v1/messages(anthropic 形,Bearer,别名 zp-cc-glm53 回包 model=glm-5.3);health 无鉴权探针仍未知名保留
- 现状两形更新:钉组形 2026-10-12 已部署 lan-mac(发起)、win 面、local-wsl 面(总台镜像)
- 命名族注记:zp-cc-* = Claude Code 专用别名族(用户口径);zp-cx-* 归属待证(owned_by 标 glm 与 xai,勿写死)

### 变更 2026-10-12 第一百二十五批:批 124 合并保真修复,rev-codex 快核 6F

- F1/F2 键空间与纪律保真:naming.md 跨机轮次与研究档键空间节按原 herdr:s5 fleet.md 语义原样重写(rounds 三件套文件名形与发起接收断言三方同步律、research 与 artifacts 带仓名层、streams 分 diary 与 events、流不替代 diary、环 1000 条与 32KB 设计值、同机不上 s5、临时键用毕 del、键空间变更走 REQ);双道三问补 backend 形(garage 与 streamstore,候实测定稿)
- F3:evals 五条三类随迁入 agent-s5/references/evals.md(参考索引同步加行);SKILL 双道行补「候 s5 首版实测定稿,实测偏差以本机 s5 --help 为准回填」标态
- F4:四处「十 skill」陈旧清零(AGENTS 断链行、docs/README、gates.md、tests docstring)
- F5:批 123 与批 124 的 CHANGELOG 条目补落(先前锚点失配静默跳过,本批改锚定批 122 标题插入)
- F6:ADR-0024 立档(herdr:s5 并入 agent-s5 的版图裁定)加索引行
- G 采纳:计数守卫扩总量连写形(任意中文数字插件计数与插件-skill 组合计数须等于实际值);G 不采纳记档:codex 缓存部署漂移属封版滚动既议(版本线不变不刷新),不手清缓存

### 变更 2026-10-12 第一百二十四批:herdr:s5 删除并入 agent-s5,用户裁定

- **本版破坏性变更预告**:技能 evo-herdr:s5(批 111 立)删除,调用名失效;s5 技能面归一为 **evo-agent:agent-s5**,定位 = 所有 agent 共享的看板与实时流,从简(用户令「不要太复杂」);版图回到五插件九 skill
- agent-s5 吸收:定位句与标题改「全局看板与实时流」,herdr:s5 的协议场景触发词收编(上云、三件套上云、轮次档、跨机研究档、对象道、流道、轨迹流、S3、S2、garage、streamstore),分工句简化为「herdr 管信号与消息,共享内容一律走本 skill」
- naming.md 增跨机轮次与研究档键空间节;evo-herdr 收两 skill(orch、flywheel),双 manifest 与 README、AGENTS、根 README、双市场清单、docs 地图、pre-commit、测试清单全同步;flywheel 与 orch 零交叉引用净删无断链;REQ-023 立档;kimi 五端旧 s5 目录退场重镜像

### 变更 2026-10-12 第一百二十三批:herdr:s5 触发词去重叠,用户裁定

- 两 s5 系技能触发词分治:s5 裸词与命令动词(put、get、append、tail、streams)归 evo-agent:agent-s5 独占;evo-herdr:s5 换协议场景触发词「上云」(独占动作 = 三件套上云),连带轮次档、跨机研究档、对象道、流道、轨迹流、garage、streamstore 场景词;description 内交叉引用改述不引裸词,消除路由模糊(该分治后被批 124 归一并取代,留档)

### 变更 2026-10-12 第一百二十二批:CHANGELOG 存量带括号标题 lint 债清理,总台令

- 存量 38 处带括号标题(含全半角混用形)按 md 标题禁括号口径去括号改写,语义原样保留:全尾包裹形剥括号接空格,尾注组形转逗号续写;lint-hook check_md 实证 CHANGELOG 零发现
- 此前批次标题规则与挡板只拦增量不拦存量,本批清完历史面,后续任何 CHANGELOG 编辑不再触发存量噪音


## [0.14.0] - 2026-10-12

版本载体齐 0.9.0。本版无破坏性变更:第五插件 evo-agent(agent-doctor 与 agent-s5 两 skill)新增,md-lint 与 ls-lint 更名(旧名仅在历史档),lint-hook 辖域修复与 config-lint 判据族随线生效;已装者逐插件 update 即可。

### 修复 2026-10-12 第一百二十一批:评审 G 项记档清理批 封版前顺手,总台令

- G-120-1/4:计数守卫重写(排 .venv 与 .pytest_cache、后缀扩 json 与 sh 与 yml、纳入插件-skill 连写组合计数、「三 skill」单用为 herdr 合法表述放行)
- G-120-2:守卫自免改拼接式模式串(不再整文件排除 tests),cn 映射换通用中文数字换算(不再 KeyError 隐患)
- G5:PEVO_CONFIG_LINT_ALLOW 未命中留痕(对齐 check.py SKIP 判例,`豁免未命中: x` note 行)
- G4:kimi 漂移对账口径收窄(目录级 skill 名集对账,文件级漂移不含);G6:lint-hook 异常集对齐 md-guard(ValueError 加 OSError);G7:措辞「辖域限仓内」改「辖域限事件 cwd 子树内」;G-118-3:config-lint kimi hooks 循环缩进归位;G-120-3:形态非法行 hooks 并列拆句
- G2 与 G3 已随批 118/119 落(占位四形文档化、口径统一),本批复核结案;G-118-4 并入 G-120-1 落
- 门禁:37 测试绿、本机 config-lint 0 错 0 警且豁免留痕实证

### 修复 2026-10-12 第一百二十批:评审三轮收尾批 纯文案与守卫,不动行为

- F3r 余账六处计数位清零:docs/README 四插件六 skill 刷五插件十 skill、pyproject 与 evo-lint README 版本线句刷五插件、tests 三处 docstring 与断言消息刷五插件;gates.md 实证注记去计数连写(时为四端后扩五)
- F2r 判据表回填:config-face 增「形态非法」error 行与单面异常兜底说明;agent-doctor SKILL 速览行补「坏形态报形态非法、单面异常兜底不吞其余面」
- 补断言:codex 枚举不可哈希形态测试(类型守卫先于 _safe 兜底命中);活面陈旧插件计数全树守卫(三、两、四插件在非档案活面零残留,序数「第几插件」形放行,守卫首跑自抓两处漏网并清)
- 门禁:37 测试绿、scan 干净、check 12/12(评审方前三轮独立复跑四门禁与我方一致)

### 修复 2026-10-12 第一百一十九批:评审二轮修订 rev-codex 复核 3F 顺手 2G

- **F1r**:codex 面 `_safe` 兜底挂上(上轮缩进锚点未命中静默跳过);三处枚举值不可哈希形态(defaultMode、approval_policy、sandbox_mode 非字符串)防御报形态非法
- **F2r**:键族判据回填 config-face error 表(词边界、大小写不敏感、四占位形)
- **F3r**:余账陈旧计数清零:根 README 钉版行刷 v0.13.1、gates.md 断链行刷五插件十 skill、AGENTS 当前阶段行 struct 补今名注记
- G-118-1 顺手:键族词边界(`MONKEY` 不再误命中,`_KEY` 分隔形仍命中);G-118-2 顺手:`$env:VAR` 占位形放行;G-118-6:s5 装位改「舰队惯例注记,本机 command -v s5 实查为准」并记 wsl 缺位判例;G-118-3 缩进与 G-118-4 守卫覆盖面记档后批
- 门禁:35 测试绿、scan 干净、断链 0、本机 config-lint 0 错 0 警

### 修复 2026-10-12 第一百一十八批:四批评审修订批 rev-codex 快核,3F 9G 1 大面 CONFIRM

- **F1 形态防御(重)**:config-lint 五处坏形态直崩(env 非对象、enabledPlugins 数组、permissions 与 hooks 非对象、grok plugins 非表、codex mcp_servers 数组表)修为逐面类型守卫报「形态非法」error;run() 加 _safe 兜底,单面异常不吞其余面
- **F2 凭证键族(中)**:SECRET_KEY 扩族加大小写不敏感(TOKEN、API_KEY、SECRET、PASSWORD、KEY、CREDENTIAL、BEARER,re.I),占位符放宽 ${VAR}、$VAR、%VAR% 形
- **F3 活面陈旧计数(轻,前批欠账)**:AGENTS 断链段与 Must 的「三插件」刷五插件、当前阶段 v0.12.0 刷 v0.13.1、根 README 三处与钉版段刷五插件与 v0.13.1、测试 docstring 刷十 skill
- G1 顺手:apiKeyHelper 非空即算有凭证(按自家手册修完不再留警);G3 顺手:gateway-face 项目面凭证口径统一并标注 CUSTOM_HEADERS 为人工判据;G8 顺手:ADR-0022 索引行加更名尾注;G9 顺手:gateway-face 去具体 finding 条数并收 hst diagnose agents 一行
- G2 占位符文档化、G4 漂移对账口径、G5 豁免未命中留痕、G6 lint-hook 与 md-guard 异常对齐、G7「限仓内」措辞改「cwd 子树内」:记档后批
- 新守卫:形态防御与键族两测试 + 活面计数守卫(AGENTS 与根 README 的 N 插件 M skill 须等于 SKILLS 实际值);评审方独立复跑四门禁与我已验面一致,批 114 辖域、批 115 更名、三方自洽、批 116 网关面四点 CONFIRM

### 新增 2026-10-12 第一百一十七批:evo-agent 第二技能 agent-s5,总台用户令插队

- **agent-s5**(客户端 evo-agent:agent-s5):工作台 agent 的 s5 全局看板与频道操作面,让所有装了插件族的 agent 都会 s5;文件道(S3 形 put/get/ls/del)当全局文件看板、流道(S2 形 append/tail/streams)当全局流消息频道
- 三节:命令面与活权威(`s5 --llms` 实查不抄命令表;装位 win 的 D:\ohmyenv\s5\s5.exe 与 linux 的 ~/.local/bin/s5;零感知凭据,钥由 config 层吃 agent 永不接触;本机缺位如实报,分发归 omc 与 ark)、命名约定速览、读写规约与消息礼仪(append 落消息 tail 取阅、写者拥有、del 不越权、频道不做请求应答)
- references/naming.md:看板 `board/<工作台>/<主题>/<文件名>` 与频道 `channel/<频道>` 键空间表、跨台规约、双道选型三问、判例簿;与 evo-herdr:s5 分工句(轮次三件套与研究档走 herdr:s5 协议,本 skill 管通用日常读写)
- REQ-022 立档;版图五插件十 skill 全同步(双 manifest、双市场清单、插件 README、AGENTS、根 README、docs 地图、pre-commit 十 skill 断链段、测试清单守卫);门禁全绿加 kimi 五端镜像(市场面随下次封版滚动)

### 新增 2026-10-12 第一百一十六批:cfg-02 研究吸收,网关面定稿与 loop 域权威化

- gateway-face 定稿回填:官方拼接规范(base 源站形无 /v1 无尾斜杠、头种 Bearer 与 x-api-key、官方验证 curl、models 发现与超时重定向语义)、三层判据表(配置对齐 error 与 advisory 分档、连通性、活性)、三网关端点惯例对照(LiteLLM liveliness 与 readiness、new-api 与 one-api /api/status、one-api 无 /v1/messages 与 HTML 控制台回退)、agent 侧四类错形(键组不齐、token 失效、映射漂移、路径双拼);overcast 路径保持不知,实装后套同一三层表
- config-lint 补两条官方形硬判据:base 以 /v1 结尾 error(会拼出 /v1/v1/messages)、base 尾斜杠 advisory;测试对账升 6 错
- goal-loop 的 loop 面权威化(cfg-02 件 2):三套调度域分立(Routines、Desktop、会话内)、idle 才触发与关停即止、7 天到期再触发一次自删、durable 落盘语义(输出 durable 字段为准、resume 恢复边界、符号链接报错)、ScheduleWakeup 夹 60 至 3600 加 stop 语义加 20 分钟兜底、25000 字节 loop.md 截断与 50 条上限
- 研究格 cfg-02 回执收执吸收(四件全过:网关先例、定时域权威、hst --llms 手册面实测 119 条 finding 全 ok、三层分判表);轮闭

### 变更 2026-10-12 第一百一十五批:evo-lint 两 skill 更名 md-lint 与 ls-lint,用户令

- skill `lint` 更名 **md-lint**、`struct` 更名 **ls-lint**(客户端显示 `evo-lint:md-lint` 与 `evo-lint:ls-lint`;目录名与 frontmatter name 同步,旧触发词 struct 保留为泛词、lint 保留为动词触发)
- 本地覆盖件 `.struct-lint.toml` 同步更名 **`.ls-lint.toml`**(rules.md 与模板头注释同步);ADR-0022 与 REQ-020 为历史档保留原名在册
- 双 manifest、双市场清单、插件 README、AGENTS、根 README、docs 地图、pre-commit 断链段、测试清单全同步;门禁全绿(32 测试、check 12、scan 干净、断链 0)
- kimi 安装面五端当场重镜像(旧 lint 与 struct 目录退场);claude/codex/grok 缓存面随下次封版版本线滚动

### 修复 2026-10-12 第一百一十四批:lint-hook 辖域限仓内,用户点报

- 后缀静检 hook 漏了辖域判定,越界检仓外 md(判例:同日拦 `~/.claude` 记忆文件);补事件 cwd 辖域(ADR-0017 同批裁定,与 md-guard 同律):事件带 cwd 且 file_path 在其外时放行,在内照检;realpath 双侧归一,跨盘符 ValueError 放行
- 回归测试 test_lint_hook_scopes_to_event_cwd(仓外放行、仓内照检两态);已装缓存面同版本不自动刷新,修复随下次封版版本线滚动生效

### 新增 2026-10-12 第一百一十三批:第五插件 evo-agent 与 agent-doctor 技能,用户令三轮收敛

- 第五插件 **evo-agent** 单 skill **agent-doctor**(客户端 evo-agent:agent-doctor):四端 agent 客户端环境诊断修复,四面 = 配置诊断修复、hook 诊断修复、goal 与 loop 状态、overcast 网关诊断(候实装框架,现状配置端 lan-mac 钉组形);定位 = 增强 hst doctor 编排补面,hst 只认 PATH 不改其源
- 载体 `skills/agent-doctor/scripts/config-lint.py`(PEP 723 零依赖):四端面(claude settings 两件、codex 与 grok 的 config.toml、kimi config.toml 加 skills 安装面),判据两级 error 与 advisory,只报不改,`--json` 机读,`--kimi-source` 漂移对账,网关键组配对检查;判据分档依据研究档 cfg-01 官方对照:claude 悬空引用是文档容忍态降 advisory、defaultMode 枚举取 doctor 2.1.296 实测集、用户面明文凭证是文档允许形态降 advisory(项目面升 error)、不做闭合白名单(schema 落后索引 45 键)
- error 族:解析失败、枚举非法、绝对路径缺失(kimi 双 OS 形只查当前 OS)、高置信秘密形态(PEM、AWS 键、sk- 令牌)、grok plugins.enabled 悬空(本机判例:卸载不回写配置残留四名)、kimi SKILL.md 形态与漂移;advisory 族:claude enabledPlugins 悬空、用户面明文凭据、未知字段、codex plugins 配置残留候选(wsl 判例三条)、网关键组不齐
- 参考 四篇:config-face(判据表加修复手册加权威入口)、hooks-face(hst doctor 诊断加 hst init 幂等修复加 codex trusted_hash 加 kimi 双 OS 形)、goal-loop(hst goal 四命令与缺省态;loop 归 Claude Code 原生 CronCreate 与 ScheduleWakeup 域,hst loop 已退役)、gateway-face(overcast 三层:配置对齐、连通性、hst diagnose 活性,端点实装后回填);研究格 cfg-01 已收执吸收,cfg-02(网关先例与定时域权威)并行在跑
- 版图五插件九 skill 全同步:双 manifest、双市场清单、插件 README、AGENTS 与根 README、docs 地图、ADR-0023 与 REQ-021 立档、pre-commit 断链段、CI 清单;evo-lint 面上无痕(六面试作全回撤,存量带括号标题三处触及即修);config-lint 行为测试(四端坏配置夹具逐面报、好配置零错零警、豁免与网关配对)加清单守卫;门禁全绿推远端


## [0.13.1] - 2026-10-11

**本版破坏性变更通告**:插件 evo-skills 更名 **evo-distil**、skill native-design 更名 **doc-cli**(旧触发词失效),已装者卸 evo-skills 装 evo-distil,evo-doc 逐插件 update;新插件 **evo-lint** 按需安装(lint 五面静检加写后 hook、struct 类型化结构);evo-herdr 新增第三 skill s5(跨机共享内容,候 s5 首版实测定稿)。live md 禁字 PostToolUse hook 已裁撤(批 105,pre-commit 挡板保留)。版本载体齐 0.8.0。

### 新增 2026-10-11,第一百一十二批:core-02 三方合成吸收,Python uv 范式

- struct python-tool 卡与 types.md Python 仓卡增补:骨架树细节(uv.lock 提交加 --locked、.python-version 钉版、PEP 735 依赖组、lib/commands/types 结构位、任务入口 uv run 不引多运行器)加依赖锁纪律与八条反面清单
- doc-cli 两句:结构律「命令层薄、纯函数域厚、进程 spawn 集中」(tool-cli-agents 新九节)加总律「发现面当测试面养」(agent-face);律 1 注册表单源、律 2 投影四要素、律 5 配置根件、agent 面与技能生态节、守卫清单节均已在册引用即可;不立新 Python 范式页(struct 卡即载体,单一权威源)

### 新增 2026-10-11,第一百一十一批:s5 跨机共享内容技能,用户令 evo-04

- evo-herdr 第三 skill **s5**(客户端 evo-herdr:s5,协同域归一:orch 台面、flywheel 信号、s5 内容):agent 跨机共享内容,文件道(S3 形 put/get/ls/del)加流道(S2 形 append/tail)双道选型三问判据,零感知凭据三不纪律,与 herdr 分工律(信号走 herdr 内容走 s5),跨机轮次三件套与研究档轨迹流键空间规范(rounds/、research/、streams/)
- 全套候 s5 首版实测定稿标注(命令面按 s5-01 立项设计,实测后回填);evals 触发用例集五条三类同步立
- 双 manifest 重写三 skill 描述、市场清单、插件 README、AGENTS、根 README 表、docs 地图、测试清单(evo-herdr 三 skill)、pre-commit(八 skill 断链段)全同步;门禁全绿推远端

### 新增 2026-10-11,第一百一十批:struct 类型化结构标准技能,用户立项 evo-03

- evo-lint 第二 skill **struct**(客户端 evo-lint:struct):四类型标准结构卡(TS CLI 仓、知识三层聚合仓、worker 服务仓、Python 工具仓;数据源四仓实形加当日结构研究)加 templates/ 声明式 toml 规则件四张(meta、required、generated、excluded、config-root、optional 六节)
- 双面:init 脚手架(既有件不动缺件补位,三层类型联动建仓五步)加 check 结构 lint(ls-lint 同族;本地覆盖 .struct-lint.toml,豁免须带因由登记);存量仓不自动施工,出差距清单走该仓蒸馏环(判例:今日五仓)
- 触发用例集 evals 件随技能入库(evo-02 纪律首批适用,五条三类);ADR-0022(挂 evo-lint、声明式自研不引依赖、豁免机制)与 REQ-020 立档;双 manifest、市场、README、AGENTS、docs 地图、测试清单(SKILLS 两 skill)、pre-commit(七 skill 断链段)全同步
- 门禁全绿:pytest 28、check 12/12、scan 干净、断链 0

### 新增 2026-10-11,第一百零九批:研究对照七条采纳落地,evo-01 加 discuss-01 四方共识

- 上游:研究格七条对照(evo-01 分判,零重复对账)加讨论轮共识定案形;采纳六项施工:doc-gov 补按路径加载与 hook 执法句(根文件短路由、领域禁则就近路径规则、硬边界 hook 失败退出);gate.md 谓词 2 升触发用例集(3 至 5 条盖应触发加近失加含糊边界,references/evals.md 随技能入库,两方各跑,隔离会话序贯加含糊独立,fail 映射三行进合取三条不立第四谓词,二值不打均值,采样留判例)加记忆与技能写入边界句(步骤写常驻记忆即绕闸记违规);doc-cli 补 llms.txt 目录索引形(llmstxt.org 规范,索引优先于全文拼接)加 MCP 分流纪律(只暴露活查询,防第二套无闸门通道);layers.md 补 evals.md 允许位加 version 纪律定案(顶层恒禁,字节拷贝分发形豁免 metadata.version 登记在册,比对义务上游代或哈希二选一,校验器豁免形认一键顶层即红)
- 领走判定与回流候选在 evo-01 回执在册(条 6 机检 ai-ccoe 先自落试跑成熟回流 evo-lint,共识 2)

### 新增 2026-10-11,第一百零八批:evo-lint 插件立项

- 用户令:增第四插件 **evo-lint**(项目静态检查报错),单 skill lint 五面:skill markdown 格式标准(frontmatter 官方字段、name 同目录名、description 形态与上限、行数上限、断链)、agents 与 claude markdown 长度限制(缺省 200 与 50 行,环境变量可裁)与结构合同与禁字、rs(cargo fmt 与 clippy 与 missing_docs)、py(ruff 含 D 系)、ts(tsc 与 eslint);references 三篇(md-faces、lang-checks、hook-face)
- **写后自动静检 hook**(用户裁):PostToolUse 按 .md/.rs/.py/.ts 后缀分派快检查,报错信息回传(退出码 2 加 stderr 逐条);Claude Code 直查、Codex apply_patch 宽容放行靠 pre-commit 兜底,hooks.json 花括号变量加 commandWindows 双形;工具缺位放行,重检查进门禁与 CI
- 市场登记双清单、AGENTS 与双 README 与 docs 地图四插件六 skill 同步;测试三件(hook 载荷宽容、md 报错回传、花括号形态)加清单一致性;pre-commit 断链段扩六 skill;版本线同 0.7.0 入列

### 变更 2026-10-11,第一百零七批:native-design 更名 doc-cli

- 用户令:evo-doc 内 skill native-design 更名 **doc-cli**(目录 git mv 保史、frontmatter name、AGENTS 与根与插件 README、docs 地图、doc-gov 意图路由与索引互引、双 manifest 与市场描述、测试清单、pre-commit 路径全同步);**破坏性**:下次封版起客户端显示改 `evo-doc:doc-cli`,旧触发词失效

### 变更 2026-10-11,第一百零六批:evo-skills 更名 evo-distil

- 用户令:插件 evo-skills 更名 **evo-distil**(目录 git mv 保史、双 manifest name、双市场清单、AGENTS 与双 README 与 docs 地图、doc-gov 互引五处、测试清单与 pre-commit 路径全同步);**破坏性**:下次封版起消费者卸 evo-skills 装 evo-distil,客户端显示改 `evo-distil:distil-skill`
- 顺修:evo-doc codex 面 longDescription 里已过时的 live hook 描述句改为 pre-commit 挡板口径(批 105 残句)

### 移除 2026-10-10,第一百零五批:live 禁字 hook 裁撤

- 用户令:删除 evo-doc 的 live md 禁字门禁 hook;插件 hooks/hooks.json 与仓 .claude/settings.json 两处 PostToolUse 注册撤除(当日实时拦编辑四犯、下游仓自有豁免面三度误拦,成本大于价值);md-guard.py 脚本保留(githooks pre-commit --staged 挡板仍用),禁字纪律不丢(挡板加 check.py PE-11)
- 测试翻转:test_hook_wiring 挂接回归改 test_live_md_hook_stays_removed(裁撤不回潮守卫);md-guard 脚本行为用例保留
- ROADMAP「md-guard 按仓豁免配置」积压项随 live hook 消失而失效,收口

### 新增 2026-10-10,第一百零四批:clean-chrome 入列与迁移引用面吸收

- clean-chrome 入列第五实践仓;distil-05 反馈单回执断言过(六坑四提案两优标回流,四件全过,门禁实跑 PASS 12)
- 吸收六项:layers.md 迁移引用面清单(入口合同、地图、门禁断言、裁定红线,rg 清零为验)、字母表跨仓前缀撞义按语义归族、模式页约束升格附则(坑二犯起配机器约束进门禁,优标回流)、资格指针内联实证最小范本(优标回流);gate.md 重门禁不适用例扩列(整树/多平台编译、跨仓验收门,代理面满足);trajectories.md 存量日记旧形豁免句
- con-05 施工单派发(单仓纪律形裁定、迁移预备、diary 新篇标准四节、M 号坑表升格模式页、防重提与流水空态、首技能候选)

## [0.13.0] - 2026-10-10

**本版无破坏性变更**:三插件五 skill 内容增强与下游布局适配,已装各端逐插件 update 至 0.7.0 即可;md 禁字与骨架门禁面不变。

### 新增 2026-10-10,第一百零三批:四仓终验齐与触发对收窄环回流

- ark_rs con-04 加 A1 人裁收口终验过(六件全过;首技能 ark-catalog-addition 受裁入集,触发对三例隔离环境实证);四实践仓治理终态齐
- 回流两笔:gate.md 触发对补初测误触发收窄复测环(第四仓首环判例:近失负例揭出触发面过宽,收窄 description 与 When NOT to Apply 复测转绿);herdr-flywheel pitfalls 增 JSON 键名 status 误取条(总台管道二犯升格,键名 agent_status,门控与派单分开发)

### 新增 2026-10-10,第一百零二批:ark_rs 入列与既有仓迁移形吸收

- ark_rs 入列第四实践仓(Rust 工具链仓,ark-rs 工位 w36:p1);distil-04 反馈单回执断言过(五坑三提案三优标回流候选,四件全过)
- 吸收六项:layers.md 建仓五步补既有仓迁移形(映射注记、git mv 保史、判例指针、首轮豁免援引、ignore 划界)、字母表补退役编号留档注记句;gate.md 谓词 1 补门禁清单固定成文句(优标回流);base-code-doc 补根检索面漂移守卫句;backends.md 补 .claude 整体 ignore 划界句;trajectories.md 补双层裁定账口径(冻结索引账加 ADR 分治,优标回流)
- con-04 施工单派发(归档统一加三层建,走 pve 判例路径:requirements 改 req、guide 升 G 入 operations、proven 启用、防重提与流水空态、首轮蒸馏试点)

### 新增 2026-10-10,第一百零一批:四仓三层聚合标准合流

- 用户立单(2026-10-10,八条裁定递进):sources 与 doc-gov 统一、四仓一致修成一个标准、优标实践回流改标准、ai-ccoe 目录正名、归档统一、doc-gov 对齐 Rust 治理、代码即文档三语言、三层项目级自持;经三实践仓反馈轮(distil-01/02/03,16 坑 10 提案断言吻合)、讨论轮(三仓全可进定稿,13 处改法采纳)、grok-01 业界对照轮(八例信源可回查,WikiSkill 排序:分叉第一、agentskills 触发面第二、Voyager 负对照第三),草案 v2 冻结(条文 13、修订清单 22、终态判据 6)
- **ADR-0021** 立档:sources 扩为唯一出处层(三类出处分根收口,relation 两根词资格判据,否证走 supersede);git 边界三选一(分仓、分目录分 git、单仓纪律形两操作件,排除记忆库内嵌技能形);归档统一字母表八元组(ADR/REQ/R/G/M/P/S/diary 定死归层,Diataxis 判据 G 只收 how-to);doc-gov 工件归层与互指;operations 收标准技能与 how-to 手册两类,技能安装路径是加载视图(常驻面仅 name 与 description);闸门证据形态扩(门禁集轮首点名、hook 拦截入证据、隔离轮判据、触发对,不引 pass rate);取样窗口非保留期;CoALA 映射注;业界负对照排除五项
- **distil-skill 文本改**:layers.md 重构(唯一出处层、CoALA 映射、frontmatter 样例块与 relation 词表含 supersedes、operations 标准面层含页头闸门记录段与回指、工件包拆层、加载视图、git 协议两层时点拆明、建仓五步挂三选一与字母表);loop.md(台账归一、取样窗口与保留期互指、单会话换帽);gate.md(门禁集轮首点名、证据形态扩含 hook 证据与隔离轮判据与触发对、标准面与 .claude 本机态混居边界);SKILL.md 核心思想与硬规则速览同步
- **doc-gov 文本改**:SKILL 意图路由挂归档字母表互指,ADR/REQ 节归层句(knowledge 页型,不换 MADR 全模板),研究档案节归层句(页在 knowledge/research、原档 sources/external);base-adr 补录指引(date 取原始裁定日);base-code-doc 新增代码即文档三语言形态表(Rust aidoc 形、TS 类型契约投影加行为契约、Python docstring 加 ruff D 加三面同源投影)
- **三仓施工单**(con-01/02/03):ai-ccoe 正名五动作已交(@019542f,graph 103/121,ADR-0006;断言五过一打回后重证);browse_rs 三层从零建与 pve-harness 归档统一加 Python 代码即文档在飞;REQ-019 登记,S015 研究档案落档

## [0.12.0] - 2026-10-10

**本版破坏性变更通告**:herdr-dev 更名 herdr-orch(功能不变),doc-gov 知识面重划(COE 三层聚合与日记轨迹迁 `evo-skills:distil-skill`,agent 原生面迁 `evo-doc:native-design`),旧触发词失效。已装 evo-doc 与 evo-herdr 者逐插件 update 至 0.6.0;新插件 evo-skills 按需安装(`evo-skills@project-evo`);Kimi 手拷者删旧 skill 目录(含 herdr-dev)重拷三插件五 skill;各端旧版本缓存目录(0.5.x)可整目录删除。

### 新增 2026-10-10,第一百批:三插件五 skill 版图与 distil-skill 技能自进化

- 用户立单(2026-10-10):与 grok 邻格对照研究 wikiskill(走产物契约协议研究轮 wiki-01,S014)后,把 doc-gov 的三层聚合剥离,立第三插件 evo-skills 承载新技能 distil-skill:项目基于自身执行经验自动产生并迭代项目级标准 skill,支持 Claude Code 与 Codex 双端。裁定三层定义:**sources = 带时间的历史轨迹总结,knowledge = 带版本的双向链接关联结构化知识,operations = 产物为双端支持的标准项目级 SKILL**;合取闸门(门禁无回归、点名义务翻转、知识链接成立)替均值闸,no_action 合法出口,知识层永不回滚、标准层拒绝即回滚
- **evo-skills 插件**落地(双 manifest、README、四端安装面);distil-skill 含 SKILL 与 references 五篇(layers、trajectories、loop、gate、backends);双端命令面以本机 --help 实查为准(实证 claude 与 codex 参数面)
- **doc-gov 三向拆分**:base-coe 删(知识升级进 distil-skill layers)、base-diary 迁为 trajectories(日记即轨迹总结,归 sources 层)、agent-face 与 tool-cli-agents 与 templates 三篇迁入新 skill **native-design**(evo-doc 第二 skill);doc-gov 聚焦 ADR/REQ、代码 doc 注释契约(新立 base-code-doc)、文档即代码、研究档案、工具链范式,references 9 篇收 5 篇
- **herdr-dev 更名 herdr-orch**(定位:主开发台初始各工作角色邻居窗格并开始配合工作,功能不变),herdr-flywheel 收准跨仓库跨项目跨机器交流;两 skill 通用原则入条文:herdr 态是检测信号,md 文件是状态与产物
- **评审与吸收**:wiki-02 评审轮(grok)三处建议全收(SKILL 篇数计数、layers 知识页 FIX 收口、backends 未实证旗标删改);wiki-03 全库业界对照评估轮(agentskills spec、Anthropic 写作实践、双市场惯例、agents.md、MADR、Diátaxis;必改二:Codex defaultPrompt 废名与 AGENTS Must 两插件残句;应改三:正斜杠路径、diary 地图归位、跨 skill 相对引用可达,md-ref-scan 扩 ../ 解析;可选四含补 evo-skills README 与市场顶层 description);蒸馏环最小实测走通(确认选择屏坑蒸馏成 pitfalls 条目,合取闸门核验)
- **无头模式三档与四端**:有人值守、无头边界内、全开 yolo(仅外部隔离环境)入 backends;wiki-04 四端研究轮(claude、codex、grok、kimi)给出各端无头边界内推荐形逐旗标实查;kimi 无沙箱无对等档,`-p` 按全开处置;生成维护 SKILL 的环默认无头边界内,接受与发布停人裁
- ADR-0020 立档登记;S014 研究档案落档登记;REQ-018 登记;测试清单与 pre-commit 扩三插件五 skill;版本线统一 **0.6.0**(三插件双 manifest、双市场清单、三 README)

### 新增 2026-10-10,第九十九批:herdr-flywheel 产物契约与共享文件

- 用户立单(2026-10-10):跨窗格飞轮对话产物落临时目录统一标准路径 md 文件共享,任务与委托型交流由提示词生成文件产物、验收按文件对账达成一致;裁定**发起方不限总台**(任何窗格 agent 可发起委托与同步)与**盘上稳态加 herdr 干预信号分治**(状态与产物由 agent 自己写盘,herdr 生命周期态只作干预检查信号,不是稳态)
- SKILL.md 落「交流分型与产物契约」节(任务、委托、同步三型文件化,讨论型不文件化;三件套 brief/state/receipt;门控用信号、判定用稳态),派单、回执、断言、吸收四节同步条文,description 触发词补产物契约面
- references 落 artifacts.md(统一标准路径、交流分型判据、三件套模板、状态档四检查点、干预矩阵、跨机细则、与官方仅兜底口径的分野;2 篇至 3 篇);pitfalls 两坑修法(done 假象、备用屏读不全)与 parallel 条件归约挂接同步;md-ref-scan 示意名跳过表补三件套名
- 邻居窗格回归实测全链走通(flywheel-01 委托轮:brief 原子写、kimi 验证工位三检查点状态档、receipt 逐件对账带行号证据、会话只回路径加摘要;prompt --wait 提交即返场景实证信号与稳态分治)
- 版本载体 0.5.2 升 **0.5.3**(两插件同线齐平;批 97 内容分发版本载体纪律),双 manifest 加市场清单加两插件 README 一致;REQ-017 登记;门禁全绿(pytest 26 用例、md-ref-scan、check、scan)

## [0.11.2] - 2026-10-09

### 新增 2026-10-09,第九十八批:doc-gov 四形态定形与工具链范式

- 用户立单(2026-10-09):doc-gov 增「纯项目记录」研究档案形态(参考两家族仓实践),定形四文档形态(COE 三层聚合双链、项目日记、研究、ADR);另扫本机各仓 uv 与 python 工具形态形成标准范式入知识库;裁定**不同项目用不同文档结构治理,只有合适的、没有硬性**(形态是选型菜单,核心思想句同步)
- **S013 档案**:三仓研究形态公因式(S 编号一题一篇、引块元信息、六态结论、对照分流、编号互链不超链)与十仓工具链范式核心,信源点名止于档案;顺带修索引漂移:S011 与 S012 补登 research README
- references 落 base-research.md 与 tool-project-kit.md 两篇(7 篇至 9 篇);SKILL 意图路由、形态速览、description 同步;AGENTS.md 定位行、docs/README.md 地图、evo-doc README 同步
- 版本载体 0.5.1 升 **0.5.2**(两插件同线齐平;批 97 内容分发版本载体纪律),双 manifest 加市场清单加两插件 README 一致;REQ-016 登记;门禁全绿(pytest 26 用例、md-ref-scan、check、scan)

## [0.11.1] - 2026-10-08

### 变更 2026-10-08,第九十七批:内容分发版本载体 0.5.1

- 用户立单(2026-10-08):更新安装。批 95 两坑落在 herdr-flywheel 插件面而版本未升(违反批 83 起内容分发版本载体纪律,版本不变消费者缓存不刷),本批补正:两插件版本线 0.5.0 齐 **0.5.1**(evo-herdr 载 pitfalls 两坑,evo-herdr 与 evo-doc 同版本线齐平),tag v0.11.1 加 Release
- 携带内容:第九十五批(pitfalls 冷启动竞态吞派单加 prompt --wait 提交即返)、第九十六批(fleet-exec 重评估,仓面非插件面)
- 升级:`/plugin marketplace update project-evo` 后 `/plugin update evo-doc@project-evo` 与 `/plugin update evo-herdr@project-evo`;Codex 同形

### 变更 2026-10-08,第九十六批:herdr 集成 py 脚本重评估,总台运维面翻转

- 用户立单(2026-10-08):重评估批 90 待定行。触发审计:S011 原写触发(lane 探针/扫描循环手拼二犯)未 fired(lane 无实跑);但 v0.11.0 舰队清理与安装轮中普通进程通道(send-text 加 enter 加 wait-output 收标加 read 回执)手拼十余次、四种任务形,仓级沉淀铁律在总台运维面成立(REQ-015)
- **结论部分翻转**:新增本仓 `.tools/fleet-exec.py` 运维薄封装(参数 machine 加 pane 加 cmd 加 marker,四步通道逐条回显 herdr 命令,活权威语义不藏;未收标不证失败仍打印实读);实证准入 = pi-server shell 格端到端实跑(收标命中,回执含 hostname,exit 0);test_fleet_exec_tool 入套件,.tools/README 登记
- **不动面**:herdr 插件面维持纯知识(ADR-0018);lane 探针与扫描循环的触发条件保留(lane 实跑二犯再议);kimi 委派驱动仍待专项研究;ROADMAP 待定行翻转为已完成

### 新增 2026-10-08,第九十五批:pitfalls 两坑吸收回写

- 吸收单(pve-harness 总台实踩,2026-10-07/08 双工位评审轮,herdr 会话内):herdr-flywheel references/pitfalls.md 派单与回执面收两坑
- **冷启动竞态吞派单**:agent start 检测就绪不等于 CLI 输入面就绪,欢迎屏渲染期键入被吞(双工位 grok 与 kimi 齐报 stalled,实读欢迎屏占屏输入框空);修法 = 驻场后实读稳态再派,stalled 后实读判送达、确认空且无在跑轮才重发
- **prompt --wait 提交即返**:根因 [推断] 收束判定现态命中与轮次启动竞态;按吸收单令对实现核实:活权威 herdr --skill(0.9.1)条文称带 5 秒活动闸门,本机热会话探针未复现(2.6 秒正常等收束终态 done,state_change_seq 228 至 580),冷启动慢起 agent 高危;修法 = 两段式(开工探针短超时加独立收束 wait),超时不证未送达

## [0.11.0] - 2026-10-07

### 变更 2026-10-07,第九十四批:封版 v0.11.0

- 用户立单(2026-10-07):封版。两插件版本线 0.4.3 齐 **0.5.0**(evo-doc 与 evo-herdr 双 manifest 加市场条目加两插件 README 当前发布行);tag v0.11.0 加 GitHub Release;README 钉版行刷 v0.11.0
- **本版破坏性变更通告**:evo-research、evo-codesec、evo-adr 三插件下线(ADR-0016/0017/0018),已装者卸载(`/plugin uninstall evo-adr@project-evo` 等三件)后按需装 `evo-doc@project-evo`;evo-adr 改名 evo-doc,herdr-review 并入 herdr-dev(ADR-0019);装 evo-doc 即得插件级 md 禁字挡板(限仓内 md)
- 升级:`/plugin marketplace update project-evo` 后 `/plugin update evo-herdr@project-evo`、`/plugin install evo-doc@project-evo`;旧缓存目录(`cache/project-evo/` 下 evo-adr、evo-research、evo-codesec 与 0.4.x 版本目录)可整删

### 变更 2026-10-07,第九十三批:挂接面回归测试补强

- 用户立单(2026-10-07):大批挪移后没有回归测试。核实缺口在挂接面(脚本行为与清单一致性已有用例),REQ-014 补三用例
- **test_hook_wiring_points_to_plugin_scripts**:hooks.json 双面命令须含插件级 `scripts/md-guard.py` 路径(花括号 token 守卫不锁路径,解耦回退不红);仓 settings.json hook 须指 plugins/evo-doc/scripts/md-guard.py 加 $CLAUDE_PROJECT_DIR 前缀(批 89 挪移期间该 hook 断过,当时无红灯)
- **test_pre_commit_matches_current_skills**:pre-commit 断链段恰等于当前 SKILLS 展开清单且引用目录存在(批 81 删 skill 后 CI 悬空漏改同类)
- **test_ci_workflow_refs_exist**:test.yml 引用的仓内 .py 与 .json 路径存在性全查
- 全套 25 用例绿(pytest 22 加 3)

### 变更 2026-10-07,第九十二批:跨机器 machine 原语语义补强

- 用户立单(2026-10-07):跨仓之外再研究跨机器,herdr 现有 machine 原语;按活权威 `herdr --skill`(本机 0.9.1)直读补强
- herdr-flywheel 跨机器工位节补六面:ID 与 live 名都 scoped 单机(同名 agent 可并存两机)、TUI 选机不重定命令向(无 --machine 恒走本地语境)、selector 语义(enabled profile ID 或唯一 label,非任意 SSH 主机名;--machine 不与 --session 加 --remote 组合;add 默认远端默认会话)、转发前提与边界(双侧支持 machine API 转发、远端 server 已在跑且 API 兼容;不装不起不重启不回落;本地配置、会话管理、安装命令、交互附着不转发;远端 worktree 路径绝对或 ~ 起)、连接失败不证未应用(重试前查远端实态)、machine list 是 profile 清册非 pane 清单
- 同步面:REQ-013、AGENTS 阶段行;六态标注 [实证: herdr 0.9.1 --skill 直读]

### 变更 2026-10-07,第九十一批:herdr 双模式定形

- 用户立单(2026-10-07):herdr 应是两个 skill:开发模式(已包含 review 窗格)与跨仓模式(不同仓库 agent 工作台对话交流);ADR-0019 与 REQ-012 落地
- **herdr-dev 开发模式**:herdr-review 整目录改名重组,SKILL 重写四主线(窗格布局定式:通用四窗格与 PI 五窗格;评审闸门:请求到放行与两规模;自省验收:清单式实测;任务分发 lane 模型),references 收五篇(request、receipt、findings、panes、lane-dispatch 移入)
- **herdr-flywheel 跨仓模式**:去布局与 lane 两节,收敛为不同仓库 agent 工作台对话交流(工位形态与多 kind 带起、跨机器工位、四步协议、并行义务图、命令面与坑),开发面内容指针到 herdr-dev
- 同步面:双 manifest 与市场条目双模式化(codex interface 与 defaultPrompt 同步)、守卫 SKILLS、pre-commit 断链段、AGENTS 定位与阶段行、根 README 表、docs 地图;版本线 0.4.3 不动待打版批

### 变更 2026-10-07,第九十批:herdr 委派与窗格布局轻吸收

- 用户立单(2026-10-07,两单):吸收蒸馏 herdr-dispatch 任务分发编排改进 herdr skill,评估 grok、kimi、codex 委派与窗格布局是否开发集成 py 脚本;吸收 PI 智能体五窗格开发布局(用户裁定:五窗格仅 PI 开发模式,通用四窗格足够,自省位可由 codex 替代)
- **S011 档案**:herdr-dispatch 对照分流(编排三分工、lane 模型、状态台账、探针契约、身份核验、多 agent 启动特化);kimi 委派上游无参照待专项研究;py 脚本评估结论 = 不开发(纯 skill 加内联探针够用、沉淀铁律未触发、活权威 herdr --skill、与纯知识加 hook 解耦方向相反)
- **S012 档案**:窗格布局定式对照(通用四窗格:主开发、研究、review、自省回归;PI 五窗格:pi 自省加副窗实战验收;双闸门收批、先推后审、会话纪律、重载铁律、TUI 就绪探测)
- **herdr-flywheel 吸收**:新增「窗格布局定式与双闸门」与「任务分发 lane 模型」两节;新篇 references/lane-dispatch.md(lane 结构、状态台账与探针契约、身份核验、codex 与 grok 启动特化、发布纪律);pitfalls.md 增三坑(agent 名回收复用、done 假象多源、TUI 未就绪悬输入框);frontmatter 触发词加窗格布局、lane、worktree、codex、grok、kimi
- 同步面:docs 地图加 S011 与 S012 行、REQ-011、ROADMAP(py 脚本重评估条件记待定行);等价桶不吸收项(JSON 判据、勿动非自建、租约防重发等,与既有口径同源互证)

### 变更 2026-10-07,第八十九批:doc-gov 三合一与 evo-doc 改名,skill 与 hook 解耦

- 用户立单(2026-10-07,整理重构批五令):doc-gov 加 code-kit 加 cli-docs 三 skill 合一为 doc-gov;evo-adr 改名 evo-doc;插件内 skill 与 hook 解耦;code-kit 工具面只带 md-guard 的 hook(init/check/scan 与模板移本仓 .tools,斜杠命令删除);知识面收敛:文档结构只有 ADR(需求决策)与 COE(三层聚合和双向链接图)两种形态,补项目日记(ADR 之外增强),留 Agent 友好 CLI 架构标准,其余复杂面不需要(ADR-0018,REQ-010)
- **结构挪移**:`plugins/evo-adr` 改名 `plugins/evo-doc`;md-guard.py 与 mdrules.py 上移插件级 `scripts/`(hooks.json 与仓 settings.json 指新路径,skill 目录纯知识);init/check/scan 移 `.tools/`(check 与 scan 经插件路径 import mdrules,三面同源单源);骨架模板移 `.tools/templates/`;verification 用例移 `.tools/verification/`;commands/ 斜杠命令三件删除
- **知识面收敛(references 20 篇收敛 7 篇)**:留 base-adr、base-req、agent-face、tool-cli-agents、templates;新写 base-diary(项目日记形态:一天一篇活轨迹、裁定与坑留痕、择要升格、ADR 之外的增强面)与 base-coe(COE 形态:sources 加 knowledge 加 operations 三层单向支撑、[[双链]]与 _index 图、指挥总纲路由、建仓五步,双 COE 操作台仓实践提炼);移除投影纪律、三栈工程合同、测试分层、封版流程、经验篇、平台矩阵等 15 篇(git 历史可恢复)
- 同步面:双市场清单与 evo-doc 双 manifest 同笔单 skill 化;守卫测试(PLUGIN_NAMES/SKILLS/工具断言/md-guard 与 mdrules 路径)与 test_repo_md_clean、CI smoke、pre-commit、gates、AGENTS、根 README、docs 地图、.tools/README 全刷齐「两插件三 skill」;SKILL 意图路由与形态速览按三形态重写
- 市场破坏性变更通告:evo-adr 改名 evo-doc,已装者卸载 `/plugin uninstall evo-adr@project-evo` 后装 `evo-doc@project-evo`;版本线 0.4.3 不动,统一打版随后批

### 移除 2026-10-07,第八十八批:evo-codesec 插件下线与 md 挡板限仓内

- 用户立单(2026-10-07,同日两令):先移除 evo-codesec 的 secret-scan 密钥深扫 skill,再下线 evo-codesec 整插件(security-audit 一并移除,ADR-0017,REQ-009),三插件七 skill 收敛两插件五 skill(evo-adr 三 skill、evo-herdr 两 skill);版本线 0.4.3 不动,统一打版仍留待整理重构批
- 删除面:`plugins/evo-codesec/` 整插件(secret-scan 与 security-audit 双 skill、双 manifest、README、secret-scan-cli 斜杠命令);tests/test_secret_scan.py 整文件退役;浅扫(工作区加 git 全历史加敏感文件)仍在 code-kit scan,失去面为 GitHub alerts 与 code search、裸克隆深历史与 PII 加 Cloudflare 译本安全审计,node 运行时依赖面随退
- 同步面:双市场清单去 evo-codesec 条目;守卫 PLUGIN_NAMES/SKILLS 与断言、pre-commit 断链段余五;doc-gov 与 code-kit 互引改指 code-kit scan;gates 豁免正则与 AGENTS 豁免注去 secret-scan 夹具;计数刷齐「两插件五 skill」
- **md 挡板限仓内 md(用户令:md 插件与扫描只针对仓内 md 文档)**:核实 md 规则五面(hook、--staged、scan、PE-11、md-ref-scan)已全部只认 .md 无需改;md-guard hook 面事件带 cwd 时 file_path 须在 cwd 项目内才检(仓外 md 如意向 plan 放行),无 cwd 载荷保持宽容不回退,--staged 面不变;新增 cwd 辖域用例
- 市场破坏性变更通告:evo-codesec 已装消费者执行 `/plugin uninstall evo-codesec@project-evo`,缓存目录可整删(正式通告随后续打版批)

### 移除 2026-10-07,第八十七批:gh-issue 与 build-release 与 evo-research 移除

- 用户立单(2026-10-07):移除 evo-adr 的 gh-issue 与 build-release 两 skill,下线 evo-research 整插件(唯一 skill research),四插件十 skill 收敛为三插件七 skill(ADR-0016,REQ-008);版本线 0.4.3 不动,统一打版留待整理重构批(用户裁定)
- 同步面全改:双市场清单(evo-research 条目删除、evo-adr 描述去两句)与 evo-adr 双 manifest(codex 面 interface 与 defaultPrompt 同步);守卫测试 PLUGIN_NAMES/SKILLS 与计数;幸存 skill 互引(doc-gov SKILL 与 flow-release 与 flow-archive 与 references 索引、cli-docs、code-kit 三 references)不留死链;pre-commit 断链段余七;AGENTS 与根 README 与 docs 地图与 gates 计数刷齐(顺手修 AGENTS Commands 与 docs 地图两处既有「十一 skill」漂移)
- 用户令:readme 类文档不带历史轨迹描述(根 README 迁移段叙事收敛为现行指引,evo-research 卸载通告只落本 CHANGELOG,与 skill 正文零历史轨迹同口径)
- 顺手修复:CI smoke test.yml 悬空 report 行(第八十一批漏改,现状即红)删除;ROADMAP moot 的「report 渲染字体族参数化」待定行删除;根 README 外部命令清单清 bh/typst/aria2c 陈货
- 市场破坏性变更通告:evo-research 已装消费者执行 `/plugin uninstall evo-research@project-evo`,缓存目录可整删(正式通告随后续打版批)

### 变更 2026-10-02,第八十六批:herdr-review 对话状态门控与事件驱动收件

- 用户立单(2026-10-02):herdr-review 的对话状态判断方式参考飞轮第八十五批同款改进(状态门控、事件驱动、超时兜底)
- **panes.md 对话配方升级**:第二节 4 从「prompt 加 read」两步升四步(agent get 状态门控五路分派、prompt --wait 提交与等待同一请求、agent wait 收束事件兜底(插队单与补等形)、read 备读回执);已有格分派行补 unknown 走 explain;篇头实证注收敛为无年代形(用户令:skill 内容不带历史轨迹)
- **SKILL 命令面与路由**:命令块加 agent get 门控与 agent wait 收件两形(本会话实跑准入,沿飞轮实证记录);正文补「对话状态门控与事件驱动收执同 herdr-flywheel 四步协议口径」衔接句;意图路由加「判评审格忙闲、等评审收束回执」行;frontmatter 涵盖句与触发词同步
- **receipt.md 收件纪律挂机制**:「评审会话 idle 才收件」升为「收件以收束事件为准,wait 返回后再 read(idle 与 done 皆可收;blocked 问用户;超时处置同飞轮回执节)」
- 同步面:双 manifest 与市场条目 description 三处逐字同(herdr-review 括号加对话状态门控与事件驱动收件)、codex 长描述、evo-herdr README、docs 地图 herdr-review 行;版本线四插件 0.4.2 齐 0.4.3

### 变更 2026-10-02,第八十五批:herdr 飞轮跨工作台状态门控与事件驱动收执

- 用户立单(2026-10-02):飞轮方法没判 agent 状态做事件驱动;裁定跨工作台对话 = 状态判断、事件驱动、超时兜底(与 tmux 无关,是 herdr 的 agent 状态判断)
- **SKILL 四步协议升级**:派单步加状态门控前置(`herdr agent get` 判 agent_status:idle 与 done 直派,working 先 `agent wait --until idle --until done --until blocked --timeout <租约余量>` 排队候位或插队,blocked 问用户,unknown 走 `agent explain` 排查);回执步加事件驱动收执主通道(`agent wait` 等 settle 事件后 `agent read` 收回执,插队单与补等走独立 wait,替代人工记挂与轮询清册)与超时兜底纪律(必带 timeout 禁裸等,超时 exit 1 加 timeout 错误 JSON,处置 = get 判现态加 read 判送达,确认前不重发,连续超时即失联判据走改派)
- **机制挂接**:跨机器节命令路由补 wait 同形跨机;并行租约纪律挂机制(时限即收执 wait 超时上限,心跳判据 = 连续超时加无回执无 commit,parallel.md 租约节与映射表同步);pitfalls「--wait 撞已决态」修法句升级(派发后轮询 agent list 甄别真开工改 `agent get` 判 working)
- **实证准入(ADR-0010,本机 herdr 0.9.1 实跑后写入)**:agent get 五态与 state_change_seq、agent wait 现态电平命中即返 exit 0、超时形 exit 1 加 `{"error":{"code":"timeout"}}`、`--until` 重复旗标形(逗号串报 invalid agent status)、working 电平命中、agent explain 出 rule 加 evidence、`--machine` 路由
- **官方语义追正(用户令,原批内)**:语义以官方 Agent automation 与 Socket API 为准(X 编排经验只标坑)。prompt --wait = 提交与等待同一请求避空窗,自带 5 秒活动闸门(agent_prompt_stalled),已 working 工位在跑轮收束即满足;开工探针形(`wait --until working`,已在跑即返,探针超时不证未送达);错误通道口径(stderr、超时与服务器错退出码 1、语法错 2、成功在 .result.agent);wait 钉解析时占用者与 `agent_not_running` 处置;审批等待形(`--until blocked` 加 read 加 send-keys);普通进程走 `pane wait-output` 即时搜快照(不走生命周期);idle 与 done 差别仅 seen(focus 标、read 不标);状态优先集成上报、无上报退屏幕检测。新增命令形已本机实跑(`--until idle --until done` 双收束、`pane wait-output` 命中与超时两路径),纯语义断言标 [经验] 待首跑回填
- 同步面:frontmatter 触发词加状态门控与事件驱动与 agent wait;双 manifest 与市场条目 description 三处逐字同;evo-herdr README 与 docs 地图;版本线四插件 0.4.1 齐 0.4.2,顺手刷四插件 README「当前发布」行存量漂移(第八十三批起停 0.4.0)

### 变更 2026-10-02,第八十四批:cli-docs 四样板对照轻吸收

- 用户立单(2026-10-02):登记 gh、cloudflare/cf、wevm/incur、gakonst/incur-rs 四样板仓,对照研究学习改进 cli-docs;gh api 源码直读加文档站抓取,关键断言五项本机二道抽查;用户裁定轻吸收档加 evo-adr 升版,并令 skill 内容不带历史轨迹
- **S010 研究档案**:四仓文档实践对照。结论:命令参考单源生成四仓共识;incur 双实现与乙面旗标七件、CTA、信封、退出码零漂移;上游新长 skills 分发基建与 OpenAPI 投影;gh 外挂实战卡 SKILL.md 补 agent 面;cf 为超大规模命令空间的 agent 发现答案。对照分流:等价四桶不重复吸收、真新增七处、留档五件;六态标注,信源点名止于档案面
- **轻吸收(agent-face 七处,五件框架与 ADR-0014 与 REQ-006 不动,正文零历史轨迹)**:--llms 机器形 manifest 版本串、错误对象可选 retryable、破坏性命令非交互路径、对外契约即接口、示例单一真源、附录升第三席 mcp 与 http api 与 skill 分发(含 openapi 同图派生);SKILL.md 附录行同步一笔
- 同步面:research 登记、docs 地图、diary
- **版本载体:四插件版本线 0.4.0 齐平 0.4.1**(双 manifest 加市场条目);顺手追正:第八十三批升版漏改 evo-herdr codex manifest 且只升一家违反四插件同版本线断言,主库守卫红灯,本批补齐并四线齐平 [实证: 2026-10-02 追正前 pytest 1 failed,追正后 26 passed]

### 变更 2026-09-23,第八十二批:evo-research 的 bh 命令面改 browse

- 用户立单(2026-09-23):research skill 的浏览器面从 `bh`(browser-harness)整体切换为 `browse`(browse_rs 0.21.0);用户同期裁定使用口径:**先 `browse status` 确认浏览器状态,不动宿主机浏览器**
- web.md 重写为 browse 指南:Google 零浏览器腿加 `--new-tab` 浏览器腿(2026-09-23 实证零浏览器腿退化只回 redirect 占位页,浏览器腿 `goto` 加 `pageEval` 抽 `a h3` 得五条标题加 URL);Medium 走 `?format=json`/RSS/GraphQL 且搜索转 Google `site:medium.com`;X 本地库通道随 bh 退役改走 Google `site:x.com` 加公开帖锚点;`browse fetch` 升级腿(正文稀薄换新引擎)立为宿主机附着态禁手
- SKILL.md 硬规则换口径:先确认浏览器态、不动宿主机浏览器(不 up/down 默认实例、不附着用户 Chrome)、研究优先隔离态(BROWSE_NAME 加 `--headless --isolated`,本机无 Chrome 如实报缺)、HTTP 优先;最小命令面与意图路由表同步;x.md/pipeline.md/evo-research README/双 manifest/市场条目/根 README/docs 地图/AGENTS 外部命令清单齐改
- 坑入实证:`browse fetch` 升级腿杀宿主机引擎 47312 换 20208(2026-09-23 实踩,用户裁定入硬规则)

### 变更 2026-09-23,第八十一批:report skill 移除加跨机器工位交流法

- 用户立单:移除 `report` 研究成文 skill(ADR-0015,REQ-007),四插件十一 skill 收敛为十 skill。`plugins/evo-research/skills/report/` 全目录移除;成文路由归 doc-gov 投影纪律出 md
- 同步面全改:守卫 SKILLS 清单与 report 断言段删除、docstring 计数十一改十;双 manifest 与市场条目描述去 report 化(codex 面 interface 与 keywords 同步);pre-commit 断链段去 report;gates 计数;根 README 意图表与定位行、docs 地图去 report 行;evo-research README 单 skill 化;research 与 doc-gov(SKILL 与 flow-archive 与 references 索引)互引路由改指投影纪律;AGENTS 合同计数与阶段行;manifest 版本线不动(批次级变更不升版)
- **herdr-flywheel 跨机器工位交流法**:SKILL.md 新节「跨机器工位」五条纪律(机器面实查、--machine 命令路由且不可叠加其它 launch 选项、派单前双查、跨机周知双侧留回执、stalled 误报处置);references/pitfalls.md 新「跨机器工位面」三坑加收尾补 --wait 撞已决态一坑;SKILL 触发词与参考行同步 [实证: 2026-09-23 OfficeCLI 维护归属周知轮 lan-ubuntu,本地十四工位加远程 lan-ubuntu 双侧回执齐]

### 新增 2026-09-21,第八十批:评审闸门轮工位实踩吸收

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

### 变更 2026-09-03

- skill 由单文件 `SKILL.md` 重构为 skill 规范仓 三层布局（SKILL.md 概览 + references/howto 详参 + verification/evals 两类评估）
- skill 命名 `project-docs` 到 `project-evo`（项目进化），description 增加进化闭环触发词
- proven 语义修正：明确为**完全成功的 plan 方案归档**（立项建方案、完成回填），非里程碑/成果列表 [经验： 用户裁定]

### 移除 2026-09-03

- 撤回用户级安装副本（`~/.claude/skills/project-evo`）与项目内 `.claude/skills/` 副本；源码唯一位置改为 `skills/project-evo/`
