---
name: build-release
description: >-
  仓无关的编译打包发布流水线指导:按仓库清单形态分型给配方(go/Cargo/package/pyproject/autotools/纯文档插件六型),
  每型含构建矩阵、测试闸、打包与 sha256 边车、gh release 直发、rclone 双段播种、自升级适用判据与元数据对齐;
  公共契约节管仓侧全链自包、镜像恒 rclone、护栏三件(一致性闸、零上传红灯、dispatch 补推口)。
  Use when 搭或改 CI/CD 流水线、编译打包、发 Release、推镜像、rclone 播种、流水线排障时。
compatibility: 需 PATH 上的 gh(发 Release)与 rclone(推段);GitHub Actions 为流水线载体;镜像端点与桶按目标环境 Secrets 配置
---

# build-release - 编译打包发布流水线指导

> 标准通用件:任何仓按清单形态对号入座拿配方,正文与模板只含参数化占位符,不含任何具体环境私有名。**三段式正源**:本地编译和打包(编译产物与离线包都在本地出:二进制交叉/实机编译,npm 形 `npm pack`、py 形 `python -m build` 本地出包)到 GitHub 产物发布(gh release 直发)到 CI/CD Action 自动播种 R2;编译与打包面不在 CI,CI 面管自动播种与随仓测试岗。**边界**:CI 不可产的大件分发不属本面。封版操作面(封版件、tag 触发、发布验收)在同插件 doc-gov 的 flow-release,互引不重复。

## 一、类型路由:什么样的项目,怎么做

按仓根清单与产物形态分型,先定型号再取配方:

| 仓形态 | 型号 | 配方要点 |
| --- | --- | --- |
| 有 `go.mod` | go 形 | `CGO_ENABLED=0` 交叉六目标(linux/darwin/windows 各 amd64 加 arm64) |
| 有 `Cargo.toml` | rust 形 | 三岗矩阵(linux 本职、win-gnu 交叉、mac arm64);自升级适用判据必答 |
| 有 `package.json` | npm 形 | `npm ci` 后 `npm pack` 离线 tgz,files/exports 控内容 |
| 有 `pyproject.toml` | py 形 | `python -m build` 出 wheel 加 sdist;C 扩展换 cibuildwheel |
| autotools/C++ 源码树 | native 形 | 自含静态构建加跨宿主容器闸 |
| 纯文档/插件仓,无二进制 | manifest 形 | 不编不播,只发清单与市场条目 |

每型配方的七要素(构建矩阵、测试闸、打包与边车、发布、播种、自升级判据、元数据对齐)见 `references/type-recipes.md`。

## 二、公共契约速览(七铁则)

1. 三段式:本地编译和打包(测试闸先行,二进制与离线包都在本地出)到 gh release 直发到 Action 自动播种;发布动作零手工过渡形态
2. 镜像恒 rclone(env 四键 Secrets 形),段制:版本段 immutable 加 stable 滚动段,dev 滚动段随仓裁
3. 逐件 `.sha256` 边车,边车即镜像锚契约
4. Release 恒 gh CLI 直发 `--latest`,禁 draft
5. 护栏三件:版本一致性闸加解包冒烟、零上传红灯、dispatch 补推口
6. 自升级:有运行时自升级能力的仓走双通道契约;无的归安装管理方单通道
7. 元数据对齐:安装管理器的工具级状态是共同真源,升级后须回写对齐

细则见 `references/common-contract.md`。

## 三、意图路由

| 你要做的事 | 入口 |
| --- | --- |
| 定型号拿配方(六型七要素) | `references/type-recipes.md` |
| 仓侧全链、rclone 形、Release 面、护栏、自升级与元数据 | `references/common-contract.md` |
| 可拷改模板(本地编译与发布命令面、各型片段、播种 workflow、自升级核对清单) | `references/templates.md` |
| 流水线排障与安全清单 | `references/common-contract.md` 第四节起 |
| 封版件、tag 触发、发布验收 | 同插件 doc-gov 的 flow-release |
| 平台矩阵与实机接管、各栈工程合同 | 同插件 code-kit(env-platform、tool-*) |
