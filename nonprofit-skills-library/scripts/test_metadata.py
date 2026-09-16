"""Regression checks for portable metadata and review lifecycle reporting."""
import contextlib
import io
import json
from datetime import date, timedelta
from pathlib import Path
import tempfile
import unittest

import check_review_status as review
import check_supervision as supervision
from skill_metadata import read_metadata

TODAY = date(2026, 9, 16)


class MetadataTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.old_review_roots = review.REPO_ROOT, review.SKILLS_ROOT
        self.old_supervision_roots = supervision.REPO_ROOT, supervision.SKILLS_ROOT
        review.REPO_ROOT = supervision.REPO_ROOT = self.root
        review.SKILLS_ROOT = supervision.SKILLS_ROOT = self.root / "skills"

    def tearDown(self):
        review.REPO_ROOT, review.SKILLS_ROOT = self.old_review_roots
        supervision.REPO_ROOT, supervision.SKILLS_ROOT = self.old_supervision_roots
        self.tmp.cleanup()

    def record(self, fields, category="finance-operations"):
        p = self.root / "skills" / category / "nonprofit-test" / "SKILL.md"
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(f"---\nname: nonprofit-test\n{fields}\n---\nBody unchanged.\n")
        return review.scan(TODAY)[0]

    def test_recent_unreviewed_is_not_current_or_overdue(self):
        s = self.record('metadata:\n  date_added: "2026-09-07"')
        self.assertEqual(s.status, "not-reviewed")
        self.assertEqual(s.days_since_added, 9)
        self.assertFalse(s.overdue)
        self.assertFalse(s.initial_review_due)
        self.assertTrue(s.needs_attention)

    def test_unknown_addition_remains_unknown(self):
        s = self.record("metadata: {}")
        self.assertIsNone(s.days_since_added)
        self.assertEqual(s.status, "not-reviewed")

    def test_initial_review_age_does_not_become_review_age(self):
        s = self.record('metadata:\n  date_added: "2025-01-01"')
        self.assertTrue(s.initial_review_due)
        self.assertIsNone(s.days_since_review)
        self.assertFalse(s.overdue)

    def test_nested_quoted_and_legacy_unquoted_dates(self):
        for fields in ('last_reviewed: 2026-09-01', 'metadata:\n  last_reviewed: "2026-09-01"'):
            with self.subTest(fields=fields):
                s = self.record(fields)
                self.assertEqual(s.status, "current")
                self.assertEqual(s.days_since_review, 15)

    def test_review_predating_import_is_allowed(self):
        s = self.record('metadata:\n  last_reviewed: "2026-09-01"\n  date_added: "2026-09-07"')
        self.assertEqual(s.status, "current")

    def test_interval_boundaries(self):
        for cat, interval in (("technology-data", 90), ("finance-operations", 365)):
            for age, expected in ((interval, False), (interval + 1, True)):
                with self.subTest(category=cat, age=age):
                    s = self.record(f'last_reviewed: "{TODAY - timedelta(days=age)}"', cat)
                    s = next(x for x in review.scan(TODAY) if x.category == cat)
                    self.assertEqual(s.overdue, expected)

    def test_invalid_and_future_dates(self):
        for key in ("last_reviewed", "date_added"):
            for value in ('"2026-02-30"', '"2027-01-01"', '""', 'null', '"20260901"'):
                with self.subTest(key=key, value=value):
                    s = self.record(f"metadata:\n  {key}: {value}")
                    self.assertEqual(s.status, "invalid-metadata")
                    self.assertFalse(s.overdue)

    def test_dual_declarations_require_agreement(self):
        same = 'last_reviewed: 2026-09-01\nmetadata:\n  last_reviewed: "2026-09-01"'
        self.assertEqual(self.record(same).status, "current")
        conflict = same.replace('"2026-09-01"', '"2026-09-02"')
        self.assertEqual(self.record(conflict).status, "invalid-metadata")

    def test_duplicate_and_malformed_yaml(self):
        for fields in (
            'last_reviewed: 2026-09-01\nlast_reviewed: 2026-09-02',
            'metadata:\n  date_added: "2026-09-01"\n  date_added: "2026-09-02"',
            'metadata: [not, a, mapping]',
            'metadata: [broken',
        ):
            with self.subTest(fields=fields):
                self.assertEqual(self.record(fields).status, "invalid-metadata")

    def test_supervision_preserves_nested_and_legacy_values(self):
        for fields in ('supervision: expert-required', 'metadata:\n  supervision: "expert-required"'):
            self.record(fields)
            s = supervision.collect()[0]
            self.assertEqual(s.supervision, "expert-required")
            self.assertTrue(s.valid)

    def test_supervision_conflicts_fail(self):
        text = '---\nname: test\nsupervision: review\nmetadata:\n  supervision: expert-required\n---\n'
        with self.assertRaises(ValueError):
            read_metadata(text)

    def test_versioned_json_does_not_pass_unreviewed(self):
        self.record('metadata:\n  date_added: "2026-09-07"')
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = review.main(["--json", "--all", "--as-of", TODAY.isoformat()])
        data = json.loads(out.getvalue())
        self.assertEqual(code, 1)
        self.assertEqual(data["schema_version"], 2)
        self.assertEqual(data["not_reviewed_count"], 1)
        self.assertEqual(data["overdue_count"], 0)
        self.assertEqual(data["attention_count"], 1)

    def test_current_only_returns_success(self):
        self.record('metadata:\n  last_reviewed: "2026-09-01"')
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(review.main(["--as-of", TODAY.isoformat()]), 0)

    def test_empty_scan_is_error_not_success(self):
        with contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(review.main(["--as-of", TODAY.isoformat()]), 2)


if __name__ == "__main__":
    unittest.main()
