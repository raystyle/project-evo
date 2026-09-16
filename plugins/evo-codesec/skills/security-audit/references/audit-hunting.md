# 漏洞狩猎

> 定位:Phase 2 覆盖驱动狩猎波次的编排契约,含 hunter 提示词必备内容、核心狩猎方法、产物提升流程、本地验证边界、结构化 hunter 结果、parent 合并与账本更新、覆盖批评波次。

### Phase 2: 运行覆盖驱动的狩猎波次

parent(编排 agent)把账本中 `planned` 的覆盖单元派工给 `general` agent。用足够多的专注 hunter(狩猎 agent)覆盖这些单元,不把无关边界合并给同一个 hunter。一个 hunter 可以拥有同一子系统内紧密相关的多个单元;任何单元都不得因 agent 数量上限而被静默放弃:预算触达不到的单元必须显式置为 `deferred`,原因记 `budget_cannot_reserve_critics_and_validation`。

当预算或 profile 限制 hunter 数量时,按优先级顺序派工单元,并把排序理由记入账本。排序依据:(1)未认证或信任最低的入口面先于已认证入口面;(2)保护最有价值资源(凭据、跨租户数据、代码执行、发布权限)的边界;(3)既往运行缺口、待复验目标与已变更源码先于同源重扫;(4)其攻击类在该目标类型上历史产出过确认发现的单元先于投机性单元。并列时按 `coverage_id` 字典序破平,保证运行确定性。

启动前,parent 把已派工单元改为 `in_progress`,设定规范的小写 `agent_id`,并创建该 agent 的 `scratch/` 与 parent 持有的 `artifacts/`。hunter 阅读源码与 parent 提供的上下文,只写自己的专属 `scratch/`,并通过 Task 工具返回一个结构化结果。它们绝不写保留产物,也绝不编辑目标源码、`architecture.md`、`coverage-ledger.json`、`findings.json` 或其他 agent 的文件。

## hunter 提示词必备内容

每个 hunter 提示词按以下顺序包含这些部分:

1. 两句角色前言:hunter 的目标是在其派工单元内找出有源码依据的安全不变量失效,并且必须返回恰好一个 JSON 对象,符合本提示词末尾的结构化结果契约。
2. 逐字附上 `architecture.md`。
3. 派工到的 coverage ID、子系统、边界、仓库相对起始路径,以及来自 `coverage-ledger.json` 的每个单元的派工块映射。
4. 所选块的精确原文(逐字复制):从 `audit-attack-classes.md` 选出的每个普通攻击类块,以及从每个选中配套文件(companion)中选出的 `Core discipline`(核心纪律)、每个选中的攻击类小节、`Universal moves`(通用动作)与 `Validation rules`(验证规则)。普通块自包含,不带配套文件式的 `Core discipline`、`Universal moves` 或 `Validation rules` 小节。不要只发块名或配套文件名。
5. 显式列出被排除的普通块与配套块,每项排除都附理由。
6. 下文的核心狩猎方法,后接提升流程块。
7. 下文的核心验证规则。
8. 沿用的同源既往确认排除项,每项仅限指纹、标题与根因;以及本 hunter 不得重复覆盖的、peer(同轮其他 hunter)持有的当前 coverage ID。
9. 专属的 scratch/产物路径、安全的 agent ID、预声明的提升允许清单与字节上限,以及结构化结果契约,包括下文的结构化 hunter 结果块,以及逐字复制的 `report-schema.json` 的 `confirmed` 与 `needs_validation` 分支。

同一路径跨越多个领域时,一个提示词可以选中多个配套块,并把这些块的约束放在一起。范围是 hunter 的覆盖义务,不是重复已排除工作的许可。若出现意料之外的不同边界,把它放入 `uncovered` 返回,由 parent 创建稳定的账本单元并在下一波次派工。

#### 核心狩猎方法:每个 hunter 提示词必含

