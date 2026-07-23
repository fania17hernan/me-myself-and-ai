# Rebuild Plan — Me, Myself & AI

*Written July 22 2026. A working plan for finishing the course: converting the 25 legacy modules into real units, in priority order, with a repeatable recipe. Pairs with HANDOFF.md (workflow + file map) and ROADMAP.md (analogy source). Read section 1 for the shape, section 4 for the recipe you will repeat 25 times.*

---

## 1. Where things stand

The site is live and healthy. The build pipeline, taxonomy governance, and bilingual deploy all work. What remains is content, not plumbing.

- **Live now (10 units):** Level 0 "What AI Isn't" (5 myth-busters) and Level 1 "Foundations" tokens and limits (5 units). Both EN and ES.
- **Glossary:** 7 terms (token, rate-limit, context-window, truncation, confabulation, training-data, prompt).
- **Figures drawn:** 1 (gas-tank). Every analogy unit needs its own.
- **Waiting in the old format (25 modules):** everything under "Still being rebuilt" on the home page. Each one needs a drawn figure plus an EN and ES markdown unit, and each drops off "Still being rebuilt" automatically the moment it is converted and the old module file is deleted.

The single largest job is drawing the ~25 analogy figures. That is the expensive, uncopyable work, and it paces everything else.

---

## 2. The content model (recap)

Three levels of structure: **Level** (a visual edition, L0 to L4) contains **Topics** which group **Units**. The unit is the atom: one idea, 2 to 3 minutes, its own URL, one markdown file with frontmatter.

Six unit types: myth-buster, analogy, concept, playbook, field-note, check. A topic usually opens with a field-note or myth-buster, carries one or more analogy and concept units, and closes with a check.

Two hard build gates to remember while planning:

1. **A unit may only `teach:` a term that already exists in `content/glossary.yml`.** Add the glossary term first, or the build refuses to emit.
2. **Every EN unit needs an ES counterpart at the same slug.** No exceptions, the build enforces it.

Full mechanics (frontmatter fields, block syntax, figure filter, Spanish rules) are in HANDOFF.md sections 4 to 6. This plan does not repeat them.

---

## 3. Proposed level map for the 25 legacy modules

