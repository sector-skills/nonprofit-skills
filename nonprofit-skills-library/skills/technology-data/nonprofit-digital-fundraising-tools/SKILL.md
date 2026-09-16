---
name: nonprofit-digital-fundraising-tools
description: "Evaluates and sets up online giving platforms (e.g., Classy, Donorbox, GiveButter, Qgiv, Network for Good), peer-to-peer/crowdfunding fundraising technology, payment processors and gateways (Stripe, PayPal, Authorize.Net), recurring-gift/subscription billing setup, and transaction fee modeling. Use for online giving platform selection, payment processor comparison, recurring donation setup, peer-to-peer platform configuration, and donation form technical setup (fields, redirects, receipts, Apple/Google Pay). Does not cover CRM/database selection or data hygiene (nonprofit-donor-crm), PCI compliance policy or data privacy (nonprofit-data-privacy), or donation page persuasive copywriting (nonprofit-donation-page-copy)."
license: MIT
metadata:
  supervision: "review"
  supervision_note: "Payment and gateway choices move donor money."
  date_added: "2026-09-07"
  date_added_source: "git:1860ed47a83901ff5e6d45abc4a2ef05be8fd4cd"
---

# Nonprofit Digital Fundraising Tools

## When to Use This Skill

Use this skill when the request is about the *technology stack* that processes and moves online
gifts, not the database that stores donor history or the words on the page. Concrete triggers:

- "Compare Classy vs. Donorbox vs. GiveButter vs. Qgiv vs. Network for Good for our online
  giving."
- "Which payment processor should we use — Stripe, PayPal, Authorize.Net — and what are the fee
  structures?"
- "Set up recurring/monthly giving with automatic retry on failed cards."
- "We're launching a peer-to-peer walk/run — what platform handles team fundraising pages?"
- "Should we cover processing fees or pass them to the donor, and how do we build that into the
  form?"
- "Add Apple Pay/Google Pay and a mobile-optimized checkout to our donation form."
- "Our recurring donors' cards are expiring — set up dunning/card-updater."

**Boundary — hand off instead of answering here:**
- Which CRM stores the donor record, dedup, and segmentation → `nonprofit-donor-crm` (most giving
  platforms integrate with a CRM; this skill covers the giving/payment tool, the CRM skill covers
  the system of record).
- PCI-DSS scope, data-sharing policy, privacy disclosures → `nonprofit-data-privacy`.
- The persuasive copy, ask amounts, and page layout content itself → `nonprofit-donation-page-copy`.
- Broad peer-to-peer *campaign strategy* (participant recruitment, team captain toolkits) →
  `nonprofit-peer-to-peer-fundraising`; this skill covers the platform/technology selection for
  running it.

## For Practitioners: Selecting and Configuring the Stack

### 1. Separate three decisions that get conflated

1. **Giving platform** (the donation page/checkout experience and campaign tools): Classy,
   Donorbox, GiveButter, Qgiv, Network for Good, Bloomerang Giving Tools, Kindful.
2. **Payment processor/gateway** (who actually moves the money): Stripe, PayPal, Authorize.Net,
   often bundled inside the giving platform's contract but sometimes a separate merchant account.
3. **CRM/system of record** (`nonprofit-donor-crm`): where the gift and constituent history live
   after the transaction completes.

Many platforms bundle #1 and #2; almost none replace #3. Confirm what syncs automatically to the
CRM (real-time API, nightly batch, or manual CSV export) before assuming integration exists.

### 2. Compare platforms on fee structure, not just sticker price

Standard deliverable: a **fee and feature comparison table** covering:

- **Platform fee**: flat monthly/annual SaaS fee vs. percentage-of-transaction vs. "free" platform
  monetized through an optional donor-paid tip/cover-fee prompt (Classy, GiveButter, and Donorbox
  all use variants of this "donor covers fees" model).
- **Payment processing fee**: typically 2.2%-2.9% + $0.30/transaction for card payments; ACH/bank
  transfer is usually cheaper (often under 1%) and worth offering for larger gifts.
- **Peer-to-peer/event fees**: often a separate, higher fee tier layered on top of standard giving
  fees.
- **Nonprofit discount rates**: PayPal, Stripe, and several platforms offer reduced nonprofit
  pricing — confirm the org is registered for it (usually requires 501(c)(3) verification).
