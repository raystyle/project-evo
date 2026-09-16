# 平台适配规范：Windows、Linux 与 macOS

> 项目骨架与工具链的三平台适配。**立项时问清目标平台矩阵**（见 base-init.md Step 2），按本篇落到 AGENTS、.gitattributes、CI 与工具选型。三平台项目实践沉淀（CI 三系统门禁、接管验收、行尾教训）[经验]。

## 一、shell 分平台约定（写进 AGENTS 操作规则）

| 平台 | shell | 禁止 |
| --- | --- | --- |
| Windows | PowerShell 7(`pwsh`) | `powershell.exe` 5.1、cmd |
| Linux | 该平台常规 shell(bash） | 依赖 Windows 专有命令 |
| macOS | zsh/bash | 同上 |
| WSL2 | 仓内 Linux 规则 | 与宿主 Windows 规则混用 |

[经验]

注意：**pwsh 7 本身跨平台**（Linux/macOS 可装），所以验证命令与工具脚本用 pwsh 写仍可三平台跑；但项目对外脚本不要假设 pwsh 存在，见「脚本载体」。

## 二、编码与行尾

- 文档与源码一律 **UTF-8**;Windows 上需兼容 PowerShell 5.1 的脚本用 **UTF-8 BOM**（无 BOM 中文 ps1 给 5.1 读会乱码） [经验]
- **`.gitattributes` 钉死行尾**（`* text=auto eol=lf` 按语言细化），不靠各机 `core.autocrlf` 配置 [经验]
- 代码中**禁止手拼路径分隔符**：用 Path API / `std::path::Path` / Node `node:path` 拼接，不写 `"a\\b"` 或 `"a/b"` 硬编码 [经验]

## 三、文档路径写法

| 场景 | 写法 |
| --- | --- |
| Windows 主开发仓的文档 | 反斜杠 `docs\adr\`（与主平台工具口径一致） |
| 跨平台协作仓/通用文档 | 正斜杠 `docs/adr/`（所有平台 shell 与 markdown 链接都认） |
| 命令示例 | 跟目标平台 shell；跨平台示例用正斜杠 + 标注 |

原则：文档路径写法**全仓统一一种**，在 AGENTS 环境节声明；同仓混用两种是断链与复制粘贴事故之源。

## 四、脚本载体：跨平台优先

| 载体 | 平台面 | 用途定位 |
| --- | --- | --- |
| **uv Python(PEP 723）** | 三平台一致 | `.tools\` 项目工具**默认载体**；一处编写三处可跑 |
| pwsh 7 脚本 | 三平台（需装 pwsh） | Windows 主场项目可用；对外交付勿假设存在 |
| ps1（5.1 兼容） | 仅 Windows | Windows 内部一次性任务；带 BOM |
| bash | Linux/macOS/WSL | Unix 侧粘合；Windows 用户跑不了，勿做唯一入口 |
| Rust/Go 单二进制 | 三平台 | 高频门禁工具升级形态（参考 reader 自身） |

沉淀铁律的跨平台版：**手拼 ≥2 次的操作升级为 uv Python 脚本，而不是平台专属脚本**。

## 五、命令示例的跨平台写法

- 同一操作给两种形态时并列标注：`# PowerShell` / `# bash`，不写「等价命令自查」
- browser-harness 管道脚本：Windows 用 here-string(`@'...'@ | browser-harness`),Linux/macOS 用 heredoc(`<<'EOF' | browser-harness ... EOF`） [实证： browser-harness SKILL 双形态约定]
- 验证命令集（verification/）以 pwsh 写，首行注明「pwsh 7 跨平台；纯 bash 环境按注释转写」或附 bash 等价块

## 六、CI 三系统门禁

- 矩阵：`windows-latest` / `ubuntu-latest` / `macos-latest`（必要时加 arm64)
- 每平台跑同一套门禁（fmt/lint/test + 文档门禁），**首跑全绿才算跨平台兼容闭环** [经验]
- **CI 文档门禁**：文档机检四件套（字符/断链/标题/lint）以与本地同口径进 CI，本地过了 CI 不过的漂移立刻现形 [经验]
- CI 门禁上岗三坑（逐个踩过） [经验]：
  1. runner **无预装**本地有的工具（uv 等需安装脚本引入）
  2. `GITHUB_PATH` 写入**仅后续步生效**，同步生效用 `export`
  3. Windows runner Python stdout 默认 cp1252，打印中文炸，脚本内重配 `sys.stdout` 为 UTF-8
- 平台差异吸收在代码与配置层（.gitattributes、条件编译、路径 API），不在 CI 层写 if/else 分叉逻辑
- Windows runner 随时退役更替（如 macos-13 Intel 退役） [经验]，矩阵选型预留交叉编译退路

## 七、接管开发验收（多机协作）

换平台接管开发时，按清单验收而非口头确认（Linux 与 mac 两路模式）：

```text
1. 仓已同步到目标 commit;工具链就位(rust/py/uv/rg/rumdl 按项目清单)
2. 门禁三件 + 文档门禁全绿(与移交方结果对账)
3. 真样本冒烟 N 路过(项目定义的最小真实输入)
4. 平台特有件验证(如 linux musl 预建、mac 交叉预建)
5. 推送后 CI 三系统绿
```

## 八、各工具平台注意速查

| 工具 | Windows | Linux | macOS |
| --- | --- | --- | --- |
| gh / git / aria2c | 三平台二进制，行为一致 | 同 | 同（arm64 注意资产选对） |
| reader | 三平台发布（musl 静态 linux 资产） | 同 | 同 [实证] |
| browser-harness | 第一优先验证 | headless 默认（无显示环境） | 支持 |
| browser-harness + WSL2 | 宿主 Windows 栈用 9223 | WSL2 镜像网络下 Linux 栈自钉端口（如 9224）避撞 | - [经验： bh SKILL 约定] |
| uv | 三平台 | 同 | 同 |
| Node/npm | 三平台；CI `npm ci` + `npm test`，矩阵 Node 22/24 [实证: browser-harness-ts] | 同 | 同 |
| `node --test` glob | Windows git-bash 必须引号：`"dist/*.test.js"`，否则目录当参数炸 [实证] | 引号同样安全 | 同 |
| spawn npm | fnm 下勿 `spawnSync('npm.cmd')`；走与 node.exe 同目录的 `node npm-cli.js` [实证] | 直接 `npm` | 同 |
| rmux | 三平台 | 同 | 同 |

## 九、立项时的平台决策（回填 base-init.md Step 2)

初始化问关键问题时必含：**「目标平台矩阵是什么？」**，单平台内部工具（只 Windows）可裁剪跨平台开销；对外交付/CI 发布产品必须三平台门禁起步。决策记进 AGENTS 环境节与对应 REQ，后续「顺便支持下 linux」类需求走 REQ 追问链，不静默扩矩阵。

## 十、全平台连接姿势（WSL 与 mesh 分工）

- **WSL 到宿主恒走回环与 interop**：`127.0.0.1` 回环 ssh 加 interop 直调（`/mnt/c` 路径互访加 `cmd`/`powershell.exe` 直调），**不走宿主 mesh IP**:WSL mirrored 网络下宿主与 WSL 共享同一 mesh 节点身份,自连被 RST 属结构性,非配置可修 [实证: 用户实弹定标 2026-09-16]
- **lan 端 mesh 地址随时随地**：lan 三端（lan-ubuntu、lan-linux、lan-mac）走 mesh 地址互访,不在此限
- **五端四机测试矩阵**：五端 = wsl（WSL 总台）、lan-win（Windows 宿主,PS 通道加 interop）、lan-ubuntu、lan-linux、lan-mac,跨四机（wsl 与 lan-win 同机两面,Linux 面与 Windows 面各自成端;用户 2026-09-16 裁定）,lan-linux2 不在矩阵（ssh 配置在但非测试基建）;全运行时装齐即成局,各仓验收按需向总台要端点测试支撑（协作协议见同市场 skill evo-herdr:herdr-flywheel）
- 各仓 AGENTS 环境节引用本口径一句,连接问题先查姿势再查配置 [经验]

## 十一、统一验收脚本载体：pwsh

- **全平台运维与验收测试脚本统一走 pwsh 一份**（五端 pwsh 7.6.6 在位）,不再各写 bash 加 cmd 加 zsh 三套 [实证: 用户定调与五端实装 2026-09-16]
- **非登录 shell PATH 兜底**：各端 pwsh 装标准路径并建 symlink（如 lan-ubuntu `/usr/local/bin/pwsh`）,非登录 shell 免全路径直达 [实证: 2026-09-16 lan-ubuntu 补装]
- **五端版本对齐判据**：验收脚本声明最低 pwsh 版本,五端 `$PSVersionTable.PSVersion` 达线才跑;不对齐先补端再跑
- 已有跨平台脚本载体（如 PEP 723 Python 经 uv）的仓不强制迁移,验收与运维面新增脚本一律 pwsh [经验]
