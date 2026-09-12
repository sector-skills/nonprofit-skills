---
name: nonprofit-housing-homeownership-programs
description: "Designs and operates nonprofit affordable homeownership programs — the Habitat-style cycle from homebuyer eligibility and selection through sweat equity, below-market financing (0% first mortgages, silent seconds, forgivable loans), underwriting, closing, and post-purchase support. Use when a user says 'draft our homebuyer selection policy', 'how many sweat equity hours should we require', 'should we use a 0% first mortgage or a silent second', 'can this family afford our house at 60% AMI', 'our homebuyer is 60 days delinquent', or 'what resale formula should our program use'. Not for community land trusts, limited-equity co-ops, or perpetual deed restrictions (use nonprofit-housing-community-ownership), build-day volunteer operations (use nonprofit-housing-construction-volunteers), the development capital stack (use nonprofit-housing-development-finance), or raising donor funds for construction (use nonprofit-capital-campaigns)."
license: MIT
supervision: review
supervision_note: "Selection policies, loan structures, and resale formulas carry fair-housing and lending-law exposure and become legal loan documents; a knowledgeable staffer must review before adoption."
last_reviewed: 2026-09-12
---

# Nonprofit Affordable Homeownership Programs

## When to Use This Skill

Use this skill when the task is to design, document, or operate a nonprofit affordable
homeownership program — the full cycle from recruiting and selecting homebuyers through
sweat equity, financing, closing, and post-purchase support. This is the Habitat-style
model where the nonprofit builds or rehabs the home, selects the family, and often holds
the mortgage itself. Concrete triggers:

- "Draft our homebuyer selection policy" / "What selection criteria can we legally use?"
- "How many sweat equity hours should we require, and how do we track them?"
- "Should we do a 0% first mortgage, a below-market rate, or a silent second?"
- "Can this family afford the payment? Walk us through the underwriting."
- "Our affiliate is the lender — what disclosure rules apply to us?"
- "Our homebuyer is 60 days delinquent. What's our playbook?"
- "What resale formula should our shared-equity program use?"

**Boundary — read before starting:**
- Community land trusts, limited-equity co-ops, 99-year ground leases, and perpetual
  stewardship of deed-restricted stock are `nonprofit-housing-community-ownership`. This
  skill covers resale formulas and shared-equity seconds *as features of a homeownership
  program*; the institutional shared-equity stewardship models belong to that sibling.
- Running volunteer build days — scheduling crews, site safety, skilled/unskilled mix —
  is `nonprofit-housing-construction-volunteers`. This skill treats buyer sweat equity as
  a *program requirement*, not as volunteer program management (general volunteer
  programs are `nonprofit-volunteer-management`).
- Assembling the development capital stack (LIHTC, HOME/CDBG awards, bonds) to build the
  homes is `nonprofit-housing-development-finance`. Raising donor funds for construction
  is `nonprofit-capital-campaigns`.
- Selection criteria with disparate-impact risk (criminal history, credit cutoffs),
  reasonable accommodation in application processes, and affirmative marketing law are
  `nonprofit-housing-fair-housing` — apply that skill alongside selection-policy work.
- Deciding how the org fits the community's housing continuum is
  `nonprofit-housing-continuum-planning`. Measuring program outcomes generally is
  `nonprofit-outcomes-measurement`.
- The note, deed of trust, shared-equity second, and restrictive covenants themselves are
  legal instruments: draft the business terms here, then route documents to counsel
  before signing (see supervision note).

## The Program Cycle

Most nonprofit homeownership programs (Habitat affiliates, CHDOs, community development
corporations) run a repeating six-stage cycle. Every deliverable in this skill attaches to
a stage:

1. **Recruit & screen** → selection policy (below)
2. **Select** → committee, scoring, waitlist
3. **Prepare** → sweat equity + homebuyer education
4. **Underwrite & close** → affordability structure, ratios, disclosures
5. **Support** → post-purchase plan, early-default counseling
6. **Resale or steward** → resale formula enforcement

