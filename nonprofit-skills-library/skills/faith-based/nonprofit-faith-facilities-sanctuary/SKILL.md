---
name: nonprofit-faith-facilities-sanctuary
description: "US worship-building operations: state property-tax exemption for religious use, RLUIPA zoning, facility-use policies for outside renters (interfaith co-use, 12-step, day care, weddings, funerals, cell tower), IRC §512(b)(3) rental UBIT and the §514 debt-financed trap, house-of-worship insurance (sexual-misconduct riders, 15-passenger van, Church Mutual / Brotherhood Mutual / GuideOne), deferred-maintenance FCAs, historic preservation, closed-church sale under denominational trust clauses (Dennis Canon, PCUSA, UMC, Jones v. Wolf), and sanctuary hosting. Triggers: 'facility use policy,' 'property tax exemption challenge,' 'wedding for non-member,' 'sell the building.' Not for trust-clause governance fights (nonprofit-faith-church-governance), church-990/UBIT (nonprofit-faith-990-exemption), RLUIPA statutory law (nonprofit-faith-religious-liberty-compliance), safe-sanctuary policy (nonprofit-faith-employment-ministerial-exception), or secular facilities (nonprofit-vendor-facilities, nonprofit-risk-management)."
license: MIT
metadata:
  supervision: "review"
  supervision_note: "Facility-use policies, insurance decisions, property-tax filings, and building-sale documents are legal instruments with tax, liability, and denominational-property consequences that require counsel and licensed-broker review."
  last_reviewed: "2026-09-10"
  date_added: "2026-09-12"
  date_added_source: "git:297d3ef69a314702df1ccc8174826716c88cff40"
---

# Faith Facilities and Sanctuary Space (Worship-Building Operations)

## When to Use This Skill

Use this skill when the user is responsible for the **physical worship building** of a
congregation or faith-based nonprofit and is working on how the building is shared, insured,
taxed, used for life-cycle events, maintained, adapted, closed, or sold. Trigger phrases include:
"draft a facility use policy," "a 12-step group / homeschool co-op / another congregation wants
to rent our space," "our property-tax exemption got challenged," "the city denied our conditional
use permit," "cell tower lease on our steeple," "wedding request from a non-member," "we're
renting the fellowship hall for weddings — is that UBIT?", "our insurer is asking about safe-
sanctuary practices before renewing," "15-passenger church van," "our building needs $2M of
deferred maintenance," "we're on the National Register — can we replace the windows?", "we're
closing and selling the building," or "a family facing deportation is asking to stay in our
sanctuary."

Boundary: this skill is the **building as an asset and shared physical space**. Governance-side
decisions about the property — a congregational split, denominational disaffiliation, a
trust-clause lawsuit between the local congregation and its judicatory — belong to
`nonprofit-faith-church-governance`; the underlying Form-990 exemption and general church UBIT
framework belong to `nonprofit-faith-990-exemption`; the statutory text and litigation of RLUIPA,
RFRA, and Charitable Choice belong to `nonprofit-faith-religious-liberty-compliance`; the
safe-sanctuary child-protection policy itself (background checks, two-adult rule, reporting
protocols) belongs to `nonprofit-faith-employment-ministerial-exception` — this skill covers only
the **insurance side** of that policy. Fundraising a capital campaign to build or renovate the
building is `nonprofit-faith-stewardship-giving`; the actual program design of the food pantry,
recovery ministry, or shelter that operates inside the building is
`nonprofit-faith-programs-social-services`. If the user's organization is a secular 501(c)(3)
with no inherently religious character, hand off to `nonprofit-vendor-facilities` and
`nonprofit-risk-management` — most of the doctrines below (property-tax exemption for religious
use, RLUIPA zoning, church-mutual insurers, denominational trust clauses) do not apply.

## Core Frameworks

Name the doctrine that governs the situation before drafting anything; the same rental agreement
reads very differently against a debt-financed §514 building than against a paid-off sanctuary,
and the same building-sale reads very differently under a Dennis-Canon polity than under a
congregational-title polity.

