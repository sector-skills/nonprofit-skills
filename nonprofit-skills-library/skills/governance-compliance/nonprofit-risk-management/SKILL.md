---
name: nonprofit-risk-management
description: "Runs enterprise risk assessment and mitigation for nonprofits: insurance coverage review (general liability, D&O, professional liability, property, cyber, abuse/molestation), liability exposure mapping, crisis response and business continuity policy, and safeguarding/incident policy design for programs serving minors or vulnerable adults. Use when asked to conduct a risk assessment, review an insurance policy or coverage gaps, design a crisis communications/response plan, write an incident reporting and safeguarding policy, run background-check/screening protocols for staff or volunteers working with vulnerable populations, or build a business continuity/disaster recovery plan. Does not cover internal financial controls or fraud prevention (use nonprofit-financial-controls), data privacy/cybersecurity policy for donor data specifically (use nonprofit-data-privacy), or volunteer recruitment/onboarding mechanics generally (use nonprofit-volunteer-management)."
license: MIT
---

# Nonprofit Risk Management

## When to Use This Skill

Use this skill for organization-wide risk identification, insurance, crisis response, and
safeguarding policy. Trigger tasks include: "do a risk assessment for our organization," "review our
insurance policy — are we covered for X," "we run programs for kids — what safeguarding policy do we
need," "write a crisis communications plan for [an incident]," "design an incident reporting
procedure," "what background-check protocol should volunteers working with minors go through," or
"build a business continuity plan in case we lose our building/ED/key system."

Boundary: this skill covers physical, reputational, program-safety, and insurable risk. Internal
financial controls and fraud/segregation-of-duties design are `nonprofit-financial-controls`. Donor
data privacy, PCI compliance, and data-sharing policy specifically are `nonprofit-data-privacy`.
Volunteer recruitment and general onboarding mechanics are `nonprofit-volunteer-management` (this
skill's screening protocols feed into, but don't replace, that onboarding process).

## Core Framework: Enterprise Risk Management (ERM) for Nonprofits

Move beyond ad hoc "what could go wrong" brainstorming to a structured **risk register**:

1. **Identify** risks across categories: programmatic (harm to a client/beneficiary), financial
   (fraud, loss of major funding), operational (loss of facility, key-person dependency), reputational
   (media/PR crisis, social media incident), compliance/legal (regulatory violation, employment
   claim), and governance (board dysfunction, ED departure without succession plan — see
   `nonprofit-succession-planning`).
2. **Assess** each identified risk on two axes: **likelihood** (rare/unlikely/possible/likely/almost
   certain) and **impact** (insignificant/minor/moderate/major/catastrophic) — plot on a 5x5 heat map
   to prioritize, rather than treating every risk as equally urgent.
3. **Mitigate** each high-priority risk with a named strategy: **avoid** (stop the activity),
   **reduce** (add controls/training), **transfer** (insurance, contractual indemnification/waivers),
   or **accept** (document the decision to retain the risk, usually for low-impact/low-likelihood
   items only).
4. **Assign ownership and review cadence** — a risk register with no named owner per risk and no
   review schedule (recommended: at least annually, presented to the board or a risk/audit committee)
   becomes a static document nobody revisits until after an incident occurs.
5. **Standard deliverable**: a risk register (spreadsheet or table) with columns for risk
   description, category, likelihood, impact, mitigation strategy, owner, status, and last-reviewed
   date.

## Insurance Coverage Review

Map coverage against the risk register rather than reviewing policies in isolation. Core policy
types and what each actually covers:

- **General Liability (GL)** — third-party bodily injury/property damage claims (e.g., a visitor
  slips at an event); baseline coverage almost every nonprofit needs, but does not cover professional
  errors or abuse claims — those need separate riders/policies below.
- **Directors & Officers (D&O)** — covers board/officer decisions and governance-related claims
  (e.g., wrongful termination allegations against the ED, a disgruntled former board member suing
  over a removal); pairs with the bylaws indemnification clause (`nonprofit-bylaws-policy`) —
  indemnification without D&O insurance behind it is a hollow protection if the organization lacks
  funds to actually cover a claim.
- **Professional Liability / Errors & Omissions (E&O)** — covers claims arising from the
  professional service itself (e.g., a counseling nonprofit's clinical advice, a legal-aid org's
  representation) — essential for any organization providing licensed or quasi-professional services,
  not covered by GL.
- **Abuse/Molestation Coverage** — a distinct rider or policy, NOT automatically included in GL or
  even umbrella policies — mandatory to explicitly confirm for any organization serving minors,
  elderly, or vulnerable adults (youth programs, camps, mentoring, disability services, some
  faith-based programs); a shockingly common gap is assuming GL covers this when the policy
  explicitly excludes it.
- **Property insurance** — building, equipment, and contents; confirm whether the policy covers
  replacement cost vs. actual cash value (depreciated), and whether it's adequate for owned vs.
  leased space (see `nonprofit-vendor-facilities` for the lease-side obligations).
