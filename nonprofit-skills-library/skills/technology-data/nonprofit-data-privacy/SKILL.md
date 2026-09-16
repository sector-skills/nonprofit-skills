---
name: nonprofit-data-privacy
description: "Designs donor and constituent data privacy practices: privacy policy and donor Bill of Rights language, PCI-DSS scope reduction for online donation pages, data-sharing/co-op and list-rental agreements, consent and opt-in management, breach response, and CCPA/GDPR/state-privacy-law applicability for nonprofits. Use for privacy policy drafting or review, PCI compliance questions about card data handling, donor list rental/exchange agreements, and data subject access/opt-out requests. Does not cover choosing or configuring the CRM itself (nonprofit-donor-crm) or selecting a payment processor/giving platform (nonprofit-digital-fundraising-tools)."
license: MIT
metadata:
  supervision: "expert-required"
  supervision_note: "Privacy policy, PCI-DSS scope and breach response carry statutory obligations."
  date_added: "2026-09-07"
  date_added_source: "git:1860ed47a83901ff5e6d45abc4a2ef05be8fd4cd"
---

# Nonprofit Data Privacy

## When to Use This Skill

Use this skill when the request is about the *rules and safeguards* governing donor/constituent
data, rather than the systems that store it. Concrete triggers:

- "Draft/review our donor privacy policy."
- "Are we PCI compliant if we use [payment processor] on our donation page?"
- "Can we rent or exchange our donor mailing list with another nonprofit?"
- "A donor asked us to delete their data / stop emailing them — what's our process?"
- "Do CCPA or GDPR apply to us? We have donors in California/Europe."
- "We had a data breach (lost laptop, phishing, vendor incident) — what do we do?"
- "Write our donor Bill of Rights / data-sharing opt-out language."

**Boundary — hand off instead of answering here:**
- Picking or configuring the CRM, dedup, and segmentation tooling → `nonprofit-donor-crm`.
- Choosing an online giving platform or payment gateway → `nonprofit-digital-fundraising-tools`
  (this skill covers the *compliance requirements* that platform choice must satisfy, e.g. PCI
  scope, not the vendor comparison itself).
- General website terms of service or non-donor data (e.g., HR/employee data) is out of scope.

## For Practitioners: Building the Privacy Program

### 1. Start from the Donor Bill of Rights

The **Donor Bill of Rights** (jointly issued by AFP, AHP, CASE, and the Giving Institute) is the
sector-standard baseline: donors have the right to know how their gift is used, to be informed of
who is soliciting them, to have their name kept confidential/removed from lists on request, and to
expect that all relationships with the organization are handled with respect and professionalism.
Anchor your privacy policy language to these commitments, not generic legalese.

### 2. Write the privacy policy with these standard sections

A nonprofit donor privacy policy (standard deliverable, usually 1-2 pages, published on the
website) covers:

1. **What data is collected** (name, contact info, payment info, giving history, event/volunteer
   activity, website analytics/cookies).
2. **How it's used** (gift processing, tax receipts, stewardship communication, program reporting
   to funders in aggregate/de-identified form).
3. **Whether/how lists are shared or rented** — state explicitly whether the org ever
   rents/exchanges its donor list with other organizations; if it does, this must be disclosed and
   opt-out-able.
4. **Opt-out mechanism**: how a donor requests removal from mailing/calling/list-sharing, and the
   committed turnaround time (commonly 30 days per direct-mail industry norms).
5. **Data security measures** at a high level (encryption, access controls) without disclosing
   exploitable detail.
6. **Anonymous gift handling**: how donor-requested anonymity is enforced internally (e.g., a
   restricted-visibility flag in the CRM, not just a note).
7. **Children's data** if the org runs youth programs (COPPA considerations for under-13 data).
8. **Contact point** for privacy questions/requests.

### 3. PCI-DSS: scope it correctly, don't over-build

Most small/mid nonprofits should **never touch raw card numbers** — use a PCI-compliant
processor/gateway (Stripe, Authorize.Net, PayPal, or a giving platform with a hosted/embedded
payment field) so cardholder data never transits the org's own servers. This qualifies for
**SAQ A** (Self-Assessment Questionnaire A) — the lightest PCI compliance tier, applicable when
payment fields are fully outsourced to a PCI-validated third party via redirect or iframe.

