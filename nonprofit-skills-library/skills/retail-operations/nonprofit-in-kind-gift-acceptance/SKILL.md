---
name: nonprofit-in-kind-gift-acceptance
description: "Handles donor-side tax receipting/valuation for non-cash gifts: IRS Form 8283, qualified appraisals over $5,000, gift acceptance policy for accepting/declining in-kind donations. Use for 'donor wants a receipt for a car/stock/art,' 'do we need an appraisal,' 'write our gift acceptance policy.' Physical intake/grading of resale goods is nonprofit-donation-intake-grading."
license: MIT
---

# Nonprofit In-Kind Gift Acceptance

## When to Use This Skill

Use this skill for donor-side tax documentation and policy decisions on any non-cash (in-kind) gift —
not limited to resale/thrift goods: real estate, vehicles, securities, art, equipment, intellectual
property, or a large batch of resale-bound goods that crosses a tax-reporting threshold. Typical
triggers: "a donor wants a tax receipt for a car they gave us," "does this donation need a qualified
appraisal," "help a donor complete Form 8283," "write or update our gift acceptance policy," "should
we accept this donated property given the liability/cost to unload it."

**Boundary:** this skill is the donor-side tax valuation/receipting and acceptance-policy layer. The
physical drop-off logistics, sorting, quality grading, and basic at-donation receipt (no value stated)
for resale-bound goods is `nonprofit-donation-intake-grading` — that skill issues the simple receipt
at time of donation; this skill handles what happens when a donor needs more than that (a stated-value
acknowledgment, Form 8283 signature, or appraisal cooperation) or when the item isn't resale goods at
all. The strategic decision to run a resale retail enterprise in the first place — should the org open
a thrift store, what business model — is `nonprofit-revenue-diversification`; this skill assumes that
decision is already made and focuses on the tax/compliance/acceptance-policy mechanics of individual
in-kind gifts.

## Core Framework: The Substantiation Ladder

IRS non-cash charitable contribution rules scale documentation requirements to gift size — treat this
as a ladder, and always confirm current dollar thresholds and forms against current IRS guidance
before finalizing a specific donor's paperwork, since thresholds and form details are periodically
updated:

1. **Under $250**: donor needs a receipt (or reliable written records) but no special appraisal or
   form; the organization's basic at-donation receipt from `nonprofit-donation-intake-grading`
   typically satisfies this tier.
2. **$250-$500**: donor needs a **contemporaneous written acknowledgment (CWA)** from the
   organization — dated, describing the property, and stating whether any goods/services were
   provided in exchange (and their value, if so). No item-by-item value is stated by the
   organization; the donor determines fair market value themselves.
3. **$500-$5,000**: donor must file **IRS Form 8283, Section A**, generally with tax return, describing
   the property and how/when acquired; the organization does not sign this section but may be asked
   to confirm receipt.
4. **Over $5,000** (except publicly traded securities): donor generally needs a **qualified
   appraisal** by a qualified appraiser and must file **Form 8283, Section B**, which requires the
   organization's authorized representative to sign acknowledging receipt of the described property
   — signing acknowledges receipt only, not the appraised value, and the organization should never
   represent or imply agreement with the donor's valuation.
5. **Over $500,000**: the appraisal itself generally must be attached to the donor's return.

Note the **donee reporting trigger**: if the organization sells, exchanges, or disposes of
contributed property (Form 8283 Section B item) within 3 years of the contribution, it may need to
file **Form 8282** with the IRS and send a copy to the donor — directly relevant to resale operations,
since reselling a high-value donated item within the window can trigger this filing. Track Section-B
items with a disposal date for this reason.

## Standard Terminology

- **Contemporaneous written acknowledgment (CWA)**: the donor's required receipt for gifts of $250+,
  obtained before the donor files their return; must state whether goods/services were exchanged.
- **Qualified appraisal / qualified appraiser**: an appraisal meeting specific IRS requirements
  (performed no more than 60 days before the gift, by an appraiser meeting defined credentialing and
  independence requirements) required for most non-cash gifts over $5,000.
- **Form 8283**: the donor's tax form for reporting non-cash charitable contributions; Section A for
  $500-$5,000, Section B (with organization signature) for over $5,000.
- **Form 8282**: the organization's required filing if it disposes of a Section-B-reported item within
  3 years of receiving it, notifying the IRS and donor of the disposal and sale price.
