# rulings:检索域判例档案

> 日期/现象/结论形;判例真源在 browse workspace 仓(git 7814fc0 面)与 fleet intelligence 工作台实跑件,本篇只留提炼结论。

## 2026-10-17 google 主搜索面出路由

- 现象:本机实跑判读机,回执 `verdict=challenged`,落在 `/sorry` 挑战页(IP 限流/反爬);此前该面在别的出口也高发挑战
- 结论:网页检索主通道定为 bing,google 主搜索面不进路由、不设备胎;挑战出现即弃走,不重试不硬闯

## 2026-10-17 scholar 直通

- 现象:同一出口同一时段,`scholar.google.com/scholar?q=..&hl=en` fetch 直出 HTTP 200 满页 10 条,无挑战无验证码;锚点 `#gs_res_ccl_mid .gs_r`
- 结论:scholar 与 google 主面风控独立,学术通道 fetch 首击即可;「Scholar 反爬比主面凶」的保守推测被实测推翻

## 2026-10-17 bing fetch 零引擎直出

- 现象:`browse fetch 'https://www.bing.com/search?q=<词>' --markdown` HTTP 200 全 SERP(`via: http`),无头引擎 goto+js 抽取亦通
- 结论:bing 面成本梯从 fetch 起,引擎只在 fetch 塌后起;无头即通,不需要有头与 profile 养护

## 2026-10-17 渲染裸 sleep 退役

- 现象:A/B 对照,goto 默认提交等待与 `wait:none`+固定拍两种敲法结果数与标题全同(6 条/1.0s 对 6 条/2.8s)
- 结论:SERP 渲染等待由 goto 默认提交等待覆盖,编排里裸 sleep 退役;限速退避 sleep 保留为正用

## 2026-10-17 Rune 入口裸形定形

- 现象:入口写 `pub async fn main() -> Result` 编译错;Rune 不支持返回类型注解
- 结论:编排入口一律裸形 `pub async fn main() {`;旧 README 的 `-> Result` 形不引,以 workspace 仓头为准

## 2026-10-17 实弹敲法坑

- `--vars` 值含空格不整体引号:rune 报「只要一个脚本位」退出 2
- `browse userscript install` 路径按 CWD 解析:workspace 件用绝对径,README 相对径例形以 workspace 根为 CWD 前提
- 非终端 stdin 跑 `browse rune`:先打一行「管道读入为空串」提示,是噪音不是错,照常执行
