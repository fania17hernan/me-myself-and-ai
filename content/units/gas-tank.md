---
id: gas-tank
title: "Tokens are gas in a tank"
type: analogy
level: 1
topic: tokens-and-limits
order: 2
minutes: 2
teaches: [token, rate-limit]
professions: [manager, teacher, small-business-owner, hvac-technician]
prereqs: []
volatility: evergreen
tool_scope: agnostic
verified: 2026-07-20
sources:
  - url: https://platform.openai.com/tokenizer
    publisher: OpenAI
    retrieved: 2026-07-20
    supports: "A token is roughly three-quarters of an English word"
capability: "Explain why an AI answer stops mid-sentence."
takeaway: "AI has a gas tank. Long conversations burn more fuel."
slug_history: []
---

::analogy
Tokens are gas in a tank.
::

Every word you type burns a little gas. Every word the AI writes back burns gas too. When the tank
hits empty, everything stops. ~~Even mid-sentence.~~ Even on the highway.

::figure id=gas-tank label="Fig. 1 — The tank" caption="Drawn once, reused in the glossary entry for [[token]] and on the share card."

::note
Rate limits? That's the gas station that only lets you fill up so many times an hour.
::

That's the whole mental model. Everything else in this topic is detail about how big the tank is
and how the gas gets burned.

::say-it-back
"AI has a gas tank. Long conversations burn more fuel."
::
