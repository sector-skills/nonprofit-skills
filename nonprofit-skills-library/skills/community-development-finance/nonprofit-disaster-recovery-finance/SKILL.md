---
name: nonprofit-disaster-recovery-finance
description: "US disaster recovery and mitigation finance for nonprofits: the federal rebuild funding map (FEMA Public Assistance for private nonprofits, SBA disaster loans, HUD CDBG-DR/CDBG-MIT through state grantees), PN eligibility and registration checklists, CDBG-DR subrecipient readiness, the FEMA PA appeal path, and rebuild capital stacks layering insurance, SBA, CDBG-DR gap fill, philanthropy, and CDFI lending. Use when a user says 'our nonprofit building flooded — how do we pay to rebuild,' 'are we eligible for FEMA Public Assistance,' 'the state announced CDBG-DR funds — how do we get some,' 'should we take the SBA disaster loan,' 'FEMA denied our project — can we appeal,' or 'how do we stack the rebuild funding.' Not for international humanitarian response (use the intl-aid pack), CDFI lending programs generally (use nonprofit-cdfi-finance), community facilities financing outside a disaster (use nonprofit-community-facilities-finance), or risk registers and continuity planning (use nonprofit-risk-management)."
license: MIT
metadata:
  supervision: "review"
  supervision_note: "FEMA, SBA, and CDBG-DR filings carry strict deadlines, duplication-of-benefits rules, and audit exposure; appeals need counsel."
  last_reviewed: "2026-09-12"
  date_added: "2026-09-12"
  date_added_source: "git:184e56d49996189ac0083abc8dc85965945dd2d3"
---

# Nonprofit Disaster Recovery Finance

## When to Use This Skill

Use this skill when a US nonprofit is paying for disaster damage and mitigation: getting declared-disaster
money for a damaged facility, deciding whether to take an SBA disaster loan, chasing CDBG-DR or CDBG-MIT
funds through a state or local grantee, appealing a FEMA determination, or assembling the full capital
stack to rebuild. Trigger tasks include: "the flood destroyed our community center — what federal money
exists," "are we eligible for FEMA Public Assistance as a nonprofit," "FEMA says we're not an eligible
facility — what now," "the county got a CDBG-DR allocation and has an RFP for subrecipients," "SBA offered
us a loan at 3.625% — take it or wait for grants," "how do we avoid duplication of benefits," or "build
us a timeline from registration to closeout."

**Boundary:** This skill covers the US federal disaster-recovery funding stack for nonprofits.
International humanitarian and disaster response is the separate intl-aid pack. CDFI lending programs,
certification, and deal structures outside a disaster context are `nonprofit-cdfi-finance`. Financing
community facilities (health centers, child care, charter schools, food retail) with no declared disaster
in play is `nonprofit-community-facilities-finance`. Org-wide risk registers, insurance reviews, and
business continuity planning are `nonprofit-risk-management`. Day-to-day operating liquidity and lines of
credit are `nonprofit-reserves-cash-flow`; charitable fundraising campaigns for a rebuild are
`nonprofit-capital-campaigns`.

## What Changed, 2025-2026 — Verify Before You Advise

Anchor these; the landscape is moving (all "as of" September 2026):

- **FEMA Public Assistance policy**: the Public Assistance Program and Policy Guide (PAPPG), **Version 5.0
  Amended (FP 104-009-2), issued January 2025, effective for incidents declared on or after January 6,
  2025** — supersedes V4.1. Use V5 for any new declaration.
- **Cost share**: baseline federal share is **at least 75%** of eligible PA costs, with per-disaster
  increases to 90% or 100% still appearing in 2025 declaration amendments (e.g., 90% for some states, 100%
  for debris/emergency work windows of 120 days). The **Public Assistance Mitigation Cost Share Incentives
  Policy** (issued September 26, 2024, which offered up to an 85% federal share) was **rescinded retroactively
  for all disasters by FEMA's June 10, 2025 bulletin** — do not plan around mitigation-based cost-share bumps.
- **Project thresholds, FY2026**: minimum project cost **$4,100**; **Large Project threshold $1,093,800**
  (FY2025: $4,000 / $1,062,900). Thresholds are set each federal fiscal year by CPI and apply to incidents
  declared within that fiscal year — always pull the current table from FEMA's Per Capita Impact Indicator
  page.
