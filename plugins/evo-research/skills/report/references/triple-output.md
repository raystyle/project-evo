# 三件套纪律与渲染管线

> Markdown 是唯一真源;生成物是投影,禁手改、禁只交一份。

## 一、产物形态

- 每篇报告固定三件套:`reports/YYYY-MM-DD-短名.md` 与同名 `.pdf`、`.docx`,缺一不算完成
- md 有任何改动必须重渲全部产物;只交 PDF 或只交 md 都不算完成
- 生成物禁止手工编辑(与文档即代码投影纪律同源)

## 二、PDF 管线(Typst + cmarker,随 skill 发行)

- 渲染器 typst,模板 `../assets/templates/report.typ`(cmarker 把 md 展开为 Typst 元素)
- 脚本 `../scripts/render.py`(PEP 723 零依赖):定位 typst(--typst/TYPST/PATH 三选一,命令分发由宿主工具链 omc 与 ark 统一维护)、把模板复制进根下 `.report-render/` 编译(入口文件须在 --root 内)、完删
- 首次编译联网拉取 `@preview/cmarker` 包(typst 包缓存,之后离线可用)
- `--check` 渲到临时目录只校验编译,不覆盖正式产物,可接门禁

## 三、字体前提与静默丢字坑(实证)

- 模板字体链是中文字体(宋体/黑体/华文中宋/楷体);渲染侧须有 CJK 字体,Linux 面缺字体(如最小容器)时 typst 只打 unknown font 告警、**退出码仍 0,产物文本层只剩 ASCII,中文字被静默丢弃**
- render.py 检测到未知字体告警会显式提示;根治装 CJK 字体(如 fonts-noto-cjk),字体族参数化(按平台注入字体链)列积压
- 校验产物时抽文本层确认中文在案,别只看文件大小与退出码

## 四、Markdown 书写与渲染的碰撞点(实证)

- **加粗标签的标点写在加粗外**:写 `**关键词**:内容`,不写 `**关键词:**内容`。后者在 CommonMark 里不构成 right-flanking,加粗失效且星号原样印进 PDF;render.py 的 lint 会警告
- **单换行折叠成空格**:题头这类结构化信息必须写成列表或一行,不靠单换行
- **章节序号写进标题**:渲染不自动编号(见 skeleton.md)
- **报告须有二级标题**:模板以首个 `## ` 拆题头区与正文;无二级标题时题头区为空串(原家族模板此处为 none,cmarker 报 Markdown must be a string,已修)

## 五、docx 管线(知识面,下游自建)

- 形态:python-docx(>=1.1)做样式基底与区域微调,OfficeCLI 负责把 Markdown 展开为原生元素、目录页码刷新与 schema 校验
- 版式映射照抄 PDF 模板参数:A4 边距 2.6/2.5/2.4cm;题名黑体 20pt 居中;章节华文中宋 15/14pt;正文宋体 12pt 首行缩进 2 字符;表格三线表 10.5pt;页眉楷体 9pt 报告名、页脚宋体 9pt 页码,首页不显示
- 带外部依赖(python-docx、OfficeCLI),不合本仓脚本零依赖惯例,故以知识形态承载,下游仓按需实现

## 六、产物同步校验

- 比对抽取文本或字节数,不比哈希:typst 内嵌时间戳,同一 md 两次渲染字节数可同但哈希必不同
