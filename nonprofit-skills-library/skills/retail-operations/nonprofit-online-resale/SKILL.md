---
name: nonprofit-online-resale
description: "Runs multi-channel online resale of high-value donated items through marketplaces (ShopGoodwill, eBay-style auctions): identifying/photographing items, writing listings, shipping logistics, online customer service. Use for 'list this on ShopGoodwill,' 'set up our eBay auction workflow,' 'handle online resale shipping.' In-store pricing/floor merchandising lives in nonprofit-retail-pricing-merchandising."
license: MIT
metadata:
  supervision: "unsupervised"
  supervision_note: "Marketplace listings and photos; mistakes are relisted."
  date_added: "2026-09-07"
  date_added_source: "git:1860ed47a83901ff5e6d45abc4a2ef05be8fd4cd"
---

# Nonprofit Online Resale

## When to Use This Skill

Use this skill to build or run an online resale channel for donated goods identified as too valuable,
too niche, or too collectible for standard floor pricing: marketplace/auction listing operations
(ShopGoodwill, eBay-style platforms, or a nonprofit's own e-commerce storefront), item photography and
research, shipping/fulfillment logistics, and online customer service. Typical triggers: "we found a
valuable item, should we list it online," "set up our ShopGoodwill/eBay workflow," "reduce shipping
complaints on online orders," "build a research process for identifying high-value donations."

**Boundary:** this skill covers the online marketplace channel only. Identifying that a specific item
is online-worthy happens partly during grading (`nonprofit-donation-intake-grading` — items flagged
during triage as high-value get routed here) and the floor-facing pricing/display of everything else
stays in `nonprofit-retail-pricing-merchandising`. Register/POS operations and cash handling for
in-store sales are `nonprofit-retail-store-operations`. If an item needs formal tax-valuation
documentation for the donor (Form 8283, qualified appraisal), that's `nonprofit-in-kind-gift-
acceptance` — handle that in parallel with, not instead of, the listing decision.

## Core Framework: The Online Resale Pipeline

Treat online resale as a distinct operational pipeline parallel to the floor, not an overflow valve:

1. **Identification** — a trained reviewer (not general sort-line staff) flags candidate items during
   or after grading: name-brand/designer goods, vintage or collectible items, complete boxed sets,
   working electronics/tools above a floor-price ceiling, and anything with recognizable resale
   comps online.
2. **Research and comp-pricing** — check completed/sold listings (not just active asking prices) on
   the target marketplace to set a realistic reserve or starting price before listing.
3. **Photography and listing** — produce marketplace-quality photos and a complete, accurate written
   listing (condition disclosure is critical — online buyers can't handle the item before purchase).
4. **Fulfillment** — pick, pack, and ship against the marketplace's required handling-time window.
5. **Customer service and returns** — respond to buyer questions and resolve disputes within the
   marketplace's service-level expectations, since marketplace seller ratings directly affect future
   listing visibility.

## Standard Terminology

- **Sold comps**: completed/sold listing prices for comparable items on the same platform — the only
  reliable pricing signal for resale goods; active/asking prices overstate achievable value.
- **Reserve price**: the minimum acceptable sale price on an auction-format listing, set to protect
  against a low-ball final bid on a genuinely valuable item.
- **Handling time**: the marketplace-stated number of business days between order and ship-by date;
  consistently missing it degrades seller rating and future listing placement.
- **Condition grade disclosure**: a standardized, marketplace-appropriate condition description (New,
  Like New, Good, Fair, For Parts) stated explicitly in every listing — the leading driver of buyer
  disputes when omitted or inflated.
- **Seller rating / feedback score**: the marketplace's cumulative reputation metric for the
  organization's account; a small number of unresolved disputes can disproportionately suppress
  visibility, so protecting it is an operational priority, not just a customer-service nicety.

## Step-by-Step: Running the Online Resale Channel

1. **Set the identification threshold** with the intake/grading team: a floor-price ceiling above
   which an item is automatically routed to online review (e.g., "anything a grader would price above
   $25 on the floor gets a second look for online potential"), plus named category triggers (designer
   labels, vintage indicators, complete sets, working power tools/electronics).
2. **Build a lightweight research step**: search sold/completed comps on the target platform before
   committing to list; if there's no resale comp history, the item likely belongs on the floor, not
   online.
3. **Standardize photography**: neutral background, multiple angles, close-ups of maker's marks/flaws/
   damage, and a consistent lighting setup — poor photos are the single biggest suppressor of online
   sell-through for otherwise good inventory.
4. **Write listings with full condition disclosure** and accurate measurements/specifications;
   under-disclosure drives returns and dispute rates that hurt the seller rating far more than a
   lower price would have cost in revenue.
5. **Choose listing format deliberately**: fixed-price for items with a well-established comp price,
   auction format (with or without reserve) for genuinely uncertain or collectible-driven value where
   competitive bidding can outperform a guessed fixed price.
6. **Set a shipping and packaging standard** appropriate to category (breakables, electronics, framed
   items) and price it into the listing or shipping charge — absorbing hidden shipping costs
   silently erodes the margin this channel exists to capture.
7. **Fulfill within the platform's handling-time window** every time; build a same-day or next-day
   pack-and-ship routine rather than batching, since missed handling time is a top driver of poor
   seller ratings.
8. **Monitor and respond to buyer messages within the platform's expected response window**, and
   resolve disputes generously enough to protect the seller rating — a disputed sale that damages
   rating typically costs more in future visibility than the item's sale price.
9. **Review a monthly online-channel report**: average sale price vs. floor-price estimate, sell-
   through time, shipping cost as % of sale price, and dispute/return rate — use this to recalibrate
   the identification threshold and photography/listing quality over time.

## Standard Deliverables

- Online-eligibility identification criteria (threshold + category triggers)
- Listing template with required condition-disclosure fields
- Photography setup guide
- Shipping/packaging standard by category
- Monthly online-channel performance report

## Common Failure Modes

- **No identification threshold**, so valuable items are missed on the general sort line and sold on
  the floor for a fraction of achievable online value.
- **Pricing from active/asking listings instead of sold comps**, systematically over- or under-pricing
  items.
- **Poor or inconsistent photography**, suppressing buyer interest regardless of item quality.
- **Condition over-stated in listings**, driving returns/disputes that damage the seller rating more
  than accurate disclosure would have cost in sale price.
- **Missed handling-time windows** from batched or irregular fulfillment, degrading marketplace
  visibility over time.
- **Shipping cost absorbed silently**, eroding the margin advantage this channel is supposed to
  capture over floor sale.

## Practitioner vs. Advisor Framing

- **As the staff/volunteer running online resale**, protect the seller rating as the channel's most
  valuable asset — a slightly lower sale price from generous dispute resolution almost always beats
  the compounding cost of a damaged rating suppressing every future listing.
- **As a consultant advising a resale operation on launching or scaling online sales**, size the
  channel realistically against available labor — photography, listing-writing, and fulfillment are
  genuinely time-intensive per item, so recommend starting with a narrow, high-confidence category
  (e.g., only designer clothing or only collectibles) before promising the org broad online coverage
  it doesn't have staffing to sustain.
