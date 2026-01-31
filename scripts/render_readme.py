#!/usr/bin/env python3
"""
Render categorized lists from awesome-ai-societies.jsonl.

This is optional. Many maintainers prefer editing README manually.
If you want automation, use this to generate category blocks that you can paste into README.

Usage:
  python scripts/render_readme.py > /tmp/blocks.md
"""

import json
import os
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(__file__))
JSONL_PATH = os.path.join(ROOT, "awesome-ai-societies.jsonl")

CATEGORY_TITLES = {
    "ai-only-public-community": "AI-only Public Communities (agents post/engage at scale)",
    "hybrid-community-space": "Hybrid Human+AI Community Spaces (group chat / rooms)",
    "social-simulation": "Social Simulation Worlds (town/city/world sandboxes)",
    "organizational-society": "Organizational Societies (virtual teams / “AI companies”)",
}

def main():
    groups = defaultdict(list)
    with open(JSONL_PATH, "r", encoding="utf-8") as f:
        for ln in f:
            ln = ln.strip()
            if not ln:
                continue
            obj = json.loads(ln)
            groups[obj.get("category","uncategorized")].append(obj)

    for cat, title in CATEGORY_TITLES.items():
        items = groups.get(cat, [])
        if not items:
            continue
        print(f"### {title}\n")
        for it in sorted(items, key=lambda x: (x.get("name","").lower())):
            name = it.get("name","")
            url = it.get("url","")
            stars = it.get("stars")
            star_str = f" — ⭐ {stars}" if isinstance(stars, int) else ""
            notes = it.get("notes","").strip()
            suffix = f" — {notes}" if notes else ""
            print(f"- **{name}** — {url}{star_str}{suffix}")
        print()

if __name__ == "__main__":
    main()
