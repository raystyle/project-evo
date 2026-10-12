# hook 诊断修复面

> 四端 hook 的诊断与修复以 hst 为活权威(hst doctor 诊断、hst init 幂等修复、hst hook verify 无头验收);本面是编排与判读手册。hst 只认 PATH,分发归宿主工具链 omc 与 ark。

## 诊断

```bash
hst doctor          # 零网络体检:逐 agent 逐 check(yolo、trust、binary、state、登录态、hook 形态、状态栏)
```

- `hooks.form` check:hook 形态须为 shim 形(`~/.hst/hooks/` 自含状态写入器,用户级注册);**dead 或 absolute 任何位置 = 直接重跑 hst init**(doctor 原话)
- `trust.hooks` check:codex 侧 `~/.codex/hooks.json` 与 config.toml `[hooks.state.*]` 的 trusted_hash 键哈希须 match
- claude 会话内 `/doctor` 与 CLI `claude doctor`:设置文件被丢条(Settings Warning)与坏文件(Settings Error)的复盘面;`-p` 模式静默忽略校验失败文件,事后用 doctor 看丢了什么
- codex `codex doctor --json` 的 `config.load`:坏 TOML 即 fail

## 修复

```bash
hst init            # 幂等:hook 注册、shim 落位、状态栏(裸 init 全套;带旗标范围设计性跳过)
hst hook init       # 单面:hook 注册部署与 shim 落位(含 ~/.oma 迁 ~/.hst heal 改写)
hst hook verify     # hook 层无头验收
```

- 改 hook 脚本或配置后:重部署 -> `hst hook verify` -> `hst doctor` 的 hooks.form 复验全过
- codex trusted_hash 时效:hooks.json 内容变更后哈希不 match,codex 拒执行或提示;重信任走交互确认回填,或 hst init 重部署后确认
- kimi 双 OS 形:`~/.kimi-code/config.toml` 的 `[[hooks]]` powershell 与 bash 两套按设计共存(hst init 双形部署);config-lint 只查当前 OS 形路径,别把异 OS 形当死路径清掉

## 形态判读

- herdr 态 hook:herdr-agent-state(claude SessionStart、kimi 全事件)与 hst-state/token 并存,herdr 态是检测信号(见 evo-herdr:herdr-orch)
- goal hook 双挂:claude Stop 事件与 state 腿双挂(hst goal 的 rounds 计数与提醒注入);候 REQ-047 发布批扩四事件双挂(加 SessionEnd 加 Notification 加 PermissionRequest)[知会: 2026-10-12]
- token 腿(hst-token,secretguard):block 级 exit 2 拦截密钥外泄;state 腿只写盘不扫密钥

## 纪律

- 诊断双源:hst doctor 运行时形态 + agent-doctor config-lint 静态度(命令绝对路径缺失等),两源都过才算修完
- 不手改 shim 脚本(`~/.hst/hooks/` 由 hst init 生成,重跑即收敛,REQ-032 薄穿透)
