---
id: tokens-check
title: "Quick check: the tank"
type: check
level: 1
topic: tokens-and-limits
order: 5
minutes: 2
teaches: [token, rate-limit, truncation]
professions: [manager]
prereqs: [whats-in-the-tank]
volatility: evergreen
tool_scope: agnostic
verified: 2026-07-20
sources: []
capability: "Diagnose a stalled AI answer in under ten seconds."
slug_history: []
---

No grades. Just proof it landed.

::check answer=0
Your AI's answer stops mid-sentence. What most likely happened?
- It ran out of tokens, the tank hit empty
- It got confused by your question
- The internet connection dropped
::good Exactly. Out of gas, even mid-sentence. Reply "continue" and it refuels.
::bad Not quite. It ran out of tokens mid-answer. The fix: reply "please continue."
::
