---
name: nonprofit-financial-controls
description: "Designs internal financial controls (segregation of duties, approval/signing thresholds, check/wire authorization, credit card and expense reimbursement policy, bank reconciliation review), and manages annual audit preparation, PBC (provided-by-client) list fulfillment, and auditor liaison, including responding to management letter findings. Use when asked to design or fix internal controls, address a segregation-of-duties gap (especially in a small finance team), set approval thresholds and signing authority, prepare for a financial statement audit, assemble a PBC list, or respond to an audit management letter. Does not cover the annual budget (use nonprofit-budgeting), producing the statements being audited (use nonprofit-financial-statements), or Form 990 filing itself (use nonprofit-form-990)."
license: MIT
supervision: expert-required
supervision_note: "Audit preparation and control design are reviewed by a licensed auditor."
---

# Nonprofit Financial Controls

## When to Use This Skill

Use this skill to design or repair internal financial controls, or to run audit preparation and
auditor liaison. Trigger tasks include: "our finance team is only two people — how do we handle
segregation of duties," "what should our check-signing/approval thresholds be," "design a credit
card and expense reimbursement policy," "we have an audit in 90 days — what do we need to prepare,"
"draft responses to our auditor's management letter findings," or "the board wants an internal
controls memo before hiring a new bookkeeper."

Boundary: this skill covers *control design and audit process*, not the budget being controlled
(`nonprofit-budgeting`) or the statements being audited (`nonprofit-financial-statements`). Form 990
public-disclosure filing itself is `nonprofit-form-990`.

## Core Framework: Segregation of Duties (SoD)

The classic internal control model splits every financial transaction cycle across at least three
incompatible functions so no single person can both execute and conceal a error or fraud:

1. **Authorization** — approving that a transaction should happen (e.g., approving a purchase, an
   expense report, a new vendor).
2. **Custody** — physical/system control of the asset (signing checks, initiating wires, having
   check stock or bank login credentials).
3. **Record-keeping** — entering the transaction into the books (posting the journal entry,
   reconciling the account).

No one person should hold two of these three for the same transaction cycle. Full three-way
segregation is straightforward in a large finance department; it is the central practical challenge
in nonprofits with 1-3 finance staff, which is the normal situation, not the exception — the fix is
compensating controls, not "hire more staff we can't afford."

### Compensating Controls for Small Teams

- **Independent review**, not independent execution: if the same person must enter and reconcile
  transactions, have someone outside finance (ED, board treasurer, finance committee chair) review
  and sign off on the bank reconciliation monthly.
- **Dual signature/dual approval above a threshold**: require two authorized signers (never both from
  the same household or direct reporting line) on checks/wires above a set dollar amount, and a
  single signer below it, with the threshold reviewed annually.
- **Positive pay and bank alerts**: use the bank's positive-pay/ACH-block services so unauthorized
  checks or electronic debits are flagged automatically — a low-cost technology compensating control
  for a thin team.
- **Board treasurer or finance committee as the second set of eyes**: routes some "custody" or
  "authorization" functions to a volunteer board role specifically to break up the finance staff's
  concentration of duties, e.g., the treasurer reviews and initials the bank statement monthly.
- **Rotate who reconciles what** periodically if more than one staff person touches the books, so no
  single account is reconciled by the same person who posts to it every month.

## Approval Thresholds and Signing Authority

Write a specific, named threshold table — do not leave this as "use judgment":

- **Purchase/expense approval** — e.g., under $500: program manager; $500-$5,000: ED; over $5,000:
  ED + board treasurer or finance committee notification; over a bylaws-defined amount: full board
  approval (check `nonprofit-bylaws-policy` for any bylaws-set threshold).
- **Check/wire signing** — single signer under a set amount; two authorized signers above it; never
  allow the same person who requested/approved a payment to be its sole signer.
- **Credit card policy** — named cardholders only, defined allowable categories, required
  original-receipt submission within a set number of days, and a non-cardholder reviewer who
  approves the monthly statement before payment — never let the cardholder self-approve their own
  statement.
- **New vendor setup and payroll changes** — require a second approver distinct from whoever
  requested the change, since vendor-master and payroll-master files are classic fraud vectors
  (fictitious vendor, unauthorized pay-rate change).
