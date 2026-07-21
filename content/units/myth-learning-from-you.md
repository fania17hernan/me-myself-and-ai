---
id: myth-learning-from-you
title: "\"It's learning from everything I type\""
type: myth-buster
level: 0
topic: what-ai-isnt
order: 3
minutes: 2
teaches: [training-data]
professions: [manager, accountant, nurse, recruiter, nonprofit]
prereqs: []
volatility: fast
tool_scope: tool-specific
verified: 2026-07-20
sources:
  - url: https://openai.com/enterprise-privacy/
    publisher: OpenAI
    retrieved: 2026-07-20
    supports: "Business and enterprise tiers do not train on customer content by default"
  - url: https://privacy.anthropic.com/en/articles/7996868-is-my-data-used-for-model-training
    publisher: Anthropic
    retrieved: 2026-07-20
    supports: "Consumer and commercial data handling differ, and settings are user-controllable"
capability: "Decide what you can safely paste, based on which tier you're actually using."
takeaway: "The tier you're on decides this, not the technology. Check once, then stop worrying."
slug_history: []
---

This is the one that stops senior people from pasting anything real, which means they only ever test
it on toy problems and conclude it's a toy.

## The part that's true

It matters where you type. It genuinely does.

Free consumer tiers and paid business tiers handle your text differently, and the defaults are not
the same. Being cautious until you know which one you're on is correct, not paranoid.

## The part that isn't

The fear imagines a live memory: you paste something confidential, and it lodges somewhere, and
later it surfaces in someone else's answer.

That isn't how it works. ==[[training-data]] is fixed at a point in the past.== The model you're
talking to finished learning before your conversation started. Your message shapes the reply in
front of you and doesn't teach it anything.

The real question is narrower and more answerable: **is my text retained, and could a human review
it?** That's a policy question about your account tier, not a mystery about the technology.

## What to actually do

Once, for whichever tool your organisation uses:

- Find out which tier you're on
- Check whether that tier trains on content by default
- Turn it off if it's on and you can

Then paste real work, because testing AI only on fake problems is how you conclude it's useless.

::note
Check with whoever owns tooling at your organisation. This changes, which is why this unit carries a
date.
::