- **Cyber liability** — data breach response costs, ransomware, and business interruption from a
  cyber incident; increasingly necessary given donor/client PII exposure (coordinate with
  `nonprofit-data-privacy` on the underlying data practices this insures against).
- **Umbrella/excess liability** — extends limits above the underlying GL/auto/D&O policies for
  catastrophic claims; cost-effective way to raise total coverage without buying up every underlying
  policy's limit individually.
- **Volunteer accident/workers' comp considerations** — confirm whether volunteers are covered under
  GL, a separate volunteer accident policy, or excluded entirely; paid staff need workers'
  compensation per state law regardless of nonprofit status.

### Insurance Review Checklist

1. Pull the full list of current policies and their declarations pages (coverage limits,
   deductibles, exclusions).
2. Cross-walk against the risk register — for every "transfer via insurance" mitigation, confirm an
   actual policy covers it (not assumed).
3. Check named-insured accuracy — related entities (a supporting 501(c)(4), a fiscal-sponsored
   project) may not be automatically covered under the parent's policy unless specifically named
   (see `nonprofit-c3-c4-structure` and `nonprofit-mergers-fiscal-sponsorship`).
4. Review exclusions closely, especially abuse/molestation carve-outs and any communicable-disease
   or pandemic exclusions added since 2020.
5. Benchmark limits against peer organizations of similar size/activity via a broker who specializes
   in nonprofit coverage, not a generalist commercial broker.
6. Set an annual renewal review on the calendar, not just an auto-renewal default.

## Safeguarding and Incident Policy (Programs Serving Minors/Vulnerable Adults)

1. **Screening protocol**: criminal background checks (and, where relevant, sex-offender registry
   checks and reference checks) for every staff member and volunteer with unsupervised access to
   minors/vulnerable adults, re-run on a periodic cycle (commonly every 1-3 years), not just at hire.
2. **Two-adult rule / no-unsupervised-contact policy**: require two screened adults present for
   activities with minors, and prohibit one-on-one unsupervised contact (including electronic/social
   media contact) as a structural control, not a trust-based one.
3. **Mandatory reporting training**: train all staff/volunteers on state mandatory-reporter
   obligations for suspected abuse/neglect, including exact reporting channel and timeline (varies by
   state — confirm current law rather than assuming a uniform national rule).
4. **Incident reporting procedure**: a written, simple process any staff/volunteer/participant can use
   to report a concern, naming who receives reports (should include a channel outside the normal
   chain of command, mirroring the whistleblower channel design in `nonprofit-bylaws-policy`), the
   required response timeline, and escalation to law enforcement/child protective services where
   legally required.
5. **Board/ED notification protocol**: define which incident severities require immediate ED
   notification vs. board notification vs. legal counsel engagement — a common failure mode is an
   incident that should have reached the board getting stuck at the program-manager level.

## Crisis Response and Business Continuity

1. **Crisis response plan** structure: activation trigger (what counts as a crisis), a named crisis
   team with backup designees (not just one person who might be unreachable), a communications
   protocol (internal staff/board notification before external statements), designated spokesperson,
   and a decision log kept during the event.
2. **Draft holding statements in advance** for foreseeable scenarios (safety incident, financial
   scandal, natural disaster affecting facility/clients) so the first public response doesn't have to
   be composed from scratch under pressure — coordinate with `nonprofit-media-relations` for
   execution mechanics once a statement is needed.
3. **Business continuity/disaster recovery plan**: identify single points of failure (one person who
   knows the payroll system, one physical location for all records) and mitigate — offsite/cloud
   backup of critical records, a documented emergency operating procedure if the primary facility is
   unusable, and a named line of authority succession if the ED is suddenly unavailable (full
   leadership pipeline planning is `nonprofit-succession-planning`; this skill covers the emergency-
   authority stopgap specifically).
4. **Test the plan** — a tabletop exercise annually with the crisis team walking through a realistic
   scenario surfaces gaps a written plan alone won't reveal.

## Standard Deliverables

- Risk register (categorized, scored, mitigation-assigned, owned)
- Insurance coverage cross-walk against the risk register with gap list
- Safeguarding policy (screening protocol, two-adult rule, mandatory reporting training plan)
- Incident reporting procedure with escalation thresholds
- Crisis response plan with holding statements
- Business continuity/disaster recovery plan

## Practitioner vs. Advisor Framing

- **As the ED or operations lead**, start from the risk register, not the insurance policy — buying
  more coverage without first identifying what's actually exposed wastes budget on the wrong lines
  and leaves real gaps (most commonly abuse/molestation coverage) unaddressed; run the tabletop
  crisis exercise before an actual crisis, not after.
- **As an advisor**, use the insurance-coverage cross-walk as a fast, concrete diagnostic to open a
  broader risk conversation with a client board — a missing abuse/molestation rider or an unnamed
  related entity on a D&O policy are specific, credible findings that build trust for a deeper
  engagement, more effective than a generic "you should manage risk better" recommendation.
