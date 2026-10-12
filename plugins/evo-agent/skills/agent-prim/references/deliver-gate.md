# DELIVER 门控、代记与信封

> 蒸馏自契约一、四、五a、六节。DELIVER = 定向传递;三道保险 = 门控、代记、审计。

## 门控判据

- 投前查目标格 agent_status:working/blocked 拒投(exit 1,gate_refused);idle/done/unknown 放行
- 用户令(2026-10-12):消息传递要判窗口状态,防打断在干活或被卡的格
- `--force` 强投:过门控直投,并追记审计(见下);位置恒在尾参
- 例外:**agents prompt 裸走门控但无信封无代记无审计**(自由文,最轻形);其余四域 DELIVER 全套

## --force 审计

- 每次 force 强投追记 `room/force-audit` 流:src、目标、域、id;不记正文
- 查审计:`streams view room/force-audit`

## 拒投代记与补收

- 拒投时原文意图以 OPERATE 记入 `room/deferred/<收方名>` 流(字段行加 `mode=deferred`),退出码仍 1,CTA 注明代记流名
- 收方补收:`streams view room/deferred/<自己的名字>`
- 消息不静默丢失:拒投不等于没发,意图在代记流里等你
- [实证] v2.0.0 实装:streams、shares、tasks、pipes 四域 DELIVER 均落代记;agents prompt 拒投即退不代记

## 幂等 id 与版本字段（契约 v2.3 面）

- 字段行尾可选 `id=<一次传递的标识>`:重发沿用同 id,收方按见过即弃
- 字段行尾可选 `v=1`(缺省 1):新字段只加行尾;主版本收方不识 = 不执行取用行(记 engine_fail)
- [实证] 两字段 v2.0.0 实装未落;重发防重靠收方自觉比对 seq 与正文

## 信封三行形（逐字稳定）

```
[<域>] <src> <一句话动作>
src=<host>:<pane> <域字段...>
取用:<可复制命令行>
```

- 人话行可自由;字段行与取用行禁改写(自然语言信封的失败处 = 对方改写取用命令)
- 五域字段:shares = key/name;streams = stream;tasks = cwd;pipes = addr;agents prompt 无模板
- 第三行前缀一律 `取用:`(读尾、验证、连接等旧前缀全部收编)
- 收方动作:执行取用行;失败时回信给 src(先核验,见 addressing.md)
