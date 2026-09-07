#!/usr/bin/env python3
"""Report which SKILL.md files are overdue for review.

Every SKILL.md carries a `last_reviewed: YYYY-MM-DD` frontmatter field. This
script reads that field, applies the library's review cadence, and prints an
overdue report.

Cadence
-------
- Fast-moving categories (reviewed every 90 days):
    * technology-data
    * fundraising-development
    * governance-compliance
  These categories touch AI/CRM tools, IRS/990 rules, grant platforms, and
  fundraising tech, which move quickly.

- All other categories: reviewed every 365 days.

Usage
-----
    python3 scripts/check_review_status.py              # list overdue skills
    python3 scripts/check_review_status.py --all        # list every skill with its status
    python3 scripts/check_review_status.py --json       # machine-readable output

Exit code 1 if any skill is overdue, else 0. Useful in CI to gate merges.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, asdict
from datetime import date, datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_ROOT = REPO_ROOT / "skills"

FAST_MOVING_CATEGORIES = {
    "technology-data",
    "fundraising-development",
    "governance-compliance",
}
FAST_INTERVAL_DAYS = 90
DEFAULT_INTERVAL_DAYS = 365

LAST_REVIEWED_RE = re.compile(r"^last_reviewed:\s*(\d{4}-\d{2}-\d{2})\s*$", re.MULTILINE)
NAME_RE = re.compile(r"^name:\s*(\S+)\s*$", re.MULTILINE)


@dataclass
class SkillStatus:
    name: str
    category: str
    path: str
    last_reviewed: str | None
    interval_days: int
    days_since_review: int | None
    overdue: bool
    missing_field: bool


def parse_frontmatter(text: str) -> tuple[str | None, date | None]:
    if not text.startswith("---"):
        return None, None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, None
    fm = parts[1]
    name_match = NAME_RE.search(fm)
    date_match = LAST_REVIEWED_RE.search(fm)
    name = name_match.group(1) if name_match else None
    reviewed = None
    if date_match:
        try:
            reviewed = datetime.strptime(date_match.group(1), "%Y-%m-%d").date()
        except ValueError:
            reviewed = None
    return name, reviewed


def scan(today: date | None = None) -> list[SkillStatus]:
    today = today or date.today()
    results: list[SkillStatus] = []
    for skill_md in sorted(SKILLS_ROOT.rglob("SKILL.md")):
        rel = skill_md.relative_to(REPO_ROOT)
        category = skill_md.relative_to(SKILLS_ROOT).parts[0]
        interval = FAST_INTERVAL_DAYS if category in FAST_MOVING_CATEGORIES else DEFAULT_INTERVAL_DAYS
        name, reviewed = parse_frontmatter(skill_md.read_text())
        if reviewed is None:
            results.append(SkillStatus(
                name=name or skill_md.parent.name,
                category=category,
                path=str(rel),
                last_reviewed=None,
                interval_days=interval,
                days_since_review=None,
                overdue=True,
                missing_field=True,
            ))
            continue
        days = (today - reviewed).days
        results.append(SkillStatus(
            name=name or skill_md.parent.name,
            category=category,
            path=str(rel),
            last_reviewed=reviewed.isoformat(),
            interval_days=interval,
            days_since_review=days,
            overdue=days > interval,
            missing_field=False,
        ))
    return results


def format_row(s: SkillStatus) -> str:
    if s.missing_field:
        return f"  MISSING  {s.name:45s} {s.category:25s} (no last_reviewed field)"
    tag = "OVERDUE " if s.overdue else "ok      "
    return (
        f"  {tag} {s.name:45s} {s.category:25s} "
        f"reviewed {s.last_reviewed} ({s.days_since_review}d ago, interval {s.interval_days}d)"
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--all", action="store_true", help="Show every skill, not just overdue ones")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of a text report")
    args = parser.parse_args(argv)

    statuses = scan()
    overdue = [s for s in statuses if s.overdue]

    if args.json:
        print(json.dumps({
            "checked": len(statuses),
            "overdue_count": len(overdue),
            "skills": [asdict(s) for s in (statuses if args.all else overdue)],
        }, indent=2))
        return 1 if overdue else 0

    to_show = statuses if args.all else overdue
    print(f"Nonprofit Skills review status  ({len(statuses)} skills checked)")
    print(f"Overdue: {len(overdue)}  |  Fast-moving interval: {FAST_INTERVAL_DAYS}d  |  Default interval: {DEFAULT_INTERVAL_DAYS}d")
    print()
    if not to_show:
        print("  All skills are within their review interval.")
    else:
        for s in to_show:
            print(format_row(s))
    return 1 if overdue else 0


if __name__ == "__main__":
    sys.exit(main())
