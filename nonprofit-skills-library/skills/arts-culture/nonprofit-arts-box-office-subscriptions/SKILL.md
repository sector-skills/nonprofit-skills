---
name: nonprofit-arts-box-office-subscriptions
description: "Nonprofit arts box office strategy: ticketing platforms (Tessitura, Spektrix, AudienceView, PatronManager, Eventbrite — fee models, embedded vs passed-through fees); subscription packages (full-season, mini, flex); zone, preview, dynamic and tiered pricing; subscriber renewal economics; group sales and school matinees; fee disclosure under the FTC all-in rule, exchanges, refunds. Use when a user says 'our subscribers aren't renewing,' 'should we switch ticketing platforms,' 'is dynamic pricing right for us,' 'what do we charge for previews,' or 'our service fees feel too high.' Not for member tiers (use nonprofit-arts-membership-program), venue rental (use nonprofit-arts-venue-rental-earned-income), galas (use nonprofit-fundraising-events), sponsorships (use nonprofit-arts-season-sponsorship), donor conversion (use nonprofit-donor-retention), CRM selection (use nonprofit-donor-crm), season selection (use nonprofit-arts-season-planning), or education programming (use nonprofit-arts-education-programs)."
license: MIT
supervision: review
supervision_note: "Published ticket prices, per-ticket fees, and discount policies become public commitments that are hard to walk back and need knowledgeable staff review before they go live."
last_reviewed: 2026-09-13
---

# Box Office and Season Subscriptions

## When to Use This Skill

Use this skill when a nonprofit arts organization — theater, orchestra, dance, opera, presenting
organization, community arts center — is making decisions about how it sells tickets: which
ticketing platform to run, how to price the house, how to structure and renew season subscription
packages, how to forecast single-ticket vs. subscription revenue, how to run group sales and
school matinees, and what its box office policies say about fees, exchanges, and refunds. The
user is typically a managing director, marketing director, box office manager, or a consultant
helping one. Trigger phrases: "our subscribers aren't renewing," "should we switch off our
ticketing platform," "is dynamic pricing right for a nonprofit," "what do we charge for
previews," "our service fees feel too high," "we need a group sales policy," "how do we price
zones in our house."

**Boundary:** This skill covers the earned-income machinery of selling tickets: platforms,
pricing, subscriptions, group sales, and box office policy. Membership programs (member tiers,
benefits, member communications) are `nonprofit-arts-membership-program`. Renting the hall,
studio, or gallery, and ancillary lines like parking, concessions, and bar, are
`nonprofit-arts-venue-rental-earned-income`. Galas and benefit events are
`nonprofit-fundraising-events`. Pricing and valuation for season and production sponsorships are
`nonprofit-arts-season-sponsorship`. Converting subscribers into donors beyond the subscription
relationship, and lapsed-subscriber win-back framed as giving, are `nonprofit-donor-retention`.
Choosing or replacing the fundraising CRM (and whether ticketing should live in the same
database as development) is `nonprofit-donor-crm`. Selecting the season itself, balancing budget
against artistic ambition, and setting the calendar are `nonprofit-arts-season-planning` —
coordinate with that skill when forecasting the single-ticket/subscription mix. Teaching-artist
rosters, curriculum, arts-education funders, and program evaluation are
`nonprofit-arts-education-programs`; this skill covers only the box-office logistics of school
matinee sales. General event-ticketing for workshops and small events that a nonprofit runs
through a consumer platform can stay here; fundraising events route out as above.

## Part 1 — Choose the Ticketing Platform

### Know the field

The nonprofit arts market has a distinct platform set. As of September 2026:

| Platform | Model and fee mechanics | Typical fit |
|---|---|---|
| **Tessitura** | Nonprofit member network (Tessitura Network, Inc. is itself a 501(c)(3)); unified CRM + ticketing + fundraising in one database. Lifetime-license model with annual membership dues — no per-ticket fees. Dues scale with the org's operating budget; third-party benchmarks run roughly $25,000–$150,000+/year for mid-to-large institutions, with implementation commonly $40,000–$100,000+; its hosted web module (TNEW) starts around $1,000/month. | Large theaters, orchestras, opera companies that need ticketing and development on one system and can absorb a heavy implementation. |
| **Spektrix** | Cloud ticketing + CRM + fundraising; UK-based with a New York office since 2014, and it reached agreement to acquire Theatre Manager in 2025. Single service fee that scales with sales and activity — no setup fee, no per-ticket line item; the fee covers hosting, support, and updates. | Mid-size to large theaters and arts centers wanting one integrated system without enterprise cost. |
| **AudienceView Professional** (formerly OvationTix) | Choice of flat per-ticket fee or annual subscription, at the org's preference; both include the full platform, onboarding, unlimited users, and 24/7 support. | Small-to-midsize theaters migrating up from consumer platforms. |
| **PatronManager** | Ticketing + fundraising built natively on Salesforce. Annual-license benchmarks start around $23,000/year, with a per-ticket fee model available; support and storage are line items, so read the full quote. | Orgs already committed to the Salesforce ecosystem. |
| **Arts People** (acquired by Neon One) | Per-ticket pricing with no monthly platform fee; positioned for small nonprofit performing arts. | Small theaters and community arts orgs under about $500K ticket volume. |
| **ThunderTix** | Low monthly plans with the org keeping ticket revenue: general admission $20/month (+$1.00/ticket), reserved seating $25/month (+$1.25/ticket), White Glove $175/month; a K12 schools plan runs $0.65/ticket plus processing with no monthly fee. | Small orgs, community theaters, school-district venues. |
| **Eventbrite** | Consumer platform. US fees: 3.7% + $1.79 service fee per paid ticket plus 2.9% payment processing per order, passed to the buyer by default; free events are free. Nonprofits get 50% off Pro plan pricing — but the discount does **not** apply to ticketing fees. | General-admission events and workshops only; weak for reserved-seat seasons and subscriptions. |
| **Ticketmaster / AXS** | Commercial primary ticketing; fees are negotiated per event and are high. A 2025 New York study by NITO found average primary-market fees of 28.7% of face value, with Ticketmaster/TicketWeb/AXS averaging 34.7% vs. 18.7% for all other providers; GAO's 2018 estimate was ~27%. | Arena-scale presenting relationships only; almost never right for a nonprofit's own season. |

Treat every number in this table as a starting point for a quote request, not a rate card —
platform pricing moves frequently. Verify current rates on each vendor's pricing page before
putting a number in any deliverable, and date the quote.

### Decide who pays the fee — embedded vs. passed-through

This is the first structural decision, because it drives both the marketing price display and
the legal disclosure obligation (see Part 7):

1. **Passed-through fees** add a per-ticket or per-order charge on top of your face value. Your
   advertised price stays low, but the buyer's checkout total is higher than the advertised
   price — which is exactly the "drip pricing" pattern the FTC's fees rule targets. If you
   pass fees through, the all-in total must be displayed upfront (Part 7).
2. **Embedded (absorbed) fees** build the platform's cost into the face value. Cleaner display,
   simpler compliance, better buyer perception; the cost shows up as lower net ticket revenue.
   ThunderTix's org-pays model and Spektrix's single service fee are variants: the org pays the
   platform directly rather than laundering the cost through the buyer.
3. **Run the math before choosing.** Example: a $35 ticket on a platform charging 5% + $1.50
   passed through costs the buyer $38.25 (a 9% surcharge — a review-generating annoyance);
   embedded, the org nets $31.75 on the same ticket, and the marketing price is honest. At
   20,000 tickets/year the embedded choice costs about $70,000 in gross revenue — decide
   whether price integrity and disclosure simplicity are worth it, or raise face value ~$3 and
   embed.

### Run a disciplined selection process

1. **Write the requirements before the demos:** reserved-seating subscription handling (payment
   plans, season seat holds, exchange tooling), group-sales invoicing, comp ticket controls,
   CRM fields shared with development, API access, PCI compliance, and data export.
