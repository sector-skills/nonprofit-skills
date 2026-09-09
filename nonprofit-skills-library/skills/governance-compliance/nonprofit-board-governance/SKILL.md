---
name: nonprofit-board-governance
description: "Designs board roles/responsibilities frameworks, meeting structures and agendas, committee charters, board self-assessment tools, and the ED-board relationship (executive limitations, ED evaluation process). Use when asked to run or fix board meetings, write a board meeting agenda or consent agenda, design or reshuffle standing/ad hoc committees, run a board self-assessment or board matrix health check, clarify board-vs-staff decision boundaries (governance vs. management), draft board member job descriptions or a code of conduct, or design the ED performance review and ED-board communication cadence. Does not cover recruiting or onboarding new board members (use nonprofit-board-recruitment), drafting bylaws or conflict-of-interest/whistleblower/document-retention policy text (use nonprofit-bylaws-policy), or Form 990 board-related disclosure questions (use nonprofit-form-990)."
license: MIT
supervision: review
supervision_note: "Internal process design; consequential but not externally filed."
---

# Nonprofit Board Governance

## When to Use This Skill

Use this skill for the ongoing operation of an already-seated board: meeting design, committee
structure, the board's relationship with the executive director (ED)/CEO, and board performance
diagnostics. Trigger tasks include: "our board meetings run long and nothing gets decided," "design
a consent agenda," "what committees should a nonprofit board actually have," "run a board
self-assessment," "the board keeps micromanaging staff — how do we fix that," "design the ED annual
evaluation process," or "write board member job descriptions and a code of conduct."

Boundary: this skill assumes the board already exists. Building a recruitment matrix, cultivating
and onboarding *new* board members is `nonprofit-board-recruitment`. Writing the legal text of
bylaws, conflict-of-interest policy, whistleblower policy, or document retention policy is
`nonprofit-bylaws-policy` (this skill references those policies operationally but does not draft
them). Board-related Form 990 disclosure questions (Part VI governance section) live in
`nonprofit-form-990`.

## Core Framework: Governance vs. Management

