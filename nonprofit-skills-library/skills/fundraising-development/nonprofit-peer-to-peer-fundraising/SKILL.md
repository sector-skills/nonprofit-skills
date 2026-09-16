---
name: nonprofit-peer-to-peer-fundraising
description: "Plans and runs walk/run/ride and team-fundraising campaigns: participant and team-captain recruitment, individual fundraising page copy templates, team captain toolkits, incentive/leaderboard mechanics, and peer-to-peer email/social prompts to participants' own networks. Use when a user asks to plan a walkathon/run/ride fundraiser, recruit or support team captains, write participant fundraising-page copy or coaching emails, design a leaderboard or incentive structure, or grow per-participant fundraising averages. Does not cover corporate sponsorship of the event (use nonprofit-corporate-sponsorships), venue/day-of event logistics (use nonprofit-fundraising-events), or one-time appeal letters not routed through individual participant networks (use nonprofit-annual-appeals)."
license: MIT
metadata:
  supervision: "unsupervised"
  supervision_note: "Participant toolkits and prompts; low stakes and easily corrected."
  date_added: "2026-09-07"
  date_added_source: "git:1860ed47a83901ff5e6d45abc4a2ef05be8fd4cd"
---

# Peer-to-Peer & Team Fundraising

## When to Use This Skill

Use this skill specifically for campaigns where individual participants or teams raise money from
their own personal networks (walks, runs, rides, "birthday fundraisers," DIY campaigns) — not for
sponsorship sales for the same event (`nonprofit-corporate-sponsorships`), not for venue/day-of
logistics (`nonprofit-fundraising-events`), and not for a direct org-to-donor mass appeal
(`nonprofit-annual-appeals`). Typical triggers:

- "Plan our annual walk/run/ride fundraiser"
- "Write email templates for participants to send to their networks"
- "Design a team captain toolkit"
- "Set up a leaderboard and fundraising incentives/prizes"
- "How do we recruit more team captains and raise our per-participant average?"
- "Write fundraising-page copy participants can copy and personalize"

## Core Model

Peer-to-peer (P2P) fundraising works by converting participants into fundraisers who solicit their
own networks — the org's job is to recruit and equip participants, not to solicit end donors
directly. Revenue is a function of three levers, and diagnosing underperformance means checking
each independently:

\[ \text{Total raised} = \text{(number of participants)} \times \text{(participation-to-fundraising conversion rate)} \times \text{(average amount raised per active fundraiser)} \]

- **Registration** ≠ fundraising: a large share of registrants in most P2P campaigns never
  personalize their page or send a single ask — the highest-leverage intervention is usually
  converting registrants into active askers within the first few days, not recruiting more
  registrants.
- **Team structure**: participants recruited onto a team (led by a captain) consistently
  out-fundraise unaffiliated individual participants, because captains apply direct peer pressure
  and coaching.

## Team Captain Toolkit

A captain toolkit should include: a recruitment email template captains send to invite teammates,
a team fundraising goal-setting worksheet, a suggested team-communication cadence (kickoff, midpoint
push, final week sprint), sample social posts, and a captain recognition/incentive structure
distinct from individual participant incentives.

## Participant Fundraising Page & Email Copy

1. **Page copy structure**: personal reason for participating (why this cause, in the
   participant's own words) + a specific fundraising goal + a concrete impact statement tied to a
   dollar amount + a personal photo. Coach participants that a personalized page outperforms the
   default template dramatically — this is usually the single highest-leverage coaching point.
2. **Email sequence to the participant's own network** — provide templates for: (a) a launch
   ask sent to the full contact list in week one, (b) a midpoint update/progress ask, (c) a final
   week urgency ask, (d) a thank-you sent to every donor by the participant personally, not just by
   the org.
3. **Ask-string guidance for participants**: coach them to suggest specific amounts tied to the
   cause's impact framing (mirroring the ask-string logic in `nonprofit-annual-appeals` but
   personalized to the participant's own story) rather than leaving asks fully open-ended.

## Standard Deliverables

- **Campaign timeline** — registration open date, captain recruitment deadline, kickoff event/call,
  midpoint push, final sprint, event day, post-event thank-you/wrap window.
- **Team captain toolkit** (recruitment templates, goal worksheet, comms cadence, recognition tiers).
- **Participant coaching email sequence** (page-personalization nudge, launch-ask template,
  midpoint template, final-week template).
- **Leaderboard/incentive structure** — tiered prizes or recognition for individual and team
  fundraising milestones (e.g., $100/$500/$1,000 tiers), with incentive cost budgeted against
  expected incremental revenue lift.
- **Post-campaign performance report** — total raised, participant count, % of registrants who
  became active fundraisers (the key diagnostic metric), average raised per active fundraiser,
  average raised per team, and year-over-year trend.

## Concrete Steps

1. Set the campaign's overall goal and back into required participant count using the historical
   average-raised-per-active-fundraiser figure (not per-registrant) — this prevents overestimating
   revenue from registration counts alone.
2. Recruit team captains first, prioritizing former captains and highly engaged past participants;
   captains then recruit their own teams.
3. Onboard every registrant immediately with a personalization nudge (a templated but personal
   email/call within 48 hours of registration prompting them to add a photo, personal story, and
   goal) — the highest-impact single intervention for lifting the registrant-to-fundraiser
   conversion rate.
4. Deploy the coaching email sequence on a fixed cadence (launch, midpoint, final week) to all
   participants, giving captains parallel prompts to push their own teams.
5. Track the leaderboard publicly (with participant consent) to leverage social proof and
   friendly competition; award recognition/incentive tiers as thresholds are hit.
6. In the final week, send an urgency-focused push (deadline framing, matching-gift challenge if
   available) — a large share of P2P dollars typically comes in during the final days.
7. After the campaign, calculate the conversion-rate and per-fundraiser-average metrics, and diagnose
   which lever (registration volume, conversion rate, or average raised) most limited this cycle's
   result before planning next year's targets.
8. Thank every participant and every donor promptly; route acknowledgment mechanics to
   `nonprofit-donor-retention` for donors who are new to the organization's file.

## Common Failure Modes

- **Optimizing registration volume alone**: recruiting more registrants without addressing the
  registrant-to-fundraiser conversion gap wastes recruitment spend on people who never ask anyone.
- **Default, unpersonalized pages**: participants who never edit the template page raise far less;
  treat personalization coaching as a required onboarding step, not optional.
- **No captain structure**: running the campaign as unaffiliated individuals loses the peer-pressure
  and coaching effect teams provide.
- **Weak final-week push**: under-communicating in the final days, missing the urgency-driven
  giving spike most P2P campaigns rely on.
- **Incentive cost exceeding lift**: prize structures that cost more than the marginal revenue they
  generate — budget and evaluate incentives against actual incremental fundraising, not just
  participant enthusiasm.

## For Advisors

When a client's P2P event revenue plateaus or declines, get the three-lever breakdown
(registrants, conversion rate, average per fundraiser) before recommending any tactic — clients
often default to "we need more marketing to get more registrants" when the actual gap is
onboarding/coaching registrants into active askers. Recommend a dedicated, calendared captain
recruitment push starting well before general registration opens, since captain quality and count
predict overall campaign performance more reliably than total registrant count. Advise clients to
track and report the conversion-rate metric to the board explicitly, since it's the actionable lever
most orgs never measure.