- **BRIC is gone**: FEMA announced on **April 4, 2025** it was ending the Building Resilient Infrastructure
  and Communities pre-disaster mitigation program, returning roughly $882 million to Treasury. Post-disaster
  mitigation money now runs mainly through HMGP and CDBG-MIT.
- **FEMA Act of 2025 (H.R. 4669)** — proposed sliding 65-85% cost shares, estimate-based grants replacing
  reimbursement, IA reforms — was **ordered reported by committee in September 2025 but had not become law
  as of this review**. Check current status before relying on it; under current law PA remains a
  cost-reimbursement program.
- **CDBG-DR Universal Notice**: HUD published its **Universal Notice (FR-6489-N-01) on January 8, 2025**,
  a standing framework of waivers and alternative requirements that activates with each Allocation
  Announcement Notice (AAN); it was amended in **March 2025** to conform to executive orders. New CDBG-DR
  appropriations follow this structure.
- **SBA**: 2025-2026 SBA announcements quote nonprofit physical disaster loan rates **as low as 3.625%**
  (terms up to 30 years), and the loan cap is **$2 million** (combined physical + EIDL), with a 12-month
  deferral and no interest accrual in the first 12 months.

## The Federal Rebuild Funding Map

Work the map in this order — sequence matters because eligibility and duplication-of-benefits rules cascade:

| Program | What it funds for a nonprofit | Nonprofit access path |
|---|---|---|
| **FEMA PA, Categories A-B** | Debris removal, emergency protective measures | Direct applicant if critical PN, or via the legally responsible government |
| **FEMA PA, Categories C-G** | Repair/replace damaged facility to pre-disaster function + code upgrades | Direct applicant if critical PN; noncritical PNs only for costs SBA won't cover |
| **SBA physical disaster loan** | Repair/replace real estate, equipment, inventory, leaseholds; +20% mitigation add-on | Direct borrower, apply within 60 days of declaration |
| **SBA EIDL** | Operating capital for disaster-caused economic injury | Direct borrower, ~9-month window |
| **FEMA HMGP (Section 404)** | Post-disaster mitigation projects (75/25 cost share) | Subapplicant through the state/tribe; requires FEMA-approved local mitigation plan |
| **CDBG-DR** | Unmet recovery needs: rebuilds, buyouts, housing, economic revitalization, gap fill after insurance/SBA/FEMA | Through the state/local/tribal grantee's action plan — as subrecipient or direct beneficiary |
| **CDBG-MIT** | Mitigation: buyouts of flood-prone property, resilience infrastructure | Through the grantee; carries its own mitigation-definition rules |
| **FEMA IA programs** | Not for the org itself — nonprofits deliver services into IA (case management, crisis counseling, D-SNAP outreach) | State-administered service contracts/grants |
| **Philanthropy / CDFI rebuild lending** | Gap capital, bridge loans, forgivable loans, rebuild grants | Direct |

**Rule of thumb:** insurance first, FEMA PA and SBA in parallel immediately after declaration, HMGP and
CDBG-DR months later as the gap fill, philanthropy and CDFI capital as bridge and match. Every dollar of
federal disaster aid reduces eligibility for other federal aid for the same loss — track duplication of
benefits (DOB) from day one.

## FEMA Public Assistance for Private Nonprofits (PNPs)

### Eligibility — Who Qualifies

A private nonprofit (FEMA says "PNP") is an eligible PA applicant only if it:

1. Holds an **IRS ruling letter in effect on the declaration date** under **IRC 501(c), (d), or (e)**
   (or state documentation that it is a non-revenue-producing nonprofit under state law), and
2. **Owns or operates an eligible facility** providing an eligible service.

**Critical services** (eligible for emergency work and permanent work, no SBA-first requirement):
education, utilities, emergency services, medical services.

**Noncritical essential social services** (PAPPG V5 Table 4 — open to the general public unless noted):
community and senior centers, performing arts centers and educational enrichment, homeless shelters,
houses of worship and faith-based organizations, libraries, museums, zoos, food banks and food assistance
programs, alcohol and drug treatment, assisted living, custodial care and center-based childcare (both
eligible even if not open to the general public), day care for people with disabilities, low-income
housing, domestic abuse shelters, residential services for people with disabilities, health and safety
services including animal control, and religious instruction.