Practitioners (program directors, affiliate staff) need operational detail: tracking
sheets, hour logs, servicing cadences. Advisors/consultants should push for written,
board-adopted policies at each stage — most affiliates that fail compliance reviews or
fair-housing complaints failed at the *documentation* step, not the intent step.

## Homebuyer Eligibility and Selection Policy

**Deliverable: a homebuyer selection policy draft.** Habitat's classic triad — used by
hundreds of affiliates and adaptable to any program — is **need for adequate shelter,
ability to pay, and willingness to partner**. Structure the policy around those three,
each with objective, verifiable criteria:

**Need (housing inadequacy).** Define it concretely: overcrowding (persons-per-room
threshold), cost burden (paying over 30-50% of income for housing), physical defects
(verifiable condition issues), instability (doubled-up, substandard, or transitional
housing), or distance from work/school for a documented reason. "Need" must be a checklist
a reviewer can score from documents, not a narrative impression.

**Ability to pay.** Income band set from HUD Section 8 area median income (AMI) limits —
most programs target 30-80% AMI, some 50-80% AMI to ensure full PITI affordability.
Decide the band first; it drives everything else (lottery vs. queue, subsidy depth,
funder rules). Verify income the way HUD programs do: recent pay stubs, tax returns,
award letters for Social Security/SSI/VA, court orders for child support; count gross
income with a written, consistent definition (annualize seasonal work; discount
non-recurring income).

**Willingness to partner.** Expressed as the sweat equity requirement plus required
homebuyer education — define hours and completion conditions in the policy (below), not
as a vibe.

**Committee and scoring.** Numbered checklist for the policy draft:

1. State the mission, service area, and eligible household definition.
2. State the income band (AMI %) and household-size income limits table, updated annually
   when HUD limits publish (and state the update month).
3. Define need criteria as a scored checklist (e.g., 0-2 points per factor, thresholds
   for automatic eligibility).
4. Define minimum ability-to-pay thresholds (see Underwriting) — including a stated
   maximum back-end ratio and minimum residual income.
5. Define sweat equity hours and education requirements.
6. Describe the selection committee: quorum, conflict-of-interest rules (committee
   members recuse from applications they know personally or financially), and a rule that
   committee members score against written criteria only.
7. Describe the waitlist: rank by score then date, or lottery among qualified applicants;
   state the application validity period and re-qualification rules (typically 6-12
   months, re-verify income).
8. State reasons for ineligibility and an appeal path (review by an officer or board
   committee not involved in the original decision).
9. State the denial-letter practice: written, criteria-based, and consistent — the
   single most important fair-housing protection.
10. Attach the scoring rubric as an appendix and set an annual review date.

Failure-and-remedy: if your criteria include criminal-history screens, credit-score
cutoffs, or "stable employment" language, they carry disparate-impact risk — route the
criteria list through `nonprofit-housing-fair-housing` before adoption. Use alternative
credit (rent, utility, insurance, and phone payment histories) instead of score cutoffs
wherever possible.

Advisor note: benchmark the policy against 2-3 peer affiliates and against the funder's
rules (HOME-assisted homebuyers require underwriting per HUD standards) before board
adoption; get the board to adopt it by resolution, not staff memo.

## Sweat Equity Policy

**Deliverable: a sweat equity policy.** Purpose: stake, skills, and buy-in — it is not
free labor and must never be valued as such on financial reports. Components:

- **Hour requirement.** Typical range is 200-500 hours scaled by household size (single
  heads of household commonly earn or receive reduced requirements). State the per-adult
  expectation and whether hours are per-adult or per-household.
- **Eligible activities.** Construction on their own home, construction on other
  partner-family homes, homebuyer education classes (state the hours-per-class credit),
  office/admin support, and program events. Decide explicitly whether ReStore-type
  activities count; if you operate a retail social enterprise, its staffing rules belong
  to the retail-operations skills.
- **Tracking.** A log per family with date, activity, hours, and supervisor sign-off;
  monthly statements to the family; a named staff owner of the ledger. No
  verbal-confirmation credits — if it isn't in the log with a signature, it didn't happen.
