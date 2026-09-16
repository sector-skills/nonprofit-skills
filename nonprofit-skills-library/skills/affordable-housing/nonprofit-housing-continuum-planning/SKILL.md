---
name: nonprofit-housing-continuum-planning
description: "Maps a community's housing ecosystem across the housing continuum, from homelessness services to affordable homeownership; measures the need-vs-supply gap by AMI band and tenure using HUD CHAS, PIT, and local needs data; and helps nonprofit boards decide where the org should play: enter a stage, expand, exit, or partner. Use when a user says things like \"map our community's housing continuum,\" \"what's our county's housing gap,\" \"should we get into permanent supportive housing,\" or \"should we exit our shelter program and partner instead.\" Not for org-wide strategic planning (use nonprofit-strategic-planning), general needs-assessment methodology (use nonprofit-needs-assessment), market study or pro forma for a specific deal (use nonprofit-housing-development-finance), or design of one stage's programs (use nonprofit-housing-homelessness-services, nonprofit-housing-rapid-rehousing-transitional, nonprofit-housing-permanent-supportive-housing, nonprofit-housing-homeownership-programs)."
license: MIT
metadata:
  supervision: "review"
  supervision_note: "Gap math and board-level play decisions must be checked by a housing staffer before they inform strategy or funding requests."
  last_reviewed: "2026-09-12"
  date_added: "2026-09-12"
  date_added_source: "git:466adeb4b20092f7790a7d1d6b555af30dd69b99"
---

# Nonprofit Housing Continuum Planning

## When to Use This Skill

Use this skill to map a community's housing ecosystem, quantify the gap between housing need and supply by AMI band and tenure, and turn that map into "where we play" portfolio recommendations for a nonprofit board. Typical triggers: "we're writing a housing strategy — where is the gap in our county?", "how many of our renters are cost-burdened at 30% AMI?", "should our org get into permanent supportive housing?", "there's no path to ownership here — is that a gap we should fill?", "should we hand our transitional program to another agency?"

**Boundary with siblings:**
- If the board process is a full org-wide strategic plan where housing is one pillar, run `nonprofit-strategic-planning` and use this skill only for the housing-portfolio analysis inside it.
- If the user needs general community needs-assessment methodology (surveys, focus groups, indicator dashboards across health/education/housing), use `nonprofit-needs-assessment`. This skill is specifically about housing need/supply gaps on the continuum.
- Once a decision is made to pursue a specific deal, feasibility, market study, site control, and capital stack are `nonprofit-housing-development-finance`.
- Designing or operating the programs at a chosen stage: street outreach/shelter/diversion/coordinated entry is `nonprofit-housing-homelessness-services`; rapid rehousing and transitional housing operations are `nonprofit-housing-rapid-rehousing-transitional`; PSH design and Housing First fidelity are `nonprofit-housing-permanent-supportive-housing`; affordable rental operations are `nonprofit-housing-affordable-rental-operations`; ownership programs are `nonprofit-housing-homeownership-programs`; repair/preservation is `nonprofit-housing-repair-preservation`; CLT/shared-equity stewardship is `nonprofit-housing-community-ownership`.
- Housing-market advocacy and zoning reform that emerges from the gap map is `nonprofit-housing-advocacy-land-use`.

## Framework 1: The Housing Continuum as an Organizing Map

The continuum orders every housing intervention by household stability and permanence, from crisis response to market participation:

1. **Homelessness services** — street outreach, diversion/prevention, coordinated entry (no beds).
2. **Emergency shelter** — crisis beds, 30-90 day stays, low or no barrier.
3. **Transitional housing / rapid rehousing (RRH)** — time-limited housing with services (TH) or short-term rental assistance without a project bed (RRH, typically ESG- or CoC-funded, 1-2 year subsidy taper).
4. **Permanent supportive housing (PSH)** — permanent affordable housing with voluntary wraparound services, targeting chronically homeless and disabled households, Housing First model.
5. **Subsidized affordable rental** — LIHTC units, HOME/CDBG-assisted units, public housing, Housing Choice Voucher (HCV) tenancies, mission-driven nonprofit rental.
6. **Market rental** — unsubsidized, rent set by the market.
7. **Affordable homeownership** — shared equity, down-payment-assisted, or full-market ownership paths for households priced out of market ownership.

