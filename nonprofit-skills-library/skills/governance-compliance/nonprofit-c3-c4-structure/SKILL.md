---
name: nonprofit-c3-c4-structure
description: "Structures and operates paired 501(c)(3)/501(c)(4) entity arrangements: entity design decisions, the 501(h) expenditure test election for lobbying limits, substantial-part-test alternative, cost-sharing and shared-staff/shared-resource allocation compliance, common-control governance, and inter-entity transaction documentation. Use when asked to decide whether an organization needs a companion 501(c)(4), set up or review a dual c3/c4 structure, elect or evaluate the 501(h) expenditure test versus the substantial-part test, allocate shared staff time/overhead/facilities costs between the two entities, or document inter-entity transactions and cost-sharing agreements to withstand IRS scrutiny. Does not cover direct legislator meeting/testimony/lobby-day tactics (use nonprofit-legislative-advocacy) or general coalition MOU structuring (use nonprofit-coalition-building)."
license: MIT
metadata:
  supervision: "expert-required"
  supervision_note: "Entity structure and 501(h) election decisions carry tax-exemption risk."
  date_added: "2026-09-07"
  date_added_source: "git:1860ed47a83901ff5e6d45abc4a2ef05be8fd4cd"
  last_reviewed: "2026-11-09"
---

# Nonprofit 501(c)(3)/501(c)(4) Dual-Entity Structure

## When to Use This Skill

Use this skill for the legal/structural and compliance mechanics of operating a 501(c)(3) alongside
a companion 501(c)(4), and for lobbying expenditure limit elections. Trigger tasks include: "should
we set up a 501(c)(4) alongside our 501(c)(3)," "explain the difference between the 501(h)
expenditure test and the substantial-part test," "should we make the 501(h) election," "how do we
allocate shared staff time between our c3 and c4," "draft a cost-sharing/shared-services agreement
between the two entities," or "are we at risk of the c4's activity jeopardizing the c3's exempt
status."

Boundary: this skill covers entity structure and expenditure-limit compliance. The actual tactics of
meeting with legislators, preparing testimony, and lobby days are `nonprofit-legislative-advocacy`.
Building multi-organization advocacy coalitions and their MOUs (a different kind of inter-
organization document than the cost-sharing agreement here) is `nonprofit-coalition-building`.

## Why Organizations Pair a 501(c)(3) with a 501(c)(4)

A 501(c)(3) can lobby, but only within strict limits (below), and cannot engage in any partisan
political campaign activity (supporting/opposing candidates) at all — that prohibition is absolute,
with no expenditure-test equivalent. A 501(c)(4) social welfare organization may lobby without limit
(lobbying germane to its social welfare purposes can even be its primary activity) and may engage in
a limited amount of political campaign activity (though such activity cannot be the organization's
"primary activity," and c4s face separate, distinct reporting requirements around campaign spending,
including possible tax on political expenditures under IRC 527(f)). A lobbying c4 may also have to
give members a notice of the share of dues used for lobbying or pay a proxy tax (IRC 6033(e)).
Organizations set up a paired c4 specifically to house unlimited lobbying and/or
electoral-adjacent work that would either exceed the c3's lobbying cap or that a c3 cannot do at all,
while keeping charitable, tax-deductible-donation-eligible work in the c3. The trade-off: c4
donations are NOT tax-deductible to the donor, which is why organizations keep the c3 primary for
fundraising and use the c4 narrowly for the activity that requires it.

## Lobbying Expenditure Limits: Two Tests

Every 501(c)(3) that lobbies at all must operate under one of these two regimes — silence is not a
safe default, because the default (if no 501(h) election is made) is the vaguer, riskier test:

1. **Substantial Part Test (default)** — the IRS default absent a 501(h) election. Prohibits
   lobbying from being a "substantial part" of the organization's activities, but does not define
   "substantial" with a bright-line percentage, and no percentage is a safe harbor — it's a
   facts-and-circumstances test covering both expenditures AND volunteer/staff time, which makes it
   harder to measure and defend than a pure dollar test. Excessive lobbying in any taxable year can
   cost the organization its exempt status (making all its income taxable), plus a 5% excise tax on
   that year's lobbying expenditures, and a separate 5% tax on managers who knowingly agreed to them
   (IRC 4912).
2. **501(h) Expenditure Test (elective)** — made by filing Form 5768, a one-time election
   (revocable) that replaces the vague substantial-part test with clear, sliding-scale dollar
   limits on lobbying expenditures as a percentage of the organization's exempt-purpose expenditures.
   The statutory limit (IRC 4911(c)(2); not inflation-indexed) is 20% of the first $500,000 of
   exempt-purpose expenditures, 15% of the next $500,000, 10% of the next $500,000, and 5% of the
   rest, capped at $1,000,000 (reached at $17,000,000 of exempt-purpose expenditures) — confirm
   against the statute and current IRS guidance before relying on them. Critically, the 501(h)
   test also sets a separate, smaller sub-limit specifically for **grassroots lobbying** (calls to
   action directed at the general public to contact legislators) versus **direct lobbying**
   (communicating directly with legislators or their staff) — grassroots lobbying is capped at 25%
   of the total lobbying allowance, so classifying spend correctly between the two
   categories matters for compliance, not just total lobbying spend. Exceeding either limit in a
   year triggers a 25% excise tax on the excess (IRC 4911(a)); normally exceeding 150% of either
   limit, measured over a four-year period, puts exempt status at risk (IRC 501(h)(1)-(2)).