- **Completion condition.** Set the closing gate: e.g., 100% of hours complete before
  closing, or a floor (e.g., 80%) with the remainder scheduled before move-in plus a
  written deferment process for medical, birth, or employment disruptions.
- **Modification and hardship.** Written process for reducing or deferring hours for
  disability (a reasonable-accommodation matter — coordinate with
  `nonprofit-housing-fair-housing`), single parenthood, or documented hardship.
- **Safety.** Minors' hours (if allowed) limited per child-labor rules; no power tools
  or roofing for volunteers under 18; site safety rules route to
  `nonprofit-housing-construction-volunteers`.

Failure-and-remedy: hours drift because families can't get build-site slots — schedule
families at their qualification time, not when the house is ready, and credit education
hours generously.

## Affordability Structures

**Deliverable: an affordability worksheet outline** — the calculation flow a staff
underwriter runs per family, in order:

1. **Household gross monthly income** (verified, annualized) →
2. **Target front-end ratio:** monthly PITI (principal, interest, taxes, insurance, and
   any HOA) as a percent of gross income. Conventional lenders use ~28%; Habitat-style
   programs commonly hold buyers at or below **30%** — set your program's ceiling (often
   30-33%) in policy and apply it to every file.
3. **Price/terms solve:** given the 0% (or below-market) first mortgage, back-solve the
   affordable price: income × ceiling ratio = allowable PITI; subtract taxes, insurance,
   HOA; the remainder is available for principal (at 0% interest this equals price minus
   subsidy, which is why 0% structures stretch so far).
4. **Back-end ratio:** all debt service (PITI + auto, student, credit card minimums, court-
   ordered obligations) vs. gross income — keep at or below roughly 36-43%.
5. **Residual income check:** income minus PITI and known debt vs. a realistic household
   budget (food, utilities, transport, childcare, medical). This protects the family the
   ratios miss — a VA-style net-income test catches the 30%-of-gross household with five
   children and a car loan.
6. **Payment-shock check:** compare the new total monthly housing cost (include utilities
   if you can estimate them) against current housing cost. If the jump is severe — a
   common rule of thumb flags increases beyond roughly 1.5x — require budget counseling
   and a trial savings period (buyer "pays" the difference into savings for 3 months)
   before final approval.
7. **Cash contribution and reserves:** state the minimum buyer contribution (if any —
   many programs require $500-2,000) and whether gifts are allowed; verify the buyer can
   cover closing costs and has a small maintenance reserve.

**Structures to choose among** (often stacked):

