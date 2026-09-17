---
name: cli-docs
description: >-
  CLI 项目对外面双标准:甲面 README 标准(业界标杆 ripgrep/fzf/bat/fd 研究提炼,四节骨架:项目介绍、部署、配置、使用,人类阅读优先)
  加可拷改骨架模板;乙面 agent 友好三件(--llms 紧凑手册面至多 120 行加机器形、--json 输出信封协议与退出码与 stderr 单行错误、活命令树三面同源自省禁手维护)。
  Use when 写或改 CLI 的 README、配 --llms 手册、定 JSON 输出契约、做命令自省与漂移守卫时。
compatibility: 仓无关标准件;乙面实现随栈(clap、argparse、commander 等命令树皆可套);正文与模板零私有名
---

# cli-docs - CLI 对外面双标准:README 与 agent 面

> 仓无关标准件:人类面(README)与 agent 面(手册、协议、自省)各一套可拷改配方。发现通道与 token 经济学设计面在同插件 code-kit 的 tool-cli-agents(互引不重述),编译打包发布流水线在 build-release。正文与模板零私有名,实现出处只在仓内 diary 留档。

## 一、意图路由

| 你要做的事 | 入口 |
| --- | --- |
| 写或改 CLI 的 README(结构与写法) | `references/readme-standard.md` 加 `references/templates.md` 第一节 |
| 给 CLI 配 --llms 手册面 | `references/agent-face.md` 第一节加 `references/templates.md` 第二节 |
| 定旗标七件与信封协议(类型化 CTA) | `references/agent-face.md` 第二节加 `references/templates.md` 第三节与第四节双语言模板 |
| 做命令自省与漂移守卫 | `references/agent-face.md` 第三节加 `references/templates.md` 第五节 |
| 发现通道怎么选(--llms 与 mcp 与市场) | 同插件 code-kit 的 tool-cli-agents |

## 二、双面速览

**甲面 README 四节骨架**(研究四标杆定稿):项目介绍(定位加特性加演示)到部署(全平台安装)到配置(配置文件加环境变量)到使用(教程式示例加集成);可选尾节排障与开发与许可

**乙面 agent 三件**:

1. `--llms` 手册面:裸出 markdown 紧凑手册至多 120 行,`--llms --json` 出机器形;活命令树渲染禁手维护
2. 输出协议:**旗标七件**(--filter-output、--format、--full-output、--help/-h、--llms、--json、--schema)加信封 `{ok, data|error, meta?, commands?}`;commands 即类型化 CTA(command,args,description),ok 与 error 回执都可携带,人读形渲染 Next: 块;错误 stderr 单行 JSON,退出码 0/1/2
3. 自省:活命令树为唯一真源,help、手册、JSON 三面同源派生,漂移守卫锁全旗标覆盖

细则与模板见 references。
