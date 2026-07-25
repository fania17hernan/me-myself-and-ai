---
id: whiteboard
title: "The context window is a whiteboard"
type: analogy
level: 1
topic: context-windows
order: 1
minutes: 2
teaches: [context-window]
professions: [manager, teacher, recruiter, accountant]
prereqs: [gas-tank]
volatility: evergreen
tool_scope: agnostic
verified: 2026-07-25
sources: []
capability: "Explain why an AI seems to forget the start of a long conversation."
takeaway: "The AI works on a whiteboard, not a memory. When it fills up, the oldest notes get wiped."
slug_history: []
---

::analogy
The AI works on a whiteboard, not out of a memory.
::

Everything in your conversation is written on one whiteboard: your first question, its answers, the
document you pasted, all of it. While there is room on the board, the AI can see the whole thing at
once. That space is the [[context-window]].

::figure id=whiteboard label="Fig. 1 — The whiteboard" caption="The same board holds your words and its words. Room is finite."

When the board fills up, it does not grow. It makes room by wiping the oldest lines. So in a long
chat the AI can genuinely lose the thing you said at the very top, not because it stopped caring,
but because those words are no longer on the board.

::note
This is why it feels sharp early and foggy later. Same board, less of your early context still on it.
::

That is the whole idea. The next units are about how big the board is and how to keep the lines that
matter from getting wiped.

::say-it-back
"The AI works on a whiteboard. When it fills up, the oldest notes get wiped."
::
