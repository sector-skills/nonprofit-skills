---
name: nonprofit-housing-homelessness-services
description: "Operates US homelessness services: street outreach, emergency shelter operations, low-barrier and trauma-informed shelter practice, diversion and homelessness prevention, coordinated entry participation, HMIS data quality, and Point-in-Time counts. Use when a user says 'draft our shelter operations manual', 'what should our street outreach protocol include', 'train staff on diversion conversations', 'we need a coordinated entry access plan', 'plan our PIT count', or 'what are the ESG rules for shelter and prevention funding'. Not for rapid rehousing or transitional housing program design (use nonprofit-housing-rapid-rehousing-transitional), permanent supportive housing (use nonprofit-housing-permanent-supportive-housing), or drafting eviction-defense legal filings (route to legal aid partners)."
license: MIT
metadata:
  supervision: "review"
  supervision_note: "Shelter rules, safety protocols, and field outreach decisions carry liability and directly affect vulnerable people; a knowledgeable staffer must review before adoption."
  last_reviewed: "2026-09-12"
  date_added: "2026-09-12"
  date_added_source: "git:466adeb4b20092f7790a7d1d6b555af30dd69b99"
---

# Operating Homelessness Services

## When to Use This Skill

Use this skill for the front end of the homelessness system: reaching people where they are, getting
them inside, keeping them from losing housing in the first place, and connecting everyone to the
community's coordinated entry system. Concrete triggers:

- "Draft our emergency shelter operations manual."
- "What should our street outreach protocol include? Teams keep getting turned away at encampments."
- "Train staff on diversion / problem-solving conversations at the front door."
- "We're a new provider — how do we plug into the Continuum of Care and coordinated entry?"
- "Plan our Point-in-Time count."
- "What can we actually spend ESG street outreach / prevention money on?"

**Boundary — read before starting:**
- Designing or operating rapid rehousing or transitional housing projects is
  `nonprofit-housing-rapid-rehousing-transitional` — this skill covers them only as destinations to
  refer households to.
- Permanent supportive housing design and Housing First fidelity in permanent housing is
  `nonprofit-housing-permanent-supportive-housing`.
- Legal strategy for eviction defense or drafting court filings is outside this skill: note the
  issue and route the household to legal aid partners; do not draft legal documents.
- International/humanitarian or refugee shelter (camps, displacement settings) belongs to the
  library's international-aid pack, not this US-focused skill.
- Whole-community housing ecosystem mapping and gap analysis across AMI bands is
  `nonprofit-housing-continuum-planning`.
- Fair-housing complaints and accommodation law deep-dives are `nonprofit-housing-fair-housing`.

## The System Backbone: CoC, ESG, and HMIS

Every deliverable in this skill sits inside three federal structures. Learn them first:

1. **Continuum of Care (CoC)** — the regional planning body required by the McKinney-Vento Act as
   amended by the HEARTH Act (2009), governed by the CoC Program rule (24 CFR Part 578). Key roles:
   - **CoC Board** — sets written standards for administering assistance, ranks projects in the
     annual HUD funding competition (the CoC NOFO), and can reallocate funds from underperforming
     projects.
   - **Collaborative Applicant** — submits the CoC's consolidated application and runs planning.
   - **HMIS Lead** — operates the community's Homeless Management Information System.
   - **Coordinated Entry Lead** — runs the access/assessment/prioritization pipeline.
   - **Project applicants** — providers like the reader's organization.
