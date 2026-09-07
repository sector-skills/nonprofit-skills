---
name: nonprofit-donor-crm
description: "Selects and configures a donor CRM/database (e.g., Salesforce Nonprofit Cloud, Bloomerang, Little Green Light, Neon CRM, DonorPerfect, Virtuous), designs data hygiene routines (deduplication, standardized constituent records, data entry policy), and builds list segmentation for mailings and reporting. Use for CRM RFPs/vendor comparison, field mapping and data migration planning, dedup and merge rules, household/soft-credit setup, and saved-segment or query-tag design. Does not cover writing appeal copy or ask strings (nonprofit-annual-appeals), online giving/payment processor setup (nonprofit-digital-fundraising-tools), or donor data privacy/PCI policy (nonprofit-data-privacy)."
license: MIT
---

# Nonprofit Donor CRM

## When to Use This Skill

Use this skill when the request involves the donor database itself as a system: choosing a CRM,
migrating data into one, keeping records clean, or building segments/queries the database will
run. Concrete triggers:

- "Help us pick between Bloomerang, Little Green Light, Neon CRM, DonorPerfect, Virtuous, and
  Salesforce Nonprofit Cloud."
- "Our database has duplicate donor records — how do we de-dupe and prevent it going forward?"
- "We're migrating from spreadsheets/[old CRM] to [new CRM] — what's the field map and cleanup plan?"
- "Build a segment of lapsed donors who gave $250+ in the last 3 years but nothing in the last 12
  months" (the segmentation logic and field design, not the appeal copy sent to that segment).
- "Set up households and soft credit so a couple's joint gifts roll up correctly."
- "Write a data entry policy so every staff member enters gifts the same way."

**Boundary — hand off instead of answering here:**
- Ask strings, segmentation *content*, and appeal calendars → `nonprofit-annual-appeals`.
- Setting up the online donation form, payment gateway, or peer-to-peer platform →
  `nonprofit-digital-fundraising-tools`.
- Data privacy policy, PCI-DSS scope, consent/opt-in language, data-sharing agreements →
  `nonprofit-data-privacy`.
- Moves-management pipeline stages and stewardship workflow *design* → `nonprofit-donor-pipeline`
  (this skill covers the database fields/automation that support that pipeline, not the strategy).

## For Practitioners: Choosing and Running the CRM

### 1. Frame the decision as fit, not features

Nonprofit CRMs cluster into tiers. Match the org to the tier before comparing feature checklists:

- **Entry tier** (under ~$1.5M budget, 1-3 fundraising staff): Little Green Light, Bloomerang,
  DonorPerfect Online. Optimized for low administrative overhead and fast time-to-value.
- **Mid tier** (growing shop, multiple fundraisers, program + development need shared records):
  Neon CRM, Virtuous, Kindful (now part of Bloomerang), DonorPerfect (advanced tier).
  Add-ons for volunteer management, event ticketing, or peer-to-peer often matter here.
  Distinguish this decision (which CRM) from picking the *donation page/payment tool* that plugs
  into it — that comparison belongs to `nonprofit-digital-fundraising-tools`.
- **Enterprise tier** (multi-program, multi-site, complex reporting, often $5M+ budget or a
  dedicated database admin): Salesforce Nonprofit Cloud (built on NPSP or the newer Nonprofit
  Cloud data model), Blackbaud Raiser's Edge NXT. Higher implementation cost and staff time; needs
  a systems admin role, not just a database user.

### 2. Run a structured RFP/comparison, not a demo tour

Standard deliverable: a **CRM comparison matrix** scoring each candidate on:

1. Core gift/constituent data model (does it natively support households, organizations, soft
   credits, matching gifts, recurring gifts, pledges?)
2. Integration ecosystem (email platform, online giving, accounting/QuickBooks sync, wealth
   screening feeds)
3. Reporting/query flexibility (ad hoc report builder vs. requires developer/consultant)
4. Total cost of ownership over 3 years: license + implementation + data migration + training —
   not just sticker price per user/month
