# COE 形态:三层聚合与双向链接图

> 知识库操作台仓的文档形态:三层单向支撑加双链图检索。本形态的仓只有知识没有执行面,开发与操作从本台出发(查路由、按手册做、在框架仓落地、结果回流写回本台),接管框架仓文档体系,与框架实况冲突时以框架仓为准 [经验: 双 COE 操作台仓实践提炼]。

## 三层结构(单向支撑)

| 层 | 承载 | 回答 |
| --- | --- | --- |
| `sources/` | 依据原件(外部文档 verbatim、实证抓取、上游决策) | 出处是什么 |
| `knowledge/` | 定义、结论、关系(concepts 概念页、docs 结论页、index 索引页) | 是什么、为什么 |
| `operations/` | 可执行手册(按域分册、index 入口) | 怎么做、验收什么 |

- 单向支撑:knowledge 页靠 sources 撑,operations 手册靠 knowledge 撑,反向不成立
- 硬规则:知识页无 sources 标 unverified,不得当手册依据;手册无 knowledge 链接不得当规范执行;原理不进手册,步骤不进知识页,正文不进入口总纲
- 流转:新实证入库 = 新建 sources 件加更新对应 knowledge 页并链接;知识已稳要落地 = 写或改 operations 手册;手册与知识冲突 = 带 sources 的 knowledge 页为准,改手册或标 supersedes

## 双向链接与图

- 知识页 frontmatter 登记 `links`(target 加 relation,如 derived_from、supports);正文 `[[路径去 .md]]` 双链:单独成行 = 挂到主题,句中 = 参见
- `_index/graph.json` 是双链图:入边登记、可再生成、损坏可忽略;`_index/graph.py --query <id>` 双向检索一页的出入边
- 检索纪律:回答必须带路径,没有就说没有;跟双链展开默认最多 2 跳,要出处再进 sources/

## 入口与路由

- `AGENTS.md` 指挥总纲:仓定位、技能面、启动四步(读完即停、按路由表映射意图、只开对应 index 与一页目标文件、双链限跳)、任务路由表(意图、先读、再读三列)
- 偏好、进行中状态、临时约束不进本仓,由 agent 自带 memory 管
- 项目日记(`diary/`)挂本仓做活轨迹,一天一篇,机制见 base-diary.md

## 建仓五步

1. 立入口:AGENTS 指挥总纲加任务路由表
2. 立三层目录与各自 index
3. 首批知识页带 sources 入库,frontmatter 登记 links
4. 立双链图:入边登记与查询脚本,双链约定写进总纲
5. 日记开篇,回流纪律(结果写回本台)跑起来