Two rules make the continuum a planning tool rather than a diagram:

- **People flow both directions.** A household at 25% AMI does not "graduate" to 60% AMI units in a tight market; the map must show choke points, not a one-way ladder. The most common structural failure is a community rich in shelter and rich in 60-80% AMI product with almost nothing in between — households exit shelter into homelessness, not into PSH or deeply affordable rental.
- **Count every stage, including ones you don't operate.** A gap map with an org-shaped hole (stages where the org has no visibility) is advocacy, not analysis. Inventory the whole ecosystem: public agencies, other nonprofits, for-profit LIHTC developers, PHAs, and informal supply (family doubling-up, which CHAS and PIT both miss).

**Practitioner vs. advisor:** a practitioner (housing org staff) builds the map to steer their own portfolio and to speak credibly in the local Consolidated Plan process. An advisor/consultant builds the same map but must also pressure-test the client's self-definition — boards describe what they do by program name, not continuum stage, and half the engagement is translating.

## Framework 2: AMI Bands and the 30%-of-Income Standard

**AMI** (Area Median Income) is HUD's estimate of median family income for a metro area or non-metropolitan county, adjusted by household size and updated annually. Every affordability conversation in US housing resolves to AMI bands:

- **≤30% AMI** — extremely low income (ELI). HUD defines ELI as the greater of 30% AMI or the federal poverty guideline.
- **31-50% AMI** — very low income (VLI); the HCV/public-housing eligibility world.
- **51-80% AMI** — low income; the LIHTC standard (the Section 60%-of-40%-at-50% test makes LIHTC buildings effectively serve this band).
- **81-120% AMI** — "workforce"/middle income; served by market product or modest subsidy.
- **Above 120% AMI** — market.

**The 30% standard:** a household is *cost-burdened* when housing (rent or ownership costs plus utilities) exceeds 30% of gross income; *severely cost-burdened* at 50%. This is the federal benchmark embedded in CHAS data, in the Brooke Amendment rent ceiling for public housing, and in virtually every needs assessment. Compute the affordability line per band: at 30% AMI, an "affordable" rent is 30% of that band's income, roughly the Section 8 standard of rent-plus-utilities equal to 30% of adjusted income (tenant-paid share is income-based, not unit-based).

