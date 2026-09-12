---
name: nonprofit-faith-990-exemption
description: "Special US federal tax status of churches, synagogues, mosques, temples, integrated auxiliaries, and conventions/associations of churches: automatic IRC §501(c)(3) exemption without Form 1023, Form 990 filing exemption under §6033(a)(3)(A), the IRS 14-point church test, integrated-auxiliary internal-support test, denominational group exemption rulings, church UBIT and Form 990-T, and IRC §7611 church-audit procedures. Use when a church administrator, clergy, denominational staffer, or advisor asks about filing a 990 or 1023, integrated-auxiliary status, group rulings, UBIT on parking/cell-tower/bookstore income, or IRS church-audit protections. Does not cover generic 990 filing (use nonprofit-form-990), clergy comp / housing allowance (nonprofit-faith-finance-clergy-comp), federal-grant faith-based compliance (nonprofit-faith-religious-liberty-compliance), or property-tax exemption for the sanctuary (nonprofit-faith-facilities-sanctuary)."
license: MIT
supervision: review
supervision_note: "Determinations about church status, integrated-auxiliary classification, UBIT liability, and audit-procedure invocation have direct federal tax consequences and should be reviewed by qualified tax counsel before filing or response."
last_reviewed: 2026-09-10
---

# Church, Integrated-Auxiliary, and Convention/Association Federal Tax Status (IRC §§508, 6033, 7611)

## When to Use This Skill

Use this skill when the user is asking about the special federal tax treatment US law gives to
**churches, their integrated auxiliaries, and conventions or associations of churches** — status
that does not flow to a generic 501(c)(3). Trigger phrases: "do we need to file Form 1023 for our
new congregation," "our accountant says churches don't file a 990 — is that right," "does our
seminary / mission board / publishing house / denominational agency have to file," "we're
starting a new mosque / temple / synagogue — what do we file with the IRS," "the denomination has
a group exemption — how does that work for us," "we rent the parking lot / lease a cell tower /
run a coffee shop — do we owe unrelated business income tax," "the IRS sent a letter about our
church — what protections do we have," or "our foundation grantor is asking for our 501(c)(3)
letter and we don't have one."

Trigger it too when a **denominational treasurer or advisor** is deciding whether a subordinate
belongs on the group-exemption roster, when an independent congregation is weighing whether to
file a 1023 despite being automatically exempt, or when a practitioner is staring at an IRS notice
and needs to know whether IRC §7611 procedural protections apply.

Boundary: this skill covers only the **federal tax exemption, federal information-return exemption,
denominational group ruling, church UBIT, and IRC §7611 audit procedure** questions unique to
houses of worship and their closely related bodies. For everything adjacent, route out:

- Generic Form 990 / 990-EZ / 990-N filing mechanics for a normal 501(c)(3) that must file →
  `nonprofit-form-990`.
- Generic state charitable-solicitation registration and unified registration statement work →
  `nonprofit-charitable-registration`.
- Generic enterprise risk management for nonprofits (D&O, cyber, employment practices) →
  `nonprofit-risk-management`.
- Clergy federal income tax status, IRC §107 housing allowance, SECA / dual tax status, W-2 vs
  1099 for clergy, love offerings, benevolence-fund controls → `nonprofit-faith-finance-clergy-comp`.
- A faith-based org that takes federal grants and has to navigate Charitable Choice / Equal
  Treatment separation of inherently religious activity → `nonprofit-faith-religious-liberty-compliance`
  and `nonprofit-faith-programs-social-services`.
- Real-property tax exemption for the sanctuary, shared-use agreements, and rental-income facility
  interactions → `nonprofit-faith-facilities-sanctuary` (note: state property tax; this skill
  covers only the federal-tax overlay).
- Congregational vs. presbyterian vs. episcopal polity, bylaws, member meetings, denominational
  reporting relationships → `nonprofit-faith-church-governance`.

## Core Frameworks

Name the statute, reg, or IRS pub before drafting anything. Church tax status is unusually
statute-driven, and generic 501(c)(3) advice is often wrong for a church.

