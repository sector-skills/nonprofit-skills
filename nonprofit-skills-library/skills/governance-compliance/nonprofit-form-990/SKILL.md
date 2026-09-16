---
name: nonprofit-form-990
description: "Supports Form 990/990-EZ/990-N/990-PF preparation: choosing the correct variant, assembling schedules (A, B, C, G, J, L, O, R, etc.), functional expense allocation for Part IX, Part VI governance-question responses, public disclosure/inspection requirements, and a compliance calendar for the annual filing deadline and extensions. Use when asked to prepare or review a Form 990, decide which 990 variant applies, complete or check a specific schedule, respond to Part VI governance questions, handle a public disclosure request for the 990 or exemption application, or build a filing-deadline compliance calendar. Does not cover producing the underlying financial statements the 990 draws from (use nonprofit-financial-statements) or state charitable solicitation registration filings, which are separate from the federal 990 (use nonprofit-charitable-registration)."
license: MIT
metadata:
  supervision: "expert-required"
  supervision_note: "Filed with the IRS; errors carry penalties and public-disclosure consequences."
  date_added: "2026-09-07"
  date_added_source: "git:1860ed47a83901ff5e6d45abc4a2ef05be8fd4cd"
---

# Nonprofit Form 990 Preparation & Compliance

## When to Use This Skill

Use this skill for the federal annual information return and its public-disclosure obligations.
Trigger tasks include: "which 990 do we file — 990-N, 990-EZ, or full 990," "help me complete Schedule
A public support test," "what goes in Part VI governance questions," "someone requested a copy of our
990 — what are we required to provide," "build our 990 filing compliance calendar," or "explain
Schedule L related-party transactions to the board."

Boundary: this skill assembles and reviews the *return itself*; producing the statement of
activities/financial position and functional expense allocation the 990 is built from is
`nonprofit-financial-statements`. Separate state-level charitable solicitation registration filings
(which often require a copy of the 990 as an attachment but are a distinct compliance regime) are
`nonprofit-charitable-registration`.

## Choosing the Correct Variant

Match gross receipts and asset thresholds to the correct form (verify current-year IRS thresholds
before relying on exact dollar figures, since they are periodically adjusted):

- **990-N (e-Postcard)** — organizations normally with gross receipts ≤ $50,000; an 8-question
  online-only filing. No paper alternative exists — missing three consecutive years causes automatic
  revocation of exemption regardless of how small the organization is.
- **990-EZ** — gross receipts < $200,000 AND total assets < $500,000; a shortened version of the full
  return still requiring applicable schedules.
- **990 (full)** — gross receipts ≥ $200,000 OR total assets ≥ $500,000; the complete form with all
  applicable schedules.
