---
name: nonprofit-social-media
description: "Builds nonprofit social media strategy and execution: platform selection, content calendars, post-format mix (volunteer spotlights, donor shoutouts, program updates, behind-the-scenes), posting cadence, and engagement/growth tactics. Use for tasks like \"build our social media content calendar,\" \"what should we post this month on Instagram,\" \"write a volunteer spotlight post,\" \"plan our #GivingTuesday social push,\" or \"our engagement is dropping, diagnose our social strategy.\" Does not cover the org's core brand voice/messaging house (nonprofit-brand-messaging), e-newsletter content (nonprofit-email-newsletter), press/media pitching (nonprofit-media-relations), peer-to-peer fundraising participant tools (nonprofit-peer-to-peer-fundraising), or paid ad campaign strategy/budgets (general marketing, not covered here)."
license: MIT
supervision: unsupervised
supervision_note: "Ordinary channel content; mistakes are cheap and reversible."
---

# Nonprofit Social Media

## When to Use This Skill

Use this skill for nonprofit social media planning and content production: choosing platforms,
building a content calendar, writing individual post copy, and diagnosing engagement problems.
Typical triggers: building a monthly/quarterly content calendar, planning platform-specific content
for a campaign moment (#GivingTuesday, an awareness day, an event), writing a volunteer or donor
spotlight post, or troubleshooting declining reach/engagement.

**Boundary:** This skill executes on social channels using voice/positioning defined elsewhere —
it does not define brand voice or key messages (`nonprofit-brand-messaging` owns that; pull from it,
don't redefine it here), does not write e-newsletter content (`nonprofit-email-newsletter`), does not
pitch journalists (`nonprofit-media-relations`), and does not build participant fundraising page
tools for walk/run/ride campaigns (`nonprofit-peer-to-peer-fundraising`, though this skill can
promote such a campaign on social).

## Platform Selection Framework

Don't default to "be everywhere." Choose platforms by matching audience and content type:

- **Instagram:** Best for visual storytelling, program photos, Reels/short video, and
  younger/millennial donor and volunteer audiences. Strongest for volunteer/beneficiary spotlights
  (with consent per `nonprofit-storytelling` rules).
- **Facebook:** Still the strongest for reaching older donor demographics and for event promotion,
  Facebook Fundraisers, and community-group engagement; often the platform with the most
  engaged existing donor base for established nonprofits.
- **LinkedIn:** Best for board recruitment signals, corporate sponsor visibility, thought leadership
  from the ED, and reaching corporate/foundation partners rather than individual donors.
- **TikTok/YouTube Shorts:** Best for volunteer recruitment and awareness/reach among Gen Z; requires
  more casual, native-format video (not repurposed polished donor-video content) to perform.
- **X/Threads:** Useful mainly for real-time advocacy moments, media/press engagement, and
  policy-adjacent nonprofits; lower priority for direct fundraising.

Rule of thumb: pick 2-3 platforms matched to actual staff capacity rather than spreading thin across
5+ channels with inconsistent posting — inconsistent cadence hurts algorithmic reach more than being
absent from a platform entirely.

## Standard Deliverable: Content Calendar and Pillar Mix

Build calendars around a repeating content-pillar mix so the feed doesn't become 90% asks. A healthy
nonprofit ratio is roughly:

- **40% Impact/program content** — outcomes, program updates, data points (short-form, pulling from
  `nonprofit-outcomes-measurement` where possible).
- **20% People spotlights** — volunteer spotlights, staff spotlights, donor/board shoutouts (consented
  per `nonprofit-storytelling` if a beneficiary is featured).
- **20% Behind-the-scenes/organizational culture** — day-in-the-life, event recaps, office/field
  moments that build authenticity and trust.
- **10% Direct asks/CTAs** — donate, volunteer, register, sign a petition; concentrate around
  campaign moments rather than spreading evenly, so asks don't fatigue followers.
- **10% Reactive/timely** — awareness days relevant to mission, seasonal moments, responsive content.

Build the calendar at least 4-6 weeks out with placeholders for reactive content, and mark
campaign-critical dates (GivingTuesday, year-end, annual event, awareness month) 2-3 months ahead so
asset production (photos, video, graphics) isn't rushed.

### Spotlight Post Structure (Volunteer/Donor)

1. Hook: a specific, human detail, not a title ("Every Tuesday for six years, Priya has..." not
   "Volunteer Spotlight: Priya").
2. What they actually do, in concrete terms (not "supports our mission").
3. One quote in their own words.
4. A soft CTA relevant to the spotlight type (volunteer post → "interested in volunteering like
   Priya? Link in bio" ; donor post → thank-you framing, not a new ask).
5. Tag/consent check: confirm the person is comfortable being tagged/named publicly before posting.

## Step-by-Step: Building the Strategy

1. Confirm goals per platform (awareness, volunteer recruitment, donor stewardship, advocacy reach) —
   a calendar without a stated goal per platform produces generic content that serves no metric well.
2. Audit the last 90 days of posts against the pillar mix above; identify skew (most orgs over-index
   on asks and under-index on impact/people content).
3. Build the 4-6 week calendar with pillar tags on each planned post so mix stays balanced at a
   glance.
4. Draft copy pulling voice/tone and approved terminology from the org's messaging house
   (`nonprofit-brand-messaging`) rather than improvising tone post-by-post.
5. Batch-produce visual assets ahead of the posting date; flag any post needing subject consent
   (spotlights, program photos of clients) and confirm it's cleared before scheduling.
6. Schedule via a social management tool with UTM-tagged links on any post driving to the donation
   page or an event registration, so performance is attributable.
7. Review engagement monthly: track reach, engagement rate, and click-throughs by pillar type (not
   just overall follower count) to see which content actually drives action, and rebalance the mix
   next cycle.

## Common Failure Modes

- **Ask fatigue:** posting donation asks more than ~10-15% of the time, causing follower drop-off and
  desensitization right when a real campaign needs attention.
- **Inconsistent voice** because copy is written ad hoc without referencing the messaging house.
- **Posting without consent** for identifiable clients/beneficiaries — the fastest way to create a
  dignity and legal problem (coordinate with `nonprofit-storytelling`'s consent protocol).
- **Vanity metric fixation** — chasing follower count while ignoring engagement rate or, worse,
  ignoring whether social traffic converts to volunteers/donors/signups at all.
- **No campaign lead time** — scrambling for content on GivingTuesday morning because asset
  production wasn't planned 6-8 weeks out.
- **Being on a platform the audience isn't on** — e.g., heavy LinkedIn investment for a
  direct-service nonprofit whose actual donor base skews older and lives on Facebook.

## Practitioner vs. Advisor Framing

- **As the practitioner** (comms/marketing staff or volunteer running the accounts): use the pillar
  mix as a weekly planning checklist and the platform framework to justify saying no to platforms
  that don't fit current staff capacity.
- **As an advisor/consultant**: use the 90-day pillar-mix audit as a fast, evidence-based diagnostic
  deliverable early in an engagement — it quickly reveals whether a client's "social media isn't
  working" complaint is actually a strategy problem (wrong platform, ask fatigue) versus a capacity
  problem (inconsistent posting), which point to very different recommendations.
