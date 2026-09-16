# 侦察

> 定位:security-audit skill 的侦察阶段参考。父 agent 在阶段 1 并行派出 research agent 测绘目标,汇总 architecture.md,并播种与维护确定性覆盖账本(coverage ledger)。

### 阶段 1:测绘源码并规划覆盖

父 agent 初始化 `run-metadata.json`,执行 `SKILL.md` 中严格的侦察前预算门(budget gate),然后在狩猎(hunting)开始前创建 agent 暂存根目录与共享账本。若预算门未通过,则在 metadata 中记录未完成状态,且不派出任何侦察 agent。侦察只读取目标与本地可得的构建/配置状态,不接触已部署端点、外部身份提供方、registry、broker、云 API 或其他共享服务。

并行派出多个 `research` agent。它们向父 agent 返回结构化事实,不写任何文件。

**Agent 1a:产品、技术栈与本地操作**

```text
Read the target at <target>. Do not use network access. Return:
1. Product type, users, operators, and ordinary trust-sensitive actions.
2. Languages, frameworks, build system, runtimes, and locally visible deployment models.
3. Repository-relative entry points and subsystem boundaries.
4. Exact build and test commands that could run offline with local dependencies, their expected write locations, and the target-controlled inputs they process. Do not run them during reconnaissance.
5. Comparable software or protocol visible from local documentation and dependencies. If no useful comparison is source-grounded, say so.
6. Missing local toolchains or runtime facts that limit bounded execution.
Return only source facts with repository-relative file:line references.
```

**Agent 1b:主体、权威与控制**

```text
Read all source that establishes identity, authorization, isolation, and privilege. Map:
1. Each lower-trust principal and the actions it has by design.
2. Authentication or peer identity at each entry surface.
3. Per-resource authorization and tenant/owner scope.
4. Process, browser, workload, CI, plugin, model/tool, device, or local-IPC authority.
5. Privilege changes, confirmation, revocation, recovery, and fallback paths.
6. Which controls are source-visible and which depend on an unobserved deployment fact.
Return trust boundaries and control locations with repository-relative file:line references. Do not infer live reachability.
```

**Agent 1c:入口面、副本与汇聚点**

```text
Inventory every source-visible place external or lower-trust input enters:
- HTTP/browser, RPC/message/protocol, files/archive/document, CLI/env/config, plugins/dependencies/CI, cloud events/IAM selectors, model context/tool arguments, mobile/deep-link/webview, and local IPC.
For each surface, follow major transformations, stored or derived copies, and security-relevant sinks. Record source-visible limits and parallel paths to the same effect.
Return repository-relative paths and line numbers. Be complete, but do not execute or send inputs.
```

**Agent 1d:本地执行与部署可见性**

```text
Read tests, build definitions, manifests, packaging, and maintained environment overlays. Return:
1. Small offline tests or existing fixtures that could validate trust boundaries with dummy data inside the required OS-enforced sandbox.
2. Processes that could use an isolated loopback network namespace without external or shared dependencies.
3. Commands that would fetch dependencies, publish artifacts, contact paid/provider APIs, or affect shared state; mark them prohibited for this run.
4. Deployed controls and attachments that source cannot establish and therefore require needs_validation if decisive.
5. The final active source path for each deployment mode only where the repository selects it deterministically.
6. Whether the local platform can enforce an empty allowlisted environment, no external network, read-only target/toolchain mounts, scratch-only writes, and explicit CPU, memory, process, file-size, disk, and wall-clock limits. Missing controls block target-controlled execution.
7. Whether trusted parent-side code can promote predeclared scratch files with path-confined no-follow descriptor traversal, nonblocking regular-file checks, no-follow traversal of every destination parent, exclusive regular-file destination creation, and explicit per-file and cumulative size bounds. Missing promotion controls block use of scratch files as evidence.
```

为这四个 agent 未测绘到、但实质不同的部署形态或子系统追加聚焦侦察 agent。不得静默省略:若 `SKILL.md` 的预算门拦下某个聚焦 agent,则不为它派出任何 agent,把未测绘区域播种为 `deferred` 账本单元并在 reason 中写 `budget_cannot_reserve_critics_and_validation`,然后在报告中披露该缺口。

## 前次运行输入

在选择工作之前,父 agent 读取同一仓库所有可用的历史 `coverage-ledger.json` 与 `findings.json`:

- 把每条历史记录与单元的源码位置、控制点、条件及源码派生身份同当前源码比对。
- 仅当相关源码、条件与合格证据仍然成立时,才把未变化的历史 `confirmed` 记录以相同指纹带入当前候选集。把它以 `prior_status: "prior_confirmed_same_source"` 关联到某个当前 `planned` 单元,并且只把该根因放入 hunter 排除列表。重新验证该带入记录的阶段 3 verifier 成为该单元的派工属主(assignment owner);其源码复查是该单元的第一项检查,并把单元以带入指纹转为 `candidate`。
- 当任一相关源码或条件发生变化时,构建当前计划的 `prior_confirmed_changed_source` 再验证单元。不得把该根因排除出狩猎,也不得假设历史判定仍然成立。
- 为每条历史 `needs_validation`、`deferred`、`blocked`、`out_of_scope` 及源码已变化单元构建当前工作单元。这些状态是优先输入,绝不是去重或抑制键。
- 仅当当前源码支持其追踪时,才以相同指纹带入仍然受阻的历史 `needs_validation` 记录。把它以 `prior_status: "prior_needs_validation"` 关联到某个当前 `planned` 单元;该记录保留未解除的阻塞项。重新检查该带入记录的阶段 3 verifier 成为该单元的派工属主;其复查是该单元的第一项检查,并把单元以带入指纹转为 `candidate`。把该记录纳入最终验证。
- 除非当前证据改变了失败的追踪或缺失的条件,否则把历史被拒记录视为过期主张。未变化的拒绝只抑制那条完全相同的主张,不抑制对覆盖单元的复查。
- 记录缺失或不兼容的账本,而不是把它们当作空覆盖。

在 `run-metadata.json` 中记录所用路径与源码引用。`architecture.md` 只总结覆盖后果。

## 架构摘要与配套文件选择

父 agent 综合生成 `<output-dir>/architecture.md`,硬上限约 1,000 词。包含:

1. 产品、主体、正常权威与受保护资源。
2. Agent 1a 的同类软件基线(当其有源码依据时):该同类软件接受了哪些安全权衡。用它校准投入与严重级,绝不用它否定已被证实的发现;若同类软件在现实中确实出过同类缺陷模式,这反而加强该发现。不存在有意义的同类软件时省略此条。
3. 技术栈、源码可见的部署路径与离线构建/测试限制。
4. 入口面与重要的源到汇聚点(source-to-sink)或生命周期路径。
5. 信任边界,以及每条边界上最强的源码可见控制。
6. 仓库相对起始路径。
7. 前次覆盖缺口、源码已变化与受阻的再验证目标,以及同源已确认的排除项。
8. 由 [audit-attack-classes.md](audit-attack-classes.md) 派生的简短配套文件选择摘要:选中的文件,以及需要它们的源码可见边界。

派工级的普通块、已选配套块与带原因的排除块保存在每个账本单元里,不写入 `architecture.md`。这使架构上限在大型运行下依然成立,并让精确的 hunter 提示词映射可被机器检查。

不得仅因出现某语言或依赖名就选择配套文件。选择依据是:侦察发现了该文件「何时使用本文件」小节所描述的信任敏感边界。不得仅因另一个 agent 会复查相关类就排除可见边界。

## 确定性覆盖账本

父 agent 把 `<output-dir>/coverage-ledger.json` 写成顶层 JSON 数组。按运行 profile 设定的粒度,为入口面、信任边界、子系统与适用的普通或配套攻击类的每个实质组合派生一个单元(`quick` 使用单一的全范围内子系统身份;`deep` 增加生命周期形态)。对范围受限的运行,播种范围内 surface 供派工使用,并把发现的已排除 surface 保留为 `out_of_scope` 单元,让后续全量运行能把它们转为当前工作。

每个维度都有一个人读标签,并在 `canonical_refs` 中有一个稳定的源码派生值。同一源码对象跨运行使用同一规范引用(canonical reference),即使其显示标签变化。合适的引用包括:仓库相对入口路径加导出范围、源码中定义的路由或消息身份、定义某边界的源码控制点、仓库包路径,以及精确的攻击类块引用。块引用是 `FILE.md#` 加上该文件中以粗体或标题原样写出的类名;它是与文件文本匹配的稳定标识符,不是渲染后的 HTML 锚点。对配套小节块,使用括号限定语之前的标题文本(例如 `核心纪律`)。不得通过对显示标签做小写化或 slug 化来派生引用。

无损派生 `coverage_id`:

1. 要求每个引用都是 Unicode NFC,标量值有效,含可见内容,不含控制字符、格式字符、行/段分隔符或默认可忽略码点,且两端无空白。
2. 用 RFC 3986 百分号编码其 UTF-8 字节:仅 `A-Z a-z 0-9 - . _ ~` 不转义,其余每个字节用大写 `%HH`。
3. 用 `::` 连接编码后的 `surface`、`boundary`、`subsystem` 与 `attack_class` 引用;`lifecycle` 存在时追加编码后的 `lifecycle`。

quick profile 粗化后的子系统维度使用固定规范值 `profile/quick/all-in-scope-subsystems`。引用或 ID 中不得出现波次号、agent、判定、严重级或行号。每次派工前按 `coverage_id` 的字典序排列单元。出现任何重复 ID 都必须失败。若重复 ID 带有不同的语义字段,视为规范身份冲突;绝不合并或静默覆盖。验证器同样拒绝「同一语义元组由不同规范引用表示」的情况。

每个单元记录:

```json
{
  "coverage_id": "...",
  "canonical_refs": {
    "surface": "src/router.ts#POST /users/:id",
    "boundary": "src/authz.ts#requireOwner",
    "subsystem": "packages/api",
    "attack_class": "audit-attack-classes.md#访问控制"
  },
  "surface": "...",
  "boundary": "...",
  "subsystem": "...",
  "attack_class": "...",
  "starting_paths": ["repo/relative/path"],
  "ordinary_attack_class_block": "audit-attack-classes.md#访问控制",
  "selected_companion_blocks": ["FILE.md#section"],
  "excluded_blocks": [{"block": "FILE.md#section", "reason": "..."}],
  "prior_status": "new|prior_confirmed_same_source|prior_confirmed_changed_source|prior_needs_validation|prior_deferred|prior_blocked|prior_out_of_scope|prior_covered_same_source|prior_covered_changed_source|prior_rejected_claim_changed|none",
  "attempts": [],
  "wave": 1,
  "status": "planned",
  "agent_id": null,
  "reviewed_paths": [],
  "local_checks": [],
  "result_fingerprints": [],
  "unresolved": []
}
```

`lifecycle` 为实质维度时,同时增加 `canonical_refs.lifecycle` 与人读的 `lifecycle` 字段。仅当没有适用的普通块时 `ordinary_attack_class_block` 才为 null。已选配套列表包含每个适用类,外加其配套的 `核心纪律`、`通用动作` 与 `验证规则`;`excluded_blocks` 记录每个考虑过但未选中的块,以及排除它的源码事实。

父 agent 可以增加簿记字段,但保持上述语义字段稳定。`prior_status` 中,`new` 表示存在兼容历史账本时本运行首次出现的 surface;`none` 表示没有可用兼容历史账本时播种的单元。历史 `deferred`、`blocked`、`out_of_scope` 与源码已变化单元在现已进入范围时初始化为当前 `planned` 工作。历史同源已覆盖单元在当前账本中保持可见;优先派工源码已变化单元、重要生命周期路径与精确冲突,再用 coverage critic 决定它是否需要再跑一轮。

`attempts` 是承载证据的派工的只追加归档,供 coverage critic 重开。重新派工前,把先前单元的原样 `wave`、`status`、`agent_id`、`reviewed_paths`、`local_checks`、`result_fingerprints`、`unresolved` 追加进去,并附上 critic 给出的有源码依据的 `reassignment_reason`。只有 `blocked`、`covered`、`candidate` 状态可归档。归档 attempt 与活跃单元遵守相同的状态与证据不变量,使用严格递增且小于当前 wave 的波次,并保留产出它的属主与工件(artifact)。下一次派工递增 `wave`,使用全新属主,从空的活跃证据开始。若 profile 或预算不允许再次派工,则递增 `wave`,使用属主为 null、证据为空并带停止原因的活跃 `deferred` 状态。绝不把归档属主的检查或工件复制进活跃状态。之后的活跃终态只包含新 attempt 的证据;归档保持不变。

严格执行以下状态表:

| 状态 | 单元 `agent_id` | `reviewed_paths` / `local_checks` | `result_fingerprints` | `unresolved` |
|---|---|---|---|---|
| `planned` | null | 空 | 空 | 空 |
| `not_applicable`, `out_of_scope`, `deferred` | null | 空 | 空 | 非空原因 |
| `in_progress` | 规范属主(canonical owner) | 空 | 空 | 空 |
| `blocked` | 规范属主 | 两列均为非空的属主部分证据 | 空 | 非空阻塞项 |
| `covered` | 规范属主 | 两列均非空 | 空 | 空 |
| `candidate` | 规范属主 | 两列均非空 | 非空 | 可选 |

规范 agent ID 匹配 `^[a-z0-9][a-z0-9_-]{0,63}$`,且不得是 Windows 设备名。必须小写,因此一个账本内不会出现大小写折叠别名。单元级 `agent_id` 记录派工属主。每项检查记录自己的 `agent_id` 与非空 `reviewed_paths`;单元级 `reviewed_paths` 恰为它们的并集。纯源码检查使用 `artifact: null`。本地检查要求一个常规文件(regular file):它只能由受信任的父侧代码提升(promote),且精确位于 `agents/<check.agent_id>/artifacts/` 之下。这使 hunter 与 verifier 的检查得以共存于同一单元。暂存路径、输出根目录文件、symlink、特殊文件以及属于其他检查属主的工件都不是证据。

账本即覆盖主张。架构摘要、agent 数量或「已复查 auth」这类泛泛句子都不是覆盖证据。阶段 2 只依据 hunter 结构化结果中的路径与检查关闭单元。

在播种后、每次父 agent 更新后以及阶段 6 之前,运行 `node <skill-dir>/validate-coverage-ledger.cjs <output-dir>/coverage-ledger.json`。验证器拒绝超过以下任一限度的输入:5 MiB、64 层嵌套、10,000 个单元、嵌套集合中 1,000 个条目、500,000 个遍历值;并把报告的验证错误数上限设为 100。实践中 5 MiB 字节上限大约容纳 2,000 到 5,000 个真实单元,因此它会先于 10,000 单元上限生效。在派工或作出覆盖主张之前修复所有错误。
