---
name: nonprofit-faith-finance-clergy-comp
description: "US clergy pay and church finance mechanics: IRC §107 housing allowance, SECA dual tax status, W-2 vs. 1099 for clergy, love offerings and §102 gifts, accountable reimbursement plans, benevolence funds, IRC §4958 reasonable-comp process, 403(b)(9) plans, QSEHRA/ICHRA, and church cash-handling. Use when a church/synagogue/mosque administrator, treasurer, pastor, rabbi, imam, or advisor asks about housing allowance, parsonage, clergy W-2, SECA, love offering, benevolence, or a pastor's comp package. Not for 990 exemption (nonprofit-faith-990-exemption), giving statements (nonprofit-faith-stewardship-giving), firing clergy (nonprofit-faith-employment-ministerial-exception), or non-clergy HR (nonprofit-hr)."
license: MIT
metadata:
  supervision: "review"
  supervision_note: "Housing-allowance designations, W-2/1099 classification, and benevolence-fund payments have direct tax consequences for the clergyperson and the congregation."
  last_reviewed: "2026-09-10"
  date_added: "2026-09-12"
  date_added_source: "git:297d3ef69a314702df1ccc8174826716c88cff40"
---

# Faith-Based Finance and Clergy Compensation (US Tax Mechanics)

## When to Use This Skill

Use this skill when the user is running or advising a US congregation (church, synagogue, mosque,
temple, meetinghouse) or denominational body and needs to structure or fix a **clergyperson's pay
package** or the **congregational finance mechanics that touch clergy compensation**. Trigger
phrases: "designate my pastor's housing allowance," "we forgot to set the housing allowance,"
"our rabbi lives in the parsonage — what goes on the W-2," "the imam gets a monthly stipend,
should he be 1099," "the congregation took up a Christmas love offering," "retirement gift to
Pastor X," "can our benevolence fund pay a member's rent," "we've never had an accountable
reimbursement plan," "set the senior minister's compensation defensibly," "what's a 403(b)(9),"
"the church has been withholding FICA on the pastor," or "do we need an audit."

Boundary: this skill is the **clergy-tax and clergy-comp mechanics layer** plus the narrow slice
of congregational finance that touches those mechanics (offering handling, benevolence,
accountable reimbursement). **Form 990 filing exemption**, integrated auxiliaries, group exemption
rulings, church UBIT, and IRC §7611 audit protections are `nonprofit-faith-990-exemption`.
**Contributor giving statements**, quid-pro-quo disclosures, capital-campaign pledge accounting,
and religious-context planned giving are `nonprofit-faith-stewardship-giving`. **Firing a
minister**, ministerial-exception defenses, Title VII religious hiring exemption, clergy
misconduct response, and safe-sanctuary policies are
`nonprofit-faith-employment-ministerial-exception`. **Non-clergy staff HR** (handbook, FLSA for
the office administrator, PTO) is `nonprofit-hr`. Generic **budgeting, financial statements,
reserves and cash-flow** are `nonprofit-budgeting`, `nonprofit-financial-statements`, and
`nonprofit-reserves-cash-flow`. Generic **internal controls** are `nonprofit-financial-controls`;
this skill only handles the congregation-specific offering and benevolence pieces.

Multi-tradition note: "minister of the gospel" is IRS statutory language and applies functionally
to rabbis, cantors, imams, priests, deacons, ministers, and pastors who perform sacerdotal
functions, conduct worship, and share in governance of the religious body. Use the user's own
tradition-appropriate title in drafts; the tax mechanics are the same.

## Core Frameworks

Name the statute, ruling, or case before drafting an artifact — clergy tax lives in a small set
of specific authorities that a finance committee will not know by name.

- **IRC §107 — Minister's housing allowance**: excludes from gross income for federal income tax
  either (1) the rental value of a parsonage provided in kind, or (2) a cash "rental allowance,"
  to the extent used to provide a home and not exceeding fair rental value plus utilities. The
  exclusion is for income tax only — not SECA.
