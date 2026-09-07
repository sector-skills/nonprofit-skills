---
name: nonprofit-cost-allocation
description: "Calculates and negotiates indirect cost rates (de minimis 10% de minimis rate, negotiated indirect cost rate agreements/NICRA under 2 CFR 200 Uniform Guidance), builds true-cost-of-program analysis, and designs shared-cost allocation methodologies (time studies, square footage, headcount, cost pools) for splitting overhead across programs and grants. Use when asked to calculate an indirect cost rate, decide whether to elect the 10% de minimis rate, negotiate a NICRA with a federal cognizant agency, determine the true full cost of running a program, or design/document a cost allocation plan. Does not cover building the overall annual operating budget or its program/admin/fundraising split for board purposes (use nonprofit-budgeting), producing the audited functional expense statement (use nonprofit-financial-statements), or reserve/cash-timing questions (use nonprofit-reserves-cash-flow)."
license: MIT
---

# Nonprofit Cost Allocation

## When to Use This Skill

Use this skill for the formal, methodology-driven side of splitting shared costs: calculating an
indirect cost rate, deciding on the de minimis rate vs. negotiating a full rate, determining what a
program truly costs to run (including its fair share of overhead), and documenting the allocation
method itself. Trigger tasks include: "what indirect cost rate should we use on this federal grant,"
"should we take the 10% de minimis rate or negotiate our own," "a funder says they'll only cover
direct costs — what do we do," "what does our afterschool program actually cost per participant when
you include its share of overhead," or "write our cost allocation plan for the auditor."

Boundary: this skill produces the *rate and methodology*. Using that methodology inside the annual
budget-building process is `nonprofit-budgeting`. Reporting actual functional expenses on the
audited statements is `nonprofit-financial-statements`. This skill does not cover reserve or cash
timing questions (`nonprofit-reserves-cash-flow`).

## Core Terminology

- **Direct costs**: costs specifically identifiable to one program/grant/contract (program staff
  salary, program supplies, participant transportation).
- **Indirect costs (a.k.a. overhead, administrative costs, F&A — facilities & administrative costs
  in federal terminology)**: costs that benefit multiple programs and cannot be readily assigned to
  one (ED salary, HR, finance/accounting, general liability insurance, shared office rent, IT).
- **Indirect cost rate**: indirect costs ÷ a defined base (usually a modified total direct cost base,
  "MTDC," which excludes items like capital equipment, the portion of subawards over $25,000, and
  tuition remission — check the specific base definition before applying any rate).
- **Cost pool**: a grouping of similar indirect costs allocated together using one allocation basis
  (e.g., an "occupancy pool" allocated by square footage; a "shared administration pool" allocated by
  headcount or direct labor).
- **NICRA (Negotiated Indirect Cost Rate Agreement)**: a formal, binding rate agreement with a federal
  cognizant agency (or pass-through entity), valid for a set period and applicable to all federal
  awards unless a specific program restricts it.
- **De minimis rate**: under 2 CFR 200.414(f) (Uniform Guidance), any non-federal entity that has
  never had a negotiated rate may elect a **flat 10% of MTDC** without any negotiation or
  documentation burden — usable on all federal awards, and once elected, must be used consistently
  across all federal awards until the org chooses to negotiate a real rate.

## Step-by-Step: Rate Decision and Calculation

1. **Check whether a NICRA already exists.** If a federal agency or a pass-through (a state agency
   re-granting federal funds) has already negotiated a rate with this organization, that rate is
   generally usable across other federal awards per Uniform Guidance reciprocity — confirm before
   starting a new calculation.
2. **If no NICRA exists, decide: de minimis (10% MTDC) vs. negotiate a real rate.**
   - Take the **de minimis rate** if indirect costs are genuinely close to 10% of MTDC, staff time for
     a full rate proposal isn't available, or the organization is small/early-stage. It's
     immediate, requires no negotiation, and is defensible with minimal documentation.
   - **Negotiate a full rate** if actual indirect costs are meaningfully above 10% of MTDC (common for
     organizations with real facilities costs, larger finance/HR infrastructure, or heavy
     compliance overhead) — leaving real recoverable indirect costs unclaimed at a flat 10% shorts
     the organization every year going forward.
3. **To negotiate a full rate:** identify the cognizant agency (the federal agency providing the most
   direct federal funding, or via a pass-through's cognizant relationship), prepare an indirect cost
   rate proposal per the agency's format (usually following the cost principles in 2 CFR 200 Subpart
   E), and submit supporting financial statements and a cost allocation plan. Expect a multi-month
   negotiation cycle; plan around it, don't leave it for the week before a grant deadline.
4. **Build the cost allocation plan underlying any rate**: list every indirect cost pool, its
   allocation basis, and the documentation supporting that basis (time studies for personnel,
   square footage for occupancy, headcount for shared admin). This plan is the artifact auditors and
   negotiators actually scrutinize — the rate itself is just the output.
5. **Apply the rate consistently.** Once elected/negotiated, apply the same rate/methodology across
   all federal awards and, ideally, all funding sources for internal consistency — switching methods
   grant-by-grant is a red flag in both audits and rate negotiations.
6. **Watch for funder caps that override the negotiated/de minimis rate.** Some foundations and some
   federal programs cap allowable indirect recovery below the org's actual negotiated rate (e.g., a
   foundation limiting indirect to 15% regardless of the org's real NICRA) — when this happens, name
   the gap explicitly as a *subsidy the organization is providing to that grant* rather than letting
   it silently erode general operating capacity.

## True-Cost-of-Program Analysis

Distinct from the compliance-driven indirect rate: this answers "what does it really cost to deliver
this program/unit of service," for internal decision-making (pricing a contract, deciding whether to
grow or sunset a program, setting a per-participant cost for a funder conversation).

1. Start with all direct program costs (staff, supplies, direct participant costs).
2. Add the program's allocated share of every indirect cost pool using the *same* documented
   allocation bases as the compliance rate — don't invent a separate, undocumented method for internal
   analysis; keep both views reconciled to the same underlying data.
3. Divide by units of service (participants served, sessions delivered) to get a true per-unit cost.
4. Compare true cost per unit to what funders/fees/contracts actually pay per unit — this gap is the
   amount of unrestricted revenue subsidizing the program every year, and it's the number a board
   needs before deciding whether to grow, hold, or sunset that program.
5. Present this alongside — never instead of — the budget's programmatic framing, so the board sees
   both the mission case and the subsidy math (ties to `nonprofit-program-scaling` when the decision
   is to grow, and `nonprofit-budgeting` for how it flows into next year's plan).

## Common Failure Modes

- Taking the 10% de minimis rate every year without ever checking whether actual indirect costs are
  well above that — quietly leaving grant-recoverable overhead unclaimed for years.
- No documented cost allocation plan behind the rate — this is one of the most common federal audit
  findings (a rate or allocation with no supporting time studies or basis documentation).
- Applying different allocation methods to different grants to make each one's numbers look better —
  fails consistency requirements and is an audit/negotiation red flag.
- Confusing the compliance indirect rate (a specific % for federal purposes) with the board-facing
  "overhead ratio" from the functional expense statement — related but not the same number, and
  conflating them in board or funder conversations causes confusion.
- Never revisiting the rate after organizational growth (new facility, added staff) — an old rate
  understates real current indirect costs.

## Standard Deliverables

- Cost allocation plan (pools, bases, documentation)
- Indirect cost rate calculation or de minimis election memo
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
