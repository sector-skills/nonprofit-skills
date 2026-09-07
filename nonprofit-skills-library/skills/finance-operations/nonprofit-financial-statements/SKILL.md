---
name: nonprofit-financial-statements
description: "Reads and produces nonprofit financial statements under FASB ASC 958: statement of financial position (balance sheet), statement of activities (income statement with net asset classes), statement of functional expenses, and statement of cash flows; explains net asset classification (with/without donor restrictions), and translates these statements into plain-language board and committee presentations for non-finance board members. Use when asked to prepare, review, or explain monthly/quarterly/annual financial statements, reconcile net assets, build a functional expense statement, or create a board financial dashboard. Does not cover building the forward-looking annual budget (use nonprofit-budgeting), reserve/cash-flow forecasting (use nonprofit-reserves-cash-flow), Form 990 preparation (use nonprofit-form-990), or indirect cost rate methodology (use nonprofit-cost-allocation)."
license: MIT
---

# Nonprofit Financial Statements

## When to Use This Skill

Use this skill to produce, review, or explain the core nonprofit financial statements, or to
translate them for a board that isn't finance-fluent. Trigger tasks include: "prepare our Q2
statement of activities," "why did net assets without donor restriction drop this quarter," "build a
one-page financial dashboard for the board," "explain the difference between our income statement
and a for-profit's," "reconcile restricted vs. unrestricted net assets," or "walk the finance
committee through the functional expense statement before the audit."

Boundary: this skill covers the *statements themselves and explaining them*. Building the
forward-looking budget those statements will later be compared against is `nonprofit-budgeting`.
Forecasting cash timing and reserve adequacy is `nonprofit-reserves-cash-flow`. Form 990 public
filing mechanics are `nonprofit-form-990`. Formal indirect cost rate calculation/negotiation is
`nonprofit-cost-allocation`. Internal control design over who can approve/post transactions is
`nonprofit-financial-controls`.

## The Four Core Statements (FASB ASC 958)

