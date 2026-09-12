---
name: nonprofit-housing-repair-preservation
description: "Designs and operates nonprofit home repair and preservation programs: critical home repair intake-to-completion workflow (roof, HVAC, plumbing, ramps), DOE Weatherization Assistance Program weatherization, CAPABLE-style aging-in-place modifications, EPA RRP lead-safe work, work-scope and cost estimating, contractor vs. volunteer labor decisions, income eligibility and affordability covenants, and preserving at-risk stock (expiring-use and NOAH). Use when a user says 'set up a critical home repair program,' 'our repair waitlist is a year long,' 'help us scope and estimate a roof replacement,' 'do we need lead certification for pre-1978 homes,' 'should volunteers or contractors do ramp builds,' or 'how do we keep NOAH units affordable.' Not for building new homes or development finance (nonprofit-housing-development-finance), volunteer build-day operations and crew site safety (nonprofit-housing-construction-volunteers), or general vendor/contractor management policy (nonprofit-vendor-facilities)."
license: MIT
supervision: review
supervision_note: "Construction scoping and lead-safety decisions carry occupant and worker safety consequences."
last_reviewed: 2026-09-12
---

# Nonprofit Home Repair & Housing Preservation

## When to Use This Skill

Use this skill when the organization repairs, modifies, or preserves homes people already live in, or works to keep existing affordable housing stock affordable. Typical triggers: designing or fixing a critical home repair program (roof, HVAC, plumbing, electrical, accessibility ramps), running an intake and waitlist, scoping and estimating repair work, deciding contractor vs. volunteer labor, building aging-in-place or weatherization programming, handling lead paint in pre-1978 homes, writing repair-program eligibility policy and affordability covenants, or responding to expiring-use and NOAH (Naturally Occurring Affordable Housing) loss.

**Boundary:** This is repair, modification, weatherization, and preservation of existing homes. Not new construction, site control, or development finance (`nonprofit-housing-development-finance`). Not volunteer build-day scheduling, crew leadership, or site safety management for volunteer crews (`nonprofit-housing-construction-volunteers` — though this skill tells you *which* work to hand them). Not organization-wide vendor selection or contractor management policy (`nonprofit-vendor-facilities` — this skill covers bid comparison for a specific repair job, not the procurement policy). Tenant-based rental assistance and nonprofit-owned rental property operations belong to `nonprofit-housing-affordable-rental-operations`; buyer-selection and sweat-equity for homeownership programs belong to `nonprofit-housing-homeownership-programs`.

## Program Architecture: Name the Program Type First

Repair programs fail most often because "home repair" is treated as one program. Separate into tiers, because funding rules, scopes, and risk differ:

1. **Critical home repair** — health/safety or habitability threats: failed roof, nonfunctioning furnace, active plumbing leaks, electrical hazards, structural rot. Highest cost per job, greatest liability, usually contractor labor. Modeled on Rebuilding Together and Habitat for Humanity "critical home repair."
2. **Home preservation / minor repair** — preventive and exterior work: gutters, porches, steps, grab bars, smoke/CO detectors, caulking, painting. Lower cost, volunteer-friendly.
3. **Weatherization** — building-envelope and efficiency work under the DOE Weatherization Assistance Program (WAP) framework or utility programs.
4. **Aging-in-place / accessibility modification** — ramps, roll-in showers, widening, grab bars, paired with occupational-therapy assessment (CAPABLE-style).
5. **Lead-healthy homes** — lead hazard control work, often layered onto any of the above in pre-1978 housing.
6. **Affordable-stock preservation** — organizational work to retain expiring-use and NOAH units, not physical repair per unit.

Funders fund tiers differently: HUD HOME and CDBG owner-occupied rehabilitation, DOE WAP, LIHEAP, USDA Section 504 rural repair grants/loans (very low income, age-restricted grants), state housing trust funds, and utility system-benefit funds each carry distinct rules. Match the tier to the funding rule before accepting applications.