2. **Demo with your own house.** Give each vendor your actual seating chart, your subscription
   types, and your ugliest exchange scenario (subscriber, 3 days out, different price zone).
   Make them do it live. **Completion:** you have watched each finalist perform your three
   hardest workflows.
3. **Model three years of total cost**, not year one: platform fees on your real ticket
   volume, per-user charges, support tiers, email add-ons, and payment-processing rates.
   Ask whether you can bring your own merchant processor — negotiating a 2.6% + $0.10 rate
   instead of a bundled 2.9% + $0.30 saves real money at scale.
4. **Negotiate the exit before the entrance:** data ownership, export format, migration
   assistance, and contract length. Ticketing vendors hold your patron history hostage more
   often than any other software category the org will buy.
5. **Decision output:** a one-page comparison memo with the three-year total cost model, the
   fee architecture recommendation, and named references from two peer orgs of similar size
   that migrated in the last two years.

## Part 2 — Build the Pricing Architecture

### Zone pricing

Divide the house by sightline quality, not by seat count symmetry:

1. **Three to five zones** is the working range for a 300–800-seat house (e.g., orchestra
   premium / orchestra rear / mezzanine front / balcony). More zones than that and you will
   spend the season explaining the map instead of selling seats.
2. **Set zone spreads by value, not by proportion.** Price the best zone at 2–3x the worst
   zone; a $65/$45/$25 ladder works when the top zone genuinely delivers proximity and
   sightline. If the top zone isn't visibly better, collapse it.
3. **Publish the zone map at every price point** and hold the boundaries stable across the
   season — subscribers renew based on "their" seats, and re-zoning mid-season breaks seat
   retention.
4. **Hold a cheap zone deliberately.** A $20–$25 accessible zone is both mission (access) and
   marketing (low-risk trial for first-timers, who you convert to subscribers later).

### Preview pricing

Previews (the performances before opening night, 2–4 is typical) are a distinct product:

1. **Price previews 20–50% below regular prices** and label them previews openly. Previews
   sell to two audiences at once: price-sensitive buyers who fill the early house, and
   word-of-mouth multi-ticket buyers who spread hype before press night.
2. **Use previews to test demand before you commit on-sales pricing.** If previews outsell
   expectations, you have evidence to open single-ticket sales one tier higher.
3. **Never sell a preview as a regular performance at a discount** — name the product
   ("Preview: work in progress, no critics, prices reduced") or buyers will anchor to the
   discounted price.

### Dynamic and tiered pricing mechanics

Nonprofit dynamic pricing is not surge pricing — the working form is **scheduled tiers that
step up on pre-set triggers**:

1. **Build price tiers in advance** (A/B/C per zone per production), and set written triggers
   for moving up: date proximity (e.g., inside 14 days) and fill rate (e.g., 80% of house
   sold). Decide the rules before the season, in the box office policy, so staff are not
   improvising on a Saturday.
2. **Move prices up only.** If a show is soft, never visibly drop the ticket price — issue
   targeted promo codes (students, educators, lapsed subscribers) instead. Public price drops
   teach buyers to wait.
3. **Lock subscribers out of increases.** The subscription's value proposition is a guaranteed
   price; dynamic pricing must never touch a subscriber's per-ticket rate, or renewal rates
   will punish you (Part 4).
4. **Say it plainly on the ticket page:** "Prices may increase as performances approach."
   Honest disclosure both manages expectations and nudges early buying.
5. **Know the payoff and its source.** JCA's 2026 "Trends in Audience Behavior" study (44 US
   performing arts orgs, 2021-22 through 2025-26 seasons) found dynamic pricing generated a
   **median ~$240,000 in incremental revenue per organization** in the 2024-25 season for the
   35 orgs in its pricing sample, with some orgs clearing $1M. That is revenue from the same
   seats, not new buyers — budget it as pricing yield, not attendance growth.
6. **Consider Pay-What-You-Wish for one product, not the season.** If used (preview nights,
   community days), always post a suggested amount ($25–$35) — PWYW with a suggestion
   typically outperforms both flat discounting and no suggestion, and protects comp policy
   abuse.

