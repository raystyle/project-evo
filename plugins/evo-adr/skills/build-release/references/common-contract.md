# 公共契约:边界、镜像、发布、护栏、自升级

> 各型配方共用的契约节,型号无关。标准通用件:契约全部参数化,不含任何具体环境私有名。

## 一、边界与产地(三段式)

- **本地编译和打包**:编译与打包都在本地:二进制形在主开发机交叉编译与实机矩阵(mac 形在 mac 实机),npm 形 `npm pack` 与 py 形 `python -m build` 本地出离线包;工具链自控可复现;测试闸先行,版本一致性闸与解包冒烟在发布前过
- **GitHub 产物发布**:gh CLI 直发 `--latest`(本地跑),产物进 Release;禁 draft,多发布工具各建 Release 是抢 tag 事故源
- **CI/CD Action 自动播种**:Release published 事件触发 workflow,从 Release 拉资产 rclone 推镜像段,零上传红灯清点,dispatch 补推口带 tag 入参;CI 面不编译,测试岗(docs 门禁、投影门禁、测试矩阵)随仓裁
- **发布动作零手工过渡形态**:手挂 release 或手推镜像属过渡特例,禁为新形态;CI 不可产的大件分发不属本面
- **产物零 commit 回仓**:产物只进 Release 与镜像段,源码库不收二进制与离线包

## 二、detect 与产物形态

- detect 清单驱动:go.mod、Cargo.toml、package.json、pyproject.toml 有则编,无清单的纯文档仓走 manifest 形
- 包形:单顶层目录 = 二进制加 README 加 LICENSE;win 形 zip 他形 tar.gz;逐包 `.sha256` 边车(sha256sum 原生格式)
- 通道对比:Release 随仓长期且公开仓可匿名,是产物正源;镜像段自控寿命,绑域后可匿名,是下载腿与自升级源 [经验]

## 三、镜像推送恒 rclone(禁 aws-cli 形)

- Secrets 恒 env 形四键 `R2_ACCESS_KEY_ID`、`R2_SECRET_ACCESS_KEY`、`R2_ENDPOINT`(S3 兼容端点)、`R2_BUCKET`;Token 仅授权目标桶 Object Read & Write,不用 Global Key
- 配置用 env-remote 形(命名 remote):`RCLONE_CONFIG_R2_TYPE: s3`、`RCLONE_CONFIG_R2_PROVIDER: Cloudflare`、`RCLONE_CONFIG_R2_ACCESS_KEY_ID`、`RCLONE_CONFIG_R2_SECRET_ACCESS_KEY`、`RCLONE_CONFIG_R2_ENDPOINT` 各映射同名 Secrets,加 `RCLONE_CONFIG_R2_NO_CHECK_BUCKET: "true"`(受限 token 无建桶权,预检 CreateBucket 会 403,必带);命令里用 `r2:${R2_BUCKET}/<段>/` 寻址。旗标形(`--s3-endpoint` 等)等价可用
- **段制**:恒 `<tool>/<版本>/`(immutable,copy-only 不 sync,长缓存 `Cache-Control: public, max-age=31536000, immutable`)加 `<tool>/stable/`(自更新滚动段,短缓存 `max-age=60`,刷段 `rclone sync --delete-excluded` 滚代清旧)两段;有 dev 通道的仓加 `<tool>/dev/` 滚动段(main 推,sync 形同 stable);禁 `releases/<tag>/` 形
- 对外下载走镜像域 `<mirror-host>/<tool>/<version>/<asset>`(桶绑自定义域后匿名可读)
- 段内逐件 `.sha256` 边车(sha256sum 原生格式 `<hash>  <文件名>`),边车即镜像锚契约,下载腿与 digest 判新都以它为准(路由与消费面见 doc-gov 的 flow-release 第八节);聚合 `SHA256SUMS` 可作补充不替代

## 四、Release 面

- 恒 `gh release create <tag> <资产...> --latest` 直发钉回 latest,禁 draft 形;多发布工具各建 Release 是抢 tag 事故源
- Release 资产与镜像段同源同批,发布器与升级器同 digest 判据

## 五、护栏三件

1. **版本一致性闸加解包冒烟**:tag 对载体 manifest(Cargo.toml 或 package.json 或插件三清单)不一致即止红;发布前解包跑 `--version` 与 tag 逐字对(本地)
2. **零上传红灯**:播种 workflow 灌完清点对象,版本段与 stable 段分别报数,零对象即红(防半失败:版本段有物而 stable 漏滚仍绿);确无资产的仓型用显式豁免开关,不许默认静默
3. **dispatch 补推口**:播种 workflow 挂 `workflow_dispatch` 带 tag 入参,从 Release 拉资产重灌,不依赖重跑任何链