- **IRS Rev. Rul. 70-549 — "minister of the gospel" functional test**: whether a person is a
  "minister" for §107, §1402(c), and §3121(b)(8) purposes is a **functional** test, not a title
  test. Factors: (1) administers sacraments/ordinances, (2) conducts religious worship, (3)
  performs management/leadership in the religious body or an integral agency, (4) is ordained,
  commissioned, or licensed, and (5) is considered a religious leader by the body.
- **IRC §1402(a)(8) and §1402(c) — SECA on ministerial services**: ministers are treated as
  self-employed for Social Security and Medicare on both salary and housing allowance. The
  church **cannot withhold FICA** and does **not** pay the employer match. The clergyperson owes
  15.3% SECA on the combined base.
- **IRC §3121(b)(8)(A)** excludes ministerial wages from FICA; **IRC §3401(a)(9)** excludes them
  from mandatory income-tax withholding, but the clergyperson may **voluntarily** elect
  withholding on Form W-4 line 4(c) large enough to cover both income tax and SECA (standard
  pastoral practice, avoids quarterly 1040-ES).
- **Form 4361 — SECA exemption**: a narrow, **irrevocable** exemption available only to a
  minister conscientiously opposed on religious (not economic) grounds to accepting public
  insurance for ministerial services. Filed by the due date of the return for the second taxable
  year with $400+ of net ministerial earnings. Most clergy do not qualify.
- **Treas. Reg. §1.62-2 — Accountable plans**: reimbursements are excluded from wages only if
  the plan meets three tests: (1) business connection, (2) substantiation within a reasonable
  time, (3) return of excess. Fail any test and the entire arrangement is non-accountable and
  every dollar becomes W-2 wages.
- **IRC §102 — Gift exclusion** and the clergy case law: **Commissioner v. Duberstein (363 U.S.
  278, 1960)** ("detached and disinterested generosity" motive test), **Goodwin v. United States
  (67 F.3d 149, 8th Cir. 1995)** (congregation-wide "special occasion" cash gifts to pastor were
  taxable compensation), and **Banks v. Commissioner (T.C. Memo 1991-641)**. If the congregation
  is prompted to give or the amount is aggregated by the church, it is compensation.
- **IRC §4958 — Intermediate sanctions and rebuttable presumption of reasonableness**: senior
  clergy are disqualified persons. Rebuttable presumption requires (1) approval by an independent
  authorized body, (2) appropriate comparability data, (3) contemporaneous substantiation.
- **IRC §403(b)(9) — Church retirement income accounts**: church-plan variant of 403(b) with
  two features that matter: (a) retired ministers can have distributions designated as **housing
  allowance** by the plan sponsor, extending §107 into retirement — 401(k) and IRA distributions
  cannot; (b) church-plan status exempts the plan from most of ERISA.
- **IRS Publication 517** (clergy-facing) and **IRS Publication 1828** (church-facing, Tax Guide
  for Churches and Religious Organizations) are the working reference documents.

## Standard Deliverables

Every in-scope request resolves into one of these artifacts:

- **Housing allowance designation resolution** — board/session/vestry/council resolution
  designating a dollar amount as §107 housing allowance for the coming calendar year, entered in
  the minutes before the first affected payroll date.
- **Clergy compensation package memo** — line-item breakdown: cash salary, housing allowance (or
  parsonage FRV), SECA allowance, retirement contribution, health coverage (HRA), accountable-
  reimbursement budget, continuing-education budget, total cost to the church, take-home-after-
  tax estimate for the clergyperson.
- **Accountable reimbursement plan document** — written plan meeting the three §1.62-2 tests,
  adopted by the board, with submission form and receipt-retention rule.
- **Benevolence fund policy** — need criteria, application/screening, approval authority,
  documentation, prohibition on donor-directed grants, §102-gift-not-compensation treatment.
- **Reasonable-compensation packet** — comparability data pull, board resolution, and
  contemporaneous minutes building the §4958 rebuttable presumption.
- **W-2 for clergy** — wages in box 1, **no** Social Security or Medicare wages/tax in boxes 3–6,
  housing allowance informationally in box 14 (e.g., "Housing $28,000").
- **Church finance-committee charter and cash-handling procedure** — counting-team rules,
  dual-signature threshold, monthly reconciliation review, annual review scope.

