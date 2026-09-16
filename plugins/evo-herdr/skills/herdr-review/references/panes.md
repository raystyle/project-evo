# 评审窗格

> 评审会话的挂位、命名、查看与对话检索。命令均 2026-09-16 本机实证;herdr 命令语法活权威是本机直跑 `herdr --skill`。

## 一、挂位与命名

- **挂位**:工位 tab 内右侧格,与开发格同 tab 同屏(实证布局:开发格 wT:p1 加评审格 wT:p2 同 tab wT:t1)。总台切 tab 即见工位干活与评审对线双屏
- **cwd**:评审格用用户级 home cwd(非任一仓内),一格格跨仓收件,先后服务 hst_rs、ark_rs、OfficeCLI、oxvg [实证: hst trace 会话史]
- **命名**:命名评审格(如 hst-codex-review、evo-codex-review);命名后 live 名可作派单地址,编号会漂移、名不漂移,仍以 `herdr agent list` JSON 实查为准 [实证: 2026-09-16 agent list 见命名格]

## 二、检测与带起(无格则建,有格直接对话)

> 本节命令 2026-09-16 本机实证(project-evo 工位 wV:p1 右侧原无格,全流程跑通)。检测用 `--pane` 固定工位格,勿用 `--current`(按焦点格解析,焦点在别 tab 时查错对象)。

```bash
# 1 检测:工位格右侧有没有格(neighbor 落回自己即无右侧格)
herdr pane neighbor --direction right --pane <工位格>

# 2 无格则建:右分 40%,cwd 用用户级 home(跨仓收件形态)
herdr pane split <工位格> --direction right --ratio 0.4 --cwd /home/ray

# 3 起名驻场:kind codex 起在新建格,命名即地址(等待交互就绪,默认 30s)
herdr agent start <评审格名> --kind codex --pane <新格id>

# 4 有格(或建完)直接对话:prompt 派评审单,read 收回执(细则见 herdr-flywheel)
herdr agent prompt <评审格名> "<评审请求>" --wait --timeout 300000
herdr agent read <评审格名> --source recent-unwrapped --lines 200
```

- 顺序纪律:yolo 先于驻场(用户级 codex yolo 已在位即可直接起;新机先走 herdr-flywheel 带起节)
- 已有可用格(状态 idle 或 done)跳过 2、3 直接 4;working 可插队但回执按 commit sha 甄别,blocked 问用户

## 三、查看

```bash
herdr agent list                       # 评审格全景(名、pane_id、agent_status、cwd、标题)
herdr pane list                        # 全窗格布局与同 tab 关系
herdr pane read <pane_id>              # 直接看某窗格当前输出
herdr pane layout                      # 窗格几何
herdr agent read <pane_id>             # 评审格输出(收件面,细则见 herdr-flywheel)
```

- pane 标题即任务线索(实证:「评审 hst_rs 未推 main 的七笔提交」),扫 agent list 就知评审格在忙什么
- 勿关非自建窗格;评审格常驻,不随单轮评审开关

## 四、对话与轨迹检索(hst trace 六视图)

```bash
hst trace sessions --project <仓路径>                    # 该仓各 agent 会话史
hst trace search "review" --agent codex --project <仓>    # 正则检索 patch、file、双意图四域
hst trace agent codex --project <仓路径>                  # codex 在该仓的操作块时间线
hst trace file <文件> --project <仓路径>                  # 单文件轨迹:谁、何时、基于什么意图改的
```

- 评审对话存证与会话史复盘走 trace,不靠截屏;双侧开发仓(Windows 加 WSL)注意各侧各库,跨侧检索先 `hst trace sessions` 探明在册面
- 意图操作块(blocks/timeline)按 operation_id 归组,一轮评审一段,复盘对账用

## 五、坑

- 带起顺序纪律(yolo 先于驻场)见本篇第二节;派单等待与收件坑见 herdr-flywheel 的 SKILL 与 pitfalls
- 新评审会话首启可能弹 hooks 审查屏(`7 hooks need review` / `Press t to trust all`):先 trust(t)再 Esc 回工作区,未处理的审查屏会吞派单 [实证: hst_rs settle 白名单实录]
- 评审会话长对话跑久了 scrollback 会涨,读不全时长响应兜底请对方落临时 md 文件回路径(见 flywheel 回执节)
