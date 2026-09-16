# Python 工程合同：类型注解、docstring 与 uv 运行时

> Python 栈的文档即代码落地。项目从零起步照此配；投影与状态机总纲见 base-projection.md 与 base-adr.md。

## 运行时合同

- uv 运行时,Python >= 3.12;工具脚本 PEP 723 内联依赖声明,零第三方依赖优先(单文件 `uv run` 直跑,不拖锁文件) [实证: 本仓 init/check/scan/mdrules 四件实践]
- 入口脚本 argparse;stdout/stderr 非 UTF-8 时显式 reconfigure(Windows 控制台兼容) [实证]
- 类型注解全覆盖,`from __future__ import annotations` 延迟求值

## 契约注释（L1）

- 公开函数 docstring 写「做什么 + 何时用 + 边界」,不写怎么做;怎么做是代码的事
- 模块头 docstring 承载用法与白名单口径(如 scan 的 `PEVO_SCAN_ALLOW` 说明)
- 覆盖率机检用 interrogate,CI 可设下限 deny(三栈对照表口径) [推断: 选型对照,本仓未实装]

## 门禁命令（AGENTS Commands 节候选）

```text
uv run pytest -q
uv run python -m compileall scripts      # 语法冒烟
uv run interrogate --fail-under 90 .     # docstring 覆盖(选配)
```

## 投影（agent 面）

- docstring 为源:Griffe/MkDocStrings 出分模块 md,弱项可自写 JSON 补 agent 面;人看的站 MkDocs(`mkdocs build --strict` 兼作漂移门禁);示例执行 `pytest --doctest-modules` [推断: 三栈对照表口径,重文档仓可缓配]

## 工程要点

- 测试断言带语义消息(失败输出即定位线索,不当哑检查) [经验]
- 门禁脚本退出码契约 0/1/2(过/不过/出错),调用方按码断言,不解析输出文本 [经验]
