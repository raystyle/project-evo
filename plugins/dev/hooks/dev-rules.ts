#!/usr/bin/env bun
// dev-rules:PreToolUse(Edit|Write) 按路径注入开发规则(总台 hook_rules 体系,批 176)
// 规则面 = hook_rules/dev-rules/*.md(frontmatter match 字面子串或 /regex/ 形,正文 = 注入内容)
// 双层树:项目 .claude/hook_rules/dev-rules 先(项目优先),插件 CLAUDE_PLUGIN_ROOT/hook_rules/dev-rules 后,合并注入
// 加规则 = 加 md 件,本脚本零改;坑位:字面量换行用 String.fromCharCode(10),路径 env 锚定
import { join } from "node:path";
import { readdir } from "node:fs/promises";

const NL = String.fromCharCode(10);
const BS = String.fromCharCode(92);
const ruleDirs: string[] = [];
if (process.env.CLAUDE_PROJECT_DIR) {
  ruleDirs.push(join(process.env.CLAUDE_PROJECT_DIR, ".claude", "hook_rules", "dev-rules"));
}
if (process.env.CLAUDE_PLUGIN_ROOT) {
  ruleDirs.push(join(process.env.CLAUDE_PLUGIN_ROOT, "hook_rules", "dev-rules"));
}
if (ruleDirs.length === 0) ruleDirs.push(join(import.meta.dir, "..", "hook_rules", "dev-rules"));

const input = await Bun.stdin.json() as {
  tool_name?: string;
  tool_input?: { file_path?: string };
};
const tool = input.tool_name || "";
const filePath = (input.tool_input?.file_path || "").split(BS).join("/");

if (!["Edit", "Write"].includes(tool) || !filePath) process.exit(0);

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
      const pat = (fm.match || "").trim();
      if (!pat) continue;
      // match 形:字面子串或 /regex/ 形
      const isRe = pat.startsWith("/") && pat.lastIndexOf("/") > 0;
      const hit = isRe
        ? new RegExp(pat.slice(1, pat.lastIndexOf("/"))).test(filePath)
        : filePath.includes(pat);
      if (hit) guidances.push(body.trim());
    }
  } catch (e) {
    console.error("dev-rules: 规则面读败:", dir, e);
  }
}

if (guidances.length > 0) {
  console.log(JSON.stringify({
    hookSpecificOutput: {
      hookEventName: "PreToolUse",
      permissionDecision: "allow",
      additionalContext: guidances.join(NL + NL),
    },
  }));
}
