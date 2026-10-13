---
name: agent-s5
description: >-
  所有 agent 共享的 s5 操作面:全局文件看板(S3 形:put、get、ls、del)加全局实时流(S2 形:
  append、tail、streams)。命令面活权威 = s5 --llms(装位为舰队惯例注记,本机以 command -v s5
  实查为准;零感知凭据,钥由 config 层吃,agent 永不接触);看板 board 与频道 channel 命名约定、
  跨机轮次与研究档键空间、跨台读写规约、消息礼仪(append 落消息 tail 取阅)。与 agent-prim 分工:
  agent-prim 管投递与信号操作(herdr 已退役出操作面),共享内容引擎面一律走本 skill(含轮次三件套上云)。
  Use when 往全局看板放或取文件、跨台读写频道消息、append 落消息 tail 取阅、查 streams、
  三件套上云、跨机递轮次档或研究档时;触发词 agent-s5、s5、看板、board、频道、channel、
  put、get、append、tail、streams、全局文件、消息频道、跨台共享、上云、三件套上云、轮次档、
  跨机研究档、对象道、流道、轨迹流、S3、S2。
---

# agent-s5 - evo-agent 全局看板与实时流

**定位**:所有装了 evo 插件族的 agent 共享的看板与实时流:文件道当**全局文件看板**(跨台放取对象),流道当**全局实时流**(跨台播报与取阅,含飞轮轮次轨迹)。本 skill 教三件事:命令面去哪查、键怎么命名、怎么读写不越礼。

## 一、命令面与活权威

- **活权威 = `s5 --llms`**(手册面,每台实查;命令与参数随版本演进,本 skill 不抄命令表)
- 装位(舰队惯例注记,本机以 `command -v s5` 实查为准):win 的 `D:\ohmyenv\s5\s5.exe`、linux 的 `~/.local/bin/s5`;skill 只认 PATH(或等价显式路径);本机缺位时如实报「本机无 s5」(判例:2026-10-12 总台 wsl 缺位),安装与分发归宿主工具链 omc 与 ark,不代装不猜命令
- **零感知凭据**:钥由 config 层吃,agent 永不接触钥,禁把钥写进命令行、频道消息、看板文件或文档;三不 = 不读配置(路径都不探)、不写配置、不回显(输出与日志凭据字段零出现);命令面零凭据参数(--key、--token、--endpoint 形不出现,端点也收配置层);凭据失效症状(403、超时)上报人类或总台处置,agent 不换钥不自修;配置文件 0600、不进 git
- 双道:文件道 S3 形(`put`、`get`、`ls`、`del`,对象交换)、流道 S2 形(`append`、`tail`、`streams`,记录流)(对象道后端 garage、流道 streamstore;候 s5 首版实测定稿,实测偏差以本机 `s5 --help` 为准回填)

## 二、看板与频道命名约定

键空间与判例详见 `references/naming.md`,速览:

- 看板:`board/<工作台>/<主题>/<文件名>`(工作台名 = 舰队端名:如 wsl、lan-mac);窗格登记簿 `board/<工作台>/panes/registry`(角色到格的持久名册,总台 sweep 单写,时序见 references/naming.md)
- 频道:`channel/<频道>`(全局 kebab 短名,开新频道前 `ls` 查重)

## 三、读写规约与消息礼仪

- **看板写者拥有**:哪台放上哪台管版本,改 = 同 key 重 put 覆盖;跨台只读取用,不并发编辑他人对象;`del` 只清自己工作台前缀下的对象
- **频道 append-only**:人人可发;消息一行一事,带端名前缀(如 `[wsl] ...`);消费 = `tail` 取阅,取阅不回写、不 re-put
- 频道不做请求-应答与派单(那是 agent-rloop 轮次域,见 evo-agent:agent-rloop);只做播报、周知、留痕;大内容走看板文件,频道里放 key 引用
- 与 agent-prim 分工:agent-prim 管投递与信号操作(herdr 已退役出操作面);消息与产物的传递内置走本 skill:派单发布任务(rounds 键)、总台取结果(get 回执文本或 tail 实时流)、agents to 只递键指针(键空间见 references/naming.md)
