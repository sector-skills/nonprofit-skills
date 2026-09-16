---
name: nonprofit-reserves-cash-flow
description: "Designs operating reserve policy (target months of expense, funding sources, drawdown/replenishment triggers), builds 12-13 week and annual cash flow forecasts, and plans bridge financing for seasonal or grant-timing funding gaps (lines of credit, grant advances, reimbursement-cycle float). Use when asked how many months of reserves a nonprofit should hold, to build a cash flow forecast or cash flow projection, to diagnose a cash crunch or seasonal gap, to write a board reserve policy, or to plan around delayed reimbursement grants. Does not cover the annual operating budget itself (use nonprofit-budgeting), producing GAAP financial statements (use nonprofit-financial-statements), or indirect cost rate/true-cost analysis (use nonprofit-cost-allocation)."
license: MIT
metadata:
  supervision: "review"
  supervision_note: "Reserve policy and cash forecasts drive real solvency decisions."
  date_added: "2026-09-07"
  date_added_source: "git:1860ed47a83901ff5e6d45abc4a2ef05be8fd4cd"
---

# Nonprofit Reserves & Cash Flow

## When to Use This Skill

Use this skill to set or evaluate an operating reserve policy, build a cash flow forecast, or plan
around a funding timing gap. Trigger tasks include: "how many months of reserves should we hold,"
"draft a board reserve policy," "we have a cash crunch in Q3 even though our budget is balanced for
the year," "build a 13-week cash flow forecast," "our biggest grant reimburses 60 days after we
spend — how do we bridge that," or "should we open a line of credit."