## Designating the Housing Allowance — Numbered Checklist

Run this checklist every year, before the first payroll of the calendar year (or before the first
payroll after hire for a mid-year start). The failure mode is **retroactivity**: a designation
adopted after payment cannot cover payments already made.

1. **Confirm the person qualifies as a "minister" for §107**. Apply the Rev. Rul. 70-549
   functional test. Ordained/commissioned/licensed status alone is not enough; unordained staff
   who do not perform ministerial functions do not qualify even if their title says "minister of
   music."
2. **Have the clergyperson estimate annual housing costs** in writing for the coming year:
   mortgage principal and interest (or rent), property taxes, homeowners/renters insurance,
   utilities, furnishings and appliances, repairs and maintenance, HOA dues, yard/pest care. Do
   **not** include food, domestic help, or the cost of a second home. Add a 10–15% cushion — the
   allowance can be under-used with no penalty, but any excess over actual expenses is taxable.
3. **Cap-check against fair rental value**. The §107 exclusion is the **lesser of** (a) the
   amount designated in advance, (b) actual housing expenses paid, or (c) fair rental value of
   the home furnished plus utilities. Keep a defensible FRV — realtor estimate, Zillow Rent
   Zestimate, or comp memo — in the file. Matters most for clergy in owned homes in expensive
   markets.
4. **Adopt the designation by the governing body in a written resolution** before the first
   affected payroll date. Must (a) name the minister, (b) state the period, (c) state the dollar
   amount (or percentage-of-salary formula that produces one), (d) be recorded in the official
   minutes. A pastor cannot designate their own allowance.
5. **Include a standing/carry-forward clause** so a missed year does not zero out the allowance:
   "Until further action of the board, the housing allowance designated for [Name] shall
   continue at the amount above for each subsequent calendar year." Still readopt annually as
   part of the budget cycle.
6. **Handle parsonage-plus-cash correctly**. If the church provides a parsonage in kind, the FRV
   is excluded under §107(1) and does not appear in W-2 box 1 (but the FRV **is** in the SECA
   base). Any additional cash allowance for utilities or furnishings needs its own separate
   §107(2) designation.
7. **Update the payroll system**. Housing allowance is excluded from W-2 box 1; report it
   informationally in **box 14** ("Housing $28,000"). Nothing in box 3 or 5 (no FICA wages for
   clergy). If payroll software cannot handle it, code it as a non-taxable earnings type outside
   gross pay and reconcile monthly.
8. **State-tax variation**. Most states conform. **Pennsylvania** does not fully conform and
   taxes housing allowance for state PIT. Confirm state and local treatment.
9. **Communicate the year-end reconciliation duty**. The clergyperson must compare designated
   allowance vs. actual expenses vs. FRV+utilities at tax time and include any excess on Schedule
   1 line 8. The housing allowance **is** subject to SECA on Schedule SE unless a valid Form 4361
   is on file.
10. **Retired-minister housing allowance from a 403(b)(9)**. The plan sponsor (denominational
    pension board or the church board for a single-employer plan) can designate all or part of
    each year's distribution as housing allowance. Confirm the designation is on file before the
    first distribution. IRA and 401(k) distributions do not get this treatment.

## Dual Tax Status — How Clergy Payroll Actually Works

Clergy occupy a unique split status that constantly trips up new church treasurers and secular
payroll services. State it flatly:

- **For federal income tax**, the clergyperson is a **common-law employee** of the church and
  receives a **W-2** (not 1099-NEC). True for almost every settled senior pastor, rabbi, imam,
  or associate clergyperson.
- **For Social Security and Medicare on ministerial income**, the same clergyperson is **treated
  as self-employed** and owes **SECA** (15.3%: 12.4% Social Security up to the wage base, 2.9%
  Medicare, plus 0.9% Additional Medicare above threshold) on **cash salary, designated housing
  allowance, and the FRV of any parsonage/utilities provided in kind**.
- **The church cannot withhold FICA** (§3121(b)(8)(A)) and does **not** pay the 7.65% employer
  match. A church that has been withholding FICA is doing it wrong: stop immediately, correct via
  Form 941-X for open quarters, refund the improperly withheld employee share.
