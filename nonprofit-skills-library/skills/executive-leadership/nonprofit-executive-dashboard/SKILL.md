---
name: nonprofit-executive-dashboard
description: "Designs the nonprofit ED/COO one-page executive dashboard and matching quarterly board scorecard: picking 8–15 cross-functional KPIs across finance, fundraising, programs, people/culture, and mission delivery; separating leading from lagging indicators; setting SMART targets and yellow/red thresholds; assigning owners and data sources; wiring the monthly leadership-team and quarterly board review rhythms; tying it to the strategic plan. Use when asked to build or fix an executive dashboard, KPI scorecard, leadership team scorecard, monthly ops review, or the board scorecard/metrics section of a board packet. Does not cover preparing the underlying financial statements (use nonprofit-financial-statements), program outcome and evaluation design (use nonprofit-outcomes-measurement), installing EOS org-wide (use nonprofit-eos-traction), writing the strategic plan (use nonprofit-strategic-planning), or the CEO's narrative board report that uses this dashboard (use nonprofit-ceo-board-partnership)."
license: MIT
metadata:
  supervision: "review"
  supervision_note: "Board-facing KPIs drive decisions; a wrong indicator misdirects the org."
  last_reviewed: "2026-09-07"
  date_added: "2026-09-07"
  date_added_source: "git:34f6bfb6b4bc8cabe1683622f7fc16704d6a80b9"
---

# Nonprofit Executive Dashboard

## When to Use This Skill

Use this skill when an executive director, COO, CEO, or board chair needs a working
cross-functional KPI system: a one-page dashboard the leadership team reviews monthly, and a
shorter scorecard the board reviews quarterly. Trigger tasks include: "design our ED dashboard,"
"pick the KPIs our leadership team should watch every month," "our board scorecard has 40 metrics
and no one reads it — cut it down," "set targets and yellow/red thresholds for our KPIs," "we only
report lagging numbers — what leading indicators should we add," "align the dashboard to the
strategic plan," or "separate what the ED reviews weekly/monthly from what the board sees
quarterly."

Boundary: this skill designs the dashboard *system* — metric selection, targets, thresholds,
owners, layouts, and review rhythms — not the underlying data. Preparing the financial statements
that feed the finance KPIs is `nonprofit-financial-statements`. Designing program outcome
indicators, theory of change, and evaluation methodology is `nonprofit-outcomes-measurement` (this
skill *pulls from* those indicators but does not design them). Installing EOS across the whole
organization (Vision/Traction Organizer, L10 meeting pulse, Rocks, People Analyzer) is
`nonprofit-eos-traction`; this skill uses the scorecard *discipline* from EOS/Rockefeller Habits but
does not install the full system. Writing the strategic plan the dashboard measures is
`nonprofit-strategic-planning`. The CEO's narrative report to the board that *uses* this dashboard
is `nonprofit-ceo-board-partnership`.

## Core Framework: Two Dashboards, Not One

The single most common failure is one dashboard trying to serve both the leadership team and the
board. They have different jobs, different time horizons, and different audiences — split them:

- **ED/COO operational dashboard**: 8–15 KPIs, reviewed monthly by the leadership team (weekly for a
  smaller "pulse" subset). Answers "are we on track this quarter?" Includes leading indicators the
  team can *act on* between meetings. Owned by the ED.
- **Board scorecard**: 5–8 KPIs, reviewed quarterly by the board. Answers "is the organization
  healthy and on strategy?" Skews toward lagging outcome and financial-health indicators, plus a
  narrative on the one or two things that matter most this quarter. Owned by the board chair with
  the ED.

If the board is looking at monthly cash disbursements by vendor, the governance/management line is
broken (see `nonprofit-board-governance`). If the ED's team is only looking at quarterly
lagging outcomes, they cannot steer.

## Named Frameworks to Draw From

- **Balanced Scorecard, adapted for mission** (Kaplan & Norton, adapted): use four perspectives —
  **mission impact** (replaces "customer" as the top perspective for a nonprofit), **financial
  health**, **stakeholder/constituent**, and **learning & growth (people/culture)**. Force at least
  one KPI per perspective so the dashboard cannot silently collapse into all-finance or all-output-
  counts.
- **Nonprofit Finance Fund financial-health indicators**: **months of cash / liquid unrestricted net
  assets (LUNA)**, **operating reliance** (share of expenses covered by reliably renewable revenue),
  **debt ratio**, and **operating surplus/deficit margin**. These are the finance-perspective floor
  for any ED dashboard.
- **Propel Nonprofits balance-sheet + income-statement indicators**: pairs balance-sheet strength
  (months of LUNA, debt as % of unrestricted net assets, receivables aging) with income-statement
  performance (revenue composition, program vs. M&G+fundraising expense mix, change in net assets)
  — use to round out the finance panel beyond a single "months of cash" number.
- **Rockefeller Habits / EOS scorecard discipline**: every KPI has a **named human owner** (not a
  department), a **weekly or monthly cadence** with an actual number entered, and a **red/yellow/
  green** status against target — reviewed at a standing leadership meeting. The point is not the
  spreadsheet; it is the review meeting that closes the loop.
- **Leading vs. lagging indicators**: a **lagging** indicator confirms what already happened (YTD
  revenue, months of cash, program participants served). A **leading** indicator predicts it (major
  gift pipeline stage-weighted value, grant proposals submitted this month, staff eNPS, program
  waitlist growth). A dashboard with no leading indicators is a rearview mirror. Rule of thumb: aim
  for at least one leading indicator per Balanced Scorecard perspective.
- **SMART targets**: every KPI's target is Specific, Measurable, Achievable, Relevant, Time-bound —
  and set *before* the period starts, not reverse-engineered from what was hit.
