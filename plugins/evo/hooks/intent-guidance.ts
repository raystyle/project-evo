#!/usr/bin/env bun
// intent-guidance:UserPromptSubmit 意图识别注入(总台 hook_rules 体系,批 176)
// 规则面 = hook_rules/intents/*.md(frontmatter patterns 词表,正文 = 注入内容)
// 双层树:项目 .claude/hook_rules/intents 先(项目优先),插件 CLAUDE_PLUGIN_ROOT/hook_rules/intents 后,合并注入
// 加规则 = 加 md 件,本脚本零改;坑位:字面量换行用 String.fromCharCode(10),路径 env 锚定
import { join } from "node:path";
import { readdir } from "node:fs/promises";

const NL = String.fromCharCode(10);
// 双层树:项目树 .claude/hook_rules/(先,项目优先)加插件树 hook_rules/(后),合并注入
const ruleDirs: string[] = [];
if (process.env.CLAUDE_PROJECT_DIR) {
  ruleDirs.push(join(process.env.CLAUDE_PROJECT_DIR, ".claude", "hook_rules", "intents"));
}
if (process.env.CLAUDE_PLUGIN_ROOT) {
  ruleDirs.push(join(process.env.CLAUDE_PLUGIN_ROOT, "hook_rules", "intents"));
}
if (ruleDirs.length === 0) ruleDirs.push(join(import.meta.dir, "..", "hook_rules", "intents"));

const input = await Bun.stdin.json() as { prompt?: string };
const prompt = (input.prompt || "").toLowerCase();

function parseFrontmatter(text: string): { fm: Record<string, string>; body: string } {
  const m = text.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n?([\s\S]*)$/);
  if (!m) return { fm: {}, body: text };
  const fm: Record<string, string> = {};
  for (const line of m[1].split(NL)) {
    const kv = line.match(/^(\w[\w-]*):\s*(.*)$/);
    if (kv) fm[kv[1]] = kv[2];
  }
  return { fm, body: m[2] };
}

const guidances: string[] = [];
for (const dir of ruleDirs) {
  try {
    for (const f of await readdir(dir)) {
      if (!f.endsWith(".md")) continue;
      const text = await Bun.file(join(dir, f)).text();
      const { fm, body } = parseFrontmatter(text);
      // patterns: [词1, 词2] 形
      const words = (fm.patterns || "").replace(/[[\]]/g, "").split(",").map((s) => s.trim().toLowerCase()).filter(Boolean);
      if (words.some((w) => prompt.includes(w))) {
        guidances.push(body.trim());
      }
    }
  } catch (e) {
    console.error("intent-guidance: 规则面读败:", dir, e);
  }
}

if (guidances.length > 0) {
  console.log(JSON.stringify({
    hookSpecificOutput: {
      hookEventName: "UserPromptSubmit",
      additionalContext: guidances.join(NL + NL),
    },
  }));
}
