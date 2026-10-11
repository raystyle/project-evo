# 四类型标准结构卡

> 数据源:四实践仓实形(2026-10-11 终态)加同日结构研究(单仓折中形:知识三层居仓根、产品代码归 src、子工程成员化、配置根件一工具一件、生成投影在发现位)。规则件本体在 `../templates/*.toml`,本篇是人读卡。

## 一、TS CLI 仓(ai-ccoe 判例形)

```
仓根: AGENTS.md CLAUDE.md(@桥接) README.md CHANGELOG.md
      package.json pnpm-workspace.yaml tsconfig.json vitest.config.ts(配置一工具一件,不收 config/)
      llms.txt(生成,头声明禁手改) contracts 投影件(类型契约,md 形) behavior.yaml(行为契约真源)
sources/{diary,external,evidence}      knowledge/{adr,req,references,concepts,ledger/_index}      operations/
src/{cli 入口,commands/,lib/,types/}   tests/
可选: apps/(可部署子工程,自持 package.json) crates/(Rust 子工程,输出归 workspace target/) tools/(仓级脚本)
禁入源码树: dist/(tsc outDir) node_modules/ target/ .claude/settings.local.json
```

要点:三层居仓根不收 docs/(ADR 判例);知识页手册契约与代码同提交,拆仓断漂移检查;两账本(distill-log、skill-impact)收 knowledge/ledger/ 防流水当概念。

## 二、知识三层聚合仓(v2 标准形,browse_rs/pve/ark/clean-chrome 判例)

```
docs/ 中心形(或仓根形,仓自选唯一):
  docs/sources/{diary,external,evidence,INDEX}   docs/knowledge/{adr,req,references,research,mistakes,skill-impact,流水,INDEX}
  docs/operations/{G 手册族,skills/,INDEX}
AGENTS.md(纪律句:单仓纪律形或 git 三选一)   .claude/skills/(加载视图,符号链接或投影加守卫)
```

要点:字母表八元组定归层(distil-skill layers);git 边界三选一;防重提页空态也要立;既有 docs 全家桶仓走既有仓迁移形(映射注记、引用面清单、rg 旧名清零)。

## 三、worker 服务仓

```
仓根: AGENTS.md CLAUDE.md README.md CHANGELOG.md  部署清单与入口(按平台)
src/ 或 apps/<名>/(自持 package.json 与工具链,独立部署)
配置: 环境样例件(.env.example 等值)在仓,真密钥禁入;配置根件一工具一件
tests/  docs/(简面:adr 加 req 加 diary 即可,不必全三层)
禁入源码树: 构建输出、依赖目录、运行时状态目录
```

要点:可独立部署是判定面(自持清单加独立入口);作为大仓子工程时归 apps/ 成员位(pnpm workspace packages 列表收编),独立仓时本卡适用。

## 四、Python 工具仓(pve-harness 判例形)

```
仓根: AGENTS.md CLAUDE.md README.md CHANGELOG.md pyproject.toml uv.lock
src/<包名>/   tests/   .tools/(PEP 723 零依赖脚本,uv 直跑)   docs/(三层聚合或 doc-gov 面,按仓)
配置: pyproject 一件收 ruff(select 含 D 系加按仓 ignore)与 pytest;真源不手改生成面
禁入源码树: __pycache__/ .venv/ dist/ *.egg-info/
```

要点:ruff D 系 docstring 纪律进门禁(D415 全角句尾坑在册);投影面走注册表三面同源判例(help 加 --llms 加 --schema 单源渲染)加 --check 漂移守卫。