- **Walz v. Tax Commission, 397 U.S. 664 (1970)**: upheld the constitutionality of property-tax
  exemption for religious use. Walz is the ceiling — it permits exemption but does not require
  it. Every state sets its own rules and assessors apply them parcel by parcel. Assume nothing
  is exempt until the exemption is filed for, granted, and periodically renewed.
- **IRC §501(c)(3) automatic church exemption**: automatic federal recognition does not create
  state property-tax exemption, which is a separate filing in most states. Do not conflate the
  two. See `nonprofit-faith-990-exemption` for the federal side.
- **RLUIPA (42 U.S.C. §2000cc)**: bars local zoning schemes from imposing a "substantial
  burden" on religious exercise without a compelling interest and the least restrictive means,
  and bars unequal treatment vs. comparable secular assemblies. For statutory analysis, use
  `nonprofit-faith-religious-liberty-compliance`; here, treat RLUIPA as the operational leverage
  a congregation has when the planning commission says no.
- **IRC §512(b)(3) — rental of real property**: rents from real property are generally excluded
  from Unrelated Business Income Tax, so wedding-rental, hall-rental, and tenant-nonprofit
  office rent are typically not UBIT for a church.
- **IRC §514 — debt-financed property**: the §512(b)(3) rental exclusion is lost pro-rata to the
  extent the property is subject to "acquisition indebtedness." A congregation that borrows to
  build a large multi-purpose building and then rents it out has UBIT exposure on the borrowed
  portion, even though bare rental is normally excluded. This is the single most-missed UBIT
  trap in faith facilities.
- **IRC §512(b)(3)(A) parenthetical — services rendered**: the rental exclusion is lost when the
  church provides "substantial services" with the space (catering, event staffing, AV operation,
  security, cleaning done as part of the rental package rather than a routine maintenance
  overhead). Bare rental with tenant self-service is the safe posture; "wedding package with
  coordinator, sound tech, and reception service" is not.
- **Notice 2018-99 and the parking-lot mess**: the TCJA-era employee-parking UBIT rules created
  a compliance panic for congregations that rent parking; the 2019 legislative repeal and
  subsequent guidance simplified but did not eliminate the analysis. Event parking and permit
  parking are still analyzed as real-property rental (usually excluded) unless services are
  bundled.
- **Fulton v. City of Philadelphia, 593 U.S. ___ (2021)**: where the state acts as a
  contractor, a system of individualized exemptions triggers strict scrutiny of religious
  burdens. Read Fulton for the state-actor-pressure line (municipal facility-use conditions,
  government-tenant demands) — not as blanket authority for private-org rental discretion.
- **Bostock v. Clayton County (2020), Masterpiece Cakeshop (2018), 303 Creative (2023)**:
  Bostock reaches sexual-orientation and gender-identity discrimination in employment;
  Masterpiece and 303 Creative preserve expressive/religious protections in specific
  compelled-speech postures. The unresolved live question for faith facilities is whether
  renting the sanctuary to outside parties triggers public-accommodation analysis under state
  law. Route to counsel in every state.
- **Jones v. Wolf, 443 U.S. 595 (1979) — neutral-principles doctrine**: civil courts resolve
  church-property disputes by applying neutral principles of property, trust, and contract law
  to the deed, state statutes, articles/bylaws, and any denominational trust clause. Every
  property-sale analysis for a church in a hierarchical denomination begins here.
- **Denominational property trust clauses**: the Episcopal Church's Dennis Canon (Canon I.7.4),
  the PCUSA's property trust clause (Book of Order G-4.0203), the UMC Trust Clause (¶2501 of the
  Book of Discipline, central to disaffiliation-era property disputes under the now-sunset
  ¶2553), and comparable provisions in ELCA, RCA, AME, and Roman Catholic diocesan structures.
  Congregational-polity Baptist, non-denominational, and independent Jewish and Muslim
  congregations typically hold title free of a denominational trust — but always check the deed
  and the state statute, not the polity assumption.
- **Partners for Sacred Places / National Fund for Sacred Places**: leading US practitioner
  research on aging religious buildings, deferred maintenance, and adaptive reuse; treat their
  "Halo Effect" studies and FCA templates as the standard reference.
