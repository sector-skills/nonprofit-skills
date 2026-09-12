---
name: nonprofit-community-facilities-finance
description: "Designs capital stacks for nonprofit community facilities — health centers (FQHCs), child care centers, charter schools, grocery and healthy-food retail, community centers, workforce training space — layering USDA Community Facilities loans and grants, tax-exempt 501(c)(3) conduit bonds (bank-qualified or public), NMTC equity, CDFI debt, government grants, and philanthropic gap capital. Use when a user says 'how do we finance our new health center / child care building / charter school facility,' 'are we eligible for USDA Community Facilities,' 'should we do a bank-qualified bond,' 'help us put together the capital stack,' or 'what funders pay for this kind of facility.' Not for NMTC deal structuring (use nonprofit-nmtc-deals), CDFI lending and awards (use nonprofit-cdfi-finance), housing projects (use nonprofit-housing-development-finance), donor-side capital campaigns (use nonprofit-capital-campaigns), or disaster-rebuild financing (use nonprofit-disaster-recovery-finance)."
license: MIT
supervision: review
supervision_note: "Bond documents, USDA applications, and intercreditor agreements need bond counsel and financial advisor review before execution or filing."
last_reviewed: 2026-09-12
---

# Nonprofit Community Facilities Finance

## When to Use This Skill

Use this skill to plan, structure, or troubleshoot the financing of a brick-and-mortar community facility a nonprofit will own, lease, or develop: FQHC health centers and clinics, child care centers, charter schools, food retail and grocery, community centers, and workforce training space. Trigger tasks include: "how do we finance a new health center building," "our child care center needs a bigger building — who funds that," "are we eligible for USDA Community Facilities money," "should we issue a bond or get a bank loan," "help us put together the capital stack for our project," or "the bank will only lend 60% of cost — how do we fill the gap."

**Boundary:** this skill covers the *facility-side* capital stack. It does not cover NMTC deal mechanics (QEIs, leverage loans, allocation applications, 7-year compliance — use `nonprofit-nmtc-deals`), CDFI certification, award programs, and lending products (use `nonprofit-cdfi-finance`), housing projects and LIHTC/HOME stacks (use `nonprofit-housing-development-finance`), donor-side campaign strategy and gift solicitations (use `nonprofit-capital-campaigns`), or post-disaster rebuilding funds like CDBG-DR and FEMA Public Assistance (use `nonprofit-disaster-recovery-finance`). Operating lines of credit for cash-timing gaps route to `nonprofit-reserves-cash-flow`.

## The Facility Landscape: How Funder Mix Differs by Type

The single biggest predictor of what a project can raise is facility type, because each type carries a distinct revenue base, federal program fit, and lender ecosystem. Build the funder-mix comparison below before naming any funder.

| Facility type | Revenue that repays debt | Anchor public programs | Typical stack shape |
|---|---|---|---|
| FQHC / community health center | Section 330 grant revenue + Medicaid/Medicare/mixed-payer PPS reimbursement — stable, underwritable | USDA CF (rural); occasional HRSA one-time capital grants; state health facility authority bonds | Conduit bond or bank loan as senior debt; NMTC equity (health centers in eligible tracts are common NMTC users); CDFI/health-center specialty lenders; philanthropy |
| Child care center | Tuition + state child care subsidy — thin margins, low sticker prices | USDA CF (rural); state child care facility funds; Head Start/Early Head Start co-location; CDBG (locally, if national objective met) | Grant-heavy: government and foundation grants plus subordinated CDFI debt (child care specialists), small bank first mortgage; ARPA-era stabilization funds have lapsed — do not assume them |
| Charter school | Per-pupil revenue from enrollment — needs enrollment covenant | State per-pupil facility allotments (only some states); state charter revolving funds and credit enhancement; some states give charters access to school bond guarantees | Conduit bonds through charter/bond authorities, charter specialty lenders, NMTC equity; little grant capital — debt-heavy stack priced on enrollment risk |
| Food retail / grocery | Store sales — thin-margin commercial revenue | Healthy Food Financing Initiative (HFFI, USDA/Reinvestment Fund); state healthy food funds; USDA CF for rural food hubs, food banks, pantries | NMTC equity + CDFI retail lenders + HFFI grants/TA + subordinate philanthropic capital; the hardest type to debt-finance on projections alone |
| Community center / multipurpose | Program fees, memberships, rentals — rarely covers debt service | USDA CF (rural); CDBG; city capital budget partnerships | Campaign gifts (route to `nonprofit-capital-campaigns`) + government grants + modest bank debt; often only financeable with a public co-owner |
| Workforce training space | Grants and contracts (WIOA-type funds are operating, not capital) | State economic development and workforce capital grants; employer contributions; community college partnerships | Philanthropy + state grants + NMTC (if job-creation case in eligible tract); debt sized to a fraction of facility cost |