## Part 3 — Design Subscription Packages

### Use the sector's package taxonomy

JCA Arts Marketing's subscription research uses a four-type taxonomy; use these names in
planning because your platform vendors implement all four:

| Type | Mechanics | Trend signal |
|---|---|---|
| **Fixed subscription** | Same seats, same set of performances, chosen at purchase. Traditional model. | Declining: JCA found package sales of all types fell 41% in FY 2022 vs. 2019, and fixed subscriptions kept sliding ~9% more from 2021-22 to 2022-23. |
| **Choose Your Own (CYO)** | Subscriber picks their own set of dates/seats at purchase. | Growing — sales up ~43% between 2021-22 and 2022-23 among orgs offering both. |
| **Ticket credits / flex pass** | Buyer purchases 4–8 redeemable credits, books shows anytime in the season. | More than doubled between 2021-22 and 2022-23. |
| **Pass / membership** | Flat monthly or annual price, attend as often as desired. | Also doubled; overlaps membership-program territory — see `nonprofit-arts-membership-program` for benefit design. |

Design implication: a traditional org that offers only a fixed full-season package is selling
its worst-fitting product to its most flexible-era audience. Offer at minimum a fixed full
season (for loyalists), a mini-subscription (3–4 shows), and a flex pass (4–6 credits).

### Design each package

1. **Price the ladder off the single-ticket rate.** Full-season subscriptions typically run
   10–25% below the equivalent single-ticket total; the discount is the marketing, but the real
   benefits are free exchanges, seat retention, and priority. Mini-packages discount less
   (5–15%); flex credits discount least (0–10%) because flexibility is the benefit.
2. **Load the flex pass with rules that protect you:** credits expire at season end, credits
   reserve any performance at the subscriber rate (not the dynamic rate), unused credits are
   not refundable but are transferable, and credits cannot be used for galas or special
   events. Write these in the purchase terms, not the FAQ discovered later.
3. **Sequence on-sales so subscribers win:** subscription renewal window → new-subscription
   sales → subscriber add-ons/exchanges → single tickets on sale. Single tickets should not go
   on sale until the renewal window closes (Part 4), and the calendar should say so — "prices
   are lowest and seats are best now" is only credible if it is true.
4. **Completion condition:** a one-page package grid (type, show count, price by zone, discount
   vs. single rate, key benefits, restrictions) that the whole staff can answer questions from.

## Part 4 — Subscriber Acquisition and Renewal Economics

### Anchor on the real numbers

- **Seasoned subscribers renew at 70–75%** — TCG data held the industry in that band for the
  decade before the pandemic, and the Wallace Foundation's Steppenwolf study put the national
  average at 73% against Steppenwolf's own 80%+.
- **First-year subscribers renew at roughly 50%.** The first-year cliff is the single most
  predictable failure in arts marketing: half of everything you acquire this year evaporates
  unless you onboard deliberately.
- **Subscription volume is structurally shrinking.** SMU DataArts counted 28% fewer
  subscription tickets in 2017 than 2004, and JCA found FY 2022 package sales down 41% and
  package revenue down 45% vs. 2019 (theater hit hardest at −51%; music held best at −34%).
  Plan around a smaller, more engaged subscriber base, not a return to 2005.

### Run the retain-vs-acquire math every year

Renewing a subscriber is dramatically cheaper than acquiring one, because acquisition pays the
marketing cost **and** absorbs the ~50% first-year loss rate while renewals ride an 80% habit.
Model the season explicitly:

1. Start with current subscriber count. Apply the renewal ladder: assume 70% of multi-year
   and 50% of first-year renew if you run a real renewal campaign (below).
2. Compute the new-subscriber target: it is not "however many we can get." To hold flat, you
   must acquire `base × (1 − blended renewal rate)` new packages. At a 5,000-package base and a
   70% blended renewal, that is **1,500 new packages every year** just to stand still —
   budget acquisition marketing accordingly, and treat every point of renewal-rate gain as
   acquisition budget you no longer need.
