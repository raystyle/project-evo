# report 参考知识体系(渐进索引)

> 四篇自包含:骨架与写作规范、三件套与渲染管线、版式复检口径、信源存档与登记。模板在 `../assets/templates/`,渲染脚本在 `../scripts/render.py`。检索与获取管线在同插件 research。

| 我要… | 看哪篇 |
| --- | --- |
| 开写一篇新报告 / 骨架怎么搭 / 写作纪律 | [skeleton.md](skeleton.md) |
| 产物形态 / md 到 PDF 怎么渲 / docx 管线 | [triple-output.md](triple-output.md) |
| 版式怎么复检 / 行距异常判定 | [layout-check.md](layout-check.md) |
| 信源怎么存档分级 / 完成后登记什么 | [sources-and-index.md](sources-and-index.md) |
| 渲染命令与坑 | `../SKILL.md` 命令节 |

## 检索方法

```powershell
rg -n "关键词" .                # 全文搜
reader query <文件> ".h2"        # 结构化提取节目录
```
