# .tools 项目脚本工具

| 脚本 | 用途 | 调用方 |
| --- | --- | --- |
| md-ref-scan.py | skills 树交叉引用断链扫描(PEP 723 自包含,零依赖) | git pre-commit;文档结构大改后必跑 |
| init.py | 文档骨架安装(幂等不覆盖已有;模板在本目录 `templates/`) | 本仓维护骨架模板时;CI smoke |
| check.py | 骨架合规诊断 PE-01 至 PE-12(只读,--json 机器读面) | git 门禁表;CI smoke |
| scan.py | 禁字与浅密钥扫描(工作区与 git 历史;豁免走 PEVO_SCAN_ALLOW) | git 门禁表 |

> md 禁字规则唯一权威是 `plugins/evo-doc/scripts/mdrules.py`(随插件 hook 走,md-guard 同目录),本目录 check.py 与 scan.py 经插件路径 import 同一份,三面同源;md-guard 由 plugin hook、`.claude/settings.json` 与 `githooks/pre-commit` 三处调用。
> `verification/command-test-cases.md` 是 check 的等价 PowerShell 用例集;`templates/` 是 init 的骨架模板十件。