- **IRC §501(c)(3)** — the substantive exemption. Churches qualify on the same terms as any other
  charity (organized and operated for exempt purposes, no private inurement, limited lobbying, no
  political-campaign intervention). The specialness is procedural, not substantive.
- **IRC §508(a) and §508(c)(1)(A)** — §508(a) is the general rule that a 501(c)(3) must notify the
  IRS (by filing Form 1023 or 1023-EZ) to be treated as exempt. §508(c)(1)(A) is the "mandatory
  exception" that carves out **churches, their integrated auxiliaries, and conventions or
  associations of churches** — they are exempt without applying. This is what people mean by
  "automatic" church exemption.
- **IRC §6033(a)(3)(A)(i) and (iii)** — the parallel information-return exemption. Churches,
  their integrated auxiliaries, and conventions or associations of churches are excused from
  filing Form 990, 990-EZ, and 990-N. This is why the church across the street has no Form 990 on
  ProPublica Nonprofit Explorer.
- **Treas. Reg. §1.6033-2(h)** — the operational definition of "integrated auxiliary of a church":
  (1) 501(c)(3), (2) affiliated with a church or convention/association of churches, and (3)
  internally supported (not primarily supported by governmental sources, fees for services, or
  admissions, sales, or receipts from unrelated trades or businesses). Elementary and secondary
  schools, colleges/universities, seminaries and mission societies get special treatment inside
  this reg — read it before classifying a denominational school or seminary.
- **IRS 14-point church test** — the working definition the IRS uses in the absence of a statutory
  one. Restated in **IRS Publication 1828 (Tax Guide for Churches and Religious Organizations)**
  and applied in cases including American Guidance Foundation v. United States and Foundation of
  Human Understanding v. Commissioner. The 14 characteristics: (1) distinct legal existence; (2)
  recognized creed and form of worship; (3) definite and distinct ecclesiastical government; (4)
  formal code of doctrine and discipline; (5) distinct religious history; (6) membership not
  associated with any other church or denomination; (7) organization of ordained ministers; (8)
  ordained ministers selected after completing prescribed courses of study; (9) literature of its
  own; (10) established places of worship; (11) regular congregations; (12) regular religious
  services; (13) Sunday schools for religious instruction of the young; and (14) schools for the
  preparation of ministers. No single factor is dispositive; regular worship + an identifiable
  community of worshippers + a distinct religious ministry are the center of gravity. Synagogues,
  mosques, temples, gurdwaras, Buddhist sanghas, and indigenous religious communities satisfy the
  test on their own equivalents — "Sunday school" reads as regular religious instruction of
  children in that tradition; "ordained ministers" reads as the tradition's recognized clergy.
- **Rev. Proc. 80-27 (as modernized by Rev. Proc. 2023-5 and its successors)** — the mechanics of
  **group exemption rulings**: a central organization (a denomination, association of congregations,
  or parent religious body) obtains a determination that its listed subordinates are exempt without
  each subordinate filing its own 1023. The central org keeps a current subordinate roster,
  submits an annual group-ruling update, and takes on general supervision or control of its
  subordinates as defined in the Rev. Proc. **Note: the IRS has not accepted new group-ruling
  applications since a moratorium beginning in 2020** — verify current IRS status before advising
  on a fresh group ruling.
- **IRC §7611** — the special church-audit procedures. Restricts IRS church tax inquiries and
  examinations to those approved by a "high-level Treasury official" on "reasonable belief" of
  noncompliance, with mandatory written notice, staged inquiry-then-examination procedure, limited
  scope, and a shorter statute of limitations. The IRS has since reorganization treated the
  "appropriate high-level Treasury official" as the Commissioner of the Tax Exempt and Government
  Entities (TE/GE) Division; the assignment has been litigated (see United States v. Living Word
  Christian Center) — verify current IRS delegation before assuming a notice complies.
- **IRC §§511-514 (UBIT)** — churches owe unrelated business income tax on the same terms as any
  other 501(c)(3). Rental income is generally excluded under §512(b)(3) unless the property is
  debt-financed under §514, in which case the debt-financed fraction is taxed. Trade-or-business
  activity regularly carried on and not substantially related to exempt purposes is UBI, and Form
  990-T is due once gross UBI exceeds $1,000.

