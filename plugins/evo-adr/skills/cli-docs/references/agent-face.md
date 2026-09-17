# 乙面:CLI agent 友好三件

> 手册面、输出协议、自省同源;实现模板在 templates.md 第二至四节。发现通道选型面见同插件 code-kit 的 tool-cli-agents。

## 一、--llms 手册面

- **旗标名恒 `--llms`**:裸跑出 markdown 紧凑手册,至多 120 行;`--llms --json` 出机器形(结构化命令清单或 JSON Schema)
- **手册内容序**:工具名加一句话定位、读序、命令节(子命令、关键参数、退出码)、输出契约(旗标七件与信封)、最小示例;版本号渲染时注入,禁手写
- **stdout、退出 0、可管道;禁交互禁分页**(无头环境安全)
- **活命令树渲染禁手维护**:手册从命令定义(clap、argparse、commander 等命令树)程序化渲染。两种实现形按仓裁:
  - 全派生形:命令树直接渲染全册(单一事实源,零漂移)
  - curated 加守卫形:语义节(输出契约、示例)手写,结构节派生,配漂移测试锁全旗标覆盖(见第三节);适用于命令树不知道的语义
- 手册与 README 分工:README 人类阅读优先(甲面),手册 agent 优先;两者互指不互抄

## 二、命令输入输出协议:旗标七件与类型化 CTA

**旗标七件**(全局面,每命令免费自带,不逐命令设计):

| 旗标 | 义 |
| --- | --- |
| `--filter-output <keys>` | 键路径过滤,逗号分隔,支持嵌套与数组索引(`foo,bar.baz,a[0,3]`) |
| `--format <fmt>` | 输出格式族:`toon`(人机统一缺省)、`json`、`yaml`、`md` |
| `--full-output` | 全信封输出(`ok,data,meta` 一并) |
| `--help` / `-h` | 人读帮助 |
| `--llms` | agent 可读命令清单(见第一节) |
| `--json` | `--format json` 简写(互斥,解析层保证) |
| `--schema` | 本命令的 args、options、output 三面 JSON Schema |

**json 信封**(机器形统一形):

```json
{ "ok": true, "data": {}, "meta": { "command": "<命令>", "duration_ms": 0 },
  "commands": [ { "command": "my-cli", "args": ["get", "1"], "description": "<下一步说明>" } ] }
```

- `ok` 布尔恒有;成功载 `data`,失败载 `error`;`meta` 放命令与计时
- **类型化 CTA**:`commands` 数组每项 `{command, args, description}`,ok 与 error 回执都可携带;agent 链式操作免猜免问,拿建议直接拼下一命令
- **人读形 CTA**:正文后渲染 `Next:` 块逐条列命令加描述(与 json 形的 commands 同源,非双份)
- **jsonl**:列表型数据逐行对象,无信封(数据即数据)
- **错误分道**:结构化模式下错误走 **stderr 单行 JSON** `{"code":"<错误码>","message":"<人读信息>"}`,stdout 保纯数据;人读模式错误 `<工具名>: <信息>` 前缀 stderr
- **退出码约定**:0 成功;1 业务未命中(搜索无结果类);2 用法错误与系统错误(grep 语义族)
- **字段序稳定**:JSON 字段序与人读行序一致(序列化保插入序,禁默认字母序重排)

## 三、自省:三面同源

- **活命令树为唯一真源**:help、`--llms` 手册、JSON schema 三面从同一命令定义派生,禁任何一面手维护(手维护即第二真相漂移)
- **漂移守卫**(集成测试):遍历命令树,断言每个子命令与长旗标出现在 `--llms` 输出中(防新增参数漏登记);curated 实现形下此守卫必配
- **版本单源**:手册与 help 的版本号从载体 manifest 注入(Cargo.toml、package.json 等),与版本一致性闸同口径
- schema 形:`--llms --json` 出命令清单或 JSON Schema(一族工具同构时 agent 换工具零学习,设计面见 tool-cli-agents 四面 schema)
