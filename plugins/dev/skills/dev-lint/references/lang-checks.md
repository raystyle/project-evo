# rs、py、ts 三语言静检

> 命令以本机 `--help` 实查为准,参数随版本演进不写死;判定纪律:退出码制,`cmd > log 2>&1; echo $?` 形,禁尾管吞红。

## rs(Rust)

- `cargo fmt --check`:格式漂移即红
- `cargo clippy --all-targets -- -D warnings`:lint 升错误,零警告口径
- `missing_docs = "deny"`(Cargo.toml [lints.rust]):公开项 docstring 缺失即红(代码即文档纪律,详见市场技能 `evo:doc-gov` 三语言表)
- CI 分岗:linux 全量,win-gnu 与 mac 按仓裁(clippy 加 test)

## py(Python)

- `ruff check .`:select 按仓裁剪,起步 E/F/W/I/B/UP;docstring 纪律加 D 系(per-file-ignores 裁 tests 与生成物)
- 已知坑:D415 不认全角句尾,docstring 句尾统一半角 `.`(ruff 0.16 实测判例);豁免留因由注释
- PEP 723 零依赖脚本面(工具脚本):ruff 同辖,uv 直跑不装包

## ts(TypeScript)

- `tsc --noEmit`:类型面零错
- eslint 随仓配置:有配置才跑,无配置记不适用(不强制引入)
- 类型即契约:公开面类型完备是静检的第一道(详见 `evo:doc-gov` 三语言表 TS 行)

## 门禁接线(语言面)

- 门禁清单固定成文于 AGENTS 或 README(命令原文加退出码口径),首点名即引清单
- pre-commit 跑快速子集(fmt、ruff、tsc),全量进 CI;重门禁(整树编译、真浏览器)记当轮不适用附理由或走代理面
- 判定纪律与触发面:沿市场技能 `evo:distil` 的 gate 面(退出码自取、隔离轮判据、触发对)
