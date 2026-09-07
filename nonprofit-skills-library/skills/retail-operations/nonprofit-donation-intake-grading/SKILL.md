---
name: nonprofit-donation-intake-grading
description: "Runs donated-goods intake for a thrift/resale operation: drop-off and pickup scheduling and logistics, sorting and quality grading, sell/recycle/discard triage, and at-donation receipt issuance. Use for 'set up a donation drop-off process,' 'grade incoming donations,' 'reduce discard rate.' Does not cover tax valuation/Form 8283 (nonprofit-in-kind-gift-acceptance) or shelf pricing (nonprofit-retail-pricing-merchandising)."
license: MIT
---

# Nonprofit Donation Intake & Grading

## When to Use This Skill

Use this skill to design or fix the physical intake pipeline for a resale operation (Goodwill-style
retailer, Habitat ReStore, hospital/church thrift shop): donor drop-off and pickup logistics, sorting
and grading donated goods, deciding what goes to the sales floor versus salvage/recycling versus the
landfill, and issuing the at-donation receipt donors need for their own records. Typical triggers:
"we have a backlog of unsorted donations," "design our drop-off shed workflow," "our discard rate is
too high," "train new intake volunteers on grading," "set up an at-donation receipt process."

**Boundary:** this skill handles the physical intake/sort/grade/triage workflow and the basic
at-donation receipt (a dated acknowledgment of items received, no value stated). It does not handle
donor-side tax valuation or receipting beyond that basic receipt — IRS Form 8283, the $500/$5,000
appraisal thresholds, qualified appraisals, and gift acceptance policy for high-value or unusual
in-kind gifts live in `nonprofit-in-kind-gift-acceptance`. Once an item is graded and released to the
floor, its price and merchandising treatment is `nonprofit-retail-pricing-merchandising`; if it's
routed to online sale instead of the floor, handoff to `nonprofit-online-resale`.

## Core Framework: The Intake Funnel

Model intake as a funnel with a named decision at each stage, not an undifferentiated "donations
pile":

1. **Acceptance** — accept or decline at the point of donation (curbside, drop-off door, home
   pickup) against a written accepted/not-accepted items list.
2. **Sort** — split by category (clothing, housewares, furniture, electronics, books/media,
   hazardous/recall) and by initial condition.
3. **Grade** — apply a consistent quality standard within each category.
4. **Triage** — route each graded item to one of four lanes: **Sell-floor**, **Sell-online** (high
   value, handoff to `nonprofit-online-resale`), **Salvage/recycle/textile-recycler or auction-bin
   liquidator**, or **Discard** (landfill, last resort).
5. **Receipt** — issue the donor's at-donation receipt before or at drop-off, regardless of which
   lane the item is later routed to.

Track a **sell-through rate by intake lane** and a **discard rate as % of donation volume by
weight or unit** — these two numbers are the standard health metrics for an intake operation; a
rising discard rate is the earliest signal of an acceptance-policy or donor-communication problem,
not a grading problem.

## Standard Terminology

- **Accepted items list**: the written, publicly posted list of what the org takes (e.g., clothing,
  small furniture, working small appliances) and explicitly does not take (mattresses without law
  tags, cribs pre-2011 standard, CRT TVs, upholstered furniture with rips/stains, recalled items).
- **Grading tiers**: typically Premium/Boutique (like-new, name-brand, sets), Standard (sellable,
  normal wear), Value/As-Is (functional but heavily worn, sold at a flat low price or by-the-pound),
  and Reject (not sellable — routed to salvage or discard).
- **Salvage stream / diversion rate**: goods routed to textile recyclers, scrap-metal buyers, or
  bulk/auction liquidators instead of the sales floor or the landfill; tracking this as a % of total
  intake demonstrates environmental-mission impact to funders and is often reportable separately from
  retail revenue.
- **Bailment period**: the short window (commonly 24-72 hours) between drop-off and formal
  acceptance during which title has not yet transferred, used in some donation agreements to allow a
  final accept/decline decision after inspection — check state law and the org's own gift acceptance
  policy before relying on a bailment clause.

