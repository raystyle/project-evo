# 客户端与浏览器狩猎

> security-audit skill 的客户端与浏览器篇:当有意义的信任决策或不可信渲染发生在浏览器中时使用,覆盖浏览器 sources 与 sinks、origin 边界、浏览器持久化与跨站点状态 oracle 的攻击类与验证规则。

#### 何时使用本文件

当有意义的信任决策或不可信渲染发生在浏览器中时使用本文件:单页应用、浏览器扩展、内嵌 webview、service worker、离线应用,以及把可被攻击者影响的内容渲染进 DOM、接收跨窗口消息或使用浏览器存储的代码。这些路径包含服务端永远看不到的 sources,如 URL fragment、`window.name`、`postMessage` 与先前缓存的内容。

与 `audit-attack-classes.md` 配合使用。本文件覆盖浏览器 sources 与 sinks、origin 边界、浏览器持久化与跨站点状态 oracle。webview 桥的原生侧见 `audit-ipc.md`;服务端 CSRF、会话与认证回调见 `audit-web-auth.md`。

## 核心纪律(纳入本领域每个 agent 提示词)

```
- A client-side candidate needs a controllable source and an executing or disclosing sink. Name both and show attacker-influenced data reaching the sink.
- The impact must reach a victim's session, another origin, or shared persistence. Self-injection and disclosure of the attacker's own data are not findings.
- Framework escaping, browser same-origin policy, CSP, COOP/CORP, service-worker scope, and modern noopener defaults are real controls. Verify them before assigning impact.
- Browser storage and caches are shared by origin and may outlive login state. Identify who writes, who reads, and which account, tenant, or worker lifecycle clears each record.
- Use `confirmed` only for complete source evidence plus bounded local browser tests. Use `needs_validation` when renderer, extension permission, deployed header, or browser-policy behavior is required but unavailable.
```

## DOM 与对象状态攻击类(subagent_type: `general`)

**基于 DOM 的 XSS**
追踪 `location` 字段、`document.referrer`、`window.name`、消息数据、storage 与浏览器控制的 document 状态,流入 `innerHTML`、`outerHTML`、`document.write`、字符串求值 API、可执行 URL、jQuery HTML API 或框架逃生舱。框架已转义的插值不是 finding。

**DOM clobbering(对象属性遮蔽)**
攻击者注入的 `id` 或 `name` 属性遮蔽一个全局、form 属性、配置对象或初始化标志,代码随后信任被遮蔽的值。要求同时具备保留该属性的 markup 路径与被遮蔽值的安全相关使用。

**原型污染与 gadget 链**
攻击者控制的 key 到达递归写入(如 deep merge 或路径赋值)并修改 prototype 状态;随后一个可达 gadget 消费被污染的属性,改变授权、执行、导航或渲染。`JSON.parse`、浅拷贝或没有 gadget 的污染都不足够。

## 跨源消息与网络攻击类(subagent_type: `general`)

**`postMessage` 的 origin 与 source 信任**
handler 在没有精确 origin allowlist 的情况下用 `event.data` 执行敏感动作,且在多 frame 共享同一 origin 时未校验预期的 `event.source`。发送侧,发往 `*` 的敏感数据会到达非预期的嵌入方。弱的子串、前缀、后缀或未锚定正则的 origin 匹配不是 origin 校验。

**跨站 WebSocket 请求利用**
WebSocket 升级在没有 `Origin` 校验或通道专属 token 的情况下接受来自不可信 origin 的附带 cookie,使受害者会话可读取或篡改数据。需同时确认升级行为与一个安全相关的消息 handler。

**带凭证的 CORS 信任**
服务端在允许凭证的同时反射或弱匹配 `Origin`,并返回敏感响应。带凭证的裸通配符会被浏览器拒绝;只报告实际反射/放行的 origin 路径与跨源数据或变更。

## Service worker 与浏览器存储攻击类(subagent_type: `general`)