3. **Completion:** the budget memo shows subscriber count, projected renewals by cohort,
   new-subscriber targets, and the marketing cost per renewal vs. per acquisition.

### The renewal pricing ladder

Set prices by cohort, in writing, before renewal sales open:

1. **Loyalty lock:** returning multi-year subscribers get the smallest increase — typically
   0–5% — or a locked rate as an advertised benefit.
2. **Early-renewal incentive:** renew before the renewal deadline (before single tickets go
   on sale) and get a discount ($25–50 off the package) or bonus tickets.
3. **New-subscriber price:** full package price, possibly with a first-year incentive that is
   a gift (backstage tour, concession credit) rather than a deeper discount — the first-year
   cliff is a price problem less often than an onboarding problem.
4. **Lapsed win-back:** one-touch offer at a modest discount (10–15%), never a fire sale —
   former subscribers who lapsed in the last 2 years are the highest-response direct-mail list
   an arts org owns.
5. **Down-sell before you lose:** when a subscriber calls to not renew, offer the flex pass or
   mini-package first. A down-sold subscriber keeps the relationship; a lost one costs real
   money to re-acquire.

### Onboard first-year subscribers like they are donors

First-year onboarding is where the 50% cliff is fought: a welcome series (parking, dining,
what-to-wear, how exchanges work), a mid-season check-in with the box office, a seat-upgrade
offer before renewal, and using their names at will call. Treat subscriber onboarding as the
earned-income twin of new-donor onboarding in `nonprofit-donor-retention`.

## Part 5 — Forecast the Single-Ticket vs. Subscription Mix for Season Planning

Coordinate with `nonprofit-arts-season-planning` on rep selection and calendar; this skill owns
the revenue model underneath:

1. **Model subscription revenue first — it is near-certain money.** Packages × average package
   price, with the renewal ladder from Part 4, lands before the season opens. Subscription
   revenue is also advance cash: it arrives in spring/summer against fall–spring performances.
   Note for the finance office: subscriptions sold before performances occur create deferred
   revenue (`nonprofit-financial-statements` conventions) — don't book it all as earned on
   receipt.
