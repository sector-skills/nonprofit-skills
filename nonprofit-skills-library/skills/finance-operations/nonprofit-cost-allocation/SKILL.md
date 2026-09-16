---
name: nonprofit-cost-allocation
description: "Calculates nonprofit indirect costs, evaluates federal de minimis elections and NICRA negotiation, and documents shared-cost allocation and true program costs. Use for rate selection, overhead allocation, or full-cost analysis. Does not build annual budgets, audited functional expense statements, or cash-flow plans; use nonprofit-budgeting, nonprofit-financial-statements, or nonprofit-reserves-cash-flow respectively."
license: MIT
metadata:
  supervision: "expert-required"
  supervision_note: "Indirect cost rates and NICRAs under 2 CFR 200 are negotiated with the federal government."
  date_added: "2026-09-07"
  date_added_source: "git:1860ed47a83901ff5e6d45abc4a2ef05be8fd4cd"
---

# Nonprofit Cost Allocation

## When to Use This Skill

Use this skill for the formal, methodology-driven side of splitting shared costs: calculating an
indirect cost rate, deciding on the de minimis rate vs. negotiating a full rate, determining what a
program truly costs to run (including its fair share of overhead), and documenting the allocation
method itself. Trigger tasks include: "what indirect cost rate should we use on this federal grant,"
"should we elect a de minimis rate or negotiate our own," "a funder says they'll only cover
direct costs — what do we do," "what does our afterschool program actually cost per participant when
you include its share of overhead," or "write our cost allocation plan for the auditor."

Boundary: this skill produces the *rate and methodology*. Using that methodology inside the annual
budget-building process is `nonprofit-budgeting`. Reporting actual functional expenses on the
audited statements is `nonprofit-financial-statements`. This skill does not cover reserve or cash
timing questions (`nonprofit-reserves-cash-flow`).

## Core Terminology

- **Direct costs**: costs specifically identifiable to one program/grant/contract (program staff
  salary, program supplies, participant transportation).
