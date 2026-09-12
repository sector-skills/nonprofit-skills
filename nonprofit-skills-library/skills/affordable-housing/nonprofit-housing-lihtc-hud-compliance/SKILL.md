---
name: nonprofit-housing-lihtc-hud-compliance
description: "Compliance operating system for LIHTC (Section 42) and HUD-assisted affordable housing: income and rent limits, gross rent and utility allowances, tenant certifications, student and unit rules, credit recapture triggers, HOME/ESG/CoC/HCV monitoring, tenant file audits, and MOR/state HFA monitoring-visit prep, with a file-readiness checklist, findings-and-remedies list, and annual compliance calendar. Use when a user says 'our state HFA monitoring visit is next month', 'what counts as gross rent under Section 42', 'we missed an annual recertification', 'the agency filed a Form 8823 on us', or 'help us get tenant files audit-ready'. Not for day-to-day property management, tenant selection, or rent-setting operations (use nonprofit-housing-affordable-rental-operations), fair-housing complaints or reasonable accommodation disputes (use nonprofit-housing-fair-housing), or deal structuring and capital-stack design before close (use nonprofit-housing-development-finance)."
license: MIT
supervision: expert-required
supervision_note: "Certifications are filed with state HFAs and the IRS and errors trigger credit recapture; every compliance filing needs attorney or CPA review before submission."
last_reviewed: 2026-09-12
---

# LIHTC and HUD Program Compliance

## When to Use This Skill

Use this skill when a user asks you to do any of these:

- "We have a state HFA monitoring visit in six weeks — how do we prepare?"
- "What counts as gross rent under Section 42? Do pet fees count?"
- "We missed an annual recertification deadline — what's our exposure?"
- "The agency sent a Form 8823 with noncompliance codes — how do we respond and cure?"
- "A tenant's income went over 140% at recert — do we have to evict or raise rent?"
- "Our tenant's a full-time student — is the unit still qualified?"
- "Help me build a tenant file checklist and a compliance calendar."
- "We just layered HOME funds onto a LIHTC deal — what extra rules apply?"
- "HUD's contract administrator scheduled a Management and Occupancy Review."
- "How do we avoid credit recapture when we sell in year eight?"

This skill is for owners, asset managers, compliance staff, and consultants at nonprofit owners of
affordable rental housing. Practitioners run these checklists against live portfolios; advisors
should use them to structure a mock audit, remediation plan, or monitoring-response engagement.

**Boundary:** This skill covers program compliance, monitoring, and file-readiness only. Route
day-to-day property management — tenant selection plans, waitlists, rent collection, staffing,
turnovers — to `nonprofit-housing-affordable-rental-operations`. Route fair-housing allegations,
reasonable accommodation/modification disputes, disparate-impact analysis, and LEP compliance to
`nonprofit-housing-fair-housing`. Route deal structuring before close — pro formas, capital-stack
design, LIHTC equity negotiation, site control — to `nonprofit-housing-development-finance`.

## The Compliance Landscape

Know which regulator owns which risk; every deliverable here maps to one of these:

| Program | Governing law | Regulator | Core filings | What bites |
|---|---|---|---|---|
| LIHTC | IRC Section 42 | State HFA + IRS | Form 8609 (per building), annual owner certification, state compliance reports | Form 8823 → credit recapture or credit disallowance |
| HOME | 24 CFR Part 92 | Participating jurisdiction (city/county/state) | Annual owner certification, IDIS draws, rent/income compliance | Repayment of HOME funds, unit disallowance |
| ESG | 24 CFR Part 576 | Local grantee / state | ESG CAPER, monthly expenditure reports, HMIS data | Repayment, suspension of future grants |
| CoC | 24 CFR Part 578 | CoC Collaborative Applicant / HUD | APR, HMIS data quality, subrecipient monitoring | Grant termination, competition penalties |
| HCV / PBV | 24 CFR Parts 982–983 | Local PHA | Reexaminations, HQS/NSPIRE inspections, HAP contracts | Abatement of HAP, contract termination |
| HUD multifamily (PBRA/RAD) | 24 CFR and handbooks | HUD / contract administrator | TRACS certifications (50059s), MOR responses, NSPIRE inspections | Findings, HAP adjustments, subsidy repayment |

Layered deals are the norm: a typical nonprofit deal carries LIHTC + HOME + a state soft loan, and
possibly a PBV or rental-assistance contract. When programs overlap on one unit, apply the strictest
applicable rule for each dimension (income limit, rent limit, recert frequency, file documentation).
Never assume one program's certification satisfies another's.

## Section 42 Essentials

### Minimum set-aside and average income minimum

