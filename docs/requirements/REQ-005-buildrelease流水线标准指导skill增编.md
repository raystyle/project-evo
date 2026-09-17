---
id: REQ-005
title: build-release 流水线标准指导 skill 增编
status: implemented
priority: must
trace: tests/test_project_evo.py
---

# REQ-005:build-release 流水线标准指导 skill 增编

## Scenario

各仓编译打包发布形态散在各仓工作流与 REQ,新仓接入靠逐仓考古。总台派单(2026-09-17)起草全仓标准,经六轮追正定形:仓无关指导 SKILL 落 evo-adr,类型路由制加公共契约节加可拷改模板;通用性终约束:私有名称与私有信息零出现(正文、注脚、示例、模板默认值全禁),契约全部抽象参数化,实证引不进 SKILL 留仓内 diary;边界只辖仓侧 GitHub CI/CD 自建流。

## Criteria

- [x] skill 落位 `plugins/evo-adr/skills/build-release/`(SKILL.md 加 references 四篇含索引),frontmatter name 与目录一致,description 兼做什么与何时用并含触发词
- [x] 类型路由制成文:六型(go/rust/npm/py/native/manifest)各配七要素(构建矩阵、测试闸、打包与边车、发布、播种、自升级判据、元数据对齐);起草期 fleet-heavy 型按追正六剔除,边界一句注记
- [x] 公共契约节成文:仓侧全链自包、detect 与流水线形态、rclone 恒形与双段制、Release 直发、护栏三件、自升级与元数据对齐、跨宿主闸与回执对账、排障表、安全清单
- [x] 可拷改模板四节:本地编译与发布命令面(版本闸、测试闸、交叉编译、包形与逐包边车、解包冒烟、gh 直发与 dev prerelease 滚动)、各型本地编译片段、CI/CD 播种 workflow(release published 触发、拉资产、env-remote r2:、零上传红灯三段报数、dispatch 带 tag 入参)、自升级契约核对清单
- [x] 通用性纪律:私有名称零出现(镜像域 `<mirror-host>/<tool>/<version>/`、安装管理器元数据抽象化、Secrets 通用 R2 族);实证引全部留仓内 diary 不入 SKILL
- [x] 同步面全改:ADR-0013 与索引、双 manifest 与市场条目描述、守卫 SKILLS 十 skill、pre-commit 第十段、AGENTS 与根 README 与 docs 地图与 gates 计数、evo-adr README 四 skill 化、doc-gov 草稿篇 flow-build.md 退役与三面回退、CHANGELOG、ROADMAP、diary;uv run pytest 全绿与 md-ref-scan 十 skill 零断链
