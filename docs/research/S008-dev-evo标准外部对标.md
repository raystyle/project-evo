# S008:dev-evo 标准外部对标

> 问题:dev-evo 作为文档即代码标准与外部生态的差距与可借鉴点。方法:agentskills.io 规范全文抓取、gh 搜生态仓、web 检索采用率。2026-09-16 飞轮批调研,与 ark_rs、ohmycloud、hst_rs 九条用后感互证。

## 发现

### agentskills spec 现行版

- frontmatter 字段全集:name 与 description 必填,license、compatibility、metadata、allowed-tools 可选;allowed-tools 标注 Experimental,支持度随实现而异 [实证: 2026-09-16 agentskills.io/specification 全文抓取]
- 结构约束:name 须与目录名一致、禁连续连字符;SKILL.md 建议 500 行内、正文 5000 token 内;文件引用建议一级深;渐进披露三层:元数据约 100 token、激活载全文、资源按需 [实证: 同上]
- 官方校验器 skills-ref validate(agentskills/agentskills 仓) [实证: 同上]
- 对照本仓:四 skill 合规,compatibility 已在用;allowed-tools 与 metadata 未评估,skill-spec.md 需对表 [推断]

### AGENTS.md 生态

- agentsmd/agents.md 24388 star 开放格式标准;microsoft/skills 3020 star;VoltAgent/awesome-design-md 115983 star,DESIGN.md 同类格式在视觉域走热 [实证: 2026-09-16 gh search repos]
- gh 代码搜 filename:AGENTS.md 默认采样面 198 仓,量级仅示意 [实证]
- agent0ai/dox 1459 star 主打 Self-documenting AGENTS.md,自文档与生成物方向同 ohmycloud 反馈的迁移映射表生成物 [实证加推断]

### llms.txt 惯例

- SE Ranking 30 万域样本采用率 10.13%;提议标准而非官方;社区最常见诉求是可发现性;链接目的地为结构化 markdown 时 agent 读取更快更稳 [实证: 2026-09-16 web 多源检索]
- 定位分工:llms.txt 管找到并理解内容,AGENTS.md 管按规则行动,互补不互斥;dev-evo 的 llms.txt 式检索面与 AGENTS 五节合同分层与此一致 [实证加推断]

### ADR 惯例

- adr.github.io 三段式(Markdown 文件、标题含状态、编目目录)仍是社区基线;本仓 frontmatter 状态机是超集;PE-06/07 判式与规范文档的契约差已被 ohmycloud 两轮打回实证 [推断: 基线常识加内部实证,未单独深挖]

## 对照九条内部反馈的优先级建议

- 高:check 全量报告(去前 5 截断)与 --json 机器读面,飞轮回执刚需,ark-1 与 hst-2 同向
- 高:PE-12 扫描面扩散到 llms.txt 等检索面,ark-3,与 llms.txt 生态同向
- 中:整文件豁免形态官方示例,hst-3,机制已支持路径前缀正则(hst_rs 以 ^docs/proven/ 整目录实证),补 gates.md 示例即可
- 中:迁移映射表生成物,omc-1,与 dox 自文档方向同向
- 中:ADR 与 REQ 的 frontmatter 字段表显式化(omc-3)与 init 模板 rumdl MD025 撞规预防(hst-1)同属模板契约面,可并批
- 低:PE-10 一次性迁移修复子命令,omc-2

九条已落 ROADMAP 阶段二积压;spec 对表(allowed-tools 与 metadata 是否引入)另立待办。
