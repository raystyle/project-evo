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

<旗标七件与信封一行式;stderr 错误形>

## 示例

<三五个最小可拷示例>
```

## 三、信封 schema 与旗标模板

```json
// 成功:<tool> --json
{ "ok": true, "data": <载荷>,
  "meta": { "command": "<命令>", "duration_ms": 0,
    "cta": { "description": "Suggested commands:",
             "commands": [ { "command": "<cli> get 1", "description": "<说明>" } ] } } }
// 失败:stdout 无输出,stderr 单行(可携 cta 同形)
{ "code": "<错误码>", "message": "<人读信息>" }
```

- 信封 `error` 字段定形:字符串(人读信息);错误码与结构化细节走 stderr 单行形,不混载
- 人读 CTA(与 meta.cta 同源渲染,正文后):

```text
Suggested commands:
  <cli> get 1 - <说明>
```

必选旗标七件加可选扩展件全表见 agent-face 第二节;退出码 0/1/2;字段序保插入序。

裸调用输出示例(无参进入,两形任一,exit 恒 0):

```text
<cli> <一句话定位>。
命令清单:<cli> --llms;详情:<cli> --help
```

```text
<cli>@<version> <一句话定位>
Usage: <cli> <command>

Commands:
  get      <取详情>
  list     <列表>
  update   <自升级>

Global Options:
  --llms    agent 命令清单
  --help    人读帮助
```

## 四、双语言实现模板(TS 加 Rust)

TypeScript(信封、类型化 CTA 与帮助渲染):

```typescript
type Cta = string | { command: string; args?: Record<string, unknown>; options?: Record<string, unknown>; description?: string };
interface CtaBlock { commands: Cta[]; description?: string }
interface FormattedCta { command: string; description?: string }

function formatCta(name: string, cta: Cta): FormattedCta { // CLI 名自动前缀,值折占位
  if (typeof cta === "string") return { command: `${name} ${cta}` };
  const prefix = cta.command === name || cta.command.startsWith(`${name} `) ? "" : `${name} `;
  let cmd = `${prefix}${cta.command}`;
  if (cta.args) for (const [k, v] of Object.entries(cta.args)) cmd += v === true ? ` <${k}>` : ` ${v}`;
  if (cta.options) for (const [k, v] of Object.entries(cta.options)) cmd += v === true ? ` --${k} <${k}>` : ` --${k} ${v}`;
  return { command: cmd, ...(cta.description ? { description: cta.description } : {}) };
}
function renderCta(block: { description: string; commands: FormattedCta[] }): string { // 人机同源
  return [block.description, ...block.commands.map(c => `  ${c.command}${c.description ? ` - ${c.description}` : ""}`)].join("\n");
}
function stderrError(code: string, message: string, cta?: CtaBlock, name = "<cli>") { // stderr 单行
  const b = cta && cta.commands.length ? { description: cta.description ?? "Suggested commands:", commands: cta.commands.map(c => formatCta(name, c)) } : undefined;
  process.stderr.write(JSON.stringify({ code, message, ...(b ? { cta: b } : {}) }) + "\n");
}
```

帮助输出示例(叶形,renderHelp 产物):

```text
<cli>@<version> <一句话描述>
Usage: <cli> get <id> [options]

Arguments:
  id    <资源标识>

Options:
  --format <toon|json|yaml|md>    输出格式(default: toon)
  --json                          --format json 简写
  [deprecated] --out              改用 --filter-output

Examples:
  <cli> get 1          # 取详情
  <cli> get 1 --json   # 机器形

Global Options:
  --filter-output <keys>    键路径过滤
  --help, -h                人读帮助
  --schema                  三面 JSON Schema

Environment Variables:
  <CLI>_TOKEN
    set: ****abcd
    default: (unset)
```

Rust(serde 形):

```rust
#[derive(serde::Serialize)]
struct FormattedCta { command: String, #[serde(skip_serializing_if = "Option::is_none")] description: Option<String> }

#[derive(serde::Serialize)]
struct CtaMeta { description: String, commands: Vec<FormattedCta> }

#[derive(serde::Serialize)]
struct Envelope {
    ok: bool,
    #[serde(skip_serializing_if = "Option::is_none")] data: Option<serde_json::Value>,
    #[serde(skip_serializing_if = "Option::is_none")] error: Option<String>, // 人读信息;错误码走 stderr
    meta: Meta,
}

#[derive(serde::Serialize)]
struct Meta {
    command: String,
    duration_ms: u64,
    #[serde(skip_serializing_if = "Option::is_none")] cta: Option<CtaMeta>,
}

fn format_cta(name: &str, cta: &str) -> FormattedCta { // 字符串形;结构形同 TS 折算规则
    FormattedCta { command: format!("{name} {cta}"), description: None }
}
fn render_cta(b: &CtaMeta) -> String { // 人机同源:描述行加两空格缩进
    let mut s = b.description.clone();
    for c in &b.commands { s.push_str(&format!("\n  {}", c.command)); if let Some(d) = &c.description { s.push_str(&format!(" - {d}")); } }
    s
}
fn stderr_error(code: &str, message: &str) { // stderr 单行 JSON
    eprintln!("{}", serde_json::json!({ "code": code, "message": message }));
}
```

帮助输出示例(组形,renderHelp 产物):

```text
<cli>@<version> <一句话描述>
Usage: <cli> <command>

Commands:
  get      <取详情>
  list     <列表>
  update   <自升级>
```

## 五、自省与漂移守卫核对清单

- [ ] `--llms` 与 `--help` 从命令树渲染(全派生)或 curated 加漂移测试(curated 形守卫必配)
- [ ] 集成测试遍历命令树:每个子命令与长旗标出现在 `--llms` 输出
- [ ] 版本号从载体 manifest 注入,零手写(帮助头行与手册同源)
- [ ] help、`--llms`、`--schema` 三面同源,无一面手维护;描述文案与 schema describe 同源
- [ ] `--llms` 至多 120 行,stdout 退出 0,无交互无分页
