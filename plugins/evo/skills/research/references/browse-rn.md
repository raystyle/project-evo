# browse-rn:rn 编排五律与裸形入口

> 写多页采集、批量关键词、需循环分支异步的采集时读本篇;单页抽取用方言片段即可,不值编排。

## 入口契约（裸形）

Rune 不支持返回类型注解:入口 `pub async fn main() {`,错误用 `?` 传播、回值用 `Ok(..)`/`Err(..)`;旧 README 的 `-> Result` 形编译错,不引。原生 CDP `cdp::raw("Domain.method", params)`;封装 `cdp::goto(url)`、`cdp::js(code, args)`、`cdp::dialect(动词, 参)`;等待节流 `time::sleep(time::Duration::from_millis(..))`。

## 最小编排件（2026-10-17 本机实跑,无头引擎 bing 三条干净返回）

```rune
pub async fn main() {
    match cdp::goto("https://www.bing.com/search?q=rust+cdp").await {
        Ok(_) => (),
        Err(e) => { return Ok("{\"error\":\"goto:" + e.message + "\"}"); }
    }
    let out = match cdp::js(r#"function collect(args) {
  const out = [];
  for (const a of document.querySelectorAll('#b_results > li.b_algo h2 a')) {
    out.push({ title: a.textContent.trim(), href: a.href });
  }
  return JSON.stringify(out.slice(0, 3));
}
return collect(args);"#, #{}).await {
        Ok(v) => v,
        Err(e2) => { return Ok("{\"error\":\"js:" + e2.message + "\"}"); }
    };
    Ok(out)
}
```

存为 `.rn` 件后跑:`browse rune <编排件绝对径> --timeout 90`。

## 编排五律（重采集判例）

| 律 | 义 |
| --- | --- |
| JS 片尾必须 `return <fn>(args)` | 页内代码自调用收口;闭包不捕获外层变量,receipt 走 args 传入 |
| 会话自愈 | 开头先 `cdp::js` ping,Err 即 `cdp::dialect("newTab", "")` 重建;跨轮死会话是最高频故障 |
| 原子错误 | 失败面单 JSON 回执,已收数据不因后续段失败而丢 |
| 全等待段帽 | 每个等待段写死超时上限,不许裸等 |
| 限速退避保留 | 引擎间限速用 sleep 是正用;SERP 渲染等待不是 |

## 定谳与坑

- goto 默认提交等待已覆盖 SERP 就绪(A/B 对照:默认等待与 `wait:none`+固定拍结果全同),渲染裸 sleep 退役,只留限速退避
- `--vars 'k=v w'` 含空格必须整体引号:裂参后 rune 报「只要一个脚本位」退出 2
- 模板变量按 Jinja 渲染(`<%= 键 %>`,`default('x')` 兜底);未提供的键执行前退出 2
- 判读机消费例:`browse rune ~/.browse-rs/workspace/page-skills/google-search/mech.rn --vars 'q=rust cdp' --vars top=3 --timeout 180`,回执 verdict 族见 `channels.md` google 节
- workspace 生成物件(`mech.rn`、`probe.*.user.js`)勿手改,源在 build/
