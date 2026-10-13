---
id: REQ-034
title: grok 业界先例评审吸收(收口、独立 semver、命名细节、distil 压缩、环境变量)
status: implemented
priority: must
trace: tests/test_project_evo.py
---

# REQ-034:grok 业界先例评审吸收

## Scenario

总台令(2026-10-13):让邻居 grok(w8:p4)对比业界先例优化市场重构终形。grok 六条评审送达(全文 /tmp/grok-evo-review.md,对照 Claude Code 插件市场、VS Code 扩展、npm scope 与 changesets、oh-my-zsh)。裁定:落五条,hold 一条(评审 2 拆 dev-lint 中文面与用户明令 lint 三合一相抵,候用户裁;评审 5 distil 归 dev 取轻形先压缩 description,目录不动候下轮)。

## Criteria

- [x] 收口:README 三处 evo-doc 残留、doc-gov 两路由行(evo:distil-skill 与 evo:dev-cli)、双插件 codex 面 shortDescription 与 defaultPrompt、AGENTS 当前阶段,全部随终形
- [x] 独立 semver:两插件各自升版本(本批各进 0.14.0),市场快照仍 git tag(下一号 v0.16.0 候打),守卫改独立校验(0.13 起可混装)
- [x] 命名细节:keywords 分域;agents description 加适用域句防读 AGENTS.md 误触发;四域 description 瘦身,共享规则只在 agents
- [x] distil description 压缩(约 767 字至约 350 字,触发词保留)
- [x] 环境变量:EVO_LINT_* 新名 DEV_LINT_*(旧名再认一版),hook-face 表随改;hook 与脚本归属保持(dev 插件根 + skill scripts)
- [x] 四门禁全绿 + fleet 回执 + 回信 grok(w8:p4);hold 项与 distil 目录迁移候用户裁
