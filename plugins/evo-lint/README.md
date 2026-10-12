# evo-lint

> project-evo 治理插件市场第四插件:项目静态检查与结构标准。市场 `raystyle/project-evo`,客户端显示 `evo-lint:md-lint` 与 `evo-lint:ls-lint`。

单 skill **md-lint**:五面静检:skill markdown(格式标准:frontmatter 官方字段、name 同目录名、description 形态与上限、行数上限、断链)、agents markdown 与 claude markdown(长度限制、结构合同、禁字四类)、Rust(cargo fmt 与 clippy 与 missing_docs)、Python(ruff 含 D 系 docstring)、TypeScript(tsc 与 eslint)。纪律:门禁三态退出码、判定不接吞退出码管道、pre-commit 提交挡板、逐条修不豁免凑绿。

第二 skill **ls-lint**:类型化项目结构标准:四类型模板卡(TS CLI 仓、知识三层聚合仓、worker 服务仓、Python 工具仓,templates/ 声明式 toml 规则件),init 面(既有件不动缺件补位)加 check 面(声明式比对,豁免带因由本地覆盖);ADR-0022 与 REQ-020 在册。

## hook 面:写后自动静检

插件带 PostToolUse hook:Edit/Write 落盘后按后缀(.md/.rs/.py/.ts)自动静检,报错信息回传(Claude Code 直查;Codex apply_patch 宽容放行靠 pre-commit 兜底,花括号变量形态双端兼容)。只做秒级快检查,重检查进门禁与 CI;行数限额可裁(环境变量)。

## 安装

- Claude Code:`/plugin marketplace add raystyle/project-evo` 后 `/plugin install evo-lint@project-evo`
- Codex:`codex plugin marketplace add raystyle/project-evo` 后 `codex plugin add evo-lint`
- Grok:`grok plugin install evo-lint@project-evo --trust`
- Kimi:无市场,拷 `plugins/evo-lint/skills/*` 至 `~/.kimi/skills`

当前发布:0.10.0。版本线随市场五插件同线(ADR-0021 族版本纪律)。
