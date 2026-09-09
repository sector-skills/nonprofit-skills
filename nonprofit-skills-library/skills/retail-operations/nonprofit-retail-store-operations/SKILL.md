---
name: nonprofit-retail-store-operations
description: "Runs resale-store floor procedures: point-of-sale/inventory systems, cash handling and reconciliation, loss prevention/shrinkage control, opening/closing procedures. Use for 'set up our POS,' 'design a daily cash reconciliation process,' 'reduce shrinkage.' Org-wide control policy lives in nonprofit-financial-controls; this implements it on the floor."
license: MIT
supervision: review
supervision_note: "Cash handling, reconciliation and loss prevention are financial controls."
---

# Nonprofit Retail Store Operations

## When to Use This Skill

Use this skill to build or fix the day-to-day operating procedures of a resale storefront: point-of-
sale (POS) and inventory system selection/configuration, daily cash handling and till reconciliation,
loss prevention and shrinkage control, and opening/closing checklists. Typical triggers: "our till
never balances," "we need a POS system for the thrift store," "shrinkage is climbing, what's our loss-
prevention plan," "write an opening/closing checklist for store staff," "reconcile daily cash across
multiple registers."

**Boundary:** this skill is the retail-floor procedure layer — how controls are executed at the
register and on the floor day to day. Org-wide internal control *policy design* (approval thresholds,
segregation of duties, board-adopted financial policy, audit prep) is `nonprofit-financial-controls`;
this skill implements those policies at store level and should reference, not redesign, the
org's approval-threshold table. Pricing strategy and merchandising are
`nonprofit-retail-pricing-merchandising`. Online marketplace operations are `nonprofit-online-resale`.
Staffing/scheduling of the people running these procedures is `nonprofit-retail-staffing`.

## Core Framework: The Store Operations Triangle

Every resale store's floor operation rests on three interlocking systems, each with its own named
failure mode if under-built:

1. **POS/inventory system** — the transaction and stock-tracking backbone; weak systems produce
   unreliable sales and shrinkage data that makes every other control (cash reconciliation, loss
   prevention) impossible to verify.
2. **Cash handling and reconciliation** — the daily till-count, deposit, and reconciliation cycle
   that turns register activity into verifiable, bank-matched revenue.
3. **Loss prevention** — the combination of physical, procedural, and data controls that keep
   shrinkage (inventory or cash loss from theft, error, or breakage) within an acceptable, tracked
   range.

A resale store is unusually exposed on all three relative to ordinary retail: donated inventory has
no invoice trail to check receipts against, item-level pricing is often set at the register rather
than pre-ticketed with barcodes, and high volunteer-to-staff ratios raise both training and
accountability challenges. Build procedures assuming these conditions, not a standard retail template.

## Standard Terminology

- **Shrinkage / shrink rate**: inventory value lost to theft, damage, spoilage, or administrative
  error, typically expressed as a % of retail sales; track it monthly and investigate any month-over-
  month jump immediately rather than averaging it away.
- **Till float**: the fixed starting cash amount in a register drawer at open, counted back to the
  same amount at close before the day's sales are deposited.
- **Over/short report**: the daily reconciliation output showing the difference between expected
  cash (float + recorded sales) and actual counted cash per register/cashier.
- **Dual-count verification**: two people independently counting and initialing a cash drawer at
  open/close/deposit — the single highest-leverage cash control for a thrift store's small-team
  reality.
- **Sweep**: periodically removing excess cash from the register to a locked drop safe during the
  business day, so the working till never accumulates more than a set cap exposed at the counter.

## Step-by-Step: Building Store Operations Procedures

1. **Select or configure a POS/inventory system** that supports category-level (not necessarily full
   SKU-level, given donated-goods volume) sales tracking, discount/markdown-tag entry, and a daily
   close-of-day sales report by category and payment type.
2. **Write opening procedures**: unlock/alarm sequence, till float count-in with dual verification,
   register/terminal power-on and system check, floor walk-through for safety, and a designated
   opener sign-off.
3. **Write closing procedures**: final sale cutoff, till count-out with dual verification against the
   POS close-of-day report, discrepancy documentation on any over/short, deposit prep, alarm/lock
   sequence, and a designated closer sign-off.
4. **Set the daily over/short threshold and escalation path**: define what dollar variance is normal
   register error (e.g., under $5) versus what triggers a manager review and, above a second
   threshold, a report up to whoever owns org-wide financial controls per `nonprofit-financial-
   controls`'s approval structure — this skill executes that org policy at store level rather than
   setting the threshold itself.
5. **Build the deposit and reconciliation cycle**: bank the counted deposit promptly (same or next
   business day), reconcile the bank-deposit slip against the POS close-of-day total, and route any
   variance to a second person for review, never the same person who counted the till.
6. **Design physical and procedural loss-prevention controls**: fitting-room item-count tags, staffed
   or camera-monitored blind spots, a no-cash-in-pockets policy for register staff, mandatory receipt
   for every transaction (also a fraud control — no receipt enables a "no-sale" cash skim), and a
   locked backroom/donation-holding area so unsorted or unpriced inventory isn't accessible to
   shoppers or unsupervised staff.
7. **Track and review shrinkage monthly** by comparing POS-recorded inventory movement against
   physical spot counts in high-value categories (electronics, boutique section); investigate any
   month with a shrink-rate jump before the next inventory cycle, not after.
8. **Run periodic unannounced till audits** and rotate which staff/volunteers are paired for
   dual-count duties, so no single pairing becomes a long-term blind spot.
9. **Document every procedure in a store operations manual** accessible to all shift staff and
   volunteers, and retrain to it whenever a POS system changes or a new loss-prevention control is
   added.

## Standard Deliverables

- POS/inventory system configuration checklist
- Opening/closing procedure checklists with sign-off lines
- Daily over/short report template and escalation thresholds
- Deposit reconciliation procedure
- Loss-prevention control checklist (physical + procedural)
- Monthly shrinkage report

## Common Failure Modes

- **Single-person till counts** with no dual verification, removing the only real-time check against
  cash skimming or simple counting error.
- **No receipt required for every sale**, which both frustrates customers on returns and opens a
  "no-sale" register fraud vector.
- **POS system used only for ringing sales, not tracked for shrinkage**, so inventory loss goes
  undetected until a full physical count reveals a large unexplained gap.
- **Deposits delayed or batched irregularly**, making bank reconciliation difficult and creating a
  window where cash sits unsecured on-site.
- **Store-level procedures invented ad hoc instead of tied to the org's approval-threshold policy**,
  creating a gap between what `nonprofit-financial-controls` says should happen and what actually
  happens at the register.
- **Unsorted/unpriced backstock accessible to the sales floor**, enabling both shrinkage and
  inconsistent off-book pricing by whoever reaches it first.

## Practitioner vs. Advisor Framing

- **As a store manager**, treat the over/short report as a daily habit, not a monthly audit artifact
  — same-day review of a variance is far more likely to identify a training gap or an actual loss
  than a variance discovered weeks later with no memory of that day's specifics.
- **As a consultant advising a resale store**, don't propose new policy thresholds from scratch —
  first confirm the org's board-adopted approval/threshold policy from `nonprofit-financial-controls`
  and design the store procedure to execute that policy; a floor-level fix that contradicts org policy
  creates an audit finding even if it "solves" the immediate operational complaint.