**Service worker 注册与 scope 接管**
可被攻击者影响的内容可以成为注册的 worker 脚本、控制一个获得过宽 `Service-Worker-Allowed` scope 的路径,或在无完整性控制下改动更新导入。验证最终脚本 URL、响应 MIME type、origin、scope,以及谁控制每个被导入的脚本。带预期 scope 的正常同源 worker 不是缺陷。

**Service worker 缓存与身份混淆**
worker 在策略中未包含账号、租户、授权状态或请求模式就缓存个性化响应,然后在账号切换或登出后继续返回它们。审查 fetch 事件路由、缓存名与键、导航 fallback、缓存清理,以及错误/离线路径是否返回另一个用户先前的响应。

**浏览器存储泄露与过期授权**
token、私有响应、草稿数据或授权决定留在 `localStorage`、`sessionStorage`、IndexedDB、Cache Storage、扩展存储或客户端状态中,变得可被另一个账号或更低信任的同源组件读取。仅存储 token 不是 finding;要求存在真实的更低权限读取者,或撤销/登出后的持续使用。

**跨上下文存储与广播混淆**
`storage` 事件、`BroadcastChannel`、shared worker 或 origin 级缓存在标签页之间携带身份或命令,却不把它们绑定到当前会话。检查账号切换、隐私/普通窗口、租户变更,以及可能覆盖较新认证状态的过期标签页。

## 跨站信息泄露类(subagent_type: `general`)

**XS-Leaks 与跨源状态 oracle**
攻击者页面能在浏览器附带受害者凭证的同时,通过资源 load/error 事件、frame 或窗口状态、重定向行为、计时、缓存状态或响应大小区分受保护的跨源状态。要求一个具体的含秘密谓词,例如私有对象、角色或账号是否存在。泛化的计时差异或公共资源可用性不是 finding。

**窗口与 opener 状态泄露**
跨源窗口被允许获取的元数据或导航结果泄露受保护状态,或保留的 opener/命名窗口关系让攻击者控制的页面影响一次特权导航。检查 COOP、frame 保护、`noopener`、精确 origin,以及可观测状态是否机密。

## UI 遮挡与导航攻击类(subagent_type: `general`)

**Clickjacking(点击劫持)**
被 frame 嵌入的状态变更动作缺少有效的 `frame-ancestors`、`X-Frame-Options` 或等价的 UI 隔离。要求存在敏感动作,并确认它能在被 frame 嵌入状态下完成;只读内容缺失这些头属于 hardening(加固)笔记。

**客户端导航混淆**
客户端 source 在没有 scheme 与目的地策略的情况下控制重定向或导航,包括可执行的 `javascript:` 或 `data:` 目的地。Reverse tabnabbing 只适用于代码显式保留 `window.opener`、使用无隔离的 `window.open`、或支持无隐式 `noopener` 浏览器的情形。

## 通用动作(横跨以上各类)

- 从 DOM、导航、worker、消息与 storage sink 出发,向后追踪到仅浏览器可见与服务器控制的 source。记录本应阻断该路径的浏览器策略。
- 用本地测试 origin 与虚构账号测试账号切换、登出、worker 更新、离线 fallback 与过期标签页状态。不使用生产用户、origin 或共享服务。
- 对 XS-Leaks,只列出由源码与本地浏览器行为证明的谓词;然后识别能消除该 oracle 的响应头或渲染选择。

## 验证规则(在此报告任何 finding 前应用)

1. 引用 source、sink、浏览器策略、受影响 origin/会话,以及可观测的变更或泄露。
2. 原型污染要证明递归写入与一个安全相关 gadget;DOM clobbering 要证明 markup 存活且被遮蔽值被使用。
3. service worker 与存储要证明生命周期可达性:攻击者控制的写入或缓存条目必须到达不同的账号、租户或更晚的授权状态。
4. 消息、CORS、WebSocket 与 XS-Leaks 要展示精确的 origin/source 校验与被暴露的受保护状态或动作;确认 CSP、COOP/CORP、cookie 与 SameSite 策略并未已经阻止它。
5. 仅在具备完整客户端路径与有界本地证据时返回 `confirmed` findings;返回 `needs_validation` 时附上所有者必须验证的确切已部署响应头、扩展权限、浏览器版本或 renderer 行为。
