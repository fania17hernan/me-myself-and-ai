---
id: whats-in-the-tank
title: "What's actually in the tank"
type: concept
level: 1
topic: tokens-and-limits
order: 3
minutes: 3
teaches: [token, context-window]
professions: [manager, accountant, recruiter]
prereqs: [gas-tank]
volatility: slow
tool_scope: agnostic
verified: 2026-07-20
sources:
  - url: https://platform.openai.com/tokenizer
    publisher: OpenAI
    retrieved: 2026-07-20
    supports: "100 words is roughly 130 tokens"
capability: "Predict which requests will be expensive before you send them."
takeaway: "Input and output both count. A short question with a long answer still drains the tank."
slug_history: []
---

A [[token]] is the unit AI actually reads and writes. Roughly three-quarters of a word, so 100 words
is about 130 tokens. Close enough: ==words are tokens==.

## Both directions burn gas

Here's what surprises people: it isn't just what you type. Input, meaning your message plus
everything earlier in the conversation, and output, the AI's reply, both count. A short question
that needs a long answer burns plenty of fuel too.

## Long conversations get slow and pricey

Each time you send a message, the AI re-reads the whole conversation so far. Message 40 in a long
chat burns far more than message 2. You're hauling the entire trip history with you.

::check answer=1
Which burns fuel?
- Only what you type
- Both, input and output
- Only what the AI writes back
::good Right, both directions burn fuel. Short question, long answer? Still pricey.
::bad Almost. Both count, which is why long questions and long answers both drain the tank.
::

::say-it-back
"Input and output both count."
::