- **Gift acceptance policy**: the board-adopted written policy defining what types of in-kind gifts
  the organization will and won't accept (e.g., real estate with environmental liability, vehicles
  needing costly repair/disposal, restricted or encumbered property) and the approval chain for
  exceptions.
- **Quid pro quo contribution**: a gift where the donor receives something of value in return (e.g., a
  gala ticket); the CWA must state the fair market value of what was received so the donor can deduct
  only the excess.

## Step-by-Step: Handling an In-Kind Gift Request

1. **Classify the gift against the substantiation ladder** by the donor's estimated value to determine
   which documentation tier applies.
2. **Check the gift against the written gift acceptance policy** before accepting anything unusual
   (real estate, vehicles with liens or environmental issues, restricted-use property, gifts with
   ongoing carrying costs) — route anything outside standard categories to the approval chain the
   policy defines (ED, board, or finance committee depending on gift size/type) rather than accepting
   informally at the point of donation.
3. **Issue the CWA promptly** for any gift of $250+, before the donor's tax filing deadline, describing
   the property without stating a dollar value and confirming no goods/services were exchanged (or
   their value, if a quid pro quo situation applies).
4. **For gifts in the $500-$5,000 Form 8283 Section A range**, be prepared to confirm receipt details
   to the donor or their preparer but do not sign anything — Section A doesn't require an
   organizational signature.
5. **For gifts over $5,000**, direct the donor to obtain a qualified appraisal *before* the
   organization signs Form 8283 Section B, and have the authorized signer review the form to confirm
   it signs only for receipt-of-property, not appraised value — never let a signer casually co-sign
   a valuation.
6. **Log every Section-B-signed item with its receipt date** in a tracking register so the 3-year
   Form 8282 disposal-reporting window is monitored — this matters directly for a resale operation
   likely to sell a high-value item well within 3 years.
7. **File Form 8282 within the required window** if a tracked item is sold/disposed of within 3 years
   of the original gift, sending a copy to the original donor as required.
8. **Review and update the gift acceptance policy** at least every 1-2 years or whenever the org
   encounters a new gift type it hadn't anticipated, and get board adoption/re-adoption on record.
9. **Train front-line intake and development staff** to recognize when a donation crosses from
   "issue the basic receipt" (`nonprofit-donation-intake-grading`) into this skill's territory —
   the donor asking for "a receipt with a value on it" or mentioning an appraisal is the trigger to
   hand off.

## Standard Deliverables

- Board-adopted gift acceptance policy
- Contemporaneous written acknowledgment (CWA) template
- Form 8283 Section B signature/review procedure
- Section-B item tracking register (receipt date, description, 3-year disposal window)
- Form 8282 filing procedure

## Common Failure Modes

- **Organization staff stating or implying a dollar value** on a receipt or in conversation with a
  donor, which is the donor's own responsibility to determine, not the recipient organization's.
- **Signing Form 8283 Section B without understanding it acknowledges receipt only**, then facing a
  dispute if the appraised value is later challenged by the IRS.
- **No tracking of Section-B items' 3-year disposal window**, missing a required Form 8282 filing when
  a high-value donated item is resold quickly.
- **No written, board-adopted gift acceptance policy**, leading to ad hoc acceptance of high-liability
  gifts (encumbered real estate, vehicles needing costly disposal) at the point of donation.
- **Front-line intake staff issuing only the basic at-donation receipt** for a gift that actually needs
  a CWA or Form 8283 cooperation, leaving the donor under-documented at tax time.
- **Appraisal obtained after, not before, signing Section B**, creating sequencing problems with the
  IRS's 60-day appraisal-timing requirement.

## Practitioner vs. Advisor Framing

- **As development/finance staff**, keep a simple running log of every gift that crosses the $250 and
  $5,000 tiers, since these are the two decision points where documentation requirements change
  materially — most errors happen when a gift is handled at the wrong tier rather than an intentional
  policy failure.
- **As a consultant advising a nonprofit on gift acceptance**, treat the written policy as the
  deliverable that prevents the most damage — most in-kind gift problems trace back to an informal
  "yes" accepted at the point of donation (a car needing $3,000 in disposal costs, real estate with an
  environmental lien) rather than a documentation error, so prioritize getting a board-adopted
  acceptance policy with a clear exception-approval chain before refining the paperwork mechanics.