**Two traps:**
- AMI for a 1-person household is not the 4-person AMI you see in the newspaper. Always cite the income limit for the actual household size, and never mix HUD AMI with state or city income-limit systems (some states and municipal programs publish their own, which differ).
- "Affordable" is not "available." A unit affordable to a 30%-AMI household may be occupied by a higher-income household. Gap analysis must count *affordable and available* units (NLIHC's distinction), not just rents below the threshold.

## Framework 3: Gap Analysis — Sources and Method

Build the needs/supply picture from four data layers, in this order:

1. **HUD CHAS data** — the Comprehensive Housing Affordability Strategy tabulation, HUD's special tabulation of American Community Survey data (5-year estimates), published by HUD PD&R for every state, county, place, and tract. CHAS gives households by income band (0-30%, 30-50%, 50-80%, 80-100%, 100%+ AMI) cross-tabbed by tenure, cost burden, overcrowding, and housing problems — this is the spine of the AMI-band needs table, and the same data the local Consolidated Plan uses, so your numbers reconcile with the jurisdiction's.
2. **HUD CPD documents** — the jurisdiction's 5-year Consolidated Plan and annual Action Plans (on HUD Exchange) contain the region's own priority needs, plus counts of HOME/CDBG/ESG-funded units. If your target community has a Consolidated Plan, mine it before collecting anything; a gap map that contradicts the ConPlan needs a reason why.
3. **PIT and HIC** — the Point-in-Time count (one-night census of sheltered and unsheltered homeless persons, each January, required by HUD for each Continuum of Care) and the Housing Inventory Count (beds by program type: ES, TH, RRH, PSH, safe haven). Together they size the homelessness-services end of the continuum. PIT is an undercount with known day-to-day variance — treat it as a floor, compare 3-5 years of trend, and note the CoC geography rarely matches your service-area geography.
4. **State/local/regional needs assessments** — state HFA housing needs studies, regional housing needs allocations (e.g., RHNA-style regional plans), city housing element gap analyses, university/PPRI studies. Layer these for the 80-120% AMI and ownership bands CHAS underexplains, and for local market dynamics (job growth, rent trends).

Supplementary sources for supply-side counts: HUD's LIHTC database and state HFA allocation plans for subsidized units, the National Housing Preservation Database for expiring-use risk, HUD TRACS/public housing inventory for deep-subsidy units, and NLIHC's *The Gap* and *Out of Reach* reports for national/state benchmarks (the 2026 Gap report finds a shortage of 7.2 million affordable and available rental homes for ELI renter households nationwide, ~35 per 100 ELI renters — useful to anchor how bad local numbers are against the national picture).

**The AMI-band needs/supply table** — the core analytical deliverable. For each AMI band, by tenure (renter/owner):

| Column | Source |
|---|---|
| Households in band | CHAS |
| Affordable units in band | CHAS / local inventory |
| Affordable **and available** units | CHAS (subtract higher-income occupants) |
| Gap (households − available units) | computed |
| Cost-burdened / severely burdened | CHAS |
| Pipeline units (LIHTC, HOME, city) | ConPlan Action Plan, HFA pipeline |

Read the table diagonally as well as by row: households priced out of their band overflow downward, so a 50-80% AMI shortage shows up as cost burden at 30-50% AMI.

## Framework 4: Where-We-Play Decisions

Once the gap map exists, the board question is: enter a stage, expand, exit, or partner? Score each candidate move against four tests, and require all four before recommending entry or expansion:

1. **Mission fit** — does the population in the gap match the org's mission population and theory of change?
2. **Gap evidence** — is the gap documented (your table), durable (not a one-year market wobble), and unclaimed (no other provider is competently filling it — duplication is a failure, not competition)?
3. **Right to win** — credible access to the operating model: for PSH, service capacity and CoC/HMIS standing; for LIHTC rental, a development partner or developer affiliate; for ownership programs, lending partners and stock to buy; for shelter, land and neighborhood acceptance.
4. **Financial sustainability** — an operating pro forma for the stage's dominant funding stream (CoC grants for PSH/RRH, project-based vouchers for deep rental, buyer-fee models for ownership). Do not recommend entering a stage whose funding stream the org has never raised; flag it as a prerequisite.

**Exit and partner are real options, not failures.** A shelter provider with full occupancy and strong RRH outcomes but no PSH pipeline should often *partner* (referral MOU with a PSH operator) rather than build PSH. Exiting a stage: recommend exit when (a) the gap has closed or moved, (b) another provider has clear comparative advantage, or (c) the funding stream has structurally eroded — and pair every exit recommendation with a transition plan for participants, staff, and funders. Never recommend an exit from a stage where the org is the sole provider without naming the successor.

**Practitioner vs. advisor:** the practitioner presents the decision memo to their own board with a recommendation. The advisor presents the same evidence but should hold the recommendation loosely — the classic consultant failure is recommending entry into the stage the client's ED already wanted. Test alternatives explicitly in the memo.

## Deliverable 1: Continuum Gap Map

1. Define the geography (county, city, or CoC) and state why; note where CoC, county, and city boundaries diverge — this changes PIT numbers.
2. Inventory every provider at every stage: programs, unit/bed counts, target population, waitlist if obtainable.
3. Overlay flows: where do households go when they exit each stage (ask providers for exit-destination data; HMIS reports it for CoC-funded programs)?
4. Mark choke points (exits to homelessness, waitlists >1 year, bands with zero product) and surpluses/duplication.
5. Draw the one-page map: continuum across the top, providers and bed counts underneath, gap flags in bold.
**Done when:** a reader can name the community's two worst choke points without asking, and every stage has a number (including zero) with a source.

## Deliverable 2: AMI-Band Needs/Supply Table

1. Pull latest CHAS 5-year data for the geography (state the vintage; CHAS lags the ACS by ~2 years).
2. Build the table by band and tenure with the columns above; compute the affordable-and-available line, not just affordability.
3. Add PIT/HIC counts under the ≤30% AMI renter column as a cross-check (CHAS misses sheltered/unsheltered households in group quarters).
4. Add pipeline and expiring-use risk (National Housing Preservation Database) so the gap is net.
5. Write a 3-5 finding narrative: the bands where the gap is structural, the bands that are actually fine.
**Done when:** every number has a named source and year, and the table reconciles with the Consolidated Plan's cited figures (or explains the discrepancy).

## Deliverable 3: Where-We-Play Decision Memo

Structure (keep to 5-7 pages):

1. **The gap in one page** — the map plus the table's headline findings.
2. **Our current position** — the org's stages, scale, performance, and financial exposure by funding stream.
3. **Options considered** — enter / expand / exit / partner / hold for each candidate stage, each scored against the four tests. Include at least one option the board will resist.
4. **Recommendation** — one primary move, with prerequisites (funding, partners, HMIS/coordinated-entry standing, board policy changes) and what it costs to be wrong.
5. **What we will not do** — explicit stop/de-prioritize list; a play memo with no subtraction has not decided anything.
6. **First 12 months** — the 3-4 milestones that make the move real or kill it (e.g., "execute MOU with the PSH operator" not "explore PSH").
**Done when:** the board can vote on a single motion naming the move, the prerequisites, and the stop list.

## Advisor Framing

- Scope data work separately from the decision memo — clients can build the gap table in-house with this skill and hire you only for the board process.
- Present the map to the full ecosystem (CoC, city housing staff, other providers) before the client's board sees recommendations; a recommendation built on other providers' data that they haven't seen breeds coalition damage that outlasts the engagement.
- In Consolidated Plan cycles, time the engagement so findings land during the jurisdiction's public-comment window — one engagement can shift HOME/ESG allocations, which is often the real motive behind commissioning the map.

## Common Failure Modes

- **Org-shaped map:** only stages the client operates are analyzed; gaps where the client could never play are ignored, so the board "decides" to keep doing what it does. Fix: inventory every provider before opening any option discussion.
- **Affordable ≠ available error:** counting units with low rents as gap-closers without checking who occupies them. Fix: always compute the affordable-and-available line.
- **CHAS vintage and geography mismatches:** comparing a 2023 5-year CHAS against last night's shelter count, or PIT (CoC-wide) against city boundaries. Fix: date-stamp every source in the table; convert to one geography and state the method.
- **One-way-ladder thinking:** presenting the continuum as a graduation pipeline when the actual flow is households stuck at the bottom. Fix: show exit-destination data and choke points explicitly.
- **Enter-bias:** the board always wants to add a stage; partner/exit options are never scored. Fix: require every option paper to include a partner and an exit scenario.
- **Uncosted recommendation:** "we recommend entering PSH" with no operating-funding analysis — PSH without committed services funding becomes an unaffordable rental property. Fix: a stage-entry recommendation without its funding stream analysis is returned, not circulated.
- **Funder-grade overreach:** the memo quietly becomes a fundraising pitch, dropping the inconvenient bands. Fix: keep the findings narrative and the recommendations in separate documents with separate review.