```text
## Defensive vulnerability-finding method

Your goal is to find source-grounded security invariant failures and the smallest fix,
not to expand harm beyond the boundary result. Stay within source review and bounded local execution.
Do not contact deployed endpoints, provider APIs, registries, identity systems,
message brokers, shared services, or other users. Use local dummy data only.

READ THE CODE AT DEPTH. Follow each assigned input through parsing, identity,
authorization, normalization, state, derived copies, and the final sink. Read sibling,
legacy, batch, retry, cancellation, migration, and error paths that produce the same
effect. Compare sibling controls for equivalence, not only presence, and compare what
one component guarantees with what the next component assumes.

WORK FROM A CONCRETE INVARIANT:
1. Name the lower-trust principal and starting capability.
2. Name the accepted value, action, state transition, or resource selector.
3. Locate the control that should reject, bind, isolate, limit, or revoke it.
4. Trace the exact source path after that decision.
5. Stop at the smallest affected dummy record, wrong return value, process-integrity
   effect, or locally observable shared-resource effect.
6. State a source-level change and regression case that enforce the invariant.

DEPTH BOUND: trace only paths that can reach your assigned boundary or whose
guarantees that boundary relies on. Stop a line of investigation as soon as the
invariant is settled either way, and record the result in your structured output —
a covered, candidate, or blocked disposition, or an `uncovered` entry — instead of
continuing to search.

TEST SAD PATHS AND DISAGREEMENTS. Check absent, empty, zero, negative, maximum,
over-limit, duplicate, mixed encoding, stale, revoked, reordered, concurrent,
partially migrated, failed dependency, and rollback state only where the interface
accepts them. Compare canonicalization and units at every parser or policy handoff.
For multi-step issues, treat each output as a prerequisite and do not assume a later
boundary. If any prerequisite is not established, record a blocker.

When a proposed high or critical candidate reveals a reusable root cause, search paths
owned by the assigned coverage IDs for lexical, structural, and logical variants.
Consolidate the same root cause, but establish each variant's conditions and impact
independently. Do not investigate peer-owned units. Return a variant with no current
coverage unit as `uncovered`.

USE THE NARROWEST LOCAL CHECK THAT SETTLES THE CLAIM. Target-controlled builds,
tests, processes, browsers, emulators, fuzzers, and fixture processing may run only
inside the parent-approved OS-enforced sandbox. It must disable external networking,
start from an empty allowlisted environment, expose target and tools read-only, permit
writes only to your scratch directory, and apply low CPU, memory, process, file-size,
disk, and wall-clock limits. Isolated loopback is allowed only for a local fixture.
If any control is unavailable, do not execute: return needs_validation with that exact
blocker. Prefer an existing unit test, minimal function harness, dummy-tenant service
call, small malformed fixture, deterministic race schedule, or locally rendered policy.
Do not install or fetch tools.

Record the exact input, command, limits, and minimum result. For the environment,
record only allowlisted variable names and safe non-secret values needed to reproduce
the check. Never capture the ambient environment, inherited variables, credentials,
authentication state, or unrelated host paths. The target-controlled process writes
only in scratch. After the sandbox and all its processes terminate, only trusted
parent-side code may promote predeclared scratch-relative files, following the
promotion procedure block included verbatim in this prompt. You and target code never
write retained artifacts. If promotion is unavailable or fails for decisive evidence,
return needs_validation with the exact promotion blocker.
Never stress availability, invoke a live target, use a real credential, publish an
artifact, or continue past the minimum observed effect.

A deployment, browser, provider, broker, OS, proxy, package, secret, or identity fact
outside source is not proof either way. If one such fact is decisive, return a
needs_validation record with the exact missing observation and safe owner-observed check.
```

#### 提升流程:把本提升流程逐字复制进每个 hunter 提示词

