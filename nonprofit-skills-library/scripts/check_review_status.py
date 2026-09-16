#!/usr/bin/env python3
"""Report review coverage and age without treating an addition as a review.

Read metadata.last_reviewed and metadata.date_added (legacy top-level fields are
also accepted). Dates are scheduling evidence, not content certification.
Missing review dates are NOT_REVIEWED, never silently CURRENT or REVIEW_OVERDUE.
date_added means first addition to this repository, not original creation.

Usage from nonprofit-skills-library:
    python3 scripts/check_review_status.py
    python3 scripts/check_review_status.py --all --json
    python3 scripts/check_review_status.py --as-of 2026-09-16

JSON schema version 2 separates not_reviewed_count from overdue_count.
Exit 1 for any not-reviewed, overdue, or invalid record; 0 only when all records
are current; 2 for invocation/scan errors. No CI gate or scheduled job is installed.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from datetime import date
from pathlib import Path

from skill_metadata import read_metadata

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_ROOT = REPO_ROOT / "skills"
FAST_MOVING_CATEGORIES = {"technology-data", "fundraising-development", "governance-compliance"}
FAST_INTERVAL_DAYS = 90
DEFAULT_INTERVAL_DAYS = 365


@dataclass
class SkillStatus:
    name: str
    category: str
    path: str
    last_reviewed: str | None
    date_added: str | None
    interval_days: int
    days_since_review: int | None
    days_since_added: int | None
    status: str
    overdue: bool
    missing_field: bool
    initial_review_due: bool
    error: str | None

    @property
    def needs_attention(self):
        return self.status != "current"


def parse_date(value, field, today):
    if value is None:
        return None
    text = str(value)
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", text):
        raise ValueError(f"{field} must be YYYY-MM-DD")
    try:
        parsed = date.fromisoformat(text)
    except ValueError as exc:
        raise ValueError(f"{field} is not a valid calendar date") from exc
    if parsed > today:
        raise ValueError(f"{field} is in the future relative to {today}")
    return parsed


def scan(today=None):
    today = today or date.today()
    paths = sorted(SKILLS_ROOT.glob("*/*/SKILL.md"))
    if not paths:
        raise ValueError(f"No skills found under {SKILLS_ROOT}")
    results = []
    for path in paths:
        category = path.parent.parent.name
        interval = FAST_INTERVAL_DAYS if category in FAST_MOVING_CATEGORIES else DEFAULT_INTERVAL_DAYS
        name, reviewed, added, error = path.parent.name, None, None, None
        missing = True
        try:
            fields = read_metadata(path.read_text(encoding="utf-8"))
            name = fields.get("name", name)
            missing = "last_reviewed" not in fields
            # An explicitly empty date is invalid, not a missing review record.
            for field in ("last_reviewed", "date_added"):
                if field in fields and fields[field] is None:
                    raise ValueError(f"{field} is empty; omit unknown dates")
            reviewed = parse_date(fields.get("last_reviewed"), "last_reviewed", today)
            added = parse_date(fields.get("date_added"), "date_added", today)
        except ValueError as exc:
            error = str(exc)
        review_age = (today - reviewed).days if reviewed else None
        added_age = (today - added).days if added else None
        overdue = error is None and reviewed is not None and review_age > interval
        status = ("invalid-metadata" if error else "not-reviewed" if reviewed is None
                  else "review-overdue" if overdue else "current")
        results.append(SkillStatus(
            name=name, category=category, path=str(path.relative_to(REPO_ROOT)),
            last_reviewed=reviewed.isoformat() if reviewed else None,
            date_added=added.isoformat() if added else None, interval_days=interval,
            days_since_review=review_age, days_since_added=added_age,
            status=status, overdue=overdue, missing_field=missing,
            initial_review_due=status == "not-reviewed" and added_age is not None and added_age > interval,
            error=error,
        ))
    return results


def format_row(s):
    tag = s.status.upper().replace("-", "_")
    if s.error:
        detail = s.error
    elif s.last_reviewed:
        detail = f"reviewed {s.last_reviewed} ({s.days_since_review}d ago; interval {s.interval_days}d)"
    else:
        detail = (f"added {s.date_added} ({s.days_since_added}d ago)" if s.date_added else "addition date unknown")
        if s.initial_review_due:
            detail += "; initial review past scheduling interval"
        detail += "; no review date recorded"
    return f"  {tag:16s} {s.name:45s} {s.category:25s} {detail}"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--all", action="store_true", help="Show current records as well as those needing attention")
    parser.add_argument("--json", action="store_true", help="Emit versioned JSON")
    parser.add_argument("--as-of", type=date.fromisoformat, help="Use a fixed YYYY-MM-DD for reproducible checks")
    args = parser.parse_args(argv)
    today = args.as_of or date.today()
    try:
        statuses = scan(today)
    except (ValueError, OSError) as exc:
        print(f"Review-status error: {exc}", file=sys.stderr)
        return 2
    attention = [s for s in statuses if s.needs_attention]
    summary = {
        "schema_version": 2, "as_of": today.isoformat(), "checked": len(statuses),
        "current_count": sum(s.status == "current" for s in statuses),
        "not_reviewed_count": sum(s.status == "not-reviewed" for s in statuses),
        "overdue_count": sum(s.overdue for s in statuses),
        "invalid_count": sum(s.status == "invalid-metadata" for s in statuses),
        "initial_review_due_count": sum(s.initial_review_due for s in statuses),
        "attention_count": len(attention),
    }
    shown = statuses if args.all else attention
    if args.json:
        print(json.dumps({**summary, "skills": [asdict(s) for s in shown]}, indent=2))
    else:
        print(f"Nonprofit Skills review status ({len(statuses)} skills; as of {today})")
        print(f"Current: {summary['current_count']} | Not reviewed: {summary['not_reviewed_count']} | "
              f"Review overdue: {summary['overdue_count']} | Invalid: {summary['invalid_count']}")
        print("NOT_REVIEWED means no review date is recorded, not proof that no review ever occurred.")
        for s in shown:
            print(format_row(s))
    return 1 if attention else 0


if __name__ == "__main__":
    sys.exit(main())