## Deliverable 1: Intake-to-Completion Workflow

Numbered workflow with observable completion conditions. Scale staffing to volume; a program doing more than ~100 jobs a year needs a dedicated construction manager separate from intake staff.

1. **Outreach and application intake.** Publish eligibility criteria plainly (income limit, geography, homeowner status, occupancy requirement). Collect: owner-occupancy proof (deed, tax bill), household income documentation, photo evidence of the problem, and any code-enforcement or utility-shutoff notices. *Complete when:* every application has a completeness check logged and a unique ID in the tracking system.
2. **Eligibility determination.** Verify income against the program's limit (see eligibility section below) with third-party documentation. Confirm title/ownership and that property taxes and insurance are current or enrolled in a remedy — decide your policy on tax-delinquent homes in writing, not case by case. *Complete when:* an eligibility determination letter (approved/waitlisted/denied with reason and appeal path) is sent and filed.
3. **Triage and risk-ranked waitlist.** Rank by health/safety urgency (no heat in winter, active leak, no working plumbing, electrical hazard = emergency tier with a service-level target, e.g., 72-hour response, 30-day resolution), then habitability, then deferral candidates. Never run a first-in-first-out list for safety issues. *Complete when:* waitlist is sorted by tier with documented review dates, and applicants are told their tier.
4. **Home assessment/inspection.** Conduct a whole-home inspection by trained staff or a licensed inspector using a written standard (local property maintenance code, HQS/UPCS-style standards, or a program-defined deficiency list) — not just the reported problem, so you find the roof leak *and* the reason for it. Photograph everything; note pre-1978 construction for lead screening and visible asbestos suspects. *Complete when:* a signed inspection report with photos and a coded deficiency list is in the file.
5. **Scope development and estimating.** Convert deficiencies to a line-item work scope with quantities, materials spec, and cost estimate (next section). Order a lead test or EPA RRP determination where applicable before finalizing scope. *Complete when:* scope is approved by the construction manager and, if required, the funder.
6. **Funding packaging and owner agreement.** Confirm the funding source(s), secure owner signature on a repair agreement covering: what work will/won't be done, occupant responsibilities (access, moving belongings), grant/loan terms, any affordability covenant and lien terms, and a warranty/complaints clause. *Complete when:* agreement executed and any deed restriction or mortgage lien recorded (if program requires).
7. **Procurement and scheduling.** Solicit contractor bids for contractor-performed work (bid comparison sheet below); schedule volunteer crews for volunteer-appropriate work only. Verify licenses, insurance (GL and workers' comp certificates naming your org as additional insured), and EPA Lead-Safe Certified Firm status *before* dispatch. *Complete when:* contracts signed and a start date communicated to the occupant.
8. **Construction monitoring.** Inspect at defined hold points (e.g., roof decking before covering, rough plumbing/electrical before closing walls, ramp footings before pour). Never rely on the contractor's word for concealed work. Require permits and final municipal inspections where triggered. *Complete when:* each hold-point inspection is signed off with photos.
9. **Final inspection and punch list.** Walk the job with the occupant, document deficiencies on a punch list, and hold final payment until the punch list closes and all permits have final sign-off. *Complete when:* signed completion certificate, final photos, and paid invoices are in the file.
10. **Warranty and follow-up.** Track warranty periods (workmanship warranty of at least 12 months is a standard program requirement), log occupant callbacks, and schedule a 6–12 month quality follow-up. *Complete when:* warranty terms delivered in writing to the owner and callbacks logged against the contractor's record.

Advisors: when auditing a struggling repair program, the diagnosis is almost always in steps 3, 5, and 9 — unranked waitlists, scopes written before inspections, and final payments released before punch-list closure.

## Deliverable 2: Work-Scope Template

Every scope should be a line-item document the contractor can bid from without a site visit beyond one walk-through. Template fields:

- **Header:** job ID, address, owner, funding source(s), pre-1978 flag and RRP determination, permit requirements.
- **Deficiency-to-scope crosswalk:** each deficiency from the inspection maps to one or more scope line items with its code (safety/habitability/systems/envelope) — this is what proves to funders that federal dollars addressed a qualifying need.
- **Line items:** location (e.g., "rear elevation roof"), unit of measure and quantity, specification (e.g., "25-yr architectural shingles, ice-and-water shield at eaves, replace 2 rafters at chimney"), and estimated cost. Spec the *outcome and standard*, not the brand, unless the funder does.
- **Exclusions:** what the program will not do (stated explicitly to the owner — e.g., "kitchen cabinets, flooring beyond the work area, tree removal") to prevent scope-creep disputes.
- **Contingency:** carry 10–15% (15–20% on older homes) for concealed conditions; state who approves contingency draws.
- **Allowance items:** for unknowns (e.g., "$X per square for deck sheathing replacement beyond 3 squares").
- **Priority codes:** P1 life-safety/critical system, P2 preventing further deterioration, P3 comfort/efficiency/access. If funds run short, cut P3 before P2 — and document the deferral in writing to the owner.

Estimating: use a published cost database (RSMeans, Craftsman/National Repair & Remodeling Estimator) adjusted to your region's index, then sanity-check against your own completed-job actuals, which you should track per unit (cost per roof square, per ramp, per HVAC replacement). A database number more than ~20% off your actuals means your spec or your market has changed — reconcile before budgeting a pipeline.

## Deliverable 3: Eligibility Policy

Write the policy before the first applicant, covering each element:

- **Income limit and definition.** State the limit as a percentage of Area Median Income (HUD AMI, household-size adjusted) — commonly 50%, 60%, or 80% AMI for repair programs — or as a percentage of federal poverty level. State *whose* income counts (all adults in the household), the *lookback period* (e.g., prior 30/60/90 days or annualized), and permitted forms of verification (pay stubs, benefit award letters, tax returns, third-party employer verification). DOE WAP uses its own income limits (households at or below 200% of poverty or a state-set standard, with categorical eligibility via LIHEAP or SSI in many states); if you braid WAP and HOME funds, each dollar must meet its own program's test — build a dual-certification worksheet rather than one-size eligibility.
- **Asset and property tests.** Owner-occupied (typically principal residence), single-family or small multifamily where the owner occupies a unit; value caps or mobile-home policies; whether investor-owned rentals are excluded (most federally funded owner-occupied rehab requires owner-occupancy).
- **Geography and priority populations.** Service area, plus lawful priorities (elderly, disabled, veterans, households with children under 6 for lead programs). Prioritization by protected class is prohibited; prioritization by need-based, non-protected criteria is not — route fair-housing questions to `nonprofit-housing-fair-housing`.
- **Affordability covenants and recapture.** Grant dollars secured by the home require an instrument: forgivable loan (forgiveness period often 5–15 years, pro-rata or full recapture on sale/transfer/rental), deferred-payment lien, or resale restriction. If HOME funds are involved, HOME sets tiered affordability/resale periods by assistance amount (5/10/15 years). Record the instrument at closing; an unrecorded covenant is unenforceable when the home sells. Decide and document treatment of: early death of owner, transfer to heirs, conversion to rental, refinance.
- **Loan vs. grant.** Zero-interest deferred loans preserve recycling capital and deter quick flips; grants are simpler but spend down. Many programs use grants under a threshold and deferred loans above it.
- **Denials and appeals.** Written denial reasons and an appeal path, plus a deferral policy for homes where repair is infeasible (severe structural failure, active condemnation) — deferral is a program decision that needs criteria, not an ad hoc judgment.

## Deliverable 4: Safety and Inspection Checklist

Two distinct checklists — job safety (worker/occupant) and housing condition (the inspection that drives scope).

**Job-site safety gates (every job, both contractor and volunteer):**
- Licenses, insurance certificates, and (pre-1978 work disturbing paint) EPA Lead-Safe Certified Firm and certified renovator verified in the file before dispatch.
- Occupant protection plan: work-area separation/containment, occupant relocation decision for hazards like major lead disturbance or fumigation, daily cleanup.
- Utilities: lockout/tagout for electrical, gas shutoff verification before plumbing/HVAC, water shutoff for supply work.
- Fall protection above 6 feet; ladder inspection; scaffold tags for masonry/roofing.
- Asbestos suspect materials (pre-1980: pipe wrap, popcorn ceilings, 9x9 floor tile) tested before disturbance — do not demo suspected asbestos.
- Permits pulled and posted; required municipal inspections scheduled at hold points.
- OSHA hazard-communication sheets on site; first aid and emergency contact posted.
- Weather cutoffs (heat, wind for roofing, lightning) and a no-unaccompanied-minors rule.

**Housing condition inspection domains (write scope from these):** roof and envelope; structure (foundation, framing, porches, stairs, railings); electrical (service capacity, GFCI, knob-and-tube or aluminum branch wiring flags); plumbing (supply leaks, drainage, water heater TPR valve and venting); HVAC (heat source operability, combustion safety/backdrafting, CO alarms); health hazards (lead, mold/moisture sources, pest entry, radon where prevalent); accessibility barriers (entry steps, door widths, bath transfer); fire safety (smoke/CO detectors, egress windows, egress path). Photograph and code every deficiency; a coded deficiency list is what makes the scope auditable and comparable across homes.

## Deliverable 5: Contractor Bid Comparison Sheet

Solicit at least three bids on contractor-performed jobs above your threshold. Compare on a fixed set of columns:

| Column | What it captures |
|---|---|
| Base bid | Total for the scope as written, apples-to-apples |
| Scope conformance | Line-by-line: matches spec / substitution proposed / omitted |
| Allowances & unit prices | Stated $/unit for anticipated extras (sheathing squares, rafter count) |
| Exclusions & qualifiers | Anything the bid carves out — the most important column |
| Schedule | Start availability and duration |
| License, insurance, RRP cert | Number, expiration, additional-insured status, lead cert if pre-1978 |
| Warranty | Workmanship warranty term and what it covers |
| References / track record | Prior jobs for your program: on-time %, callback rate, punch-list disputes |
| Payment terms | Draw schedule; never more than a small deposit with balance on completion |

Disqualify non-conforming bids or normalize them before comparing. Award to the lowest *conforming, responsible* bid — and document why, since federal funds require documented procurement. The most expensive bid is often the one that read the scope; the cheapest is often the one that didn't.

## Contractor vs. Volunteer Labor Decision

Decide per line item, not per job:

- **Licensed/certified contractor required:** roofing, electrical, plumbing, HVAC, gas lines, structural framing changes, lead hazard control, asbestos abatement, anything requiring a permit trade license — regardless of volunteer skill, insurance and warranty requirements make this non-negotiable in most programs. This is where you hire; this skill's bid sheet governs.
- **Contractor-preferred:** excavation/footings for ramps (grade and drainage failures are the #1 ramp callback), exterior carpentry at height.
- **Volunteer-appropriate with a skilled leader:** ramp and deck builds under a skilled crew leader (route build-day planning and crew safety to `nonprofit-housing-construction-volunteers`), painting and landscaping (pre-1978 homes: RRP applies to volunteers too if disturbing >6 sq ft interior / >20 sq ft exterior lead paint — volunteer status is not an exemption), caulking, gutter cleaning, insulation air-sealing under WAP protocols, grab-bar and handrail installs with OT-specified placement.
- **Hybrid pattern:** contractor does rough and technical work; volunteers finish (paint, trim, cleanup) — the standard Habitat-style model.

Blended-cost rule: compare fully loaded costs. Volunteer labor isn't free (crew leadership, tools, materials waste rate, supervision time) and contractor labor carries warranty value. Track cost-per-job by labor model and let data, not culture, set the mix.

## Weatherization (DOE WAP Framework)

- **Whole-home energy audit first.** WAP requires a priority-based audit (NEAT for single-family) to rank measures by savings-to-investment ratio (SIR ≥ 1 required for most energy measures); do not install measures the audit doesn't justify with federal WAP dollars.
- **Typical measure stack:** air sealing, attic insulation, heating-system repair/replacement (where allowed), duct sealing, ventilation (ASHRAE-based, to avoid creating combustion backdrafting), plus limited related repairs that enable the measures.
- **Health-and-safety funds are separate** from energy-measure funds in WAP: combustion safety testing, CO/smoke detectors, and some incidental repairs are health-and-safety line items with their own caps — keep the accounting separate or you'll fail monitoring.
- **Per-unit average cost limits** apply to WAP jobs; a job projected to exceed the limit needs supervisor approval and justification.
- **Common braids:** WAP + utility programs + your critical-repair dollars — sequence so the roof repair happens *before* the attic insulation, or you're insulating a leaking envelope. One integrated scope across funders, separate accounting per funder.
- **Deferral protocol:** homes with unresolvable moisture, combustion, or structural problems are deferred in writing with referral — never insulate over an unsolved moisture problem.

## Aging-in-Place and Accessibility Modification (CAPABLE-Style)

- **Assessment before scope.** The evidence-based model is Johns Hopkins' CAPABLE (Community Aging in Place — Advancing Better Living for Elders): a short, time-limited series of nurse visits addressing self-care barriers, occupational-therapy visits that produce a prioritized modification and equipment list tied to the person's actual functional limitations, and a handyworker visit sequence that executes it. Copy the structure: OT assessment → specified modification list → execution — don't build ramps from a phone request.
- **High-value, low-cost tier first:** grab bars, handheld showerheads, tub benches, raised toilets, lever handles, remove throw rugs, improve lighting — thousands of dollars of fall-risk reduction per home at minimal cost.
- **Ramp specifics:** rise/run at 1:12 maximum, 36-inch clear width, landings at top and door side, edge protection, max 30-inch rise per run; threshold ramps for smaller steps. Build to code standard even where permits aren't required — a program-built ramp is a foreseeable-harm liability item.
- **Pair modification with the person:** a modification the occupant won't use (a ramp on the wrong entrance, a grab bar at the wrong height) is a failed outcome; OT-specified placement is what makes the CAPABLE-style approach work.
- **Measure function, not units:** track falls, self-reported difficulty with activities of daily living, and ability to age in place, not just ramps built.

## Lead-Safe Work (EPA RRP Context)

- **Trigger:** the EPA Renovation, Repair and Painting (RRP) Rule under the Toxic Substances Control Act applies to work disturbing more than 6 sq ft of painted surface interior or 20 sq ft exterior in pre-1978 housing (and any window replacement): your organization must be an EPA Lead-Safe Certified *Firm*, the job must have a certified *renovator*, lead-safe work practices and containment are mandatory, and occupants get the "Renovate Right" pamphlet with documented delivery.
- **HUD's Lead Safe Housing Rule** (24 CFR Part 35) adds requirements when *federal* dollars touch the unit: visual assessments for pre-1978, and for larger rehabilitation, risk assessment and lead hazard reduction with clearance testing. Clearance dust-wipe testing by a certified technician — not a visual check — is the standard of done.
- **Practical program rules:** screen every intake for year built; when pre-1978, assume lead or test before disturbing; budget RRP compliance (containment, cleaning verification, and clearance) into every pre-1978 estimate — commonly adding meaningful cost per job; never let volunteers disturb suspected lead paint without certified supervision.
- **Aging + lead overlap:** pre-1950 homes and children under 6 make lead hazard control a priority population criterion for HUD lead grant programs.

## Preserving At-Risk Affordable Stock (Expiring-Use / NOAH)

Repair programs naturally lead into preservation strategy; know when to escalate:

- **Expiring-use federally assisted housing:** older HUD-subsidized properties (project-based Section 8 contracts, Section 236, BMIR) reach contract or mortgage events where owners can exit affordability. Signals: subsidy contract expiration dates, notice of prepayment or opt-out, sale listings. Responses (resident notification triggers, purchase efforts, state intervention) run through development finance — route transactions to `nonprofit-housing-development-finance`, but the *monitoring* (a watchlist of expiration dates in your service area) is preservation-program work.
- **NOAH:** unsubsidized, market-rate stock affordable only because of age/condition/location. The repair lens: a large repair burden (roof, systems) is often the trigger for a small landlord to sell or for rents to jump. Nonprofit responses include acquisition/rehab, repair-grant or low-interest-loan programs conditioned on rent or affordability commitments, and code-enforcement partnerships that pair citations with repair resources. Rent covenant terms and acquisition deals belong with `nonprofit-housing-development-finance` and `nonprofit-housing-affordable-rental-operations`.
- **Owner-occupied preservation is preservation:** keeping a low-income owner in a paid-off home is often the cheapest affordability intervention in a market — frame repair programs in housing-policy terms (cost per unit preserved vs. cost per unit built) when advocating for funding.
- **Data to maintain:** count of income-restricted units and expiration dates by year (from HUD and state agency lists), NOAH segment estimates, and your repair-program deferral/loss data (homes lost to disrepair, tax sale, or condemnation).

## Common Failure Modes

- **First-in-first-out waitlist** with a no-heat household behind ten gutter jobs — triage by urgency tier or accept the safety exposure.
- **Scoping from the application instead of the inspection** — the reported "roof leak" is a failed flashing plus rotted decking plus a bathroom vent problem; scope from the coded inspection, always.
- **Pre-1978 lead screening skipped** until demo day — retrofitting containment mid-job, or worse, contaminating the home and the program's federal funding.
- **Underestimated scopes / no contingency** — concealed rot, outdated panels, and asbestos suspects are the norm in the housing stock that qualifies; a 0% contingency budget guarantees mid-job stalls.
- **Unrecorded covenants** — recapture promises that evaporate at the first title transfer; the lien must be recorded to exist.
- **Braided funds with single-fund accounting** — HOME, CDBG, WAP, and LIHEAP each monitor their own dollars; mixed books fail every audit.
- **Volunteers on licensed trades or lead disturbance** — well-intentioned, uninsured, and a liability and compliance breach.
- **Final payment on substantial completion, not punch-list closure** — the punch list is leverage; releasing it early removes the only leverage you have.
- **No warranty/callback tracking** — repeat business awarded to contractors with hidden callback rates.
- **Insulating over moisture** — weatherization that seals in a roof or crawlspace moisture problem creates mold and condemnation risk.
- **Ramps built from phone specs** — wrong entrance, wrong rise, unused ramp; OT assessment fixes this.

## Practitioner vs. Advisor Framing

- **As the practitioner** (repair program staff): live in the workflow — triage tiers, inspection-to-scope discipline, and the bid sheet are your daily tools; track cost-per-job actuals per labor model and per measure so estimating and procurement improve every quarter.
- **As the advisor/consultant** (assessing or designing a program for a client): diagnose against the six program tiers and the ten workflow steps; the highest-leverage findings are usually missing eligibility policy documents, unrecorded covenants, lead screening gaps, and unranked waitlists. Be explicit about which fixes are program-design work (this skill) versus capital transactions or new development (`nonprofit-housing-development-finance`), and route fair-housing questions in eligibility design to `nonprofit-housing-fair-housing`.
