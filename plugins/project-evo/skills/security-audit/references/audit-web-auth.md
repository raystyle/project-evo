# HTTP 协议与认证狩猎

> 定位:当目标在解析、缓存、浏览器认证或身份边界上使用 HTTP 时,审计协议与身份层造成的 principal、请求、保证等级或 token 混淆类漏洞。

#### 何时使用本文件

当目标在解析、缓存、浏览器认证或身份边界上使用 HTTP 时使用本文件:Web 应用、API、反向代理、CDN、网关、自定义 HTTP 服务器,以及实现 session、JWT、OAuth/OIDC、SAML、密码找回、MFA、passkey、API key 或 mTLS 的服务。与 `audit-attack-classes.md` 配合使用:访问控制审查问的是某个 principal 是否可以执行某个操作;本文件问的是 HTTP 或身份层是否会混淆该操作属于哪个 principal、哪个请求、哪个保证等级(assurance)或哪个 token。

从 Phase 1 选取攻击类。把大目标拆分为:请求分帧与缓存策略、浏览器认证、联邦身份、强认证与找回、服务凭证、session 生命周期。位于不可观测的托管代理之后的单台服务器,可由源码确认的走私(request smuggling)面很小;代理或自定义解析器则大得多。

## 核心纪律(本域每个 agent prompt 都要包含)

```
- Framing and cache findings require two interpretations of the same request, response, or key. Name both components and the exact normalized value on each side.
- For every credential, find the signature or secret verification and every binding required for its role: issuer, audience, origin, RP, client, session, principal, resource, assurance, expiry, and one-time state.
- Host, Forwarded, X-Forwarded-*, Origin, Referer, redirect targets, callback state, and request-derived URLs are trust decisions. Trace each to the affected identity or response.
- A missing header, cookie attribute, MFA prompt, or rate limit is not a finding alone. Require an accepted invalid request, cross-principal impact, assurance downgrade, or credential disclosure.
- Classify `confirmed` only from complete source evidence and bounded local request/token tests. Use `needs_validation` when proxy, IdP, browser, certificate, secret, or deployed configuration is required but not visible.
```

## HTTP 分帧与缓存攻击类(subagent_type: `general`)

**请求分帧与 desync(解析失步)**

前端与后端对请求长度或头部规范化的理解不一致。审查多个 `Content-Length` 值、`Transfer-Encoding`、HTTP/2 或 HTTP/3 降级、头部名规范化、禁用的 connection 头,以及 CR/LF 转换。确认一个组件把哪些字节划给某个请求,其对端把哪些字节划给下一个请求。

**通过未纳入 cache key 的输入进行 Web 缓存投毒**

某个请求值会改变缓存内容或安全相关头部,却没有进入 cache key。将 cache key 的构造与每种响应变体对照,包括转发的 host/scheme、被选中的 cookie、查询串规范化、语言/设备头部与授权状态。

**缓存欺骗与私有响应被缓存**

缓存路由把私有动态路径当作公共静态资源,或缓存了策略缺失身份与授权输入的响应。将边缘缓存判定与应用路由解析、后缀/路径参数规范化以及响应缓存指令对照。

**Host 与转发头信任**

不可信的 host/代理元数据决定了绝对 URL、租户路由、回调、重置链接、cache key 或授权所用的客户端地址。确认谁能提供该头部,以及可信入口是否会移除客户端提供的副本。

**响应头注入**

不可信数据带着不安全控制字符或经规范化后进入 `Location`、`Set-Cookie`、CSP 或其他响应头。报告前先验证框架是否拒绝,并要求有安全相关的响应变化。

## 浏览器会话攻击类(subagent_type: `general`)

**常规 CSRF**

浏览器把环境凭证(ambient credentials)发送到一个接受跨站请求的状态变更端点,且该端点没有有效的 anti-CSRF token、同站请求绑定或严格的 Origin/Referer 校验。盘点每一个以 cookie 认证的变更操作,包括表单、类 JSON、multipart、method-override 与遗留路由。SameSite 只对实际使用的 cookie 与浏览器上下文有效;登录 CSRF 与跨站子资源请求可能有不同的要求。

**会话固定与失效**

session 标识在登录、账号切换、MFA 完成、模拟登录(impersonation)或其他权限变化时不轮换,或在登出、改密、吊销与禁用账号后仍有效。检查服务端 session、refresh token、签名 cookie、websocket 状态、缓存副本与回退端点。

**Cookie 作用域与传输**

敏感 cookie 的 `Domain` 或 `Path` 过宽,可能跨越不安全传输,或与另一组件以不同方式选中的同名 cookie 冲突。单纯缺少属性只是加固建议,除非存在现实的更低信任 origin、网络位置或浏览器路径能够获取或替换该凭证。

## 联邦身份攻击类(subagent_type: `general`)

先厘清角色。授权服务器的控制(如重定向白名单与 code 签发)不属于 relying party 客户端。校验与绑定缺陷归属于消费该构件(artifact)的组件。

**JWT 校验与声明绑定**

检查签名验证、服务端固定的算法与密钥来源,再查 `exp`、`nbf`、`aud` 与 `iss`。把 `kid`、`jku`、`x5u` 作为不可信的密钥选择器审查,关注重复头部/头部规范化,以及只解码不验签的路径。对另一服务有效的 token 在此处无效,即便它由可信 issuer 签发。

**OAuth/OIDC 请求与回调绑定**

当目标是授权服务器时,校验 `redirect_uri` 的精确归属;绑定 session 的 `state`;适用处的 PKCE 与授权码绑定;ID token 的 issuer/audience/签名/nonce;以及多 provider 流程中所选 IdP 的绑定。对照首次回调、重试、mobile/deep-link 与账号关联路由。