## Standard Deliverables

A request in scope resolves into one of these artifacts:

- **Church-status memo** — applying the 14-point test to a specific congregation, with written
  conclusion and residual risks.
- **"Should we file Form 1023 anyway?" decision memo** — grantor, state, and reputational trade-
  offs, with a recommendation.
- **Integrated-auxiliary classification memo** — for a seminary, mission board, publishing arm,
  denominational agency, retreat center, or affiliated ministry, walking the three-part test.
- **Group-exemption package or update** — for a denomination: initial group-ruling readiness
  review (subject to current IRS moratorium), annual subordinate-list update, or onboarding
  checklist for a new subordinate.
- **Federal-filing map for the church** — what the church does NOT file (990/990-EZ/990-N) and
  what it DOES still file (941, W-2/1099, 1098-C, 8282, 5578, 990-T if UBI).
- **UBIT analysis** — for a specific revenue stream (parking-lot rental, cell tower lease,
  bookstore, coffee shop, retreat rentals, thrift store, bulletin advertising, sponsorships), with
  Form 990-T threshold and estimated-tax implications.
- **§7611 response plan** — when an IRS letter arrives: church tax inquiry or examination; were
  procedural prerequisites met; what is the scope; what is the church's response window.

## Determining Whether an Organization Is a "Church" for IRC Purposes — Numbered Checklist

Run this whenever the user asks "are we a church for tax purposes" or is claiming church status on
a filing, a state exemption application, or in response to an IRS letter. The failure mode is
concluding "yes" from religious identity alone without walking the 14 characteristics.

1. **Purpose confirmation**: confirm the org is organized and operated for religious purposes
   under §501(c)(3) substantively. If it fails substantive §501(c)(3), the procedural specialness
   is moot.
2. **Distinct legal existence**: identify the state-law entity (nonprofit corporation,
   unincorporated association, trust). "Distinct" means not merely a program of another org.
3. **Regular worship + regular congregation**: the practical center of gravity. Regularly
   scheduled worship (weekly or more is the archetype) held for an identifiable, returning
   community, not primarily for the founder's household or a broadcast audience.
4. **Established place of worship**: a fixed, regularly used location — owned, leased, or shared.
   A church that meets in a school gym or a mosque in a leased storefront still qualifies; a
   purely virtual or broadcast-only ministry with no gathering place trends against.
5. **Ecclesiastical government + code of doctrine + creed and form of worship**: a recognizable
   polity (elder-led, congregational, denominational, imam-led, rabbinic-led), an articulated body
   of teaching, and a recognizable worship form. Write them down in a doctrinal statement,
   siddur/liturgy/prayer-book use, or a governing document.
6. **Ordained ministers, selected after prescribed studies + minister-preparation pathway**: name
   the tradition's ordination or recognition process (seminary, yeshiva, madrasa, monastic
   training, denominational credentialing, apprenticeship under a recognized teacher). A sole
   self-appointed founder with no external recognition trends against.
7. **Religious instruction of the young ("Sunday schools")**: identify the tradition's equivalent —
   Sunday school, Hebrew school, weekend Islamic school, dharma school, catechism, first-communion
   prep, bar/bat mitzvah prep, youth halaqa. Absence is not fatal; presence weighs heavily.
8. **Membership discipline**: an identifiable membership or its tradition's equivalent — regular
   congregants, registered families, mosque or temple members. Being part of a denomination is
   fine.
9. **Distinct religious history + literature of its own**: recognizable tradition (denominational,
   ancient, or newly emerging); "literature of its own" is satisfied by sermons, a newsletter,
   prayer book, study guide, Sunday-school curriculum, or tradition-specific liturgical texts.
10. **Weigh, do not tally**: no fixed number of factors is required. The associational features —
    regular worship, regular congregation, established place, community-recognized clergy, and
    instruction of the next generation — carry the most weight. Traditions that express these
    differently (a Quaker meeting with no ordained minister, a Buddhist sangha with a teacher
    rather than seminary-trained clergy) are not disqualified when the associational substance is
    there.
