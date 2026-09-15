# 攻击类目

> 定位:security-audit skill 的攻击类目总表。按应用形态选择配套专题文件,并定义普通攻击类(ordinary attack class)的狩猎与验证要点。

#### 攻击类目:依据阶段 1 选择与拆分

选择与应用类型相关的攻击类。不是每个类都适用于每个代码库。下面这份清单只是起点;从阶段 1 补充应用特有的类,并按子系统拆分大型代码库。把工作框定为发现、验证、修复漏洞并排定优先级。验证只限源码复查与有界的本地 fixture;不开发 payload 链,不在在线服务上测试可用性,不在共享环境中采取行动。

只有当源码证据与有界验证共同确立了完整边界与有意义结果时才用 `confirmed`。当某个具体的部署、提供方、平台、身份或运行时事实不可得时用 `needs_validation`;写明缺失的事实,以及能解除它的、属主可安全观测的检查或本地检查。

> **原生/二进制/内核目标**(C/C++/Rust-unsafe、内核模块、解析器与解码器、FFI、并发运行时、二进制加载器、JIT、固件):使用 [audit-memory-binary.md](audit-memory-binary.md) 中的内存安全、整数/ABI、并发、二进制加载器与特权接口各类。
>
> **AI/LLM/agent 目标**(聊天机器人、RAG、持久记忆、工具调用 agent、MCP server/client、prompt 组装或模型控制动作):使用 [audit-ai-llm.md](audit-ai-llm.md) 中的上下文、记忆投毒、动作绑定、tool schema、MCP 身份与输出各类。
>
> **HTTP、web 与身份目标**(普通 web 应用、API、反向代理、CDN、网关、自定义 HTTP 解析器、session、CSRF、JWT、OAuth/OIDC、SAML、MFA、passkey、账户找回/关联、API key 或 mTLS):使用 [audit-web-auth.md](audit-web-auth.md)。
>
> **客户端与浏览器目标**(SPA、浏览器扩展、内嵌 webview、service worker、浏览器存储、跨窗口消息、CORS、WebSocket 或 DOM 渲染):使用 [audit-client-side.md](audit-client-side.md)。
>
> **供应链与发布目标**(依赖解析、生成输入、CI、发布/签名/晋升、更新、插件或扩展):使用 [audit-supply-chain.md](audit-supply-chain.md)。
>
> **云与部署目标**(IAM、基础设施即代码、容器/Kubernetes、service mesh、serverless/edge、ingress、provider 事件或运行时配置):使用 [audit-cloud-deploy.md](audit-cloud-deploy.md)。
>
> **协议、RPC 与消息目标**(gRPC、GraphQL 传输、Protobuf/Cap'n Proto/Thrift、自定义协议、队列、broker、pub/sub、webhook 或流式 RPC):使用 [audit-protocols-rpc.md](audit-protocols-rpc.md)。
>
> **资源耗尽与可用性目标**(不可信工作可消耗共享 CPU、内存、磁盘、连接、worker、队列、配额或运营方支出):使用 [audit-resource-exhaustion.md](audit-resource-exhaustion.md)。
>
> **数据隔离与生命周期目标**(多租户存储、缓存/搜索、对象链接、分析、导出/备份、迁移、删除、保留或恢复):使用 [audit-data-lifecycle.md](audit-data-lifecycle.md)。
>
> **桌面、移动与本地 IPC 目标**(原生应用、deep link、webview 桥、导出组件、特权 helper、本地 daemon、Unix socket/XPC/Binder/D-Bus):使用 [audit-ipc.md](audit-ipc.md)。

**注入**(subagent_type: `general`)
追踪不可信输入从入口到危险汇聚点(sink)的路径。什么算「危险汇聚点」取决于应用:
- Web 应用:SQL 查询、HTML 输出、shell 命令、模板引擎、文件路径、HTTP 重定向、反序列化
- 库:任何不加验证就处理调用方数据的函数,包括缓冲区操作、解析器、格式化字符串
- CLI 工具:shell 命令构造、文件路径处理、环境变量插值
- 服务:查询构造、消息序列化、日志注入、LDAP/XPATH 查询
- 客户端(浏览器/JS):DOM XSS、原型污染(prototype pollution)、`postMessage`/origin 信任及其他浏览器侧类;选中时由 [audit-client-side.md](audit-client-side.md) 配套块覆盖

不要停在明显的直接路径上。找间接注入:数据被安全存储,随后由另一段代码取回并用于危险上下文。找经由字段名、键、header 与 metadata 的注入,而不只是值。找向次要系统(日志、缓存、搜索索引、分析)的注入。

**访问控制**(subagent_type: `general`)
验证调用方无法做出超出其权限的动作。不要止于确认权限检查存在;要验证它们经由*正确的*机制、对*正确的*资源检查*正确的*权限:
- 是否存在到达同一状态变更、却检查另一个(更弱)权限的路径?
- 请求体中的字段能否覆盖权限系统本意要限制的内容?
- 是否存在以认证做门禁却忘记授权的端点?
- 同一资源是否有多条检查互不一致的访问路径?
- 批量/批处理/导出/导入操作呢?它们是否强制逐项权限?

复杂访问模型按「认证绕过」与「授权逻辑」拆成独立 agent。

**资源与文件处理**(subagent_type: `general`)
- 路径穿越(读取/写入预期目录之外),包括经由 symlink、编码序列与 null 字节
- SSRF(让应用抓取攻击者控制的 URL),包括经由重定向、DNS rebinding 与 URL 解析器差异
- 不安全反序列化、压缩包解压(zip slip)、临时文件处理
- 内存安全(如适用):缓冲区溢出、use-after-free、整数溢出
- 文件操作上的竞态条件(check 与 use 之间的 TOCTOU)

**密码学与机密**(subagent_type: `general`)
- 安全关键值(token、密钥、nonce)使用弱随机数
- 硬编码机密;出现在日志、错误消息、URL 或客户端可见响应中的机密
- 密钥派生破损、缺少 HMAC 验证、nonce 重用
- 机密比较上的时序侧信道
- 密码学原语误用(ECB 模式、无认证加密、静态 IV 等)
- 密码学操作失败时会发生什么?错误路径是否回退为不加密?

**业务逻辑**(subagent_type: `general`)
手工狩猎逻辑错误:标准扫描器找不到它们,而它们能产出高影响发现。对每个主要工作流:
- **状态机违规**:能跳过步骤吗?能倒退吗?能到达无效状态吗?重放一个已完成的流程会怎样?部分失败呢?三步中的第 2 步失败时,第 1 步会回滚吗?
- **有业务影响的竞态条件**:并发操作产生无效状态(双花、重复批准、丢失更新)。聚焦非原子的先检查后行动(check-then-act)操作。
- **数值/数量操纵**:负值、零值、溢出、精度丢失、字符串与数字之间的类型强转。
- **访问边界违规**:不是「权限检查是否存在」,而是「它对这条业务规则是否是正确的检查」?一个操作的输入能否绕过施加在另一个操作上、但效果相同的限制?
- **隐式信任假设**:来自存储、配置、其他组件或插件的数据被假定安全,理由是「进来时已验证过」。如果写入它的是另一条代码路径呢?
- **时间相关逻辑**:过期检查、调度、限流窗口、时钟偏移。在精确的边界时刻会发生什么?组件之间的时区差异呢?
- **默认与回退行为**:配置缺失时安全姿态如何?feature flag 关闭时呢?依赖不可用时呢?系统处于迁移中途时呢?

**功能滥用与数据泄露**(subagent_type: `general`)
被用于非预期目的的合法功能。找设计中的 bug,而不只是代码中的:
- **导出/备份即外泄**:低权限用户能否触发包含高于其访问级数据的导出、快照或备份?能否导出其他用户的数据?导出是否包含已删除/草稿/私密内容?本应剪除的修订历史呢?
- **导入/恢复即注入**:导入能否覆盖既有数据?能否创建绕过正常验证的记录?能否向用户无写权限的集合注入内容?它是否遵守与 UI 相同的权限模型?
- **搜索/过滤/排序即 oracle**:搜索查询能否揭示用户无法直接访问的内容是否存在?过滤参数能否让用户探测其不应知晓的状态、角色或字段?按隐藏字段排序能否通过结果顺序泄露其值?
- **经由副作用的枚举**:「不存在」与「无访问权」的错误消息是否不同?响应时间是否不同?响应大小呢?HTTP 状态码呢?能否经由密码重置、邀请或注册流程枚举用户?
- **预览/草稿/staging 泄露**:预览 token 是限定于单个条目,还是解锁更广访问?草稿内容能否通过搜索、RSS、sitemap 或 API 列举端点被发现?缓存 header 会不会让 CDN 公开提供私密内容?
- **通知/webhook 即 SSRF**:用户能否设置服务器会去抓取的通知 URL、webhook URL 或回调 URL?是否针对内部网络做了验证?重定向之后呢?

**漏洞链与信任边界**(subagent_type: `general`)
单独看被允许或已被围控的行为,当另一个组件或生命周期步骤依赖更强保证时,会成为漏洞:
- **多步边界失败**:测绘低权限 principal 可以读、写、调用与留存什么,然后只把具体输出连接到后续信任决策。确认每个前提,不要假设下游效果。
- **跨组件信任缺口**:组件 A 验证输入后交给组件 B。比对 A 产出的精确保证与 B 所假设的内容,包括截断、类型强转、规范化、租户范围与插件/扩展访问。
- **二阶使用(second-order use)**:存储时安全的数据在后续上下文可能变得危险。字段名变成 JSON path,slug 变成文件路径,转义文本进入原始渲染,存储字符串变成 URL、regex、模板或策略表达式。
- **范围与能力增长**:token、API key、插件、OAuth、MCP 或 AI 能力在委托、刷新、缓存、角色变更或组合之后范围变宽。说出最终 principal 不应拥有的那个具体操作。
- **时序与顺序**:复查 setup、迁移、软删除、撤销/缓存过期、check/use、验证/消费这些窗口。报告前确认过期状态确实被接受。
- **回滚与恢复**:取消删除、恢复、修订回滚与撤销操作必须应用当前的 ownership、验证与授权。确认恢复的是哪个无效状态。

**通配**(subagent_type: `general`)
没有给你指定类别。找出已指派标准类之外的漏洞。

阅读看起来乏味或与安全无关的代码。追踪不完整、实验性、兼容性与回退性质的功能,但保持与其他类相同的具体边界与验证要求。

用这些起点,但不限于它们:
- 代码库里最奇怪的代码是什么?它为什么存在?被滥用会发生什么?
- 有没有让人觉得半成品、实验性或硬拼上去的功能?它们得到的复查最少,因此安全最弱。
- 以前端绝不会采用的方式使用 API 会怎样?UI 约束用户,API 不约束。哪些 API 调用是可能的、却从未被客户端发出?
- 有没有隐藏或未写入文档的端点、参数、header 或功能?到路由注册、middleware 与配置里找文档中没有的东西。
- 把并非为协同设计而设的功能混用会怎样?本地化 + 预览 + 缓存。导入 + 插件 + webhook。OAuth + impersonation + API key。
- git 历史里有没有值得注意的东西?被回退的安全修复、被注释掉的认证检查、提交后又删除的机密(仍在历史里)。
- 哪些合法账户动作会影响其他用户、共享完整性、可用性或运营方成本?围绕这些动作验证遏制、配额、授权与恢复。
- 哪些操作不可逆或需要提权确认?把授权与批准绑定到最终 principal、动作与资源。
- 代码对环境做了哪些假设?假设数据库在本地、时钟准确、DNS 可信、文件系统区分大小写?
- 看测试文件:它们**没有**测什么?把开发者想到过的边界情况(有测试)与没想到过的(没有测试)做比较。

在被指派范围内追查异常,直到不变量有了定论。某处看起来奇怪,就读到你能断言它是否安全为止。如果函数有注释解释它为何安全,验证这个解释。如果变量名叫 `temp`、`hack` 或 `legacy`,仔细读它。

**显见问题**(subagent_type: `general`)
其他 agent 狩猎微妙 bug。本 agent 检查那些容易被忽视的基本暴露项:人人都假定别人已经查过,它们于是最容易被漏掉:
- 源码里有没有硬编码密码、API key、token 或机密?(grep `password`、`secret`、`apikey`、`token`、`Bearer`、`-----BEGIN` 与常见默认密码)
- 有没有涉及安全的 TODO/FIXME/HACK/XXX 注释?(`TODO: add auth`、`FIXME: validate input`、`HACK: skip permission check`)
- debug 模式/dev 模式是否有正确门禁?能否经环境变量、查询参数或 header 在生产开启?
- 有没有在生产能用的 test/example/seed 凭据?
- 有没有未加保护的 `/debug`、`/admin`、`/test`、`/status`、`/health`、`/metrics`、`/env`、`/.env`、`/config` 端点?
- 有没有签入仓库的 `.env`、`.env.local`、`credentials.json`、`*.pem`、`*.key` 文件?
- `.gitignore` 是否真的覆盖机密、上传与本地配置?
- 依赖是否固定版本?依赖树里有没有已知 CVE?(查 lockfile)
- 有没有 `eval()`、`exec()`、`child_process`、`Function()`、`vm.runInContext`、接受动态输入的 `import()`?
- CORS header 是否设为 `*` 或过宽?`Access-Control-Allow-Credentials` 是否与通配 origin 同时使用?
- cookie 是否缺 `HttpOnly`、`Secure` 或 `SameSite` 属性?
- 有没有开放重定向?(名为 `redirect`、`return`、`next`、`url`、`goto`、`continue` 且未经验证就进入重定向的参数)
- 是否强制 TLS?有没有仅走 HTTP 的端点?
- 生产错误响应是否返回栈回溯、内部路径或 SQL 错误?

本 agent 不需要创意,需要彻底与按字面执行。逐项检查,逐项报告结果。

**重要**:对本 agent 报告的任何发现,必须验证完整代码路径,而不是表面现象。若 cookie 缺少 `HttpOnly`,检查该 cookie 是否含安全敏感数据、JS 是否按设计需要读取它。若错误消息包含字段名,检查该字段是否真的会被填充敏感数据。一个标志不是发现:先追踪影响,再报告。
