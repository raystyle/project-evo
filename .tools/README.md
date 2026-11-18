# .tools 项目脚本工具

| 脚本 | 用途 | 调用方 |
| --- | --- | --- |
| mdrules.py | md 禁字规则唯一权威(四类禁字与 SKILL description 三句形检;PEP 723 零依赖) | check/scan/md-guard 同源 import |
| termrules.py | 约束术语表唯一权威(ENFORCED 与 PENDING 两层) | term-lint 与 check PE-13 同源 import |
| md-guard.py | markdown 四类禁字门禁(--staged 检暂存区;批 105 live hook 裁撤后只走 pre-commit) | githooks/pre-commit |
| term-lint.py | 约束术语表静检(ENFORCED 层门禁,--pending 列存量不计门禁) | githooks/pre-commit;改文档后手跑 |
| term-mine.py | 术语挖词(gw_logs 语料批量块频,S020/S021 出处) | 扩表时 |
| md-ref-scan.py | skills 树交叉引用断链扫描(PEP 723 自包含,零依赖) | git pre-commit;文档结构大改后必跑 |
| init.py | 文档骨架安装(幂等不覆盖已有;模板在本目录 `templates/`) | 本仓维护骨架模板时;CI smoke |
| check.py | 骨架合规诊断 PE-01 至 PE-13(只读,--json 机器读面) | git 门禁表;CI smoke |
| scan.py | 禁字与浅密钥扫描(工作区与 git 历史;豁免走 PEVO_SCAN_ALLOW) | git 门禁表 |
| fleet-exec.py | 跨机 shell 格普通进程通道薄封装(send-text 加 enter 加 wait-output 收标加 read 回执;逐条回显 herdr 命令) | 总台舰队运维(清理、安装、探针轮) |

> md 禁字与约束术语表五脚本原在 dev 插件 scripts/(批 180 dev 插件退役迁入,先例 = 第八十九批 init/check/scan 移本仓 .tools、ADR-0018 工具与 skill 解耦);check.py 与 scan.py 经本目录同源 import mdrules 与 termrules,多面同一权威;md-guard 与 term-lint 由 `githooks/pre-commit` 调用(hook 已撤)。
> `verification/command-test-cases.md` 是 check 的等价 PowerShell 用例集;`templates/` 是 init 的骨架模板十件。
