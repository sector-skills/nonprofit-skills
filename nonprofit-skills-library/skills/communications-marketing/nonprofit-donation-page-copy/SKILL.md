---
name: nonprofit-donation-page-copy
description: "Writes and structures nonprofit website donation/giving pages to maximize completed gifts: headline and form-flow copy, ask-string/suggested-amount design, impact framing per gift amount, trust signals, and friction-reduction fixes for checkout abandonment. Use for tasks like \"rewrite our donate page to convert better,\" \"what suggested donation amounts should we use,\" \"our donation form has high abandonment, diagnose it,\" \"write the thank-you/confirmation page copy,\" or \"add impact statements next to each gift amount.\" Does not cover paid ad copy, general website copy outside the giving flow, annual appeal email/letter copy (nonprofit-annual-appeals), peer-to-peer participant fundraising pages (nonprofit-peer-to-peer-fundraising), or payment processor/platform selection (nonprofit-digital-fundraising-tools)."
license: MIT
---

# Nonprofit Donation Page Copy

## When to Use This Skill

Use this skill specifically for the on-site giving/donation page and its checkout flow — the page a
donor lands on to actually complete a gift, whether from an appeal, social post, or direct navigation.
Typical triggers: rewriting donate page copy for conversion, designing suggested-gift amounts and
impact statements, diagnosing high cart/form abandonment, or writing the post-gift thank-you/
confirmation screen.

**Boundary:** This is conversion copywriting and page structure for the giving transaction itself —
not the appeal that drives someone to the page (`nonprofit-annual-appeals` owns the email/letter
copy that generates the click), not participant fundraising pages for walk/run/ride campaigns
(`nonprofit-peer-to-peer-fundraising`), and not the choice of payment processor/platform technology
(`nonprofit-digital-fundraising-tools` — this skill assumes a platform is already in place and
optimizes the copy/UX layered on it).

## Core Framework: Donation Page Conversion Elements

A high-converting donation page has these elements, each doing a specific persuasion job:

1. **Headline that states impact, not process.** "Give a child a safe place to learn" outperforms
   "Make a Donation" — the headline should answer "why should I give right now," not describe the
   mechanical action.
2. **Ask string calibrated to actual donor data**, not round guesses. Standard technique: set 3-5
   suggested amounts anchored around the median or mode of recent gifts at that entry point (e.g., a
   social-driven page skews lower than an event-driven page) — include one amount noticeably above
   typical giving to anchor upward, per anchoring-effect research on suggested giving amounts.
3. **Impact statement per amount** ("$50 provides one week of after-school tutoring for a student") —
   concrete, verifiable translations of dollars to outcomes measurably increase perceived value of
   giving at that tier. Never invent a ratio that finance/programs can't defend if a donor asks.
4. **Recurring-gift default or prominent option.** Framing monthly giving as the default or a visually
   equal option (not a buried checkbox) is a standard, effective lever for lifting recurring-donor
   acquisition, which materially improves donor lifetime value and retention economics (coordinate
   with `nonprofit-donor-retention` on downstream stewardship of new recurring donors).
5. **Trust signals near the form**, not just elsewhere on the site: a security/SSL indicator,
   nonprofit status (EIN/501(c)(3) confirmation for tax-deductibility), a charity-rating badge if
   held (Charity Navigator, Candid/GuideStar Seal), and a one-line financial transparency statement.
6. **Minimal required fields.** Every additional required form field is a documented drop-off point;
   ask only for what's operationally necessary (name, email, payment, and address only if required for
   receipting/compliance) and defer optional fields (phone, "how did you hear about us") to
   post-gift follow-up rather than the transaction itself.
7. **Progress/clarity in multi-step forms.** If the flow spans multiple steps (amount → info →
   payment → confirm), show step progress; unclear length is a common abandonment driver.
8. **Mobile-first layout.** A large share of nonprofit donation traffic, especially from social and
   email, arrives on mobile — a form requiring pinch-zooming or awkward payment-field taps loses
   completions that a desktop-only QA pass would never catch.

## Thank-You/Confirmation Page

Treat the confirmation page as a stewardship touchpoint, not an afterthought:

- Confirm the gift amount and (if recurring) the schedule clearly.
- Reiterate impact in the same terms as the ask string ("Your $50 gift will fund...").
- Include the tax-receipt/EIN information or note that a receipt is coming by email.
- Offer one, and only one, secondary action (share on social, sign up for the newsletter) — avoid
  stacking multiple asks that dilute the primary confirmation purpose.
- Trigger this page content to also inform the automated thank-you email sequence so on-page and
  email messaging match (donors notice inconsistency).

## Step-by-Step: Auditing or Building a Donation Page

1. Pull current conversion data if available: page views vs. completed gifts (conversion rate),
   average gift size, and, if instrumented, form-step drop-off rates — diagnose before rewriting so
   fixes target the actual leak point (e.g., a headline problem looks different from a payment-step
   abandonment problem).
2. Check mobile rendering and load speed first — a slow or broken mobile form invalidates any copy
   improvement.
3. Rewrite the headline to lead with impact/urgency relevant to the current campaign context.
4. Recalibrate the ask string using recent actual gift data segmented by traffic source if possible;
   don't reuse one universal ask string for social-driven, email-driven, and direct-navigation
   traffic if their typical gift sizes differ meaningfully.
5. Add or refresh impact statements per amount; verify each with program/finance before publishing.
6. Set or reposition the recurring-gift option to be visually prominent, not a low-contrast checkbox.
7. Audit form fields; remove any field not strictly necessary for processing or legal receipting.
8. Add/verify trust signals (EIN, security badge, rating seal) are present near the payment fields,
   not just in a distant footer.
9. Rewrite the confirmation page and check it against the automated thank-you email for consistency.
10. Re-test conversion rate after changes; isolate one major change at a time (e.g., ask string vs.
    headline) if running a true A/B test, since bundling multiple changes obscures which one worked.

## Common Failure Modes

- **Guessed ask strings** disconnected from actual donor gift-size data, anchoring too low (leaving
  money on the table) or too high (scaring off first-time or smaller donors).
- **Too many required fields**, especially asking for phone number or detailed address when not
  needed for receipting — a well-documented abandonment driver.
- **Generic "Donate Now" headline** with no impact framing, failing to answer "why should I give
  today" for a donor who just arrived from an appeal or social post.
- **Recurring giving buried** as an unchecked, low-visibility checkbox rather than a real choice
  presented with equal visual weight to one-time giving.
- **No mobile QA**, silently losing the majority-mobile share of nonprofit online giving traffic.
- **Thank-you page as dead end** — a blank "Thank you for your donation" with no impact reinforcement
  or receipt clarity, wasting the highest-trust moment in the entire donor relationship.
- **Copy/finance mismatch** — impact-per-dollar claims that programs or finance can't actually
  substantiate if questioned, creating a credibility and compliance risk.

## Practitioner vs. Advisor Framing

- **As the practitioner** (development/digital staff): treat this as an ongoing optimization
  practice, not a one-time rewrite — recheck ask strings and impact statements at least annually as
  program costs and typical gift sizes shift.
- **As an advisor/consultant**: use the conversion-funnel diagnostic (page views → form starts →
  completions) as the entry analysis for any "our online giving underperforms" engagement, and be
  explicit with the client about which layer a given fix belongs to — a copy fix (this skill) won't
  solve a payment-platform reliability problem (`nonprofit-digital-fundraising-tools`), and vice
  versa.
