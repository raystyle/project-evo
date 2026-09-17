# 六型配方:每型七要素

> 构建矩阵、测试闸、打包与边车、发布、播种、自升级判据、元数据对齐;公共契约(边界、rclone 形、护栏)见 common-contract.md,此处只写型差异。

## go 形(go.mod)

- **构建矩阵**:`CGO_ENABLED=0` 交叉六目标:linux/darwin/windows 各 amd64 加 arm64;主包在 `cmd/<bin>` 时改 build 路径
- **测试闸**:`go test ./...` 先行,过才打包
- **打包与边车**:`<bin>-<os>-<arch>[.exe]` 逐件 `.sha256`
- **发布/播种**:公共契约第三节与第四节(gh 直发加 rclone 双段)
- **自升级判据**:有运行时自升级能力即双通道契约,无则安装管理方单通道
- **元数据对齐**:公共契约第六节回写对齐

## rust 形(Cargo.toml)

- **构建矩阵(本地)**:三目标实证形:`x86_64-unknown-linux-gnu`(主开发机本职)、`x86_64-pc-windows-gnu`(主开发机 mingw 交叉出 PE,CRT 静态零 DLL 依赖)、`aarch64-apple-darwin`(mac 实机);扩岗(aarch64-linux 交叉、musl 纯静态)随仓裁
- **测试闸**:`cargo test --locked` 先行(本地跑);交叉件运行时冒烟在目标实机
- **打包与边车**:单顶层目录 = 二进制加 README 加 LICENSE,win 形 zip 他形 tar.gz,逐包 `.sha256`;交叉件运行时冒烟用专岗(下载 artifact 在原生 OS 跑)
- **发布/播种**:公共契约第三节与第四节(gh 直发加 rclone 段制)
- **自升级判据**:必答项;带 update 子命令的自研 CLI 适用双通道契约,库或 fork 形归安装管理方单通道
- **元数据对齐**:回写对齐;载体唯一权威是 Cargo.toml(workspace 版集中处)

## npm 形(package.json)

- **构建矩阵(本地)**:Node 22 级;`package-lock.json` 在则 `npm ci`
- **测试闸**:`npm test --if-present` 加 `npm run build --if-present`
- **打包与边车**:`npm pack --pack-destination`,files/exports 控 tarball;workspace 全子包加 `--workspaces`;逐 tgz `.sha256`
- **发布/播种**:公共契约第三节与第四节
- **禁令**:npm publish 禁,离线 tgz 是唯一分发形;双处 version 纪律见 code-kit 的 tool-typescript
- **自升级判据**:库形通常无自升级面,归安装管理方;CLI 形按运行时能力判
- **元数据对齐**:公共契约第六节回写对齐

## py 形(pyproject.toml)

- **构建矩阵(本地)**:Python 3.12 级;纯 Python 用 `python -m build`
- **测试闸**:pytest 先行(有测试面时)
- **打包与边车**:wheel 加 sdist 逐件 `.sha256`;C 扩展或多平台 wheel 换 cibuildwheel matrix
- **发布/播种**:公共契约第三节与第四节
- **禁令**:twine upload 禁
- **自升级判据**:多为工具脚本形,归安装管理方单通道
- **元数据对齐**:公共契约第六节回写对齐

## native 形(autotools/C++ 源码树)

- **构建矩阵**:容器内自含静态构建,树内依赖闭包(禁宿主库拖链);configure 加 make 出静态产物
- **测试闸**:仓内测试面加**跨宿主容器闸**:同一产物在不同构建宿主冒烟(如 22.04 构建在 24.04 容器跑);ldd 静态断言双流重定向加 file 双断言
- **打包与边车**:tar.gz 包形逐件 `.sha256`(同公共契约包形,不发裸二进制:播种白名单只收包形与边车,裸件会静默漏灌)
- **发布/播种**:公共契约第三节与第四节
- **自升级判据**:多为 fork 静态件,归安装管理方单通道(版本 pin 滚即升)
- **元数据对齐**:公共契约第六节回写对齐
- **特记**:OpenSSL legacy provider 类 dlopen 会拖宿主库互踩,构建参数自含跳过并配容器闸

## manifest 形(纯文档/插件仓)

- **构建矩阵与打包**:不适用(无二进制面)
- **无编译无播种**:不产二进制,不进镜像段
- **测试闸**:仓内规范与一致性门禁(测试、断链、禁字、清单守卫)
- **发布形**:清单三处一致(manifest 双面加市场条目),版本一致性闸仍适用;tag 触发市场快照刷新;无镜像播种
- **自升级判据**:不适用;消费侧由客户端插件机制自管
- **元数据对齐**:不适用(无二进制面)
