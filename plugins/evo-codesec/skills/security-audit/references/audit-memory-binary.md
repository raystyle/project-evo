# 内存安全、二进制与内核猎取

> 角色:内存安全、二进制与内核领域的漏洞猎取参考;当目标在内存不安全或特权上下文中处理不可信字节时使用。

#### 何时使用本篇

当目标在内存不安全或特权上下文中处理不可信字节时使用本篇:C/C++/Objective-C、Rust `unsafe`、FFI(外部函数接口)、内核模块与驱动、解析器与解码器、网络守护进程、固件、二进制加载器、语言运行时与 JIT。协议授权与状态机逻辑见 `audit-protocols-rpc.md`;本篇负责进程完整性、内存安全、ABI 边界与加载器行为。

从 Phase 1 中挑选相关攻击类,大目标按解析器、分配器/生命周期、FFI、并发、加载器、运行时或特权接口拆分。

## 核心纪律(并入本领域每个 agent 的提示词)

```
- Re-derive every bound and lifetime from attacker-controlled inputs and all callers. Validate against the worst accepted case, not a typical test vector.
- A panic, sanitizer finding, or crash proves a defect only when a realistic untrusted input reaches it. Do not infer memory corruption, code execution, or shared availability impact from a label alone.
- Validate in a local harness with sanitizers, deterministic concurrency tests, existing fuzz targets, and debugger-assisted fault classification. Stop after proving the violated invariant and observable impact; do not develop post-corruption techniques.
- Assembly, JIT code, custom allocators, intra-object accesses, and foreign libraries can escape sanitizer coverage. Identify which relevant instructions are instrumented.
- Classify as `confirmed` only after source evidence and bounded local validation establish the defect and effect. Use `needs_validation` when ABI, allocator, architecture, feature, deployment, or reachability facts remain unknown.
```

## 边界、整数与表示攻击类(subagent_type: `general`)

**越界读或越界写**
长度、偏移、索引或终止符在缺少正确边界的情况下触及固定或已分配缓冲区。在前缀、对齐、填充与终止符之后重新计算可用余量。同时检查源与目标的容量,以及是否存在先信任声明长度、随后按其读过短输入的情形。

**整数溢出、下溢、截断与符号性**
在分配、拷贝、循环、索引与指针运算之前审查攻击者可控算术。高命中模式包括 `b > a` 时的 `a - b`、`count * element_size`、接近类型上限的加法、负值转无符号、64 位长度收窄进 32 位字段,以及 `-1` 这类哨兵值变成大尺寸。确认后续使用的是哪个经过校验的表示。

**单位与指针深度混淆**
代码混用字节、元素、码元、页、字、线上单位或嵌套指针的元素大小。在解析、校验、分配、API 边界与拷贝各处比对单位。边界检查若与分配用同一个错误单位,依然是错的。

**未初始化或部分初始化数据**
缓冲区、填充、结构体字段或 vector 容量在初始化之前被返回、比较、哈希、序列化或跨信任边界传递。要求存在可观测的消费者与现实的输出长度;栈分配本身不构成泄露。

## 生命周期、类型与并发攻击类(subagent_type: `general`)

**释放后使用(use-after-free)、失效视图与重复释放**
所有者被释放时,回调、等待队列、定时器、迭代器、借用的切片或缓存的裸指针仍可能使用它。审查每一条错误、取消、关闭与 realloc 路径。对嵌入式通知锚点,每条释放路径都必须排空或摘除全部观察者。

**类型混淆与非法向下转型**
标签、vtable、union 判别式、对象种类或外部句柄的检查方式与随后读取的表示不一致。寻找未检查的 dynamic cast、复用后的过期标签,以及被校验元素与被消费元素不一致的序列化类型。在本地确认一次错误类型的读或写即可,测试不要扩展到被违反不变量之外。

**引用计数与所有权竞争**
非原子的 retain/release、检查之后无锁使用,或线程间所有权不一致,都可能让对象在访问期间被释放或修改。对比快速、错误、关闭与兼容路径是否遵守同一套锁与所有权规则。

**共享状态竞争与 TOCTOU**
并发解析流、全局缓存、惰性初始化、信号处理器与资源清理都可能让先前建立的边界、策略或指针失效。用可复现的本地调度、屏障或 thread sanitizer 验证竞争;没有安全相关状态迁移的假想交错保持 `needs_validation`。

**锁序、死锁与饥饿**
外部可达操作以不一致顺序获取锁,或在回调与阻塞 I/O 期间持锁。只有当有界输入能让共享进度停摆时才按可用性上报;否则作为并发缺陷记录待修。

## FFI 与 ABI 攻击类(subagent_type: `general`)

