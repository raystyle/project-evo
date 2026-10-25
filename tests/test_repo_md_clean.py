"""回归测试(集成约束形态四):仓内 markdown 四类禁字与约束术语清零常驻回归。

来历:第十六/十七批新增文本连犯破折号禁字(各被 scan 当场抓住),按「二犯升格 +
集成约束」裁定(2026-09-04)转为 CI 常驻回归用例;规则同源 plugins 内 mdrules.py。
批 175 加术语面:termrules ENFORCED 层仓内零命中为常驻契约,PENDING 存量词
收紧迁移时先清存量再动表,本用例锁底。
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
_MDRULES = REPO / "plugins" / "dev" / "scripts" / "mdrules.py"
_TERMRULES = REPO / "plugins" / "dev" / "scripts" / "termrules.py"

sys.path.insert(0, str(_MDRULES.parent))  # termrules 复用 mdrules 豁免机制

_spec = importlib.util.spec_from_file_location("pevo_mdrules", _MDRULES)
mdrules = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mdrules)

_tspec = importlib.util.spec_from_file_location("pevo_termrules", _TERMRULES)
termrules = importlib.util.module_from_spec(_tspec)
_tspec.loader.exec_module(termrules)


def _iter_md():
    for p in sorted(REPO.rglob("*.md")):
        rel = p.relative_to(REPO).parts
        if any(part in mdrules.SKIP_DIRS or part.startswith(".git") for part in rel):
            continue
        yield p


def test_repo_markdown_clean():
    if not _MDRULES.is_file():
        pytest.skip("非仓内运行(安装态),跳过")
    bad: list[str] = []
    for p in _iter_md():
        for line, cats in mdrules.file_violations(p.read_text(encoding="utf-8")).items():
            bad.append(f"{p.relative_to(REPO).as_posix()}:{line} {'、'.join(cats)}")
    assert not bad, "markdown 禁字回归失败(集成约束形态四): " + "; ".join(bad[:10])


def test_repo_markdown_terms_clean():
    """ENFORCED 术语层仓内清零(PENDING 不计;迁词入 ENFORCED 前先清存量,批 175 两层政策)。"""
    if not _TERMRULES.is_file():
        pytest.skip("非仓内运行(安装态),跳过")
    bad: list[str] = []
    for p in _iter_md():
        for line, hits in termrules.file_term_violations(p.read_text(encoding="utf-8")).items():
            cats = "、".join(cat for cat, _ in hits)
            bad.append(f"{p.relative_to(REPO).as_posix()}:{line} {cats}")
    assert not bad, "ENFORCED 术语回归失败(清存量或降 PENDING): " + "; ".join(bad[:10])
