# herdr 飞轮治理操作坑

> 跨仓治理实操踩坑实录,按现象、根因、修法收录;新坑当场追加,二犯升格进 SKILL 正文纪律条目。

## 派单与回执面

| 坑 | 现象与根因 | 修法 |
|---|---|---|
| send-text 不是派单 | pane send-text 仅投草稿不提交,agent 不开始轮次 | 正式派单恒走 herdr agent prompt(原子文本加编码 Enter) |
| 工位编号漂移 | 合同或旧档写的编号与实况不符,凭记忆派单投错工位 | 派单前必 herdr agent list 实查,pane ID 从 JSON 响应取 |
| 备用屏读不全 | agent 跑在终端备用屏,加大 --lines 也读不到出屏行(出屏行不进宿主回滚缓冲) | 兜底:请对方把完整回执落临时 md 文件回路径,直读文件 |
| yolo 后落不追认 | agent 驻场在先、hst init --yolo 落盘在后,会话许可模式定格旧态,全会话审批阻塞 | 带起顺序恒 hst init --yolo 先于 agent 驻场;可提 hst doctor 加「会话活模式与盘上 yolo 一致性」检测项 |

## 仓级统一操作面

| 坑 | 现象与根因 | 修法 |
|---|---|---|
| checkout-index 假成功 | git checkout-index -f -a 对在场文件「强制重写」假成功,盘上 CRLF 原样不动;stat 缓存命中视为最新,-f 不真覆盖 | 清场再检出:git ls-files -z 加 xargs -0 rm -f 后 checkout-index -f -a |
| 整片 M 而 diff 空 | 工作树按索引重写后整片 M 但 diff 全空,似内容漂移实未变;索引条目 stat 陈旧的 racily-clean 形 | git add -u 刷索引条目即愈;收工前验 diff --cached 为零 |