**指针长度与所有权契约不匹配**
调用方与被调方对谁来分配、释放、pin 住或修改缓冲区、指针有效期多长、长度单位是字节还是元素各执一词。追查每条 `extern`、CGo/JNI/Python/native 绑定与生成包装器的两侧。检查 null、零长度、别名与回调驻留。

**布局、对齐与枚举不一致**
外部代码收到的 struct、位域、紧凑记录、回调签名、整数宽度、枚举或调用约定随架构或编译标志而异。核对 `repr`、packing、对齐、字节序与 ABI 特有类型。仓内声明不一致可在本地确认;外部实现不透明时需 `needs_validation`。

**栈展开、异常与线程亲和性违规**
异常或 panic 跨越禁止展开的 ABI、回调在清理之后仍运行,或要求单一运行时线程的 API 在别处被调用。审查错误转换与取消逻辑。在认定影响之前先确认进程是中止还是状态被破坏。

## 二进制加载与运行时攻击类(subagent_type: `general`)

**库、插件与可执行文件搜索顺序信任**
特权进程从较低信任主体可写的路径加载库、插件、运行时镜像或辅助程序,或经攻击者可影响的工作目录或环境解析裸名称。对比预期安装属主与每条回退及兼容搜索路径。用户向自己的进程加载自己的插件不构成边界违规。

**缺失工件身份或签名绑定**
加载器校验了一个文件或元数据记录,却映射了另一个镜像,原因是路径解析、文件替换、架构切片或内嵌资源未与该检查绑定。供应链真实性归 `audit-supply-chain.md`;本类只覆盖本地校验到映射之间的缺口。

**畸形二进制元数据与重定位处理**
偏移、计数、节、重定位、符号、字节码或调试元数据在范围、重叠与表示检查之前就被信任。用有界的本地 fixture 与 sanitizer 测试解析器。把内存破坏与被安全拒绝的畸形文件区分开。

**JIT 与生成代码一致性**
校验器、解释器、优化器与生成代码对类型、边界、副作用或生命周期的认知不一致。用同一本地输入对比优化与未优化路径。确认进程完整性层面的效果;仍在语言语义之内的输出差异不是发现。

**卸载、重载与清理安全**
活跃函数指针、回调、工作线程或数据视图在模块卸载或运行时重置之后仍然存活。像审查启动一样细审关闭与加载失败的清理路径。

## 内核与特权接口攻击类(subagent_type: `general`)

**用户拷贝边界与重复读取**
syscall、ioctl、驱动或内核解析器从用户内存得出一个可信事实,随后再次读取同一可变地址。整份请求一次性拷贝,或对后一次拷贝重新校验。同时审计每个 user-copy 原语的尺寸、方向与访问检查。

**特权对象生命周期与分发一致性**
外部可达对象存在不配对的 retain/release、无观察者排空的清理、未检查的选择器/表索引,或遗漏守卫的重复兼容路径。逐条并排对比每个分发与释放路径。

**授权不足的高权限接口**
设备节点、管理 socket、辅助程序或管理 API 只校验形状,不校验调用方对该资源的权限。先确立接口的实际属主与可达性;权限或 sandbox 策略在仓外时记 `needs_validation`。

## 通用手法(适用于以上各类)

- 审计同一 source 到 sink 形态的修复代码与重复路径。某个调用方、架构、协议角色、特性开关或兼容路径上的检查保护不了它的兄弟路径。
- 为每个解析器或 FFI 边界建一张表:接受的长度/类型、被校验的表示、分配属主、消费者、线程与清理。多数原生发现就是这张表里的一处不一致。
- 使用现成语料与本地生成的小型边界 fixture。保存确切的 sanitizer/运行时输出与触发它的输入属性;避免大规模资源消耗与任何真实在线目标。

## 验证规则(上报本领域任何发现前适用)

1. 确立现实的不可信入口与确切操作,证明其违反边界、类型、生命周期、ABI、并发、加载器或权限不变量。
2. 分类可观测效果:非法读、非法写、失效别名、错误对象、未初始化输出、未授权镜像加载、死锁或安全的进程终止。不要宣称超出观测的更强效果。
3. 用能复现该效果的最窄本地 harness、现有测试、sanitizer 或 fuzzer。核实 sanitizer 对致错操作的覆盖,并记录架构/编译条件。
4. 并发类用确定性调度或 sanitizer 轨迹。二进制加载类要证明被校验身份与被映射身份不同,并指认较低信任的写入者。
5. `confirmed` 发现必须附带确切输入、源码追踪与观测结果。存在具体未决的可达性、ABI、编译、部署或运行时事实时返回 `needs_validation`,并写明所需的有界检查。