- **National Register of Historic Places / Section 106 / Secretary of the Interior's
  Standards**: designation restricts what can be modified and triggers review when federal
  funds or permits are involved, but also unlocks Historic Rehabilitation Tax Credits and
  historic-preservation grants.

## Standard Deliverables

Every in-scope request resolves into one of these artifacts:

- **Property-tax exemption application or renewal**, including the parcel-by-parcel use analysis
  and mixed-use pro-rata schedule.
- **Facility Use Policy** — the master document governing which outside groups may use the
  building, on what terms, with what fees, with what insurance, and with what mission-alignment
  criteria.
- **Facility use / rental agreement** — the individual contract signed with a specific outside
  user, referencing the policy.
- **Wedding policy and funeral/memorial policy** — special-case use agreements for life-cycle
  events, typically with clergy-officiant provisions.
- **Insurance program review memo** — the annual walk-through of coverages, sub-limits, riders,
  and named perils against the congregation's actual risk footprint.
- **Facility condition assessment (FCA) narrative** — the 5- to 20-year deferred-maintenance
  plan translated into board-actionable language and reserve-funding targets.
- **Building sale / closure memo** — the denominational-approval, deed-review, use-restriction,
  and reuse-buyer analysis for a congregation preparing to close or consolidate.
- **Physical-sanctuary hosting policy** — the board-adopted policy governing whether and how the
  congregation will provide physical shelter to vulnerable individuals (typically undocumented
  families facing deportation), and the operational protocol if it does.

## Producing a Facility Use Policy — Numbered Checklist

Run this checklist whenever a congregation asks to formalize outside use. The failure mode is
saying yes to individual requests ad hoc until an incident forces the policy to be written under
pressure.

1. **Inventory current and expected users**: list every group already using the building
   (another congregation, 12-step meeting, Scout troop, homeschool co-op, day care, polling
   place, community theater, immigrant community association, wedding parties, memorial
   services, film shoots, cell-carrier antenna lease, music studio). Separate by
   ecumenical/interfaith co-use, community-nonprofit use, for-profit use, and life-cycle use —
   the policy treats each category differently.
2. **Set eligibility categories and mission-alignment criteria**: draft the eligibility clauses
   before the fee schedule. Typical categories are (a) congregation members and
   member-sponsored events, (b) other faith communities, (c) community 501(c)(3)s aligned with
   mission, (d) neutral civic uses (polling place, blood drive), (e) commercial and for-profit
   users. Include a mission-alignment clause consistent with the congregation's teachings and
   any denominational standards — but frame it as content of the use, not identity of the user,
   and route to counsel any clause that could read as unlawful discrimination under applicable
   state or municipal law.
3. **Build the fee schedule with member / nonprofit / commercial tiers**: rate differentiation is
   normal and defensible, but keep the tiers documented so an assessor or auditor can see the
   logic. Distinguish a use fee (which looks more like a commercial transaction) from a required
   donation (which looks more like offset of building costs) — the framing matters for the
   §512(b)(3) rental analysis, though substance controls over labels.
4. **Require certificate of insurance and additional-insured status from every outside user**:
   minimum limits are congregation- and insurer-specific (a common floor is $1M per occurrence /
   $2M aggregate general liability; higher for events with alcohol, children, or physical
   activities). The COI must name the congregation as additional insured, not merely as
   certificate holder — the distinction is what actually triggers the user's insurer to defend
   the congregation.
5. **Address alcohol, kitchen, tech, keys, and cleaning explicitly**: each is a common incident
   source. For alcohol: prohibit outright, or require a licensed bartender and event-specific
   liquor liability from the user. For kitchen: require food-handler certification for warm food
   service, or restrict to catered/pre-packaged. For AV: require congregation-operator or
   pre-training; do not let untrained users touch the sound system. For keys: assign, log, and
   collect; consider coded locks for recurring users. For cleaning: define restore-to-condition
   and a damage deposit large enough to fund it.
6. **Add indemnification, hold-harmless, and choice-of-law clauses**: standard boilerplate but
   often missing in the church-drafted rental agreement. Include a cancellation policy with
   escalating forfeitures and force-majeure language.