- The building must satisfy one of the minimum set-asides elected at allocation: 20% of units at or
  below 50% AMI, 40% at or below 60% AMI, or the average income minimum. The set-aside is
  building-level and tested continuously, not just at year end.
- Under the average income minimum, units may be designated at AMI levels between 20% and 80% in 10%
  increments, averaging at or below 60%, with each unit tested against its own designation. Follow
  the IRS regulations current for your allocation year — averaging methodology (including rounding)
  was contested in proposed regulations and later guidance; use your state HFA's interpretation,
  which controls in practice.
- The set-aside must be met by the end of the first year of the credit period and maintained
  throughout the 15-year compliance period. If it fails, credits are disallowed prospectively until
  cured, and prior credits may be recaptured.

### Income and rent limits

- Use the HUD Multifamily Tax Subsidy Projects (MTSP) income limits — not standard Section 8 limits —
  for LIHTC properties. They are published annually, typically in spring, generally effective 30 days
  after publication, and held harmless against declines at the area level: limits can plateau but not
  drop.
- Limits are household-size-specific; a unit's rent limit is keyed to the income limit for its
  designated AMI percentage and bedroom size (a statutory household-size assumption of roughly 1.5
  persons per bedroom). Always use the HFA's published rent-limit tables rather than computing from
  scratch — state agreements may impose stricter limits.
- Apply new limits to new move-in certifications and, per most HFA rules, at the next annual
  recertification; existing rents do not float up mid-lease. If rent exceeds a newly effective limit
  at recert, restrict it to the new limit.

### Gross rent

Gross rent = rent charged (including mandatory charges) plus the utility allowance. Get these right:

- **Include mandatory fees.** Any charge required as a condition of occupancy is rent: mandatory pet
  fees, required garage/storage charges, mandatory cable, internet, or service packages, mandatory
  RUBS utility charges. Optional services the tenant could decline are excluded.
- **Utility allowances.** Subtract the applicable allowance (PHA schedule, or engineered/consumer
  approach where the HFA permits). Update allowances on the HFA's schedule — commonly annually — and
  apply at the next lease or renewal per state rules. A stale allowance silently pushes gross rent
  over the limit; it is one of the most common findings.
- **Gross rent floor.** In low-income areas the statutory floor can exceed the
  30%-of-imputed-income calculation. The HFA's tables bake this in — use them.
- Test gross rent at move-in and every certification. Charging even a few dollars over the limit
  makes the unit noncompliant for the whole period — the test is pass/fail, not materiality-based.

### Tenant certifications

- **Initial certification at move-in:** complete before or on the lease effective date. The
  household's income must be at or below the applicable limit as of move-in. An uncertified or late
  move-in cert can cost the unit's credit for the entire year.
- **Annual recertification:** complete annually, effective within 12 months of the prior
  certification's effective date (many HFAs require effective dates within 120 days of the
  anniversary). Third-party verification of income and assets is required — self-certification alone
  does not support a LIHTC cert except where rules expressly permit (e.g., certain asset amounts
  under HOTMA-derived rules). Missed or late recerts are reportable noncompliance even if the
  household would have qualified.
- **Verification hierarchy:** third-party written verification first; then source documents (pay
  stubs, award letters, bank statements); oral third-party verification with a dated note;
  self-certification last and only where rules permit. Document the method used for each source.
- Certifications must be signed and dated by tenant and owner/agent, dated in logical order
  (verifications obtained before the cert is signed), and internally consistent. Auditors read files
  for contradictions before anything else.

### Student eligibility

A household is ineligible if it consists entirely of full-time students. A part-time student, a
household with one non-student member, or a household meeting a statutory exception is fine.
Exceptions include: a household receiving TANF or similar state assistance; a student in a state
job-training assistance program; a single parent with minor children who is not a dependent of
another taxpayer and does not live with someone who could claim them; married students entitled to
file a joint return; and a household including a person who was in foster care or received
foster-care assistance in the prior six months. Document student status, including mid-year changes
— tenants turning full-time mid-tenancy is a recurring hidden finding.

### The 140% / next available unit rule

When a household's income rises above 140% of the current income limit at annual recert (and was
income-qualified at move-in), the tenant is **over-income but not out of compliance**. Do not evict
and do not raise rent above the limit. The unit's status depends on the **next available unit rule**:
the next comparable or smaller unit that becomes vacant must be rented to a qualified low-income
household at a restricted rent before any unit of that size or larger goes to a non-qualifying
household. If a comparable or larger unit is rented to an over-income household first, the original
unit permanently loses qualified status. Track over-income flags in the rent roll and enforce the
rule in the leasing queue.

