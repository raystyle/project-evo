---
id: REQ-022
title: evo-agent 第二技能 agent-s5:全局看板与频道操作面
status: implemented
priority: must
trace: tests/test_project_evo.py
---

# REQ-022:agent-s5 全局看板与频道技能

## Scenario

总台插队令(2026-10-12,用户令):evo 插件族新增 agent-s5 skill,让所有装了插件的工作台 agent 都会操作 s5。定位 = 全局文件看板(S3 道:put/get/ls/del)加全局流消息频道(S2 道:append/tail/streams)。裁定挂 evo-agent 第二 skill(客户端 evo-agent:agent-s5):工作台 agent 能力域与 agent-doctor 同插件;与 evo-herdr:s5 分工(那管跨机治理轮次协议,本 skill 管通用看板与频道日常读写)。

## Criteria

- [x] SKILL.md 三节:命令面与活权威(s5 --llms,不抄命令表;装位 win 的 D:\ohmyenv\s5\s5.exe 与 linux 的 ~/.local/bin/s5;零感知凭据,agent 永不接触钥;缺位如实报)、命名约定速览、读写规约与消息礼仪
- [x] references/naming.md:看板 board/<工作台>/<主题>/<文件名> 与频道 channel/<频道> 键空间表、跨台读写规约(写者拥有、del 不越权、append-only、tail 取阅不回写)、大内容走看板、双道选型三问、判例簿
- [x] 与 evo-herdr:s5 及 herdr 飞轮分工句(轮次三件套与研究档走 herdr:s5 协议,请求应答走派单域,本 skill 只做单向播报与文件交换)
- [x] 版图全同步:双 manifest、双市场清单(五插件十 skill)、插件 README、AGENTS、根 README、docs 地图、pre-commit、测试清单(SKILLS 守卫)
- [x] 四门禁全绿 + 分发道通(kimi 五端镜像 agent-s5;市场面随下次封版滚动)