2. **Emergency Solutions Grants (ESG)** — formula-allocated to states and entitlement
   localities, which subgrant to nonprofits. ESG components (24 CFR Part 576): **street outreach,
   emergency shelter, homelessness prevention, rapid rehousing, HMIS, and administration** (admin
   capped at 10% of the recipient's award). This skill covers the outreach, shelter, and prevention
   components; RRH program design routes to the sibling skill.
3. **HMIS** — the community-level database of client, bed, and service records required for
   ESG- and CoC-funded projects. Victim service providers are prohibited from entering client
   personally identifying information into HMIS and must run a comparable confidential database.

A provider that takes ESG or CoC dollars signs up for: documented eligibility at intake,
recordkeeping that survives monitoring, HMIS data quality, and coordinated entry participation.

### Checklist: joining your community's system

1. Identify your CoC (find it via HUD's CoC list or your state's interagency council on homelessness)
   and get on the CoC's provider mailing list and board-committee calendar.
2. Request the CoC's **written standards** and **coordinated entry written policies and
   procedures** — your intake rules must align with them.
3. Confirm with the ESG grantmaker (city/county/state) the current-year eligible activities,
   match requirement (ESG requires a dollar-for-dollar match), and reporting calendar.
4. Complete HMIS user training and sign the HMIS participation/participation-data-sharing
   agreements before the first client is served.
5. Map which roles your org must fill (access point? assessment site? referral receiver?).

**Done when:** intake staff can state, from the CoC's own written CE policies, how a person
enters the system, gets assessed, and gets referred — and your grant agreements, HMIS access, and
written standards copies are on file.

## Street Outreach Protocol

Street outreach is not case delivery to a captive audience — people outside have no obligation to
engage. The work is relationship-building with a housing purpose, funded (when ESG-funded) only for
people in Category 1 of HUD's homeless definition ("literally homeless" — unsheltered, or in
shelters/institutions where they cannot stay). ESG outreach essential services center on engagement
and case management, and can include emergency health-related services, transportation, linkage to
emergency shelter, and services for special populations.

### Protocol contents (the deliverable)

1. **Engagement standards** — first contact is trust-building, not screening; no ultimatums;
   consistent team assignment so the same faces return; harm-reduction orientation (meet basic
   needs first: water, blankets, food, harm-reduction supplies); "housing ready" conversations come
   after rapport, not as the price of service.
2. **Field safety rules** — two-person minimum teams; a check-in/check-out procedure with a base
   (time out, locations, expected return); weather thresholds and cold-weather escalation (warming
   centers, "Code Blue"-style protocols); sharps and biohazard handling; naloxone carried and staff
   trained to use it; a de-escalation policy; what staff do (and never do) when encampment
   residents are armed, hostile, or in medical crisis (call emergency services; do not intervene
   physically).
3. **Encampment practice** — never participate in a clearance/sweep without a rehousing plan;
   document every household's location and contacts so people are not lost when a camp closes;
   give notice of any closure effort and work the by-name list before the closure date.
4. **Data and eligibility capture** — document Category 1 homelessness where you meet the person
   (where they slept, for how long, third-party verification options) so later program enrollment
   doesn't stall; record engagements in HMIS per your CoC's data-entry timelines; carry consent
   forms.
5. **Referral connections** — every contacted person gets information about the access point and,
   if they consent, a direct warm handoff into coordinated entry.

**Done when:** a brand-new outreach hire can read the protocol and execute a safe first contact,
and the protocol has passed review by your safety/risk officer and (if ESG-funded) matches the
subaward terms.

## Emergency Shelter Operations

### ESG shelter funding rules to design around

- Eligible costs: essential services (case management, life skills, child care, transportation,
  services for special populations, employment assistance), **operating costs** (rent, utilities,
  food, maintenance, security, insurance, supplies), and rehabilitation/conversion — the last with
  per-project cost caps and minimum period-of-use commitments, so verify current limits with your
   grantmaker before budgeting rehab dollars.
- Shelter clients must meet the applicable homeless definition; document it at intake.
- Shelter is low-cap-exit by design: the operating goal is as short a stay as possible with
  diversion, rapid exit planning, and housing-focused case management — not a waiting-for-PSH
   warehouse.

### Low-barrier, Housing First–oriented, trauma-informed design

- **Low-barrier ("shelter-first")**: drop rules that screen people out — sobriety requirements,
  government ID at intake, income requirements, zero-tolerance curfews that punish workers, bans on
  couples, pets, or possessions. Every barrier added means beds stay empty while people sleep
  outside; measure and manage bed utilization accordingly.
- **Housing First orientation inside shelter**: housing search starts at intake, not after
  "readiness"; services are voluntary; sobriety and treatment are never conditions of staying.