The single most common board dysfunction is confusing **governance** (the board's job) with
**management** (the ED/staff's job). Use this line to diagnose almost every board complaint:

- **Board governs**: sets mission/vision, hires/fires/evaluates the ED, approves the annual budget
  and audit, sets policy, ensures legal/fiduciary compliance, engages in strategic planning, and
  monitors organizational performance at the outcomes level.
- **Staff manages**: day-to-day operations, hiring/supervising staff below the ED, program delivery
  decisions, vendor selection, and operational budget execution within board-approved parameters.

A board that debates which vendor to use for the office copier is doing management, not governance —
redirect it. Conversely, an ED who sets strategic direction without board sign-off has flipped the
line the other way. Two named models operationalize this split:

- **Policy Governance / "Carver model"** (John Carver): the board writes **Executive Limitations**
  policies (what the ED may *not* do — e.g., "the ED shall not allow financial conditions that
  jeopardize solvency") and **Ends policies** (what results the organization exists to produce for
  whom, at what cost), then monitors the ED's compliance against those written limits rather than
  approving each operational decision.
- **Consensus/traditional model**: board approves budgets, major contracts, and policies directly by
  vote at meetings — more common in smaller and mid-size nonprofits than full Carver adoption.

Name which model (or hybrid) a client/organization is using before recommending agenda structure or
delegation language — the advice differs materially between them.

## Meeting Structure and Agendas

1. **Consent agenda** — bundle routine, non-controversial items (prior minutes, standard reports,
   routine policy renewals) into a single motion voted on without discussion, freeing meeting time
   for strategic topics. Any board member can pull an item off the consent agenda for discussion
   before the vote.
2. **Agenda design principle**: order items by decision importance, not chronology — put the highest
   -stakes strategic discussion when the board is freshest (early-to-mid meeting), not last after
   attention has degraded.
3. **Standard agenda skeleton**: call to order/quorum check → consent agenda → ED report (narrative,
   not just numbers) → committee reports (by exception — only flag items needing board action) →
   old business → new business/strategic discussion → executive session (if needed) → adjourn.
4. **Timeboxing**: assign a minute allocation to every agenda item in advance and appoint a
   timekeeper; a board packet sent 5-7 days ahead (not at the meeting) is the single biggest lever for
   shortening meetings, since members arrive prepared instead of reading materials live.
5. **Executive session**: reserve time without staff present for sensitive topics (ED evaluation,
   legal matters, compensation) — minute only that a session occurred and its general subject, not
   full discussion detail, unless legally required otherwise.
6. **Quorum and voting**: confirm the bylaws-defined quorum and any supermajority requirements (e.g.,
   removing a director, amending bylaws) before convening a vote — check `nonprofit-bylaws-policy` or
   the organization's actual bylaws for the exact figures, since this skill does not draft them.

## Committee Design

Common standing committees and what each actually owns:

- **Executive Committee** — acts with delegated authority between meetings on time-sensitive matters
  only; should not become a shadow board that pre-decides everything before the full board sees it.
- **Finance Committee** — budget development oversight, financial statement review, recommends
  reserve levels; distinct from the Audit Committee where org size allows separation (small boards
  often combine Finance + Audit, which creates an independence tension worth flagging to a client).
- **Audit Committee** — auditor selection, oversight of the audit process, and receiving the
  management letter directly, ideally with no staff (including the ED/CFO) as voting members, to
  preserve independence (see `nonprofit-financial-controls` for the audit process itself).
- **Governance/Nominating Committee** — board self-assessment administration, board matrix
  maintenance, slate development for new members (recruitment details in
  `nonprofit-board-recruitment`), and orientation.
- **Development/Fundraising Committee** — board fundraising participation and accountability, not
  execution of the annual fund itself.
- **Program/Impact Committee** — deeper-dive oversight of outcomes and evaluation data feeding board
  monitoring, without taking over program management decisions.

Every committee needs a **written charter**: purpose, authority (recommends to full board vs. can
act independently), membership/chair term, and reporting cadence — an unwritten charter is why
committees drift into duplicating or contradicting each other.

## Board Self-Assessment

Run annually or every 2 years, separate from individual board member performance review:

1. Distribute a confidential written self-assessment survey covering: understanding of mission/
   fiduciary duty, meeting effectiveness, committee functioning, ED-board relationship quality,
   fundraising participation, and board composition/diversity gaps.
2. Aggregate anonymously; never attribute individual responses in the full-board readout.
3. Present findings to the Governance Committee first, then a summary with an action plan to the
   full board — a self-assessment with no resulting action item is a wasted cycle and a common
   funder/rating-agency red flag (e.g., in due diligence questionnaires).
4. Feed composition gaps identified (skills, sector experience, lived experience, demographics)
   directly into `nonprofit-board-recruitment`'s recruitment matrix.

## ED-Board Relationship and ED Evaluation

- **Fiduciary duties** every board member owes regardless of governance model: **duty of care**
  (reasonable diligence in decisions), **duty of loyalty** (act in the organization's interest, not
  personal interest — operationalized via the conflict-of-interest policy drafted under
  `nonprofit-bylaws-policy`), **duty of obedience** (act consistent with mission and law).
- **ED evaluation**: run annually, tied to written goals set jointly at the start of the review
  period (not invented retroactively), gathering input via a structured tool (self-assessment +
  board chair/committee input, optionally 360-degree staff/peer input) and delivered in executive
  session by the board chair (or a designated committee), never as a surprise.
- **Compensation setting**: for the ED's pay, apply the IRS **rebuttable presumption of
  reasonableness** process — independent body approval (no one with a conflict of interest voting),
  use of comparability data (peer nonprofit compensation surveys), and contemporaneous documentation
  of the decision and rationale — this protects both the ED and board from an excess-benefit-
  transaction finding.
- **Common failure mode**: an ED who reports informally to individual board members instead of the
  board as a whole, creating rogue direction-setting — fix by channeling all ED direction through the
  board chair and full board votes, never a single director acting unilaterally.

## Standard Deliverables

- Board meeting agenda template with consent agenda and timeboxes
- Committee charter template (purpose, authority, membership, reporting cadence)
- Board self-assessment survey and action-plan summary
- ED annual evaluation tool and goal-setting worksheet
- Board member job description / code of conduct one-pager

## Practitioner vs. Advisor Framing

- **As the ED or board chair**, redesign the agenda and packet cadence first — most "board
  dysfunction" complaints are solved by better meeting mechanics before any personnel or bylaws
  change is needed; bring the governance-vs-management distinction into the room explicitly when a
  director starts directing staff work.
- **As an advisor**, name which governance model (Carver/Policy Governance vs. traditional) the
  client board is actually operating under before recommending agenda or delegation structure, and
  frame committee-charter gaps and self-assessment results as a specific action plan with owners and
  dates for the Governance Committee — not just a diagnostic memo.
