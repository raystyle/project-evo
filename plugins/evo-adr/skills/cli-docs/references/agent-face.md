# 乙面:CLI agent 友好五件

> 手册面、输出协议、默认帮助面、自省、裸调用面;实现模板在 templates.md 第二至五节。发现通道选型面见同插件 code-kit 的 tool-cli-agents。

## 一、--llms 手册面

- **旗标名恒 `--llms`**:裸跑出 markdown 紧凑手册,至多 120 行;`--llms-full` 全量变体(可选件,长手册与 schema 附录);`--llms --json` 出机器形(结构化命令清单或 JSON Schema)
- **手册内容序**:工具名加一句话定位、读序、命令节(子命令、关键参数、退出码)、输出契约(旗标与信封)、最小示例;版本号渲染时注入,禁手写
- **stdout、退出 0、可管道;禁交互禁分页**(无头环境安全)
- **活命令树渲染禁手维护**:手册从命令定义(clap、argparse、commander 等命令树)程序化渲染。两种实现形按仓裁:
  - 全派生形:命令树直接渲染全册(单一事实源,零漂移)
  - curated 加守卫形:语义节(输出契约、示例)手写,结构节派生,配漂移测试锁全旗标覆盖(见第四节);适用于命令树不知道的语义
- 手册与 README 分工:README 人类阅读优先(甲面),手册 agent 优先;两者互指不互抄

## 二、命令输入输出协议:旗标全家与类型化 CTA

**必选旗标七件**(全局面,每命令免费自带,不逐命令设计):

| 旗标 | 义 |
| --- | --- |
| `--filter-output <keys>` | 键路径过滤,逗号分隔,支持嵌套与数组索引(`foo,bar.baz,a[0,3]`) |
| `--format <fmt>` | 输出格式族:`toon`(人机统一缺省)、`json`、`yaml`、`md` |
| `--full-output` | 全信封输出(`ok,data,meta` 一并) |
| `--help` / `-h` | 人读帮助(见第三节) |
| `--llms` | agent 可读命令清单(见第一节) |
| `--json` | `--format json` 简写(互斥,解析层保证) |
| `--schema` | 本命令的 args、options、output 三面 JSON Schema |

**可选扩展件**(各仓按需裁剪,裁剪须显式记录在仓内文档):

| 旗标 | 义 |
| --- | --- |
| `--llms-full` | 全量手册变体(可选) |
| `--mcp` | MCP stdio 服务面(可选件,见附录) |
| `--token-count` / `--token-limit <n>` / `--token-offset <n>` | token 经济三件(计数、截限、偏移) |
| `--update` | 自升级入口 |
| `--version` | 版本 |
| `--config <path>` / `--no-config` | 选项缺省文件 |

**json 信封**(机器形统一形):

```json
{ "ok": true, "data": {},
  "meta": { "command": "<命令>", "duration_ms": 0,
    "cta": { "description": "Suggested commands:", "commands": [ { "command": "<cli> get 1", "description": "<说明>" } ] } } }
```

- `ok` 布尔恒有;成功载 `data`,失败载 `error`(字符串,人读信息;错误码走 stderr 分道,见下);`meta` 放命令、计时与 CTA 块
- **类型化 CTA**(ok 与 error 回执皆可带,agent 链式免猜免问):
  - 载体形:`commands` 数组每项为字符串或 `{command, args?, options?, description?}`;description 缺省单数 `Suggested command:` 复数 `Suggested commands:`
  - 折算:CLI 名自动前缀;args 值为 true 折 `<键>` 占位、否则字面;options 值为 true 折 `--键 <键>`、否则 `--键 值`
  - 渲染(人机同源):描述行加两空格缩进条目 `<折算后命令> - <描述>`;折算后形进信封 meta.cta,人读形由同一块渲染
- **jsonl**:列表型数据逐行对象,无信封(数据即数据)
- **错误分道**:结构化模式下错误走 **stderr 单行 JSON** `{"code":"<错误码>","message":"<人读信息>"}`(可携 cta),stdout 保纯数据;人读模式错误 `<工具名>: <信息>` 前缀 stderr
- **退出码约定**:0 成功;1 业务未命中(搜索无结果类);2 用法错误与系统错误(grep 语义族)
- **字段序稳定**:JSON 字段序与人读行序一致(序列化保插入序,禁默认字母序重排)

## 三、默认帮助面(--help)

**节序**(根与组形):头行、Usage、Commands;叶形:头行、Usage、Arguments、Options、Examples、Global Options、Environment Variables。

- **头行**:`name@version` 连接一句描述(版本在头行,注入勿手写)
- **Usage** synopsis 形:`<必选>` 加 `[可选]` 加 `<variadic...>` 加 `[options]`,有子命令加 `| <command>`;多 usage 行对齐
- **Commands**(组与根):两空格缩进,名按最长名对齐填充,后接两空格加描述;**组只列 Commands,叶全节**(组与叶双形)
- **Arguments**:位置参数逐条,名加描述
- **Options**:`--kebab, -短 <类型>` 形;枚举值竖线连列全;默认值后缀 `(default: x)`;弃用前缀 `[deprecated] `;旗标列对齐
- **Examples**:命令列对齐,`# 描述` 后缀
- **Global Options**:字典序,旗标列对齐,取值尖括号占位且枚举列全值;仅根生效的旗标只在根出
- **Environment Variables**:逐条给 `set:` 值(脱敏,只露尾四位)与 `default:`
- **描述单一真源**:所有描述文案与 schema 描述字段同源(校验层 describe 同款),禁双份手维护;描述风格 = 简短祈使短语
- 帮助输出示例见 templates.md 第四节(双语言模板各带一份:叶形与组形);帮助与 `--llms` 同出命令树(见第四节自省)

## 四、自省:三面同源

- **活命令树为唯一真源**:help、`--llms` 手册、JSON schema 三面从同一命令定义派生,禁任何一面手维护(手维护即第二真相漂移)
- **漂移守卫**(集成测试):遍历命令树,断言每个子命令与长旗标出现在 `--llms` 输出中(防新增参数漏登记);curated 实现形下此守卫必配
- **版本单源**:帮助头行与手册的版本号从载体 manifest 注入(Cargo.toml、package.json 等),与版本一致性闸同口径

## 五、裸调用面(无参进入)

无参运行是 agent 的第一探针,标准四条:

1. **必不弹交互、必不纯报错**:无参 = 导航事件,不是错误;弹交互 TUI 是 agent 陷阱,纯错误文加 usage 亦反例
2. **输出两形任选**:
   - 紧凑形(agent 首荐,token 最省):一行定位加一行指引(`--llms` 打印命令清单、`--help` 看详情)
   - 全貌形:帮助体含命令表(与第三节帮助面同体)
   - 两形都必含 `--llms` 发现面指引
3. **退出码恒 0**(裸调用非错误;exit 1 或 2 属待对齐)
4. **管道特例**:有管道模式或代码模式的仓,非 TTY 面显式分离归代码面,不算违规

实测参照:全貌形与紧凑形各有正例,弹交互与纯报错各为反例;上游产品形与旧俗形(usage 长文)属豁免参照,不改上游。示例见 templates.md 第三节末。

## 附录:可选件 mcp 与 http api

- `--mcp`(MCP stdio 服务)与 http api 两面为**可选件,非标准必选**(默认不做);需要工具编排或远程面时按仓显式引入
- 引入时:mcp 工具回执同带信封与 CTA(人机同源);http api 复用同一 schema 与信封,不再另立契约