- **Trauma-informed practice** — institutionalize SAMHSA's six principles: physical and
  psychological safety; trustworthiness and transparency; peer support; collaboration and
  mutuality; empowerment, voice, and choice; and attention to cultural, historical, and gender
  issues. In shelter terms: knock before entering a sleeping area; explain every rule and its
  reason; give guests choices about location and services; ask "what happened to you," never "what's
  wrong with you."
- **Equal access**: placement in single-sex facilities consistent with a person's gender identity
  per HUD's Equal Access rules; family composition policies that keep families together; never turn
  away people for disability-related behavior that a reasonable accommodation would address — route
  accommodation questions to `nonprofit-housing-fair-housing`.

### Safety architecture (the liability-heavy part)

- VAWA compliance (notice of rights, emergency transfer awareness, confidential handling of any
  domestic-violence status), incident logs with same-day documentation, mandatory-reporting rules
  understood, fire and occupancy-code compliance, infirmary/isolation space in outbreak plans,
  infectious-disease protocols built with your local health department, overdose response (naloxone
  in the building, a standing order if allowed in your state), medication storage and self-medication
  policy, and de-escalation-first use-of-force rules (staff never restrain; they disengage and call
  for help).

### Shelter operations manual outline (the deliverable)

1. Purpose, model, and target population; capacity and bed types (adult, family, DV-safe where
   applicable).
2. Intake and admission: hours, documents NOT required (ID, income), screening only for safety,
  placement consistent with gender identity.
3. Rules of conduct: minimal, safety-only rules; each rule paired with the reason and the
   graduated response — plus the guest rights and grievance procedure.
4. Day-to-day: curfew exceptions (work, medical), meal service, laundry, storage, pets, visitors,
  mail and phone/message handling.
5. Case management: voluntary services, housing plan started at intake, rapid-exit/diversion
   follow-through, warm referrals.
6. Safety and emergencies: fire, medical, overdose, behavioral crisis, evacuation, incident
   reporting.
7. Health and sanitation: cleaning schedules, outbreak response, pest control.
8. Staffing and training: shift structure, boundaries, mandated reporter duties, trauma-informed
   and de-escalation training requirements.
9. Discharge/exit: no "service-proof" exit requirements; re-entry welcome; documentation.
10. Data and reporting: HMIS entry timelines, bed utilization tracking (this feeds the HIC),
    funder reports.
11. Compliance appendix: ESG recordkeeping, VAWA notices, Equal Access, state licensing if any.

**Done when:** the manual covers all 11 sections, an attorney or insurer has reviewed the rules
and safety sections, and staff can trace every house rule to a safety rationale.

## Diversion and Homelessness Prevention

### Diversion (problem-solving) — the front-door conversation

Diversion is a light-touch, housing-focused conversation with a person presenting for shelter who
could resolve their own housing crisis with modest, short-term help. It is never a gatekeeping
interview.

**The conversation structure:**
1. Open with safety: "Before we talk options — is anyone unsafe tonight?" (If yes, follow the DV
   protocol; safety exceptions override diversion.)
2. Ask what happened, then the magic question: "If money weren't an issue, where would you stay
   tonight, and who might you call?" Most diversion success comes from the household's own network.
3. Brainstorm together: returning to family or friends with mediation or a one-time payment,
  travel to housing elsewhere, landlord negotiation to end an eviction before it starts, resolving
   the immediate barrier (car repair, utility arrearage, ID fees).
4. Offer the small resources that unlock self-resolution: mediation, a bus ticket, a night or two
   of motel or rent bridge, deposit help where allowed.
5. Close honestly: whatever the household decides, shelter access is unconditional — "if this
   doesn't work tonight, come back."

**Diversion rules of the road:** minutes, not weeks; never repeat the conversation for the same
household as the price of shelter; never fund diversion out of a prevention award when
program-eligibility rules don't fit; record outcomes in HMIS per your CoC's data standards.

**Decision tree (deliverable):** safe tonight? → could stay somewhere tonight with small help?
→ resolve there with diversion resources → no? → shelter tonight, housing plan starts at intake →
any eviction or court date anywhere in this path → legal aid partner referral.

### ESG homelessness prevention — what makes a household eligible