7. **Adopt in writing by the governing body and reference by date**: the policy is a governance
   artifact — the board, session, vestry, council, or trustees adopt it, minute it, and revisit
   it annually. The individual rental agreements reference the policy version by date.
8. **Set the exclusion/denial review process before you need it**: define who decides a close
   call, in what timeframe, on what criteria, and with what appeal — so the first controversial
   denial (a wedding that conflicts with the congregation's teachings, a political rally, a
   competing religious group) is handled inside a documented process rather than by the pastor
   at 9 p.m. on the phone.

## Property-Tax Exemption — Parcel-by-Parcel Discipline

Property-tax exemption is granted on a **parcel and use** basis, not on the org's federal status.
Walk each parcel through the same four questions:

- **Who owns it?** The religious organization must hold title (or, in some states, hold a
  qualifying leasehold). Property held by a member or a related LLC is often not exempt even
  when used religiously.
- **What is the primary use?** The sanctuary and directly religious-use property is the easy
  case. The parsonage (clergy residence provided as part of ministerial employment) is exempt in
  most states, sometimes with a value cap. A food pantry, ESL classroom, or after-school program
  operated by the congregation is usually exempt. Rented-out office space to unrelated tenants,
  a coffee shop open to the public with no religious character, and land held vacant for future
  expansion are often not exempt — treatment varies sharply by state and by whether "held for
  future religious use" is recognized.
- **Is the use mixed?** Many states pro-rate exemption by square-footage-and-time of religious
  vs. non-religious use. A cell-carrier antenna on the steeple typically results in a small
  taxable carve-out of the antenna footprint and equipment cabinet. A rented office suite is
  taxed on its square-footage share. Document the calculation before the assessor asks.
- **Is there acquisition indebtedness or a mortgage?** In most states, a mortgage does not defeat
  exemption — but note that the federal UBIT analysis under §514 is separate and **does** care.

When challenged by an assessor, respond with: proof of religious-organization ownership; a
current use inventory with square footage, calendar hours, and photographs; the mixed-use
pro-rata worksheet; and the governing-body-adopted mission and use policy. Do not respond with
theology; respond with parcel data. If the challenge continues, engage local counsel with
property-tax-exemption experience before the appeal deadline; deadlines are short and unforgiving.

## Zoning and RLUIPA — Operational Reality

Zoning is where most congregations first meet serious municipal friction. Recurring patterns:

- **Pre-existing nonconforming use**: an older sanctuary in a since-rezoned district is
  typically grandfathered, but expansion, change of use, or extended abandonment can
  extinguish that status. Do not let the building sit unused across the local abandonment
  threshold (often 6-24 months) without a documented continuation plan.
- **Conditional use permits (CUP) and special-use permits**: adding a school, day care,
  shelter, or food pantry often requires a new permit with public hearing. RLUIPA does not
  eliminate parking / traffic / "character" objections but does bar treating a house of worship
  worse than a comparable secular assembly (theater, banquet hall, private club).
- **Parking is the recurring killing constraint**: many codes require one space per three
  sanctuary seats. Sanctuary redesign, expansion, or shared-use approval often stands or falls
  on parking. Document shared-parking agreements with adjacent owners as recorded easements
  where possible.
- **Historic district overlays**: designation adds a Historic Preservation Commission review
  layer on top of standard zoning for exterior work. Time every project for the review cycle,
  not the construction season.
- **Food-pantry parking-lot use and shelter-in-church cases**: municipalities have tried to
  restrict outdoor food distribution and overnight shelter as "nonconforming intensification."
  This is the recurring RLUIPA fact pattern; route to counsel promptly and preserve the
  administrative record.
