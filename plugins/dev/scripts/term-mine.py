# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
# term-mine:从 gw_logs 对话语料挖约束术语候选(一次性研究道,不进门禁)。
# 连接:~/.ctx/reader.env(CTX_URL/CTX_USER/CTX_PASSWORD,SELECT 只读);HTTP 失败
# 自动落 ssh 备道(lan-linux2 docker clickhouse-client)。原文只落 --out-dir(仓外),
# 蒸馏结论才进仓(docs/research/S020)。用法:
#   uv run plugins/dev/scripts/term-mine.py --since 2026-05-01 --slice 14d \
#     --kind assistant,user --out-dir /tmp/term-mine/
from __future__ import annotations

import argparse
import subprocess
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

ENV_FILE = Path.home() / ".ctx" / "reader.env"
TIMEOUT = 60


def load_env() -> dict[str, str]:
    env: dict[str, str] = {}
    for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
        if "=" in line and not line.strip().startswith("#"):
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip()
    return env


def query_http(sql: str, env: dict[str, str]) -> str:
    """主道:HTTPS 8123 GET + Basic 认证(自签链:CTX_CA 可用时载入,否则跳过校验)。"""
    import base64
    import ssl

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ca = env.get("CTX_CA", "")
    if ca and Path(ca).is_file():
        ctx.load_verify_locations(ca)
    else:
        ctx.verify_mode = ssl.CERT_NONE
    url = env["CTX_URL"].rstrip("/") + "/?query=" + urllib.parse.quote(sql)
    req = urllib.request.Request(url)
    cred = base64.b64encode(
        f"{env['CTX_USER']}:{env['CTX_PASSWORD']}".encode()
    ).decode()
    req.add_header("Authorization", f"Basic {cred}")
    with urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx) as resp:
        return resp.read().decode("utf-8")


def query_ssh(sql: str) -> str:
    """备道:ssh + docker clickhouse-client,SQL 走 stdin 免远端引号解析。"""
    cmd = [
        "ssh", "lan-linux2", "docker", "exec", "-i",
        "dctl-ch-gwlogs-26.8", "clickhouse-client",
        "--secure", "--port", "9440", "--host", "127.0.0.1",
        "--config-file", "/etc/clickhouse-server/dctl/cli.xml",
    ]
    r = subprocess.run(
        cmd, input=sql, capture_output=True, text=True, timeout=TIMEOUT * 4,
    )
    if r.returncode != 0:
        raise RuntimeError(f"ssh 备道失败:{r.stderr.strip()}")
    return r.stdout


def query(sql: str, env: dict[str, str]) -> str:
    try:
        return query_http(sql, env)
    except Exception as e:  # noqa: BLE001 主道任何失败落备道
        print(f"[note] HTTP 主道失败({e}),转 ssh 备道", file=sys.stderr)
        return query_ssh(sql)


def slice_dates(since: str, until: str | None, days: int) -> list[tuple[str, str]]:
    start = datetime.fromisoformat(since).replace(tzinfo=timezone.utc)
    end = (
        datetime.fromisoformat(until).replace(tzinfo=timezone.utc)
        if until
        else datetime.now(timezone.utc)
    )
    out: list[tuple[str, str]] = []
    cur = start
    while cur < end:
        nxt = min(cur + timedelta(days=days), end)
        out.append((cur.strftime("%Y-%m-%d"), nxt.strftime("%Y-%m-%d")))
        cur = nxt
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="gw_logs 术语候选挖词(研究道,原文只落仓外)")
    ap.add_argument("--since", required=True, help="起始日 YYYY-MM-DD(gwlog 窗 180 天)")
    ap.add_argument("--until", default=None, help="结束日 YYYY-MM-DD(默认今天)")
    ap.add_argument("--slice", default="14d", help="切片宽(如 14d,防超时)")
    ap.add_argument("--kind", default="assistant,user",
                    help="payload kind 过滤(逗号分隔,默认 assistant,user)")
    ap.add_argument("--out-dir", type=Path, required=True, help="原文落盘目录(仓外)")
    ap.add_argument("--limit", type=int, default=200_000,
                    help="每片行数上限(默认 200000)")
    ap.add_argument("--sample", type=int, default=5,
                    help="抽样百分比 1-100(默认 5,挖词不需全量)")
    args = ap.parse_args(argv)

    days = int(args.slice.removesuffix("d"))
    kinds = ", ".join(f"'{k.strip()}'" for k in args.kind.split(","))
    env = load_env()
    args.out_dir.mkdir(parents=True, exist_ok=True)

    # 探活:主备两道各跑一条 count
    probe = "SELECT count() FROM gw_logs.gwlog WHERE ts >= now() - INTERVAL 7 DAY"
    n = query(probe, env).strip()
    print(f"[probe] 近 7 天块数 {n}")

    for s, e in slice_dates(args.since, args.until, days):
        out_file = args.out_dir / f"gwlog-{s}_{e}.jsonl"
        if out_file.exists():
            print(f"[skip] {out_file} 已存在")
            continue
        sql = (
            "SELECT ts, kind, substringUTF8(payload, 1, 2000) AS payload "
            "FROM gw_logs.gwlog "
            f"WHERE ts >= '{s} 00:00:00' AND ts < '{e} 00:00:00' "
            f"AND kind IN ({kinds}) "
            f"AND lengthUTF8(payload) > 50 "
            f"AND rand() % 100 < {args.sample} "
            f"LIMIT {args.limit} FORMAT JSONEachRow"
        )
        print(f"[dump] {s} -> {e}")
        rows = query(sql, env)
        out_file.write_text(rows, encoding="utf-8")
        n_rows = sum(1 for _ in rows.splitlines() if _.strip())
        print(f"[done] {out_file.name}: {n_rows} 行")

    print("[done] 全片落盘完成;候选提取与蒸馏见 docs/research/S020")
    return 0


if __name__ == "__main__":
    sys.exit(main())
