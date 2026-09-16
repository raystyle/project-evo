// 研究报告 PDF 渲染模板(Markdown 单一真源)
// 用法(由 scripts/render.py 拼装,也可手跑):
//   typst compile --root <项目根> --input md=/<报告相对路径>.md <模板> <输出>.pdf
//
// 版式口径:中文报告骨架
//   字体  正文宋体 / 标题黑体 / 章节华文中宋 / 加粗黑体 / 强调楷体
//   字号  题名二号(20pt) 章小三(15pt) 节四号(14pt) 正文小四(12pt) 引注五号(10.5pt)
//   段落  首行缩进 2 字符(所有段落),行距与段距 1.02em,两端对齐
//   表格  三线表;页码居中,页眉带报告名

#import "@preview/cmarker:0.1.10": render

#let md = sys.inputs.at("md", default: "/reports/report.md")
#let author = sys.inputs.at("author", default: "研究智能体")

// ---- 拆出题头区(首个二级标题之前)与正文 ----
#let lines = read(md).split("\n")
#let cut = lines.position(l => l.starts-with("## "))
#let title = lines.first().replace(regex("^#\\s+"), "").trim()
// 题名单独排版,其余题头(副题、编制信息、摘要、关键词)交给 cmarker
// 无二级标题时题头区取空串(().join 得 none,会让 cmarker 报 Markdown must be a string)
#let front = if cut == none { "" } else { lines.slice(1, cut).join("\n") }
#let body = if cut == none { lines.join("\n") } else { lines.slice(cut).join("\n") }

// ---- 字体(本机可用;Latin 用 Times,中文回落) ----
#let latin = (name: "Times New Roman", covers: "latin-in-cjk")
#let f-body = (latin, "SimSun")
#let f-hei = (latin, "SimHei")
#let f-zhong = (latin, "STZhongsong")
#let f-kai = (latin, "KaiTi")

#let ink = rgb("#1a1a1a")

#set document(title: title, author: author)

#set page(
  paper: "a4",
  margin: (x: 2.6cm, top: 2.5cm, bottom: 2.4cm),
  header: context {
    if counter(page).get().first() > 1 {
      set text(font: f-kai, size: 9pt, fill: luma(45%))
      align(center)[#title]
    }
  },
  footer: context {
    if counter(page).get().first() > 1 {
      set text(font: f-body, size: 9pt, fill: luma(45%))
      align(center, counter(page).display())
    }
  },
  header-ascent: 1em,
)

// ========== 题头区 ==========

#align(center, text(font: f-hei, size: 20pt, weight: 700, title))
#v(0.3em)

#[
  #set par(first-line-indent: 2em, leading: 1.02em, spacing: 2em)
  #set text(font: f-body, size: 12pt, fill: ink, lang: "zh", region: "cn")
  #show strong: set text(font: f-hei, weight: 400)
  #show emph: set text(font: f-kai)
  #show list: set text(font: f-body, size: 10.5pt)
  #show list: set par(first-line-indent: 0pt, leading: 1.02em, spacing: 0.3em)
  #set list(indent: 1.1em, spacing: 0.75em)
  #show quote: it => align(center, block(above: 0.8em, below: 1em, text(font: f-body, size: 12pt, it.body)))
  #show heading.where(level: 3): it => align(center, block(
    above: 1.2em,
    below: 1.4em,
    text(font: f-zhong, size: 15pt, weight: 700, it.body),
  ))
  #render(front)
]

#v(0.6em)

// ========== 目录(题名页内,正文另起一页)==========

#align(center, text(font: f-zhong, size: 15pt, weight: 700, [目　录]))
#v(0.9em)
#show outline.entry: set par(first-line-indent: 0pt, leading: 1.02em, spacing: 0.55em)
#show outline.entry: set text(font: f-body, size: 12pt)
#outline(title: none, depth: 2, indent: auto)
#v(1.1em)
#pagebreak()

// ========== 正文 ==========

#set text(font: f-body, size: 12pt, fill: ink, lang: "zh", region: "cn")
#set par(
  justify: true,
  leading: 1.02em,
  spacing: 1.02em,
  first-line-indent: (amount: 2em, all: true),
)

// 中文加粗换黑体;强调换楷体
#show strong: set text(font: f-hei, weight: 400)
#show emph: set text(font: f-kai)

// 列表、表格单元格与标题不首行缩进
#show list: set par(first-line-indent: 0pt)
#show enum: set par(first-line-indent: 0pt)
#show table.cell: set par(first-line-indent: 0pt)
#set list(indent: 2em, spacing: 0.4em)
#set enum(indent: 2em, spacing: 0.4em)

// ========== 章节标题:华文中宋,逐级递减 ==========

#show heading: set par(first-line-indent: 0pt)
#show heading: set block(above: 1.3em, below: 1.1em)
#show heading: set text(font: f-zhong, weight: 700, fill: ink)
#show heading.where(level: 2): set text(size: 15pt)
#show heading.where(level: 3): set text(size: 14pt)

// ========== 引用 ==========

#show quote: it => block(
  inset: (left: 10pt),
  above: 0.7em,
  below: 1em,
  text(fill: luma(30%), it.body),
)
#show quote: set par(first-line-indent: 0pt)

#show link: set text(fill: rgb("#0b4a8f"))

// ========== 三线表 ==========

#show table: t => {
  let n = t.rows.len()
  set table(
    stroke: (x, y) => (
      top: if y == 0 { 0.08em } else { none },
      bottom: if y == n - 1 { 0.08em } else if y == 0 { 0.05em } else { none },
      left: none,
      right: none,
    ),
    fill: none,
    inset: (x: 7pt, y: 5pt),
    align: left + horizon,
  )
  set text(font: f-body, size: 10.5pt)
  if t.columns.all(c => c == auto) {
    table(columns: (1fr,) * t.columns.len(), align: t.align, ..t.children)
  } else {
    t
  }
}
#show table: set block(above: 0.9em, below: 1.1em)

// ========== 正文 ==========

#render(body)
