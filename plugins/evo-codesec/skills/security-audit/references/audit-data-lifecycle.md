# 数据隔离与生命周期猎取

> 角色:数据隔离与生命周期领域的漏洞猎取参考;让一条数据贯穿每一份副本与每一次状态迁移,覆盖多租户隔离、派生数据、导出备份恢复迁移与删除撤销保留。

#### 何时使用本篇

目标存储多租户或受访问控制的数据、派生搜索/索引/缓存/分析副本、签发对象链接、导出或恢复记录、迁移 schema,或承诺删除、撤销与保留行为时使用本篇。本领域让一条数据贯穿每一份副本与每一次状态迁移。端点级访问控制见 `audit-attack-classes.md`,提供方级存储策略见 `audit-cloud-deploy.md`。

大目标按主存储、缓存/搜索、对象/blob 存储、分析/日志、导出/备份、删除/撤销与迁移拆分。

## 核心纪律(并入本领域每个 agent 的提示词)

```
- A tenant or owner field on a record is not isolation. Find the query, key, path, policy, or row-level control that enforces it for each read and write path.
- Trace derived copies. Sanitized primary data can become unsafe in search, cache, analytics, export, previews, logs, replicas, and backups with different ACL and retention rules.
- Deletion and revocation are lifecycle contracts. Check current, historical, cached, indexed, exported, restored, and queued copies within the product's stated boundary.
- Privacy or retention preference is not automatically a security vulnerability. Require an explicit data-access boundary or deletion/revocation guarantee and an unauthorized reader or later operation.
- Use `confirmed` for complete source-visible lineage and bounded dummy-tenant tests. Use `needs_validation` when external storage policy, retention, CDN behavior, replica lag, or backup access is unavailable.
```

## 租户与对象隔离攻击类(subagent_type: `general`)

**缺失租户或属主强制**
读、更新、删除、列表、计数或批量查询识别了对象,却未把它绑定到已认证租户/属主,或信任 body 字段提供该身份。对比直接查找、嵌套关系、后台、admin、导入与遗留路径。

**复合键与命名空间冲突**
缓存键、对象路径、数据库唯一性、搜索文档 ID、临时文件或去重键遗漏租户或环境。即便应用记录各有其主,两个主体仍可能覆盖或取回同一逻辑键。

**策略与查询不一致**
行级策略、ORM 默认 scope、授权过滤器与 raw/绕过客户端应用着不同谓词。检查 join、聚合、别名、视图、事务、`unscoped` 或 service 客户端,以及上下文缺失的错误路径。

**blob 与签名引用越权**
对象键、附件 ID、版本 ID、共享链接或签名 URL 允许超出签发主体访问范围的操作或命名空间,或在底层 ACL 变更之后仍然有效。要绑定操作、确切对象/版本、受众、有效期与租户。

## 派生数据与泄露攻击类(subagent_type: `general`)

**搜索、缓存与索引 ACL 漂移**
主记录的 ACL 或生命周期变了,可搜索、缓存、内嵌、缩略图、RSS、预览或索引副本却未失效。除文档摄取与失效之外,还要在取回时验证过滤。

**分析、日志、追踪与诊断成为替代读者**
私有内容或凭证被发送到访问更宽、保留更久或租户混存的系统。要确认数据类别与现实读者;字段名、公开标识符与预期策略下仅运营者可见的内容不足以构成发现。

**枚举与聚合 oracle**
计数、过滤、排序、报错、唯一约束、时序、通知行为或存在性检查泄露受保护对象或账户状态。要求一个具体的机密谓词与可观测区分,而不是一般性的响应差异。

## 导出、备份、恢复与迁移攻击类(subagent_type: `general`)

**导出与备份范围扩张**
导出、快照、可携带包、报告或备份包含了其他租户、不可访问的对象字段、软删除数据、秘密值或超出请求者权限的历史。要检查选取之后的逐项授权,以及下载最终工件的授权。

**导入与恢复权限扩张**
恢复/导入绕过属主、schema、ACL、唯一性或校验规则,覆盖既有资源,或在请求者无权写入的租户重建记录。要把归档内容当不可信数据校验,并对产生的操作做授权,而不是信任先前出处。

**迁移默认值与属主混淆**
旧记录缺租户/ACL/生命周期字段、不兼容 ID 相撞,或灰度发布让新旧读取者应用不同默认值。审查回填、双读/双写、兼容、回滚与续跑迁移路径。

**备份与复制边界漂移**
加密密钥、存储账户、跨区域副本、恢复环境或支持快照的身份或租户范围比主数据更宽。源码只能确认仓内策略;托管侧访问与保留需 `needs_validation`。

## 删除、撤销与生命周期攻击类(subagent_type: `general`)

**软删除与墓碑绕过**
直接查找、搜索、关系遍历、对象链接、后台处理器或恢复无视生命周期谓词,返回或作用于已删除/已撤销记录。检查软删除标识符能否在全部引用消失之前被重新注册。

**过期授权与派生副本使用**
移除成员资格、更新 ACL、撤回同意、吊销秘密或降级角色之后,会话、缓存、订阅、任务或物化数据未失效,继续为后续操作提供授权。

**保留与排队任务越界**
主存储删除完成的同时,排队处理器、重试、导出、分析或生成物在承诺边界之外重建或保留数据。要查找幂等删除与墓碑传播。

**恢复重新引入失效状态**
备份、撤销、反删除或副本恢复带回了当前策略不再允许的数据、凭证、成员资格或权限。要对恢复出的状态重新授权,并重放快照之后做过的生命周期变更。

## 通用手法(适用于以上各类)

- 挑一条受保护记录,画出主写入、查询、缓存、索引、事件、导出、备份、删除与恢复路径。在每条边标注主体与租户。
- 经同一批本地 service 方法对比两个哑租户,再在 ACL 变更、删除、账户切换与恢复之后重复。不要使用真实用户数据。
- 从绕过客户端、后台任务、迁移、全局唯一性与缓存键入手。这些路径常遗漏交互端点携带的请求级身份。

## 验证规则(上报本领域任何发现前适用)

1. 写明攻击者或较低信任主体、受保护数据/状态、受影响的属主/租户、替代副本或操作,以及未授权泄露或变更。
2. 同时引用预期的权威(source of truth)策略与遗漏或背离它的路径。确认没有另一层在强制同一租户/生命周期条件。
3. 用本地哑租户与非敏感 fixture 证明跨范围访问或过期生命周期行为。停在最小可观测记录或操作。
4. 若依赖外部缓存、对象存储、副本、分析、备份或保留策略,分类为 `needs_validation`,并写明需属主侧观测的检查。
5. 只有具备完整血缘与具体边界影响才返回 `confirmed`。返回 `needs_validation` 时写明未决的存储、ACL、失效、保留或恢复事实。
