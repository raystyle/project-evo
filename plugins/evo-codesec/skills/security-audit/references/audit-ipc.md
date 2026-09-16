# 桌面、移动与本地 IPC 猎取

> 角色:桌面、移动与本地 IPC 领域的漏洞猎取参考;当目标是桌面/移动应用、特权 helper、更新器、本地守护进程、webview 宿主、deep-link 处理器或本地 IPC 端点时使用。

#### 何时使用本篇

目标是桌面或移动应用、特权 helper、更新器、本地守护进程、webview 宿主、deep-link 处理器、浏览器 native messaging 宿主或本地 IPC 客户端/服务端时使用本篇。相关不可信主体可能是下载的文档、远程网页内容、另一个本地应用、另一名 OS 用户、sandbox 内进程或低权限账户。要写明攻击者的起始能力,而不是把所有本地用户等量齐观。

浏览器侧 webview 行为见 `audit-client-side.md`,原生内存与加载器安全见 `audit-memory-binary.md`,更新真实性见 `audit-supply-chain.md`。

## 核心纪律(并入本领域每个 agent 的提示词)

```
- Establish the realistic local or remote-content attacker: another app, another OS user, a sandboxed child, an untrusted document, or a remote origin. Self-harm within the same account and authority is not a boundary violation.
- Paths, process names, bundle/package IDs, and claimed sender fields are not peer authentication. Use OS peer credentials, code identity, capability handles, or protected channel state.
- The native bridge or helper must authorize each operation and final resource after parsing. A trusted UI or broker does not make attacker-influenceable arguments trusted.
- OS sandbox, signing, entitlements, permissions, keychain ACLs, exported-component policy, and prompt behavior are real controls when pinned and visible.
- Use `confirmed` for source evidence plus bounded local/emulator tests. Use `needs_validation` when signing, manifest merge, OS version, device policy, installer ACL, or packaging is required but not observable.
```

## deep-link、回调与导航攻击类(subagent_type: `general`)

**自定义 scheme 与 deep-link 歧义**
其他应用或页面可以调用一个变更状态、导入数据、完成认证或选择账户的路由,而缺少当前会话与一次性回调绑定。审查 URI 规范化、重复查询字段、scheme/host/path 匹配、导出 activity/handler 策略与过期/重放链接。

**应用与账户交接混淆**
OAuth、SSO、magic-link、邀请、设备配对、无密码或支付回调可能回到错误的已安装应用、profile、租户或待处理交易。要把状态绑定到发起方应用身份、当前会话、账户、provider、操作与有效期。

**文件打开与 intent 权限混淆**
关联文件、分享 intent、拖放项、粘贴板/剪贴板记录、通知动作或打开文件事件触发特权操作,而未确认内容类型、适用时的发送者信任、当前用户意图与最终目标。

## webview 与原生桥攻击类(subagent_type: `general`)

**导航源到桥的混淆**
远程或攻击者控制的 frame 可以触达只打算给打包内容用的 JavaScript/原生桥。要在调用时以及每次导航、重定向、子 frame 创建、弹窗与错误/回退页之后校验 origin。URL 前缀检查与首次加载检查都不够。

**原生桥能力过宽**
网页内容可以经通用桥选择任意文件、命令、IPC 方法、凭证或系统动作。检查方法允许列表、规范化参数、用户/租户权限、手势/确认要求与返回值泄露。

**webview 文件与全域访问**
远程内容可以读取应用本地文件、特权自定义 scheme 或内部 origin,原因是文件访问、全域访问、混合内容、调试接口或自定义协议处理器意外打通了 origin。缺少某个限制性设置但无可达受保护内容,属加固项。

## 本地 IPC 与导出组件攻击类(subagent_type: `general`)

**IPC 对等认证缺口**
Unix socket、命名管道、XPC、Binder、D-Bus、native messaging、RPC、共享内存或回环监听接受较低信任的对端,而不检查 OS 凭证、代码身份、sandbox 令牌或信道属主。判定要求信道背后存在有意义的方法或信息泄露。