- **Indirect costs**: shared costs not readily assignable to one cost objective, such as shared
  HR, accounting, insurance, rent, or IT; classification depends on actual circumstances.
  Administrative costs are not automatically indirect: distinguish a program's administrative-cost
  cap from its indirect-cost rules. See [OMB FAQs 51–52](https://www.cfo.gov/assets/files/2%20CFR%20Revised%20FAQs%201-30-25.pdf).
- **Indirect cost rate**: allowable indirect costs divided by the specified allocation base when
  calculating a negotiated rate; an elected de minimis percentage is not a calculation of actual
  overhead. Use the base authorized for the applicable award and rate agreement, not total project
  cost or a board-facing overhead ratio.
- **MTDC (modified total direct costs)**: under the revised rule, direct salaries/wages, applicable
  fringe, materials/supplies, services, travel, and up to the first **$50,000 of each subaward**,
  regardless of its period of performance. Exclude equipment, capital expenditures, patient care,
  rental costs, tuition remission, scholarships/fellowships, participant support, and each
  subaward's excess over $50,000; other exclusions require serious-inequity grounds and cognizant
  agency approval. Distinguish subawards from contractor payments; do not reset the subaward
  threshold each year. See [2 CFR 200.1](https://www.law.cornell.edu/cfr/text/2/200.1).
- **Cost pool**: a grouping of similar indirect costs allocated together using one allocation basis
  (e.g., an "occupancy pool" allocated by square footage; a "shared administration pool" allocated by
  headcount or direct labor).
- **Federal NICRA (Negotiated Indirect Cost Rate Agreement)**: an agreement with the Federal
  cognizant agency specifying rate, base, type, and effective period. Federal negotiated rates
  carry acceptance protections; a rate negotiated only with a pass-through entity is not
  automatically binding on other funders. See [2 CFR 200.414(c)–(d)](https://www.law.cornell.edu/cfr/text/2/200.414)
  and [200.332(b)(4)](https://www.law.cornell.edu/cfr/text/2/200.332).
- **De minimis election**: eligible recipients/subrecipients without a **current Federal negotiated
  rate, including a provisional rate**, may choose **up to 15% of MTDC**, not a mandatory 15%.
  Having had an expired rate is not itself disqualifying; resolve outstanding provisional/fixed
  rate obligations with the cognizant agency. No documentation is required to justify use of the
  de minimis rate, but ordinary cost records and an accurate base remain necessary. Do not apply it
  to cost-reimbursement contracts issued directly by the Federal Government under the FAR.
  See [2 CFR 200.414(f)](https://www.law.cornell.edu/cfr/text/2/200.414) and
  [OMB FAQs 24, 55, 57](https://www.cfo.gov/assets/files/2%20CFR%20Revised%20FAQs%201-30-25.pdf).

## Step-by-Step: Rate Decision and Calculation

1. **Establish award applicability before selecting a percentage.** Collect the Federal award,
   subaward if any, amendments, agency implementation guidance, existing rate agreements, and
   proposed cost period. Record the governing rule version and effective date. The 2024 revisions
   generally govern Federal awards entered into on or after October 1, 2024; older awards require
   agency implementation through amendment or an authorized documented exception. A new subaward
   date alone does not update an older underlying Federal award. Do not retroactively charge the
   increased de minimis rate, or silently replace an existing NICRA's $25,000 subaward base with
   $50,000. Honor its approved base until appropriately revised. See
   [COFFA implementation guidance](https://www.energy.gov/sites/default/files/2025-08/COFFA-FY%202024%20Revisions%20to%202%20CFR-%20Federal%20Agency%20Implementation.pdf).
2. **Check current agreements and eligibility.** Identify Federal versus pass-through negotiation,
   rate type (including provisional), effective dates, extensions, base, and outstanding settlements.
   Use a current Federal negotiated rate subject to applicable exceptions. If none exists, assess
   the de minimis election or negotiation; for subawards, resolve any existing pass-through agreement
   and determine the appropriate rate collaboratively, rather than assuming Federal reciprocity.
   See [200.332(b)(4)](https://www.law.cornell.edu/cfr/text/2/200.332).
3. **Compare eligible options without promising recovery.** Model the elected percentage, allowable
   base, available award funding, and unrecovered costs. Consider negotiation if the recoverable
   difference warrants the work. De minimis is optional and does not require a rate proposal or proof
   of actual overhead. Do not add it when all costs, including overhead, are already charged directly.
   See [200.414(f)](https://www.law.cornell.edu/cfr/text/2/200.414) and
   [OMB FAQs 57, 67](https://www.cfo.gov/assets/files/2%20CFR%20Revised%20FAQs%201-30-25.pdf).
4. **Prepare the appropriate support.** For negotiation, confirm the Federal cognizant agency under
   the nonprofit assignment rules in Appendix IV, paragraph C.2.a, then prepare its required
   proposal, financial statements, pools, bases, and supporting allocation records; do not assume a
   pass-through's own cognizant agency is the nonprofit's. For a pass-through-negotiated rate, obtain
   that entity's process and scope. For de minimis, record the election, applicability, MTDC
   calculation, exclusions, and cumulative subaward amounts as operational controls, not as a
   requirement to substantiate the percentage. See the cognizant-agency definition in
   [200.1](https://www.law.cornell.edu/cfr/text/2/200.1) and
   [200.414(f)](https://www.law.cornell.edu/cfr/text/2/200.414).
5. **Apply consistently without double charging.** Once elected, use de minimis for Federal awards
   until choosing to receive a negotiated rate, while respecting award-version and effective-date
   differences. Do not switch methods to maximize individual claims or charge the same cost directly
   and indirectly. Reconcile internal allocation records to each award's authorized rate and base;
   different funder reimbursement rules do not justify inconsistent cost classification. See
   [200.414(f)](https://www.law.cornell.edu/cfr/text/2/200.414).
6. **Verify a cap's authority before accepting it.** A private foundation using non-Federal funds
   may set its own reimbursement terms. For Federal funds, agencies and pass-through entities may
   not force a lower de minimis rate than the eligible recipient's election unless Federal statute
   or regulation requires it; federally negotiated rates have the acceptance and deviation rules in
   [200.414(c)–(f)](https://www.law.cornell.edu/cfr/text/2/200.414).
   Ask for the written authority behind a conflicting cap and escalate to the grants/finance
   specialist before finalizing. Quantify any lawful recovery gap as an organizational subsidy;
   do not assume it qualifies as Federal cost share.
7. **Stop for qualified review.** Deliver a draft with a named finance/CPA or indirect-cost
   specialist checking eligibility, applicable rules, rate/base pairing, calculations, and any
   exceptions before submission or reliance. Completion means reconciled calculations, documented
   review status, and no unresolved assumption presented as an approved rate.

## Worked MTDC Check

Use this example only after confirming the revised rules apply and the nonprofit is eligible
and elects 15%. Assume all listed direct costs are otherwise allowable:

| Direct-cost component | Amount | Included in MTDC |
|---|---:|---:|
| Salaries/fringe, supplies, services, and travel | $150,000 | $150,000 |
| One subaward, full-period total | $80,000 | $50,000 |
| Equipment | $20,000 | $0 |
| Rental costs | $10,000 | $0 |
| Participant support | $5,000 | $0 |
| Total | $265,000 | $200,000 |

Indirect costs are $200,000 × 15% = $30,000; total direct plus indirect is $295,000.
The excluded $65,000 does not become unallowable merely because it is outside MTDC.
If $40,000 of that subaward has already entered the base, only $10,000 more can enter,
not a fresh $50,000 in the next year. These exclusions follow
[200.1](https://www.law.cornell.edu/cfr/text/2/200.1); never transplant this base into
an older award or a NICRA with different approved terms.

## True-Cost-of-Program Analysis

Distinct from the compliance-driven indirect rate: this answers "what does it really cost to deliver
this program/unit of service," for internal decision-making (pricing a contract, deciding whether to
grow or sunset a program, setting a per-participant cost for a funder conversation).

1. Start with all direct program costs (staff, supplies, direct participant costs).
2. Add the program's allocated share of every indirect cost pool using documented, benefit-based
   allocation methods. Reconcile this actual-cost view to the same underlying accounting data,
   separately explaining Federal exclusions and reimbursement limits; a de minimis recovery
   calculation is not a measure of actual overhead.
3. Divide by units of service (participants served, sessions delivered) to get a true per-unit cost.
4. Compare true cost per unit to what funders/fees/contracts actually pay per unit — this gap is the
   amount of unrestricted revenue subsidizing the program every year, and it's the number a board
   needs before deciding whether to grow, hold, or sunset that program.
5. Present this alongside — never instead of — the budget's programmatic framing, so the board sees
   both the mission case and the subsidy math (ties to `nonprofit-program-scaling` when the decision
   is to grow, and `nonprofit-budgeting` for how it flows into next year's plan).

## Common Failure Modes

- Treating 10% as the current universal ceiling, or 15% as compulsory, without checking election,
  eligibility, and award applicability.
- Reading "no documentation to justify use" as permission to omit expense records, base exclusions,
  or double-charge checks; conversely, demanding a negotiated-rate proposal for a de minimis election.
- Applying the percentage to total direct costs, resetting the subaward threshold annually, or
  changing a NICRA's base without an approved revision.
- Applying different allocation methods to different grants to make each one's numbers look better —
  fails consistency requirements and is an audit/negotiation red flag.
- Confusing the compliance indirect rate (a specific % for federal purposes) with the board-facing
  "overhead ratio" from the functional expense statement — related but not the same number, and
  conflating them in board or funder conversations causes confusion.
- Never revisiting the rate after organizational growth (new facility, added staff) — an old rate
  understates real current indirect costs.

## Standard Deliverables

- Cost allocation plan for negotiated-rate support or internal actual-cost analysis, as applicable
- Indirect cost calculation or de minimis election memo, with award/version/effective-date matrix,
  rate/base authority, exclusions, cumulative subaward tracking, and qualified-review status
- NICRA negotiation package (if pursuing a full rate)
- True-cost-per-unit analysis by program

## Practitioner vs. Advisor Framing

- **As finance staff**, keep time studies and allocation basis documentation current year-round, not
  reconstructed retroactively at audit time — auditors and rate negotiators will ask for
  contemporaneous support.
- **As an advisor**, the de minimis-vs-negotiate decision is a quantifiable one: model actual
  indirect costs as a % of MTDC before recommending either path, and quantify any funder-imposed
  indirect cap as an explicit subsidy amount so the board can weigh it as a real cost of accepting
  that grant, not an invisible one.

Targeted federal indirect-cost check: September 16, 2026. Recheck the linked regulations,
agency implementation, and actual award/rate documents at use; this is not a certification
of an organization's eligibility or a comprehensive professional review of this skill.
