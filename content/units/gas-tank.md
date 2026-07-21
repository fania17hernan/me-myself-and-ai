---
# ── Identity ──────────────────────────────────────────────────────
# The slug is permanent. It does not encode level, topic or position,
# because all three of those will change and the URL must not.
id: gas-tank
title: "Tokens are gas in a tank"
type: analogy

# ── Placement (metadata, NOT the URL) ─────────────────────────────
level: 1
topic: tokens-and-limits
order: 2
minutes: 2

# ── Facets ────────────────────────────────────────────────────────
# `teaches` is validated against glossary.yml. Unknown term = build fails.
# This is what generates the glossary's "Learn this properly" links,
# in both directions, so a definition and its lesson can never drift.
teaches: [token, rate-limit]
professions: [manager, teacher, small-business-owner]
prereqs: []

# ── Governance ────────────────────────────────────────────────────
# evergreen → review in 24 months
# slow      → 12 months
# fast      → 3 months, and requires at least one source
volatility: evergreen
tool_scope: agnostic
verified: 2026-07-20

sources:
  - url: https://platform.openai.com/tokenizer
    publisher: OpenAI
    retrieved: 2026-07-20
    supports: "A token is roughly three-quarters of an English word"

# ── Outputs ───────────────────────────────────────────────────────
# capability → the "what you can now do" list
# takeaway   → the exportable cheat sheet
capability: "Explain why an AI answer stops mid-sentence."
takeaway: "AI has a gas tank. Long conversations burn more fuel."

slug_history: []
translations:
  es: content/es/units/gas-tank.md
---

::analogy
Tokens are gas in a tank.
::

Every word you type burns a little gas. Every word the AI writes back burns gas
too. When the tank hits empty everything stops, even mid-sentence, even on the
highway.

And rate limits? That's the gas station that only lets you fill up so many times
an hour. Come back too often and they make you wait.

::note
That's the whole mental model. Everything else in this topic is detail about how
big the tank is and how the gas gets burned.
::

::say-it-back
Tell someone at work tomorrow: "AI has a gas tank."
::