```text
Artifact promotion procedure (trusted parent-side code only):
Reference only for you: the parent performs these steps; you never perform them.

Before execution, the parent opens and retains trusted, non-inheritable directory
descriptors for the agent's scratch/ and artifacts/ roots, and records an allowlist
of expected scratch-relative artifact files plus explicit per-file and cumulative
byte limits. Never pass those descriptors to the agent or sandbox. After the sandbox
and all its processes terminate, trusted parent-side code promotes each allowlisted
file separately:

1. Validate the declared relative path: reject absolute, empty, `.`, `..`, or
   symlinked components.
2. Walk each parent component from the retained scratch-root descriptor with
   no-follow directory-relative operations; never reopen by path.
3. Open the leaf no-follow and nonblocking.
4. Verify with `fstat` that it is a regular file with link count exactly one and
   within the recorded per-file and cumulative byte limits.
5. Enforce those limits again while reading from that descriptor.
6. Copy exactly the verified size, repeat `fstat`, and reject a changed identity,
   type, link count, or size.
7. For the destination, walk every parent component from the retained
   artifacts-root descriptor with no-follow directory-relative operations; require
   each existing component to be a real directory, and create any missing directory
   exclusively before reopening and verifying it no-follow.
8. Create the leaf exclusively without following links, verify that the opened
   destination is a regular file with link count exactly one, and copy from the
   verified source descriptor without reopening either path.
9. Use equivalent race-safe APIs on non-POSIX systems.
10. Never recursively copy or glob scratch, extract an archive into artifacts, or
    open or promote a symlink, FIFO, socket, device, directory, hard-linked file,
    changing file, or file that exceeds its bound.
11. If any check is unavailable, cannot be enforced, or fails, discard the scratch
    entry; if it is decisive evidence, retain `needs_validation` with the exact
    promotion blocker.
```

#### 核心验证规则:每个 hunter 提示词必含

```text
## Candidate gate

1. A candidate needs a complete repository-relative source trace and evidence for the
   claimed root cause, including the strongest source-visible control.
2. A proposed confirmed record needs a bounded local observed result, meaningful impact
   across a stated boundary, complete conditions, and no visible preventing layer.
3. Do not strengthen a crash into code execution, ordinary work into shared availability,
   or a same-principal action into privilege gain.
4. If a required fact is not source-visible or locally observable, use
   needs_validation. Name exact blockers; do not give it severity or speculative completion.
5. A missing best practice with no affected principal/resource is excluded or hardening,
   not a finding. A candidate disproved by source is not needs_validation.
6. Use the same source-derived fingerprint for the same root cause in every state.
   It must match `^[A-Za-z0-9][A-Za-z0-9._:/@+-]*$` and must not include a line,
   wave, agent, severity, or verdict.
7. Return an empty candidate array when nothing survives these gates.
```

## 本地验证边界

本地执行用于确认,不用于扩大影响面:

- **仅限在必需的 OS sandbox(沙箱)内允许:** 使用现有依赖的离线构建;使用哑状态的隔离 loopback 进程;单元与集成测试;小型 fixture 处理;sanitizer;有界 fuzz/回归测试;确定性并发检查;用哑账号做本地 browser/emulator 测试;用哑身份做渲染清单与策略评估;被 mock 的外部或付费调用。
- **禁止:** 真实或已部署流量;向非为本隔离检查而启动的服务发请求;安装网络依赖;真实账号或凭据;生产数据;共享队列、云资源、runner、registry、签名或发布服务;对外发布;压力、饱和或成本制造;在最小哑数据边界结果之后的任何工作。

sandbox 以空环境启动,不给目标代码任何外部网络或宿主可写路径,并对每次检查(而非只对预期昂贵的检查)执行明确的低资源与低时限约束。scratch 输出在退出后仍处于目标代码控制之下,只能按 `SKILL.md` 中不跟随符号链接、路径受限、仅普通文件、有界大小的宿主侧流程提升。缺少任何 sandbox 或提升能力都不会抹掉有源码依据的候选;把确切阻塞项写进 `needs_validation`。

## 结构化 hunter 结果

返回恰好一个 JSON 对象,不带任何前后散文:

```json
{
  "units": [
    {
      "coverage_id": "one assigned ID",
      "disposition": "covered|candidate|blocked",
      "reviewed_paths": ["repo/relative/path"],
      "checks": [
        {
          "agent_id": "canonical owner of this check",
          "reviewed_paths": ["repo/relative/path owned by this check"],
          "invariant": "specific control checked for this unit",
          "method": "source|local",
          "result": "what source or the bounded check established",
          "artifact": "agents/<agent-id>/artifacts/file for local, null for source"
        }
      ],
      "candidate_fingerprints": [],
      "unresolved": []
    }
  ],
  "candidates": [],
  "hardening": ["concrete non-finding note"],
  "uncovered": [
    {
      "surface": "...",
      "boundary": "...",
      "subsystem": "...",
      "attack_class": "...",
      "starting_paths": ["repo/relative/path"],
      "reason": "why this needs its own deterministic coverage unit"
    }
  ]
}
```