### The vacant unit rule

If a qualified unit becomes vacant, the owner may continue claiming credit if (a) reasonable
attempts were made to rent it and (b) the rent during vacancy does not exceed the restriction.
Document marketing attempts in the file. Noncompliance is corrected when the unit is again occupied
by a qualified household — but unreasonably long vacancies will be flagged.

### First-year deadlines and forms

- File Form 8609 (with Schedule A) for each building with the owner's tax return by the due date,
  including extensions, for the first year of the credit period; the state HFA must have issued the
  8609 with Part I completed. Sign Part II, and complete Schedule A unit designations.
- The minimum set-aside must be met by the end of the first credit year. If lease-up is behind,
  check the current-year IRS guidance on grace periods and cure windows, and call the HFA before the
  year closes — agencies can often help but only if told early.
- The 10-year credit period runs after the building is placed in service; the 15-year compliance
  period runs from the first credit year. The extended-use agreement (typically 30 years or more,
  state-specific) survives the compliance period.

### Recapture triggers

Credit recapture (acceleration of prior credits plus interest) is triggered by: disposition or
change of ownership of the building or an ownership interest during the compliance period (subject
to the statute's bond-posting and restoration options); a reduction in qualified basis (beyond the
casualty/disaster allowance); failure to satisfy the minimum set-aside; gross rent above the limit;
failure to file required certifications; and noncompliance not corrected within the cure period.
Form 8823 noncompliance does not automatically mean recapture — most findings are corrected and the
credit survives — but uncorrected findings feed the recapture machinery. Respond to every 8823
within the stated correction period, cure, and confirm the agency files the closure 8823.

## HUD Program Compliance

### HOME (24 CFR Part 92)

- Low HOME rent and high HOME rent limits apply per unit; track which units are HOME-designated and
  keep the required percentage of HOME units at the low rent, rented to qualifying households.
- Initial income certification at move-in and annual reexamination for HOME-assisted tenants
  (confirm exceptions with the PJ, e.g., continuous rental assistance).
- Lease-up and expenditure deadlines tightened under the 2024 HOME Final Rule — PJs must commit
  funds within one year (limited exceptions) and complete within shorter windows than the old
  four-year rule. A project left uncommitted risks recapture by the PJ.
- Record in IDIS on the PJ's schedule; submit annual HOME certifications; keep tenant files and rent
  records for the PJ's monitoring period, typically five years after the PJ's program-year records
  are submitted.

### ESG (24 CFR Part 576)

- Maintain eligibility documentation for every rapid re-housing or prevention household: proof of
  homelessness or at-risk status per the applicable ESG definitions, income where required, and a
  documented housing instability reason.
- Follow the recordkeeping requirements covering financial, participant, and service records;
  submit the ESG CAPER on the grantee's deadline (commonly within 90 days of program-year end) and
  any monthly/quarterly expenditure reports.
- Meet shelter standards for any congregate facility, participate in HMIS (or a comparable database
  for victim-service providers), and meet HMIS data-quality thresholds — grantees monitor error
  rates, not just completeness.

### CoC (24 CFR Part 578)

- Submit the APR within HUD's deadline after each operating year; late or low-quality APRs hurt
  the CoC's competition score and flow downhill.
- Recipients must monitor subrecipients at least annually; keep monitoring reports, corrective
  action plans, and follow-up evidence on file — the quality of your subrecipient monitoring is
  itself a monitoring item.
- Housing First fidelity, habitability standards, and VAWA requirements are standard review areas.

### HCV and project-based voucher

- Annual reexaminations, HQS/NSPIRE inspection cycles (the unit must pass before HAP begins and at
  each cycle; failures can abate HAP), and timely reporting of income and household changes.
- Under HOTMA rules, income calculation changed materially — asset treatment (a threshold below
  which assets are self-certified), earned income disallowance availability, and exclusions. Pull
  current HUD notices when computing income; do not rely on pre-2024 worksheets.
- PBV adds a HAP contract with unit designation, rent-reasonableness, and waiting-list rules on top
  of the LIHTC layer.

### HUD multifamily: MOR and TRACS

- The **Management and Occupancy Review (MOR)** is conducted by HUD or the contract administrator
  using form HUD-9834: certifications, leases, EIV reports and income discrepancies, waiting lists,
  VAWA paperwork, and management procedures. Respond to findings with a written corrective action
  plan by the stated deadline.
- Monthly certification data (50059s) submitted to **TRACS** must reconcile with voucher billings;
  fatal errors and unreported changes surface as MOR findings and subsidy adjustments. Run the
  Enterprise Income Verification (EIV) reports monthly (income discrepancy, no-income, failed
  validation) — unresolved EIV discrepancies are a guaranteed finding.
