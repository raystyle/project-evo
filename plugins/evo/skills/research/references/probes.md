# probes:油猴探针骨架与装法

> 页面结构高频漂移、`--js` 抽取失稳时读本篇;稳定静态站直接 `--js`,不值装探针。

## 判据:漂移面才值得探针

值装探针的页面 = 结构高频漂移面(社交时间线、SERP 动态壳);判读逻辑进探针后,选择器漂移只改探针不改编排。稳定静态站(文档站、产品页)用方言 `--js` 一次抽取即可。

## 两段式骨架

- 骨架段 `@run-at document-start`:KB 级采样与收齐引擎,唯一判读方;采样指纹、判 verdict、把结果写 `document.documentElement` 的 `probe` 属性
- 重段 `@run-at document-idle`:settled 后把 SERP/正文转 markdown,写回同一 `probe` 属性
- 油猴标准头:`@match` 域面、`@grant GM_xmlhttpRequest`、`@connect 127.0.0.1`(事件上报走本机 daemon `/events`)

## 装法与读法（2026-10-17 本机实装）

```bash
browse userscript install ~/.browse-rs/workspace/page-skills/google-search/probe.skeleton.user.js ~/.browse-rs/workspace/page-skills/google-search/probe.heavy.user.js --restart
browse events --last 20
```

- 装法要点:路径按 CWD 解析,workspace 件用绝对径或先 cd 到 workspace 根;多件一条命令装,`--restart` 让引擎重读
- 装后探针随 `@match` 自动注入对应页;编排侧只等 `probe` 属性 settled 信号(mech 模式)
- `browse events` 读上报事件环(满 1000 条丢最旧);`browse userscript list/enable/disable/remove` 管理
- 更换探针件后须 `--restart`;管理页 `chrome://userscripts`

## 现成件真源

google-search 两段式探针与判读机在 workspace `page-skills/google-search/`;antibot-vendor、gm-bridge、x-timeline 等手写源不经生成器。生成物件勿手改,漂移修正走 workspace 仓 git 通道,零 browse 发版。