**Ineligible**: facilities established or primarily used for political activities, athletic, recreational,
or vocational activities, academic training, or conferences. Mixed-use facilities get prorated eligibility.

### The SBA-First Rule for Noncritical PNPs

For noncritical facilities, **FEMA only funds Permanent Work costs an SBA disaster loan will not cover**.
Apply to SBA first; if SBA denies the loan or authorizes an insufficient amount, FEMA fills the verified
gap. Taking the full SBA loan you can afford is often correct — it arrives years faster than CDBG-DR.

### Emergency Work (Categories A-B) for Nonprofits

Noncritical PNs are generally **not** reimbursed directly for emergency protective measures because those
are legally the state's/local government's responsibility — get deployed at the government's request and
funded through that government as the applicant, with certification. Exceptions where the PNP is funded
directly: medical/custodial facility patient evacuation costs, and urgent life-safety facility components
(e.g., a nonprofit hospital ER, water treatment). Debris removal is limited to debris on the eligible
facility's own property.

### Registration Checklist — First 30 Days After Declaration

1. **Confirm the declaration covers your county** and lists Public Assistance (and whether IA was
   authorized). **Completion condition:** declaration number, PA category designations, and cost share
   recorded in the disaster file.
2. **Submit a Request for Public Assistance (RPA) in FEMA's Grants Portal within 30 days of the date
   your area is designated** — this is a hard gate; late RPAs need a time-extension request with
   justification. **Completion condition:** RPA confirmation in Grants Portal.
3. **Assemble proof of PN status**: IRS ruling letter effective at declaration, articles/bylaws, evidence
   of facility ownership or a written legal responsibility to operate (leases count where they transfer
   restoration responsibility). **Completion condition:** eligibility documents uploaded to Grants Portal.
4. **Assign a Grants Portal owner and a single point of contact**; attend the applicant briefings the
   state (Recipient) runs after every declaration.
5. **Photograph all damage before cleanup; keep every invoice, contract, payroll record, and bank
   statement** — PA is cost-reimbursement for large projects; undocumented costs are denied costs.
6. **Notify insurers immediately and track all insurance advances** — FEMA reduces awards by insurance
   proceeds, and failure to obtain obtainable insurance is a stated eligibility problem in later awards.
7. **Document pre-disaster condition** (photos, maintenance records, appraisals) to support
   pre-disaster-design-and-function restoration scopes.
8. **Register with SAM.gov and maintain an active UEI** if not current — it will be required for
   grant-award steps downstream.

### Projects, Thresholds, and Cost Share

- Categories: **A** debris removal; **B** emergency protective measures; **C** roads and bridges;
  **D** water control; **E** buildings and equipment; **F** utilities; **G** parks and recreation.
- **Small Projects** (above the FY minimum — $4,100 for FY2026 — and below the Large Project threshold,
  $1,093,800 for FY2026) are paid on the estimate, with no adjustment to actuals — a Small Project that
  comes in under budget keeps the difference; over budget requires a re-scoping appeal.
- **Large Projects** are reimbursed against documented actual costs and carry the full documentation and
  procurement burden (2 CFR 200 procurement standards apply).
- **Cost share**: at least 75% federal / 25% non-federal by statute; some declarations amend to 90% or
  100% for defined categories and windows — read the declaration notice and amendments for your specific
  disaster, and budget the match (cash, volunteer time at FEMA rates, materials, or other non-federal
  sources). Note that HMGP and Other Needs Assistance stay at 75% even when PA is increased.
- **Improved projects and 406 mitigation**: repairs must restore pre-disaster design, function, and
  capacity in conformity with current codes; Section 406 hazard mitigation funding can be added to PA
  repair projects — cost-effectiveness case required.

### The PA Appeal Path

Two-tier administrative appeal under 44 CFR 206.206 — for disasters declared after January 1, 2022, both
tiers run on **60-day clocks**:

1. **First appeal** — in writing to the Recipient (state/tribe/territory) within **60 days** of FEMA's
   transmittal of the determination (eligibility finding, project worksheet version, or other decision),
   with the supporting documentation and citation to PAPPG/Stafford Act authority. The Recipient reviews
   and forwards to FEMA.
