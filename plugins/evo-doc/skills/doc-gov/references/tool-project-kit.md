# 项目工具链范式:uv 加 PEP 723 零依赖骨架

> 工程骨架形态:自用工具归档目录加 README 清单、python 脚本 PEP 723 内联元数据 uv 直跑、门禁三态退出码加提交挡板、发布三段式加哈希边车。多仓实证提炼;形态跟项目形态走,不硬套。

## 工具归档目录

- 目录名 `.tools/` 或 `tools/` 任一,进 git;全仓自定义脚本归此,不散置
- 目录带 README 清单表(脚本、用途、调用方),新增或改动同步登记
- 命名小写连字符;脚本 docstring 写用法、参数、退出码
- 临时脚本第二次会用即归档入目录;一次性脚本用完即弃

## python 运行形态

- PEP 723 内联元数据:`# /// script` 块加 `requires-python` 加 `dependencies`,`uv run` 直跑,不建 venv 不装依赖
- 零依赖是默认;带依赖是例外,须在 README 给理由
- requires-python 下限跟仓主线(新仓取 >=3.12);对外分发的 SDK 面另取最宽兼容下限,两轨独立
- 有真测试套件才立 pyproject 加 uv.lock(dev 组放 pytest);纯脚本仓零项目文件直跑
- 宿主为 Windows 加 PowerShell 7 的仓,验收与运维面脚本统一 pwsh,python 只作跨平台工具面

## 门禁与退出码

- 三态退出码:0 过、1 有违规、2 出错;机器读面给 `--json` 载荷
- 路径级豁免走环境变量正则通道;根三件(合同、索引、自述)永不豁免
- 提交挡板:`git config core.hooksPath <钩子目录>`,pre-commit 跑门禁脚本,不过不进库
- 无 hooks 仓退化为 AGENTS Commands 裸命令纪律加 CI 兜底
- md 禁字规则唯一权威单文件维护,check、scan、hook 多面同源引用,不复制规则
- 文档骨架合规检查项编号化(合同五节、目录与索引、状态机、命名、六态、禁字、断链),门禁脚本可跨仓复用

## 合同与发布

- AGENTS 五节合同(Commands、Must、Must not、Read first、环境)加 CLAUDE.md 单行桥接;知识库仓可全文复制
- CHANGELOG 只记版本级里程碑,与研究档案、提交信息三面正交
- 发布走 release 脚本三段式:预检、构建、验证分发;产物配 sha256 边车
- 版本载体唯一权威一处(插件 manifest、Cargo.toml、package.json 任一),载体外出现版本号即第二真相

## 选型与边界

- 分化可选项:目录名、python 下限、hooks 强度、测试框架、文档门禁层级,跟仓形态走,只有合适的没有硬性
- 知识库仓可无工具面:双链图本身即是结构门禁
- 无 python 面的仓整个范式不适用,不为此引入 python