- **The church is not required to withhold federal income tax** either (§3401(a)(9)), but the
  clergyperson almost always should elect **voluntary income-tax withholding** on Form W-4 line
  4(c) large enough to cover both federal income tax **and** SECA. Standard practice; avoids
  quarterly Form 1040-ES.
- **SECA offset / SECA allowance** is a common package line: the church pays roughly 7.65% of
  salary + housing as additional taxable cash to offset the employer half of SECA the church is
  not paying. The offset is fully taxable for income tax and SECA (so grosses up imperfectly),
  but naming it as its own line item is cleaner than burying it in base salary.
- **Form 4361** is a narrow escape hatch, not planning. Grounds are **religious conscientious
  opposition** to public insurance benefits for ministerial services — not economic disagreement,
  not "I have my own plan." File by the due date of the return for the second taxable year with
  $400+ net ministerial earnings. **Irrevocable**. Certain Anabaptist, some Pentecostal, and a
  small number of other traditions qualify; most do not. Do not draft one without confirming the
  minister genuinely holds the required religious opposition.
- **Non-ministerial income** (secular professor salary, general-market book royalties, wedding-
  officiant work at a secular venue) is treated normally — regular FICA if W-2, regular
  self-employment if 1099.

## W-2 vs. 1099 Classification for Clergy — Get This Right

- **Default: W-2 for any settled clergyperson serving a specific congregation**, even though
  clergy are dual-status for SECA. Common-law-employee factors (behavioral control, financial
  control, relationship of the parties) almost always resolve to employee for a called or
  appointed clergyperson: congregation dictates schedule and duties, provides workspace, pays
  regularly, expects an ongoing relationship, all documented in a call agreement or
  denominational appointment.
- **Common misclassification**: a church puts a new associate pastor or small-church solo pastor
  on 1099-NEC to "keep it simple" or because "she asked for it." Wrong. Costs the church payroll-
  tax and backup-withholding exposure on audit and costs the pastor voluntary withholding,
  benefits eligibility, and — critically — the ability to have a clean §107 housing-allowance
  designation.
- **Legitimate 1099 cases** are narrow: **guest/supply preacher** paid a one-time honorarium, a
  **visiting scholar**, a **wedding officiant** not on staff, an **itinerant evangelist**, or a
  **musician** hired for a single service. Issue a 1099-NEC if $600+ in a calendar year.
- **Denominational assignment vs. local call**. In appointive systems (United Methodist, Roman
  Catholic, LDS, some Episcopal functions), the denomination/bishop appoints, but the local
  church is usually the employer of record for payroll unless the denominational structure
  explicitly employs the clergyperson (diocesan priests in some cases, denominational executive
  staff, most missionaries). In call systems (Baptist, congregational, Presbyterian in most
  functions, most synagogues, most mosques), the local congregation is clearly the employer.
  Housing-allowance designation must come from the actual employer's governing body.

## Love Offerings, Honoraria, and Gifts to Clergy — The §102 Trap

- **The §102 exclusion is narrow for clergy.** The **Duberstein** motive test asks whether the
  transfer was made from "detached and disinterested generosity." Cash collected via pulpit
  prompt, bulletin announcement, or formal appeal is almost never disinterested; the congregation
  is compensating the pastor.
- **Goodwin v. United States** controls: regular "special occasion" cash gifts collected from
  congregants and remitted to the pastor were taxable compensation. Any love offering that is
  (a) solicited by or through the church, (b) collected in a church envelope or fund, or (c)
  aggregated by the church and paid to the clergyperson, is **W-2 wages** — even if the church
  calls it a "gift."
- **Named patterns**:
  - **Christmas offering** taken up by the church for the pastor → W-2 wages, SECA base.
  - **Anniversary gift** organized by the deacons, funds routed through the church → W-2 wages.
  - **Retirement gift** funded by a church-designated fund or announced from the pulpit → W-2
    wages. A small ceremonial item (plaque, watch under de minimis) can be excluded under §132;
    a $50,000 "purse" cannot.
  - **Honorarium for a wedding, funeral, or bar/bat mitzvah** paid by the family directly to the
    clergyperson: **self-employment income on Schedule C**, reported by the payer on 1099-NEC if
    $600+. If the congregation requires all fees be paid to the church and then paid to the
    clergyperson, they become W-2 wages.
  - **Truly private gift** from one congregant to the clergyperson — direct, unsolicited,
    unaggregated, motivated by personal relationship — is likely a §102 gift, not taxable, and
    **not deductible** by the giver as a charitable contribution. The donor cannot take a
    charitable deduction for a designated gift to a specific individual routed through the
    church, no matter how the church labels it.
