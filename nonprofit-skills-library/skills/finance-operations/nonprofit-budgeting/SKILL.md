---
name: nonprofit-budgeting
description: "Builds a nonprofit's annual operating budget: revenue and expense projections, program-vs-admin-vs-fundraising allocation across functional categories, zero-based vs. incremental budgeting approaches, budget-to-actual variance setup, and the board approval process and calendar. Use when asked to build, draft, revise, or present an annual budget, allocate costs by function for budgeting purposes, set up a budget calendar, or prepare a budget narrative for board vote. Does not cover reading/producing the audited statement of activities or functional expense statement after the fact (use nonprofit-financial-statements), operating reserve targets or cash flow timing (use nonprofit-reserves-cash-flow), indirect cost rate calculation for grants (use nonprofit-cost-allocation), or internal control design (use nonprofit-financial-controls)."
license: MIT
---

# Nonprofit Budgeting

## When to Use This Skill

Use this skill to build or revise a nonprofit's annual operating budget, decide between budgeting
methodologies, allocate projected costs across program/management-general/fundraising, or run the
budget through board approval. Trigger tasks include: "build our FY27 operating budget," "help me
figure out what percent of our budget should be program vs. overhead," "we need a zero-based budget
this year instead of just adding 3%," "draft a budget narrative for the finance committee," "set up
a budget calendar," or "our board wants a multi-year budget projection tied to the strategic plan."

Boundary: this skill produces the *plan*. Turning actuals into GAAP-format financial statements is
`nonprofit-financial-statements`. Setting reserve targets or forecasting cash timing within the
budget year is `nonprofit-reserves-cash-flow`. Calculating a formal indirect cost rate for a federal
or foundation grant is `nonprofit-cost-allocation`. Designing who approves what dollar threshold is
`nonprofit-financial-controls`.

## Core Framework

A nonprofit operating budget is a **board-approved financial plan of revenue and expense for one
fiscal year**, built at the account/program level and rolled up to functional categories for external
reporting. Treat it as three linked documents, not one:

1. **Revenue budget** — grants, contracts, individual giving, events, earned income, investment
   income, in-kind — each line tied to a named source or a documented assumption (e.g., "renewal
   probability 80% based on 3-year history").
2. **Expense budget** — built by natural category (salaries, benefits, occupancy, professional fees,
   travel, supplies) *and* tagged by program/department, so it can be re-sliced into functional
   categories.
3. **Functional allocation** — the same expense dollars re-cut into Program Services, Management &
   General, and Fundraising, per FASB ASC 958-720. This is what a board and outside reviewers (Charity
   Navigator, GuideStar/Candid, grantors) will judge.

## Budgeting Methodologies — Choosing and Naming the Approach

- **Incremental budgeting**: prior year actuals ± a percentage adjustment. Fast, low-conflict, but
  perpetuates existing allocation and hides sunk-cost programs. Default for stable organizations.
- **Zero-based budgeting (ZBB)**: every line must be justified from zero each cycle, program by
  program. Surfaces programs that no longer earn their keep; expensive in staff time. Recommend for
  organizations that haven't reassessed program mix in 3+ years, post-merger, or after a major
  revenue shock.
- **Priority-based (a.k.a. Budgeting for Outcomes)**: rank programs against mission/strategic
  priorities first, then fund top-ranked programs fully before funding lower-ranked ones — useful
  when revenue is flat or declining and across-the-board cuts would hurt high-performing programs as
  much as weak ones.
- **Program/activity-based budgeting**: build the budget by program (each with its own mini P&L)
  rather than only by natural expense category — needed once an org has 3+ distinct programs with
  different funding mixes, since it exposes which programs are subsidized by unrestricted revenue.
- **Rolling/multi-year forecast**: 12-month budget plus a 2-3 year projection updated quarterly — pair
  with `nonprofit-strategic-planning` outputs when the board wants the budget to visibly fund
  strategic priorities.

State which method is being used and why; do not silently default to incremental when the
organization's situation (declining revenue, program pruning, post-merger) calls for ZBB or
priority-based.

## Program-vs-Admin-vs-Fundraising Allocation

- Every cost is either **direct** (traceable to one program, e.g., a case manager's salary) or
  **shared/indirect** (benefits multiple functions, e.g., the ED's salary, rent, IT, the finance
  director).
- Allocate shared costs using a documented, defensible basis — headcount %, square footage, time
  studies/timesheets by function, or a negotiated indirect cost rate (see `nonprofit-cost-allocation`
  for the formal rate-negotiation version of this). Time studies are the most audit-defensible basis
  for personnel costs that split across functions.
- Common failure mode: dumping all occupancy, IT, and admin salaries into "Management & General"
  without allocation, which inflates the reported overhead ratio and triggers funder/watchdog
  scrutiny (Charity Navigator and BBB Wise Giving Alliance both flag high M&G ratios). Fix by
  allocating a reasonable share of shared costs to programs based on actual usage.
- Common failure mode #2: over-allocating to programs to make the overhead ratio look artificially
  low — this fails an audit or a funder cost review when the allocation basis isn't documented and
  reproducible. Every allocation percentage must be traceable to a stated method (see
  `nonprofit-cost-allocation`).
- There is no single "correct" overhead ratio; benchmark against organizations of similar size/sector
  rather than a flat 15%/85% rule of thumb, and be ready to explain the ratio's composition rather
  than just the number.

## Step-by-Step: Building the Annual Budget

1. **Set the calendar.** Work backward from the fiscal year start and the board's final vote date.
   Typical timeline for a June 30 fiscal year end: kickoff/assumptions in February, department/program
   drafts in March, finance committee review in April, board first read in May, board approval in
   June. Adjust similarly for a December 31 fiscal year end.
2. **Set budget assumptions first, in writing** — salary increase %, benefits inflation, known grant
   renewals/losses, new program launches, inflation on occupancy/insurance. Circulate assumptions to
   department heads before they draft numbers so everyone budgets against the same baseline.
3. **Build revenue first, conservatively.** Use a probability-weighted approach for uncommitted
   revenue (committed/contracted = 100%, highly likely = 75-90%, prospective/unconfirmed = 25-50%).
   Never budget to a fundraising goal that has no plan behind it — cross-check every revenue line
   against the development plan/pipeline (see `nonprofit-donor-pipeline` for the underlying pipeline).
4. **Build expenses program-by-program and department-by-department**, tagging each line with the
   program/department it belongs to so the functional roll-up is mechanical, not a re-derivation.
5. **Reconcile to net.** Decide upfront whether the board requires a balanced budget, allows a planned
   deficit funded from reserves (state the dollar amount and reserve impact explicitly — see
   `nonprofit-reserves-cash-flow`), or requires a modest surplus to build reserves.
6. **Run the functional allocation** and check the resulting Program / M&G / Fundraising percentages
   against the prior year and peer benchmarks before it goes to committee — large swings need a
   one-line explanation ready for the board.
7. **Finance committee review.** Expect questions on: variance vs. prior year actuals, any new FTEs,
   assumptions behind the largest revenue lines, and the M&G ratio. Bring a one-page assumptions memo,
   not just the spreadsheet.
8. **Board approval.** Most bylaws require full board vote on the annual budget (check
   `nonprofit-bylaws-policy` if unclear); present a summary page (revenue by source, expense by
   function, net, reserve impact) plus the detail as an appendix — do not hand the board the full
   general-ledger-level workbook as the primary document.
9. **Set up budget-to-actual monitoring** — monthly or quarterly variance reports against this
   approved budget, with a defined threshold (e.g., >10% or >$5,000 variance) that triggers a written
   explanation to the finance committee.
10. **Amend formally when needed.** A material shift (new large grant, lost major funder, unplanned
    hire) should go back to the board or finance committee as a budget amendment, not be silently
    absorbed — keep an amendment log for audit trail.

## Standard Deliverables

- Budget assumptions memo (1 page)
- Revenue detail by source with probability weighting
- Expense detail by natural category, tagged by program/department
- Functional expense summary (Program / M&G / Fundraising %)
- Board-facing budget summary (1 page) + full detail appendix
- Budget calendar with named owners and dates
- Budget-to-actual variance report template (monthly/quarterly)

## Common Failure Modes

- Budgeting revenue to a fundraising *goal* rather than a *pipeline* — creates a mid-year crisis when
  the gap surfaces in month 8.
- No written assumptions, so a board member's "why did salaries jump 12%?" has no ready answer.
- Treating the functional allocation as an afterthought done only for the 990, instead of building it
  into the budget structure from day one — this causes a scramble every year and inconsistent
  methodology year to year.
- No variance monitoring cadence set at approval time, so the board only learns of a problem at
  year-end.
- Approving a deficit budget without an explicit reserve drawdown plan and reserve-policy check.

## Practitioner vs. Advisor Framing

- **As the ED/finance staff**, build the budget bottom-up from program and department input, own the
  assumptions memo, and drive the calendar so finance committee/board deadlines aren't missed.
- **As an advisor/consultant**, frame budget review as a governance and strategy conversation for the
  board: is the functional allocation defensible to funders and watchdogs, does the revenue mix match
  the strategic plan's priorities, and is the board being shown a decision-ready summary rather than
  a raw spreadsheet. Push back diplomatically on incremental "add 3% to everything" budgets when the
  underlying situation (revenue decline, program underperformance) calls for zero-based or
  priority-based budgeting instead.