- **Common failure mode**: a staff member takes a donor's card number over the phone and types it
  into a non-PCI system, or a form vendor's fields aren't truly hosted/iframed (this pushes the
  org into a heavier SAQ tier). Audit exactly how card data flows before claiming SAQ A.
- Never store full card numbers, CVV, or magnetic-stripe data in the CRM, spreadsheets, or email —
  even "just to look something up later." If a processor's data ever needs referencing, use the
  last-4/token reference only.
- Annual requirement: complete the applicable SAQ and, if a merchant services agreement requires
  it, an external vulnerability scan (ASV scan) — confirm with the payment processor which SAQ
  tier and scan requirements apply to the org's specific setup.

### 4. List sharing, co-ops, and rentals

- **List rental/exchange** (common in direct-mail-heavy orgs) must be disclosed in the privacy
  policy and must honor any prior donor opt-outs before the list is shared.
- Use a written **data-sharing agreement** with any list broker or exchange partner specifying
  permitted use (one-time mail use only, no retention, no resale), a suppression file process, and
  data destruction after use.
- Compiled/enhanced donor data purchased from a data co-op still requires disclosure that
  supplemental data sources are used.

### 5. State and international privacy law applicability

- **CCPA/CPRA (California)**: applies based on revenue/data-volume thresholds that most nonprofits
  fall under, but nonprofits are not categorically exempt for all activities (e.g., a nonprofit
  running a for-profit-like data business could trigger obligations) — check current thresholds
  rather than assuming blanket exemption, and note that CCPA's consumer-vs-nonprofit exemption is
  narrower than many assume.
- **GDPR**: applies if the org has donors/website visitors in the EU/UK and processes their
  personal data — commonly relevant to nonprofits with international program work or European
  fundraising. Requires a lawful basis for processing, clear consent for marketing email, and a
  data subject rights process (access, deletion, portability).
- **State breach notification laws**: nearly all US states require notifying affected individuals
  (and sometimes the state AG) within a defined window after a breach involving specific data
  types (SSN, financial account, etc.) — the notification clock and required content vary by
  state; identify which states the affected individuals reside in, not just where the org is
  based.
- Advisors should flag this as an area for actual legal counsel review, not a DIY answer — this
  skill helps structure the questions and draft language, not substitute for legal sign-off on
  final compliance determinations.

### 6. Breach and incident response

Standard deliverable: a short **incident response checklist**:

1. Contain (revoke access, isolate affected system/account).
2. Assess scope (what data, how many records, what states/countries affected individuals are in).
3. Notify per applicable state law timelines; involve legal counsel before public statements.
4. Notify the CRM/payment vendor if the breach originated or flowed through their system.
5. Document the incident and remediation for the board and, if relevant, cyber insurance carrier.
6. Post-incident: patch the specific gap (e.g., MFA enforcement, staff phishing training).

## For Advisors: Framing for the Board and Leadership

- Present privacy/PCI risk in terms the board acts on: reputational risk (a breach damages donor
  trust and future giving), financial risk (breach notification costs, potential fines, payment
  processor penalties for PCI non-compliance), and legal exposure.
- Recommend the org adopt a **written data privacy and security policy** approved by the board,
  not just a public-facing website statement — the internal policy should assign a responsible
  owner and an annual review cadence.
- If advising during a CRM or giving-platform selection (led under `nonprofit-donor-crm` or
  `nonprofit-digital-fundraising-tools`), inject PCI scope and data-sharing terms as selection
  criteria rather than an afterthought — vendor contracts should include a data processing
  addendum and breach notification obligations.

## Common Failure Modes

- Privacy policy exists but doesn't match actual practice (e.g., says lists are never shared, but
  the org participates in a co-op exchange).
- Card numbers captured outside a PCI-compliant flow (phone orders typed into email/spreadsheet).
- No process for honoring donor opt-out or "please remove me" requests, or no tracked turnaround
  time.
- Treating GDPR/CCPA as automatically inapplicable without checking actual donor geography or
  activity thresholds.
- No breach response plan until after an incident occurs.