- **Rule to give the finance committee**: if the church touches the money on its way to the
  clergyperson, or the congregation was prompted to give, put it on the W-2. Personal gifts go
  direct from congregant to clergyperson, not through the church books.

## Accountable Reimbursement Plans — Adopt One or Bleed Deductions

Since TCJA eliminated the unreimbursed-employee-business-expense deduction for W-2 employees, an
accountable reimbursement plan is the **only** way a clergyperson gets tax-free treatment of
business expenses paid personally. Without one, mileage, books, conference travel, and
continuing-education costs come out of after-tax pocket.

- **The three §1.62-2 tests**:
  1. **Business connection** — ordinary and necessary trade-or-business expenses incurred in
     performing services for the employer.
  2. **Substantiation** — receipts, mileage logs, business purpose, date, amount, within a
     reasonable time (60-day safe harbor).
  3. **Return of excess** — unsubstantiated advances or over-reimbursements returned within a
     reasonable time (120-day safe harbor).
- **Failure of any test collapses the whole plan**; every dollar becomes W-2 wages subject to
  income tax and SECA. Most common expensive mistake in small-church payroll.
- **Do not "gross up" salary as a car allowance**. A flat $500/month auto allowance paid
  regardless of mileage is non-accountable and fully taxable. Convert to per-mile IRS-rate
  reimbursement against a mileage log, or reimburse actual receipts against a documented plan.
- **Reasonable categories**: business mileage (current IRS rate), business travel and lodging,
  continuing education, books and periodicals used in ministry, professional dues, robes/
  vestments used exclusively in ministerial functions, substantiated business meals, business-
  use cell phone.
- **Do not reimburse personal expenses** (family clothing, personal meals, family travel on a
  business trip, home-to-sanctuary commuting) — makes them taxable and puts the plan's
  accountable status at risk.
- **Budget the plan on top of salary**, not as a salary slice. A salary-reduction structure is
  legally permitted but must be a genuine employer plan reimbursing actual expenses, not
  disguised salary; budgeting the reimbursement line separately is safer.

## Benevolence Funds — §102 Gifts vs. Compensation

Benevolence to individuals in need is one of the most theologically important and legally error-
prone activities a congregation does.

- **Recipient side (§102)**: a benevolence payment to a genuinely needy individual, made per a
  board-adopted policy, based on documented need, and not in exchange for services, is a §102
  gift — excluded from the recipient's gross income, not reportable on 1099 or W-2.
- **Donor side (§170)**: a contribution to the **general benevolence fund** is deductible because
  the church retains full discretion. A contribution **designated for a named individual** is
  generally **not deductible**; it is a personal gift routed through the church, and the church
  cannot issue an acknowledgment for it. See `nonprofit-faith-stewardship-giving` for full
  donor-side rules.
- **Written benevolence policy — required elements**:
  1. **Purpose** — emergency/temporary need for basic necessities (rent, utilities, food,
     medical, funeral) consistent with the congregation's charitable purpose.
  2. **Eligibility** — who can apply; if restricted to members, check public-benefit
     implications.
  3. **Need standard and documentation** — situation description, verification (utility shut-off
     notice, eviction notice, medical bill), and requested amount.
  4. **Approval authority** — benevolence committee or designated staff, dollar-level tiers (e.g.,
     pastor up to $500, committee up to $2,500, board above). Senior clergy should not be the
     sole approver for large amounts.
  5. **Payment method** — pay the **vendor directly** where possible (landlord, utility,
     hospital, funeral home). Cash to individuals is legal but harder to defend.
  6. **Prohibition on donor-directed grants** — donor-advised benevolence collapses the donor's
     deduction and the recipient's §102 characterization. Refer donors who want to help a
     specific person to give cash direct.
  7. **Prohibition on compensation-disguised-as-benevolence** — payments to a staff member (or
     former staff member) that look like severance, or to anyone who just did work for the
     church, will be recharacterized as wages.
  8. **Recordkeeping** — application, need documentation, approval minutes, payment record.