ESG prevention is narrow and documentation-heavy: income at or below 30% of area median income, no
resources or support network to fall back on, and a qualifying imminent-risk situation under the
current "at risk of homelessness" definition in the ESG rule (for example facing eviction with no
new residence lined up within days, exiting an institution or foster care without resources, or
fleeing domestic violence). Verify each element against the current regulation before writing your
screening criteria, because HUD has amended this definition. Rent/short-term assistance caps apply
(a multi-month limit within a multi-year period), so confirm the current limits with your
grantmaker.

**Eviction-diversion legal strategy is not yours to draft:** when a household has an active court
case or needs defense strategy, note the facts and route to legal aid partners; this skill stops at
the program-design and referral layer.

### Prevention program checklist

1. Write screening criteria that track the ESG eligibility elements verbatim, with the documentation
   evidence each element requires.
2. Build the income certification, homeless/at-risk status documentation, and payment trail to the
   standard your grantmaker monitors against.
3. Set the diversion conversation standards and resources separate from the prevention award rules.
4. Establish the legal aid referral list and a warm-referral script for court-involved households.
5. Define success as "housing retained/crisis resolved without shelter entry," and set up HMIS
   tracking of that outcome.

**Done when:** a monitor could reconstruct eligibility for every assisted household from the file
alone, and front-door staff can distinguish diversion from prevention in one sentence.

## Coordinated Entry Access Plan

Coordinated entry (CE) requirements come from the CoC Program rule and HUD's coordinated entry
notice (CPD-17-01, and successor guidance): the CoC must operate CE covering its entire geography,
with a standardized access process, a standardized assessment, written prioritization standards, and
referral procedures for participating projects — all documented in written CE policies. ESG- and
CoC-funded projects must participate; victim service providers may run an approved comparable
process.

### Building or improving your CE access piece (the deliverable)

1. **Map access points**: define every place a person can present (shelter, outreach, 2-1-1/hotline,
   drop-in centers, partner agencies, hospital discharge, jail release) so there is "no wrong door";
   specify after-hours and rural coverage — an access system that only works 9–5 fails the test.
2. **Standardize the access experience**: one script and triage questions everywhere, safety
   screening for DV, no eligibility pre-screening that excludes anyone from CE.
3. **Assessment**: adopt the CoC's chosen tool (many CoCs use the SPDAT family or a locally designed
   tool); use it to inform prioritization, never as a program eligibility gate; assess in private,
   once, without making people re-prove homelessness repeatedly.
4. **Prioritization**: publish how referrals are ranked (CoC written standards — commonly highest
   vulnerability and longest homeless time for permanent housing); make sure shelter access is
   never prioritization-gated: anyone gets shelter tonight.
5. **Referrals and queue management**: define who sees the queue, how offers are made, and the
   decline/appeals policy (people can refuse a referral without losing their place in line).
6. **Governance and feedback**: a CE oversight committee including people with lived experience of
   homelessness, a grievance procedure, and an annual data review of access equity.
7. **Compliance wiring**: nondiscrimination, VAWA/confidentiality, limited English proficiency
   access, and equal access regardless of gender identity.

**Done when:** a person with no phone and no ID can still be entered through some access point,
and every requirement above is written into your segment of the CE policies the CoC approved.

## HMIS Basics and Data Quality

- **What goes in**: HUD's HMIS Data Standards define universal data elements (collected on every
   client) plus program-specific elements; bed occupancy data feeds the Housing Inventory Count
   (HIC).
