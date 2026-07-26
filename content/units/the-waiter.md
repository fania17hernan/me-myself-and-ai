---
id: the-waiter
title: "APIs are the waiter"
type: analogy
level: 4
topic: apis
order: 1
minutes: 2
teaches: [api]
professions: [manager, small-business-owner, accountant, other]
prereqs: [dining-room-and-kitchen]
volatility: slow
tool_scope: agnostic
verified: 2026-07-25
sources: []
capability: "Explain, in plain terms, how one app gets data or actions from another."
takeaway: "An API is the waiter: you order off the menu, it carries the request to the kitchen and brings the result back."
slug_history: []
---

::analogy
An API is the waiter between the dining room and the kitchen.
::

Now that the app is a restaurant, how does your order reach the kitchen? A waiter. An [[api]] is that
waiter: it takes your request off a fixed menu, carries it to the kitchen, and brings back exactly what
you asked for. You never step into the kitchen, and you don't need to.

::figure id=the-waiter label="Fig. 4 — The waiter" caption="You order off the menu. It fetches. The kitchen stays private."

The fixed menu matters. You can order what's listed, in the way the menu allows, and not "anything at
all." That's why apps connect through APIs: it's a controlled counter, one app asking another for a
specific thing, without either one wandering into the other's kitchen.

::note
When two tools "integrate," this is usually how. One is the diner placing orders, the other is the kitchen filling them, and the API is the waiter in between.
::

::say-it-back
"An API is the waiter: you order off the menu, it fetches, you never enter the kitchen."
::