- **Recurring pattern to avoid**: monthly benevolence payments to the same person for years look
  like a stipend and can be recharacterized as taxable income (and as wages if any services are
  performed in return). Structure ongoing support as employment, contract, or a referral to a
  professional social-service partner.

## Setting Reasonable Clergy Compensation — Building the §4958 Rebuttable Presumption

Senior clergy are "disqualified persons" under IRC §4958 in most churches. Excess benefit
triggers a 25% excise tax on the clergyperson and 10% on board members who knowingly approved.
The **rebuttable presumption of reasonableness** shifts the burden to the IRS if built properly.
Run this whenever senior clergy comp is set or materially changed.

1. **Independent authorized body**. Compensation committee with **no conflicts**: no family, no
   subordinate employees, no business relationship. Pastor is out of the room and does not vote.
2. **Pull appropriate comparability data**. Standard clergy sources:
   - **Church Law & Tax Compensation Handbook for Church Staff** (annual, Christianity Today) —
     the most-used Christian-congregation survey, sliced by attendance, budget, region,
     denomination, and role.
   - **Compass Compensation** and other role-specific salary databases.
   - **Denominational compensation guidelines**: UMC conference guidelines, PC(USA) presbytery
     minimums, ELCA synod guidelines, Episcopal diocesan clergy grids, RCA/CRC classis
     guidelines. Reform, Conservative, and Reconstructionist Jewish movements publish rabbinic
     compensation resources through their rabbinical assemblies; Orthodox congregations often
     rely on regional/community norms.
   - **GuideStar / Candid** for compensation reported on Form 990 by similar 501(c)(3) faith-
     adjacent employers (Christian schools, denominational agencies, parachurch orgs). Most
     churches themselves do not file 990, so direct church-to-church data is limited but
     denominational-agency data is usable.
   - **Local cost-of-living adjustments** (BLS, PayScale, ERI).
3. **Total the whole package**, not just salary: cash salary + housing allowance (or parsonage
   FRV) + SECA offset + retirement contribution + health/HRA + life/disability + accountable
   reimbursement budget (excluded from §4958 comp) + continuing education + other fringes.
   Compare **total compensation** against the comparable data's total-comp figure.
4. **Decide in advance**. Retroactive "we would have approved that" documentation does not build
   the presumption.
5. **Contemporaneous written documentation** within the 60-day safe harbor: (a) terms and date,
   (b) members of the body present and voting, (c) comparability data relied on and how it was
   obtained, (d) actions by anyone with a conflict, (e) basis for the determination. Minutes
   adopted by the next meeting.
6. **Refresh annually**. Every material change (raise, new benefit, one-time bonus) needs its
   own presumption-building record.
7. **Watch the total**. A pastor with $70,000 salary, $30,000 housing allowance, rent-free
   parsonage (~$36,000 FRV), $10,000 SECA offset, 12% retirement, full HRA, and a $15,000
   Christmas offering has a very different total than the salary line suggests. Comp
   comparability applies to the whole package.

## Church Retirement Plans

- **403(b)(9) church retirement income accounts** are the workhorse: (a) available only to
  churches and qualified church-controlled organizations; (b) **church plan** exempt from most of
  ERISA (no Form 5500 unless the church elects ERISA coverage); (c) retired ministers can have
  distributions designated as housing allowance by the plan sponsor, extending §107 into
  retirement; (d) fewer nondiscrimination restrictions than corporate 401(k)s.
- **Denominational pension boards** administer most 403(b)(9) plans and handle the housing-
  allowance-in-retirement designation at the plan level. Major ones: **The Pension Boards —
  United Church of Christ**, **Board of Pensions of the Presbyterian Church (U.S.A.)**,
  **GuideStone Financial Resources** (Southern Baptist and broadly evangelical), **Wespath
  Benefits and Investments** (United Methodist), **MMBB Financial Services** (American Baptist
  and broader), **Church Pension Group** (Episcopal), **Portico Benefit Services** (ELCA), and
  **Concordia Plan Services** (LCMS). For synagogues, the **Reform Pension Board** and other
  movement-affiliated plans serve rabbis and cantors.
