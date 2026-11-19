---
name: ccinit
description: >-
  项目 Claude 配置初始化:按六件资产分工(CLAUDE.md/rules/skills/agents/memory/hooks)
  加 .reference 参考仓规范,为项目铺设 .claude/ 基线。
  Use when: 初始化 Claude 配置、ccinit、给这个项目配 Claude、建 .claude、铺资产基线。
  不要用于已建成项目的日常维护迭代或与 Claude 配置无关的脚手架。
---

# ccinit:项目 Claude 配置初始化面

> 核心纪律:**六件资产各司其职,放错位置 = 上下文浪费或纪律失效**。

## 初始化流程(问项目、铺资产、验证)

### 第一步:勘察项目(先看再铺,不盲铺)

1. `ls` 仓根:有无 `CLAUDE.md`、`docs/`、`README.md`:已有配置先读后改,不覆盖
2. 问用户(或从 README 推断)三个定位问题:
   - **项目类型**(库 / 应用 / 基建 / 参考仓),决定 rules 的路径域怎么切
   - **有无写操作红线**(部署 / 生产环境 / 不可逆动作),决定要不要 hooks
   - **要不要先例参考面**(.reference/),研究型项目才要

### 第二步:铺六件资产(按分工表逐件落)

| 资产 | 职责 | 写入者 | 载入时机 | 判据 |
| --- | --- | --- | --- | --- |
| `CLAUDE.md`(仓根) | 项目常驻上下文:资产导航 + 仓规红线 | 人定稿 | 每会话首载 | **每个会话都要知道的事实**才进 |
| `.claude/rules/*.md` | 路径域规则 | 人 | 匹配 paths 时 | 只对某类文件要的规则(frontmatter 带 `paths:`) |
| `.claude/skills/<名>/` | 多步骤过程知识 | 人 | 调用时 | 过程性知识(步骤/流程/意图到工具映射) |
| `.claude/agents/*.md` | 子代理定义 | 人 | Agent 调用时 | 独立工具面 + 独立职责(如先例研究) |
| `.claude/memory/` | 会话性状态 + 学习指针 | Claude(auto) | 每会话 | 跨会话工作状态;**固化决策进 docs/ 后只留指针** |
| `.claude/hooks/` | 确定性强制 | 人 | 每次工具调用 | **必须拦的动作**;CLAUDE.md 只是约定,hook 才是闸门 |

**判据口诀**:每会话要的事实 = CLAUDE.md;某类文件的规则 = rules;过程 = skill;状态 = memory;强制 = hook;决策/需求/里程碑 = docs/(memory 只留指针)。

### 第三步:CLAUDE.md 骨架(仓根)

```markdown
# CLAUDE.md

<一两句项目定位>

## 三大资产导航
- `.claude/rules/`:<路径域规则一句话>
- `.claude/skills/`:<skill 清单一行一个>
- `.claude/memory/`:会话性记忆(固化决策在 docs/,此处只留指针)

## 仓规红线
- <不可违反的约定,一至三条;细节规则放 rules 不堆这里>
```

### 第四步:rules(带 paths frontmatter)

```markdown
---
paths:
  - "<目录>/**/*.ts"
---

# <域>规则

- **<规则一>**:<一句判据>(<违反后果/先例>)
```

规则内容来源:**项目踩过的坑**(战史),不是想象中的最佳实践。没坑可写的域不建 rule。

### 第五步:hooks(仅当有写操作红线)

```json
// .claude/settings.json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [{ "type": "command", "command": "<校验脚本,拦红线命令>" }]
      }
    ]
  }
}
```

hook 脚本读 stdin JSON,拦则 exit 2 加 stderr 说明。**没有红线不建 hook**(hook 失败会阻塞正常流)。

## .reference/ 参考仓规范(研究型项目可选)

`.reference/` 放**外部参考的项目仓库与文档**:供本项目的先例研究子代理只读查阅的先例语料(整仓快照或源码与文档片段),是「外部经验进本仓」的唯一落点,运行时绝不写入。

布局:

```text
.reference/
├── <仓或 case 名>/
│   ├── (源码片段、文档或整仓快照)
│   ├── NOTES.md          # 结论:机制/判据/坑,≤60 行
│   └── _provenance.yaml  # repo/commit/license/fetched/reason
```

纪律:

- **只读**:运行时绝不写入;唯一写入者是先例研究子代理(agents/precedent-researcher.md)
- **出处链**:`_provenance.yaml` 必填 repo / commit / original_path / license / fetched / reason;归档文件与上游 pin commit 字节一致(git hash-object 比对)
- **片段优先**:整仓只收「趟坑证据最强」的;其余片段级(源文件或文档加 NOTES)
- **索引**:CLAUDE.md 或 .reference/README.md 维护一张表(目录 / 是什么 / 技术栈 / 快照版本)

## 验证清单(铺完自查)

- [ ] CLAUDE.md < 100 行(超了说明塞了 rules 该管的内容)
- [ ] 每条 rule 的 paths 能真实匹配项目文件
- [ ] skills 的 description 含触发词(用户会怎么说)
- [ ] memory/ 有 MEMORY.md 索引(一行一记忆)
- [ ] hooks 只拦红线,失败路径可测(故意触发一次)
- [ ] .reference/ 每目录有 _provenance.yaml

## 判例

- **memory 不复制 docs**:固化决策写 docs/(decisions/requirements/planning),memory 只留指针(否则双份漂移)
- **rules 省 context**:路径域规则只在触及时载入,CLAUDE.md 塞满 = 每会话浪费
- **hook 是闸门不是约定**:CLAUDE.md 写「禁止 X」没人半夜三点还记得,hook 拦得住
- **先例归档先出候选清单**:研究代理列仓等用户点名,绝不擅自写 .reference/
