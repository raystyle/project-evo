---
name: agent-s5
description: >-
  工作台 agent 的 s5 全局看板与频道操作面:让每个装了插件的 agent 都会 s5。文件道(S3 形:put、
  get、ls、del)做全局文件看板,流道(S2 形:append、tail、streams)做全局流消息频道;命令面
  活权威 = s5 --llms(装位:win 的 D:\ohmyenv\s5\s5.exe、linux 的 ~/.local/bin/s5;零感知
  凭据,钥由 config 层吃,agent 永不接触);看板与频道命名约定(board 与 channel 键空间)、
  跨台读写规约、消息礼仪(append 落消息 tail 取阅)。与 evo-herdr:s5 分工:那管跨机治理轮次
  协议(三件套上云、研究档、轨迹流),本 skill 管通用看板与频道日常读写。
  Use when 往全局看板放或取文件、跨台读写频道消息、append 落消息 tail 取阅、查 streams、
  给他台递共享内容时;触发词 agent-s5、s5、看板、board、频道、channel、put、get、append、
  tail、streams、全局文件、消息频道、跨台共享。
---

# agent-s5 - evo-agent 全局看板与频道操作面

**定位**:所有装了 evo 插件族的工作台 agent 都会操作 s5:文件道当**全局文件看板**(跨台放取对象),流道当**全局流消息频道**(跨台播报与取阅)。本 skill 教三件事:命令面去哪查、键怎么命名、怎么读写不越礼。

## 一、命令面与活权威

- **活权威 = `s5 --llms`**(手册面,每台实查;命令与参数随版本演进,本 skill 不抄命令表)
- 装位(舰队惯例注记,本机以 `command -v s5` 实查为准):win 的 `D:\ohmyenv\s5\s5.exe`、linux 的 `~/.local/bin/s5`;skill 只认 PATH(或等价显式路径);本机缺位时如实报「本机无 s5」(判例:2026-10-12 总台 wsl 缺位),安装与分发归宿主工具链 omc 与 ark,不代装不猜命令
- **零感知凭据**:钥由 config 层吃,命令面零凭据参数;agent 永不接触钥,禁把钥写进命令行、频道消息、看板文件或文档
- 双道:文件道 S3 形(`put`、`get`、`ls`、`del`,对象交换)、流道 S2 形(`append`、`tail`、`streams`,记录流)

## 二、看板与频道命名约定

键空间与判例详见 `references/naming.md`,速览:

- 看板:`board/<工作台>/<主题>/<文件名>`(工作台名 = 舰队端名:如 wsl、lan-mac)
- 频道:`channel/<频道>`(全局 kebab 短名,开新频道前 `ls` 查重)

## 三、读写规约与消息礼仪

- **看板写者拥有**:哪台放上哪台管版本,改 = 同 key 重 put 覆盖;跨台只读取用,不并发编辑他人对象;`del` 只清自己工作台前缀下的对象
- **频道 append-only**:人人可发;消息一行一事,带端名前缀(如 `[wsl] ...`);消费 = `tail` 取阅,取阅不回写、不 re-put
- 频道不做请求-应答与派单(那是 herdr 域,见 evo-herdr:herdr-flywheel);只做播报、周知、留痕;大内容走看板文件,频道里放 key 引用
- 与 evo-herdr:s5 分工:跨机治理轮次(三件套上云、研究档、轮次档共享、轨迹流键空间)走 evo-herdr:s5 协议;日常看板与频道读写走本 skill,两不混用