**声称主体与信道身份不符**
已认证进程/信道属于某个应用或用户,请求字段却选择另一个用户、租户、profile 或能力。要把每个方法与资源绑定到对端凭证,而不是调用方自报的标识。

**导出 service、activity、receiver 或 provider 越权**
移动组件或本地自动化端点可被外部调用,并执行本应只属于应用自身的操作。审查最终合并 manifest、intent filter、permission/signature 级别、路径授权与替身别名。打包后 manifest 状态未知时需 `needs_validation`。

**IPC 生命周期与关联混淆**
可预测的请求 ID、复用的句柄、过期信道、继承的描述符、全局可写 socket 路径或重启行为,能让一个对端应答、取消或复用另一个对端的操作。审查 socket 文件、锁、端口与共享映射的创建权限与清理。

## 特权 helper 与本地文件攻击类(subagent_type: `general`)

**特权 helper 成为糊涂代理人(confused deputy)**
低权限调用方可以选择特权命令、文件、服务、用户或系统设置,而缺少逐操作授权。审查 sudo/polkit/UAC/XPC helper 规则,并确保 helper 独立校验规范化后的参数。

**安装、更新与修复路径信任**
特权安装器/helper 在授权之后读取较低信任主体可写的 manifest、脚本、包、symlink、工作目录或修复状态。要把授权绑定到不可变内容与安全目标路径。

**本地文件属主与 TOCTOU**
应用先检查文件/路径,随后在特权读写期间跟随了替换、symlink、挂载或大小写/规范化变化。使用基于描述符的相对操作并核实最终属主。文件打开之后的解析问题归 `audit-memory-binary.md`。

**凭证存储与本地秘密边界不匹配**
keychain/keystore 条目、token 文件、备份、日志、剪贴板、通知预览或本地配置可被权限更低的另一个应用/profile/用户读取。仅同一预期 OS 账户可读的明文并不自动构成漏洞;要写明较低信任的读取者与凭证权限。

## 应用状态与设备生命周期攻击类(subagent_type: `general`)

**账户切换、登出与设备恢复泄露**
缓存数据、后台任务、小组件、通知、本地数据库、webview 存储或生物识别批准在登出/账户切换后存活,并在后续账户下出现。审查备份/恢复与多 profile 行为。

**待办动作与用户在场混淆**
通知、小组件、快捷方式、分享面板、生物识别弹窗或延迟操作授权了与展示不同的动作、在过期之后执行,或使用另一个 profile 的待办状态。要把确认绑定到规范化动作、资源、账户与当前前台状态。

## 通用手法(适用于以上各类)

- 枚举每个进程、应用组件、本地端点、URI scheme、文件关联、webview origin 与 helper。记录 OS 身份、运行时权限、调用方与可调用操作。
- 阅读最终打包输入:合并 manifest、entitlements、安装器规则、native messaging 注册、协议处理器与 ACL 创建。源码声明可能在下游被覆盖。
- 在隔离机器/模拟器上用哑 profile 与非敏感本地 fixture 验证。不要与其他用户的应用、凭证或生产服务交互。

## 验证规则(上报本领域任何发现前适用)

1. 写明攻击者起始能力、越过的 OS/应用主体、入口信道、被接受的参数或状态,以及未授权操作或泄露。
2. 确认适用的 OS sandbox、对等凭证、签名、entitlement、permission、用户同意与安装器控制。打包/运行时事实未知时需 `needs_validation`。
3. webview 桥类要同时引用导航/origin 控制与特权原生 sink。IPC 类要引用对等认证与逐资源授权。helper 类要核实最终规范化目标。
4. 本地测试保持有界,使用哑内容/账户。证明边界结果即停;不要把证明扩展为持久化或更大范围的系统修改。
5. 只有具备完整源码与本地证据链才返回 `confirmed`。返回 `needs_validation` 时写明所需的 OS、manifest、签名、ACL 或设备生命周期事实。
