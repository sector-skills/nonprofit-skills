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
curl -o SKILL.md https://raw.githubusercontent.com/<your-org>/nonprofit-skills/main/skills/fundraising-development/nonprofit-grant-writing/SKILL.md
```

Or clone the whole library and point your agent at the `skills/` directory.

## Categories

| Category | Skills |
|---|---|
| [Fundraising & Development](skills/fundraising-development) | donor pipeline, major gifts, grant writing, grant research, annual appeals, planned giving, capital campaigns, peer-to-peer fundraising, corporate sponsorships, donor retention, fundraising events |
| [Governance & Compliance](skills/governance-compliance) | board governance, bylaws & policy, Form 990, charitable registration, risk management, 501(c)(3)/(c)(4) structure |
| [Finance & Operations](skills/finance-operations) | budgeting, financial statements, reserves & cash flow, cost allocation, financial controls, HR, vendor & facilities |
| [Programs & Impact](skills/programs-impact) | program design, outcomes measurement, needs assessment, program scaling |
| [Communications & Marketing](skills/communications-marketing) | storytelling, annual report, brand messaging, social media, email newsletter, media relations, donation page copy |
| [Advocacy & Public Policy](skills/advocacy-policy) | policy analysis, legislative advocacy, coalition building, voter engagement, grassroots mobilization |
| [Volunteer & People](skills/volunteer-people) | volunteer management, board recruitment, staff retention, succession planning |
| [Strategy & Growth](skills/strategy-growth) | strategic planning, EOS/Traction for nonprofits, revenue diversification, mergers & fiscal sponsorship, change management |
| [Technology & Data](skills/technology-data) | donor CRM, data privacy, digital fundraising tools |
| [Retail & Resale Operations](skills/retail-operations) | donation intake & grading, retail pricing & merchandising, retail store operations, online resale, retail staffing, in-kind gift acceptance |
| [Executive Leadership](skills/executive-leadership) | CEO ↔ board partnership, executive transitions, executive search, executive communications, executive dashboard |

## All skills (63)

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
---
```

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
python3 scripts/check_review_status.py         # list overdue skills
python3 scripts/check_review_status.py --all   # show every skill with its status
python3 scripts/check_review_status.py --json  # machine-readable output
```

Fast-moving categories (`fundraising-development`, `governance-compliance`, `technology-data`)
use a 90-day review interval; all others use 365 days. The script exits non-zero when anything
is overdue, so it can gate CI merges.
