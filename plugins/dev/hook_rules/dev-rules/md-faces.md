---
match: .md
---

## md 写作纪律(改 md 时)

- 禁字四类:破折号/连接号、Unicode 箭头、emoji、智能引号与全角字母数字;提交挡板 md-guard --staged 必挂
- 标题禁括号(PE-10);文件名禁空格/括号/冒号(PE-05);中文语境半角标点属排版偏好非 error
- 行量纪律:AGENTS 200 行、CLAUDE 50 行(单行 @AGENTS.md 桥接)、SKILL.md 500 行内
- skill frontmatter 仅官方字段(name/description),description 三句形(做什么 + Use when 触发句 + 不要用于排除句)≤400 字符
- 断链:references 与正文相对链接须可达,md-ref-scan 挡板