5. Data ownership and export rights (can you get a full clean export if you leave?)
6. Vendor support model and average implementation timeline

As an advisor, this matrix — with weighted scoring the client's staff fill in themselves — is the
standard deliverable for a CRM selection engagement; do not just hand over a vendor list.

### 3. Design the data model before migrating

Common failure mode: migrating bad data into a new system just reproduces the mess. Before
migration:

1. **Define the constituent record standard**: individual vs. organization vs. household; one
   record per person, never one record per gift.
2. **Standardize name/address formatting** and pick a single source of truth for each field when
   merging systems (e.g., spreadsheet vs. old CRM vs. mailing list).
3. **Build the field map**: old system field → new system field, flagging fields with no home
   (park them in a custom field rather than dropping data silently).
4. **Set gift-vs-pledge-vs-soft-credit logic** explicitly — this is the most common post-migration
   support ticket (a matching gift or a spouse's gift posted as a duplicate hard credit instead of
   a soft credit).
5. **Run a test migration** on a data subset and have two staff members audit it against source
   records before the full cutover.

### 4. Data hygiene: ongoing, not one-time

- **Deduplication cadence**: run an automated or manual dedup pass at least quarterly; most CRMs
  (Bloomerang, DonorPerfect, Salesforce with NPSP) have a native or app-exchange dedup tool — use
  it rather than building one from scratch.
- **Data entry policy** (standard deliverable, usually 1-2 pages): required fields for every new
  constituent, naming conventions ("Jane Smith" not "jane smith" / "J. Smith"), how to record
  anonymous or in-honor-of gifts, and who has edit vs. view-only permissions.
- **National Change of Address (NCOS)** or mail-service address updates run before every major
  mailing to cut bounce-back costs.
- **Common failure mode**: no designated database owner. Assign one staff member as the CRM
  steward responsible for hygiene standards, even in a one-person development shop.

### 5. Segmentation and reporting setup

- Build **saved segments/smart lists** for recurring uses: current-year donors, lapsed (12/24/36
  month lookback), major gift prospects by giving tier, board members, in-kind donors, grant
  funders (if tracked in the same system).
- Use **tags or custom fields**, not free-text notes, for anything you'll need to query later
  (interest area, event attended, volunteer status).
- Set up a **dashboard** covering: total raised YTD vs. goal, gift count, average gift, donor
  retention rate, new vs. returning donor mix — pull these metrics from the CRM rather than
  rebuilding them in a spreadsheet each month.

## For Advisors: Running a CRM Engagement

1. **Discovery**: audit current system(s), export a data sample, and interview the 2-3 staff who
   touch donor data most to surface workaround habits (shadow spreadsheets are the biggest tell
   that the current system doesn't fit).
2. **Requirements document**: translate discovery into must-have vs. nice-to-have features tied to
   actual workflows (e.g., "gift officer needs mobile access to log a visit note same-day").
3. **Vendor comparison matrix** (above) presented to the client with a recommendation and a 3-year
   TCO estimate, not just a feature grid.
4. **Migration project plan** with a named data owner on the client side — advisors should not be
   the sole holder of migration knowledge; build client capacity during the engagement.
5. **Post-launch check-in at 30/60/90 days**: confirm adoption, not just go-live. The most common
   engagement failure mode is a technically successful migration that staff quietly abandon
   because reports or gift entry got harder, not easier.

## Common Failure Modes

- Choosing a CRM based on price alone and outgrowing it within 18 months.
- No dedup discipline — duplicate records inflate donor counts and produce embarrassing double
  mailings to the same household.
- Migrating without a field map, losing soft-credit and pledge history.
- Treating the CRM selection as an IT decision instead of a fundraising-workflow decision —
  development staff must be in the room for requirements and vendor demos.
- No exit plan: signing a contract without confirming data export rights if the org switches
  vendors later.