Levels follow the current L0 to L4 scheme (L0 What AI Isn't is already built). Analogies are taken from ROADMAP.md, which the legacy module titles already match. "New glossary terms" flags what must be added to `glossary.yml` before that unit can build.

### Level 1, Foundations — how the tool behaves (finish this level first)

| Module (legacy) | Analogy | Type | New glossary terms |
|---|---|---|---|
| Context Windows | The Whiteboard | analogy + concept | context-window (exists) |
| Hallucination | The Confident Intern | analogy | confabulation (exists) |
| Free vs. Paid | The Test Drive vs. the Lease (ES: la Renta) | concept | plan-tier |
| Your First AI Workflow | The Sous Chef | playbook | workflow |

### Level 2, The Tools — features people see and do not understand

| Module (legacy) | Analogy | Type | New glossary terms |
|---|---|---|---|
| Chats vs. Projects | The Phone Call and the Office | analogy | project |
| Artifacts | The Workbench | analogy | artifact |
| Connectors | The Set of Keys | analogy | connector |
| Custom Assistants | The Trained Specialist | analogy | custom-assistant |
| Beyond Text (voice, images) | Giving AI Eyes and Ears | concept | multimodal |
| Picking a Model | Choosing the Vehicle | concept | model |

### Level 3, Make It Yours — customization

| Module (legacy) | Analogy | Type | New glossary terms |
|---|---|---|---|
| Custom Instructions | The House Rules | analogy | custom-instructions |
| Memory | The Notebook That Keeps Notes | analogy | memory |
| Saved Prompts | Your Recipe Box | playbook | template |

### Level 4, Under the Hood — for the curious who hit real tech terms

| Module (legacy) | Analogy | Type | New glossary terms |
|---|---|---|---|
| AI 101 | The Airport | concept | (orientation, reuses terms) |
| Vibe Coding | Director, Not Bricklayer | analogy | vibe-coding |
| Frontend vs. Backend | The Dining Room and the Kitchen | analogy | frontend, backend |
| APIs | The Waiter | analogy | api |
| Databases | The Filing Cabinet | analogy | database |
| Hosting & Deployment | Opening the Shop | analogy | deployment |
| Human in the Loop | The Pilot and the Autopilot | concept | human-in-the-loop |
| Loops | The Night Shift | analogy | loop |
| Orchestration & Workflows | The Conductor | concept | orchestration |
| The Claude Family | Anthropic's Garage | field-note | (reuses model) |
| The ChatGPT Family | OpenAI's Fleet | field-note | (reuses model) |
| The Gemini Family | Google's Fleet | field-note | (reuses model) |

Note: the three model-family units are `volatility: fast` and must carry `sources:` and a "Checked <month>" stamp, since model names and prices go stale in months. Most other units are evergreen or slow.

---

## 4. The per-unit recipe (repeat this 25 times)

This is the loop. Once it is smooth, the profession tracks and theming are cheap by comparison.

1. **Add glossary terms first.** For each new term the unit teaches, add an entry to `content/glossary.yml` (id, term_en, term_es, plain_en, plain_es, volatility, related). Skipping this fails the build on purpose.
2. **Draw the figure.** Copy `content/figures/gas-tank.svg` as the template, redraw for the new analogy, keep the feTurbulence and feDisplacementMap wobble so it reads as pencil. Add a `<title>` and `<desc>` for screen readers. Save as `content/figures/<id>.svg`.
3. **Write the EN unit.** Create `content/units/<slug>.md` with full frontmatter (id, title, type, level, topic, order, minutes, teaches, professions, prereqs, volatility, tool_scope, verified, capability, takeaway). Body uses the block syntax (`::analogy`, `::figure`, `::note`, `::check`, `::say-it-back`).
4. **Write the ES unit.** Create `content/es/units/<slug>.md` at the same slug. Natural in both Mexico and Spain, no regionalisms, no untranslated English, no em-dashes, never the word coger. Keep token, chat, prompt, software, email in English and gloss on first use. Narrator voice is feminine (Stephanie).
5. **Validate.** Run `node build/validate.mjs .` It should report 0 errors before you go further.
6. **Build.** Run `node build/build.mjs .` from `~/Developer/me-myself-and-ai`.
7. **Delete the legacy module** it replaces (`module-N.html`), so it drops off "Still being rebuilt."
8. **Ship.** GitHub Desktop, commit to main, push. The Action re-validates, builds, and deploys. Live in about a minute.

**Definition of done for one unit:** figure drawn with a11y text, EN + ES units at the same slug, all taught terms in the glossary, validate clean, legacy module deleted, deployed, and the analogy passes the "could they explain it to a coworker tomorrow" test.

---

## 5. Recommended sequence

Each step ships independently and is testable with beta readers before the next.

1. **Pilot: Context Windows, The Whiteboard.** One unit, all the way through the recipe. It reuses an existing glossary term, so no new vocabulary friction, and it is the natural next Foundations concept. Purpose: prove the loop once and time it.
2. **Finish Level 1 Foundations:** Confident Intern, Test Drive vs. Lease, Sous Chef. Completes the "how the tool behaves" level.
3. **Level 2, The Tools** (your stated priority earlier): the 6 units above. Consider trimming to the 4 that matter most for non-users first (Chats vs. Projects, Artifacts, Connectors, Custom Assistants) and adding Beyond Text and Picking a Model after.
4. **Glossary pass:** the new terms accumulate as you go, so the glossary grows for free. Just review wording once Levels 1 and 2 are done.
5. **Level 3, Make It Yours.**
6. **Level 4, Under the Hood** (largest level, 12 units). Do AI 101 (the Airport) first as its orientation piece.
7. **Profession tracks:** once the analogy base is rich, remix existing units with role-specific examples (start with 2 to 3: PM, Teacher, Realtor). Cheap because it is the same unit with swapped examples.

---

## 6. Secondary work (not blocking content)

- **Per-level "edition" theming:** Level 0 cooler paper through Level 4 darker, so progress is something you can feel. A design pass on `assets/studio.css` tokens. Nice-to-have.
- **In-page prompt box:** deferred. Needs an API key, a proxy, and rate limiting. Revisit after content.
- **Your photo on the foreword:** one-time, once you have a shot you like.
- **Level-select landing polish:** the home page already lists levels, refine the progress rings and the "By profession" tile (mark it "coming soon" until tracks exist).

---

## 7. Open decisions

1. **Level names:** keep "What AI Isn't / Foundations / The Tools / Make It Yours / Under the Hood," or rename?
2. **Level 2 scope:** all 6 tool units, or the leaner 4 first?
3. **Lock levels or leave them open?** Recommendation: leave open at first, let people roam.
4. **Any analogy that does not sit right?** Cheaper to swap now than after it is drawn and built.
5. **Quarterly fact review:** who owns re-checking the `fast` units (the three model families especially)? The mechanism exists, it needs a name against it.
6. **Source allowlist:** which publishers count as authoritative for `fast` units. Vendor docs are authoritative but promotional, decide how to treat them.