**SAML 签名对象与断言绑定**

确保被验证签名的元素就是被用作身份的元素。审查未签名/回退路径、安全的 XML 解析器配置、规范化差异,以及新鲜度/绑定字段:有效期窗口、audience/recipient、请求关联与重放状态。

## MFA、passkey 与账号迁移攻击类(subagent_type: `general`)

**MFA 注册与保证等级降级**

注册、替换、禁用、恢复码生成、可信设备创建与回退登录都要求预期的前置保证等级。检查:仅凭有效的第一因子,能否在缺少策略要求的新鲜认证时注册或替换第二因子;被禁用或过期的因子是否停止为会话授权。

**Step-up 绑定与绕过**

挑战成功后升级到了错误的 session、账号、租户、操作或 API 请求,或者某条替代路由省略了保证等级检查。把挑战绑定到 principal、当前 session、保证目标、必要时到操作或资源、有效期与一次性完成。对照 UI、API、批量、恢复与续接流程路径。

**WebAuthn 与 passkey 验证**

注册时,把 challenge、RP ID、期望 origin、凭证、user/userHandle、算法与策略要求的 user verification 绑定到发起会话。认证时,验证 challenge、RP/origin、凭证归属、签名与预期的用户在场/验证。检查账号发现与关联流程中的 userHandle 或凭证与账号的混淆。签名计数器处理只有在产品把计数回退当作克隆信号时才有意义。

**账号关联与身份冲突**

向既有账号添加 IdP、passkey、email、手机号、设备或外部账号,必须要求当前已认证会话、对新身份的已验证所有权、策略要求的 step-up,以及绑定到发起关联账号的回调 state。审查解绑/重绑与邀请接受路径中的已验证标识符冲突或租户冲突。

**密码重置与更广的找回**

恢复 token、客服/管理员找回、备用码、设备迁移与 email 或手机号变更常常成为最弱的认证路径。验证 token 随机性、用户/操作绑定、有效期、一次性状态、速率/记账控制、投递 URL 信任,以及对先前 token 与会话的失效处理。仅泄露公开的账号存在性的差异化响应不自动构成安全发现。

## API key 与 mTLS 攻击类(subagent_type: `general`)

**API key 作用域与资源绑定**

key 认证到的租户、资源、操作或环境比其服务端记录授权的更宽,或请求参数覆盖了这些绑定。审查 key 查找、前缀/完整 secret 验证、publishable key 与 secret key 的类型混淆、scope 检查、轮换、吊销缓存与批量端点。

**API key 暴露与不安全传输**

key 出现在客户端打包产物、URL、重定向、日志、错误路径、构建产物或更低信任 principal 可访问的响应中。名为 key 的公开标识符不是 secret。确认 key 的类型与泄露所获得的权限。

**mTLS 对端与应用身份混淆**

进程信任来自任意网络对端的客户端证书身份头;或验证了证书链,却把攻击者可影响的 subject 文本错误映射到账号;或接受了错误信任域、扩展用途、audience 或有效期策略的证书。当可信代理终结 mTLS 时,验证:只有该代理能连接、它移除入站身份头、后端把净化后的身份绑定到请求。

**证书生命周期回退**

过期、吊销、缺失或续期失败的证书导致静默回退为仅 bearer 或匿名运行,或长寿连接池在吊销后仍保留授权。部署侧缺吊销数据使结论为 `needs_validation`;仓内的 fail-open 分支可由源码确认。

## 通用动作(适用于以上各类)

- 对每个凭证与挑战,走查签发(issue)、存储(store)、传输(transmit)、消费(consume)、刷新(refresh)、吊销(revoke)全链路。对照正常、错误、重试、迁移、遗留与账号切换路径。
- 枚举通往同一身份的每一扇门与通往同一敏感操作的每一条路由。有效策略是最弱的并行路径,而不是最精美的 UI。
- 并排 diff 解析器、代理、路由、缓存与应用的规范化行为。本地验证时,把相同的受控请求 fixture 喂给每个组件,而不是向线上部署发流量。
- 对找回与关联,画出账号前后状态图。每条边必须标注当前 principal、新身份的证明、所需保证等级、回调/session 绑定与吊销效果。

## 验证规则(报告本域任何发现前都要执行)

1. 应用源码可见性门槛。代理链、边缘 cache key、IdP 策略、证书信任、浏览器 cookie 行为、secrets 与已部署的认证模式可能在仓库之外。记录精确的 `needs_validation` 候选,而不是断言缺失的基础设施行为。
2. 对分帧与缓存发现,指明两个组件与分歧的解析/key。用受控的本地 fixture 确认跨请求、跨用户或私有响应的影响。
3. 对 token、MFA、passkey、账号关联、找回、API key 与 mTLS 发现,引用校验代码行与缺失的 principal/session/resource/origin/audience/action/assurance 绑定。证明服务器接受了无效的状态迁移或凭证。
4. 对 CSRF,指明环境凭证、状态变更路由、被接受的跨站请求形态、浏览器 cookie 策略与缺失的有效检查。只读操作与要求非环境 bearer token 的路由不算数。
5. 验证框架与库的默认行为。版本或配置未知时用 `needs_validation`;不要把未验证的严重断言降级为更低严重度的 confirmed 发现。
6. 只有具备完整源码追踪且可观察到未授权的身份、状态或泄露时才返回 `confirmed`。对 `needs_validation`,指明缺失的事实以及能解决它的安全本地检查或由所有者观察的检查。