- **0% first mortgage (Habitat classic).** Loan = house cost minus buyer contribution
  minus subsidy, amortized over 20-30 years at zero interest. Simple, deeply affordable,
  easy to explain to donors and buyers. Serviced in-house; watch the accounting (loan
  receivable discounting — hand that to the org's auditor).
- **Below-market rate first mortgage.** A modest rate (1-4%) preserves deeper subsidy for
  later families and eases portfolio economics; requires the same underwriting discipline.
- **Silent (soft) second mortgage.** 0%, non-amortizing, no monthly payment; recorded
  behind the first. Use it to close the gap between appraised value and program cost, or
  to buy the payment down. Two distinct flavors — decide explicitly which you mean:
  - **Forgivable:** forgives on a schedule (e.g., 20% per year over 5 years, or on the
    10th anniversary); balances the mission goal (stability) against subsidy recapture.
  - **Due-on-sale / shared-appreciation:** sits silently until resale, refinance, or
    transfer, then recoups principal plus a share of appreciation. This is the standard
    enforcement vehicle for program-level shared equity (below).
- **Grant + recapture.** Direct price subsidy with a recorded recapture note returning
  subsidy from resale proceeds.

Failure-and-remedy: a silent second with unclear forgiveness and on-sale terms clouds
every future title closing. Write the terms into a recorded instrument with an exact
payout formula — reviewed by counsel — not a letter.

Advisor note: when federal HOME funds subsidize the home, HUD's homeownership rules
(24 CFR Part 92) impose underwriting standards, value limits, and either a *resale* or
*recapture* provision with an affordability period that scales with the subsidy (roughly
5, 10, or 15 years by assistance tier). Map the structure to those rules before drafting.

## Underwriting Basics

Run every file through a written, repeatable standard — same documents, same math, same
decision logic:

- **Stability:** 2-year income and employment history; treat benefits, part-time, and
  self-employment income consistently across files (annualize, verify with tax returns).
- **Alternative credit:** when there's no score, build a credit profile from rental,
  utility, phone, insurance, and childcare payment histories (12 months typical). Judge
  recent conduct and explanation letters over ancient derogatory items.
- **Ratio tests:** front-end ceiling and back-end ceiling per policy, plus residual income
  and payment shock (worksheet above). The 0% structure makes the *tax/insurance* portion
  of PITI the most common shock for buyers who never escrowed — always estimate taxes and
  insurance with real local quotes, not national averages.
- **Decision:** one underwriter, a written file summary, and a second-review threshold
  (all denials and exceptions reviewed by a supervisor). Denials cite the specific
  criterion missed.

## Federal Compliance Touchpoints When the Nonprofit Lends

When your organization originates or services the mortgage (most affiliates do), you are
a creditor — not merely a grantmaker. Touchpoints that change behavior:

- **TILA / RESPA (TRID) disclosures.** The seller-financer exemptions from integrated
  disclosure rules generally cover natural persons, estates, and trusts — **not
  nonprofits** — so assume the full framework applies: a Loan Estimate within 3 business
  days of receiving an application, and the Closing Disclosure delivered at least 3
  business days before consummation. Zero-percent loans are still consumer credit
  secured by a dwelling.
- **Ability-to-repay and originator rules.** Federal loan-originator (SAFE Act / Reg Z)
  rules include exemptions used by bona fide nonprofit employees making low-interest
  loans, and ability-to-repay rules include charitable-creditor exemptions — but they
  hinge on loan terms and compensation limits. Verify with your state financial regulator
  and counsel which exemptions apply to your model; do not assume.
- **RESPA Section 8.** No kickbacks or unearned fees for settlement services; watch
  affiliated-arrangement disclosure rules if you require buyers to use in-house education,
  insurance placement, or closing services.
- **Servicing rules.** If your loans are covered mortgage loans, early-intervention
  expectations apply — live contact by roughly day 36 of delinquency and written notice
  with loss-mitigation info by day 45 — good operating practice regardless of coverage.
  Servicing-transfer notices apply if you move servicing out.
- **HOME funds.** Subsidy from HUD's HOME program brings the underwriting, value-limit,
  and resale/recapture provisions in 24 CFR Part 92 noted above.

All statutory citations and instrument drafting here go to counsel; this skill sets
business terms and flags the touchpoints.

## Homebuyer Education

Require it, fund it, and count sweat equity hours for it. Components to set in policy:

- **Pre-purchase course:** a minimum curriculum (budgeting, credit, the mortgage and note,
  taxes and insurance, maintenance and utilities, predatory-lending awareness), typically
  8+ classroom hours. If your organization is or partners with a **HUD-approved housing
  counseling agency**, remember counselors must be HUD-certified (post-2021 rule) for
  HUD-program participation.
- **One-on-one counseling:** individual budget review against the actual house payment,
  including an escrowed taxes-and-insurance walk-through.
- **Maintenance module:** hands-on or video series covering HVAC filters, water shutoffs,
  caulk/paint, GFCI outlets, and when to call a pro — this is default prevention as much
  as the counseling is.
- **Documentation:** certificate of completion required before closing; log it in the
  family file alongside sweat equity.

## Post-Purchase Support and Early-Default Counseling

**Deliverable: a post-purchase support plan.** First-year delinquency is the failure mode
this section exists to prevent. Structure the plan in four layers:

1. **Scheduled contact.** A named family-support staffer calls at 30 days, 6 months, and
   12 months post-closing; agenda: payment ease, escrow surprises, maintenance questions,
   referrals. Advisor note: this cadence is what distinguishes the plan from "they know
   our number."
2. **Ongoing supports.** Annual maintenance workshop; volunteer mentor or neighbor
   program; newsletter; a simple home-repair referral list (deep repair programs belong to
   `nonprofit-housing-repair-preservation` — build the referral, not the program).
3. **Delinquency playbook.** Written escalation: automated courtesy contact at 1 missed
   payment; live staff outreach immediately after; loss-mitigation application offered early
   (by day 45 at the latest); documented forbearance and modification options before
   referral to foreclosure counsel. Sequence: outreach → counsel → forbearance →
   modification → negative-equity options (short sale/deed-in-lieu) → foreclosure as last
   resort, every step documented in the servicing file. Nonprofit servicers win by
   forbearing early — the 0% loan gives you room.
4. **Foreclosure-prevention counseling partnership.** Formal referral relationship with a
   HUD-approved counseling agency for buyers in serious default, and to the state's
   HAF-type assistance programs or legal aid while they exist.

Failure-and-remedy: silent-second programs with no post-purchase contact discover
unauthorized refinance attempts at resale; annual outreach including "call us before you
refinance or list" protects both the family and the affordability mechanism.

## Shared-Equity Resale Formulas (Program Level)

When the program holds a shared-appreciation or recapture second, the **resale formula**
determines what the seller receives and what the program recaptures. Choose one, write it
into recorded instruments, and apply it mechanically:

- **Fixed-rate equity growth (common among Habitat affiliates).** Seller receives their
  initial equity plus a fixed annual appreciation credit (often roughly 1-2%) plus the
  documented cost of capital improvements. Predictable; insulates the buyer from market
  swings in both directions; simple to compute at closing.
- **Index-based.** Growth indexed to area AMI or CPI — keeps pace with what the *next*
  income-qualified family can afford, at the cost of market-tracking complexity.
- **Shared-appreciation split.** Sale proceeds split between seller and program by a stated
  percentage (25-50% to the program is common), typically pairing with a resale to the
  program at an affordable price.
- **Pairing requirements.** Every formula needs: the program's option or right of first
  refusal to purchase, a resale-to-income-qualified-buyer requirement (how HOME resale
  provisions work), a defined term for the affordability obligation, and the recorded
  second mortgage or covenant as the enforcement mechanism.

Balance test: the formula trades homeowner wealth-building against keeping the home
affordable for the next family. State the tradeoff in policy and pick deliberately —
fixed-growth favors predictability and stability; index/shared-appreciation favors
perpetual affordability. Stewardship of a perpetual portfolio (ground leases, CLT
membership, institutional stewardship) is `nonprofit-housing-community-ownership`.
Every formula requires counsel-drafted instruments and a resale price calculation
procedure the closing agent can execute without interpretation.

## Common Failure Modes

- **Ability-to-pay assumed because the rate is 0%.** Remedy: run full PITI with real tax
  and insurance quotes, plus payment shock — a 0% principal payment that ignores a 40%
  tax/insurance share still defaults.
- **Committee improvises criteria per file.** Remedy: rubric appendix, written decisions,
  recusal rules; every denial cites the criterion.
- **Sweat equity tracked on trust.** Remedy: signed logs, monthly family statements, a
  closing gate in the purchase agreement.
- **Silent second terms in a letter, not a recorded instrument.** Remedy: counsel-drafted
  recorded note with exact forgiveness/on-sale math.
- **"TRID doesn't apply to nonprofits."** Remedy: assume it does; verify exemptions with
  counsel before the first loan, not at the first complaint.
- **First contact with the buyer at day 60 of delinquency.** Remedy: the day-1/day-36/45
  cadence in the post-purchase plan.
- **Resale formula unenforceable at closing.** Remedy: rehearse the resale calculation and
  recorded-document package with a title company before the first family closes.
- **Income limits not refreshed annually.** Remedy: policy states the update month tied to
  HUD income-limit publication.