- **Data quality dimensions**: timeliness (entry within the CoC's standard, commonly a few days),
   completeness, accuracy, and consistency (matching pick-lists, no free-text where codes exist).
   Track error rates; clean on a schedule, not just before the annual submission.
- **Privacy**: informed consent at intake (explain what is shared and with whom), user access
   limited by role, and retention long enough to satisfy HUD and your subaward terms (HUD
   recordkeeping rules run years — verify current retention periods rather than assuming your
   general nonprofit file policy suffices).
- **Common report outputs**: point-in-time bed utilization, length of stay, exits to permanent
   housing, and unduplicated counts by household type — these drive both funder reports and your
   own performance review.
- **Practitioner note**: assign data quality to a named HMIS admin with protected weekly review
   time; audit a sample of ten files monthly.
- **Consultant note**: when reviewing a shelter's operations, ask for their data quality scorecard
   and the last monitoring findings before anything else — it reveals how the org actually runs.

## Point-in-Time (PIT) Count Plan

HUD requires each CoC to count sheltered and unsheltered people at least biennially (most do it
annually), on a single night in the last ten days of January, reported through HUD's data exchange;
the results feed the Annual Homeless Assessment Report to Congress and the CoC NOFO scoring. The
sheltered count comes largely from HMIS; the unsheltered count is the operational lift.

### The count plan (the deliverable)

1. **Fix the night**: a January date within the allowed window, chosen with your CoC; recruit
   volunteers (community groups, students, faith partners) starting in November.
2. **Build the canvass map**: known locations from outreach teams, 2-1-1/encampment reports, and
   prior-year maps, plus a plan to cover the rest of the geography (district-based canvassing or,
   where a full canvass is impossible, a documented sampling approach accepted by HUD guidance).
3. **Instrument**: a short survey (where did you sleep last night, household, age, veteran status,
   disability, DV history question where permitted, duration/pattern of homelessness per HUD's
   reporting categories); volunteers never judge who "looks homeless" — they count what the survey
   says.
4. **Train volunteers**: one mandatory session covering survey administration, safety (do not
   wake anyone sleeping to count them — observe respectfully), when to deploy staff instead of
   volunteers, and the script for refusing to answer.
5. **Count night logistics**: check-in/out tracking of volunteers, weather backup decision rule
   made in advance, phone hotline for the public to report locations, deduplication instructions
   (no counting the same person twice; no counting people in cars twice, etc.).
6. **Sheltered side**: verify every shelter, transitional housing, and hotel/motel voucher
   program's occupancy for that exact night — people in RRH or permanent housing are NOT homeless
   and must be excluded.
7. **Reporting**: enter results into HUD's Homelessness Data Exchange by the CoC's deadline and
   hold a debrief to improve next year — keep methodology stable across years so trend lines are
   real.

**Done when:** the methodology section answers who/where/when/how for every segment, the count
compiles within a week of the night, and the CoC's data lead signs off before submission.

## Common Failure Modes

- **Rules creep in shelters** — each well-meaning rule (curfews, chores as conditions, sobriety
  testing) empties beds and keeps people outside. Remedy: audit every rule annually; delete any
  rule you cannot tie to immediate safety.
- **Diversion becomes gatekeeping** — staff pressure people to "self-resolve" or delay shelter
  access to hit a diversion metric. Remedy: diversion is minutes long, unconditional shelter access
  stands, and no diversion quota exists.
- **Coordinated entry run as a screening barrier** — using assessment scores to exclude people
  from services. Remedy: assessment informs prioritization only; publish this in written CE
  policies and train to it.
- **Prevention files that fail monitoring** — income or homelessness-risk documented after the
  fact, or not at all. Remedy: collect eligibility evidence at intake, in the order the ESG
  recordkeeping rules require.
- **Outreach documented nowhere** — people met in encampments become invisible when camps close.
  Remedy: document location and Category 1 status at the point of contact; keep a by-name list.
- **Sweeps without rehousing** — participating in closures with no housing destination. Remedy:
  refuse participation absent a rehousing plan; give notice; work the by-name list first.
- **PIT methodology drift** — new questions, new geography, new night logic, so trends are
  meaningless. Remedy: change one thing at a time and document it in the methodology section.
- **Data quality panic before submissions only** — errors compound all year. Remedy: named HMIS
  admin, weekly error review, monthly ten-file audit.
- **Shelter as permanent residence** — no housing plan started at intake; stays stretch to
  months. Remedy: housing-focused case management with weekly touchpoints from day one; track
  median length of stay as a core metric.
- **Safety theater over real safety** — sign-in sheets and cameras substituting for de-escalation
  training and naloxone. Remedy: budget training and overdose response before security hardware.

For advisors/consultants: the first diagnostic trio is (1) bed utilization rate, (2) median length
of shelter stay, and (3) the last monitoring findings — they expose model problems faster than any
interview tour.
