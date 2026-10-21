# S019:agent 原生 CLI 标准聚合

> 交流波知识页二:CLI 标准专题六仓票聚合去重定稿案。票源 = rust-exchange 流 seq 9 至 14(browse、hst、s5、reader、dctl、ark 六票,derived_from,全文见 `../sources/external/2026-10-21-rust-exchange-stream.md`);业界背书 S017;互鉴面 S018。产物 = dev-cli 技能公约面(REQ-060),规范条目以 dev-cli 技能为准,本页是信源与分流档案。pi-rs-agent 票未到,到票后增量定稿(补记于此,不回写)。

## 聚合规则

- 去重合流:同义公约合一,票源并列;反票降级(ark 判类型化 CTA 不适用,降应该级)[实证: 流 seq 14]
- 分级:必须 = 破坏互操作或埋坑的硬公约;应该 = 收益明确但仓可裁
- 聚合结果:必须 10 条、应该 3 条[实证: 本页聚合,2026-10-21]

## 必须级公约（10 条）

| 号 | 公约 | 要点 | 票源 |
| --- | --- | --- | --- |
| C1 | 三面同源派生 | 命令树唯一真源,curated 段配穷尽对锁漂移守卫(精确等值断言),锁输出形态不锁旗标,守卫进 CI 发布链;手写第二份清单 lint 红 | browse、ark、s5、hst[实证: seq 9 至 11] |
| C2 | 机器形统一信封 | --llms --json 机器形;信封 ok、data 或 error、meta;next-step 载体类型化进 meta 且字段名舰队统一;字段序稳定禁字母序重排 | hst、reader、browse、s5[实证: seq 9 至 12] |
| C3 | 错误机器化 | 非 0 必有结构化 stderr 单行 JSON 携 code 与 message;code 稳定枚举;解析级错误同走机器形灭双解析;stdout 数据 stderr 诊断恒分道;裁 2 须记录 | hst、s5、dctl[实证: seq 10、11、13] |
| C4 | 退出码契约三态文档化 | 0 成功、1 业务未命中、2 用法与系统错误;信号码直通记档;契约写进 --llms 表;裸调用恒 0 | ark、reader、s5;dctl 自认裸调用 2 缺口属本条翻转对象[实证: seq 11 至 14] |
| C5 | 写级动词预览缺省 | 写级操作预览缺省,确认旗标才执行;非交互路径不弹询问 | hst[实证: seq 10] |
| C6 | 版本单源注入 | 版本号从载体 manifest 注入(编译期),手写版本号即第二真相 | ark、hst、reader[实证: seq 12、14] |
| C7 | 生成物进仓与投影守卫 | 生成物进仓 clone 即得,凡投影必带 --check 严格门禁进 CI 发布链 | browse、hst[实证: seq 9、10] |
| C8 | 安全面 | 凭据零参数(守卫断言)、回显掩码、密档 0600、外插子进程文本不裸进机器面 | s5、dctl[实证: seq 11、13] |
| C9 | 快照守卫标配 | 人机可读面(help、llms、信封、文案)insta 或等价快照锁;路径时间戳 redact;CI 防静默改金 | reader、S017[实证: seq 12 加 S017] |
| C10 | 多端味实机冒烟 | 每平台味产物三面(help、version、llms)实机冒烟 | s5[实证: seq 11] |

## 应该级公约（3 条）

| 号 | 公约 | 要点 | 票源 |
| --- | --- | --- | --- |
| C11 | agent 检测机器形默认 | is-ai-agent 检测自动切 JSON,管道与人读兜底 | dctl[实证: seq 13] |
| C12 | 成功面 next-step 结构化 | 成功回执可带结构化指引(命令加说明形) | dctl[实证: seq 13] |
| C13 | 类型化 CTA 分级 | 类型化 code 必须;CTA 独立字段应该,错误面已有 hint 类字段覆盖时可不重复(反票判例) | s5 首提、ark 反票[实证: seq 11、14] |

## 与 dev-cli 五件映射（C1 至 C13 落点）

- C1 落第四节自省;C2 与 C3 落第二节协议;C4 落第二节加第五节;C5 落第二节写级扩展;C6 落第三节加第四节(既有条升公约级);C7 落第一节;C8 落第二节安全面新增;C9 落第一节发现面扩展;C10 落第四节邻域;C11 至 C13 落第二节邻域[经验: 映射为本页判定,落文以 REQ-060 补丁为准]

## 定稿判点（聚合中浮现,待 pi-rs 票后终裁）

- next-step 载体字段名:票面有 next_step(browse、reader)与 guidance 三元组(dctl)两形;dev-cli 既有 meta.cta 的 commands 数组形;建议统一字段名 next_step、承 commands 数组折算律、cta 作兼容别名[假设: 建议,待终裁]
- dctl 裸调用 exit 2 缺口:公约 C4 的点名翻转对象,dev-cli 第五节既有裸调用恒 0 条文盖得住,dctl 侧按公约对齐即可,不另立标准[经验]