1. **Statement of Financial Position** (nonprofit's "balance sheet"): Assets = Liabilities + Net
   Assets, at a point in time. Net Assets split into exactly two classes since ASU 2016-14: **Net
   Assets Without Donor Restrictions** and **Net Assets With Donor Restrictions** (the old
   unrestricted/temporarily restricted/permanently restricted three-bucket model was retired for
   fiscal years starting after Dec 15, 2017 — flag it if a client's template still shows three
   buckets, that's outdated).
2. **Statement of Activities** (the nonprofit "income statement"): Revenue less Expenses = Change in
   Net Assets, shown by net asset class, for a period. Unlike a for-profit P&L, it must show how
   restricted revenue becomes unrestricted as restrictions are satisfied — the "net assets released
   from restriction" line, which nets to zero across the two columns but is often the line board
   members misread as new revenue.
3. **Statement of Functional Expenses**: every expense cross-tabbed by *natural category* (rows:
   salaries, benefits, occupancy, supplies, travel, professional fees, depreciation) against
   *functional category* (columns: Program Services — often split by individual program —
   Management & General, Fundraising). Required for most nonprofits' audited statements and feeds
   Form 990 Part IX directly.
4. **Statement of Cash Flows**: operating/investing/financing activities, reconciling change in net
   assets to change in cash — often the most-skipped statement in board packets but the one that
   answers "do we actually have the cash," which the accrual-basis statement of activities does not.

## Net Asset Classification — Get This Right

- **Without donor restrictions**: available for any purpose consistent with mission, including
  board-designated funds (e.g., a board-designated reserve) — board designations are *internal* and
  do NOT create a donor-restricted class; they stay in the "without restrictions" bucket but should be
  footnoted/schedule-disclosed separately so the board can see what's actually free vs.
  self-restricted.
- **With donor restrictions**: purpose-restricted (must be spent on X), time-restricted (can't be
  spent until year Y), or perpetual (endowment corpus that must be held forever, with only earnings
  spendable per the spending policy). A pledge/multi-year grant is restricted revenue in full at the
  time it's unconditionally promised, recognized in the year pledged, not spread across the years
  it will be spent — this is the single most common recognition error in nonprofit books and it
  distorts year-over-year comparisons if done inconsistently.
- Endowments follow UPMIFA (Uniform Prudent Management of Institutional Funds Act) state law for what
  counts as corpus vs. spendable appreciation; don't assume all realized gains are free to spend
  without checking the gift instrument and state UPMIFA rules.

## Step-by-Step: Producing Monthly/Quarterly Statements

1. **Close the books first** — all bank/credit card reconciliations done, AP/AR cutoffs applied,
   payroll accrued, depreciation posted, before pulling statements. A statement pulled from an
   unreconciled ledger is not a deliverable.
2. **Pull the trial balance** and map it to the chart of accounts' functional/program tags (this
   mapping should already exist from the budgeting process — see `nonprofit-budgeting`).
3. **Build the Statement of Financial Position** first — it's the foundation; verify Assets =
   Liabilities + Net Assets ties exactly before moving on.
4. **Build the Statement of Activities**, split by net asset class, including the "released from
   restriction" line for any restricted funds spent this period.
5. **Build/update the Statement of Functional Expense** allocation using the same allocation basis
   used in the budget (time studies, headcount %, square footage) — consistency year-over-year
   matters more than the specific method, since auditors and funders check for consistent
   application.
6. **Run budget-to-actual variance** against the approved annual budget (from `nonprofit-budgeting`)
   and flag variances over the organization's stated threshold.
7. **Draft the plain-language narrative** — 3-5 bullet points translating the numbers: cash position,
   any restricted-fund concentration risk, notable variances, and the bottom-line change in net
   assets, in plain English with no undefined jargon.
8. **Package for the audience.** Full committee gets all four statements plus variance detail; full
   board gets a 1-page dashboard (see below) plus statements as an appendix.

## Explaining Statements to a Non-Finance Board

- Translate "change in net assets" as "did we grow or shrink our financial cushion this period,"
  not "profit."
- Show the *trend* (3-5 periods side by side), not just the current snapshot — a single month/quarter
  in isolation invites misreadings of normal seasonality (e.g., a summer program's revenue arriving
  in Q3 looks like a "loss" in Q1-Q2 if shown alone).
- Explicitly separate "money we can spend on anything" (net assets without restriction, minus any
  board designations) from "money that's already spoken for" (with donor restrictions) — board
  members routinely conflate total net assets with available cash.
- Build a **one-page financial dashboard**: total revenue vs. budget, total expense vs. budget, net
  assets without restriction (available), cash on hand in days of operating expense, and the
  functional expense ratio — this is the standard board-ready artifact, with full statements attached
  as backup only.
- Common failure mode: presenting the full GAAP-format statements with no narrative and no trend,
  leaving the board to either disengage or ask granular questions the meeting has no time for. Lead
  with the narrative and dashboard; keep the statements as appendix.
- Common failure mode: describing restricted grant revenue received this period as "available" —
  this misleads the board on true flexible capacity and can lead to overspending unrestricted funds.

## Standard Deliverables

- Statement of Financial Position (current + prior period comparative)
- Statement of Activities (with/without donor restriction columns)
- Statement of Functional Expenses
- Statement of Cash Flows
- Budget-to-actual variance report
- One-page board financial dashboard with plain-language narrative

## Practitioner vs. Advisor Framing

- **As finance staff/ED**, close the books before pulling statements, keep the functional allocation
  methodology consistent period to period, and translate every board packet into a narrative — never
  hand over raw statements with no cover explanation.
- **As an advisor**, use these statements diagnostically in a client engagement: check whether net
  asset classification is correctly bifurcated post-ASU 2016-14, whether board designations are
  disclosed separately from true unrestricted funds, and whether the functional allocation
  methodology is documented and consistent — inconsistent or undocumented allocation is one of the
  most common audit management-letter findings and a frequent driver of a `nonprofit-financial-controls`
  engagement.