3. **Why most advocacy-active c3s elect 501(h)**: it converts an ambiguous, facts-and-circumstances
   standard into a bright-line, plannable dollar budget — advisors should generally recommend the
   election for any c3 doing regular, planned advocacy work, unless the organization is a private
   foundation or church (both ineligible to elect 501(h) — private foundations face an entirely
   separate, stricter lobbying prohibition regime; churches remain under the substantial-part test by
   default).
4. **Filing mechanics**: Form 5768 can be filed at any time during the first tax year it is to cover
   and remains in effect until revoked (a revocation takes effect the following tax year); track
   actual lobbying expenditures against the elected limits continuously (not just at filing time)
   and report them on Schedule C of Form 990 (see `nonprofit-form-990`).

## Cost-Sharing and Shared-Staff Compliance

The central IRS risk in a dual c3/c4 structure is that the c4's non-charitable activity (especially
unlimited lobbying or political activity) ends up being subsidized by the c3's tax-deductible funds
or resources — this is the failure mode every allocation practice below exists to prevent.

1. **Time tracking for shared staff**: any employee who works for both entities must track actual
   time spent on each entity's activities (contemporaneous timesheets, not an annual estimate), and
   each entity pays its proportional share of that employee's salary/benefits based on actual
   time — a retroactive, round-number allocation (e.g., "we'll just call it 50/50") is a common audit
   finding.
2. **Shared facilities/overhead**: rent, utilities, equipment, and administrative overhead shared
   between entities must be allocated on a reasonable, documented basis (square footage, headcount,
   or usage hours) and the c4 must actually pay its share — an unpaid or underpaid allocation is, in
   substance, a subsidy of the c4 by the c3; for a 501(h)-electing c3, the regulations treat such a
   below-fair-market-value transfer to a lobbying c4 as the c3's own lobbying expenditure, up to the
   c4's lobbying spend (26 CFR 56.4911-3(c)(3)).
3. **Written cost-sharing/shared-services agreement**: put the allocation methodology in a signed
   agreement between the two entities (even though under common control) specifying the basis for
   each shared cost category, the payment/reimbursement schedule, and a periodic true-up process —
   an unwritten or informal arrangement is far harder to defend under IRS examination than a
   documented one.
4. **Separate bank accounts and books**: each entity must maintain its own financial records and bank
   accounts; commingling funds (paying c4 expenses from the c3 account "temporarily") is a bright-line
   practice to avoid regardless of intent to true up later.
5. **Governance separation considerations**: the two entities can share some board members (common
   control is normal and expected in these structures) but should hold separate board meetings/
   minutes for each entity's own decisions, and any board member with a financial interest in
   transactions between the entities should follow the conflict-of-interest recusal process
   (`nonprofit-bylaws-policy`).
6. **The c4 may make grants to the c3, but not the reverse in a way that funds c4 lobbying/political
   activity** — a c3 cannot fund the c4's political campaign activity at all (the c3 prohibition
   covers indirect participation), and for a 501(h)-electing c3, below-fair-market-value transfers
   to a lobbying c4 count against the c3's own lobbying limits (see item 2), since otherwise the c3
   would indirectly do what it's restricted from doing directly; any inter-entity grant needs
   restriction language and monitoring confirming the funds are used only for activities the
   granting entity itself could fund directly.

## Common Failure Modes

- No 501(h) election made, then treating lobbying informally under the vaguer substantial-part test
  without ever measuring volunteer/staff time spent on advocacy, leaving no defensible record if
  challenged.
- Estimating shared-staff time allocation once a year from memory instead of contemporaneous
  timesheets.
- The c4 using c3-purchased equipment, mailing lists, or office space without a documented,
  reimbursed cost-sharing agreement.
- Treating grassroots lobbying spend as ordinary direct lobbying spend under the 501(h) test, missing
  that grassroots lobbying has its own tighter sub-limit.
- A c3 grant to the c4 with no restriction language, effectively funding c4 lobbying/political
  activity indirectly.

## Standard Deliverables

- Entity-structure decision memo (whether a companion c4 is warranted, and why)
- 501(h) election analysis and Form 5768 filing recommendation
- Cost-sharing/shared-services agreement template (staff time, facilities, overhead allocation
  methodology)
- Lobbying expenditure tracking log (direct vs. grassroots, against elected limits)
- Inter-entity grant restriction language template

## Practitioner vs. Advisor Framing

- **As the ED or general counsel liaison**, get contemporaneous timesheets and a signed cost-sharing
  agreement in place before the c4 does any real work, not after — retroactively reconstructing an
  allocation methodology under audit pressure is far harder than tracking it from day one; file Form
  5768 early if the organization plans any regular advocacy work.
- **As an advisor**, treat the decision to form a c4 as a significant structural commitment requiring
  ongoing administrative discipline (separate books, timesheets, agreements), not a one-time legal
  setup — flag to a client that the compliance burden of maintaining the wall between entities is
  often underestimated relative to the benefit of unlimited lobbying capacity, and confirm the
  organization's actual advocacy volume justifies it before recommending the structure.
