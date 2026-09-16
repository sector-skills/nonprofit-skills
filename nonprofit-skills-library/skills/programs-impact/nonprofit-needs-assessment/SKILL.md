---
name: nonprofit-needs-assessment
description: "Plans and conducts community needs assessments and landscape/gap scans to justify launching, continuing, or discontinuing a nonprofit program, including secondary data review, primary data collection (surveys, focus groups, key informant interviews), asset mapping, and gap analysis against existing providers. Use when a user asks to assess community need before starting a program, prove there is unmet demand for a funder or board, conduct a landscape scan of who else serves this population, run a gap analysis, plan community listening sessions or focus groups, or decide whether to sunset a program because the need has shifted. Covers the pre-program research phase, not the causal design of the program itself once need is established (nonprofit-program-design) and not measuring outcomes once the program is running (nonprofit-outcomes-measurement)."
license: MIT
metadata:
  supervision: "review"
  supervision_note: "Primary data collection involves human participants and consent."
  date_added: "2026-09-07"
  date_added_source: "git:1860ed47a83901ff5e6d45abc4a2ef05be8fd4cd"
---

# Nonprofit Needs Assessment

## When to Use This Skill

Use this skill for research that establishes whether — and what kind of — a community need exists,
before or independent of designing a specific program response. Concrete triggers:

- "We want to start a new program — is there actually demand for it?"
- "The funder wants evidence of need in our proposal."
- "Do a landscape scan: who else in the region serves this population?"
- "Run a gap analysis between what's needed and what's currently provided."
- "Plan community listening sessions / focus groups / key informant interviews."
- "Should we sunset this program? Has the need changed?"
- "Build a community needs assessment report for the board or a funder."

**Boundary — read before starting:**
- Once need is established, building the logic model/theory of change for the program response is
  `nonprofit-program-design` — this skill stops at "here is the documented need and the gap," not
  "here is how the program will address it."
- Tracking whether a running program is achieving outcomes is `nonprofit-outcomes-measurement` — a
  needs assessment is normally a point-in-time (or periodic, e.g., every 3–5 years) study, not an
  ongoing monitoring system.
- If the ask is about assessing a funder or partner's fit rather than a community's need, that is
  `nonprofit-grant-research`, not this skill.

## Core Frameworks

### 1. Needs Assessment Triangulation Model

Credible needs assessments triangulate three data types — do not rely on only one:

1. **Secondary/quantitative data**: existing public data (Census/ACS, county health rankings,
   school district data, CDC/state health department data, HUD point-in-time homelessness counts,
   Bureau of Labor Statistics, 211 call data, existing needs assessments from hospitals/United
   Ways/community foundations that may already cover the geography).
2. **Primary quantitative data**: surveys of the target population or service providers, structured
   to produce comparable numbers (Likert-scale need ratings, service utilization/barriers surveys).
3. **Primary qualitative data**: key informant interviews (service providers, government officials,
   faith/community leaders), focus groups, and community listening sessions/town halls with the
   population itself — essential for capturing lived experience that administrative data misses, and
   for avoiding a needs assessment that speaks *about* a community rather than *with* it.

A needs assessment built on secondary data alone is the most common quality shortfall funders and
evaluators flag — it documents that a problem exists in the abstract but not that this specific
population, in this specific service area, experiences it in a way this organization is positioned
to address.

### 2. Asset Mapping / Landscape Scan

Before concluding a gap exists, map what already serves the population:
- **Provider inventory**: who else offers this or an adjacent service in the geography (name,
  capacity/slots, eligibility criteria, waitlist status, funding source).
- **Community assets, not just deficits**: existing informal supports, cultural/faith institutions,
  natural helpers — an assets-based (vs. purely deficit-based) framing is increasingly expected by
  funders and avoids a report that only catalogs problems.
- **Capacity vs. demand gap**: the actual gap is rarely "no service exists" — more often it's
  insufficient capacity, wrong eligibility criteria, wrong hours/location/language access, or long
  waitlists. Name the *specific* gap type; "duplicative service" is a common and damaging finding if
  the scan is skipped.

### 3. Gap Analysis Structure

State findings as: **Need (documented) → Current capacity (mapped) → Gap (the delta) → Implication
for this organization** (fill gap directly, partner/refer instead of duplicating, or no organizational
role). A needs assessment that stops at documenting need without this last step gives leadership
nothing decision-ready.