- **401(k) plans** are permissible but forfeit the §107-in-retirement advantage — 401(k) and IRA
  distributions cannot be excluded as housing allowance. Default to 403(b)(9).
- **457(b)** plans can layer on additional deferrals for a highly-compensated senior clergyperson
  beyond 403(b) limits; separate ERISA and unfunded-plan analysis required.

## Health Coverage — HRAs for Small Congregations

- Most congregations are too small for a group plan. The two workable HRA substitutes:
  - **QSEHRA (Qualified Small Employer HRA)** — fewer than 50 FTEs, no group plan offered.
    Reimburses individual-market premiums and qualified medical expenses up to statutory annual
    caps (indexed; ~$6,150 self / ~$12,450 family for 2024 — verify current year). 90-day written
    notice required.
  - **ICHRA (Individual Coverage HRA)** — no size limit, no dollar cap; employees must be
    enrolled in individual-market coverage; can be varied by defined employee classes.
- **Minister-only HRA**: informal premium reimbursement outside QSEHRA/ICHRA risks ACA market-
  reform violations and $100/day/employee penalties. Structure single-clergyperson arrangements
  as a compliant QSEHRA or ICHRA; do not "just reimburse" off-book.
- **Clergy tax-parity history**: informal reimbursement was penalized during the ACA transition;
  the QSEHRA statute (2016) and ICHRA regulations (2019) restored a compliant path. Confirm
  current-year contribution limits before drafting.
- **Health-sharing ministries** are not insurance and generally not HRA-reimbursable; a church
  payment to a sharing ministry on behalf of the clergyperson is usually taxable comp.

## Congregational Cash-Handling and Finance Oversight — The Narrow Slice

Full internal-controls design is `nonprofit-financial-controls`. This skill covers only the
church-specific pieces:

1. **Three-person offering-count rule**. Offerings counted by a rotating team of at least two
   unrelated counters (three is better), none of whom are the senior clergyperson, treasurer, or
   their family. Counters sign a count sheet listing loose cash, checks by donor, and envelope
   totals; a separate person posts to the giving database. Most-recommended and most-violated
   congregational control.
2. **Dual signatures on checks over threshold**. Set a written threshold ($1,000 or $2,500
   common) above which two authorized signers are required. Banks typically honor a single
   signature even on two-signature accounts, so the control lives in policy plus monthly
   reconciliation review.
3. **Segregate check-writing from bank reconciliation**. If the same person must do both in a
   small church, a finance-committee member opens the bank statement first and spot-reviews
   before handing it to the reconciler.
4. **Monthly finance-committee review**: bank reconciliations, budget-to-actual, related-party or
   benevolence checks over threshold, and reasonableness of the pastor's aggregate accountable-
   reimbursement submissions.
5. **Finance committee vs. finance team**. Governance oversight (committee, board members) is
   distinct from operational execution (team, staff and volunteer bookkeepers). The committee
   approves policy and reviews reports; the team writes checks. Blurring hides fraud.
6. **Annual review scope**. Most churches do not need — or cannot afford — a full **audit**
   (CPA opinion). Graduated options, cheapest to most expensive: **compilation** (no assurance),
   **review** (limited analytical, negative assurance), **audit** (full opinion). Many
   denominations require a review over a budget threshold (~$500K) and an audit over another
   (~$2M); confirm the denominational rule. State charitable-solicitation registration also
   imposes audit thresholds in NY, CA, FL and others, though churches are often exempt — see
   `nonprofit-faith-990-exemption`.
7. **Pastor and treasurer roles do not merge**. The senior clergyperson should not be a check
   signer, sole online-banking user, or offering counter. Protects the clergyperson as much as
   the church.

Cite **IRS Publication 1828** as the church-facing reference and **IRS Publication 517** as the
clergy-facing reference. Both are periodically updated; check version before drafting.

