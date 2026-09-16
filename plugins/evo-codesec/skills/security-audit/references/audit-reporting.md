# 验证、结构化输出、复核与报告

> security-audit skill 的验证与报告篇:覆盖阶段 3 到 6 的候选独立验证、`findings.json` 结构化输出与校验、终稿全新视角复核,以及目标中立报告(`REPORT.md`、`FINDINGS-DETAIL.md`、`NEEDS-VALIDATION.md`)的产出规范。

### 阶段 3:独立验证每个候选

在干净的 coverage-critic 通过或显式记录的提前停止之后,按稳定 fingerprint 与根因合并阶段 2 的候选与承袭的同源先前确认。把每条去重后的拟议 `confirmed` 与 `needs_validation` 候选交给一个未参与狩猎它的全新 `general` verifier(验证者)。承袭的先前确认即使来自狩猎者已排除的未变更根因,也走同样的当期验证路径。verifier 可以阅读 hunter(狩猎者)或先前的 artifact,但必须重读每处被引用的当期源码位置,并独立执行任何它能安全复现的决定性检查。

给每个 verifier 分配一个规范的小写唯一 ID,以及 `<output-dir>/agents/<verifier-id>/scratch/` 与父方拥有的 `artifacts/`。verifier 只写 `scratch/`,从不写留存 artifact。它只接收:候选本身、其关联的 coverage unit 检查与 artifact 路径、解读该路径所需的架构事实、确切相关的配套验证块、下文的提升程序块、source/local 执行边界、逐字复制的 `report-schema.json` 的 `confirmed`、`needs_validation` 与 `rejected` 分支,以及同 fingerprint 的先前记录。它不得收到另一个 verifier 的结论。

#### 候选 verifier 提示词

```text
You did not write this candidate. Try to refute it from repository source and bounded
local evidence. Do not contact deployed endpoints or external/shared services. Run
target-controlled code only inside the approved OS-enforced sandbox: no external
network, empty allowlisted environment, read-only target and tools, scratch-only
writes, and explicit low resource and wall-clock limits. If any control is unavailable,
do not execute; retain the exact missing capability as a needs_validation blocker.
Treat every scratch entry as target-controlled after execution. After the sandbox and
all its processes terminate, only trusted parent-side code may promote a predeclared
scratch-relative file, following the promotion procedure block included verbatim in
this prompt. You and target code never write retained artifacts. If promotion is
unavailable or fails, do not use that file as evidence.

1. Verify every trace and evidence file, positive line number, scope, and description.
   Confirm the first entry is a real lower-trust entrypoint and the last is the
   claimed sink or boundary effect.
2. Reconstruct the strongest source-visible validation, identity, authorization,
   normalization, lifecycle, framework, and containment controls on the path.
   Where the architecture summary names a comparable baseline, note whether it
   shares the pattern: as calibration, never as grounds to dismiss.
3. For a proposed confirmed candidate, independently reproduce the minimum observed
   result when possible. Verify inputs, interface shape, conditions, and affected
   dummy principal/resource. Do not infer a stronger result or continue after it.
4. Verify that likelihood, impact, confidence, and the proposed source fix match only
   what the evidence establishes.
5. For a proposed needs_validation candidate, decide whether the blocker is genuinely
   outside source/local observation. If source refutes the trace, reject it. If the
   missing fact remains decisive, keep needs_validation and make the local and
   owner-observed plans exact and non-destructive.
6. Preserve the fingerprint for the same source-derived root cause across every state.

Return exactly one JSON object and no surrounding prose:
{"decision": "confirmed|needs_validation|rejected", "record": { ... }}
where record exactly matches the decision's verdict branch of the schema included
in this prompt. A corrected record replaces the hunter's wording.
```

把下面这段提升程序逐字复制进每个候选 verifier 提示词:

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

verifier 只有在独立确立完整路径与有界观测结果之后,才能把 `needs_validation` 提升为 `confirmed`。当某个具体的部署或运行时事实仍未知时,把拟议确认降级为 `needs_validation`。当源码、本地行为、可见控制、缺失实质影响或不可能的先决条件驳倒该主张时,使用 `rejected`。`needs_validation` 绝不是投机想法的停放处。

父方检查每个 verifier 是否返回了同一 fingerprint,除非它识别出真正不同的根因。合并修正,把决定记录进每个关联 coverage unit,并确保每个 fingerprint 只有一条最终记录。格式错误或被散文包裹的 verifier 结果直接丢弃、不做修复;预算允许时用全新 verifier 重跑该候选,否则按不完整运行规则它仍只是 ledger(台账)中的未验证候选。

