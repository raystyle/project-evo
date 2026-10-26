"""project-evo 脚本与插件面测试。

脚本为 PEP 723 零依赖形态,仓自用工具从 .tools/ 加载、md-guard 从插件级 scripts/ 加载(无安装态包,单源无副本)。
覆盖:init 幂等、check 抓违(PE-01/PE-11/围栏感知)、scan 历史泄漏与 md 告警、
退出码、市场清单与双 manifest 一致性守卫(改一面须同步另一面)。
"""

from __future__ import annotations

import importlib.util
import json
import os
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
PLUGIN_NAMES = ("dev", "evo")
PLUGINS = {n: REPO / "plugins" / n for n in PLUGIN_NAMES}
SCRIPTS = REPO / ".tools"
GUARD = PLUGINS["dev"] / "scripts" / "md-guard.py"
LINT_HOOK = PLUGINS["dev"] / "scripts" / "lint-hook.py"
SKILLS = {
    "dev": ["dev-cli", "dev-doc"],
    "evo": ["agents", "ctxs", "desks", "distil", "machines", "mcps", "pipes", "ports", "research", "shares", "streams", "tasks"],
}
HOOK_RULES = {  # 批 176 知识面:skill 壳指路,知识本体在 hook_rules(ADR-0027)
    "dev": {"intents": 6, "dev-rules": 4},
    "evo": {"intents": 26, "dev-rules": 0},
}