## 六、自升级与元数据对齐

- **能力归属判据**:有运行时自升级能力的仓(可执行 CLI 且自身带 update 子命令)走双通道契约;无自升级面(库、静态资产、fork 族)归安装管理方单通道
- **双通道契约**:self update 双通道,自家镜像 stable 段优先,GitHub release 404 自动回落;digest 判新加 `.sha256` 边车锚校验;发布器与升级器同 digest 判据;dev 加 stable 双通道是否随仓开放由仓裁
- **单通道契约**:升级归安装管理方,走其版本 pin(清单滚即升);终态与自升级路径同 digest
- **元数据对齐**:安装管理器的工具级状态是共同真源;自升级器升级后须回写对齐(或管理器以实值探活判,不残留旧版漂移)
- **对齐判据**:各端升级路径一致,管理器 update 或各仓 self update 终态同 digest;双通道判新互认(同一工具 self update 与管理器 update 同报已最新)为验收判据;管理器侧与管理侧验收双面核

## 七、跨宿主闸与回执对账

- **跨宿主闸**:同一产物在不同构建宿主上冒烟(容器闸),防 glibc 与 openssl 互踩;ldd 静态断言双流重定向加 file 双断言
- **回执对账**:发布回执 digest 一律 gh api 自取,GitHub 与镜像与管理器清单三方逐字等才闭环;对方陈述不作数(协议面见 evo-herdr:herdr-flywheel)

## 八、上游追新(fork 维护仓)

- **上游源与合入**:remote 加 `upstream` 指上游仓;追新 = `git fetch upstream` 后 `git merge upstream/<默认分支>`(merge 保审计迹为默认,rebase 随仓裁);追新批独立成 commit,不与功能批混
- **追新节奏**:随上游 release tag 跟,不追上游滚动分支(压冲突面)
- **冲突面纪律**:冲突只允许出现在自有改动面(补丁、构建脚本、工作流);核心源文件冲突 = 自有改动侵入过深信号,升级为重评移植策略,不硬解
- **版本 bump**:fork 版本策略写进仓内 AGENTS(对齐上游 tag 形随仓定),载体 manifest 与 tag 一致性闸照走
- **回跑矩阵**:追新批必过全量回跑再发布:测试闸、构建、跨宿主容器闸(native 形)、解包冒烟;上游新依赖进树仍要自含闭包
- **发布**:追新批同三段式正源(本地编译和打包、gh 直发、Action 播种)

## 九、故障排查表

| 现象 | 处理 |
| --- | --- |
| go 形找不到 main | 改 build 路径 `./cmd/<bin>` |
| rust 形名不对或链接失败 | 核 Cargo.toml name 或 Variable;aarch64 装 gcc-aarch64-linux-gnu 并设 linker |
| npm 形 pack 文件不全 | 核 package.json 的 files/exports 与 .npmignore |
| py 形 build 失败 | 补 pyproject.toml 的 build-system |
| publish 被 skip | PR 故意跳;四类全 skip = 仓无清单;镜像零对象红灯看第五节 |
| R2 AccessDenied | Token 权限面、桶名、endpoint 匹配;禁 Global Key |
| Release 没文件或没置 latest | 核推的是 v* tag;gh CLI 加 --latest 直发,勿 draft |
| 升级态漂移 | 第六节对齐判据:各端终态同 digest,双面核 |
| 元数据旧漂(版本残留) | 第六节元数据对齐:升级器回写或管理器实值探活判 |
| 产物异宿主崩溃 | 第七节跨宿主容器闸;ldd 双流断言 |
| 上游 merge 冲突在核心源 | 第八节冲突面纪律:自有改动侵入过深,重评移植策略,不硬解 |

## 十、安全清单

- R2 Token 仅目标桶 Object Read & Write,定期轮换
- Secret 只在 GitHub Secrets,文档与 YAML 只留占位
- 产物不进源码库;公开仓 Release 资产视为公开,敏感工具走私有仓加私有桶
- 下载侧核对 `.sha256` 边车;镜像锚以边车为唯一契约
- 不发公共注册表:npm publish、twine upload、cargo publish 一律禁,含 Trusted Publishing
