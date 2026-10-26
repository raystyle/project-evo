---
patterns: [油猴, 探针, userscript, 漂移, SERP 壳, 动态页, probe 属性]
---

## research 油猴探针指导

- 判据:仅结构高频漂移面(社交时间线、SERP 动态壳)值装探针;稳定静态站直接方言 `--js` 抽取,不值装
- 两段式:骨架段 document-start(KB 级采样判 verdict,结果写 documentElement 的 probe 属性)+ 重段 document-idle(settled 后转 markdown 写回同属性);`@grant GM_xmlhttpRequest`、`@connect 127.0.0.1`
- 装法:`browse userscript install <骨架件> <重件> --restart`(路径按 CWD 解析,workspace 件用绝对径);读上报 `browse events --last N`(环满 1000 丢最旧)
- 现成件真源在 browse workspace `page-skills/`;生成物件勿手改,漂移修正走 workspace 仓 git 通道
