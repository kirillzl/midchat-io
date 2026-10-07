#!/usr/bin/env python3
"""Patch all five plugin.json files with midchat.io listing URLs and rebuild dist zips.

Skills-only rebuilds only (no mcp.json). PDF → Sheets keeps skills-only ZIP without MCP —
do not Directory-submit it; MCP URL belongs in next-steps / release ZIP only.
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]  # chatgpt-plugins/
PLUGINS = [
    "billfast",
    "friday-pack",
    "action-loop",
    "expense-sheet",
    "pdf-to-sheets",
]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--domain", default="midchat.io", help="apex domain (no scheme)")
    ap.add_argument("--email", default="support@midchat.io")
    ap.add_argument(
        "--author-url",
        default=None,
        help="defaults to https://<domain>/",
    )
    ap.add_argument(
        "--dry-run",
        action="store_true",
        help="print URLs only; do not write plugin.json or rebuild zips",
    )
    a = ap.parse_args()
    domain = a.domain.strip().lower().removeprefix("https://").removeprefix("http://").strip("/")
    if not domain or "your_domain" in domain or "example." in domain:
        sys.exit("Refusing: --domain looks like a placeholder.")
    base = f"https://{domain}"
    author_url = (a.author_url or f"{base}/").rstrip("/") + "/"
    email = a.email

    print(f"Domain: {domain}")
    print(f"Author URL: {author_url}")
    print(f"Email: {email}")
    print("MCP (documented only, not written to skills-only packages): "
          f"https://mcp.{domain}/mcp")

    for name in PLUGINS:
        pkg = ROOT / name
        pj = pkg / "plugin.json"
        if not pj.exists():
            sys.exit(f"Missing {pj}")
        site = f"{base}/{name}/"
        urls = {
            "websiteURL": site,
            "supportURL": f"{site}support/",
            "privacyPolicyURL": f"{site}privacy/",
            "termsOfServiceURL": f"{site}terms/",
        }
        print(f"\n{name}:")
        for k, v in urls.items():
            print(f"  {k}: {v}")
        if a.dry_run:
            continue
        data = json.loads(pj.read_text(encoding="utf-8"))
        shutil.copy(pj, pkg / "plugin.json.bak")
        iface = data.setdefault("extensions", {}).setdefault("com.openai", {}).setdefault("interface", {})
        iface.update(urls)
        data["homepage"] = site
        author = data.setdefault("author", {})
        author["name"] = "Midchat"
        author["email"] = email
        author["url"] = author_url
        pj.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"  wrote {pj.relative_to(ROOT)} (backup plugin.json.bak)")

    if a.dry_run:
        print("\nDry run — no files changed.")
        return

    # Rebuild all skills-only zips (excludes mcp.json / mcp-server / submit-prep)
    cmd = [sys.executable, str(ROOT / "tools" / "build_dist.py")] + PLUGINS
    print("\nRebuilding dist zips:", " ".join(cmd))
    subprocess.check_call(cmd, cwd=ROOT)
    print("Done. Skills-only zips updated; MCP not included.")
    print("PDF → Sheets: do NOT Directory-submit dist/pdf-to-sheets.zip until MCP release.")


if __name__ == "__main__":
    main()
