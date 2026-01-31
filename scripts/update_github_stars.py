#!/usr/bin/env python3
"""
Update GitHub stars in awesome-ai-societies.jsonl.

Usage:
  export GITHUB_TOKEN=...
  python scripts/update_github_stars.py

Notes:
- Only entries with GitHub URLs are updated.
- Writes back to the JSONL file in-place.
"""

import json
import os
import re
import sys
import requests

ROOT = os.path.dirname(os.path.dirname(__file__))
JSONL_PATH = os.path.join(ROOT, "awesome-ai-societies.jsonl")

GH_RE = re.compile(r"^https?://github\.com/([^/]+)/([^/#?]+)")

def parse_github_repo(url: str):
    m = GH_RE.match(url.strip())
    if not m:
        return None
    owner, repo = m.group(1), m.group(2)
    return owner, repo

def main():
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        print("Missing GITHUB_TOKEN env var.", file=sys.stderr)
        sys.exit(2)

    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "awesome-ai-societies-updater",
    }

    updated = 0
    lines_out = []

    with open(JSONL_PATH, "r", encoding="utf-8") as f:
        lines = [ln.rstrip("\n") for ln in f if ln.strip()]

    for ln in lines:
        obj = json.loads(ln)
        repo_id = parse_github_repo(obj.get("url", ""))
        if not repo_id:
            lines_out.append(json.dumps(obj, ensure_ascii=False))
            continue

        owner, repo = repo_id
        api = f"https://api.github.com/repos/{owner}/{repo}"
        r = requests.get(api, headers=headers, timeout=30)
        if r.status_code != 200:
            print(f"Failed: {owner}/{repo} -> {r.status_code}", file=sys.stderr)
            lines_out.append(json.dumps(obj, ensure_ascii=False))
            continue

        data = r.json()
        obj["stars"] = data.get("stargazers_count")
        obj["pushed_at"] = data.get("pushed_at")
        obj["updated_at"] = data.get("updated_at")
        updated += 1
        lines_out.append(json.dumps(obj, ensure_ascii=False))

    with open(JSONL_PATH, "w", encoding="utf-8") as f:
        for ln in lines_out:
            f.write(ln + "\n")

    print(f"Updated {updated} GitHub entries.")

if __name__ == "__main__":
    main()