每个 `candidates` 条目都符合 schema 形状,唯一差别是用 `proposed_verdict` 代替 `verdict`:

- `proposed_verdict: "confirmed"`:除 `verdict` 外,包含 `report-schema.json` 的 `confirmed` 分支要求的每个字段:`fingerprint`、title、description、`root_cause`、`intended_behavior`、有序 `trace`、`evidence`、`conditions`、目标中立的 `execution`、`remediation`、`severity` 与 `confidence`。execution 指令只描述已执行的有界本地检查。`payloads` 存放最小测试输入、fixture 或原生调用。`observed_result` 记录实际本地输出。整体严重度不得超过已观测影响。
- `proposed_verdict: "needs_validation"`:除 `verdict` 外,包含该 schema 分支要求的每个字段:`fingerprint`、title、description、`claimed_root_cause`、有序 `trace`、`evidence`、非空 `blockers`,以及至少含一个适用 `local` 或 `deployment` 步骤的 `validation_plan`。不要编造不适用的上下文。不要包含 severity、execution、remediation、reason 或已确认的 `root_cause`。`deployment` 是由属主观测的检查,不是探测在线目标的请求。

每个已派工的 coverage ID 在 `units` 中恰好出现一次。`covered` 单元需要有属主、非空 `reviewed_paths` 与 `checks`、无未决事实、无候选。`candidate` 单元拥有同样的自有证据,且是唯一携带关联指纹的状态。`blocked` 单元是一次有属主的部分审查:路径、检查与未决事实均非空,但没有指纹。所有源码路径都是仓库相对路径,绝不是绝对路径或目录穿越路径。多 entry 的 trace 从 `entrypoint` 开始、到 `sink`(汇聚点)结束,中间步骤标注 `propagation`。每个 check 都有自己的规范小写 `agent_id` 与非空 `reviewed_paths`;单元级列表恰好是这些自有路径的并集。`source` 检查使用 `artifact: null`。`local` 检查使用一个由 parent 成功提升的、位于 `agents/<check.agent_id>/artifacts/` 之下的普通文件;这允许 verifier 追加独立持有的证据,而不从 hunter 手中拿走所有权。绝不链接 scratch、输出根目录下的文件或其他 check 属主的产物。

## parent 合并与账本更新

parent 校验每个单元结果,把它映射到恰好一个已派工 `coverage_id`,且只更新该账本单元。拒绝:重复或缺失的 ID、不安全的单元或 check agent ID、带产物的 source 检查,以及未经可信 parent 侧代码提升进 check 属主 artifacts 子树的本地产物。把单元的 `reviewed_paths`、其 `checks` 写入单元的 `local_checks`、关联产物路径、候选指纹与未决事实复制进账本。把每个 hunter 的 `hardening` 列表保存在相关单元的一个 parent 记账字段里(语义字段之外),供 Phase 6 报告。失败、畸形或不受支持的结论让该单元保持 `planned` 待重新派工。未被触碰的预算/profile 单元变成未派工的 `deferred` 单元,证据为空并带原因;不要把部分证据藏进 `deferred`。更新后运行 `validate-coverage-ledger.cjs`;无效账本不能驱动下一次派工。这一逐单元契约允许一个 hunter 关闭一个单元的同时为另一个单元返回候选或阻塞项。

候选条目先按指纹合并,再按根因合并。同一根因暴露多个入口路径或影响的,是一个候选,配最强完整 trace。相关但相互独立的缺失控制用不同指纹。重复指纹记入相关账本单元,不要把重复候选送去验证。

## 覆盖批评波次

每个 hunter 波次结束后,立即把保留的调用额度花在一个全新的 `research` 波次后覆盖批评者(critic)上。它接收 `architecture.md`、含每个派工块映射的完整覆盖账本、当前候选指纹与状态、既往账本缺口摘要。它读源码,但不写也不运行目标。要求它恰好返回这个 JSON:

```json
{
  "missing_units": [
    {
      "surface": "...",
      "boundary": "...",
      "subsystem": "...",
      "attack_class": "...",
      "starting_paths": ["repo/relative/path"],
      "selected_companion_blocks": ["FILE.md#section"],
      "excluded_blocks": [{"block": "FILE.md#section", "reason": "..."}],
      "reason": "source-backed coverage gap"
    }
  ],
  "reassign_ids": ["existing-id-that-did-not-close"],
  "resolved_prior_leads": ["fingerprint"],
  "stop": false
}
```

批评者检查:未映射的入口点、未检查的并行路径、缺失的生命周期模式、选了配套类却没有对应单元、无理由的排除、没有路径/检查就关闭的单元,以及没有任何单元处理的既往 `needs_validation` 或已变更源码缺口。它提出的是覆盖建议,不是发现。`stop` 是批评者自己的判断:只有当它不接受任何 `missing_units` 且不接受任何 `reassign_ids` 时才为 `true`;是否再跑一个波次由下文 parent 的循环条件决定,而非单看 `stop`。对 `resolved_prior_leads` 中的每个指纹,parent 把关联单元或既往线索条目标记为已解决,并记录批评者的源码依据理由。

parent 拒绝超出审查范围或 source/local 边界的提议单元,为接受的单元派生规范 ID,并与现有单元去重。既往同源已完成单元可以提供证据;既往 `deferred`、`blocked`、`out_of_scope` 或已变更源码单元变成当前工作,绝不压制已接受的单元。规范 ID 冲突时宁可直接失败也不合并。对每个带活跃 `blocked`、`covered` 或 `candidate` 证据的合法 `reassign_id`,把该确切终态记录连同批评者的源码依据 `reassignment_reason` 追加进单元的 `attempts`,并在该归档中保留其属主、检查、产物、指纹与未决事实。递增活跃 `wave`;下一个 hunter 必须是全新属主,收到一个活跃证据为空的 `in_progress` 单元。hunter 的终态结果只把新证据写进活跃字段。绝不把归档属主的检查或产物复制进新的活跃尝试。下一次派工前,先排序 ID 并校验账本。在 `standard` 与 `deep` profile 下,当波次后批评者不再报告任何被接受的 `missing_units` 或合法 `reassign_ids` 且没有 `planned` 单元残留时,把单独保留的调用额度花在一个不同的最终清洁批评者上。只有该批评者也不返回任何被接受的工作时,覆盖才算完整。若它找到工作,入队并重复:波次、波次后批评者、最终清洁流程。若时间或资源迫使提前停止,把每个未触碰单元标记 `deferred`,保留批评者理由,并在报告中披露缺口。绝不把静默的波次数或 agent 数上限当作覆盖完整的证据。

运行 profile 约束这个循环。`quick` 运行恰好有一个 hunter 波次,随后恰好一次最终批评。把每个被接受的 `missing_unit` 加入当前账本,标记 `deferred`,原因 `quick_profile_final_critic`。对每个携带证据的合法 `reassign_id`,把活跃终态归档进 `attempts`,递增 `wave`,并把活跃状态置为未派工的 `deferred`,证据为空,原因 `quick_profile_final_critic`。不再发起第二个 hunter 波次或另一个批评者。在限定范围(scoped)的运行中,批评者仍会报告它注意到的范围外缺口,但 parent 把它们记为 `out_of_scope` 并附批评者理由,而不是派工。上文提前停止规则是同一机制:`quick` 是预先声明的提前停止,不是覆盖完整的证据。

预算以同样方式约束循环。每波次派工前,把剩余预算与该波次的 hunter 数量、验证保留额、紧随的波次后批评者、保留的最终清洁批评者相比较(`quick` 只保留其单个最终波次后批评者)。按优先级顺序取单元,收缩 hunter 波次以适配预算。若这些强制保留额放不下,该波次不发任何 hunter,把其 planned 单元标记 `deferred`,原因 `budget_cannot_reserve_critics_and_validation`。批评者提议的单元进入同一优先级队列,而不是扩展预算。若存续候选超过验证保留额,遵循 `SKILL.md` 的不完整运行规则:停止狩猎,按指纹顺序验证,未验证单元保留为未决候选,绝不把它们呈现为发现。