def _load(name: str):
    spec = importlib.util.spec_from_file_location(f"pevo_{name}", SCRIPTS / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


init_mod = _load("init")
check_mod = _load("check")
scan_mod = _load("scan")


def test_scaffold_creates_and_idempotent(tmp_path: Path):
    created, skipped = init_mod.generate(tmp_path, "demo")
    assert len(created) >= 10, "骨架文件不少于 10 件"
    assert (tmp_path / "AGENTS.md").exists()
    assert "demo" in (tmp_path / "AGENTS.md").read_text(encoding="utf-8"), "AGENTS 标题渲染项目名"
    assert (tmp_path / "docs" / "adr" / "0000-template.md").exists()
    assert (tmp_path / "docs" / "requirements" / "0000-template.md").exists()
    assert "{name}" not in (tmp_path / "AGENTS.md").read_text(encoding="utf-8"), "占位符已渲染"
    # 幂等:二次生成全跳过,内容不变
    before = (tmp_path / "AGENTS.md").read_text(encoding="utf-8")
    created2, skipped2 = init_mod.generate(tmp_path, "demo")
    assert not created2 and len(skipped2) == len(created)
    assert (tmp_path / "AGENTS.md").read_text(encoding="utf-8") == before, "已有文件不被覆盖"


def test_check_passes_on_scaffold(tmp_path: Path):
    init_mod.generate(tmp_path, "demo")
    results, ok = check_mod.check(tmp_path)
    assert ok, [r for r in results if r[1] == "FAIL"]


def test_check_catches_violations(tmp_path: Path):
    init_mod.generate(tmp_path, "demo")
    (tmp_path / "AGENTS.md").unlink()  # PE-01 是 AGENTS 五节合同
    results, ok = check_mod.check(tmp_path)
    assert not ok
    assert "PE-01" in {r[0] for r in results if r[1] == "FAIL"}, "缺 AGENTS 应被 PE-01 抓住"


def test_check_adr_state_machine(tmp_path: Path):
    """PE-06:status 非法与 superseded_by 悬空都要 FAIL,合法状态过。"""
    init_mod.generate(tmp_path, "demo")
    adr = tmp_path / "docs" / "adr"
    (adr / "ADR-0001-选库.md").write_text(
        "---\nid: ADR-0001\nstatus: accepted\ndate: 2026-09-15\n---\n# ADR-0001\n", encoding="utf-8")
    (adr / "ADR-0002-换库.md").write_text(
        "---\nid: ADR-0002\nstatus: bogus\n---\n# ADR-0002\n", encoding="utf-8")
    (adr / "ADR-0003-又换.md").write_text(
        "---\nid: ADR-0003\nstatus: superseded\nsuperseded_by: ADR-0099\n---\n# ADR-0003\n",
        encoding="utf-8")
    results, _ = check_mod.check(tmp_path)
    fails = {r[0]: r[2] for r in results if r[1] == "FAIL"}
    assert "PE-06" in fails and "bogus" in fails["PE-06"], "非法 status 应被 PE-06 抓住"
    assert "悬空" in fails["PE-06"], "superseded_by 悬空应被 PE-06 抓住"
    # 修成合法状态与可达 supersede 链后 PE-06 通过
    (adr / "ADR-0002-换库.md").write_text(
        "---\nid: ADR-0002\nstatus: proposed\n---\n# ADR-0002\n", encoding="utf-8")
    (adr / "ADR-0003-又换.md").write_text(
        "---\nid: ADR-0003\nstatus: superseded\nsuperseded_by: ADR-0001\n---\n# ADR-0003\n",
        encoding="utf-8")
    results, _ = check_mod.check(tmp_path)
    assert "PE-06" not in {r[0] for r in results if r[1] == "FAIL"}


def test_check_req_trace_and_index(tmp_path: Path):
    """PE-07:implemented 缺 trace FAIL;PE-08:未登记索引 FAIL。"""
    init_mod.generate(tmp_path, "demo")
    req = tmp_path / "docs" / "requirements"
    (req / "REQ-001-骨架.md").write_text(
        "---\nid: REQ-001\nstatus: implemented\npriority: must\ntrace: null\n---\n# REQ-001\n",
        encoding="utf-8")
    results, _ = check_mod.check(tmp_path)
    fails = {r[0]: r[2] for r in results if r[1] == "FAIL"}
    assert "PE-07" in fails and "trace" in fails["PE-07"], "implemented 缺 trace 应被 PE-07 抓住"
    assert "PE-08" in fails and "REQ-001" in fails["PE-08"], "未登记索引应被 PE-08 抓住"


def test_check_title_bracket(tmp_path: Path):
    init_mod.generate(tmp_path, "demo")
    (tmp_path / "docs" / "guides" / "cook-面条.md").write_text(
        "# 指南:命名(详版)\n\n## 一、命名\n", encoding="utf-8"
    )
    _, ok = check_mod.check(tmp_path)
    assert not ok, "标题带括号应被 PE-10 抓住"


def test_check_ignores_fenced_code_comments(tmp_path: Path):
    """代码块内的 # 注释带括号不算标题违规(PE-10 围栏感知)。"""
    init_mod.generate(tmp_path, "demo")
    (tmp_path / "docs" / "guides" / "cook-面条.md").write_text(
        "# 指南\n\n## 命名\n\n```powershell\n"
        "# 1. 看 skill 本体(意图路由入口)\nGet-Content SKILL.md\n```\n",
        encoding="utf-8",
    )
    _, ok = check_mod.check(tmp_path)
    assert ok, "围栏内 # 注释不应触发 PE-10"


def test_check_pe11_allowlist_exempts_history(tmp_path: Path, monkeypatch):
    """PEVO_CHECK_ALLOW 命中的历史档案禁字报 SKIP 不 FAIL,豁免不掩护活跃面。"""
    init_mod.generate(tmp_path, "demo")
    (tmp_path / "docs" / "diary" / "2026-01-01-旧档.md").write_text(
        "# 旧档\n\n改造走向全量镜像 —— 第一批落定\n", encoding="utf-8"
    )
    monkeypatch.delenv("PEVO_CHECK_ALLOW", raising=False)
    _, ok = check_mod.check(tmp_path)
    assert not ok, "未设豁免时存量禁字应 FAIL"
    monkeypatch.setenv("PEVO_CHECK_ALLOW", r"docs/diary/2026-01-01-旧档\.md:3")
    results, ok = check_mod.check(tmp_path)
    assert ok, "豁免命中后应通过(退出码 0)"
    pe11 = next(r for r in results if r[0] == "PE-11")
    assert pe11[1] == "SKIP", "豁免面应显式报 SKIP 留审计痕迹"
    (tmp_path / "README.md").write_text("# demo\n\n走向 —— 全量\n", encoding="utf-8")
    monkeypatch.setenv("PEVO_CHECK_ALLOW", ".*")
    _, ok = check_mod.check(tmp_path)
    assert not ok, "根三件是活跃面,全域正则也不得掩护"


def test_check_reports_all_violations(tmp_path: Path):
    """全量报告:单检查超 5 处全量列出;PE-11 同文件逐行列出(旧逻辑只报首行与前 5)。"""
    init_mod.generate(tmp_path, "demo")
    (tmp_path / "docs" / "guides" / "many-bad.md").write_text(
        "# 指南\n\n" + "".join(f"## 小节{i}(注)\n\n" for i in range(7)), encoding="utf-8")
    (tmp_path / "docs" / "diary" / "2026-01-02-多犯.md").write_text(
        "# 档案\n\n" + "".join(f"第{i}批 —— 存量\n\n" for i in range(6)), encoding="utf-8")
    results, _ = check_mod.check(tmp_path)
    pe10 = next(r for r in results if r[0] == "PE-10")
    pe11 = next(r for r in results if r[0] == "PE-11")
    assert len(pe10[3]) == 7, "PE-10 七处违规应全量进 violations(旧截断只报 5)"
    assert pe10[2].count("docs/guides/many-bad.md:") == 7, "人读 note 同样全量"
    diary_hits = [v for v in pe11[3] if v.startswith("docs/diary/2026-01-02-多犯.md:")]
    assert len(diary_hits) == 6, "PE-11 同文件六行应逐行列出(旧逻辑每文件只报首行)"


def _git(cwd: Path, *args: str) -> None:
    subprocess.run(["git", "-C", str(cwd), *args], check=True, capture_output=True,
                   env={**__import__("os").environ, "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t",
                        "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@t"})


def test_scan_finds_secret_in_history(tmp_path: Path):
    _git(tmp_path, "init", "-b", "main")
    (tmp_path / "cfg.txt").write_text("token = ghp_0123456789abcdefghijklmnop\n", encoding="utf-8")
    _git(tmp_path, "add", "-A"); _git(tmp_path, "commit", "-m", "leak")
    (tmp_path / "cfg.txt").unlink()
    _git(tmp_path, "add", "-A"); _git(tmp_path, "commit", "-m", "remove")
    finds = scan_mod.scan_history_secrets(tmp_path)
    assert any(f["rule"] == "GitHub token" for f in finds), "历史中的 token 应被抓到"
    _, clean = scan_mod.run_scan(tmp_path)
    assert not clean
    # 报告脱敏:不回显完整 token
    joined = " ".join(f["snippet"] for f in finds)
    assert "ghp_0123456789abcdefghijklmnop" not in joined


def test_scan_md_reports_file_and_line(tmp_path: Path):
    (tmp_path / "A.md").write_text(
        "# 标题\n\n规则:登记到立项——执行“完”\n\n```text\n# 注释(豁免)—— →\n```\n",
        encoding="utf-8",
    )
    finds, clean = scan_mod.run_scan(tmp_path, history=False)
    assert not clean
    md = [f for f in finds if f["kind"] == "md"]
    assert md and md[0]["file"] == "A.md" and md[0]["line"] == 3, "标注文件与行号"
    assert any("破折号" in f["rule"] for f in md) and any("智能引号" in f["rule"] for f in md)
    assert all(f["line"] != 6 for f in md), "围栏内豁免"


def test_init_creates_missing_target(tmp_path: Path):
    """脚手架语义:目标目录不存在则创建(同日两犯升格:本地 e2e 与 CI 冒烟各踩一次)。"""
    target = tmp_path / "nested" / "demo"
    r = subprocess.run([sys.executable, str(SCRIPTS / "init.py"), str(target), "--name", "demo"],
                       capture_output=True, text=True, encoding="utf-8")
    assert r.returncode == 0, r.stderr
    assert (target / "AGENTS.md").is_file()


def test_check_script_exit_codes(tmp_path: Path):
    """子进程直跑:PEP 723 零依赖,系统 python 即可;退出码 0/1。"""
    init_mod.generate(tmp_path, "demo")
    r_ok = subprocess.run([sys.executable, str(SCRIPTS / "check.py"), str(tmp_path)],
                          capture_output=True, text=True, encoding="utf-8")
    assert r_ok.returncode == 0, r_ok.stdout + r_ok.stderr
    (tmp_path / "AGENTS.md").unlink()
    r_bad = subprocess.run([sys.executable, str(SCRIPTS / "check.py"), str(tmp_path)],
                           capture_output=True, text=True, encoding="utf-8")
    assert r_bad.returncode == 1


def test_check_json_clean_scaffold(tmp_path: Path):
    """--json 干净脚手架:JSON 取代人读表,schema 形状与计数,violations 全空,退出码 0。"""
    init_mod.generate(tmp_path, "demo")
    r = subprocess.run([sys.executable, str(SCRIPTS / "check.py"), str(tmp_path), "--json"],
                       capture_output=True, text=True, encoding="utf-8")
    assert r.returncode == 0, r.stdout + r.stderr
    assert r.stdout.lstrip().startswith("{")
    data = json.loads(r.stdout)
    assert data["ok"] is True
    assert data["counts"] == {"pass": 10, "fail": 0, "skip": 3}, "脚手架态 PE-06/07/09 SKIP"
    assert [x["id"] for x in data["results"]] == [f"PE-{i:02d}" for i in range(1, 14)]
    assert all(x["violations"] == [] for x in data["results"])
    assert all(set(x) == {"id", "status", "note", "violations"} for x in data["results"])


def test_check_json_failures_list_violations(tmp_path: Path):
    """--json 注错面:violations 为 file:line 串且非空,退出码 1。"""
    init_mod.generate(tmp_path, "demo")
    (tmp_path / "docs" / "guides" / "bad.md").write_text(
        "# 指南\n\n## 小节(注)\n\n坏行 —— 连接\n", encoding="utf-8")
    r = subprocess.run([sys.executable, str(SCRIPTS / "check.py"), str(tmp_path), "--json"],
                       capture_output=True, text=True, encoding="utf-8")
    assert r.returncode == 1
    data = json.loads(r.stdout)
    assert data["ok"] is False and data["counts"]["fail"] == 2
    by_id = {x["id"]: x for x in data["results"]}
    assert by_id["PE-10"]["violations"] == ["docs/guides/bad.md:3"]
    assert by_id["PE-11"]["violations"] == ["docs/guides/bad.md:5(破折号/连接号)"]


def test_check_json_skip_counts_via_allow(tmp_path: Path):
    """--json 豁免面:PEVO_CHECK_ALLOW 命中报 SKIP,counts.skip 直读(取代正则抓结论行)。"""
    init_mod.generate(tmp_path, "demo")
    (tmp_path / "docs" / "diary" / "2026-01-01-旧档.md").write_text(
        "# 旧档\n\n存量 —— 禁字\n", encoding="utf-8")
    r = subprocess.run([sys.executable, str(SCRIPTS / "check.py"), str(tmp_path), "--json"],
                       capture_output=True, text=True, encoding="utf-8",
                       env={**os.environ, "PEVO_CHECK_ALLOW": r"docs/diary/2026-01-01-旧档\.md:3"})
    assert r.returncode == 0, r.stdout + r.stderr
    data = json.loads(r.stdout)
    pe11 = next(x for x in data["results"] if x["id"] == "PE-11")
    assert pe11["status"] == "SKIP" and pe11["violations"] == [], "豁免行不进 violations"
    assert data["counts"]["skip"] == 4, "脚手架 3 处 SKIP 加豁免 PE-11"


def test_check_pe13_term_allowlist(tmp_path: Path):
    """PE-13 术语面:违规 FAIL、PEVO_TERM_ALLOW 豁免 docs/ 报 SKIP、根三件永不受益。"""
    init_mod.generate(tmp_path, "demo")
    (tmp_path / "docs" / "diary" / "2026-01-01-旧档.md").write_text(
        "# 旧档\n\n这方案是个抓手\n", encoding="utf-8")
    r_bad = subprocess.run([sys.executable, str(SCRIPTS / "check.py"), str(tmp_path), "--json"],
                           capture_output=True, text=True, encoding="utf-8")
    assert r_bad.returncode == 1
    data = json.loads(r_bad.stdout)
    pe13 = next(x for x in data["results"] if x["id"] == "PE-13")
    assert pe13["status"] == "FAIL" and any("抓手" in v for v in pe13["violations"])

    r_ok = subprocess.run([sys.executable, str(SCRIPTS / "check.py"), str(tmp_path), "--json"],
                          capture_output=True, text=True, encoding="utf-8",
                          env={**os.environ, "PEVO_TERM_ALLOW": r"docs/diary/2026-01-01-旧档\.md:3"})
    data = json.loads(r_ok.stdout)
    assert data["ok"] is True, r_ok.stdout
    pe13 = next(x for x in data["results"] if x["id"] == "PE-13")
    assert pe13["status"] == "SKIP", "豁免命中报 SKIP 不 FAIL"

    (tmp_path / "README.md").write_text("# demo\n\n这方案是个抓手\n", encoding="utf-8")
    r_root = subprocess.run([sys.executable, str(SCRIPTS / "check.py"), str(tmp_path), "--json"],
                            capture_output=True, text=True, encoding="utf-8",
                            env={**os.environ, "PEVO_TERM_ALLOW": ".*"})
    data = json.loads(r_root.stdout)
    pe13 = next(x for x in data["results"] if x["id"] == "PE-13")
    assert pe13["status"] == "FAIL", "根三件永不受益(与 PEVO_CHECK_ALLOW 同律)"


def test_term_lint_exit_codes(tmp_path: Path):
    """term-lint 三态退出码:0 净 / 1 违规 / 2 无参用法错。"""
    term_lint = PLUGINS["dev"] / "scripts" / "term-lint.py"
    clean = tmp_path / "clean.md"
    clean.write_text("干净一行\n", encoding="utf-8")
    dirty = tmp_path / "dirty.md"
    dirty.write_text("这方案是个抓手\n", encoding="utf-8")
    r0 = subprocess.run([sys.executable, str(term_lint), str(clean)],
                        capture_output=True, text=True, encoding="utf-8")
    assert r0.returncode == 0
    r1 = subprocess.run([sys.executable, str(term_lint), str(dirty)],
                        capture_output=True, text=True, encoding="utf-8")
    assert r1.returncode == 1 and "抓手" in r1.stdout
    r2 = subprocess.run([sys.executable, str(term_lint)],
                        capture_output=True, text=True, encoding="utf-8")
    assert r2.returncode == 2


def test_termrules_table_sanity():
    """词表健全:四层 ENFORCED 表非空、键不跨表重复、PENDING 与 ENFORCED 不相交、修法非空。"""
    spec = importlib.util.spec_from_file_location(
        "pevo_termrules", PLUGINS["dev"] / "scripts" / "termrules.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    enforced = [mod.ZH_BANNED, mod.ZH_CHOICE, mod.EN_JARGON, mod.TERM_VARIANTS]
    assert mod.ZH_BANNED and mod.ZH_CHOICE and mod.EN_JARGON, "三层主表须非空"
    assert isinstance(mod.PENDING, dict) and mod.PENDING, "PENDING 存量层须在位"
    seen: set[str] = set()
    for tbl in enforced:
        for w, fix in tbl.items():
            assert w and fix, f"条目须词与修法齐: {w!r}"
            assert w not in seen, f"跨表重复词: {w}"
            seen.add(w)
    assert not seen & set(mod.PENDING), f"ENFORCED 与 PENDING 相交: {seen & set(mod.PENDING)}"
    """清单守卫:市场名 project-evo 收两插件、双清单一致、每插件双 manifest 与市场版本同步、
    两插件独立 semver(0.13 起可混装,批 142)、skill 分属正确与 hook 面在位(ADR-0025 市场重构,dev 与 evo)。"""
    claude_mkt = json.loads((REPO / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
    codex_mkt = json.loads((REPO / ".agents" / "plugins" / "marketplace.json").read_text(encoding="utf-8"))
    assert claude_mkt["name"] == codex_mkt["name"] == "project-evo", "市场名须为 project-evo"

    names_c = {p["name"] for p in claude_mkt["plugins"]}
    names_x = {p["name"] for p in codex_mkt["plugins"]}
    assert names_c == names_x == set(PLUGIN_NAMES), f"市场恰收两插件(ADR-0025): {names_c}"
    for p in claude_mkt["plugins"]:
        assert (REPO / p["source"].removeprefix("./")).is_dir(), f"Claude source 不可达: {p['source']}"
    for p in codex_mkt["plugins"]:
        assert (REPO / p["source"]["path"].removeprefix("./")).is_dir(), "Codex source 不可达"

    versions = set()
    for name in PLUGIN_NAMES:
        plugin = PLUGINS[name]
        claude_man = json.loads((plugin / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
        codex_man = json.loads((plugin / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
        for k in ("name", "version", "description"):
            assert claude_man[k] == codex_man[k], f"{name} 双 manifest 的 {k} 漂移,须同步改两面"
        entry = next(p for p in claude_mkt["plugins"] if p["name"] == name)
        assert entry["version"] == claude_man["version"], f"{name} 市场清单版本与 manifest 漂移"
        versions.add(claude_man["version"])

        skills = plugin / "skills"
        dirs = sorted(d.name for d in skills.iterdir() if d.is_dir())
        assert dirs == sorted(SKILLS[name]), f"{name} 的 skills 须为 {sorted(SKILLS[name])}: {dirs}"
        for sname in dirs:
            text = (skills / sname / "SKILL.md").read_text(encoding="utf-8")
            assert text.startswith("---\n"), f"{sname}/SKILL.md 缺 frontmatter"
            head = text.split("---")[1]
            declared = next(l.split(":", 1)[1].strip() for l in head.splitlines() if l.startswith("name:"))
            assert declared == sname, f"frontmatter name({declared}) 须与目录名({sname})一致"
            assert "hook_rules" in text, f"{sname}/SKILL.md 薄壳缺 hook_rules 指路行(批 176)"

    for v in versions:
        parts = tuple(int(x) for x in v.split("."))
        assert parts >= (0, 13), f"两插件独立 semver,起步线 0.13 可混装(grok 评审批 142): {v}"

    tools = REPO / ".tools"
    for s in ("init.py", "check.py", "scan.py", "md-ref-scan.py"):
        assert (tools / s).is_file(), f"仓工具缺失: {s}"
    assert (tools / "templates").is_dir(), ".tools 缺骨架模板目录"
    plugin_scripts = PLUGINS["dev"] / "scripts"
    for s in ("md-guard.py", "mdrules.py", "lint-hook.py",
              "termrules.py", "term-lint.py", "term-mine.py"):
        assert (plugin_scripts / s).is_file(), f"插件级脚本缺失: {s}"


def _run_md_guard(payload: str) -> subprocess.CompletedProcess:
    env = {**os.environ, "PYTHONIOENCODING": "utf-8"}
    return subprocess.run(
        [sys.executable, str(GUARD)],
        input=payload, capture_output=True, text=True, encoding="utf-8",
        errors="replace", env=env,
    )


def test_md_guard_hook_tolerates_alien_payload(tmp_path: Path):
    """Codex apply_patch 面载荷宽容:tool_input 是对象但无 file_path,或整体不是对象,均放行 0。"""
    codex_shape = json.dumps({
        "hook_event_name": "PostToolUse",
        "tool_name": "apply_patch",
        "tool_input": {"command": "*** Begin Patch\n*** Update File: note.md\n+x\n*** End Patch\n"},
        "tool_response": "Success. Updated files.",
    })
    assert _run_md_guard(codex_shape).returncode == 0
    alien_shape = json.dumps({"hook_event_name": "PostToolUse", "tool_input": "*** Begin Patch"})
    assert _run_md_guard(alien_shape).returncode == 0
    assert _run_md_guard("not json at all").returncode == 0


def test_md_guard_hook_flags_forbidden_chars(tmp_path: Path):
    """Claude 面判据不回退:file_path 指向含禁字的 .md 时退出 2 并写 stderr。"""
    bad = tmp_path / "bad.md"
    bad.write_text("正常一行\n带破折号 \u2014 的一行\n", encoding="utf-8")
    bad_payload = json.dumps({"hook_event_name": "PostToolUse", "tool_input": {"file_path": str(bad)}})
    r = _run_md_guard(bad_payload)
    assert r.returncode == 2, r.stdout + r.stderr
    assert "禁字" in r.stderr
    clean = tmp_path / "ok.md"
    clean.write_text("干净一行\n", encoding="utf-8")
    ok_payload = json.dumps({"hook_event_name": "PostToolUse", "tool_input": {"file_path": str(clean)}})
    assert _run_md_guard(ok_payload).returncode == 0


def test_md_guard_hook_scopes_to_event_cwd(tmp_path: Path):
    """挡板辖域限仓内(ADR-0017 同批裁定):事件带 cwd 且 file_path 在其外时放行,在内照检。"""
    bad = tmp_path / "bad.md"
    bad.write_text("带箭头 → 的一行\n", encoding="utf-8")
    outside = json.dumps({"hook_event_name": "PostToolUse", "cwd": str(tmp_path / "repo"),
                          "tool_input": {"file_path": str(bad)}})
    assert _run_md_guard(outside).returncode == 0, "仓外 md 不在挡板辖域,应放行"
    inside = json.dumps({"hook_event_name": "PostToolUse", "cwd": str(tmp_path),
                         "tool_input": {"file_path": str(bad)}})
    assert _run_md_guard(inside).returncode == 2, "仓内 md 照检"


def _run_lint_hook(payload: str) -> subprocess.CompletedProcess:
    env = {**os.environ, "PYTHONIOENCODING": "utf-8"}
    return subprocess.run(
        [sys.executable, str(LINT_HOOK)],
        input=payload, capture_output=True, text=True, encoding="utf-8",
        errors="replace", env=env,
    )


def test_lint_hook_tolerates_alien_payload():
    """evo-lint hook 载荷宽容:Codex apply_patch 形(有 tool_input 无 file_path)与非对象整体均放行 0。"""
    codex_shape = json.dumps({
        "hook_event_name": "PostToolUse",
        "tool_name": "apply_patch",
        "tool_input": {"command": "*** Begin Patch\n*** Update File: note.md\n+x\n*** End Patch\n"},
    })
    assert _run_lint_hook(codex_shape).returncode == 0
    assert _run_lint_hook(json.dumps({"tool_name": "Edit", "tool_input": {}})).returncode == 0
    assert _run_lint_hook("not json at all").returncode == 0


def test_lint_hook_flags_md_forbidden(tmp_path: Path):
    """evo-lint hook md 面:禁字与超限退出码 2 加 stderr 报错信息;净文件放行 0。"""
    bad = tmp_path / "AGENTS.md"
    bad.write_text("# 合同\n\n正文 —— 有破折号\n", encoding="utf-8")
    r = _run_lint_hook(json.dumps({
        "hook_event_name": "PostToolUse", "tool_name": "Write",
        "tool_input": {"file_path": str(bad)},
    }))
    assert r.returncode == 2, "禁字须 exit 2 回传报错"
    assert "禁字" in (r.stderr or "")

    good = tmp_path / "AGENTS.md"
    good.write_text("# 合同\n\n正文无禁字\n", encoding="utf-8")
    r2 = _run_lint_hook(json.dumps({
        "hook_event_name": "PostToolUse", "tool_name": "Write",
        "tool_input": {"file_path": str(good)},
    }))
    assert r2.returncode == 0


def test_live_md_hook_stays_removed():
    """批 105/174 裁撤:live PostToolUse 禁字静检 hook(插件 hooks.json 与仓 settings.json)不得回潮。

    历史:hook 实时拦编辑当日四犯(本仓三笔破折号加一笔标题括号),下游仓自有豁免面三度误拦;
    裁撤后禁字纪律由 githooks pre-commit 的 --staged 挡板与 check.py PE-11 承担,
    脚本本体保留。批 176(ADR-0027)hooks.json 重启用,但只挂 UserPromptSubmit 与
    PreToolUse 注入面(intent-guidance/dev-rules 加载器);PostToolUse 禁令不破:段存在即红。
    """
    hooks = json.loads((PLUGINS["dev"] / "hooks" / "hooks.json").read_text(encoding="utf-8"))
    assert not hooks.get("hooks", {}).get("PostToolUse"), \
        "hooks.json 不得回挂 PostToolUse hook(批 105 禁字面裁撤、批 174 静检面整段裁撤)"
    cmds = " ".join(h.get("command", "") + h.get("commandWindows", "")
                    for g in hooks.get("hooks", {}).get("PostToolUse", []) for h in g.get("hooks", []))
    assert "md-guard" not in cmds, "md-guard 不得作 live hook(批 105 裁撤),只走 pre-commit --staged"
    settings = json.loads((REPO / ".claude" / "settings.json").read_text(encoding="utf-8"))
    assert not settings.get("hooks", {}).get("PostToolUse"), \
        "仓 settings.json 不得回挂 live PostToolUse 禁字挡板(批 105 裁撤)"


def test_hook_loaders_wired_and_isolated():
    """批 176 注入面守卫:两插件各挂 UserPromptSubmit + PreToolUse(Edit|Write),命令花括号形;
    statusMessage 英文短形带插件前缀;加载器双拷贝字节等一(dev 正源,evo 拷贝,双 manifest 同步先例)。"""
    for name in PLUGIN_NAMES:
        plugin = PLUGINS[name]
        hooks = json.loads((plugin / "hooks" / "hooks.json").read_text(encoding="utf-8"))
        events = hooks.get("hooks", {})
        assert set(events) == {"UserPromptSubmit", "PreToolUse"}, \
            f"{name} hooks.json 须恰挂 UserPromptSubmit + PreToolUse(批 176),实际 {sorted(events)}"
        for group in events["PreToolUse"]:
            assert group.get("matcher") == "Edit|Write", f"{name} PreToolUse 须限 Edit|Write"
        for ev, groups in events.items():
            for g in groups:
                for h in g["hooks"]:
                    for field in ("command",):
                        cmd = h.get(field, "")
                        assert "${CLAUDE_PLUGIN_ROOT}" in cmd, f"{name} {field} 须花括号形: {cmd}"
                        assert "$env:" not in cmd, f"{name} {field} 禁 PowerShell 语法"
                    msg = h.get("statusMessage", "")
                    assert msg.startswith(f"{name} "), f"{name} statusMessage 须带插件前缀: {msg}"
                    title = msg.removeprefix(f"{name} ")
                    assert re.fullmatch(r"[a-z0-9-]+", title), f"{name} statusMessage 段名须英文短形: {msg}"
    for f in ("intent-guidance.ts", "dev-rules.ts"):
        a = (PLUGINS["dev"] / "hooks" / f).read_bytes()
        b = (PLUGINS["evo"] / "hooks" / f).read_bytes()
        assert a == b, f"加载器双拷贝漂移(唯一权威 dev 正源,evo 须同步): {f}"


def test_hook_rules_tree_valid():
    """批 176 规则面守卫:两插件 hook_rules 树 frontmatter 校验(intents patterns 非空、dev-rules
    match 非空)、正文非空、禁字与约束术语清零、件数与 HOOK_RULES 计数断言一致。"""
    import importlib.util as _ilu
    spec = _ilu.spec_from_file_location("pevo_mdrules", PLUGINS["dev"] / "scripts" / "mdrules.py")
    mdr = _ilu.module_from_spec(spec)
    spec.loader.exec_module(mdr)
    tspec = _ilu.spec_from_file_location("pevo_termrules", PLUGINS["dev"] / "scripts" / "termrules.py")
    import sys as _sys
    _sys.path.insert(0, str(PLUGINS["dev"] / "scripts"))
    trm = _ilu.module_from_spec(tspec)
    tspec.loader.exec_module(trm)
    for name in PLUGIN_NAMES:
        counts = {"intents": 0, "dev-rules": 0}
        for sub in ("intents", "dev-rules"):
            d = PLUGINS[name] / "hook_rules" / sub
            assert d.is_dir(), f"{name} 缺 hook_rules/{sub}"
            for f in sorted(d.glob("*.md")):
                counts[sub] += 1
                text = f.read_text(encoding="utf-8")
                m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
                assert m, f"{f.relative_to(REPO)} 缺 frontmatter"
                fm, body = m.group(1), m.group(2)
                key = "patterns" if sub == "intents" else "match"
                kv = re.search(rf"^{key}:\s*(.+)$", fm, re.M)
                assert kv, f"{f.relative_to(REPO)} 缺 {key} 字段"
                val = kv.group(1).strip()
                assert val not in ("", "[]"), f"{f.relative_to(REPO)} {key} 空"
                assert body.strip(), f"{f.relative_to(REPO)} 正文空"
                assert not mdr.file_violations(text), f"{f.relative_to(REPO)} 禁字违规"
                assert not trm.file_term_violations(text), f"{f.relative_to(REPO)} 约束术语违规"
        assert counts == HOOK_RULES[name], \
            f"{name} hook_rules 计数漂移: 实际 {counts} 对断言 {HOOK_RULES[name]}"


def test_hook_loader_live_fire(tmp_path):
    """批 176 加载器实弹:tmp 项目树起样例规则,intent-guidance 按词表命中注入、dev-rules 按路径注入;
    无 bun 则 skip(分型 bun 主道)。"""
    import shutil
    bun = shutil.which("bun")
    if not bun:
        import pytest
        pytest.skip("bun 不在 PATH(分型 bun 主道),跳过实弹")
    proj = tmp_path / "proj"
    (proj / ".claude" / "hook_rules" / "intents").mkdir(parents=True)
    (proj / ".claude" / "hook_rules" / "intents" / "样例.md").write_text(
        "---\npatterns: [网关, gateway]\n---\n\n## 样例注入\n\n- 样例行\n", encoding="utf-8")
    r = subprocess.run(
        [bun, str(PLUGINS["dev"] / "hooks" / "intent-guidance.ts")],
        input=json.dumps({"prompt": "帮我看网关"}),
        capture_output=True, text=True, encoding="utf-8",
        env={**os.environ, "CLAUDE_PROJECT_DIR": str(proj)},
    )
    assert r.returncode == 0, r.stderr
    out = json.loads(r.stdout) if r.stdout.strip() else {}
    ctx = out.get("hookSpecificOutput", {}).get("additionalContext", "")
    assert "样例注入" in ctx, "词表命中须注入正文"
    r2 = subprocess.run(
        [bun, str(PLUGINS["dev"] / "hooks" / "intent-guidance.ts")],
        input=json.dumps({"prompt": "无关提示"}),
        capture_output=True, text=True, encoding="utf-8",
        env={**os.environ, "CLAUDE_PROJECT_DIR": str(proj)},
    )
    assert r2.returncode == 0 and not r2.stdout.strip(), "未命中不得有输出"
    (proj / ".claude" / "hook_rules" / "dev-rules").mkdir(parents=True)
    (proj / ".claude" / "hook_rules" / "dev-rules" / "样例路径.md").write_text(
        "---\nmatch: /docs/\n---\n\n## 路径注入\n\n- 路径行\n", encoding="utf-8")
    r3 = subprocess.run(
        [bun, str(PLUGINS["dev"] / "hooks" / "dev-rules.ts")],
        input=json.dumps({"tool_name": "Edit", "tool_input": {"file_path": "/x/docs/页.md"}}),
        capture_output=True, text=True, encoding="utf-8",
        env={**os.environ, "CLAUDE_PROJECT_DIR": str(proj)},
    )
    assert r3.returncode == 0, r3.stderr
    out3 = json.loads(r3.stdout) if r3.stdout.strip() else {}
    assert "路径注入" in out3.get("hookSpecificOutput", {}).get("additionalContext", ""), "match 命中须注入"


def test_pre_commit_matches_current_skills():
    """提交挡板回归:pre-commit 的断链段恰覆盖当前规则面(skill 壳树加 hook_rules 树),引用路径全在。

    历史:批 81 删 skill 后 CI 悬空引用漏改而红;批 176 知识面迁 hook_rules(ADR-0027),断链段随翻。
    """
    text = (REPO / "githooks" / "pre-commit").read_text(encoding="utf-8")
    guard_ref = "plugins/dev/scripts/md-guard.py"
    assert guard_ref in text, f"pre-commit 须挂 {guard_ref}"
    assert (REPO / guard_ref).is_file(), f"pre-commit 挂的挡板不存在: {guard_ref}"
    term_ref = "plugins/dev/scripts/term-lint.py"
    assert term_ref in text, f"pre-commit 须挂 {term_ref}(批 175 术语挡板)"
    assert (REPO / term_ref).is_file(), f"pre-commit 挂的术语挡板不存在: {term_ref}"
    targets = sorted(re.findall(r"md-ref-scan\.py (\S+)", text))
    expected = sorted(
        [f"plugins/{p}/skills/{s}" for p, ss in SKILLS.items() for s in ss]
        + [f"plugins/{p}/hook_rules/{sub}" for p in PLUGIN_NAMES for sub in ("intents", "dev-rules")]
    )
    assert targets == expected, f"断链段与规则面漂移:挡板 {targets} 对清单 {expected}"
    for t in targets:
        assert (REPO / t).is_dir(), f"断链段引用的目录不存在: {t}"


def test_ci_workflow_refs_exist():
    """CI 挂接回归:test.yml 里引用的仓内 .py 与 .json 路径全部存在(悬空即红)。"""
    text = (REPO / ".github" / "workflows" / "test.yml").read_text(encoding="utf-8")
    refs = set(re.findall(r"([\w./\\-]+\.(?:py|json))", text))
    internal = {r.replace("\\", "/") for r in refs
                if r.startswith((".tools/", "plugins/", ".claude-plugin/", ".agents/"))}
    assert internal, "test.yml 应引用仓内脚本或清单(未解析到,检查正则)"
    missing = sorted(r for r in internal if not (REPO / r).exists())
    assert not missing, f"CI 引用悬空: {missing}"


def test_fleet_exec_tool():
    """fleet-exec 薄封装:--help 可跑,--machine 前缀组装正确(活权威命令逐条透传,不藏语义)。"""
    r = subprocess.run([sys.executable, str(SCRIPTS / "fleet-exec.py"), "--help"],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    assert r.returncode == 0, r.stdout + r.stderr
    assert "--machine" in r.stdout and "--marker" in r.stdout
    spec = importlib.util.spec_from_file_location("pevo_fleet", SCRIPTS / "fleet-exec.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    assert mod.build_cmd(["pane", "list"], None) == ["herdr", "pane", "list"]
    assert mod.build_cmd(["agent", "list"], "lan-mac") == \
        ["herdr", "--machine", "lan-mac", "agent", "list"]
def test_lint_hook_scopes_to_event_cwd(tmp_path: Path):
    """后缀静检辖域限仓内(ADR-0017 同批裁定,与 md-guard 同律):仓外 md 放行,仓内照检。"""
    bad = tmp_path / "bad.md"
    bad.write_text("带禁字——的一行\n", encoding="utf-8")
    outside = json.dumps({"hook_event_name": "PostToolUse", "cwd": str(tmp_path / "repo"),
                          "tool_input": {"file_path": str(bad)}})
    assert _run_lint_hook(outside).returncode == 0, "仓外 md 不在静检辖域,应放行"
    inside = json.dumps({"hook_event_name": "PostToolUse", "cwd": str(tmp_path),
                         "tool_input": {"file_path": str(bad)}})
    assert _run_lint_hook(inside).returncode == 2, "仓内 md 照检"
def _cn(n: int) -> str:
    if n == 2:
        return "两"
    digits = "零一二三四五六七八九"
    if n < 10:
        return digits[n]
    if n == 10:
        return "十"
    if n < 20:
        return "十" + digits[n - 10]
    tens, ones = divmod(n, 10)
    return digits[tens] + "十" + (digits[ones] if ones else "")


def test_live_surfaces_count_matches_reality():
    """活面计数守卫:AGENTS 与根 README 的插件与 skill 计数等于 SKILLS 实际值(通用中文数字换算)。"""
    total = sum(len(v) for v in SKILLS.values())
    text_a = (REPO / "AGENTS.md").read_text(encoding="utf-8")
    text_r = (REPO / "README.md").read_text(encoding="utf-8")
    assert f"{_cn(len(PLUGIN_NAMES))}插件" in text_a and f"{_cn(len(PLUGIN_NAMES))}插件" in text_r
    assert f"{_cn(total)} skill" in text_a and f"{_cn(total)} skill" in text_r
    assert f"{_cn(len(PLUGIN_NAMES))}插件{_cn(total)} skill" in text_a, "组合总量形须在位且正确"


def test_no_stale_plugin_counts_in_live_surfaces():
    """活面插件计数全树守卫:任意中文数字插件计数须等于实际插件数(序数第几插件放行)。"""
    import re as _re
    pat = _re.compile("[一二三四五六七八九十]{1,3}插件")
    skip_dirs = {".git", ".venv", ".pytest_cache", "__pycache__",
                 "adr", "requirements", "diary", "research"}
    suffixes = {".md", ".toml", ".py", ".json", ".sh", ".yml", ".yaml"}
    want = _cn(len(PLUGIN_NAMES)) + "插件"
    hits = []
    for p in REPO.rglob("*"):
        if p.suffix not in suffixes or any(d in p.parts or d in p.name for d in skip_dirs):
            continue
        if p.name in ("CHANGELOG.md", "ROADMAP.md") or not p.is_file():
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        for m in pat.finditer(text):
            before = text[max(0, m.start() - 1)]
            if before == "第":
                continue
            if m.group() != want:
                hits.append(f"{p.relative_to(REPO)}: {m.group()}")
    assert not hits, f"陈旧插件计数残留(应全为 {want}): {hits}"


def test_evo_primitive_skill_dirs_align_with_commands():
    """B3 目录-命令对齐守卫(REQ-057;批 164 ctxs 正名判例):evo 原语域 skill 目录名
    必须落在正典原语命令集内且为全词复数形;非命令面(渐进知识库型 distil、research)例外。
    mcps/nodes 入真源时须有意识更新本正典集与 SKILLS 清单(REQ-058),静默漂移当场红灯。
    批 173 命名三分(REQ-062):nodes 更名 machines,desk 析出(desk 命令名单数形,复数律豁免)。
    批 174 复数对齐(REQ-063):desk 更名 desks(prim 3.11.0 主名,desk 留旧名单字别名)。"""
    canonical = {"agents", "shares", "streams", "tasks", "pipes", "ports", "ctxs", "mcps", "machines", "desks"}
    primitives = set(SKILLS["evo"]) - {"distil", "research"}  # research 批 170 入列(REQ-059,渐进知识库型非命令面)
    assert primitives == canonical, \
        f"原语域目录对正典命令集漂移(改集须过 REQ,勿静默): {primitives ^ canonical}"
    for name in sorted(primitives):
        assert name.endswith("s"), f"原语域目录须命令名全词复数形: {name}"


def test_skill_description_form_repo_wide():
    """规范 A2/A3 静检(REQ-058):全仓 SKILL.md description 三句形齐(Use when 与不要用于)
    且折叠后 ≤400 字符;mdrules 为唯一判定权威,md-guard 挡板接线同源。"""
    spec = importlib.util.spec_from_file_location(
        "pevo_mdrules", PLUGINS["dev"] / "scripts" / "mdrules.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    check = mod.skill_description_violations
    good = "---\nname: x\ndescription: >-\n  做什么。\n  Use when: a, b。\n  不要用于 c。\n---\n"
    assert check(good) == []
    assert check("---\nname: x\ndescription: >-\n  " + "长" * 401 + "\n---\n") != [], "超 400 须报"
    assert any("Use when" in m for m in check("---\nname: x\ndescription: >-\n  做什么。\n---\n"))
    for p in sorted(REPO.glob("plugins/*/skills/*/SKILL.md")):
        msgs = check(p.read_text(encoding="utf-8"))
        assert not msgs, f"{p.relative_to(REPO)}: {msgs}"