当 verifier 证据更新某条 ledger 检查时,把该检查的 `agent_id` 设为 verifier 的规范 ID,并列出其非空的仓库相对 `reviewed_paths`。unit 级 `reviewed_paths` 保持等于各检查的并集。仅源码审查使用 `method: "source"` 配 `artifact: null`。`method: "local"` 只配由可信父方代码成功提升到 `agents/<check.agent_id>/artifacts/` 之下的文件。unit 保留其原分配归属,因此归属相互独立的 hunter 检查与 verifier 检查可以共存。对由承袭先前记录播种的 `planned` unit,不存在先前归属者:复检它的 verifier 成为该 unit 的分配归属者,其复检即该 unit 的第一条检查,unit 随之带着承袭 fingerprint 进入 `candidate`。

若严格的 agent 总预算无法覆盖每个候选,把运行状态设为 incomplete,并遵循 `SKILL.md` 中的确定性预算规则。未验证候选只留在 ledger 中,不得以任何 verdict 进入 `findings.json`。

### 阶段 4:写入并校验 `findings.json`

父方把所有已独立裁决的记录写入 `<output-dir>/findings.json`,按 fingerprint 排序。包含:

- `confirmed`:以源码为根据的漏洞,具备完整本地执行证据、条件、具体修复、likelihood/impact/总体 severity 与 confidence。
- `needs_validation`:以源码为根据的候选,具备确切的未决 blocker(阻塞点)与至少一个可适用的本地或所有者观测部署计划。
- `rejected`:验证期间被证伪的以源码为根据的候选;保留它们是为了让未来运行在证据未变时不重复这条缺乏支持的主张。

写入前立即读 `report-schema.json`。它使用 `additionalProperties: false`;不要把 hunter 包装字段带进记录。保持以下 verdict 契约彼此区分:

- `confirmed` 记录使用 `root_cause`、`intended_behavior`、`conditions`、`execution`、`remediation`、`severity` 与 `confidence`;不得使用 `claimed_root_cause`、`blockers`、`validation_plan` 或 `reason`。`execution` 是目标中立的,使用目标的原生接口:按适用情况为 API/HTTP 输入、CLI 调用、库调用、消息、文件 fixture、浏览器动作、渲染出的策略或本地 harness。`observed_result` 非空且符合事实。
- `needs_validation` 记录使用 `claimed_root_cause`、`trace`、`evidence`、`blockers`,以及至少一个非空的 `validation_plan.local` 或 `validation_plan.deployment` 字段;仅当两个上下文能解决不同事实时才两者都写。不得使用 severity、execution、remediation、reason 或已确认根因。
- `rejected` 记录使用 `claimed_root_cause`、`trace`、`evidence` 与 `reason`;不得使用 severity、execution、remediation、blockers、validation plan 或已确认根因。

每条记录都有稳定 fingerprint、标题、描述与仓库相对源码路径。多步 trace 以 `entrypoint` 开始、以 `sink` 结束,`propagation` 只用于两者之间。单条目 trace 使用 `entrypoint` 或 `sink`。总体 severity 不得超过已演示的影响。

运行:

```sh
node <skill-dir>/validate-findings.cjs <output-dir>/findings.json
node <skill-dir>/validate-coverage-ledger.cjs <output-dir>/coverage-ledger.json
```

继续之前修复每个结构与语义错误。findings 校验器拒绝超过 5 MiB、1000 条顶层 findings 或 64 层嵌套的输入,并把报告的错误输出截在 100 条消息。校验器通过只证明格式与 ledger 一致性。

### 阶段 5:用全新视角复核最终记录

为每条最终 `confirmed` 与 `needs_validation` 记录并行启动一个全新的 `research` verifier。该 verifier 检查的是结构化记录而非 hunter 的文字描述,并保持在 source/local 边界内。

`quick` 运行中阶段 3 与阶段 5 合并:阶段 3 的 verifier 同时执行这些记录检查并返回最终的 schema 形态记录,每个候选得到一个而非两个全新独立复审者。其他所有 profile 保持两轮分离。任何 profile 都不得跳过对 `confirmed` 记录的独立复审。

对 `confirmed`,要求它检查:

1. 每条仓库相对 trace/evidence 路径、行号、范围与所描述的操作。
2. 真实的入口接口与确切的本地输入形态。
3. 每个条件、parser/policy 步骤、源码可见的阻止层与观测到的本地结果。
4. 受影响的 principal/resource 与已演示的影响。
5. severity 分离:现实的 likelihood、已演示的影响、总体不高于影响。
6. 修复策略与任何 `code_changes`,包括修复是否在不只是转移信任的前提下强制该不变量。

对 `needs_validation`,要求它检查:

1. 源码路径真实,且只支持所述的 `claimed_root_cause`。
2. 每个列出的 blocker 都是决定性的,且并非本地已可解答。
3. 候选指名了一个边界与一个可能的具体结果,而非泛泛的担忧。
4. 至少一个 validation plan 字段存在且确切。`local` 使用有界 fixture;`deployment` 请所有者观测某个配置、身份、路由、策略或运行时事实。不为不适用的上下文编造计划,绝不向部署发送审计流量。
5. fingerprint 与同一根因的先前/当期记录一致。

