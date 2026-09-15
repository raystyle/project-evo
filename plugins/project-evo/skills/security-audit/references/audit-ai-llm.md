# AI、LLM 与 agent 狩猎

> 定位:当语言模型参与信任敏感决策时,审计模型特有的委托层:上下文与记忆、工具与动作、MCP 信任、输出与泄露。

#### 何时使用本文件

当语言模型参与信任敏感决策时使用本文件:聊天机器人与助手、RAG 管线、持久化 agent 记忆、agent/工具调用循环、MCP 服务器与客户端、从不可信输入构建 prompt 的代码,或消费模型输出并据此行动的代码。关键数据流是*不可信内容到模型或内存,再到能力、权限或接收端(sink)*。

与 `audit-attack-classes.md` 配合使用,而非替代它。传输、访问控制、查询构造、文件系统使用与输出渲染仍是普通信任边界。本文件覆盖模型特有的委托层。按检索、记忆、工具分发、MCP 与输出处理拆分大目标。

## 核心纪律(本域每个 agent prompt 都要包含)

```
- Prompt injection alone is not a finding. Require a code-level boundary failure: content reaches another principal's context, invokes authority the requester lacks, discloses data they cannot read, or drives a sink they cannot reach directly.
- Model output, memory, tool descriptions, and MCP responses are untrusted inputs. Point to the code that grants authority, trusts output, writes durable state, or feeds a sink.
- A guardrail prompt is not a security boundary. Count only deterministic checks, resource-scoped authorization, isolation, binding, and constrained credentials.
- State the attacker, affected principal, effective execution identity, resource, exact action, authority used, and observable impact. An intentional direct request to use the requester's existing authority is not a delegation defect merely because a model executes it.
- Authorization and action binding are separate controls. Attacker-controlled content that causes an action under an affected principal's valid authority is an action-binding failure when that principal did not intentionally request or approve the exact action.
- Classify every candidate as `confirmed` only after source evidence and bounded local validation establish the boundary and result. Use `needs_validation` when a required provider, deployment, model, renderer, or identity behavior is not observable locally.
```

## 上下文、检索与记忆攻击类(subagent_type: `general`)

**通过检索或摄取内容的间接注入**

攻击者可以写入进入另一个 principal 模型上下文的 RAG 文档、被索引页面、文件、邮件、issue 正文、工具响应或元数据。追查谁能写每个来源、检索如何划定其范围、哪个会话消费它,以及在该处启用了什么能力。分别检查隔离、资源授权与对消费方 principal 意图的绑定。缺陷是缺失的确定性控制,而不是有说服力的文本本身。

**跨会话或跨租户上下文渗漏**

会话历史、embedding、检索结果或 prompt 缓存的 key 划得过宽。在查询本身与每个 cache key 中验证租户与 ACL 过滤。若替代查询、共享缓存或批处理路径遗漏了对象上存储的租户字段,该字段不构成强制。

**持久记忆投毒**

攻击者可控内容或模型摘要被写入记忆,随后影响另一个任务、用户或特权会话。审查谁可以创建、更新、合并、删除记忆;其来源(provenance)与租户范围;低信任观察是否会变成持久的指令或事实;以及检索是否区分用户偏好与工具策略。由用户有意保存、且只用于该用户有意且被允许的请求的记忆,不构成跨边界发现。

**prompt 角色与来源混淆**

prompt 组装让不可信文本冒充系统消息、先前的对话轮、工具结果、策略或记忆记录。查找字符串拼接、无类型的对话历史、调用方可控的 role 字段,以及丢失来源标签的序列化往返。确认伪造的来源确实改变了某个确定性信任决策或触达了有意义的能力。

## 工具与动作攻击类(subagent_type: `general`)

**工具参数注入到下游 sink**

模型产生的参数未经 handler 侧校验就到达 SQL、shell、文件、URL 抓取或特权 API。把工具 schema 当作输入解析,然后逐字段从解码后的调用追到 sink。结构化输出收窄了形状;它不建立授权、安全路径、安全 URL 或查询语义。

**过度代理权与 confused deputy 权限**

agent 使用服务身份或宽泛凭证,而工具 handler 不重新检查请求方 principal 对指定资源的权限。同时验证有效身份,以及调用方能否通过正常产品界面执行该精确操作。带强制每用户查询范围的共享凭证不是缺陷。

**动作确认与批准绑定**

