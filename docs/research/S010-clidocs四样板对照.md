# S010:cli-docs 四样板对照

- 状态:已完成
- 日期:2026-10-02
- 关联:[cli/cli](https://github.com/cli/cli)、[cloudflare/cf](https://github.com/cloudflare/cf)、[wevm/incur](https://github.com/wevm/incur)、[gakonst/incur-rs](https://github.com/gakonst/incur-rs);吸收落点 `../diary/2026-10-02-clidocs四样板对照.md` 与 `../../plugins/evo-adr/skills/cli-docs/references/agent-face.md`(第八十四批);乙面参考源沿革见 `../diary/2026-09-17-流程标准起草.md`

> 问题:cli-docs 双标准是否对表业界成熟 CLI,乙面参考源(incur 双实现)自第七十七批吸收后有无漂移。方法:四仓源码与文档站直读(gh api 原文抓取加文档站阅读器),关键断言五项本机二道抽查。结论:五件框架与旗标七件全部站住,上游未见口径漂移;上游新长 skills 分发基建与 OpenAPI 投影两面;真新增七处轻吸收进 agent-face 与附录,五件留档。

## 背景

第七十七批立 cli-docs 时乙面以 incur 双实现(TS 加 Rust)为参考源。本批用户立单登记四个样板仓对照研究:incur 与 incur-rs 为上游漂移复核,GitHub 官方 gh 为成熟大厂样本,Cloudflare cf 为 agentic CLI 新样本。研究焦点为 CLI 文档如何同时服务人类与 agent。

## 关键结论

1. **命令参考单源生成是四仓共识,无一仓手维护第二份参考。** gh 发布期由命令树生成 man 与网站手册(gen-docs 链);cf 命令面本身由 OpenAPI 规范生成并配每命令元数据边车喂 help 与补全;incur 系从 schema 或 derive 一处定义派生 help、schema、手册、skill。[实证: 2026-10-02 gh api 源码直读(cmd/gen-docs、packages/cli/generate.ts、incur/src/manifest.rs)]
2. **incur 双实现与乙面现行口径未见漂移。** 旗标七件(--filter-output、--format、--full-output、--help、--llms、--json、--schema)与可选扩展(token 三件、--mcp、--update)在 TS 与 Rust 两实现同名同义;信封 ok/data|error/meta、CTA 折算、toon 缺省、退出码 0/1/2(默认失败 1、用法错误 2)全部对齐。[实证: 2026-10-02 gh api 源码直读(incur/src/error.rs 与 src/Cli.ts 与 src/Help.ts)]
3. **上游自第七十七批后新长两面:skills 分发基建与 OpenAPI 投影。** incur 有运行时生成 SKILL.md 的模块与 skills add 发现通道;incur-rs 有清单哈希过期检测且永不覆盖用户手写 skill 目录(有专门测试);两实现均由同一命令图投影 OpenAPI 文档。[实证: 2026-10-02 gh api 源码直读(incur-rs 的 incur/src/skills.rs 与 incur 的 src/Openapi.ts)]
4. **gh 以外挂实战卡补 agent 面,不改架构。** 仓内 skills/gh/SKILL.md 写非交互策略、--json 字段族、分页陷阱、退出码语义(不复述手册),配 `gh skill install` 分发;另有 `gh help reference` 运行时从命令树渲染全量 markdown 参考,零第二文档。[实证: 2026-10-02 gh api 源码直读(skills/gh/SKILL.md 与 pkg/cmd/root/help_reference.go)]
5. **cf 是超大规模命令空间的 agent 发现答案。** agent 上下文检测时在 help 顶部注入「先 cli search、勿链式 --help」指令块;`cf cli search` 本地自然语言搜索最多回五条 JSON;`cf schema` 内省单命令 API 请求形状;破坏性命令非交互缺 --force 打 Aborted 且 exit 0,文档显式告警成功退出不等于已执行;stdout 恒 JSON、消息走 stderr。[实证: 2026-10-02 gh api 源码直读(packages/cli/src/index.ts)加 developers.cloudflare.com/cf 文档站抓取]
6. **错误对象可携机器可判重试语义。** incur-rs 的 Error 结构含 code、message、retryable(可选布尔)、exit_code,失败 exit 1、用法错误 exit 2,进信封后 agent 可判可否重试。[实证: 2026-10-02 gh api 源码直读(incur/src/error.rs 24 至 70 行)]
7. **自称未独立验证项降级存查。** incur 宣称 toon 较 JSON 省约六成 token 的账目表、cf 宣称 2900 余条生成命令,本轮未复测。[经验: 两仓 README 与文档站自称;复核点 = 本机装后 --llms 行数与 --token-count 实测]

## 对照表

| 维度 | gh | cf | incur | incur-rs |
| --- | --- | --- | --- | --- |
| 命令参考单源 | 发布期生成 man 与网站 | OpenAPI 生成命令面 | zod schema 派生 | derive 宏派生 |
| --llms 手册 | 无(有运行时 reference) | 无(llms.txt 在文档站) | 双档含版本串 | 双档 markdown 形 |
| 输出协议 | --json/--jq/--template | stdout 恒 JSON | 信封加 toon 缺省 | 同 TS 版信封 |
| CTA | 无 | 无 | 有(类型化) | 有(成功失败与 MCP 三面) |
| 退出码 | 有专页文档 | Aborted 形 exit 0 | 0/1/2 | 0/1/2 入 error 对象 |
| skill 分发 | 仓内实战卡加 install 命令 | 无 | 生成器加 skills add | 生成加过期检测 |
| agent 上下文检测 | 无(靠非 TTY 行为) | 有(help 顶部注入) | 非交互全信封 | 非交互全信封 |

## 与 cli-docs 对照分流

### 已有等价

不重复吸收,引 agent-face 现行条款:

| 样本实践 | skill 现行条款 |
| --- | --- |
| 四仓单源派生与生成链 | 第四节自省三面同源加漂移守卫 |
| --llms 双档(索引与全量) | 第一节(--llms 与可选 --llms-full) |
| token 三件、toon 缺省、信封、CTA | 第二节旗标全家与类型化 CTA |
| 帮助节序、非交互契约、示例可拷形 | 第三节与第五节 |

### 真新增

第八十四批轻吸收进 agent-face.md,五件框架不动:

1. skill 分发面升附录可选件第三席(实战卡 SKILL.md 加安装通道加过期检测;附录改「mcp、http api 与 skill 分发」)
2. 示例单一真源(结构化示例一处定义,同进帮助与手册与 skill 三面;第三节描述单一真源纪律扩至示例)
3. --llms 机器形带 manifest 版本串(第一节,消费者判协议代际)
4. 错误对象可选 retryable 布尔(第二节错误分道)
5. 破坏性命令非交互路径(第二节,缺确认旗标打 Aborted 不弹询问,手册告警成功退出不等于已执行)
6. OpenAPI 投影(附录 http api 条细化,同一命令图派生禁手写)
7. 对外契约即接口(第二节收束纪律,旗标缺省、信封、退出码、非 TTY 行为的变更视作接口变更)

### 留档不吸收

cf 的 agent 检测注入指令块与自然语言命令搜索(千命令量级以上才成立,标准件不设此面);cf 文档站 llms.txt 与每页 md 直出(网站面,超出 skill 边界);gh 的 man page 生成链与 help 主题族(平台特有);cf 的 usecases 迁移映射(迁移场景特有);incur token 节省数字(未验证,见关键结论七)。

## 裁决

轻吸收定案(用户裁定):七处真新增以一至三行落 agent-face 对应节与附录,SKILL.md 仅同步附录行一笔,五件框架与 ADR-0014 与 REQ-006 不动;evo-adr 版本载体升 0.4.1。上游漂移复核结论:旗标七件与 CTA 与信封口径无需追正。

复核:`gh api repos/wevm/incur/contents/src/Cli.ts -H "Accept: application/vnd.github.raw"`(搜 incur.v1);`gh api repos/gakonst/incur-rs/contents/incur/src/error.rs -H "Accept: application/vnd.github.raw"`(搜 retryable)
