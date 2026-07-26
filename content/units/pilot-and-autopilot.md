---
id: pilot-and-autopilot
title: "Human in the loop: the pilot and the autopilot"
type: concept
level: 4
topic: human-in-the-loop
order: 1
minutes: 3
teaches: [human-in-the-loop]
professions: [manager, nurse, accountant, other]
prereqs: []
volatility: evergreen
tool_scope: agnostic
verified: 2026-07-25
sources: []
capability: "Decide where a person must review or approve AI work before it counts."
takeaway: "Autopilot flies most of the trip, but a pilot watches and can take the controls. That checkpoint is you."
slug_history: []
---

Autopilot handles most of a flight, and it's genuinely good at it. But there's always a pilot watching,
ready to take the controls for takeoff, landing, and anything unusual. Keeping a person at that
checkpoint is what [[human-in-the-loop]] means.

::figure id=pilot-and-autopilot label="Fig. 7 — Hands ready" caption="The autopilot flies. The pilot watches and can take over."

## Why the checkpoint exists

You already know the AI can be a confident intern: fluent, fast, and sometimes confidently wrong. The
loop is the guardrail. A person reviews or approves before the output counts, so a smooth mistake
doesn't sail straight into a contract, a diagnosis, or a payment.

## Where to place it

Match the checkpoint to the stakes. Low-stakes and reversible, a brainstorm, a first draft, let the
autopilot run. High-stakes or hard to undo, money, health, anything with your name on it, a human
signs off before it ships. The art is choosing which is which.

::check answer=1
When should you keep a firm human-in-the-loop checkpoint?
- For every task, no matter how trivial
- When the task is high-stakes or hard to undo
- Never, if the AI sounds confident
::good Right. Reserve the hard checkpoints for high-stakes, hard-to-reverse work.
::bad Not quite. The checkpoint matters most when stakes are high or a mistake is hard to undo.
::

::say-it-back
"Autopilot flies, but I'm the pilot who watches and can take over."
::