- Physical inspections run under **NSPIRE** standards (which replaced UPCS for HUD multifamily);
  know the three inspectable areas (unit, inside, outside) and the life-safety defects that cause an
  automatic fail.

### Cross-cutting: VAWA, lead, and 504

Regardless of program, expect reviewers to check: the VAWA lease addendum, notice of occupancy
rights, emergency transfer plan, and HUD-5380-series forms; lead-based paint disclosure and, for
pre-1978 assisted units, visual assessments; and Section 504 accessibility (5% fully accessible
units in multifamily projects with HUD funds, plus design/construction standards for newer
buildings).

## Tenant File Documentation Standards

Build every file in a fixed order so an auditor can verify eligibility in one pass:

1. Application, waitlist placement, and tenant-selection documentation
2. Income and asset worksheet showing each source, method of verification, and calculation
3. Third-party verifications (employer, benefits agencies, banks), dated before certification
4. Student status questionnaire and supporting evidence where applicable
5. Signed and dated Tenant Income Certification (TIC or program equivalent)
6. Lease and all addenda (LIHTC/program addendum, VAWA addendum, lead disclosure, house rules)
7. Rent-setting documentation showing gross-rent test (rent + mandatory fees + utility allowance)
8. HUD race/ethnicity form (HUD-27061) and disability-status form where required
9. Prior-year certifications and interim certs, in date order
10. Correspondence, notices, and any compliance exceptions with HFA approval attached

Audit rule: **a fact not documented did not happen.** Signature/date order errors, math that
doesn't tie, and missing verifications are the top three findings everywhere. Retain files for the
longest of: the HFA's retention period (commonly six years after the compliance-period year the
record covers), the PJ's HOME period, and any litigation hold.

## Deliverable: File-Readiness Checklist

Produce as a table with columns `Item | Evidence in file | Pass/Fail | Fix by (date) | Owner`, run
per file on a sample of at least 20% of move-ins from the last 12 months and every file flagged in
the prior review:

- [ ] Move-in cert effective on or before lease effective date, signed and dated by all parties
- [ ] Every income source verified in writing by a third party or by source documents
- [ ] Income calculation shows household at or below the AMI limit for the unit designation
- [ ] Student status documented; full-time-student households show a qualifying exception
- [ ] Gross rent worksheet: rent + mandatory fees + utility allowance at or below the limit in effect
- [ ] Utility allowance is the current HFA-approved schedule
- [ ] Lease and all required addenda present, signed, dates consistent
- [ ] Annual recerts complete, effective within 12 months of the prior cert
- [ ] Over-income (140%) households flagged; next-available-unit tracking current
- [ ] Vacant units show documented marketing efforts and restricted rent
- [ ] Interim changes (income, household composition, student status) certified and filed
- [ ] File order matches the standard above; no orphan documents or unsigned forms

Completion condition: every sampled file passes or has a dated corrective action with an owner.

## Deliverable: Monitoring-Visit Preparation Plan

Sequence for an on-site review by a state HFA, PJ, PHA, or HUD contract administrator:

1. **T-8 weeks:** Get the agency's monitoring instrument (checklist or 9834 equivalent). Pull last
   cycle's findings and confirm each corrective action has evidence in files now — repeat findings
   draw escalating remedies.
2. **T-6 weeks:** Run the file-readiness checklist on the sample the agency will likely draw (every
   move-in since last review, every flagged tenant, plus a random 10–20%).
3. **T-6 weeks:** Reconcile the rent roll against certifications: every unit's gross rent against
   the current limit table; every over-income flag against the next-available-unit log.
4. **T-4 weeks:** Mock physical inspection of sample units plus common areas under NSPIRE (or HQS
   for HCV). Repair life-safety items immediately; photograph completed work.
5. **T-4 weeks:** Verify EIV/TRACS reports are run, reconciled, and filed; resolve open income
   discrepancy reports.
6. **T-2 weeks:** Assemble the binder: entity documents, carrying-charge schedule, utility allowances
   with effective dates, insurance, management plan, tenant selection plan, marketing/AFHMP file,
   prior findings and closures.
7. **T-1 week:** Brief site staff — where files live, how recerts are scheduled, who signs certs.
   Staff who cannot explain the process are read as process failure.
8. **Day of:** A compliance lead shadows the reviewer, notes every document pulled, and answers
   factually — never speculate; commit to follow-up instead.
9. **Within 5 days:** Send any documents the reviewer requested.
10. **By the stated deadline (often 30 days):** Deliver the corrective action plan — issue, root
    cause, fix, evidence, and the control that prevents recurrence. Root cause plus a durable
    control closes findings; single-file fixes do not.