2. **Model single tickets per production, not per season.** Take each title's historical fill
   rate (or a comparable title's), apply your zone mix and any dynamic tiers, and haircut by
   the late-booking pattern — post-pandemic audiences book in shorter windows, sometimes
   inside 72 hours, so late-week sales no longer predict a flop and you must hold marketing
   spend through opening.
3. **Build three scenarios (soft / base / hot)** with the levers you will actually pull:
   promo-code targets for soft shows, tier step-ups for hot shows. Name in advance what
   triggers each lever so the season runs on the policy you set in Part 2.
4. **Budget single tickets conservatively and subscriptions realistically.** A subscription
   forecast misses by single-digit percentages; single-ticket forecasts miss by double digits.
   Orgs that budget the same confidence in both end up cutting marketing in February to cover
   an over-built season.
5. **Completion:** a one-page forecast per production showing capacity, subscription seats
   already sold, projected single tickets by scenario, and resulting earned-revenue range —
   usable directly in the season budget (`nonprofit-budgeting`).

## Part 6 — Group Sales and School Matinees

### Group sales mechanics

Group sales is its own sales channel with its own policy — standard mechanics across the
sector, drawn from working org policies (Ford's Theatre, Denver Center, Peace Center, Center
Rep, Arden Theatre):

1. **Threshold:** groups of 10+ get the group rate; discounts commonly run 10–25% off single
   price, deeper for school groups (working examples run up to 50–60% for student matinees,
   often with fees waived for groups).
2. **Deposit at booking:** 10–25% non-refundable, due at booking or within two weeks of the
   order (Denver Center takes 10% when the show is more than 12 weeks out; Peace Center and
   Center Rep take 25% within two weeks).
3. **Final payment 2–4 weeks out:** full balance due typically 30 days before the performance
   (Ford's), two weeks for smaller orgs (Mosaic Detroit). After final payment: no refunds.
4. **Numbers adjustable until final payment** — let the teacher drop from 48 to 40 without a
   penalty, as long as the order stays above the threshold. Flexibility here is why groups
   rebook.
5. **Invoice, don't require cards.** Schools and community groups pay by check against an
   invoice; publish that you do not accept purchase orders (Denver Center's published terms) so
   school bookkeepers know to plan around them.
6. **Staff it as a desk:** a dedicated group-sales contact with a phone number and a request
   form — groups convert on service, not on the website.

### School matinee logistics

1. **Schedule school-day performances** (10:00–10:30 a.m. is the standard slot) as their own
   price type: flat per-student tickets ($15–$25 is the working range; Arden Theatre charges
   $20 for student matinees with deeper discounts for Title I and district schools).
2. **Comp chaperones at a published ratio** (one free adult per 10–15 students), collect bus
   arrival times in the booking form, and plan load-in/load-out windows with front-of-house
   staff — 300 arriving fifth-graders is a front-of-house event, not a ticketing one.
3. **Cap the house per matinee and hold release forms** (school-side permissions, your
   photography policy) in the group contract.
4. **Route the education itself elsewhere:** teaching-artist residencies, curriculum links,
   study-guide content, arts-education funders, and background-check policy belong to
   `nonprofit-arts-education-programs`. This skill stops at the reservation, deposit, and
   seating logistics.

## Part 7 — Box Office Policy Set

### Fee disclosure (the legally required part)

1. **Federal floor: the FTC's Rule on Unfair or Deceptive Fees** (16 C.F.R. Part 464),
   effective May 12, 2025, covers anyone selling live-event tickets: the **all-in total price**
   — including all mandatory fees the seller knows about and can calculate — must be shown
   upfront and more prominently than any other price figure, and fees may not be
   misrepresented. Vague labels ("convenience fee") without a truthful amount and purpose are
   the violation pattern; the FTC enforced this in April 2026 with a $10M StubHub settlement
   over drip pricing. This binds nonprofits — the rule has no small-seller exemption.
2. **State all-in pricing laws stack on top.** At least nine states mandate all-in pricing for
   ticketed events with their own quirks: New York (eff. 2022), Tennessee (2023), Connecticut
   (2023), California's SB 478 Honest Pricing Law (July 2024), Maryland (June 2024), Colorado
   (Aug 2024), North Carolina and Minnesota (Dec 2024), and Massachusetts (Feb 2025), several
   of which ban junk fees across industries, not just ticketing. If you sell into those
   states (touring, streaming, online sales), you must comply with the buyer's state.
3. **Practical compliance rule:** display the all-in price everywhere — ads, website, emails,
   box office — and itemize included fees underneath as a breakdown, never as a surprise.
   Embed fees into face value where possible (Part 1's embedded-fee decision is also your
   compliance decision). Keep one written fee schedule, reviewed annually against vendor
   rate changes.

### Exchanges and refunds

1. **Exchanges are free for subscribers, fee'd for single-ticket buyers** — this is the
   subscription benefit with the highest perceived value and near-zero marginal cost. A
   working single-ticket exchange fee is $3–5 per ticket, charged to a card on file.
2. **Exchange mechanics:** higher-value seats pay the difference; lower-value seats take the
   difference as account credit for future use — never cash refunds. Set an exchange
   deadline (e.g., 24 hours before performance) and a no-show policy (missed performance =
   no credit).
3. **Refunds: the sector standard is no-refund, exchange-or-donate.** If a buyer can't come,
   offer an exchange or a donate-back: the ticket value becomes a charitable contribution,
   receipted as a donation (deductible because the buyer surrendered the ticket before the
   performance — attendance kills the deduction; follow the acknowledgment conventions in
   `nonprofit-donor-retention` for the receipt wording).
4. **Canceled performances:** offer refund or donate-back by default, and say so in advance —
   during the pandemic, orgs that offered donate-first saw meaningful retained revenue, and
   the donate-back framing ("would you consider turning your ticket into a gift?") is both
   legal and effective.
5. **Publish the whole policy set on one page** — fees, exchanges, refunds, late seating,
   comp rules — and train box office staff on the scripts. Box office trust is built at the
   complaint window, not the sale window.

## Standard Deliverables

1. **Platform selection memo** — requirements list, three-year total cost model per finalist,
   embedded vs. passed-through fee recommendation with the checkout math, contract terms to
   negotiate (data ownership, exit, merchant processing), and two peer references.
2. **Pricing architecture one-pager** — zone map with price ladder, preview pricing, dynamic
   tier triggers per production, and the subscriber price-lock statement.
3. **Subscription package grid** — fixed/CYO/flex/mini packages with prices by zone, discount
   vs. single rate, benefits, restrictions, and the on-sale calendar.
4. **Renewal and acquisition plan** — cohort renewal ladder (loyalty, early-bird, new, lapsed
   win-back), onboarding sequence for first-year subscribers, new-subscriber targets from the
   retain-vs-acquire model, and campaign calendar ending before single on-sale.
5. **Season revenue forecast** — per-production capacity, subscription seats, single-ticket
   scenarios, earned-revenue range for the season budget.
6. **Box office policy set** — fee schedule (all-in compliant), exchange and refund policy,
   group sales terms (threshold, deposit, payment deadlines, adjustment rules), school
   matinee terms and chaperone ratios.

## Common Failure Modes

- **Passing through fees and hiding them until checkout.** The advertised $35 ticket becomes
  $38.25 at checkout, buyers feel tricked, and the FTC fees rule plus nine state all-in laws
  make the pattern a legal exposure, not just a UX one. Fix: all-in price display everywhere;
  embed where the math works.
- **Pricing subscriptions as discounts and nothing else.** A subscription sold as "20% off"
  attracts price shoppers who churn at 50%; one sold as free exchanges, retained seats, and
  priority retains at 80%. Fix: put the exchange benefit on the first marketing line.
- **Skipping first-year onboarding.** Half of new subscribers vanish at year one because
  nobody welcomed them; the org then budgets as if the missing half were the market's fault.
  Fix: run the Part 4 onboarding sequence before spending more on acquisition.
- **Dynamic pricing without written triggers.** Staff raise prices by feel, a subscriber
  discovers the seat next to their locked seat sold cheaper, and the policy blows up in the
  press. Fix: tiers and triggers set in advance; subscribers structurally exempt.
- **Visible price drops on soft shows.** Dropping a published price teaches the audience to
  wait for the drop. Fix: promo codes targeted at defined groups.
- **Budgeting single tickets with subscription confidence.** Subscription forecasts miss by
  single digits; single-ticket demand misses by double digits — orgs that budget both at
  mid-scenario certainty cut marketing mid-season to cover the gap. Fix: three scenarios with
  named levers.
- **No group contract terms.** Verbal group bookings with no deposit deadline, no
  adjust-until-final-payment rule, and no no-refund clause produce April no-shows at scale.
  Fix: publish terms like the orgs cited in Part 6 and attach them to every group invoice.
- **Trusting last year's platform pricing.** Vendors reprice frequently (consumer platforms
  especially); a memo quoting stale per-ticket rates misleads the finance committee. Fix:
  re-verify vendor pricing pages the week you write the memo, and date every number.

## Verify Before Acting

Platform fees, plan structures, and vendor lineups in this skill were verified against vendor
pricing pages and sector research in **September 2026** and move fast — re-check each vendor's
published pricing the week you rely on it. The legal rules also move: the FTC fees rule took
effect May 12, 2025 and is under continued litigation and enforcement (the April 2026 StubHub
settlement is the signal enforcement to watch), and the state all-in pricing list (NY, TN, CT,
CA, MD, CO, NC, MN, MA as of September 2026) grows year over year — check the current state
list before publishing a fee schedule. Subscription and pricing benchmarks (TCG renewal rates,
JCA package-type trends, JCA 2026 dynamic-pricing medians) are sector studies, not laws;
re-pull the current JCA and TCG data before building a season forecast on them. Every published
price and fee becomes a public commitment — route the final pricing memo through knowledgeable
staff before it goes on sale.
