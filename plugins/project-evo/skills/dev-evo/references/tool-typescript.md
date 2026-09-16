# TypeScript/Node 项目工程

> 本文件 = Node/TS 仓怎么建、怎么验（运行时、tsc、测试、依赖、打包、文档即代码面）；与 tool-project.md（Python `.tools`）分栈；出仓选型纪律自含在本篇(先问标准库与平台原生)。浏览器检索见 `project-evo:super-research`；agent 脚本 workspace 见 tool-cli-agents.md。

## 一、运行时合同

- `"type": "module"`；`engines.node` 钉 `>=22`（源仓本机 Node 24.20）
- 先用 Node 内置：WebSocket、fetch、`node:sqlite`、child_process、path、test。内置能做的不进 dependencies
- 入口面一次定义：`bin`（CLI）、`main` / `types` / `exports`（库）、`files` 白名单（只出 dist、技能、资产、README、LICENSE；不出 src 与 tsconfig）

## 二、tsc 合同

家族默认编译器选项（按项目可裁，砍严选项须写理由）：

```json
{
  "compilerOptions": {
    "target": "ES2023",
    "lib": ["ES2023"],
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "exactOptionalPropertyTypes": true,
    "noImplicitOverride": true,
    "verbatimModuleSyntax": true,
    "isolatedModules": true,
    "declaration": true,
    "incremental": true,
    "skipLibCheck": true,
    "types": ["node"]
  }
}
```

含义速记：

- NodeNext 加 verbatimModuleSyntax：`.ts` 里 import 写 `.js` 扩展名
- isolatedModules：禁跨文件 const enum 一类只靠 tsc 的技巧，给以后换打包器留退路
- noUncheckedIndexedAccess：索引访问当可能 undefined

核心包用 `tsc -p tsconfig.json` 出 dist/（含 .d.ts）。不要把 CLI 或库打成单文件 bundle。

## 三、运行时依赖白名单

- dependencies 白名单制：新增 runtime 依赖走 REQ 采纳。常见现役仅 commander（CLI 解析）与 zod（环境变量与选项校验）两枚 [经验]
- devDependencies 从宽：typescript、`@types/node`、esbuild（仅浏览器 IIFE 产物需要时）
- 出仓前再问「Node 内置有没有」（阶梯:仓内到标准库到平台原生到已装依赖）

## 四、构建分面