When advising: name the 2–3 anchor funders for the facility type first, then size debt against the revenue base, then fill the residual gap with philanthropic and grant capital — never the reverse order.

## USDA Community Facilities (CF) Programs

USDA Rural Development CF is the most accessible federal facility capital for rural nonprofits. Three instruments with different geography:

- **Direct loans and grants:** eligible to public bodies, community-based nonprofits, and federally recognized tribes for *essential* community facilities (health care, child care, schools, food banks/hubs, community centers — not commercial or business undertakings) in areas of **20,000 or fewer residents** (latest decennial census) that serve the rural area where located. Direct loan rates are set quarterly by tier based on service-area median household income (MHI) and population: for the period **April 1 – September 30, 2026, poverty rate 4.500%, intermediate 4.625%, market 4.750%** (verify the current quarter at rd.usda.gov before quoting — rates reset October 1, 2026). Fixed for the loan's life, no prepayment penalty, terms up to 40 years or the facility's useful life.
- **Grants:** on a graduated scale of **15%–75% of eligible project cost**, tied to population and MHI: 75% max (population ≤5,000 and MHI below the higher of the poverty line or 60% of state nonmetro MHI); 55% (≤12,000, 70%); 35% (≤20,000, 80%); 15% (≤20,000, 90%). Applications are generally considered as loan-only first, with grant amounts awarded competitively as funds allow — apply for loan-plus-grant, assume a loan-only base case. Priority points favor communities of 5,500 or fewer and MHI below 80% of the state nonmetro MHI.
- **Guaranteed loans:** a commercial lender (bank, Farm Credit, credit union, state bond bank) lends to the nonprofit; USDA guarantees up to **90% by statute but loans approved in FY2026 carry an 80% guarantee** (percentage is published annually in the Federal Register — verify the current fiscal year's figure). Eligible areas: **50,000 or fewer residents**, not in an urbanized area contiguous to a larger city. Loans up to $100 million, terms to 40 years, rates negotiated with the lender. Fees (as of 2026): initial guarantee fee 1.25% of the guaranteed amount, annual retention fee 0.5% of outstanding principal, and 0.5% for issuing the note guarantee before construction. The lender must certify the loan would not be made without the guarantee, and the borrower must be unable to finance the project from its own resources or commercial credit at reasonable rates and terms. Guaranteed program funds are reserved for smaller places first (100% of the first $200 million for communities ≤20,000, 50% of the next $200 million, 25% above $400 million).

### USDA CF application decision framework

1. **Run the geography test first.** Pull the project address in USDA's online eligibility map. If the service area is ≤20,000, direct loan/grant is available; ≤50,000 and non-contiguous-rural, guarantee only; above 50,000, route to bonds/NMTC/CDFI. *Completion condition: a written eligibility determination (map screenshot + population citation) in the project file.*
2. **Test the "essential facility" fit.** Nonprofit applicant, facility provides an essential community service, no inherently commercial use. A nonprofit-run grocery or business incubator needs the essential-service case documented (food access, underserved area) — flag marginal cases to the state CF office before applying.
3. **Choose the instrument:** direct loan when you qualify (lowest fixed rates, long amortization); guaranteed loan when you have a bank relationship, need speed, or the loan exceeds direct-program capacity; grant only as a component — assume a loan-first award.
4. **Document credit-elsewhere:** obtain a bank turndown or terms quote showing commercial credit is unavailable or unreasonably priced, where required.
5. **Assemble readiness package:** economic feasibility study, preliminary architectural report, site control, environmental review, audited financials, operating pro forma with debt service coverage (see readiness checklist below). USDA cannot obligate funds before environmental review clears — start it early.
6. **File the pre-application with the state Rural Development office** early in the federal fiscal year (starting October 1); grant funding is appropriated annually, so late-cycle applications wait for the next year. *Completion condition: pre-application acknowledged and a named CF loan specialist assigned.*

## Tax-Exempt Bond Issuance Basics for Nonprofit Facilities

A 501(c)(3) cannot issue tax-exempt bonds in its own name. The structure is always **conduit**: a governmental issuer (state health facility or educational/cultural facilities authority, local industrial development authority, or state bond bank) issues bonds and lends the proceeds to the nonprofit under a loan agreement, with debt service secured by a mortgage on the facility and the nonprofit's revenues. The issuer lends its tax exemption, not its credit — the bonds are repaid solely from the nonprofit's revenue. Bond counsel (a specialist firm) documents the deal; the nonprofit also engages a municipal advisor. All documents go to counsel and advisor review before execution.

Two issuance paths, chosen by size:

- **Bank-qualified (small issuer) placement, roughly ≤$10 million:** if the issuer reasonably anticipates no more than **$10 million of tax-exempt bonds in the calendar year** (tested at the conduit-borrower level for 501(c)(3) deals — a single authority's issuance for multiple nonprofits doesn't blow one borrower's limit), the bonds can be designated bank-qualified and sold directly to a local bank, which may deduct 80% of its carrying costs. This bypasses the underwriting, rating, and continuing-disclosure apparatus and typically saves 25–40 basis points. The **$10 million limit is unchanged since 1986**; proposals to raise it (e.g., to $30 million) have repeatedly been introduced but **were not enacted as of September 2026** — do not assume a higher limit.
- **Publicly offered (or larger privately placed) issuance:** above the small-issuer limit, bonds are sold through an underwriter (rated and marketed) or placed with an institutional buyer. The nonprofit bears: a public hearing with 14-day notice (TEFRA approval) *before* issuance, ongoing arbitrage rebate compliance, annual continuing-disclosure filings on EMMA for the life of the bonds, and the 501(c)(3)-bond use rules — no more than 5% of proceeds for non-qualifying uses (including costs of issuance) and a **$150 million cap on non-hospital 501(c)(3) bonds outstanding per organization** (hospitals are exempt from the cap).

2025 federal tax law (the One Big Beautiful Bill Act, enacted July 4, 2025) **preserved the tax exemption for municipal bonds including qualified 501(c)(3) and private activity bonds and made no changes to the bank-qualified rules** — but it did make the New Markets Tax Credit permanent at $5 billion in annual allocation (relevant to layering, below), permanently lowered the private-activity-bond threshold for 4% LIHTC deals to 25% of basis, and raised LIHTC allocations 12% starting 2026 (housing implications route to `nonprofit-housing-development-finance`). Re-verify all of this if asked after September 2026.

## Layering One Capital Stack

Large facility gaps (typically $2M–$30M) are filled by stacking instruments with different costs and risk positions. Standard order, senior to subordinate:

1. **Senior debt** — conduit bond or bank first mortgage, sized to a debt service coverage ratio (DSCR) the facility's pro forma actually supports (lenders typically want ≥1.25x stabilized; child care and retail often can't get there without subordination).
2. **USDA CF direct or guaranteed loan** — can be senior or pari passu; a guaranteed loan often *is* the senior bank debt.
3. **NMTC equity** — since OBBBA (July 2025) the program is permanent with $5 billion in annual allocation, so allocation is no longer a reauthorization risk, but CDE allocatee relationships still take 6–12 months of lead time — start CDE conversations when the project budget is ±20% reliable, not at contract signing. NMTC equity can fill roughly 20–30% of a stack. Structure, QEI, and 7-year compliance mechanics route to `nonprofit-nmtc-deals`.
4. **CDFI subordinated debt** — patient second-position term debt; child care, health center, charter, and food-retail CDFI specialists each underwrite differently. Products and lender selection route to `nonprofit-cdfi-finance`.
5. **Government grants** — USDA CF grant (rural), state facility funds, city CDBG or capital budget, HFFI for food projects (HFFI's FARE Fund 2026 cycle offers planning/implementation grants of $20,000–$250,000 and technical assistance up to $75,000, with inquiries due July 31 and applications October 30, 2026; the 2026 HFFI Partnerships round — $20 million for $200,000–$3 million partnership awards — closed September 18, 2026; verify current rounds at investinginfood.com).
6. **Philanthropic gap capital** — foundation capital grants, program-related investments (PRIs), and campaign gifts. Donor-side strategy routes to `nonprofit-capital-campaigns`; here they function as the last-in, residual gap filler.

Layering rules that change outcomes:

- **Sequencing:** get soft commitments (grant awards, NMTC term sheet, CDFI letter of intent) before finalizing senior debt terms — lenders price better when the gap is demonstrably covered.
- **Sources must equal uses** with a construction contingency (10% is standard for rehab, 5% new construction) inside the uses, and financing costs (issuance costs, guarantee fees, NMTC structuring fees) on the uses side, not buried.
- **Grants reimburse or pay on milestones; they do not fund closing.** Budget a bridge (grant-anticipation loan or campaign-pledge line) for the gap between construction draw schedule and grant/pledge receipt — instrument selection for operating cash gaps routes to `nonprofit-reserves-cash-flow`.
- **Intercreditor terms:** every layer below senior needs a subordination and standstill agreement; federal grants may attach conditions that survive on title — surface these in the closing checklist before the senior lender's counsel finds them.
- **Pro rata funding order at closing** must be written into the financing agreements (grants typically fund last or on reimbursement, NMTC equity at QEI closing, debt at first construction draw).

## Project Readiness

Fundable projects are ready projects. Sequence the readiness checklist in this order and do not submit applications ahead of it:

1. **Needs documentation** — for the facility type: a community health needs assessment or FQHC look-alike/section 330 service-area analysis (health), a child care market/child population study (child care), an enrollment study with waitlists (charter), a food access/food desert analysis (grocery), or a program-demand and jobs study (workforce). *Completion condition: a dated third-party or well-documented internal needs study in the file.*
2. **Feasibility study** — economic feasibility (USDA requires it for CF applications): total development cost estimate by a qualified cost estimator, funding plan, and repayment analysis. Retail projects add a sales projection; charters add a pro forma per pupil.
3. **Site control and predevelopment** — purchase agreement, option, or executed long-term lease; zoning confirmation; Phase I environmental site assessment; survey and title. Charter schools leasing from their own supporting nonprofit must document the lease passes arm's-length review.
4. **Operating pro forma for the facility** — a multi-year operating projection *separate from the organization's budget*: stabilized-year revenue (patient visits, enrolled slots, enrolled pupils, projected sales), ramp-up period, operating expenses, and debt service by tranche, showing DSCR by year. Lenders decline on gap-year coverage, not stabilized coverage.
5. **Organizational file** — three years audited financials, board resolution authorizing borrowing, board-adopted debt policy or facility reserve policy, executive leadership continuity, and a capital campaign progress report if gifts are in the stack.
6. **Application package assembly** — pre-application filed with the right agency (USDA state office, conduit issuer, CDE, CDFI lender) with all of the above attached. *Completion condition: each funder confirms the application is complete and has a named reviewer and decision date.*

## Standard Deliverables

1. **Facility capital-stack template** — a sources-and-uses table: uses (acquisition, construction, equipment, FF&E, A&E, financing costs, contingency) vs. sources by layer (senior debt, USDA CF loan/grant, NMTC equity, CDFI debt, government grants, philanthropy, org equity), each with amount, terms (rate, amortization, maturity, security position), status (committed / term sheet / applied / identified), and funding timing.
2. **USDA CF decision framework** — the six-step instrument-selection memo above, ending in one of: direct loan+grant application, guaranteed-loan application with named lender, or a documented ineligible/redirect decision.
3. **Funder-mix comparison** — the facility-type table populated for the client's specific type, geography (rural/urban drives USDA eligibility and NMTC tract eligibility), and revenue base, with named anchor funders.
4. **Project-readiness checklist** — the six readiness items with owner, status, and the completion condition for each.

## Common Failure Modes

- **Quoting stale USDA rates or wrong population limits.** Rates reset quarterly and the FY guarantee percentage changes annually (80% in FY2026 vs. the 90% statutory max); the 20,000 cap is for direct loans/grants and 50,000 for guarantees. Remedy: verify at rd.usda.gov the week you cite.
- **Applying for a CF grant on a commercial project.** A nonprofit grocery or business incubator can qualify as an essential facility only with a documented food-access/community-service case; "inherently commercial enterprises" are excluded from guarantees. Remedy: pre-clear with the state CF office.
- **Assuming grant money is available at closing.** Grants reimburse on milestones; projects stall without a bridge. Remedy: build the draw-timing bridge into the stack.
- **Blowing the bank-qualified limit.** The $10 million test is per calendar year at the borrower level — a second bond issue or a refinancing in the same year disqualifies it. Remedy: confirm the year's issuance calendar with the conduit issuer before designation.
- **Starting NMTC too late.** CDE allocation relationships and structuring take 6–12 months. Remedy: open CDE conversations at concept design.
- **No facility-level operating pro forma.** Organizational budgets hide facility ramp-up losses; lenders decline on year-1 and year-2 coverage. Remedy: build the standalone multi-year facility pro forma before sizing debt.
- **Skipping TEFRA/rebate/disclosure compliance planning on public bonds.** Hearing after issuance, missed rebate filings, or lapsed EMMA disclosures impair the exemption. Remedy: bond counsel and municipal advisor engaged before the first drafting session.
- **Charter school assumes facility funding that doesn't exist in its state.** Only some states fund per-pupil facilities or give charters bond-guarantee access. Remedy: verify the state's charter facility finance landscape before the budget is set.