- **990-PF** — required for all private foundations regardless of size (asset/receipts thresholds
  don't apply — a private foundation always files 990-PF, never 990-N/EZ/full).
- Organizations should not "choose" a smaller variant to reduce disclosure burden if the actual
  numbers require a larger one — filing the wrong variant is itself a compliance error, not merely a
  transparency choice.

## Core Schedules and What Each Does

- **Schedule A** — public charity status and the **public support test**: tracks whether the
  organization still qualifies as a public charity (vs. private foundation) under the 33⅓% support
  test or the 10%-facts-and-circumstances test, averaged over a 5-year period. A multi-year decline
  in broad-based public support (e.g., increasing reliance on a small number of large donors/grants)
  can push an organization toward failing this test — flag this early, since reclassification as a
  private foundation triggers materially different excise tax and payout rules.
- **Schedule B** — schedule of contributors above the reporting threshold; generally NOT required to
  be made public (donor names/addresses on Schedule B are confidential, unlike the rest of the 990) —
  a common disclosure mistake is releasing an unredacted Schedule B.
- **Schedule C** — political campaign and lobbying activities; ties directly to the 501(h) election
  and lobbying expenditure limits covered in depth in `nonprofit-c3-c4-structure`.
- **Schedule G** — fundraising events and gaming; reconciles gross revenue, direct expenses, and net
  income from galas/special events reported elsewhere (see `nonprofit-fundraising-events`).
- **Schedule J** — compensation detail for officers, directors, key employees, and highest-compensated
  employees above reporting thresholds; ties to the rebuttable-presumption-of-reasonableness process
  (see `nonprofit-board-governance`).
- **Schedule L** — transactions with interested persons (loans, grants, business transactions with
  directors/officers/their family or entities) — pulls directly from the conflict-of-interest
  disclosures maintained under `nonprofit-bylaws-policy`; incomplete COI disclosure tracking is the
  most common cause of an incomplete Schedule L.
- **Schedule O** — required supplemental narrative explaining "Yes" answers and providing detail the
  base form's checkboxes can't capture (e.g., describing the Part VI governance process in prose) —
  a 990 with thin or boilerplate Schedule O narrative is a common quality gap funders/raters notice.
- **Schedule R** — related organizations and transactions between them; essential for any
  organization operating a related 501(c)(4), for-profit subsidiary, or supporting organization (see
  `nonprofit-c3-c4-structure` for the dual-entity structure itself; this schedule reports the
  resulting relationship on the 990).

## Part VI: Governance, Management, and Disclosure

This section is scrutinized closely by funders, GuideStar/Candid, and state regulators as a proxy
for governance quality even though most of its questions are not strictly mandatory practices:

1. Report actual voting board member count and how many are independent (no compensation or
   material financial interest beyond director fees) — a low independence ratio invites follow-up.
2. Answer whether the full board (not just a subcommittee) reviewed the 990 before filing — best
   practice is a documented board or audit-committee review with adequate advance time, minuted.
3. Confirm and describe: written conflict-of-interest policy (yes, with annual disclosure — see
   `nonprofit-bylaws-policy`), written whistleblower policy, written document retention policy, and
   the process used to determine compensation for the top management official and other officers
   (the rebuttable-presumption process).
4. State whether governing documents, COI policy, and financial statements are made available to the
   public and how — consistency between what's claimed here and actual public disclosure practice
   matters (see disclosure rules below).

## Public Disclosure Requirements

- Organizations must provide copies of their three most recent Form 990s (excluding Schedule B donor
  information) and their original exemption application (Form 1023/1024) with determination letter
  to anyone who requests them in person or in writing, within statutory timeframes (in-person
  requests: same day; written requests: within 30 days).
- Widely available exception: if the return is posted on the organization's own website or a
  recognized public database (e.g., the IRS's own tax-exempt organization search, or Candid/
  GuideStar/ProPublica Nonprofit Explorer) in a downloadable format, the organization is not required
  to separately fulfill individual copy requests.
- A reasonable copying/mailing fee may be charged for paper fulfillment; the request cannot be
  refused outright, and refusal or unreasonable delay carries per-day IRS penalties against
  responsible individuals, not just the organization.

## Compliance Calendar

1. **Due date**: the 15th day of the 5th month after fiscal year-end (e.g., May 15 for a calendar-
   year filer) — build the internal prep calendar backward from this date, not forward from year-
   start.
2. **Extension**: a single automatic 6-month extension is available via Form 8868, moving a calendar-
   year filer's deadline to November 15 — file the extension before the original deadline, not after.
3. **Internal milestones to calendar**: books closed and reconciled (30-60 days after year-end) →
   draft return from preparer/accountant → board or audit committee review window (allow at least
   2 weeks, not a same-day rubber stamp) → filing → posting to organization's website/GuideStar
   profile update.
4. **Automatic revocation risk**: failing to file for three consecutive years (including 990-N)
   triggers automatic loss of tax-exempt status with no separate IRS notice beyond standard
   correspondence — reinstatement requires a new exemption application and, depending on timing, back
   -filing and a reasonable-cause statement. Treat three consecutive missed 990-Ns as seriously as a
   missed full 990, since small organizations are the most common revocation victims.

## Standard Deliverables

- 990 variant determination memo
- Schedule-by-schedule prep checklist with source-document owners
- Part VI governance-question response draft for board review
- Filing compliance calendar with internal milestone dates
- Public disclosure fulfillment procedure (website posting + request-response process)

## Practitioner vs. Advisor Framing

- **As the ED or finance lead**, build the compliance calendar backward from the filing deadline and
  get the draft return in front of the board/audit committee with real review time, not a rubber-
  stamp — Part VI's honest answer to "did the board review this" is being tracked by funders reading
  the return.
- **As an advisor**, use Schedule A's public support test trend and Part VI's governance answers as
  quick diagnostic entry points into a broader governance or compliance engagement — a client whose
  Schedule O narrative is thin or whose Part VI shows no independent board review is very likely to
  have deeper gaps addressable through `nonprofit-board-governance` and `nonprofit-bylaws-policy`.