## Instructions

1. **Define the population and geography precisely** before collecting anything — "youth in our
   city" is not scoped enough to find or design data collection against; specify age range,
   neighborhood/zip codes, and the specific condition/need domain.
2. **Start with secondary data** to build a baseline picture and identify what's already known —
   check county/city health departments, Census/ACS, school districts, United Way/community
   foundation reports, and 211 data before commissioning any primary research.
3. **Identify the secondary-data gaps** — what the existing data can't tell you (usually: lived
   experience, specific barriers, why people don't access existing services) — and design primary
   data collection specifically to fill those gaps, not to re-confirm what secondary data already
   shows.
4. **Run the landscape/asset scan** in parallel: inventory other providers, their capacity, and
   eligibility/access barriers (cost, hours, language, transportation, documentation status, waitlists).
5. **Design primary data collection instruments** matched to the audience: short structured surveys
   for broad reach/quantifiable ratings; key informant interviews for providers and community
   leaders; focus groups or listening sessions for the population itself, held in accessible
   locations/languages/times and, where appropriate, with compensation for participants' time.
6. **Recruit for representativeness**, not convenience — flag and mitigate selection bias (e.g., only
   surveying people already engaged with the organization systematically overstates satisfaction and
   understates unmet need among the unserved).
7. **Synthesize with the triangulation model**: look for convergence and divergence across secondary
   data, primary quantitative data, and qualitative input — divergence is often the most important
   finding (e.g., data shows a service exists, but the community reports it's inaccessible).
8. **Run the gap analysis**: need → current capacity → the specific gap → organizational implication
   (fill it, refer/partner, or stand down).
9. **Write the needs assessment report** with the standard structure: executive summary, methodology
   (data sources, sample sizes, response rates, limitations), findings by data source, landscape/asset
   map, gap analysis, and recommendations.
10. **Set a revisit cadence** — needs assessments go stale; recommend refreshing every 3–5 years or
    on a major demographic/funding/policy shift, and say so in the report so it isn't treated as a
    one-time artifact.

## Common Failure Modes

- **Secondary-data-only assessments** presented as if they establish local, specific need — funders
  increasingly probe for primary data and community voice.
- **Skipping the landscape scan**, leading to a program proposal that duplicates an existing,
  underused service instead of addressing the real gap (access, capacity, or eligibility).
- **Deficit-only framing** that ignores existing community assets and reads as extractive rather than
  collaborative — increasingly penalized by funders committed to community-centered/equity-based
  grantmaking.
- **Non-representative sampling** — surveying only people already in the organization's database,
  systematically missing the unserved population the assessment is supposed to reach.
- **No compensation or accessibility planning** for community participants (transportation, child
  care, language, timing), which suppresses turnout from exactly the population most affected.
- **Stopping at "need exists"** without a gap analysis or organizational-implication statement,
  leaving the board/funder with a diagnosis but no decision.
- **Treating the assessment as one-and-done** rather than setting a refresh cadence, so program
  decisions rest on years-stale data.

## For Advisors/Consultants

- Scope the engagement explicitly around the triangulation model — clients often request "a needs
  assessment" meaning only a secondary-data literature review; clarify budget/timeline needed to add
  primary qualitative and quantitative components, since this is where most of the client's credibility
  with funders and community stakeholders is actually built.
- When facilitating listening sessions/focus groups for a client, build in a debrief step with the
  client's staff or board on findings that challenge existing assumptions — needs assessments that
  surface uncomfortable findings (e.g., "your flagship program isn't reaching the population with
  greatest need") are the ones most likely to be quietly shelved without a structured decision
  conversation attached.
- Standard advisory deliverable: a needs assessment report (methodology, findings, landscape/asset
  map, gap analysis, recommendations) plus a short board-facing decision memo translating the gap
  analysis into 2–3 concrete organizational options.
- Where the client's real question is "should we keep funding this program," reframe the assessment
  around a sunset/continue/redesign decision explicitly, and hand off a positive continue-and-redesign
  finding to `nonprofit-program-design`.

## Standard Deliverables

- Needs assessment report: executive summary, methodology, findings, landscape/asset map, gap
  analysis, recommendations, limitations
- Data collection instruments (survey, interview guide, focus group protocol)
- Provider/asset inventory table
- Gap analysis summary (need → capacity → gap → implication)
- Board/funder-facing summary memo with a recommended organizational response