11. **Write the conclusion**: "The organization is / is not a church for IRC §§508(c)(1)(A) and
    6033(a)(3)(A)(i) purposes because [factors satisfied], notwithstanding [factors weak or
    absent], based on the 14-point test and IRS Publication 1828." Note residual risk if any weak
    factor could become material on audit.

## Integrated-Auxiliary Classification — Numbered Checklist

Use this when the user has an affiliated seminary, mission board, publishing house, denominational
agency, denominational retreat center, denominational counseling center, or campus ministry and
wants to know whether it is (a) an integrated auxiliary — no Form 990 required — or (b) an ordinary
501(c)(3) affiliated with a church that still files a 990. The failure mode is stopping at
"affiliated" and skipping the internal-support test.

1. **501(c)(3) status**: confirm the entity itself is (or is applying to be) a §501(c)(3). An
   entity without its own §501(c)(3) status (and not covered by a group ruling) fails the first
   prong regardless of affiliation.
2. **Affiliation with a church or convention/association of churches**: Reg. §1.6033-2(h)(2)
   defines "affiliated" — governance/control links (shared board seats, appointment powers,
   bylaws referencing the church), coverage by the same group ruling, or an authoritative
   affiliation letter from the church or denomination. Loose branding or theological alignment is
   not enough.
3. **Internal support test**: does the org normally receive more than 50% of its support from
   church contributions and internal denominational sources, rather than from (a) governmental
   sources, (b) fees charged in the exercise of exempt functions, or (c) admissions, sales, or
   receipts from unrelated trades or businesses? If majority support is grants, tuition, fees, or
   program income, the entity generally does NOT clear internal support and is NOT an integrated
   auxiliary — even though 501(c)(3) and church-affiliated. It must file Form 990/990-EZ/990-N
   like any other charity.
4. **Special education/seminary carve-outs**: elementary and secondary schools, colleges and
   universities, and typically seminaries and mission societies have special treatment inside
   Reg. §1.6033-2(h) — often treated as integrated auxiliaries without meeting the internal-
   support test. Read the reg against the entity's activities before concluding.
5. **Recheck annually**: internal support is measured "normally," so a one-year swing doesn't
   flip classification, but a sustained shift does. A denominational counseling center that was
   internally supported at founding and now runs 80% on insurance-billed fees has probably lost
   integrated-auxiliary status and needs to start filing a 990.
6. **Document the conclusion**: write a short classification memo (entity, three-prong analysis,
   conclusion, review date). This is what you hand the auditor, the state, or the grantor when
   they ask "why doesn't this ministry file a 990."

## Group Exemption Rulings for Denominations

A group exemption ruling lets a **central organization** (denomination, association, convention of
churches) obtain a single IRS determination covering itself plus its listed subordinates
(congregations, agencies, missions, camps, schools). Subordinates then do not each file a 1023.

- **Governing authority**: Rev. Proc. 80-27, modernized by Rev. Proc. 2023-5 and successors.
  Read the current-year Rev. Proc. before filing anything.
- **Current IRS posture**: the IRS placed a moratorium on accepting new group exemption
  applications beginning in 2020, pending revised procedures (Notice 2020-36 and successors).
  Verify current status before advising a client a new group ruling is available. Existing group
  rulings continue to function.
- **Central-org obligations**: general supervision or control of subordinates; maintenance of an
  accurate subordinate list; annual group-ruling update filed at least 90 days before the close
  of the central org's accounting period, listing subordinates added, deleted, or changed;
  ensuring subordinates are of substantially the same character as those originally covered.
- **Subordinate obligations**: authorize inclusion; agree to the central org's supervision terms;
  notify the central org of material changes (dissolution, name change, address, activities).
  Subordinate churches remain independently eligible for automatic §508(c)(1)(A) exemption whether
  or not they appear on a group roster.
- **Independent (non-denominational) congregations**: cannot be added to another denomination's
  group ruling merely for convenience. Their automatic §508(c)(1)(A) exemption is sufficient in
  law but does not produce a stampable determination letter — see the 1023 decision section below.
