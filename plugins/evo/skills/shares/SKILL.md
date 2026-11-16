---
name: shares
description: >-
  文件域原语:交付或取回一份已写完的文件。put 推送上桌回内容哈希键,
  get 按键取回落盘,to 留痕加知会(入流加 agents to 一发)。
  Use when: send the file, attach, fetch a share key, 传文件、取文件、交付产物、
  上架、取回。
  不要用于还在长的字节(上游管道域已退役,日志切片走 streams --file)
  或只发一条消息(走 agents/streams)。
---

知识面在本插件 hook_rules(技能直读):按需直读 `plugins/evo/hook_rules/` 下同名与拆件(注入面 2026-11-09 用户令剔除)。