## Deliverable: Common Findings and Remedies

| Finding | Why it happens | Remedy and control |
|---|---|---|
| Missing/late annual recert | No tickler system; recerts keyed to lease date not cert date | Recertify immediately, backdate effective date per agency guidance, adopt a 90-day tickler with escalation at 60 days |
| Rent over limit (incl. mandatory fees) | Fees added without gross-rent test; stale rent tables | Refund/credit the overcharge to tenants, adjust rent prospectively, add a gross-rent test to every lease-up and renewal workflow |
| Utility allowance out of date | Allowance updates not calendared | Recompute gross rents with the current allowance, refund overcharges, calendar the HFA's allowance update date |
| Student rule violation | Move-in questionnaire never re-administered | Cure by correcting household composition or documenting an exception; re-verify student status at every annual recert |
| File documentation order/signature errors | Loose filing practices; unsigned forms | Rebuild the file to the standard order; dual review of every new file before closing |
| Over-income unit not tracked | No 140% flag in the rent roll | Add the flag; maintain the next-available-unit log; train leasing staff on the queue rule |
| Vacant unit with no marketing evidence | Turnover between staff | Attach a marketing log to every vacancy in the compliance file |
| EIV/TRACS income discrepancies unresolved | Reports run but never worked | Monthly discrepancy-resolution meeting with dated outcomes in each file |
| Late owner certification / fee to HFA | Calendar misses | Put every HFA deadline in the compliance calendar with a 30-day lead |
| HOME unit out of compliance (rent/income) | Layered-program tracking failure | Keep a unit-by-unit program matrix; apply the strictest rule per dimension |

## Deliverable: Annual Compliance Calendar

Anchor dates vary by agency; the structure below holds. Convert to dates with the specific
HFA/PJ/PHA deadlines and set 30-day lead reminders.

- **Monthly:** EIV/TRACS report review and discrepancy resolution; new move-in file audits (100%);
  vacancy marketing logs; HAP/rent-roll to certification reconciliation.
- **Quarterly:** Sample file audit (10% of occupied units); utility allowance and rent-limit table
  re-check; over-income/next-available-unit log review; 8823 open-items review with the HFA.
- **January:** Prior-year owner certifications drafted (due to many HFAs in Q1 — often early March or
  the date in the LURA); compliance fees budgeted and paid.
- **February–March:** Annual state HFA owner certification and compliance report submitted; prior-year
  8823s confirmed closed.
- **April–June:** New MTSP income and rent limits published — load into the rent system, re-test
  pending move-ins, plan application at recerts; HOME rent limits published (typically effective
  June).
- **Summer:** Agency on-site monitoring season — run the monitoring-visit preparation plan; complete
  physical inspections cycle requirements; entity-level insurance and LURA covenant reviews.
- **September–October:** CoC APR season for many CoCs (operating-year anniversaries vary); ESG CAPER
  per grantee deadline; subrecipient monitoring reports issued.
- **October–December:** Year-end file sweep on all move-ins; student status re-verification for the
  school year; tax-prep package to CPA including 8609 schedules and any 8823 history; calendar
  refresh for next year.

Completion condition: every recurring deadline above has a named owner and a lead-time reminder.

## Common Failure Modes

- **Treating LIHTC as materiality-based.** It is pass/fail: one dollar over the gross-rent limit or
  one late recert is reportable noncompliance that goes on Form 8823.
- **Applying Section 8 income rules to Section 42 (or vice versa).** Definitions and exclusions
  differ; layered units need parallel calculations.
- **Self-certifying where third-party verification is required.** If the file shows only tenant
  statements for wages, the certification is unsupported.
- **Ignoring over-income flags.** The 140% rule is quiet until the next available unit is rented
  wrong — then the qualified unit is lost for good.
- **Filing 8823 responses late or informally.** Cure within the stated period, in writing, with
  evidence, and confirm the closure filing.
- **No unit-level program matrix on layered deals.** A HOME-designated unit rented above the high
  HOME rent triggers HOME repayment even when LIHTC compliance is clean.
- **Doing compliance in a spreadsheet only the compliance officer can read.** Staff turnover is the
  leading cause of missed recerts; the calendar, tickler, and logs must survive the person.

## Supervision Note

Every certification, Form 8609, Form 8823 response, and annual owner certification produced with
this skill must be reviewed by a qualified attorney or CPA familiar with Section 42 before filing
with the state HFA or IRS. The checklists above prepare the file; they do not substitute for
professional review, and agency rules and IRS guidance change — verify current requirements with
your agency before submitting.