- **Expansion applications**: pre-file, walk the neighbors, address parking and traffic before
  the hearing packet lands, and use community-benefit data (Partners for Sacred Places "Halo
  Effect") as one input to the record, not the whole argument.

For RLUIPA statutory strategy and case law, load `nonprofit-faith-religious-liberty-compliance`.

## Shared Use, Rental, and UBIT

Shared use is the single most common facilities question a congregation will bring. Work the
UBIT analysis under §512(b)(3), §514, and §513 for every rental posture:

- **Ecumenical or interfaith co-use** — another faith community rents worship time (Jewish
  congregation Saturday, Christian congregation Sunday; two Christian congregations sharing).
  Typically bare real-property rental, excluded from UBIT. Document sanctuary layout, sacred-
  object storage, calendar coordination around each tradition's high holy days, and cleaning.
- **Community rental** (12-step recovery, homeschool co-op, Scouts, community theater, polling
  place, immigrant community associations, day care): typically excluded from UBIT if bare
  space rental. Day care is the most complex — check state licensing (which drives kitchen,
  bathroom, playground, staffing) and the state's tax treatment of the day-care square footage.
- **For-profit rental** (music studio in fellowship hall, wedding-venue rentals, film shoots):
  §512(b)(3) still excludes bare real-property rental. Two vectors flip the answer — **§514
  debt-financed property** applies UBIT pro-rata to the debt-financed portion, and
  **substantial services** (staff, catering, AV, security, coordination bundled in) collapses
  the rental exclusion into service-plus-space.
- **Cell tower and rooftop antenna leases**: typically real-property rental (excluded), subject
  to the §514 debt-financed analysis. Also check the property-tax pro-rata carve-out for the
  antenna footprint and require the carrier to indemnify for structural, RF-exposure, and
  access risks.
- **Parking-lot rental**: post Notice 2018-99 and 2019 TCJA repeal, permit and event parking
  are analyzed as real-property rental (usually excluded). Attended parking with congregation
  staff bundled in tips into services-plus-space.

When drafting the rental agreement, include: use description, times, fee, insurance (COI +
additional insured + minimum limits), damage deposit, kitchen / alcohol / tech rules,
indemnification, cancellation, and reservation-of-rights clauses. Cross-reference the Facility
Use Policy by date. Route any wedding-rental arrangement that touches the congregation's
teachings on marriage to counsel — Bostock / Masterpiece / 303 Creative and applicable state
public-accommodation statutes have not converged.

## Insurance Specific to Houses of Worship

House-of-worship insurance is a distinct market. The generic nonprofit commercial package will
underprice or misrate the risks. Work with a broker who specializes in the sector and consider
a church-mutual carrier — **Church Mutual, Brotherhood Mutual, GuideOne, Philadelphia
Insurance, and Chubb Nonprofit** all have significant faith-sector books, with different
appetites for denominational affiliation, size, and risk. Cover these lines and review annually:

- **Sexual-misconduct / sexual-abuse liability**: usually a separate line or endorsement, not
  automatic in general liability. Almost always subject to sub-limits (often $1M-$5M),
  claims-made rather than occurrence, and conditional on documented **safe-sanctuary practices**
  — background checks, two-adult rule, training records, reporting protocols. Coverage may not
  respond if the underlying policy was not being followed. For the child-protection policy
  itself, load `nonprofit-faith-employment-ministerial-exception`; here the job is confirming
  the insurance actually responds when the policy fails.
- **Directors and Officers (D&O)** for elders, deacons, trustees, session, vestry, council, or
  board. Standard secular-nonprofit D&O plus a religious-organization endorsement addressing
  clergy discipline actions and denominational-relationship claims.
- **Employment Practices Liability Insurance (EPLI)** with a religious-employer rider that
  contemplates the ministerial exception (Hosanna-Tabor, Our Lady of Guadalupe) — coverage
  should not exclude clergy-related claims outright but should acknowledge the exception's
  effect on defense strategy. Confirm the wage-and-hour sub-limit and third-party harassment
  coverage (which reaches volunteer and congregant-on-staff conduct).
- **Pastoral counseling professional liability**: some general-liability forms exclude
  professional counseling; either buy the specific endorsement or restrict clergy counseling
  practice to what the policy will cover.
- **Property**: replacement-cost basis with agreed-value endorsement for irreplaceable elements
  — steeple, stained glass, historic pipe organ, Torah scrolls, sacred art, historic pews.
  Confirm coinsurance is set correctly. Add ordinance-or-law coverage for post-loss code-
  upgrade cost (critical for historic buildings). Confirm earthquake and flood posture
  explicitly; both are typically excluded unless bought separately.
- **Auto**: church-owned vehicles and hired-and-non-owned auto for volunteers on congregation
  business. The **15-passenger van** is its own category — federal safety regulators flag
  rollover risk, insurers demand documented driver training and MVR checks, and some carriers
  will not write coverage on 15-passenger vans at all. Consider 12-passenger vans or
  contracted transportation for youth trips.
- **Event and outside-user liability** — funneled through the Facility Use Policy's COI +
  additional-insured requirement, not through the congregation's own policy.
- **Cyber liability**: increasingly standard for congregations that hold donor giving-history
  data, run online-giving platforms, or store background-check results.
- **Workers compensation** — required by state, with attention to whether clergy are covered
  (often optional to elect) and whether the SECA / dual-tax status of clergy affects payroll
  reporting (see `nonprofit-faith-finance-clergy-comp`).

## Weddings, Funerals, and Life-Cycle Events

Weddings and funerals produce more facility conflict than any other single class of event. Adopt
written policies before the next request arrives; the pastor / rabbi / imam should not be
negotiating terms during a family's grief or engagement.

For a **wedding policy**, address: eligibility (member, non-member, member-sponsored, any
category excluded on mission grounds — route eligibility definitions to counsel against the
state's marriage- and public-accommodation-law posture); officiant rules and license-signing;
timing constraints (Sabbath from Friday sundown to Saturday sundown in Jewish tradition, Sunday
morning in Christian tradition, Ramadan and Eid in Muslim contexts, Lent / Advent / High Holy
Days); alcohol posture; rehearsal / decoration / photography / music / cleanup rules; and
deposit + cancellation schedule. On money, distinguish **fee vs. donation vs. honorarium**: a
bare use fee reads like a commercial rental; a required donation reads like a cost offset; a
clergy honorarium is the clergy's income, reportable per `nonprofit-faith-finance-clergy-comp`.
Substance controls over label, but framing affects UBIT posture and public perception.

For a **funeral / memorial policy**: eligibility, cost posture (funerals are typically treated
more generously than weddings on fee — write that down so the treasurer is not surprised),
arrangements with funeral homes, tradition-specific elements (open casket, pall, Kaddish,
janazah prayer, wake), and receiving-line / meal use of fellowship hall.

## Deferred Maintenance and Building Sustainability

Deferred maintenance is the single largest hidden liability of most US congregations. The
sanctuary looks fine from the pew and terrifying from the boiler room. The remedy is discipline:

1. **Commission a Facility Condition Assessment (FCA)** from a licensed facilities professional
   — not from the trustees or a well-meaning building-committee volunteer — every 5 years, with
   annual updates. The FCA inventories every major system (roof, envelope, structure, HVAC,
   electrical, plumbing, life-safety, accessibility, historic elements) with remaining useful
   life, replacement cost, and priority.
2. **Translate the FCA into a 20-year capital plan** with year-by-year cost projections. Present
   to the governing body in a form they can act on: three scenarios (defer, minimum-viable,
   full-plan), with implications of each for reserves, capital-campaign timing, and mission
   capacity.
3. **Fund a building-reserve line separate from operating reserves and separate from any
   capital-campaign fund**. Target funding is 1-3% of replacement value per year; most
   congregations fund 0. Do not co-mingle deferred-maintenance reserves with unrestricted
   operating cash; the temptation to spend it on the current-year budget is what created the
   backlog.
4. **Cross-reference to Partners for Sacred Places research** on aging congregational buildings,
   the National Fund for Sacred Places grant program, denominational preservation funds (some
   dioceses, presbyteries, and conferences run building-loan and grant programs), and state
   historic-preservation offices.
5. **Consider adaptive reuse and building-sharing** as a strategy — a shrinking congregation may
   share the building with another congregation, lease unused space to a mission-aligned
   nonprofit, or convert underused wings to affordable housing or day care. Every option changes
   the property-tax, UBIT, insurance, zoning, and denominational-approval posture; work each one
   through the checklists in this skill before committing.

## Historic Preservation

If the building is designated on the National Register of Historic Places, a state register, or a
local historic district, the modification rules change materially:

- **Designation triggers review**: exterior modifications, and sometimes interior work in
  landmark-designated interiors, require review by the local Historic Preservation Commission
  and, when federal funds or permits are involved, **Section 106 review under the National
  Historic Preservation Act**. Plan projects to the review calendar, not the construction
  calendar.
- **Secretary of the Interior's Standards for Rehabilitation** govern what counts as an
  appropriate modification — replacement windows must match profile, roofing must match
  material, HVAC compressors must be sited to preserve exterior character. Non-conforming
  modifications risk loss of designation and eligibility for tax credits and grants.
- **Historic Rehabilitation Tax Credits (20% federal)** are generally not usable by a
  tax-exempt religious organization directly, but structured through a for-profit developer
  partnership can fund adaptive reuse of a congregation-owned historic building. Sophisticated
  transaction; engage specialist counsel and tax advisors.
- **Grant programs**: the National Fund for Sacred Places (Partners for Sacred Places + National
  Trust for Historic Preservation), state historic-preservation office grants, and
  denominational preservation grants. Most are matching grants tied to a defined project scope.

## Building Closure, Sale, and Consolidation

Closing a congregation and selling the building is the highest-stakes property decision a
faith-based nonprofit will make. Work the Jones v. Wolf neutral-principles analysis against the
actual documents:

1. **Read the deed first**. Look for reversionary clauses (property reverts if it stops being
   used for religious purposes), cemetery covenants (perpetual maintenance obligation), and
   use restrictions.
2. **Read the state statute on religious-organization property**. Many states specify how a
   religious corporation may convey real property (member vote, judicatory approval, or court
   petition).
3. **Read the local corporation's articles and bylaws** on real-property sale — required
   votes, quorum, notice, and any judicatory consent.
4. **Read any denominational trust clause** binding the local property to the larger body —
   Dennis Canon (Episcopal), PCUSA G-4.0203, UMC ¶2501, and comparable provisions in ELCA,
   RCA, AME, and Roman Catholic diocesan title typically require judicatory approval and may
   be enforced in civil court through Jones v. Wolf. Load `nonprofit-faith-church-governance`
   for the governance side; route to counsel for litigation.
5. **Deconsecration / desanctification liturgy**: most traditions have a rite for
   discontinuing sacred use. Complete the liturgy before closing; in some traditions it is a
   formal precondition to release.
6. **Reuse buyer analysis**: another congregation is often the cleanest sale; affordable-
   housing developers, community-center nonprofits, and secular buyers each carry different
   post-sale-use implications. Consider a restrictive covenant in the deed for preferences
   about future use (no bar / no strip club / no incompatible-mission use).
7. **Distribution of proceeds**: governed by denominational rules, state religious-corporation
   statutes, and the local corporation's dissolution provisions. A closing congregation may
   not simply hand the cash to a favored cause; distribution is typically constrained.

## Physical Sanctuary of Vulnerable Individuals

The sanctuary movement — a congregation offering physical shelter to a person facing
deportation, typically an undocumented family — is a distinct decision from the immigration-
legal-services program. Federal enforcement policy toward "sensitive locations" (schools,
hospitals, houses of worship) has fluctuated administration to administration and should not be
relied on as a shield. Work the decision as a board policy decision, not a pastor's judgment
call:

- **Legal exposure**: harboring analyses under 8 U.S.C. §1324 have historically been narrow in
  the shelter-in-sacred-space context but are not zero; law-enforcement posture is
  administration-specific. Route to immigration counsel with sanctuary-hosting experience before
  saying yes.
- **Insurance implications**: notify the carrier; several church-mutual carriers have written
  specific guidance on sanctuary hosting. Coverage for premises liability toward the hosted
  family and for any incident during the stay is not automatic.
- **Practical facility issues**: bathing, sleeping, cooking, laundry, HVAC, privacy, security,
  visitor management, media management, congregant volunteer scheduling, children's schooling,
  medical access. Draft an operations protocol before commitment; sanctuary is a 24/7
  responsibility that typically runs months or years.
- **Governance**: the governing body adopts the sanctuary policy in writing, with a defined
  exit posture, a defined resource limit, and a defined chain of decision for encounters with
  federal agents.

## Common Failure Modes

- **Confusing federal 501(c)(3) recognition with state property-tax exemption** — the
  congregation assumes it is exempt because it is a church, never files the state application,
  and gets a tax bill years later with penalties. Fix by filing state exemption for every
  parcel, refiling on renewal, and treating it as a distinct compliance track.
- **Ad hoc facility rental with no written policy** — every request is negotiated by clergy,
  insurance requirements are inconsistent, the first incident forces policy adoption under
  pressure. Fix by adopting a Facility Use Policy now, requiring COI + additional-insured on
  every existing user by a defined date, and moving intake to the business administrator.
- **UBIT surprise on the debt-financed multi-purpose building** — the congregation borrowed to
  build a fellowship / community-space wing and rents it out, assuming rental income is
  excluded, without running §514. Fix by running §514 pro-rata every year acquisition
  indebtedness exists and reserving for the UBIT expense.
- **"Wedding package" services-plus-space slippage** — the congregation drifts from bare rental
  into bundled coordinator / sound tech / hostess / decoration / cleaning service and loses
  the §512(b)(3) exclusion. Fix by keeping the rental agreement bare and pricing services as
  separate optional add-ons, or accepting UBIT posture explicitly.
- **Sexual-misconduct coverage assumed inside general liability** — coverage is actually a
  sub-limited, claims-made, safe-sanctuary-conditional endorsement, learned at claim time.
  Fix by pulling the endorsement, confirming limits and required safe-sanctuary practices,
  and confirming actual practice matches.
- **Deferred-maintenance denial** — trustees minimize the boiler-room reality, no FCA is
  commissioned, the reserve is funded at 0, the roof fails during a capital campaign for a
  new wing. Fix by commissioning an independent FCA and separating the building reserve from
  operating cash and campaign funds.
- **Property sale attempted without denominational trust-clause analysis** — the congregation
  votes to sell, the judicatory intervenes, litigation eats the sale value. Fix by starting
  the neutral-principles analysis (deed + state statute + articles + trust clause) before the
  sale motion is drafted, and engaging denominational counsel alongside the broker.
- **Sanctuary hosting decision made pastorally rather than governmentally** — the pastor
  commits the building to a family in crisis without a board policy, insurance notification,
  or operational protocol. Fix by adopting a sanctuary policy in advance if hosting is a live
  possibility, or declining and routing the family to a partner set up for it.

## Practitioner vs. Advisor Framing

- **As the executive / pastor / rabbi / imam / business administrator**: your defensive
  priorities in order are (1) property-tax exemption filed and current for every parcel; (2)
  written Facility Use Policy with COI + additional-insured on every outside user; (3)
  insurance program reviewed with a house-of-worship broker within the last 12 months, sexual-
  misconduct endorsement confirmed against actual safe-sanctuary practice; (4) FCA commissioned
  within the last 5 years and a building reserve funded separately; (5) any wedding, funeral,
  sanctuary hosting, or building-sale decisions made against written policy adopted by the
  governing body, not case-by-case by clergy under pressure. Wedding-rental decisions that
  touch the congregation's teachings on marriage and any sale under a denominational trust
  clause go to counsel before commitment, not after.
- **As an advisor** (denominational staff, board consultant, attorney, broker, or facilities
  consultant): name the polity and the applicable denominational property trust clause before
  touching a sale question; name the state's property-tax-exemption statute before touching an
  exemption challenge; name the state's public-accommodation posture before advising on
  wedding-rental eligibility. Push the client toward the artifacts (Facility Use Policy, FCA,
  insurance schedule, sanctuary policy) rather than resolving each incident on its facts.
  Coordinate with counsel on the four questions that most reliably become live cases: RLUIPA
  zoning, denominational property-trust litigation, sanctuary hosting, and wedding-rental
  discrimination.
