#!/usr/bin/env python3
"""Report which SKILL.md files declare a supervision level, and which don't.

Not every skill in this library carries the same risk. A draft thank-you letter
that comes out wrong costs an edit. A Form 990 or a set of bylaws that comes out
wrong is filed with the IRS or binds the organization — and the person running
the agent is often the least equipped to notice the error.

`metadata.supervision` records that difference in the frontmatter so an agent, a CI job,
or a human browsing the library can see it before the output is used.

Levels
------
- unsupervised
    Output can be used with ordinary editing. A mistake costs time, not much
    else. Example: a social post draft, an internal brainstorm.

- review
    A knowledgeable staff member must read the output before it is used or
    circulated. Consequential internally, but nothing is filed with an outside
    authority. Example: board meeting structure, a risk register.

- expert-required
    Output must be reviewed by a credentialed professional (attorney, CPA,
    licensed auditor) before it is filed, adopted, or relied on. The document
    goes to an external authority or legally binds the organization.
    Example: Form 990, bylaws, state charitable registration.

Usage
-----
    python3 scripts/check_supervision.py              # list skills missing the field
    python3 scripts/check_supervision.py --all        # list every skill with its level
    python3 scripts/check_supervision.py --json       # machine-readable output

Exit code 1 if any skill declares an invalid level, else 0. Missing fields are
reported but do not fail, so the field can be adopted incrementally.
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from skill_metadata import read_metadata

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_ROOT = REPO_ROOT / "skills"

VALID_LEVELS = ("unsupervised", "review", "expert-required")

@dataclass
class SkillStatus:
    name: str
    category: str
    supervision: str | None
    valid: bool

    @property
    def state(self) -> str:
        if self.supervision is None:
            return "MISSING"
        return "OK" if self.valid else "INVALID"


def collect() -> list[SkillStatus]:
    out: list[SkillStatus] = []
    for path in sorted(SKILLS_ROOT.glob("*/*/SKILL.md")):
        text = path.read_text(encoding="utf-8")
        fields = read_metadata(text)
        name = fields.get("name", path.parent.name)
        level = fields.get("supervision")
        if level is not None and not isinstance(level, str):
            raise ValueError(f"{path}: supervision must be a string")

        out.append(
            SkillStatus(
                name=name,
                category=path.parent.parent.name,
                supervision=level,
                valid=level in VALID_LEVELS,
            )
        )
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--all", action="store_true", help="list every skill, not just gaps")
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    args = parser.parse_args()

    try:
        statuses = collect()
    except ValueError as exc:
        print(f"Metadata error: {exc}", file=sys.stderr)
        return 2
    invalid = [s for s in statuses if s.supervision is not None and not s.valid]
    missing = [s for s in statuses if s.supervision is None]

    if args.json:
        print(json.dumps([asdict(s) for s in statuses], indent=2))
        return 1 if invalid else 0

    shown = statuses if args.all else invalid + missing
    for status in shown:
        level = status.supervision or "(no supervision field)"
        print(f"  {status.state:8} {status.name:44} {status.category:26} {level}")

    declared = len(statuses) - len(missing)
    print(f"\n{declared}/{len(statuses)} skills declare a supervision level.")

    if invalid:
        print(f"{len(invalid)} skill(s) declare a level outside {VALID_LEVELS}.")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
