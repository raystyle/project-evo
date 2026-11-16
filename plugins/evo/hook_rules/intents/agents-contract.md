---
patterns: [--llms, --json, 错误码, not_found, gate_refused, engine_fail, 退出码, 信封, CTA, 六入口, 文法, 动词标准]
---

## agents 域文法与输出契约(六入口共享面)

- 文法:`<命令> [全局旗标] <动词> [旗标] [位置参]`;全局旗标 --help -h --llms --json --format --full-output --filter-output --schema --force 任意槽;未知词 usage 退 2 禁静默 shift
- 两形同源:`--json` 机器形(单行信封 ok/data/meta,data 恒带 status),缺省人读形,字段序一致;错误一律 stderr,stdout 永纯数据
- 错误码四枚:not_found(名或机未命中,同名多格也走此)/ gate_refused(门控拒,--force 重发)/ engine_fail(引擎原文透传)/ usage(退 2);CTA 统一『下一步:』前缀
- 退出码 0/1/2 禁其他:拒投时 stdout 仍出 ok:true 信封但 exit 1,判定看退出码与 data.status 勿单信 ok;裸调用 = view,exit 0
- 动词标准(prim v5 全域统一):view = 清单与读、to = 留痕知会、start/close = 生命周期
- 六域速查:agents(to/wait/inbox/read/keys/mode/start/close/reload/trust/yolo/run/shell/dev/workbenches)、desks(view/start/close)、machines(view/add/reconnect/run/close/runtime)、streams(view/room/dm/append/to)、shares(view/put/get/to)、ctxs(view/search)
- 门控 v2:TUI 实况尾窗判标,只拒操作对话框,busy 排队不拦,误拒优于误投
