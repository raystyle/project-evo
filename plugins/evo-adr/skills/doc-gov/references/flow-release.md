# 封版发布模式：全平台门禁验收与 tag 触发

> 从「CHANGELOG Unreleased 有货」到「Release 资产验收」的封版操作手册。四轮发布实证（v0.1.0 至 v0.4.0）沉淀 [经验]。

## 一、前置裁定

- **封版 = 发布一个新版本**：版本号必前进，不存在不改版本号的封版；封版件、tag 与 Release 资产同属一次发布
- **Unreleased 有条目才封版**；空则不发布
- 版本号取舍：能力新增或行为变化取次版本号（`0.x.0`），修复取补丁号（`0.x.y`）；与 ROADMAP 阶段对照
- 发布通道只走 stable；不做自动更新（self update 同口径）

## 二、全平台门禁验收（三路全绿才进封版）

按项目平台矩阵（code-kit 的 env-platform）组织三路：

1. **主开发机**：代码门禁（lint/test 全 target，外部真样本缺失自动跳过）+ 文档门禁（lint/断链/规范机检）+ release 构建
2. **各平台实机**（每平台一台，ssh 接管）：`git pull --ff-only` 后同套门禁 + release 构建 + 真样本冒烟
3. **CI**：main 推送后平台矩阵 run 全绿

纪律 [经验]：
- 验收命令**不接吞退出码的管道**（`| tail` 之类）
- 实机远程命令用**阶段标记串**逐段确认（`&& echo STAGE-OK`）
- 实机工具链与 CI 对齐（如 `rustup run stable`），防本机默认工具链差异
- **门禁与实跑互补，缺一不可**：门禁抓格式与回归，首跑实整抓逻辑缺口，heal all 首跑抓出两真缺口、CI 首跑抓限流、停栈实测抓单实例守卫缺口，全是门禁全绿下的漏网 [经验]

## 三、封版件（一次提交）

1. **产物内版本号**改目标版本（CI 有 tag 一致性闸，不一致 job 直接红）
2. **CHANGELOG**：`[Unreleased]` 转为 `[<版本>] - <日期>`，正文只留版本级里程碑
3. **自动生成物重生**：含版本号的生成文件（SKILL.md、快照等）重生；注意 test 不重建产物，须先 build [实证]
4. **快照复审**：版本号入快照的，`.snap.new` 逐个人工审后入库
5. **门禁复跑**（本机全件）全绿后一次提交：`chore: 封版 v<版本>`

## 四、tag 触发发布

```powershell
git tag v<版本>
git push origin main v<版本>      # tag 推送即触发 release 流水线
```

流水线要点：tag 与产物版本一致性闸；`--locked`/可复现构建；每平台打包（二进制 + README/LICENSE/SKILL + `.sha256` 校验件）上传 Release [经验]。

## 五、发布验收

- release run 各 job 全绿（重依赖平台的构建是风险点）
- **资产件数齐**：平台数 ×（压缩包 + `.sha256`)
- 抽查三件：`.sha256` 校验过、解包 `--version` 冒烟过、self update（如有）报已最新
- 本机与 CI 资产 sha 不一致属预期（构建机差异），一致性以官方 `.sha256` 为准 [实证]
- **收尾义务**：CHANGELOG 已定版、ROADMAP 阶段状态翻转、diary 当天钩子

## 六、验收入壳（随验收回填）

验收记录落在本文档尾部或相关 ADR 内：各路退出码/阶段标记、run id、资产清单、抽查结果、当轮发现的新坑（进 diary 或 ADR）。每次发布一段验收记录，含实测量级与首验项 [经验]。

## 七、多仓版本标准（跨仓协调）

- **semver 触发判据**：修复与文档批取 patch（0.x.y）,能力新增或行为变化取 minor（0.x.0）,契约破裂或形态重构取 major（x.0.0）;判据写在封版 REQ 里,不凭感觉
- **各仓版本载体唯一权威**：Rust 仓 Cargo.toml（workspace 版集中处）、Node 仓 package.json 加 lock 双处、插件仓 plugin manifest 三清单;载体外出现版本号即第二真相,清理
- **统一封版协调**（多仓并进时）：总台发统一封版令,各仓按第三节封版件自理,conclusion 自验（CI 加 tag 加资产）后回执;catalog 与镜像按仓内惯例滚动,不跨仓等齐
- **版本对齐表**（总台维护）：

```markdown
| 仓 | 载体 | 当前版 | 待封 | 状态 |
| --- | --- | --- | --- | --- |
| <仓名> | Cargo.toml | 1.2.2 | 1.2.3 | 待令 |
```

## 八、统一分发体系（种子、分发与自升级）

三面可复制标准（实例源 ohmycloud,各仓接入照其实例）。**职责分工**（用户裁定 2026-09-16）：omc 负责资源分发运维与版本分发管理（catalog 真源加种子签发加镜像运维加版本对齐表）；ark 负责落地执行验收（各端 install 加 update 加 status 加 doctor 的实际执行与验收回执）；标准勿混角色：

- **打包种子发布**:env-seed 链(catalog tools.toml 加 sha256 pin 加 manifest 解析脚本加断点续跑台账)到 catalog-seed 流水(lint 加 seq 注入加 minisign 签名加三件套推对象桶)到 六小时定时加 dispatch;各仓 CI 自推镜像走 seed 通道(桶级 token 零建桶权,最小权面)
- **资源分发**:镜像域版本段路由 `<tool>/<version>/<asset>` 加 `.sha256` 边车(无 manifest,边车即锚);双通道路径镜像优先 GitHub 回退;CLI 资产三平台齐(linux 加 win-gnu 交叉加 mac)
- **自升级**:三通道体系(dev 滚动源 加 stable 正式源 加 git 源装)、镜像回退腿(GitHub 404 自动回落镜像域)、digest 判新加边车锚校验;发布器与升级器同 digest 判据 [实证: ark 与 hst 已各自跑通]

## 九、与体系其它件的衔接

| 环节 | 依据 |
| --- | --- |
| Unreleased 起步与转版 | CHANGELOG 头部约定 + AGENTS 合同「发布」相关行 |
| tag 纪律与一致性闸 | `git tag v<版本>` 后推送；已发 release 的 tag 不回退 |
| release 资产上传/验收 | `gh release create` / `gh release upload --clobber` |
| 平台矩阵与实机接管 | code-kit 的 env-platform 六/七节 |
| |
| Node/TS npm 包资产 | code-kit 的 tool-typescript 第十节：`package.json` 与 lock 双处 version、`npm pack` tgz、安装验收禁 link |
