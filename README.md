# Nonprofit Skills

A free, open library of AI agent skills for nonprofit leaders, staff, and consultants — covering
fundraising, finance, governance, programs, communications, advocacy, volunteer/people management,
strategy, and technology. Modeled on [Marketing Skills](https://marketing-skills.com) by Corey
Haines, adapted for the nonprofit sector.

Each skill is a standalone `SKILL.md` file following the open
[Agent Skills spec](https://github.com/coreyhaines31/marketingskills) — drop it into Claude Code,
Codex, Cursor, Perplexity, or any agent that supports the spec, and your agent gains nonprofit
domain expertise it can recognize and apply automatically.

Written for **both** hands-on practitioners (executive directors, development staff, program
managers) and **advisors/consultants** guiding nonprofit clients — most skills call out how the
guidance differs for each.

License: MIT — free to use, copy, modify, and redistribute.

## Install

Copy the `SKILL.md` file(s) you want into your agent's skills folder. For example, for a single
skill:

```
curl -o SKILL.md https://raw.githubusercontent.com/<your-org>/nonprofit-skills/main/nonprofit-skills-library/skills/fundraising-development/nonprofit-grant-writing/SKILL.md
```

Or clone the whole library and point your agent at the `nonprofit-skills-library/skills/` directory.

## Core categories

| Category | Skills |
|---|---|
| [Fundraising & Development](nonprofit-skills-library/skills/fundraising-development) | donor pipeline, major gifts, grant writing, grant research, annual appeals, planned giving, capital campaigns, peer-to-peer fundraising, corporate sponsorships, donor retention, fundraising events |
| [Governance & Compliance](nonprofit-skills-library/skills/governance-compliance) | board governance, bylaws & policy, Form 990, charitable registration, risk management, 501(c)(3)/(c)(4) structure |
| [Finance & Operations](nonprofit-skills-library/skills/finance-operations) | budgeting, financial statements, reserves & cash flow, cost allocation, financial controls, HR, vendor & facilities |
| [Programs & Impact](nonprofit-skills-library/skills/programs-impact) | program design, outcomes measurement, needs assessment, program scaling |
| [Communications & Marketing](nonprofit-skills-library/skills/communications-marketing) | storytelling, annual report, brand messaging, social media, email newsletter, media relations, donation page copy |
| [Advocacy & Public Policy](nonprofit-skills-library/skills/advocacy-policy) | policy analysis, legislative advocacy, coalition building, voter engagement, grassroots mobilization |
| [Volunteer & People](nonprofit-skills-library/skills/volunteer-people) | volunteer management, board recruitment, staff retention, succession planning |
| [Strategy & Growth](nonprofit-skills-library/skills/strategy-growth) | strategic planning, EOS/Traction for nonprofits, revenue diversification, mergers & fiscal sponsorship, change management |
| [Technology & Data](nonprofit-skills-library/skills/technology-data) | donor CRM, data privacy, digital fundraising tools |
| [Executive Leadership](nonprofit-skills-library/skills/executive-leadership) | CEO ↔ board partnership, executive transitions, executive search, executive communications, executive dashboard |

## Special collections

Domain packs built for practitioners in specific audiences and settings — same single-file format, deeper ground.

| Collection | Skills |
|---|---|
| [Faith-Based Organizations](nonprofit-skills-library/skills/faith-based) | church governance, finance & clergy comp, 990 exemption, stewardship & giving, ministerial-exception employment, religious liberty compliance, programs & social services, pastoral communications, lay leadership, facilities & sanctuary |
| [Affordable Housing](nonprofit-skills-library/skills/affordable-housing) | housing continuum planning, homelessness services, rapid rehousing & transitional housing, permanent supportive housing, affordable rental operations, homeownership programs, home repair & preservation, development & finance, LIHTC/HUD compliance, fair housing, land-use advocacy, community ownership, construction volunteers |
| [Community Development Finance](nonprofit-skills-library/skills/community-development-finance) | CDFI finance, NMTC deals, opportunity zones, community facilities finance, disaster recovery finance |
| [Retail & Resale Operations](nonprofit-skills-library/skills/retail-operations) | donation intake & grading, retail pricing & merchandising, retail store operations, online resale, retail staffing, in-kind gift acceptance |
| [Arts & Culture](nonprofit-skills-library/skills/arts-culture) | box office & subscriptions, membership programs, venue rental & earned income, season & production sponsorship, arts grant writing, season & exhibition planning, commissioning & new work, teaching artists & education, performance & music rights, union agreements & artist visas, AD/ED partnership |

## All skills (102)

| Skill | What it's for |
|---|---|
| `nonprofit-donor-pipeline` | Prospect identification through cultivation, solicitation, and stewardship moves-management |
| `nonprofit-major-gifts` | Major/principal gift strategy, ask amounts, proposals, gift agreements |
| `nonprofit-grant-writing` | LOIs and full grant proposals: narratives, budget narratives, evaluation summaries |
| `nonprofit-grant-research` | Funder prospect research, RFP/NOFO tracking, grant calendars |
| `nonprofit-annual-appeals` | Direct-mail/email annual appeal campaigns, segmentation, ask strings |
| `nonprofit-planned-giving` | Bequest and legacy society programs, planned-gift vehicles |
| `nonprofit-capital-campaigns` | Feasibility studies, quiet/public phase planning, gift ranges |
| `nonprofit-peer-to-peer-fundraising` | Walk/run/ride and team-fundraising campaigns |
| `nonprofit-corporate-sponsorships` | Sponsorship packages, pitch decks, renewal strategy |
| `nonprofit-donor-retention` | Thank-you process, donor journey, lapsed-donor win-back |
| `nonprofit-fundraising-events` | Galas, auctions, event budgeting and run-of-show |
| `nonprofit-board-governance` | Board roles, meeting structure, committees, ED-board relationship |
| `nonprofit-bylaws-policy` | Bylaws, conflict-of-interest, whistleblower, retention policy |
| `nonprofit-form-990` | Form 990 variant selection, schedules, governance disclosures |
| `nonprofit-charitable-registration` | Multi-state charitable solicitation registration |
| `nonprofit-risk-management` | Insurance review, liability mapping, crisis/safeguarding policy |
| `nonprofit-c3-c4-structure` | Dual 501(c)(3)/(c)(4) structuring, lobbying limits |
| `nonprofit-budgeting` | Annual operating budget build, functional allocation |
| `nonprofit-financial-statements` | Statement of activities/position, functional expense allocation |
| `nonprofit-reserves-cash-flow` | Reserve policy, cash flow forecasting |
| `nonprofit-cost-allocation` | Indirect cost rate, true-cost-of-program analysis |
| `nonprofit-financial-controls` | Internal controls, audit preparation |
| `nonprofit-hr` | Hiring, compensation benchmarking, personnel policy |
| `nonprofit-vendor-facilities` | Vendor contracts, procurement, facilities management |
| `nonprofit-program-design` | Logic models, theory of change |
| `nonprofit-outcomes-measurement` | KPI design, evaluation plans, outcomes reporting |
| `nonprofit-needs-assessment` | Community needs assessments, landscape/gap scans |
| `nonprofit-program-scaling` | Scaling/replication readiness, fidelity vs. adaptation |
| `nonprofit-storytelling` | Case for support, dignity-centered beneficiary storytelling |
| `nonprofit-annual-report` | Annual report structure and content planning |
| `nonprofit-brand-messaging` | Brand voice, positioning, messaging house |
| `nonprofit-social-media` | Social content calendars and platform strategy |
| `nonprofit-email-newsletter` | E-newsletter strategy and structure |
| `nonprofit-media-relations` | Press releases, media pitching, spokesperson prep |
| `nonprofit-donation-page-copy` | Donation page copy and conversion optimization |
| `nonprofit-policy-analysis` | Issue briefs and policy position papers |
| `nonprofit-legislative-advocacy` | Legislator meetings, lobby days, testimony |
| `nonprofit-coalition-building` | Multi-org advocacy coalition governance |
| `nonprofit-voter-engagement` | Nonpartisan voter registration and GOTV |
| `nonprofit-grassroots-mobilization` | Action alerts, petitions, supporter activation |
| `nonprofit-volunteer-management` | Volunteer recruitment, onboarding, retention |
| `nonprofit-board-recruitment` | Board skills matrix, recruitment, onboarding |
| `nonprofit-staff-retention` | Staff culture, burnout, retention practices |
| `nonprofit-succession-planning` | ED transition planning, leadership pipeline |
| `nonprofit-strategic-planning` | End-to-end strategic planning process |
| `nonprofit-eos-traction` | EOS/Traction operating system for nonprofits |
| `nonprofit-revenue-diversification` | Earned income, social enterprise, revenue mix |
| `nonprofit-mergers-fiscal-sponsorship` | Merger feasibility, fiscal sponsorship structuring |
| `nonprofit-change-management` | Leadership transitions, mergers, restructuring |
| `nonprofit-donor-crm` | CRM selection/configuration, data hygiene |
| `nonprofit-data-privacy` | Donor data privacy, PCI compliance |
| `nonprofit-digital-fundraising-tools` | Online giving platforms, payment processors |
| `nonprofit-ceo-board-partnership` | CEO's side of the board relationship: board reports, exec-session prep, chair 1:1s, CEO evaluation |
| `nonprofit-executive-transitions` | Incoming/outgoing/interim ED transitions: 90-day plans, listening tours, handoff memos |
| `nonprofit-executive-search` | Board-run ED/CEO/C-suite hiring: charter, position profile, comp benchmarking, structured interviews |
| `nonprofit-executive-communications` | First-person CEO/ED messages: all-staff, crisis/RIF, funder letters, town halls, culture notes |
| `nonprofit-executive-dashboard` | ED/COO one-page KPI dashboard and board scorecard: metric selection, thresholds, review rhythm |
| `nonprofit-donation-intake-grading` | Donated-goods drop-off/pickup, sorting, sell/recycle/discard triage |
| `nonprofit-retail-pricing-merchandising` | Pricing used goods, store floor layout, seasonal merchandising |
| `nonprofit-retail-store-operations` | POS/inventory, cash handling, loss prevention, open/close procedures |
| `nonprofit-online-resale` | ShopGoodwill/eBay-style listings, photography, shipping |
| `nonprofit-retail-staffing` | Paid+volunteer retail shift scheduling and floor training |
| `nonprofit-in-kind-gift-acceptance` | Form 8283, qualified appraisals, gift acceptance policy |
| `nonprofit-faith-990-exemption` | Church/synagogue/mosque tax status: automatic 501(c)(3) exemption, 990 filing exemption, §7611 audit protections |
| `nonprofit-faith-church-governance` | Worship-community polity: bylaws, congregational meetings, elder/vestry/shura structures, pastor call and separation |
| `nonprofit-faith-finance-clergy-comp` | Clergy pay and church finance: §107 housing allowance, SECA, love offerings, accountable plans, §4958, 403(b) |
| `nonprofit-faith-stewardship-giving` | Congregational stewardship: pledge campaigns, tithe/zakat messaging, worship-building capital campaigns, §6115 rules |
| `nonprofit-faith-employment-ministerial-exception` | Ministerial exception, §702 religious hiring, clergy misconduct and safe-sanctuary employment policy |
| `nonprofit-faith-religious-liberty-compliance` | RFRA/RLUIPA, religious hiring rights, free-exercise framework for faith-based nonprofits |
| `nonprofit-faith-programs-social-services` | Faith-based food pantry, recovery, re-entry, shelter, and resettlement programs under Charitable Choice rules |
| `nonprofit-faith-communications-pastoral` | Pastoral voice: letters, funeral/crisis notices, misconduct responses, farewell/arrival messages |
| `nonprofit-faith-volunteer-lay-leadership` | Deacon/elder/warden/trustee recruitment and formation, lay-leader burnout and sabbaticals |
| `nonprofit-faith-facilities-sanctuary` | Worship-building operations: property-tax exemption, RLUIPA zoning, facility-use policies, rental UBIT |
| `nonprofit-housing-continuum-planning` | Map the community housing continuum, AMI-band gap analysis, where-we-play portfolio decisions |
| `nonprofit-housing-homelessness-services` | Street outreach, emergency shelter, diversion/prevention, coordinated entry, HMIS, PIT counts |
| `nonprofit-housing-rapid-rehousing-transitional` | Rapid rehousing and transitional housing program design under CoC/ESG rules, landlord engagement |
| `nonprofit-housing-permanent-supportive-housing` | PSH design, Housing First fidelity, staffing models, retention, braided funding |
| `nonprofit-housing-affordable-rental-operations` | Tenant selection plans, income certs, rent setting, waitlists, property vs. asset management |
| `nonprofit-housing-homeownership-programs` | Homebuyer selection, sweat equity, below-market financing, post-purchase support, resale formulas |
| `nonprofit-housing-repair-preservation` | Critical home repair, weatherization, aging-in-place, lead-safe work, NOAH preservation |
| `nonprofit-housing-development-finance` | Site control, entitlements, pro formas, LIHTC/HOME/bond capital stacks, construction oversight |
| `nonprofit-housing-lihtc-hud-compliance` | Section 42 certifications, income/rent limits, monitoring-visit prep, tenant file readiness |
| `nonprofit-housing-fair-housing` | FHA, 504/ADA, reasonable accommodation, screening policy review, complaint response |
| `nonprofit-housing-advocacy-land-use` | Zoning reform, hearing testimony, NIMBY response, housing ballot measures, lobbying limits |
| `nonprofit-housing-community-ownership` | Community land trusts, limited-equity co-ops, shared-equity resale formulas, stewardship |
| `nonprofit-housing-construction-volunteers` | Build-season scheduling, crew-leader development, jobsite safety, AmeriCorps deployment |
| `nonprofit-cdfi-finance` | CDFI lenders and deal partners, Treasury CDFI Fund awards, nonprofit CDFI certification |
| `nonprofit-nmtc-deals` | New Markets Tax Credit deals: CDE allocations, structuring, 7-year compliance, LIHTC layering |
| `nonprofit-opportunity-zones` | QOF/QOZB structuring, current-law mechanics, nonprofit roles, community-benefit covenants |
| `nonprofit-community-facilities-finance` | Capital stacks for health centers, child care, charter schools, food retail: USDA CF, bonds, layering |
| `nonprofit-disaster-recovery-finance` | FEMA PA for nonprofits, SBA disaster loans, CDBG-DR/MIT, rebuild capital stacks |
| `nonprofit-arts-box-office-subscriptions` | Ticketing platforms and fee models, subscription packages, dynamic pricing, group sales, subscriber renewal economics |
| `nonprofit-arts-membership-program` | Member tiers and benefits, pricing, renewal campaigns, subscriber→member→donor ladder, token-benefit substantiation |
| `nonprofit-arts-venue-rental-earned-income` | Hall/gallery/studio rental programs, rental agreements and COI/liquor terms, ancillary earned lines, rental UBIT basics |
| `nonprofit-arts-season-sponsorship` | Season/production/exhibition underwriting packages, sponsor benefits matrices, in-kind valuation, renewal reporting |
| `nonprofit-arts-grant-writing` | NEA Grants for Arts Projects, state arts agencies, arts foundations: panel scoring, 1:1 cost share, grants management |
| `nonprofit-arts-season-planning` | Annual programming cycles, selection scorecards, rights and exhibition lead times, per-title cost estimating, extension math |
| `nonprofit-arts-commissioning-new-work` | Commission agreement anatomy, IP ownership and options, development pipelines, co-commissioning, gallery consignment |
| `nonprofit-arts-education-programs` | Teaching-artist rosters and classification, district partnerships, student matinees, youth safety, standards alignment |
| `nonprofit-arts-performance-licensing` | Grand vs small rights, play/musical licensing houses, PRO blankets, streaming/archival rights, film screening licenses |
| `nonprofit-arts-union-agreements-visas` | AEA/IATSE/AFM/SAG-AFTRA basics, guest-artist contracts, O-1/P visas, foreign-artist 30% withholding and CWAs |
| `nonprofit-arts-ad-ed-partnership` | AD/ED decision rights, the board's artistic mandate, tension patterns and repairs, dual-model succession |

## Contributing

This library is designed to grow. New skills should follow the same format: a single `SKILL.md`
with quoted YAML frontmatter (`name`, `description`, `license: MIT`, `last_reviewed: YYYY-MM-DD`),
a description with concrete trigger phrases and an explicit boundary line against overlapping
sibling skills, and a body full of named frameworks, standard deliverables, numbered steps, and
common failure modes — not generic advice a model already knows.

Minimal frontmatter template:

```yaml
---
name: nonprofit-example-skill
description: "One paragraph. What it does, when to use it, and an explicit boundary line against overlapping sibling skills."
license: MIT
last_reviewed: 2026-09-07
supervision: review
supervision_note: "One line on why this level, in terms of what a wrong output costs."
---
```

## Supervision level

Not every skill carries the same risk. A draft thank-you letter that comes out wrong costs an
edit. A Form 990 or a set of bylaws that comes out wrong is filed with the IRS or binds the
organization — and the person running the agent is often the least equipped to notice.

`supervision:` records that difference in the frontmatter, so an agent, a CI job, or a human
browsing the library can see it *before* the output is used.

| Level | Meaning |
|---|---|
| `unsupervised` | Usable with ordinary editing. A mistake costs time, not much else. |
| `review` | A knowledgeable staff member must read it before it is used or circulated. Consequential internally, but nothing is filed externally. |
| `expert-required` | Must be reviewed by a credentialed professional (attorney, CPA, licensed auditor) before it is filed, adopted, or relied on. |

The dividing line for `expert-required` is deliberately narrow: the output goes to an outside
authority, or it legally binds the organization. That keeps the label meaningful — if most
skills carry it, none of them do.

To see which skills declare a level:

```
python3 nonprofit-skills-library/scripts/check_supervision.py         # list skills missing the field
python3 nonprofit-skills-library/scripts/check_supervision.py --all   # show every skill with its level
python3 nonprofit-skills-library/scripts/check_supervision.py --json  # machine-readable output
```

The script exits non-zero only when a skill declares a level outside the three above. Missing
fields are reported but do not fail, so new skills can be added before their level is settled.

All 63 skills currently declare a level: **7 unsupervised, 38 review, 18 expert-required**. The
`expert-required` set is deliberately small and shares one test — a credentialed professional
(attorney, CPA, licensed auditor) is genuinely needed, not merely advisable. It covers Form 990
and charitable registration, bylaws and entity structure, audited statements, indirect cost rates
under 2 CFR 200, FLSA classification, binding contracts and leases, gift instruments and named
gifts, IRS Form 8283 appraisals, 501(h) lobbying limits, electioneering rules, executive
compensation, merger and fiscal-sponsorship structures, unrelated business income, and data
privacy obligations.

## Maintenance & review cadence

Skills stay useful only if they're maintained. This library commits to a predictable rhythm:

- **Quarterly light touch** — broken links, outdated tool names, deprecated regulations. Extra
  attention to fast-moving areas: AI tools, IRS/990 rules, grant platforms, fundraising tech.
- **Semi-annual category sweep** — rotate categories so every one is reviewed at least once a
  year. Test prompts against current models; refresh examples, sample outputs, and any embedded
  benchmarks.
- **Annual full-library audit** — re-evaluate the 10-category taxonomy for gaps or overlaps,
  retire or merge low-use or overlapping skills, publish a changelog.
- **Event-triggered updates** — major IRS/state regulatory changes, significant sector-standard
  shifts (e.g. new BoardSource frameworks), material AI model releases. Community pull requests
  and issues get a two-week response target.

Every `SKILL.md` carries a `last_reviewed: YYYY-MM-DD` field. To see which skills are overdue:

```
python3 nonprofit-skills-library/scripts/check_review_status.py         # list overdue skills
python3 nonprofit-skills-library/scripts/check_review_status.py --all   # show every skill with its status
python3 nonprofit-skills-library/scripts/check_review_status.py --json  # machine-readable output
```

Fast-moving categories (`fundraising-development`, `governance-compliance`, `technology-data`)
use a 90-day review interval; all others use 365 days. The script exits non-zero when anything
is overdue, so it can gate CI merges.