2. **Second appeal** — to the FEMA Regional Administrator within **60 days** of the first-appeal decision.
   No second appeal means the first-appeal decision is final agency action.

Use FEMA's public PA Appeals database — thousands of analyzed appeals show what arguments succeed (legal
responsibility, facility eligibility, documentation sufficiency). **Route appeals through counsel or an
experienced disaster-recovery consultant**: deadline misses are fatal and first-appeal records bind the
second appeal.

## SBA Disaster Loans for Nonprofits

As of 2025-2026 SBA announcements and sba.gov/disaster:

- **Business Physical Disaster Loans**: most private nonprofits may borrow up to **$2 million** to repair
  or replace disaster-damaged or destroyed real estate, machinery and equipment, fixtures, inventory, and
  leasehold improvements — losses not fully covered by insurance. No upgrades or expansion except
  code-required changes.
- **Rates and terms**: nonprofit physical loans quoted **as low as 3.625%** (recent SBA releases), up to
  **30 years**; when SBA determines credit is available elsewhere, rates run up to 8%. **First payment
  deferred and no interest accrual for 12 months.**
- **Mitigation add-on**: up to a **20% loan increase above verified real-estate damage** for mitigation
  — often the cheapest resilience capital a nonprofit can get.
- **EIDL**: nonprofits of any size suffering substantial economic injury may get working-capital EIDL;
  physical + EIDL combined cap is **$2 million**.
- **Deadlines**: physical damage applications due **60 days from the declaration date** (extensions
  happen — track them); EIDL ~**9 months**.
- **Collateral**: required to the extent available for physical loans over $50,000 in presidential
  declarations; SBA will not decline solely for lack of collateral.

Sequence rule: **apply to SBA regardless** — the application is free, the denial letter is exactly what a
noncritical PN needs to unlock FEMA PA permanent work, and a low-cost loan closes the gap years before
CDBG-DR money moves.

## FEMA Individual Assistance Interfaces

Nonprofits rarely receive IA funds for themselves, but they deliver IA-adjacent services and should know
the architecture (FEMA's March 22, 2024 IA reforms apply to disasters declared on or after that date —
Serious Needs Assistance, Displacement Assistance, flexible housing assistance, reduced documentation
burdens):

- **Disaster Case Management Program (DCMP)** — FEMA-funded, state-administered, nonprofit-delivered
  case management for disaster-caused unmet needs; watch the state's procurement after IA declarations.
- **Crisis Counseling Assistance and Training** — state grants, typically to nonprofit behavioral-health
  providers.
- **D-SNAP outreach and application assistance** — nonprofits often hold state SNAP agency subawards.
- **Voluntary Agency Liaisons (VALs) and donations/volunteer coordination** — the nonprofit sector's
  interface into FEMA; join the state VOAD/COAD to be at the table.
- Survivors have **60 days from an IA declaration** to register with FEMA; nonprofits doing recovery
  navigation should build intake around that window, and refer SBA loan refusals back to FEMA where IHP
  gap coverage may exist.

## CDBG-DR and CDBG-MIT for Nonprofits

### How the Money Flows

Congress appropriates CDBG-DR in a supplemental act → HUD issues an **Allocation Announcement Notice
(AAN)** to eligible states/localities/tribes → the grantee drafts an **Action Plan** (under the January
8, 2025 **Universal Notice**: due **within 90 days of the AAN**, with a **30-day public comment period**
and public hearings for larger allocations) → HUD approves → the grantee runs programs itself or through
**subrecipients**, and makes grants/loans to **direct beneficiaries**. Nonprofits participate as (1)
subrecipients administering programs, (2) direct beneficiaries receiving rebuild assistance, and (3)
service providers under procurement.

Action plan patterns to watch for (2025 vintage): housing repair/rebuild programs, voluntary buyouts,
infrastructure, and economic revitalization — each with published eligibility, national objective, and
beneficiary selection criteria. Comment on the action plan the moment the state posts it — programs get
shaped in the comment period, not after approval.

### National Objectives and Buyout/Acquisition Rules

Every CDBG-DR/MIT dollar must meet a HUD national objective: principally **benefit to low- and
moderate-income (LMI) persons** (housing LMH, area LMA, limited clientele LMC), **urgent need (UN)**, or
the buyout-specific **LMI Safe Housing Incentive (LMHI)**. Practical consequences:

- A rebuild grant to a nonprofit facility usually runs LMC (limited clientele — low-income clients) or
  urgent need; document client income data from day one.
- **Voluntary buyouts** acquire flood-prone property, demolish or relocate the structure, and deed-restrict
  the land to permanent open space — no future development. Nonprofits administering buyouts must follow
  URA (Uniform Relocation Act) notice rules; a buyout award to an LMI household meets LMB/LMHI.
- **CDBG-MIT** dropped CDBG-DR's tie-back-to-the-disaster requirement: activities must instead fit HUD's
  mitigation definition and address current and future risks. Most CDBG-MIT allocations were made from
  the 2018 appropriation; new MIT money is rare — most new dollars are CDBG-DR.

### Duplication of Benefits (DOB)

The Universal Notice's Appendix C overhauled DOB rules: total assistance for one loss from all sources
(insurance, FEMA, SBA, CDBG-DR, charity) cannot exceed the need. CDBG-DR is almost always the **last
dollar in** — grantees require documentation of all other assistance before awarding, and SBA loan
refusals or declines preserve CDBG-DR room. Keep a single DOB ledger per project from the day of loss.

### CDBG-DR Subrecipient Readiness Plan

Prepare this **before** an RFP drops — grantees award to administratively ready nonprofits:

1. **Entity standing**: active SAM/UEI, good standing, audited or professionally reviewed financials,
   no unresolved monitoring findings. **Completion condition:** pre-award self-audit passes.
2. **Capacity documentation**: written financial management system (2 CFR 200.30x), procurement policy
   compliant with 2 CFR 200.317-327, written conflict-of-interest policy, records retention (typically
   3-5 years or longer), and environmental review procedures awareness (CDBG-DR funds cannot be
   committed before HUD environmental review/clearance — never start construction early).
3. **Program design**: for the program you'd run (housing repair, case management, small-business
   assistance), draft intake, eligibility, national-objective certification, and beneficiary file
   templates. **Completion condition:** mock beneficiary file passes internal QA.
4. **Financial controls**: separate cost center per grant, drawdown discipline matching expenses,
   monthly reconciliation, and a standing single-audit (Uniform Guidance) readiness check — CDBG-DR
   subrecipients routinely trigger $1M single-audit thresholds.
5. **Relationships**: standing meetings with the grantee's disaster-recovery office and regional HUD
   Office of Disaster Recovery staff; track the grantee's action plan amendments and program guidelines.

## The Facility Rebuild Capital Stack

Build the stack as a sources-and-uses table with sequencing rules. Standard sources, in probable draw
order:

| Layer | Source | Timing | Watch-outs |
|---|---|---|---|
| 1 | Insurance proceeds (property, business interruption, flood via NFIP if mapped) | Weeks-months | RC vs ACV valuation; coinsurance; code-ordinance coverage; document offsets for DOB |
| 2 | FEMA PA Categories C-G | 1-3 years | 75%+ share; estimate vs actuals by size; codes/standards upgrades covered only if in codes; appeals |
| 3 | SBA physical disaster loan (incl. 20% mitigation add-on) | 6-18 months | 60-day application window; loan decision gates FEMA PA for noncritical PNs; collateral over $50k |
| 4 | CDBG-DR gap fill | 2-5 years | Last dollar in; DOB audit of all layers; national objective; environmental review before commitment |
| 5 | HMGP / Section 406 mitigation | 1-4 years | 75/25; jurisdiction must hold a FEMA-approved mitigation plan; state subapplication cycles |
| 6 | Philanthropic rebuild grants and campaigns | Continuous | Convert to match for non-federal share; donors move fast — use for bridge and match |
| 7 | CDFI rebuild lending (mission lenders with disaster products, e.g., post-wildfire and post-hurricane rebuild funds) | 6-24 months | Bridge against slow federal draws; forgivable components; CDFI program mechanics route to nonprofit-cdfi-finance |
| 8 | Reserves / internal bridge | Immediately | Board-approved draw policy; replenish from reimbursements |

**Uses**: site work, demolition, hard costs, soft costs (A/E, permits), code-required upgrades,
furniture/equipment, contingency (10%+), temporary facilities and relocation, and the non-federal match.