## Common Failure Modes

- **Retroactive housing allowance designation** — board discovers in February no allowance was
  designated. Fix by designating going forward from the next payroll date; missed months cannot
  be recaptured. Prevent with a standing carry-forward resolution readopted annually.
- **Church withholding FICA on clergy wages** — treasurer or secular payroll service treats the
  pastor like a regular employee. Fix by stopping immediately, filing Form 941-X for open
  quarters, refunding the improperly withheld employee share, and setting up voluntary income-
  tax withholding on Form W-4 line 4(c) to cover SECA.
- **Clergyperson on a 1099** — settled associate pastor put on 1099-NEC to keep it simple. Fix by
  reclassifying prospectively to W-2, designating housing allowance for the current year, and
  correcting prior-year forms if the exposure warrants.
- **Love offering not on the W-2** — Christmas or anniversary offering paid as tax-free gift.
  Under **Goodwin**, this is compensation. Fix by adding it to W-2 wages and the SECA base and
  truing up withholding.
- **Non-accountable reimbursement disguised as accountable** — flat monthly car or book allowance
  with no substantiation. Fix by converting to a real §1.62-2 plan or booking the payments as
  W-2 wages.
- **Donor-directed benevolence** — church takes a designated gift from one member for another,
  issues a receipt, passes the money. Blows up both sides. Fix by refusing designated-for-
  individual routing and pointing donors to give direct.
- **Senior clergy comp set without §4958 process** — board approves a raise in a hallway
  conversation. Fix by rerunning the process retroactively for the current year and putting a
  comp-committee cycle on the annual calendar.
- **Missing Form 4361 window** — a genuinely opposed clergyperson passes the second-taxable-year
  deadline and permanently loses the SECA opt-out. Fix (preventive only): identify at ordination
  whether the person may qualify and file within window.
- **Pennsylvania and similar nonconforming states** — clergy surprised by state tax on housing
  allowance. Fix by including state-tax treatment in the annual designation memo and adjusting
  state withholding or estimated payments.
- **Health premium reimbursement outside QSEHRA/ICHRA** — off-book premium reimbursement can
  trigger $100/day/employee penalties. Fix by adopting a QSEHRA or ICHRA in writing with the
  required participant notice.

## Practitioner vs. Advisor Framing

- **As the practitioner (church business administrator, treasurer, senior clergy, denominational
  staffer)**: default conservative because the exposure lands on real people. Adopt the standing
  housing-allowance resolution with a carry-forward clause. Put the clergyperson on W-2 with
  voluntary income-tax withholding sized to cover SECA. Adopt a written accountable reimbursement
  plan and benevolence policy before you need them. Build the §4958 rebuttable presumption every
  year clergy pay changes. Run housing-allowance / love-offering / benevolence / accountable-
  plan checks on an annual cycle, not one-offs. If the same person counts the offering, writes
  checks, and reconciles the bank statement, name that as an unresolved risk and get a finance-
  committee volunteer to break the loop, even imperfectly.
- **As the advisor (CPA, attorney, denominational consultant, coach to clergy)**: name the
  specific authority you are applying — the treasurer will not know §107, Rev. Rul. 70-549,
  §1.62-2, §4958, Goodwin, Form 4361, or 403(b)(9) by name, and naming them builds trust and
  protects the advice. Ask three diagnostic questions early: (1) is the person actually a
  "minister" under the Rev. Rul. 70-549 functional test, or a lay staff member the church is
  calling one? (2) is the church withholding FICA (a red-flag misconfiguration)? (3) is a written
  housing-allowance resolution on file, adopted before the first affected payroll date? Work
  outward from there to accountable reimbursement, benevolence, love-offering handling,
  retirement structure, and the §4958 cycle. Refuse to draft a Form 4361 without a substantive
  conversation about religious grounds. Route ministerial-exception, misconduct, and firing
  questions to `nonprofit-faith-employment-ministerial-exception`; 990-exemption, group-ruling,
  and church-audit-procedure questions to `nonprofit-faith-990-exemption`; contributor giving
  statements and quid-pro-quo treatment to `nonprofit-faith-stewardship-giving`.