- **Practical value of appearing on the group ruling**: the central org can furnish a subordinate
  a copy of the group determination letter and a listing letter confirming the subordinate is on
  the current roster — the artifact grantors, banks, and states want.

## The Federal-Filing Map for a Church

Churches, their integrated auxiliaries, and conventions/associations of churches are exempt from
Form 990/990-EZ/990-N. They are **not** exempt from most other federal filings. Build this map for
every church you advise.

- **Form 1023 or 1023-EZ**: NOT required (§508(c)(1)(A)). Optional — see decision section below.
- **Form 990, 990-EZ, 990-N**: NOT required (§6033(a)(3)(A)(i) and (iii)).
- **Form 941 (Employer's Quarterly Federal Tax Return)**: REQUIRED for withholding on non-clergy
  employees. Clergy are treated specially — withholding is not required (though voluntary
  withholding under a §3402(p) agreement is common) — but any non-clergy staff (secretaries,
  custodians, musicians treated as employees, childcare workers, school teachers) create Form 941
  liability. See `nonprofit-faith-finance-clergy-comp` for clergy-side detail.
- **Forms W-2 and 1099-NEC / 1099-MISC**: REQUIRED for wages and payments to independent
  contractors. Includes W-2s for clergy (clergy get W-2s even though they pay their own SECA and
  can have a housing allowance excluded).
- **Form 1098-C**: REQUIRED when the church receives a donated motor vehicle, boat, or airplane
  valued over $500 and disposes of it. Written acknowledgment to the donor within 30 days of sale
  or use.
- **Form 8282**: REQUIRED when the church disposes of donated non-cash property (other than cash
  or publicly traded securities) within 3 years of receipt if the donor's claimed value exceeded
  $500. Filed with IRS and copy to donor within 125 days of disposition.
- **Form 8283 acknowledgment**: for non-cash donations over $5,000 (over $500 for vehicles), the
  church signs Section B of the donor's Form 8283.
- **Form 5578**: annual certification of racial nondiscrimination policy for church-operated
  schools — REQUIRED for any church that operates a school (K-12 or preschool) that would
  otherwise file a 990.
- **Form 990-T**: REQUIRED when the church has $1,000 or more of gross unrelated business income
  in the tax year. See UBIT section below.
- **Backup withholding and Form 945**: if applicable.
- **Federal unemployment tax (FUTA)**: churches are generally exempt from FUTA under §3306(c)(8).
  State unemployment varies — many states also exempt but some require coverage or offer
  reimbursable-employer status.

The rule of thumb: **the 990-exemption is an exemption from the annual information return, not
from being an employer or a tax collector**. Every church with paid staff or vehicle donations or
UBI has federal filings.

## Church UBIT — Deep Dive

Churches owe UBIT on the same terms as other §501(c)(3)s. Run the three-part test on every
non-donation revenue stream: (1) a trade or business, (2) regularly carried on, (3) not
substantially related to the church's exempt (religious) purposes.

- **Parking-lot rentals to non-members**: renting the church parking lot on weekdays to commuters
  or event-goers is generally UBI. If the church merely owns the lot and rents it without services
  (no attendant, no ticketing services), rental income may be excluded under §512(b)(3) as passive
  rental of real property — unless the lot is debt-financed under §514.
- **Coffee shops and bookstores open to the public**: if the shop is primarily for the convenience
  of members and attendees (§513(a)(2)), it is not UBI. If it is a commercial coffee shop open to
  the neighborhood, it generally is UBI. Draw the line by looking at signage, hours, marketing,
  and customer mix.
- **Cell tower leases on the church roof or steeple**: passive rental of real property under
  §512(b)(3) is generally excluded from UBI. **But** if any portion of the property is
  debt-financed (mortgage on the sanctuary), §514 pulls the debt-financed fraction back into UBI.
  Also watch mixed leases — a cell-tower deal that includes services (power, maintenance, security
  monitoring) beyond bare space can lose the §512(b)(3) exclusion.
- **Advertising vs. sponsorship in bulletins, programs, and websites**: **advertising income is
  UBI**; **qualified sponsorship payments** under §513(i) are not, as long as the payment does not
  include qualitative or comparative language, price information, or an endorsement — a plain
  "This service sponsored by [Business Name]" is generally a sponsorship; "Best plumber in town —
  call 555-1212 for 20% off" is advertising.
- **Thrift stores operated by the church**: substantially-all-volunteer-labor exception under
  §513(a)(1) removes the activity from UBI even if commercial. If paid staff exceed the volunteer
  base, the exception is lost.
- **Retreat center rentals to outside groups**: renting to outside religious retreats is often
  substantially related; renting the same facility to secular corporate off-sites is generally UBI
  unless another exception applies. Split-use facilities need percentage-of-use tracking.
- **Wedding and funeral fees for non-members**: usually not UBI when integrated with religious
  services provided by clergy; fee-for-facility-only-use by non-members trends toward UBI (also see
  `nonprofit-faith-facilities-sanctuary` for the facility side).
- **Investment income, dividends, interest, royalties**: generally excluded under §512(b)(1),
  (b)(2), and (b)(5) unless debt-financed.

**Form 990-T mechanics**: the church files 990-T if gross UBI is $1,000 or more; tax is computed
at the corporate rate. Estimated taxes on Form 990-W quarterly if tax owed will exceed $500. UBI
losses can offset UBI gains within each unrelated trade or business ("silo" rule under §512(a)(6));
losses may not offset the church's exempt-purpose activities.

## IRC §7611 Church Audit Procedures — Deep Dive

The §7611 procedures apply to any IRS **inquiry into or examination of a church** to determine
tax liability or exempt status. They apply narrowly — they do NOT protect an integrated auxiliary
audit as such, they do NOT protect a payroll (Form 941) audit, and they do NOT protect audits of
non-church affiliated organizations. Confirm the target and the scope before invoking §7611.

- **Reasonable-belief threshold**: an inquiry may begin only if an "appropriate high-level Treasury
  official reasonably believes on the basis of the facts and circumstances recorded in writing"
  that the church may not qualify for exemption or may be engaged in taxable activities.
- **High-level Treasury official**: originally the Regional Commissioner. After IRS reorganization,
  the IRS designated the **Director of Exempt Organizations**, later shifted to the **Commissioner
  of TE/GE**. This assignment was ruled inadequate in *United States v. Living Word Christian
  Center* (D. Minn. 2009), and the IRS has since revised its position more than once. Verify the
  current delegation order against the signature on the notice.
- **Two-stage procedure**: (1) **Church Tax Inquiry** — a written notice sent to the church
  explaining the concerns, the general subject matter, the church's right to a conference before
  examination, and the general subject matter of the inquiry. (2) **Church Tax Examination** — a
  separate written notice, sent at least 15 days after the inquiry notice, specifying the records
  and religious activities to be examined and offering a pre-examination conference.
- **Scope**: examination is limited to what is necessary to determine liability, and religious
  activities may be examined only to the extent necessary to decide whether the org qualifies as a
  church or is engaged in an unrelated trade or business.
- **Two-year completion rule**: an examination must generally be completed within two years of the
  examination notice.
- **Statute of limitations**: shorter than the general SOL for exemption revocation and UBIT — 3
  years back for UBIT; only the tax year at issue plus (in cases of fraud) prior years, per the
  §7611 limits.
- **Narrower protection outside §7611**: §7611 does NOT apply to (a) inquiries into whether an
  organization is actually a church, if the IRS is treating it as not-a-church; (b) inquiries into
  criminal matters; (c) inquiries into third-party recordkeeping; (d) certain routine payroll and
  information-return audits (Form 941, W-2 matching). A payroll audit that opens the door to
  substantive-status questions can create dispute about whether §7611 was triggered — get counsel.
- **Enforcement history**: church audits have been rare and often controversial (see the political-
  campaign-intervention investigations of the mid-2000s, and subsequent litigation over the
  §7611 delegation). The rarity does not make §7611 optional — always check the notice against
  the statute.

## Should the Church File Form 1023 Anyway? — Decision Framework

Independent (non-denominational, non-group-covered) congregations often ask this. There is no
right answer for every church; frame the tradeoffs and recommend.

- **In favor of filing 1023 anyway**: (1) grantor foundations routinely require the determination
  letter and will not fund without one regardless of automatic status; (2) many state agencies
  (income-tax exemption, charitable-solicitation registration, sales-tax exemption, some property-
  tax offices) want a copy; (3) banks, merchant processors, and payment platforms often ask for
  the letter to open accounts or grant nonprofit rates; (4) it produces a searchable IRS record
  (Publication 78 / Tax Exempt Organization Search) donors and auditors can independently verify;
  (5) if the church later reorganizes or spins off a school or affiliate, a determination letter
  simplifies everything downstream.
- **Against filing**: (1) filing fees ($275 for 1023-EZ, $600 for full 1023); (2) full 1023 is a
  substantial narrative + financials package requiring outside help for most churches; (3) the
  church has affirmatively invited IRS review of its organization and operations; (4) no
  substantive protection is lost by not filing — automatic exemption is real; (5) for a small,
  all-donor-funded, single-site congregation with no grant plans and no state registration
  requirement, the practical benefit is marginal.
- **Recommendation shape**: for a church that (a) wants grant funding, (b) is in a state that
  requires charitable-solicitation registration for churches, or (c) plans to grow beyond a small
  member-funded model — file the 1023 (or 1023-EZ if eligible) proactively. For a small member-
  funded congregation with none of those pressures — the automatic exemption is enough; document
  it with a church-status memo and be ready to explain it to bankers.

## State-Level Implications

State law rides on top of federal exemption and diverges materially. Cover the state overlay when
scoping any church-status advice; do not stop at federal.

- **State income-tax exemption** usually piggybacks on §501(c)(3) status. Some states auto-
  recognize federal exemption on receipt of the determination letter; others require a separate
  state application. Proving federal exemption without a determination letter is harder.
- **Sales-tax exemption for church purchases**: highly state-specific. Some states exempt church
  purchases automatically; some require a state-issued exemption certificate; some exempt only
  certain categories (Bibles, prayer books, worship supplies).
- **Property-tax exemption** for the sanctuary and parsonage is entirely state property law —
  covered by `nonprofit-faith-facilities-sanctuary`, not this skill. Federal §501(c)(3) status is
  neither necessary nor sufficient for state property-tax exemption.
- **State charitable-solicitation registration**: most states that require registration exempt
  churches by statute, but not all, and exemptions vary in scope. Examples of variation:
  Illinois generally exempts religious corporations from AG registration; Virginia exempts
  churches from Solicitation of Contributions Law registration; New York exempts most religious
  corporations from Article 7-A but not automatically (see N.Y. Exec. Law §172-a); California
  requires most religious corporations to register with the AG Registry of Charitable Trusts
  unless a specific exemption applies; Florida exempts "bona fide" religious institutions from
  Ch. 496; some states exempt churches themselves but not their affiliated fundraising
  subsidiaries. Confirm state-by-state at the point of advice — an exemption in the home state
  does not follow the church to states where it fundraises. Route multi-state mechanics to
  `nonprofit-charitable-registration`.

## Common Failure Modes

- **Automatic exemption confused with automatic recognition**: the church assumes that because it
  is automatically exempt under §508(c)(1)(A), a grantor foundation must accept that. Foundations
  don't. Fix by explaining the difference between substantive exemption (automatic) and an IRS
  determination letter (only issued on filing) and, where grants matter, recommending the 1023.
- **Integrated-auxiliary status claimed without the internal-support test**: a denominational
  counseling center or camp is claimed as an integrated auxiliary based only on affiliation, and
  the 990 is never filed. If income is majority fees or grants, the entity is not internally
  supported and owes 990 filings, with escalating penalties on discovery. Fix by running the full
  three-prong test annually and documenting.
- **Church-affiliated 501(c)(3) treated as a church**: a related legal-aid ministry, food pantry
  corp, or K-12 school is treated as "the church" for 990 purposes when it is actually a separate
  §501(c)(3) that must file. Fix by mapping every legal entity in the ministry family and
  classifying each individually: church, integrated auxiliary, or ordinary §501(c)(3).
- **Ignoring UBIT because "we're a church"**: cell tower on the roof + mortgage on the sanctuary
  produces UBI via §514 debt-financing; nobody files 990-T; discovery on audit produces back tax,
  interest, penalties. Fix by inventorying every non-donation revenue stream annually and running
  the three-part UBI test plus §512(b)(3) rental analysis and §514 debt-financing check.
- **Missing payroll filings on the theory that "clergy don't pay tax"**: clergy have dual tax
  status (income tax + SECA) — they still get a W-2, and any non-clergy staff generate Form 941
  obligations. Fix by mapping every worker to clergy vs. non-clergy, employee vs. contractor,
  and building a filings calendar. Route clergy-comp mechanics to
  `nonprofit-faith-finance-clergy-comp`.
- **Group-ruling roster drift**: the denomination's subordinate list has not been updated in
  years; congregations that closed are still on it; a new congregation is not on it. Fix by making
  the annual group-ruling update a calendared responsibility with a named owner, cross-checked
  against the denomination's own congregation database.
- **Invoking §7611 for the wrong audit**: the church loudly demands §7611 procedures when the IRS
  is running an ordinary payroll audit or auditing a non-church affiliate; the church loses
  credibility and its counsel-of-record standing. Fix by first classifying the notice (what entity,
  what tax year, what tax, what stage) and only then determining whether §7611 protections apply.
- **"Church" claimed by an online-only ministry with no gathering community**: a broadcast or
  podcast ministry with no worshiping congregation claims church status. The IRS 14-point test
  centers associational features that a broadcast-only ministry does not have. Fix by advising a
  more defensible classification (ordinary §501(c)(3) religious org that files a 990) rather than
  claim-and-hope.

## Practitioner vs. Advisor Framing

- **As the church business administrator, treasurer, or senior clergy (or a chief-of-staff drafting
  for one)**: your job is to keep the church's federal-tax house tidy without spending its money
  on things it does not need. Do the church-status memo once and file it in the corporate record.
  Do the integrated-auxiliary classification for each affiliated ministry once, and re-check
  annually against the internal-support test. Build the federal-filings calendar (941 quarterly,
  W-2/1099 January, 990-T May 15 if applicable, 5578 if you operate a school, 8282 event-driven,
  1098-C event-driven) and the state overlay (state income, sales, property, charitable
  solicitation) explicitly — most compliance failures in this space are calendar failures. Decide
  once, in writing, whether the church will file Form 1023 anyway, and revisit the decision when
  the church starts seeking foundation grants, planting daughter congregations, opening a school,
  or expanding into new states. When an IRS letter arrives, do not respond substantively before
  classifying it (regular correspondence vs. §7611 inquiry vs. §7611 examination vs. non-§7611
  audit like payroll) and getting church-tax counsel involved — the §7611 protections are real but
  only if invoked correctly.

- **As an advisor (CPA, attorney, denominational staffer, or consultant)**: your first move is
  disambiguating the entity — is this a church, an integrated auxiliary, a convention or
  association of churches, an ordinary church-affiliated §501(c)(3), or a for-profit church-owned
  entity — because the entire filings map turns on the answer, and the church often does not know.
  Ask for the certificate of incorporation, EIN letter, any determination letter, any group-ruling
  listing letter, the last three years of financials, and the payroll register before opining. When
  a client is on a group ruling, verify current listing with the central org's group-ruling
  administrator; when a client is independent, do the 14-point analysis and make an explicit
  filing-strategy recommendation instead of leaving "automatic exemption" as an unstated default.
  Do not confidently opine on §7611 mechanics without checking the current delegation of the
  "high-level Treasury official" role — it has moved and been litigated more than once — and do
  not assume the substantive-exemption protection extends to payroll or auxiliary audits. On UBIT,
  push clients to inventory revenue streams proactively rather than annually rediscovering a
  cell-tower lease at year-end; on state overlay, treat charitable-solicitation registration and
  property-tax exemption as separate work products routed to
  `nonprofit-charitable-registration` and `nonprofit-faith-facilities-sanctuary` respectively.
