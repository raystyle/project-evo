---
patterns: [rn 编排, rune, 多页采集, 批量关键词, cdp, 采集编排, 循环采集]
---

## research rn 编排五律指导

- 适用:多页采集、批量关键词、需循环分支异步;单页抽取用方言片段不值编排
- 入口裸形:`pub async fn main() {`,错误 `?` 传播,回值 Ok/Err(Rune 不支持返回类型注解);CDP 原生 `cdp::raw("Domain.method", params)`,封装 `cdp::goto/js/dialect`,等待节流 `time::sleep`
- 语言基调 Rust without types:async 走 `.await`、无类型注解;语言面查 Rune 官方书(`browse fetch https://rune-rs.github.io/book/print.html --markdown` 全书单页直读),browse 封装面以 `browse --llms` 为准
- 编排侧等探针 `probe` 属性 settled 信号(mech 模式)