每个 verifier 恰好返回一个 JSON 对象:`{"decision":"verified","fingerprint":"..."}` 或 `{"decision":"replace","reason":"...","record":{...}}`,不带任何包裹散文。替换记录必须匹配其 `confirmed`、`needs_validation` 或 `rejected` schema 分支。阶段 5 的格式错误或被散文包裹结果按阶段 3 的同样方式处理:直接丢弃不修复,预算允许时用全新 verifier 重跑。

当阶段 5 替换把记录提升到更强 verdict(包括任何到 `confirmed` 的提升),或实质改变根因、trace、execution 输入或观测结果、已演示影响或 severity 时,不得把该替换作为最终结果应用。把完整替换交给一个新的独立 verifier,它未参与狩猎、未执行阶段 3 验证、也未提出该阶段 5 替换。新 verifier 在执行边界内复检当期源码并独立复现任何决定性本地结果,然后返回 `verified` 或另一个替换。只有经过这次全新验证才应用实质性替换。若又产生一个实质性替换,用全新 verifier 重复此过程。若预算或独立性不可得,从 `findings.json` 移除争议记录,其 ledger unit 保留为未决候选,并设 `run_status: "incomplete"` 与确切的 `incomplete_reason`。非实质的措辞或仓库行号修正,在不改变含义或证据时可直接应用。

每次应用替换后,重跑两个校验器并更新关联 ledger 决定。若最终 verifier 识别出另一个独立根因,分配新 fingerprint,并在纳入前送其通过独立候选验证。只有当每个 ledger 候选都有独立最终处置、且每条保留记录都通过阶段 5 时,才设 `run_status: "complete"`。

不要只验证 `confirmed` 记录。一条误导性的 `needs_validation` 交接会浪费所有者时间,并可能保留一个错误前提。

### 阶段 6:从最终记录产出目标中立报告

只有当 `findings.json` 中保留的每条记录都通过阶段 5 之后,才从最终记录、ledger 与 ledger 簿记中保留的 hunter `hardening`(加固)笔记派生散文。不完整运行可以报告已独立验证的记录,但必须指明每个未决 ledger 候选,且不得把它呈现为 finding。散文文件永不改变 verdict、severity、blocker 或已演示影响。

#### `REPORT.md`

写:

1. 运行 profile、范围、预算(如设定)及已用与计划的 agent 数、source ref、沙箱化 source-and-local-only 执行声明、先前运行的使用情况、显式的 deferred 与 out-of-scope 覆盖。点名列出承袭的同源确认与源码变更后的重验证。`quick`、限定范围、预算受限或不完整的运行要直白声明这是部分通过。若候选验证耗尽了严格预算,声明运行不完整并列出每个未验证 fingerprint 与关联 unit;不得把这些候选描述为 findings。若预算导致某个强制 critic 未运行,说明是哪个 critic 未运行,且不得作 clean-coverage 声明。
2. 一段简短的安全态势总结。
3. 一张 confirmed findings 表:severity、标题、受影响边界与一行观测结果。
4. 每条 confirmed finding:仓库源码位置、较低信任 principal、目标原生的有界复现、条件、实际结果、影响、优先级理由与最小源码修复。
5. 一张独立的 `NEEDS VALIDATION` 表。给出每条线索的标题、仓库 trace、确切 blocker、有界本地下一步与安全的所有者观测部署检查。不分配 severity,也不称之为已确认漏洞。
6. 独立的 hardening 笔记与正面源码模式。
7. 来自 ledger 的覆盖总结:covered、candidate、blocked 与 deferred 计数,外加重要排除项与最终 critic 结果。

不要把 rejected 记录描述为 findings。只有当它们能解释某个先前分歧或覆盖决定时才提及它们的 fingerprint。

#### `FINDINGS-DETAIL.md`

对每条 confirmed 的 `medium`、`high` 或 `critical` 记录,复制完整源码路径与目标中立本地复现:

- 有序的仓库相对 trace 与 evidence;
- 虚构 attacker/principal 与受影响的虚构资源;
- 原生输入、调用或 fixture 与确切的有界指令;
- 观测输出及其证明的安全不变量;
- 条件与遏制;
- 源码级修复与回归用例。

#### `NEEDS-VALIDATION.md`

对每条未决记录,复制源码 trace、已验证 evidence、确切 blocker、受影响边界,以及每个可适用的有界本地或所有者观测解决计划。把它们保持为无 severity 的优先级线索。不得把它们变成实弹测试指引,也不得假设缺失的部署事实。

HTTP 只是可能的原生接口之一,不是默认。库 finding 可以用函数调用,parser 用 fixture,CLI 用命令,桌面应用用 IPC 或文件动作,基础设施用本地渲染的策略。不要求目标不具备的 endpoint、外部账号或活环境。

报告与证据保持成比例。干净的运行可能没有任何 confirmed 记录。陈述该结果与剩余覆盖/验证限制,不发明 LOW findings。