- **True effective cost**: model total fees against actual gift volume and average gift size, not
  the advertised headline rate — a platform with a higher percentage but donor-covered fees can
  net the org more than a "cheaper" one where the org absorbs all fees.

### 3. Recurring giving setup

Recurring/monthly giving is the highest-retention revenue stream nonprofits have; configure it
deliberately:

1. Set the default recurring cadence prominently (monthly) with one-time as the secondary option,
   not the reverse — form design measurably shifts donors toward whichever option is emphasized.
2. Enable **account updater / card-updater services** (most major processors offer this) so
   expiring or reissued cards update automatically instead of silently failing.
3. Configure **dunning management**: automatic retry logic and donor email notification on failed
   recurring charges, with a grace period before canceling the recurring gift.
4. Track and report a **recurring-gift attrition/churn rate** separate from overall donor
   retention — this is the metric that reveals whether card-updater and dunning setup is actually
   working.

### 4. Peer-to-peer and crowdfunding platform setup

- Common platforms: Classy, GiveButter, Qgiv, RunSignUp (endurance events), Funraise. Evaluate on:
  team/individual page customization, leaderboard and gamification features, participant
  fundraising minimums enforcement, and registration-plus-fundraising combined checkout (for
  walk/run events with a registration fee *and* a fundraising ask).
- Configure the **default page template** participants receive so a majority of fundraising pages
  aren't blank — blank personal pages are the top driver of low participant fundraising totals.
- Confirm how participant-raised funds and any registration fees reconcile back to the CRM as
  separate, correctly-attributed gift records (registration fee vs. donation should not be
  conflated in reporting).

### 5. Technical form setup checklist

1. Mobile-responsive checkout with Apple Pay/Google Pay enabled — mobile now represents the
   majority of nonprofit web traffic for many organizations, and one-click wallet payment options
   measurably reduce checkout abandonment.
2. Automatic tax-receipt email on completion, correctly formatted per IRS substantiation rules for
   gifts (statement that no goods/services were provided, or fair market value of any provided).
3. Redirect/thank-you page and confirmation email configured — don't leave donors on a generic
   processor confirmation screen.
4. UTM/source tracking on campaign links so results tie back to the specific appeal or campaign
   driving traffic (coordinate with whatever email/social tools generate the links).
5. Test the full donor path (new card, recurring setup, Apple Pay, failed-card scenario) before
   launch — a broken checkout on a high-traffic day (year-end, Giving Tuesday) is the most common
   and costly technical failure mode.

## For Advisors: Running a Platform Selection or Fee-Optimization Engagement

1. **Volume and gift-profile analysis first**: pull the last 12-24 months of online gift data
   (count, average size, one-time vs. recurring split) before recommending a platform — fee
   structures favor different platforms at different volumes.
2. **Total cost of ownership model**: build a simple spreadsheet projecting annual fees under each
   candidate platform against the client's actual gift volume, including any implementation or
   contract minimums.
3. **Integration audit**: confirm exactly how gifts flow into the client's CRM (native
   integration, Zapier/middleware, manual import) — a beautiful giving platform that requires
   manual monthly CSV reconciliation into the CRM creates ongoing staff burden the client will
   feel long after the selection project ends.
4. **Migration/cutover plan**: if replacing an existing processor, plan for recurring donors'
   payment methods — some platforms support token migration between processors (avoiding
   re-asking every recurring donor for a new card), others require re-enrollment, which causes
   real attrition. Confirm this before recommending a switch.
5. **Deliverable**: a short recommendation memo with the comparison table, TCO projection, and an
   implementation timeline — present fee tradeoffs in terms of net dollars to mission, not just
   percentage rates.

## Common Failure Modes

- Choosing a platform on advertised "0% platform fee" without modeling the donor-covered-fee
  opt-in rate, which is never 100% and shifts real cost back to the org.
- No card-updater/dunning setup, causing silent recurring-gift attrition that looks like a
  retention problem but is actually a technical one.
- Assuming CRM sync is automatic and real-time without verifying it — leads to gift records
  "missing" for days or requiring manual reconciliation.
- Skipping a full checkout test before a high-traffic giving day.
- Not enabling ACH/bank transfer as an option for larger gifts, leaving unnecessary card
  processing fees on the table.