用户批准的是所描述的一个动作,但执行可以使用被更改的参数、不同的资源、不同的 principal 或更晚的模型轮次。当攻击者可控内容在受害者有效权限下造成副作用、而受害者并未有意请求或批准时,动作绑定缺陷同样存在,即便泛化授权允许受害者执行该操作。审查意图或确认是否绑定了规范化的工具名、完整参数对象、请求方、目标、金额、有效期与批量成员资格。检查重试与续接会话:一次批准不得授权被篡改或重复的副作用。

**工具 schema 与分发器不一致**

schema 接受了分发器或 handler 有不同解释的别名、额外字段、重复键、类型强转、嵌套自由格式对象或越界值。对照 schema 校验、规范化、生成的绑定与 handler 默认值。在值变成资源选择器或安全相关选项之处再次校验。

**无界的委托动作循环**

一个有界的请求可以反复入队花费、发送、变更或外部 API 工作,而没有按请求预算、按动作授权、取消或幂等控制。确认对共享成本、配额、其他用户或持久状态的影响。不要用耗尽服务的方式测试;使用代码级记账与本地有界循环。

## MCP 与子 agent 信任类(subagent_type: `general`)

**子 agent 与 MCP 信任继承**

被委托的任务拿到完整的会话、凭证、记忆或能力,而不是所需的最小权限。检查每次调用携带的 principal 与租户、能力收窄、凭证 audience,以及委托结果返回时是否被当作不可信。

**MCP 服务器与工具身份混淆**

调用或结果按攻击者可影响的服务器名、工具名、请求 ID、资源 URI 或模型选择的别名路由,而不是按已认证连接与未决请求。检查两个服务器能否声明同一工具或资源身份、重连是否改变绑定,以及一个服务器的响应能否满足另一个服务器的未决调用。

**MCP 元数据与 schema 被当作策略**

MCP 对端提供的工具描述、资源元数据、prompt、补全提示或 schema 被当作策略或授权信任。这些字段可以引导模型,但不能授予权力。找到在元数据冲突时仍然权威的确定性允许清单、服务器身份检查与 handler 授权。

## 输出与泄露攻击类(subagent_type: `general`)

**不安全输出渲染**

模型输出未经 sink 要求的编码与策略就到达执行中的 HTML、Markdown、模板、URL 或命令 sink。浏览器渲染方面,在 `audit-client-side.md` 中验证自动加载资源与 CSP 或净化;仓库之外的渲染器行为使该候选为 `needs_validation`。

**敏感上下文提取**

组装出的上下文包含凭证、另一用户的数据、私有源码或自身即授予访问权的策略值,而受用户影响的输出暴露了它们。阅读 prompt 组装与数据获取代码。不跨越数据边界的通用指令或行为泄露不是发现。

## 通用动作(适用于以上各类)

- 先画四张图:每个执行身份、每项能力、每个可写的上下文或记忆来源、每个输出目的地。然后把起点的 principal 连到终点的权限。
- 从有副作用的工具出发,反向穿过分发器、schema、确认、模型上下文、检索与摄取。从持久记忆读取出发,追查每一个写入者。
- 对同一动作对照直连、排队、重试、续接、批量与委托路径。最强的闸门必须应用在参数定稿之后、每个副作用之前。

## 验证规则(报告本域任何发现前都要执行)

1. 指明被跨越的边界与可观察结果:攻击者、受影响 principal 或共享资源、执行身份、目标,以及未授权或未被请求的动作或泄露。
2. 对 confused deputy 权限主张,证明工具缺少请求方与资源级授权,且攻击者正常情况下无法执行同一动作。对动作绑定主张,则证明攻击者可控内容在受影响 principal 的权限下造成了一个该 principal 并未有意请求或批准的动作。有效的泛化授权不能证明该意图。
3. 对记忆或检索主张,同时引用攻击者可控的写入与后来的跨 principal 读取或特权决策。没有可达消费者的共享记录不足够。
4. 对动作绑定,确立有意请求或规范化的已批准对象(如果存在),并与 handler 实际使用的对象对照。确认本地可观察的未被请求动作、变更、重复或权限变化,而不把测试扩展到有害执行。对 schema 不一致,对照规范化后的已验证对象与 handler 的对象。
5. 对 MCP 身份主张,验证已认证连接、请求关联、工具命名空间与有效凭证。需要外部服务器身份或部署路由时标 `needs_validation`。
6. 只有具备完整源码追踪与有意义结果时才返回 `confirmed` 发现。对具体未解决的边界事实返回 `needs_validation`,并说明解决它所需的受控本地检查或由所有者观察的检查。