- **The "one metric that matters most this quarter" rule**: name a single north-star KPI per quarter
  (or per strategic priority) that the leadership team and board both watch. Prevents the dashboard
  from becoming a wall of equal-weight numbers where nothing is actually the priority.

## Numbered Checklist: Building the Dashboard

Follow in order — skipping steps is what produces the failure modes below.

1. **Start from the strategic plan**, not from available data. List the 3–5 strategic objectives.
   Every KPI must trace to an objective; if it doesn't, cut it or cut the objective.
2. **Brainstorm candidate indicators per Balanced Scorecard perspective** — mission impact,
   financial, stakeholder, learning & growth. Expect 30–50 candidates.
3. **Cut to 8–15 KPIs for the ED dashboard, and 5–8 for the board scorecard.** More than 15 and the
   monthly review becomes a status readout instead of a decision meeting.
4. **Tag each KPI leading or lagging.** If the dashboard is more than ~70% lagging, add leading
   indicators until every perspective has at least one.
5. **Set a SMART target and yellow/red thresholds for each KPI** (e.g., green ≥ 3 months of cash,
   yellow 1.5–3, red < 1.5). Thresholds are what trigger action — no threshold, no trigger, no
   action.
6. **Assign a single named owner per KPI** (not "Finance" — the CFO by name). The owner is
   accountable for the number appearing on time and for narrating variance.
7. **Pick the authoritative data source and cadence per KPI** — one system of record per metric,
   documented, so two people never report different numbers for the same KPI.
8. **Design the one-page layout**: group by Balanced Scorecard perspective, show target vs. actual
   vs. threshold status, sparkline or trend arrow for direction, and reserve the top-right for the
   "one metric that matters most this quarter." Pick the chart form to match the question — trend
   line for direction over time, bullet chart for actual vs. target vs. threshold, stacked bar for
   composition (e.g., revenue mix), gauge only if a bounded % vs. threshold is what a non-analyst
   viewer must grasp in three seconds.
9. **Wire the review rhythm**: monthly leadership-team review of the full ED dashboard on a standing
   agenda (see below); optional weekly 15-minute pulse on a 3–5 KPI subset; quarterly board
   scorecard review at the regular board meeting.
10. **Schedule the annual reset** (see checklist below) at the same time each year, right after the
    strategic plan is refreshed and the next-year budget is approved.

## Standard Deliverables

- **One-page ED/COO KPI dashboard** grouped by Balanced Scorecard perspective, with target, actual,
  threshold status, trend, and the quarter's north-star metric highlighted.
- **Board scorecard** (fewer metrics, longer time horizon — typically trailing 4–8 quarters shown),
  paired with the CEO narrative from `nonprofit-ceo-board-partnership`.
- **KPI definitions document**, one row per KPI: name, plain-English definition, exact formula,
  system of record, owner (by name), cadence, target, yellow/red thresholds, leading/lagging tag,
  strategic-objective link.
- **Leadership-team monthly review agenda**: quick red/yellow scan (5 min) → focused discussion of
  every red and any newly-yellow KPI, owner narrates variance and proposed action (30–40 min) →
  north-star metric deep-dive (10 min) → decisions and owners captured. Reviews of green items are
  skipped by default.
- **Quarterly OKR set aligned to the strategic plan** — 3–5 objectives, 2–4 key results each,
  explicitly cross-referenced to the dashboard KPIs that measure them.
- **Annual dashboard reset checklist**: re-confirm strategic objectives; retire KPIs that no longer
  tie to an objective or no longer drive action; add KPIs for any new objective; rebaseline targets
  and thresholds against the new budget; confirm owners and data sources; refresh the one-page
  layout; recommit to the review rhythm on the calendar.

## Common Failure Modes

- **Too many metrics / vanity-metric bloat** — a 40-KPI dashboard is a report, not a decision tool.
  Cut to 8–15 for the ED, 5–8 for the board.
- **No leading indicators** — dashboard only reports after the fact; team cannot steer. Force at
  least one leading indicator per Balanced Scorecard perspective.
- **Board scorecard = ED dashboard** — governance/management line broken. Split them and defend
  the split (see `nonprofit-board-governance`).
- **No thresholds** — everything is a number with no red/yellow/green, so nothing ever triggers
  action. Set thresholds or the review meeting devolves into narration.
- **No named owner per KPI** — "Finance owns it" means no one owns it. Assign a human by name.
- **Data source ambiguity** — two people report different numbers for the same KPI because they
  pulled from different systems. Name one system of record per metric in the KPI definitions doc.
- **Dashboard never revisited** — the strategic plan evolved, the dashboard didn't, and the two
  drift apart. Run the annual reset on a fixed calendar date.
- **Conflating a plan with a scorecard** — the strategic plan lists intended activities; the
  scorecard measures whether they moved the needle. If the "dashboard" is a task list, it is a plan,
  not a scorecard.

## Practitioner vs. Advisor Framing

- **As the ED or COO**, protect the two-dashboard split and the monthly review meeting on the
  calendar; those two decisions do 80% of the work. Bring one authored draft (candidate KPIs,
  targets, thresholds, owners) to the leadership team rather than co-designing from a blank page —
  the team edits far better than it invents, and dashboard-by-committee reliably lands at 30+
  metrics.
- **As an advisor**, diagnose before designing: pull the current dashboard, tag each metric
  leading vs. lagging, map each to a strategic objective, and count owners — the gaps (usually: too
  many lagging, no leading, no owners, no thresholds) name themselves and become the redesign
  brief. Frame the redesign as a two-artifact deliverable — ED dashboard *and* board scorecard —
  plus the KPI definitions document and the review-rhythm calendar, not just a prettier one-pager.