## Step-by-Step: Building or Fixing an Intake Operation

1. **Publish a written accepted/not-accepted items list** and post it at every drop-off point, on the
   website, and with any pickup-scheduling tool — vague guidance ("bring your gently used items") is
   the single biggest driver of high discard rates and volunteer burnout from unusable donations.
2. **Design the drop-off/pickup logistics.** For staffed drop-off: define hours, a covered
   unloading area, and a "no unattended drop after hours" policy if illegal dumping at the donation
   shed is a problem. For scheduled home pickup: set a routing/scheduling cadence (e.g., weekly by
   zone), a minimum-item threshold to justify a truck stop, and a pre-pickup phone/text screen
   against the accepted-items list to avoid wasted trips.
3. **Set up the sort station** physically separate from the sales floor, with labeled bins per
   category and a clear "reject" bin visible to sorters so declines are consistent, not ad hoc.
4. **Write and train to a grading rubric** with photos of each tier per category (this is worth
   building as a real one-page laminated reference per category — clothing, housewares, electronics —
   since grading disagreement between volunteers/staff is the most common intake quality complaint).
5. **Test electronics and anything with a plug or battery** before grading it sellable; never place
   untested electrical items on the floor — this is both a safety and a return-rate issue.
6. **Route high-value or collectible-looking items to a designated reviewer** (not the general sort
   line) for a decision between sell-floor, online listing (`nonprofit-online-resale`), or referral
   to `nonprofit-in-kind-gift-acceptance` if the item may need formal tax documentation.
7. **Issue the at-donation receipt at the point of drop-off**: dated, lists the organization's name
   and EIN, a general description of item categories (not a per-item value — the donor is
   responsible for valuing their own non-cash gift for tax purposes), and a standard statement that
   no goods or services were provided in exchange. Do not let receipt issuance become a bottleneck
   that discourages donors from completing drop-off.
8. **Track discard rate and diversion rate monthly** and review with the intake team; if discard rate
   rises, the fix is almost always to the accepted-items list or donor communication, not to
   re-training graders.
9. **Reconcile intake volume against any hauling/disposal cost** — discard and salvage streams often
   carry a real cost (tip fees, recycler pickup fees); an intake operation that doesn't track this
   cost will understate the true cost of donation processing in the business model.

## Standard Deliverables

- Written accepted/not-accepted items list (public-facing)
- Drop-off and pickup logistics plan (hours, routing cadence, minimum thresholds)
- Category grading rubric with tier photos
- Intake triage flowchart (sell-floor / sell-online / salvage / discard)
- At-donation receipt template
- Monthly intake dashboard: volume, discard rate, diversion rate, sell-through by lane

## Common Failure Modes

- **Vague accepted-items list** leading to high discard rates and volunteer time spent triaging junk.
- **No separation between sort station and sales floor**, so ungraded, untested, or unsafe items
  reach customers.
- **Untested electronics placed on the floor**, creating safety complaints and refund/return churn.
- **High-value items sorted into the general line** instead of routed to a designated reviewer, losing
  revenue that online resale or a proper in-kind gift process would have captured.
- **Receipt issuance skipped or delayed**, generating donor complaints at tax time and eroding repeat
  donation behavior.
- **Discard cost untracked**, making the true cost of running the donation program invisible to
  leadership and the board.

## Practitioner vs. Advisor Framing

- **As store/intake staff or a program manager**, build the grading rubric with photos, not just
  prose — text-only standards produce inconsistent grading between volunteers on different shifts,
  which is the top driver of both high discard rates and pricing disputes downstream.
- **As a consultant advising a thrift operation**, diagnose intake problems by looking at the
  discard-rate trend line first before touching staffing or pricing — a discard-rate spike almost
  always traces back to an acceptance-policy or donor-communication gap upstream, and fixing pricing
  or staffing without fixing that gap won't move the number.