Stack rules: (1) no source may exceed its eligible share of a documented need; (2) every dollar of
insurance, FEMA, and SBA reduces CDBG-DR eligibility for the same loss; (3) sequence commitments so the
slowest, cheapest-when-fully-layered money (CDBG-DR) is applied last; (4) carry a bridge facility (CDFI
loan or line of credit) because PA is reimbursement — you front the cash; (5) rebuild mitigation in (406,
SBA 20%, HMGP) since insurers and FEMA increasingly price unmaintained risk.

## Disaster-Finance Calendar — Registration to Closeout

Anchor dates from declaration (DR) forward; actual dates vary by disaster — build this table per event:

- **Day 0**: Declaration. Record DR number, designated counties, IA/PA categories, cost share.
- **Days 1-14**: Insurance notice of claim; damage photos; emergency protective measures log; join
  VOAD/COAD calls; brief the board on the funding map.
- **≤ Day 30**: **RPA submitted in Grants Portal** (hard gate); SAM/UEI current; SBA application started
  (deadline is day 60 for physical loans).
- **≤ Day 60**: SBA physical loan application filed; survivor-registration referrals for clients; Grants
  Portal kick-off and recovery scoping meetings done.
- **Months 2-6**: Project worksheets scoped and written; small projects obligated; insurance settlements
  negotiated and documented; first HMGP subapplication window (state sets deadlines).
- **Months 3-9**: SBA loan decision — accept, decline, or accept partial (decline/insufficiency letters
  unlock FEMA PA permanent work for noncritical PNs); CDBG-DR AAN and state action-plan comment period
  (90 days post-AAN) — comment and apply.
- **Months 6-24**: CDBG-DR program guidelines published; subrecipient RFPs; environmental review
  clearance before any construction commitment; large-project construction and draws.
- **Any determination date + 60 days**: PA first-appeal deadline; **first-appeal decision + 60 days**:
  second appeal. Calendar these the day the determination arrives.
- **EIDL window (~9 months)**: economic-injury applications close.
- **Years 2-5**: CDBG-DR gap awards; HMGP projects closeout; large-project reconciliation to actuals.
- **Closeout**: all projects reconciled and closed, DOB ledger cleared, records retained (federal
  retention requirements), insurance maintained (failure to insure threatens future awards), audit
  responses complete.

## Failure Modes

- **Missing the 30-day RPA or 60-day SBA deadlines.** Remedy: calendar both on declaration day; request
  written extensions immediately if missed — silence forfeits.
- **Noncritical PN assumes FEMA will rebuild the facility.** Remedy: run the SBA-first path on day one;
  treat FEMA PA permanent work as the residual, CDBG-DR as the long-gap filler.
- **Cleaning up before documenting.** Remedy: photograph everything, keep debris and disposal records,
  log volunteer labor — pre-cleanup evidence is the claim.
- **Letting a 60-day appeal clock run out.** Remedy: on any adverse determination, same-day calendar the
  first-appeal deadline and open the FEMA appeals database for precedent; engage counsel.
- **Committing CDBG-DR funds before environmental clearance, or drawing before costs incurred.** Remedy:
  environmental review first; draw only on documented expenses; reconcile monthly.
- **Blowing the DOB ledger.** Remedy: one ledger per project tracking insurance, FEMA, SBA, charity,
  and CDBG-DR; update at every settlement; disclose everything to the grantee.
- **Skipping the action-plan comment period, then fighting the program rules.** Remedy: comment within
  the 30-day window; meet grantee staff during drafting.
- **Fronting large-project costs without a bridge.** Remedy: line up CDFI/philanthropic bridge capital
  sized to the expected reimbursement lag before construction starts.
- **Assuming BRIC still exists, or planning around the rescinded cost-share incentive policy.** Remedy:
  anchor mitigation plans to HMGP, CDBG-MIT, and Section 406 only; re-verify federal rules each
  declaration — this landscape moved repeatedly in 2025-2026.
- **Advisors vs. practitioners**: practitioners live in Grants Portal, insurance claims, and grantee
  monitoring visits; advisors should focus on the funding map briefing for the board, the capital-stack
  table, appeal strategy, and grantee negotiation — and should verify every program parameter against
  current FEMA/SBA/HUD sources before it reaches a client.
