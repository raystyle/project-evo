# 公共契约:边界、镜像、发布、护栏、自升级

> 各型配方共用的契约节,型号无关。标准通用件:契约全部参数化,不含任何具体环境私有名。

## 一、边界与产地

- **本面只辖仓侧 GitHub CI/CD 自建流**:detect、编译、测试、打包、发布、自播五环一链全在本仓流水线内完成;CI 不可产的大件分发不属本面
- **发布动作恒由流水线完成**:gh 直发加镜像播种都在 publish job 内;人工手挂 release 或手推镜像属过渡特例,标准明文禁为新形态
- **产物零 commit 回仓**:产物只进 Artifact、Release 与镜像段,源码库不收二进制与离线包

## 二、detect 与流水线形态

- detect 清单驱动:go.mod、Cargo.toml、package.json、pyproject.toml 有则编,对应 job 缺清单静默跳过
- 事件三态:PR 只 Artifact(评审下载用);main 走 Artifact;tag `v*` 加 Release 加镜像
- publish 准入:至少一类打包成功且无任何一类 failure;测试过再打包是硬闸
- 通道对比:Artifact 随 run 寿命短(约 14 天)且下载常需登录;Release 随仓长期且公开仓可匿名;镜像段自控寿命,绑域后可匿名 [经验]

## 三、镜像推送恒 rclone(禁 aws-cli 形)

- Secrets 恒 env 形四键 `R2_ACCESS_KEY_ID`、`R2_SECRET_ACCESS_KEY`、`R2_ENDPOINT`(S3 兼容端点)、`R2_BUCKET`;Token 仅授权目标桶 Object Read & Write,不用 Global Key
- 推送形:`rclone copy <产物目录> :s3:$R2_BUCKET/<tool>/<版本>/ --s3-endpoint $R2_ENDPOINT --s3-access-key-id $R2_ACCESS_KEY_ID --s3-secret-access-key $R2_SECRET_ACCESS_KEY --s3-no-check-bucket --header-upload "Cache-Control: public, max-age=31536000, immutable"`;受限 token 无建桶权,故必带 no-check-bucket(env 形等价 `RCLONE_CONFIG_<remote>_NO_CHECK_BUCKET=true`);版本段对象 immutable,禁覆写
- **双段制**:恒 `<tool>/<版本>/` 加 `<tool>/stable/` 两段;stable 是自更新滚动段,短缓存 `Cache-Control: max-age=60`,刷段用 `rclone sync ... --delete-excluded`(滚代清旧);禁 `releases/<tag>/` 形
- 对外下载走镜像域 `<mirror-host>/<tool>/<version>/<asset>`(桶绑自定义域后匿名可读)
- 段内逐件 `.sha256` 边车(sha256sum 原生格式 `<hash>  <文件名>`),边车即镜像锚契约,下载腿与 digest 判新都以它为准(路由与消费面见 doc-gov 的 flow-release 第八节);聚合 `SHA256SUMS` 可作补充不替代

## 四、Release 面

- 恒 `gh release create <tag> <资产...> --latest` 直发钉回 latest,禁 draft 形;多发布工具各建 Release 是抢 tag 事故源
- Release 资产与镜像段同源同批,发布器与升级器同 digest 判据

## 五、护栏三件

1. **版本一致性闸加解包冒烟**:tag 对载体 manifest(Cargo.toml 或 package.json 或插件三清单)不一致 job 直接红;CI 内解包跑 `--version` 与 tag 逐字对
2. **零上传红灯**:mirror job 推完清点对象,零对象即红(防上游 draft 窗或准入误判静默 skip);确无资产的仓型用显式豁免开关,不许默认静默
3. **dispatch 补推口**:publish/mirror 挂 `workflow_dispatch`,needs 链 `if` 套 `always()` 让补推不依赖重跑全链

## 六、自升级与元数据对齐

- **能力归属判据**:有运行时自升级能力的仓(可执行 CLI 且自身带 update 子命令)走双通道契约;无自升级面(库、静态资产、fork 族)归安装管理方单通道
- **双通道契约**:self update 双通道,自家镜像 stable 段优先,GitHub release 404 自动回落;digest 判新加 `.sha256` 边车锚校验;发布器与升级器同 digest 判据;dev 加 stable 双通道是否随仓开放由仓裁
- **单通道契约**:升级归安装管理方,走其版本 pin(清单滚即升);终态与自升级路径同 digest
- **元数据对齐**:安装管理器的工具级状态是共同真源;自升级器升级后须回写对齐(或管理器以实值探活判,不残留旧版漂移)
- **对齐判据**:各端升级路径一致,管理器 update 或各仓 self update 终态同 digest;双通道判新互认(同一工具 self update 与管理器 update 同报已最新)为验收判据;管理器侧与管理侧验收双面核

## 七、跨宿主闸与回执对账

- **跨宿主闸**:同一产物在不同构建宿主上冒烟(容器闸),防 glibc 与 openssl 互踩;ldd 静态断言双流重定向加 file 双断言
- **回执对账**:发布回执 digest 一律 gh api 自取,GitHub 与镜像与管理器清单三方逐字等才闭环;对方陈述不作数(协议面见 evo-herdr:herdr-flywheel)

## 八、故障排查表

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

## 九、安全清单

- R2 Token 仅目标桶 Object Read & Write,定期轮换
- Secret 只在 GitHub Secrets,文档与 YAML 只留占位
- 产物不进源码库;公开仓 Release 资产视为公开,敏感工具走私有仓加私有桶
- 下载侧核对 `.sha256` 边车;镜像锚以边车为唯一契约
- 不发公共注册表:npm publish、twine upload、cargo publish 一律禁,含 Trusted Publishing
