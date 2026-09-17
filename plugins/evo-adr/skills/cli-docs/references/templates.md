# 模板:可直接拷改的参数化空壳

> 占位符一律尖括号形,零私有名;拷进目标仓按栈替换。

## 一、README 骨架(四节加可选尾节)

```markdown
# <tool>

[徽章:CI 状态 | 版本 | 许可]

<一句话定位:是什么、替代谁、为何快或好>

## 项目介绍

- <特性短句,一条一能>
- <特性>

![演示](<截图或终端录制>)

<基准或对比表:有实力差距才放;何时不用:边界诚实>

## 部署

<主流包管理器逐平台命令块>

```bash
<包管理器A> install <tool>
<包管理器B> install <tool>
```

升级:`<tool> <update 形>` 或包管理器;二进制校验:`sha256sum -c <资产>.sha256`

## 配置

配置文件 `<路径两制:类 Unix 与 Windows>`(不存在则首跑生成):

```text
# <键> = <默认>  <作用注释>
<完整可拷样例>
```

| 环境变量 | 作用 | 默认 |
| --- | --- | --- |
| `<ENV_VAR>` | <作用> | <默认> |

## 使用

<任务型小节,渐进:最常见任务到进阶,每节可拷命令块加输出注释>

```bash
<最常见任务命令>
# <输出示意>
```

### 与其他工具集成

<可拷配方块,逐工具>

完整选项:`<tool> --help`;agent 手册:`<tool> --llms`

## 排障(可选)

| 问题 | 对策 |
| --- | --- |

## 开发与贡献(可选)

<构建、测试、贡献指引>

## 许可

<许可>
```

## 二、--llms 手册骨架(至多 120 行)

```markdown
# <tool>

> <一句话定位>。版本 <从载体注入>。手册由命令树渲染,勿手改。

## 读序

<三五行:先看哪节、常见任务直达>

## 命令

### <子命令A>

<一行作用>
<关键旗标表或行:旗标、作用、默认>

### <子命令B>

## 退出码

| 码 | 义 |
| --- | --- |
| 0 | 成功 |
| 1 | 业务未命中 |
| 2 | 用法或系统错误 |

## 输出契约

<格式族与信封一行式;stderr 错误形>

## 示例

<三五个最小可拷示例>
```

## 三、信封 schema 与旗标七件模板

```json
// 成功:<tool> --json
{ "ok": true, "data": <载荷>, "meta": { "command": "<命令>", "duration_ms": 0 },
  "commands": [ { "command": "<tool>", "args": ["get", "1"], "description": "<下一步说明>" } ] }
// 失败:stdout 无输出,stderr 单行
{ "code": "<错误码>", "message": "<人读信息>" }
```

人读形 CTA(与上 commands 同源渲染,正文后):

```text
Next:
  <tool> get 1    <下一步说明>
```

| 旗标 | 约定 |
| --- | --- |
| `--filter-output <keys>` | 键路径过滤,支持嵌套与数组索引(`foo,bar.baz,a[0,3]`) |
| `--format <fmt>` | `toon\|json\|yaml\|md`,toon 人机统一缺省 |
| `--full-output` | 全信封 ok,data,meta |
| `--help` / `-h` | 人读帮助 |
| `--llms` | agent 可读命令清单 |
| `--json` | `--format json` 简写,互斥 |
| `--schema` | args、options、output 三面 JSON Schema |
| 退出码 | 0 成功;1 业务未命中;2 用法与系统错误 |
| 字段序 | 与人读行序一致(保插入序) |

## 四、双语言实现模板(TS 加 Rust)

TypeScript(信封与类型化 CTA):

```typescript
interface CommandSuggestion { command: string; args: string[]; description: string; }
interface Envelope { ok: boolean; data?: unknown; error?: string; meta?: { command: string; duration_ms: number }; commands?: CommandSuggestion[]; }

function ok(data: unknown, cta: CommandSuggestion[] = [], meta: { command: string; duration_ms: number }): Envelope {
  return { ok: true, data, meta, ...(cta.length ? { commands: cta } : {}) };
}
function error(message: string, code = "error", cta: CommandSuggestion[] = []): string {
  return JSON.stringify({ code, message, ...(cta.length ? { commands: cta } : {}) }); // stderr 单行
}
function renderNext(cta: CommandSuggestion[]): string { // 人读形,与 commands 同源
  return cta.length ? "Next:\n" + cta.map(c => `  ${c.command} ${c.args.join(" ")}    ${c.description}`).join("\n") : "";
}
```

Rust(serde 形):

```rust
#[derive(serde::Serialize)]
struct CommandSuggestion { command: String, args: Vec<String>, description: String }

#[derive(serde::Serialize)]
struct Envelope {
    ok: bool,
    #[serde(skip_serializing_if = "Option::is_none")] data: Option<serde_json::Value>,
    #[serde(skip_serializing_if = "Option::is_none")] error: Option<String>,
    #[serde(skip_serializing_if = "Option::is_none")] meta: Option<Meta>,
    #[serde(skip_serializing_if = "Vec::is_empty")] commands: Vec<CommandSuggestion>,
}

#[derive(serde::Serialize)]
struct Meta { command: String, duration_ms: u64 }

fn ok(data: serde_json::Value, cta: Vec<CommandSuggestion>, command: &str, started: std::time::Instant) -> Envelope {
    Envelope { ok: true, data: Some(data), error: None,
        meta: Some(Meta { command: command.into(), duration_ms: started.elapsed().as_millis() as u64 }), commands: cta }
}
// 错误走 stderr 单行;字段序 = 结构体声明序(serde 保插入序,与人读行序一致)
```

## 五、自省与漂移守卫核对清单

- [ ] `--llms` 从命令树渲染(全派生)或 curated 加漂移测试(curated 形守卫必配)
- [ ] 集成测试遍历命令树:每个子命令与长旗标出现在 `--llms` 输出
- [ ] 版本号从载体 manifest 注入,零手写
- [ ] help、`--llms`、`--llms --json` 三面同源,无一面手维护
- [ ] `--llms` 至多 120 行,stdout 退出 0,无交互无分页