Boundary: this skill is about liquidity and reserves, not the underlying revenue/expense plan itself
(that's `nonprofit-budgeting`) or GAAP-format reporting of what already happened
(`nonprofit-financial-statements`). It does not cover indirect cost rate methodology
(`nonprofit-cost-allocation`).

## Core Framework: Two Distinct Problems

Nonprofits conflate "we don't have enough reserves" with "we have a cash timing problem" — they need
different fixes:

- **Reserve adequacy** is a *balance sheet* question: how large a financial cushion exists to absorb
  an unplanned shock (lost grant, program overrun, economic downturn).
- **Cash flow** is a *timing* question: even a fully funded, break-even-budget year can have months
  where cash out exceeds cash in, because revenue and expense hit the bank on different schedules
  (e.g., grant reimbursed 60-90 days after spend, or a major gala's revenue lands in Q4 but payroll is
  monthly).

Diagnose which problem is actually present before recommending a fix — a nonprofit with adequate
reserves can still face a cash crisis from pure timing mismatch, and building more reserves is the
wrong first response to a timing problem (a line of credit or accelerated invoicing is).

## Operating Reserve Policy Design

1. **Set the target in months of operating expense**, not a flat dollar figure, so it scales with the
   organization. Nonprofit Finance Fund and most sector guidance point to **3-6 months of operating
   expenses** as a typical target band; organizations with volatile or concentrated revenue
   (single-funder dependency, heavy government reimbursement, seasonal earned income) should target
   the higher end or beyond; stable, diversified-revenue organizations can run closer to 3 months.
2. **Define what counts.** Reserves are unrestricted, board-designated funds set aside specifically
   for this purpose — not the sum of all net assets without donor restriction, and never restricted
   funds. Separately disclose the reserve from other unrestricted net assets on the balance
   sheet/dashboard (ties back to `nonprofit-financial-statements` net asset disclosure practice).
3. **Name the funding source and build-up plan** — a starting board-approved allocation, then a
   routine mechanism (e.g., "1% of unrestricted revenue annually until target is met," or "year-end
   surplus first goes to reserves until target, then to program investment").
4. **Write explicit drawdown triggers and approval authority** — e.g., "ED may draw down to cover a
   documented cash shortfall of up to $X with notice to the board chair; draws above $X or for
   non-emergency purposes require finance committee approval." Vague reserve policies ("use in case
   of emergency") fail in practice because nobody agrees on what counts as an emergency when the
   moment comes.
5. **Write a replenishment requirement** — a timeline (e.g., "replenish within 24 months") and a
   named funding mechanism, so a draw doesn't become permanent erosion.
6. **Board-adopt the policy formally** and revisit the target annually alongside the budget process.

## Cash Flow Forecasting

- **13-week cash flow forecast**: the standard short-horizon tool — a rolling weekly cash-in/cash-out
  projection for the next quarter, updated weekly with actuals replacing projections as weeks pass.
  Use for organizations in or approaching a cash-tight period, or as a standing practice for any
  organization with grant-reimbursement-heavy revenue.
- **Annual cash flow forecast**: monthly cash-in/cash-out for the full fiscal year, built from the
  approved budget but re-timed — this is the step budgeting often skips. Take each budget revenue and
  expense line and ask "in which month does the cash actually move," not "in which month is it
  recognized." Payroll and rent are monthly and predictable; grant reimbursements, pledge payments,
  and event revenue are lumpy and must be modeled by actual expected receipt date.
- **Build steps:**
  1. Start with the approved annual budget (`nonprofit-budgeting` output) as the base.
  2. Re-time each revenue line to its expected cash-receipt month (not accrual/recognition month).
  3. Re-time each expense line to its expected cash-disbursement month.
  4. Add beginning cash balance for month 1.
  5. Roll forward: ending cash (month N) = beginning cash + cash in − cash out, becomes beginning
     cash for month N+1.
  6. Flag every month where the projected ending balance drops below the reserve floor or a
     board-set minimum operating cash threshold — these are the months needing a bridge plan, not
     year-end totals.
  7. Update monthly (or weekly, in a tight period) with actuals; re-forecast the remaining months
     rather than treating the original forecast as fixed.

## Bridging Seasonal and Reimbursement-Timing Gaps

- **Line of credit (LOC)**: the standard bridge tool for predictable, recurring timing gaps (e.g.,
  reimbursement grants). Secure it *before* it's needed — a lender underwriting during a cash crisis
  is a much worse negotiating position. Many community foundations and CDFIs (Community Development
  Financial Institutions) offer nonprofit-specific LOCs.
  Nonprofit Finance Fund is a well-known specialty lender in this space.
- **Grant/contract advance or accelerated invoicing**: for government cost-reimbursement contracts,
  ask the funder about advance payment provisions or invoice more frequently (monthly instead of
  quarterly) to shrink the float.
- **Deferred/negotiated payables**: for a short, known gap, negotiating vendor payment terms is
  cheaper and faster than new debt — but don't rely on this as an ongoing strategy since it damages
  vendor relationships and shifts risk downstream (see `nonprofit-vendor-facilities`).
- **Bridge/emergency loan funds**: some community foundations and CDFIs offer short-term nonprofit
  bridge loans specifically for grant-timing gaps — worth researching before defaulting to a
  commercial LOC.
- Never use restricted funds to cover an unrestricted cash shortfall (a common improper "borrowing"
  that becomes a legal and audit problem) — this is a compliance red line, not a judgment call; keep
  restricted-fund cash physically/system-segregated if reimbursement timing tempts commingling.

## Common Failure Modes

- No written reserve policy — reserves get spent ad hoc with no board visibility or drawdown
  discipline.
- Treating "cash in the bank" as fully available, ignoring that some of it is donor-restricted and
  already spoken for.
- Building the annual budget without ever re-timing it into a monthly/weekly cash forecast, so a
  perfectly balanced budget still produces a surprise cash crisis mid-year.
- Waiting until a cash crunch is already underway to apply for a line of credit.
- Informally "borrowing" from restricted funds to cover payroll during a gap.

## Standard Deliverables

- Board-adopted operating reserve policy (target, funding source, drawdown/replenishment rules)
- 13-week rolling cash flow forecast
- Annual monthly cash flow forecast tied to the approved budget
- Bridge financing plan/LOC application package for known seasonal gaps

## Practitioner vs. Advisor Framing

- **As the ED/finance lead**, keep the 13-week forecast as a living document, not a one-time exercise,
  and bring the board a reserve policy proposal with a specific number and funding mechanism rather
  than an abstract commitment to "build reserves someday."
- **As an advisor**, diagnose whether a client's stated "cash problem" is actually a reserve adequacy
  problem, a pure timing problem, or (most often) both — and don't recommend "raise more money" as
  the fix for a timing problem when a line of credit or renegotiated reimbursement cadence solves it
  faster and cheaper.