| 面 | 工具 | 产物 | 约束 |
| --- | --- | --- | --- |
| 核心包 / CLI | tsc | dist/*.js 加 .d.ts | 类型面与运行面同源 |
| 浏览器侧车 SDK | esbuild（devDependency） | 自包含 IIFE，进 git | 产物零 runtime 依赖 |
| 协议 / IDL 生成 | 仓内 gen 脚本 | `src/generated.ts` 一类 | 禁止手改；换源后 gen 再测 |

保真判据（有上游生成物时）：与上游 diff 只允许头注释差异 [实证]。

## 五、测试

家族 TypeScript 默认载体是 **node:test**（Node 内置），不是 vitest [经验]。

```powershell
npm test   # build + typecheck:apps + node --test "dist/*.test.js"
```

硬规则：

1. 先 tsc 再测编译产物；测试与源码同目录 `src/*.test.ts`，邻模块 import 写 `.js`
2. glob **必须带引号**：`node --test "dist/*.test.js"`。Windows git-bash 裸 glob 把目录当参数解析会炸 [实证: Windows 实测,已固化进 package.json 形态]
3. 测试钉临时 HOME / 数据根，禁止碰安装态与开发态家目录 [实证]
4. 混有 `.mjs` 插件或应用时另立 `tsconfig.apps.json`：`allowJs` + `checkJs` + `noEmit`，纳入 `npm test`（`typecheck:apps`）[实证]
5. 外部依赖缺失 skip，不失败不伪造（与 flow-testing 闸门同构）

vitest 可作意图层替代；新仓无理由不跟 node:test。

## 六、路径

一律 `node:path` API 拼接，禁止手拼 `\` 或 `/`（env-platform 同款，TS 落点是 `node:path`）。

## 七、开发态 vs 安装验收

npm CLI 包有两套家，禁止混用 [实证]。

判定：包根有没有 `tsconfig.json`（`files` 不含此文件）。有 = 开发态，没有 = 安装态。

| | 开发 | 安装验收 |
| --- | --- | --- |
| 入口 | `node dist/cli.js` 或 `npm link` | `npm pack` 再 `npm install -g ./<name>-*.tgz`，只用 PATH 上的命令 |
| 数据根 | 仓内 `.xxx-dev` | 用户配置目录 |
| 禁 | 从仓库起看板或守护去看安装态数据 | `npm install -g .` 与把 link 当安装验收（包根仍能看见 tsconfig，会被判成开发态） |

给人看的验收走 pack tgz，不要 link。

## 八、环境解析与空串

坏的配置值不得在 import 时把进程打死：缺省、非法、`<=0` 回落到默认。zod `safeParse`，不 throw [实证]。

空串不是缺省：失败时 `ErrorEvent.message` 一类字段给 `""`，`?? fallback` 不触发。取值用 truthiness，不用 `??` 链 [实证]。

## 九、Windows 进程与锁

- fnm 下 `Get-Command npm` 是 `npm.ps1`，`spawnSync('npm.cmd')` 无 PATH 直调失败（status null）。改走与 `node.exe` 同目录的 `node npm-cli.js` [实证]
- 无内核锁时，时间维抢占（`stealAfterMs: 30s`）会偷活锁。只认 pid 死亡，不要用超时当锁失效 [实证]
- 事件匹配键只用稳定必填字段，不用协议里 deprecated 且 optional 的字段 [实证]

## 十、CI 与封版

CI：`fail-fast: false`；矩阵 os（ubuntu / windows / macos）乘 node（22、24）；步骤 `npm ci` + `npm test`。本地过了 CI 不过，以 CI 为准修 [经验]。

封版（接 flow-release.md）：

1. `package.json` 与 `package-lock.json` 两处 version 同步
2. `npm test` 全绿
3. `npm pack` 到 `npm install -g ./<name>-*.tgz` 到 `--version` 对版 到 安装态冒烟
4. tag

`prepack` 钩子跑 build，保证 tgz 含最新 dist。

## 十一、架构经验一条

语义层对传输无关的 Host 接口编程，CLI / 插件 / worker 复用同一套 helpers，不产生第二套语义实现 [经验]。脚本 workspace 的落位与增量供给见 tool-cli-agents.md。

## 十三、文档即代码面（TSDoc 与 API Extractor）

公开契约以导出、.d.ts 与 TSDoc 为准；API 文档是投影（总纲见 base-projection.md）。

- 契约注释必须是 `/**`（两颗星）紧贴导出声明；入口文件顶 `@packageDocumentation`；发布标签 `@public`/`@beta`/`@internal`（未标 Extractor 警告）
- 标签集合白名单 `@param`/`@returns`/`@throws`/`@example`/`@remarks`/`@link` 加发布标签;**禁 JSDoc 类型声明语法**（`@param {number} a` 这类,类型只在签名里）;示例放 `@example` 下用 fenced block 标语言（```ts）
- 摘要一段（进目录页），细节 `@remarks`；不复述类型签名；链接用 `{@link parse}` 不手写 URL
- `tsconfig.build.json`：`declaration: true`、`declarationMap: true`、`removeComments: false`（removeComments:true 会挖空 Extractor）
- 投影管线：tsc 出 .d.ts 后分流,TypeDoc 出 HTML（人）,api-extractor 出 `etc/*.api.md`（进 Git,PR 审公开面）与 `.api.json`,api-documenter 出 `docs/api/`（agent 面）
- 命令面：`npm run api`（本地 --local 更新后 git add）与 `npm run api:check`（CI 无 --local,漂移必红）
- 示例锁在 Vitest 或 node:test;类型锁 `*.test-d.ts`（`expectTypeOf`）;语言无官方 doctest,可选 vite-plugin-doctest 试点但不当唯一门禁
- 落地顺序：收窄 exports 到 补 TSDoc 与测试 到 Extractor 报告进 Git 到 TypeDoc 到 短 AGENTS 到 ADR;不要一上来给私有 helper 写注释 [经验]

## 十四、验收清单（文档面增量）

- 公开导出均有 TSDoc 与 @public 标签
- etc/*.api.md 与 docs/api/ 是生成物,无人手改痕迹
- CI api:check 绿;README/AGENTS 无第二份手写 API 真相

## 十二、验收清单

- engines.node 与 CI 矩阵下限一致
- tsc 合同就位；import 扩展名 `.js`
- runtime 依赖白名单外无暗增
- `npm test` glob 带引号；测试不碰真实家目录
- 安装验收走 pack tgz，不走 link
- 路径只经 `node:path`
- 生成物禁手改