- Put the whole table in a written, board-adopted financial policy — an unwritten threshold is not an
  enforceable control and will be flagged by an auditor.

## Common Fraud/Failure Patterns to Design Against

- One person controls the entire cash cycle: opens mail/receives payments, makes the deposit, and
  records the receipt — enables skimming. Fix: separate at least the person opening mail/receiving
  payments from the person recording the deposit.
- Same person creates vendors and approves/pays invoices — enables fictitious-vendor fraud. Fix:
  second approver on new vendor setup, and periodic vendor-master review by someone outside AP.
- No one reviews the bank reconciliation independently — errors and misappropriation go undetected
  for months. Fix: monthly reconciliation review and sign-off by someone who didn't prepare it.
- Blank/pre-signed checks. Fix: never; no exceptions, no matter how "trusted" the staff member.
- Credit card statements paid without receipts or itemized review. Fix: mandatory receipt + non-
  cardholder review before payment.

## Step-by-Step: Audit Preparation and Auditor Liaison

1. **Confirm audit trigger and scope early** — many states require an audit above a revenue threshold
   for charitable organizations, and many federal/pass-through grants require a **Single Audit**
   under 2 CFR 200 Subpart F when an organization expends $1,000,000+ in federal awards in a fiscal
   year (threshold periodically updated by OMB — verify current figure before relying on it).
   Confirm which applies before scoping the engagement.
2. **Select or re-engage the auditor** with enough lead time (ideally 3-6 months before fieldwork) —
   RFP if it's been 5+ years with the same firm, per good governance practice.
3. **Close the books completely** before fieldwork: all reconciliations done, accruals posted, fixed
   asset and depreciation schedules updated, restricted/unrestricted net asset roll-forward prepared.
4. **Assemble the PBC (Provided By Client) list** the auditor sends in advance — typically includes:
   trial balance, general ledger, bank statements and reconciliations, board minutes for the audit
   period, grant/contract agreements, fixed asset schedule, payroll reports, prior-year Form 990, and
   a schedule of related-party transactions. Assign a named owner and due date to each PBC item; a
   late or incomplete PBC list is the single most common cause of audit fee overruns and delays.
5. **Hold an entrance conference** with the auditor to confirm scope, timeline, and any new
   accounting standards effective this year (e.g., changes to lease accounting, gift-in-kind
   valuation rules).
6. **Support fieldwork**: designate one internal point of contact to field auditor questions so
   requests don't scatter across staff.
7. **Review the draft management letter and financial statements** before finalization — check every
   number and every finding for factual accuracy; this is the organization's last chance to catch an
   error before it's public (Form 990 and, for many nonprofits, the audited financials themselves are
   publicly disclosable — see `nonprofit-form-990`).
8. **Respond formally to every management letter finding** with a written corrective action plan:
   what the finding was, the root cause, the specific control being added or changed, and a named
   owner and date. Present this response to the finance committee/board alongside the audit itself —
   a finding with no documented response is a repeat-finding risk next year and a governance red flag
   to funders who review audits.
9. **Present the audit to the full board**, not just the finance committee, per standard governance
   practice, with the auditor available to answer questions directly (many boards require the auditor
   to present without management in the room for part of the meeting, specifically to surface any
   concerns candidly).

## Standard Deliverables

- Written internal control policy (SoD map, approval thresholds, signing authority table)
- Credit card and expense reimbursement policy
- PBC list with owners and due dates
- Audit entrance/exit conference agendas
- Management letter response / corrective action plan

## Practitioner vs. Advisor Framing

- **As finance staff/ED**, build the control policy around the team's actual size rather than
  copying a large-organization template that assumes staff the org doesn't have — name specific
  compensating controls (board treasurer review, dual signature, positive pay) rather than leaving
  gaps unaddressed.
- **As an advisor**, a segregation-of-duties gap in a 2-person finance team is not, by itself, a
  finding to be embarrassed about — frame the engagement around whether adequate *compensating*
  controls exist, and bring a specific threshold table and PBC-list template to the client rather than
  a general "you should have controls" recommendation.
