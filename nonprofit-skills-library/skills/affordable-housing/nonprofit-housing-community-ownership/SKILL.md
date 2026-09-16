---
name: nonprofit-housing-community-ownership
description: "Designs shared-equity community ownership models — community land trusts (tri-partite governance, ground leases, resale formulas), limited-equity housing cooperatives (share purchase, occupancy agreements, co-op boards), and deed-restricted ownership (index-based, appreciation-capped, and equity-share formulas) — plus perpetuity stewardship and model selection. Use when a user says 'should we start a community land trust,' 'explain our resale formula to a homebuyer,' 'draft the key terms for our ground lease,' 'convert our rentals into a limited-equity co-op,' or 'our deed restriction expires soon — how do we enforce and renew it.' Not for homebuyer selection, education, or post-purchase support, or program-level shared-equity resale formulas in a conventional homeownership program (use nonprofit-housing-homeownership-programs), for developing the housing or its capital stack (use nonprofit-housing-development-finance), or for general nonprofit board governance (use nonprofit-board-governance)."
license: MIT
metadata:
  supervision: "expert-required"
  supervision_note: "Ground leases and deed restrictions bind real property in perpetuity; all drafts require attorney review and county recording review before adoption."
  last_reviewed: "2026-09-12"
  date_added: "2026-09-12"
  date_added_source: "git:466adeb4b20092f7790a7d1d6b555af30dd69b99"
---

# Nonprofit Housing: Community Ownership and Shared-Equity Models

## When to Use This Skill

Use this skill to design, explain, or steward permanently affordable ownership housing where the public or nonprofit interest is protected by a legal instrument rather than by ongoing subsidy: community land trusts (CLTs), limited-equity housing cooperatives (LEHCs), and deed-restricted shared-equity homeownership. Trigger tasks include: "should we start a community land trust or just use deed restrictions," "our CLT ground lease is up for revision — what terms matter," "explain our resale formula to a seller," "convert our scattered-site rentals into a co-op," "our deed restrictions expire in 15 years — what's our renewal and monitoring plan," or "draft a stewardship policy for our shared-equity portfolio."

**Boundary:** this skill covers the ownership structures and their legal/economic architecture only. Selecting, educating, and supporting individual homebuyers is `nonprofit-housing-homeownership-programs` (this skill defines the *structure* the buyer enters, not the program cycle around it). Acquiring land, entitling, constructing, and capitalizing the housing — LIHTC, HOME, CDBG, and the rest of the capital stack — is `nonprofit-housing-development-finance`. General nonprofit board mechanics (agendas, committees, ED evaluation) is `nonprofit-board-governance` — this skill covers only the CLT/co-op governance features that are distinctive to shared-equity structures. Fair-housing analysis of occupancy rules is `nonprofit-housing-fair-housing`.

## The Three Core Models at a Glance

| Dimension | Community land trust | Limited-equity co-op | Deed-restricted ownership |
| --- | --- | --- | --- |
| What the owner holds | Fee title to building; 99-year ground lease on land | Membership share + occupancy agreement/proprietary lease | Fee title with recorded restriction |
| Affordability held by | Land ownership (nonprofit) | Corporation's lien-based equity limits | Covenant running with the land |
| Governance of steward | Tri-partite CLT membership elects board | Residents govern the co-op corporation | Steward is a third-party nonprofit or agency |
| Owner resale value | Set by lease's resale formula | Par/formula value of the share | Set by restriction's resale formula |
| Startup cost to steward | High (must own land) | High (must own/build the property) | Low (needs no land or buildings) |

All three are **shared-equity** models: the homeowner builds limited equity on an "asset-building" path while a public-interest holder preserves affordability for the next buyer. The steward's job is to make the affordability **perpetual** (or very long-term), not to run a one-time subsidy program.

## Community Land Trust Design

### Tri-partite membership governance

The classic CLT (from the Institute for Community Economics model, now carried by Grounded Solutions Network and the Lincoln Institute of Land Policy) divides voting members — and the board — into three equal thirds:

1. **Leaseholder third** — residents occupying CLT homes under ground leases. Elects one-third of the board.
2. **Community third** — residents of the defined geography the CLT serves (a neighborhood, municipality, or county, stated in the bylaws). Elects one-third.
3. **At-large (public) third** — anyone with an interest in the community's housing future: local officials, funders, clergy, nonprofit partners. Elects one-third.

Rules that make the structure work: no single third may control a majority; leaseholders should never hold more than one-third (or the CLT becomes a homeowners' association protecting resale value, not a community trust); community-third eligibility should exclude CLT staff and board members to keep it independent. Write minimum quorum requirements *per third* so an empty third cannot be papered over with at-large members. Amending the ground lease or dissolving the trust typically requires supermajorities plus separate majority approval of the leaseholder class — draft that into the bylaws.

### Ground lease: the instrument that does the work

The ground lease (almost always 99-year, renewable, and inheritable) — not the deed — carries the affordability and governance obligations. Every substantive obligation must live in the lease, because the CLT cannot rely on the deed to bind future lessees.

## Resale Formula Design (all models)

The resale formula is the single most consequential design choice in any shared-equity program: it sets the owner's return, the next buyer's price, and the subsidy the steward must replace at resale.

### Formula families

1. **Index-based — fixed percentage:** resale price = original price × (1 + r)^years, r typically 1.5%–3%. Simple to administer, no appraisal needed, decouples from local market swings. Risk: if local prices rise slower than r, resale prices drift above market.
2. **Index-based — external index:** same structure indexed to HUD area median income (AMI), CPI, or regional wages. AMI-indexing tracks buyer purchasing power directly, which is the point of the program.
3. **Appreciation-capped (shared appreciation):** owner receives a fixed share (commonly 25%–40%) of the *appraised appreciation*. Reward for market participation; requires appraisals at purchase and resale and can be volatile.
4. **Equity-share / mortgage-based:** owner recovers down payment + mortgage principal amortized + documented improvements, sometimes plus a modest interest factor. Strongest affordability preservation, weakest asset-building; can leave an owner with almost nothing after a short hold in a flat market.
5. **Points-based:** base rate (e.g., 0.5%–1%/yr) plus points for household size, tenure length, improvements. Flexible but must be fully specified in advance to avoid discretionary disputes.
6. **Par-value (co-ops):** share resells at original purchase price, sometimes plus a small annual credit. Common for LEHCs.

### Cross-cutting formula rules

- **Improvements credit:** allow credited improvements only with pre-approval and receipts, capped or folded into the formula; uncapped credits are the most litigated clause in shared-equity housing.
- **Fair return:** if HOME funds are in the unit's history, 24 CFR 92.254 requires homeownership resale provisions that give the owner a fair return on investment and keep the home affordable to a reasonable range of low-income buyers — any formula must satisfy both prongs, and state/local grant terms may impose stricter standards.
- **State the formula in the instrument** (lease or restriction), not in program policy — policy can be amended by a board the homeowner never elected; the recorded/leased formula is what a court enforces.
- **Include a worked numeric example as an exhibit** so the seller's expectations are anchored at closing, not at resale.

### Worked example — one unit, three formulas

A household buys a CLT home for $180,000 (building only; land is leased), makes $5,000 of pre-approved improvements, and sells after 8 years. Appraised building value at resale: $260,000. AMI for the metro rose 22% over the period.

- **Fixed 1.5%/yr:** 180,000 × 1.015^8 = **$202,768** (+ $5,000 improvements if the formula credits them separately → $207,768).
- **Shared appreciation, 30% of appreciation:** appreciation = 260,000 − 180,000 = 80,000; owner keeps 30% = 24,000; resale price = **$204,000** (improvements usually credited fully under this formula → $209,000).
- **AMI-indexed:** 180,000 × 1.22 = **$219,600**.

The three prices differ by $17,000 for the identical household outcome. Compute all candidate formulas on the same worked example before the board picks one, and show what monthly payment each resale price implies for the next buyer at current rates. If the next-buyer payment exceeds the affordability target, the steward must either buy the price down with fresh subsidy or accept serving a higher AMI band — surface that trade-off explicitly in the memo.

## Ground Lease Key-Terms Outline

Standard sections to specify (deliverable is a key-terms outline for attorney drafting, never draft lease text yourself):

1. **Parties, premises, term** — CLT and lessee; 99-year term, renewable, inheritable, assignable to an income-qualified transferee.
2. **Lease fee** — monthly ground rent (often nominal, e.g., $25–$75); escalation and waiver during hardship.
3. **Use and occupancy** — principal-residence requirement; leasing/subletting limits.
4. **Construction and alterations** — CLT consent for structural changes; improvement approval process feeding the improvements credit.
5. **Resale** — resale formula (by reference to the exhibit), pre-approval of any listing, marketing rights and duties of both parties, timeline for CLT to produce a qualified buyer.
6. **CLT repurchase option / right of first refusal** — CLT may purchase at formula price within a fixed window (typically 15–45 days) after notice of intent to sell or a listed sale; procedures if the CLT declines.
7. **Inheritance** — devise to qualified heir (spouse/child living in home often regardless of income for a defined period); CLT repurchase from non-qualified heirs at formula price.
8. **Mortgagee protections** — this is what makes the home financeable: lender notice of default, opportunity to cure on the homeowner's behalf, assignment of lease to a new qualified buyer after acquisition, and no lease termination while a mortgage is in good standing. Leases missing standard lender protections get the home's mortgage application denied — Fannie Mae and Freddie Mac will purchase loans on CLT homes only when the ground lease meets their review criteria (a market opened up under the FHFA Duty to Serve obligation), so have lender-relations counsel confirm conformity.
9. **Taxes and insurance** — homeowner pays property tax on improvements; specify how the land's assessment is handled (some states permit land exemption or proration for CLTs — check state law rather than assuming). Hazard insurance naming both parties.
10. **Maintenance, condition standards** — repair obligations, minimum condition at resale.
11. **Default and remedies** — notice and cure periods (typically 30 days), grounds for termination, eviction as last resort with relocation obligations.
12. **Amendment, recording, perpetuity** — amendment procedure requiring leaseholder-class consent for material changes; lease recorded in the land records so it binds successors; perpetuity/renewal language.

## Limited-Equity Housing Cooperatives

An LEHC is a corporation (under the state's cooperative statute — typically the same statute covering general cooperatives or a housing-cooperative chapter) whose members collectively own the property. Structure essentials:

1. **Membership share purchase** — the buy-in is a share (or shares) in the corporation, commonly a few thousand dollars (par or formula valued), NOT real estate equity. Financing is via a "share loan" (personal loan secured by the share and occupancy agreement), which fewer lenders offer than conventional mortgages — confirm local share-loan availability before committing to the model.
2. **Occupancy agreement / proprietary lease** — the member's right to occupy a specific unit; the equivalent of the ground lease for a CLT. It carries the resale formula, subletting rules, maintenance duties, and succession rights.
3. **Monthly carrying charge** — each member's share of the underlying blanket mortgage (if any) + operating costs + replacement reserves. The board sets it; set reserve deposits high enough to avoid special assessments, which are the classic co-op killer.
4. **Co-op board basics** — resident-members elect the board; the board approves memberships, enforces the occupancy agreement, and hires/oversees management. The board's membership-approval decisions are fair-housing-critical (see `nonprofit-housing-fair-housing`) — approve against written, objective, uniformly applied standards.
5. **Limited-equity discipline** — the regulatory agreement (with a funder) or the corporate documents cap share resale value per the formula; the corporation usually holds a repurchase right and reissues shares to the next approved member.
6. **Model context** — FHA Section 213 is the federal program that insures mortgages for cooperative housing development; many older LEHCs carry it. Most new ones are formed by nonprofits converting existing rental buildings, often with expiring-use properties — the conversion feasibility analysis belongs with `nonprofit-housing-development-finance`.
7. **When to choose it** — dense multi-family buildings, resident self-governance is a goal, and the community has (or can hire) competent co-op management. Weak member-governance capacity or thin reserves argue for a rental or CLT structure instead.

## Deed-Restricted Shared-Equity Ownership

The steward records a covenant running with the land (a "deed restriction," "affordability covenant," or "community housing covenant") against a fee-simple home it does not otherwise own.

- **Instrument anatomy:** recorded restriction binding successors; resale formula; income-eligibility of future purchasers; occupancy and leasing limits; steward's enforcement rights (below); term and renewal.
- **Term:** 30, 45, or 99 years, or perpetual. Fixed terms require a renewal/re-recording calendar (see stewardship); perpetual covenants face varying state-law enforceability — an attorney must confirm the state treats the reversion/option structure as valid.
- **Equity-share variants** beyond the formulas above: silent second mortgages (subsidy recorded as a soft second, repaid at resale, optionally with appreciation share) — common where a government grantor requires recapture instead of resale.
- **Federal-funds overlay:** HOME-assisted homeownership units must use either **resale** (formula-limited price to an income-eligible buyer) or **recapture** (repay the HOME subsidy) provisions — pick one per unit, document it, and never mix them within a single HOME unit.

## Perpetuity and Stewardship

Affordability that is not stewarded is affordability on loan. Build the stewardship system when the first unit closes, not when the first violation surfaces.

### Monitoring

1. Maintain a portfolio registry: recording data, term expiration dates, formula terms per cohort, owner contact info, mortgage and lien status.
2. Annual owner contact: confirm principal-residence occupancy, insurance, property tax status, and refinance intentions. Track refinance applications — a cash-out refinance that strips equity breaks the formula at resale.
3. Watch public records (deeds, foreclosure filings, tax sales) for transfers outside the program; a tax-foreclosure sale can extinguish a restriction if the steward does not redeem or intervene.

### Enforcement

1. **Repurchase option** — steward's right to buy at formula price on notice of sale (CLT: in the lease; deed-restricted: in the covenant).
2. **Right of first refusal** — triggered by a listed or contracted third-party sale; exercise window typically 15–45 days.
3. **Equitable relief** — suit to enjoin a non-conforming sale, to set aside a deed, or quiet title to enforce the covenant. Lapse is fatal: restrictions unenforced across transactions invite adverse claims; decades of lapsed monitoring can make covenants practically (and sometimes legally) unenforceable.
4. **Cure ladder** — notice → negotiation (buy-in to a corrected price or transfer to a qualified buyer) → repurchase/ROFR exercise → litigation. Litigation against your own homeowner is a last resort and a PR event; the policy should say so.

### Renewal and expansion of term

Calendar every fixed-term restriction five years before expiration; renew early (with owner consent or a negotiated incentive) rather than in the final year when the owner's incentive to refuse is highest. Buy-and-refinance events are the natural renewal moments.

### Stewardship funding

Stewardship is a permanent liability — fund it permanently. Standard mechanics: a per-unit stewardship reserve (commonly $5,000–$10,000 per home, in a board-designated fund or a separate stewardship entity) capitalized at closing from development sources or by a stewardship fee collected at each resale (a flat fee or ~1%–2% of price, paid from seller proceeds and disclosed in the lease/covenant). Budget per-unit annual stewardship cost (typically $200–$800) and size the reserve to the portfolio, or the covenant will outlive the money that enforces it.

### Deliverable: stewardship policy outline

Cover: portfolio registry and data fields; annual monitoring protocol; refinance review procedure; enforcement ladder with decision authority (staff vs. board vs. counsel); ROFR/repurchase exercise timelines; renewal calendar; reserve funding, deposit rules, and permitted uses; homeowner education on the restriction at closing and at year five.

## Choosing Among Models

Decision drivers — walk them in order for a given context:

1. **Land cost and market pressure.** High-cost, land-constrained markets → CLT (removing land from the price equation does the most work). Low-cost rural markets → deed restriction often sufficient.
2. **Building type.** Scattered-site single-family → CLT or deed restriction. Single multi-family building with resident-governance appetite → LEHC.
3. **Who must control.** Community wants durable democratic control of land → CLT's tri-partite structure. Residents want self-governance → co-op. Steward wants minimal footprint → deed restriction.
4. **Financing reality.** CLT homes are now conventionally financeable with lender-conforming leases. Co-ops need share-loan lenders (check supply locally) and often a blanket mortgage. Deed-restricted homes finance like any home, subject to appraisal and the restriction's effect on value.
5. **Organizational capacity and capital.** CLT needs land-acquisition capital and an ongoing stewardship shop. Co-op needs strong management and reserves. Deed restriction needs the least but offers the least control.
6. **Funding source constraints.** HOME, LIHTC (which requires rental for the compliance period), and state trust-fund programs each dictate or bias structure — reconcile model choice with the capital stack via `nonprofit-housing-development-finance` before committing.
7. **Portfolio strategy.** Many stewards blend: CLT for clustered land, deed restrictions on dispersed subsidy units, co-op conversions for at-risk rental buildings.

## Standard Deliverables

- **Model-comparison memo** for a specific jurisdiction: the three (or blended) models scored against the decision drivers above, with financing feasibility and a recommendation.
- **Resale formula design memo** with worked examples (like the one above) for each candidate formula, next-buyer affordability math, and a recommendation with exhibits.
- **Ground lease key-terms outline** per the eleven-section list above, for attorney drafting.
- **Stewardship policy** per the outline above: monitoring, enforcement ladder, renewal calendar, and reserve funding.
- (For advisors) a facilitation agenda for the board/membership decision meeting on model choice.

## Common Failure Modes

- **Formula defined by policy, not instrument.** Fix: put the formula and its worked example in the recorded lease/covenant; policy supplements, never supersedes.
- **Vague "fair market value minus land" language.** Fix: name the formula family and the numbers; "fair" invites litigation.
- **Lender-hostile ground lease.** Fix: adopt standard mortgagee protections before the first closing; a home the local bank won't mortgage is unsellable.
- **Stewardship on a shoestring.** Fix: per-unit reserve capitalized at closing; annual monitoring calendar with a named owner.
- **Uncapped improvements credits.** Fix: pre-approval + receipts + cap, or fold into the formula.
- **Co-op with no replacement reserves.** Fix: carrying charges sized to fund reserves; special assessments predictably trigger member defaults and share dumps.
- **Empty board thirds / captured thirds.** Fix: per-third quorum minimums; community-third eligibility excludes insiders.
- **Refinances stripping formula equity.** Fix: lease/covenant requires steward review and consent of new debt; cap aggregate debt at the formula price.
- **Fixed-term restrictions expiring untracked.** Fix: renewal calendar with a five-year lead; the registry is a core record, not a spreadsheet on a departed staffer's laptop.
- **Mixing HOME recapture and resale on one unit.** Fix: one provision per unit, documented in the written agreement at assistance.
- **Enforcement-by-surprise.** Fix: educate the owner on the restriction at closing and at each monitoring contact; the covenant is a contract both parties should be able to recite.

## Practitioner vs. Advisor Framing

- **As the steward's staff**, your leverage is the registry and the monitoring cadence: an annual contact and a refinance-review gate prevent nearly every enforcement crisis. Bring the enforcement ladder to your board for adoption *before* the first violation, so the response is policy, not improvisation.
- **As an advisor/consultant**, never present model choice in the abstract: score the models against the client's actual market, building stock, and funder constraints in writing, and flag every place an attorney must draft or review (ground lease, covenant, co-op documents, HOME resale/recapture election). Your deliverable is a decision memo the board can adopt and a drafting outline counsel can execute — not legal text.

Every instrument this skill outlines — ground lease, deed restriction, occupancy agreement, HOME resale/recapture provision, and co-op corporate documents — must be drafted or reviewed by a real-estate attorney in the property's state before adoption or recording. Treat this skill's outlines as the functional specification, never as the legal instrument itself.
