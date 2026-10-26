---
patterns: [agent 友好, agent-friendly, llms 手册, --llms, CTA, 信封, 帮助面, 自省, 裸调用, 发现通道, token 经济学, dev-cli, 原生]
---

## dev-cli Agent 原生友好 CLI 指导

- 手册面:`--llms` 紧凑手册(至多 120 行,首行 = 名与一句话定位,尾行 = 示例)
- 输出协议:`--json` 机器形信封 `{"ok":true,"data":{...},"meta":{}}`;错误 stderr 单行 JSON 带 code/message/cta,stdout 恒纯数据;CTA 统一『下一步:』前缀
- 帮助面节序:定位 > 动词文法 > id/示例 > 旗标说明;退出码三态 0/1/2;裸调用 = VIEW 恒 exit 0(agent 可放心探测)
- 自省:活命令树三面同源(--help 人读、--llms 手册、--json 机器形皆从单一命令注册表派生,禁手维护第二份清单);漂移守卫进 CI
- 发现通道与 token 经济学:手册面渐进披露,长文档进 --full-output 不进默认面
