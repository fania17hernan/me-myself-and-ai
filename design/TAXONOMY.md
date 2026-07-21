# Taxonomy and content governance

**Date:** July 20 2026
**Status:** foundation spec. Nothing gets authored until this is agreed.

The previous IA doc specified *hierarchy* (Level → Topic → Unit) and stopped there. Hierarchy is only the containers. This document defines the parts that actually make the system survive growth: controlled vocabulary, cross-cutting facets, relationships, identifiers, and fact governance.

---

## 1. Why this matters more here than in most courses

The subject decays. Module 1 already tells the reader that model tank sizes "change often." Context windows, pricing, rate limits and model names go stale in months, while "AI has a gas tank" is true indefinitely. A course about AI that has no mechanism for tracking which of its own claims are perishable will quietly become wrong, and the first person to notice will be a skeptical senior professional who was already looking for a reason to dismiss it.

So every fact carries a source, a verification date and a volatility rating, and the build refuses to ship claims that are past review. That is the difference between a course and a snapshot.

---

## 2. Entities

Five things exist. Only two of them are containers.

| Entity | What it is | Count | Addressable |
|---|---|---|---|
| **Unit** | The atom. One idea, 2 to 3 min | ~75 | Yes |
| **Term** | A glossary concept | ~60 | Yes, by anchor |
| **Task** | An outcome in Use It, "write next week's lesson plans" | ~30 | No, renders in profession page |
| **Profession** | An audience segment | ~10 | Yes |
| **Level** / **Topic** | Structural containers | 5 / 26 | Level yes, Topic no |

**Topic is deliberately not addressable.** It groups units for authoring and for the path display, but it is not a destination. Making it one recreates the module-as-commitment problem we are removing.

---

## 3. Facets

Facets cut *across* the hierarchy. A unit sits in exactly one Level and one Topic, and carries any number of facet values. This is what makes "show me everything about prompting, regardless of level" possible without reorganising anything.

### 3.1 `type` — controlled, closed set

| Value | Ends with | Quiz |
|---|---|---|
| `myth-buster` | A reframe | No |
| `analogy` | Say-it-back prompt | No |
| `concept` | One recall question | Yes, 1 |
| `playbook` | Nothing, it is a tool | No |
| `field-note` | Nothing | No |
| `check` | Closes a topic | Yes, 3 |

### 3.2 `teaches[]` — controlled, references the glossary

A unit declares which glossary terms it teaches. **A term may only appear here if it exists in `glossary.yml`.** The build fails otherwise.

This single rule is what stops taxonomy drift, which is the normal failure mode: someone tags `context-window`, someone else tags `context_window`, and six months later the glossary and the units disagree about what the course covers.

It also generates two things for free: the "Learn this properly" link on every glossary entry, and the reverse index of which unit to send someone to when they look a term up.

### 3.3 `professions[]` — controlled, closed set

Drives the Use It tab. `teacher`, `small-business-owner`, `hvac-technician`, `nurse`, `real-estate-agent`, `nonprofit`, `recruiter`, `accountant`, `manager`, `other`.

### 3.4 `volatility` — controlled, drives governance

| Value | Meaning | Review cadence | Examples |
|---|---|---|---|
| `evergreen` | True regardless of vendor or year | 24 months | "Tokens are gas in a tank" |
| `slow` | Stable but not permanent | 12 months | "Both input and output count" |
| `fast` | Vendor-specific, changes without notice | **3 months** | Context window sizes, pricing, rate limits, model names |

### 3.5 `tool_scope`

`agnostic` or `tool-specific`. Tool-specific units get a visible "checked July 2026" stamp. Agnostic ones do not need one, and cluttering them with dates makes durable knowledge look perishable.

### 3.6 Structural and practical

`level` (0-4) · `topic` (slug) · `order` (int, within topic) · `minutes` (2 or 3) · `prereqs[]` (unit ids, usually empty).

**Prereqs are advisory, never gates.** Journey C is someone arriving cold from a Google search. Blocking them because they skipped a unit is how you lose the reference seeker.

---

## 4. Identifiers and URLs

This is question 2, and the answer is: **yes, units get their own URLs, and the hierarchy must not appear in them.**

```
/u/gas-tank/              ✅  slug only
/learn/l1/tokens/gas-tank/ ❌  encodes hierarchy
```

**Rationale.** The curriculum will get reordered. Units will move levels, topics will be renamed and merged, Level 0 did not exist a week ago. Every one of those edits breaks a hierarchical URL, and every broken URL is a dead share, a dead glossary link and a lost search ranking. Hierarchy is the most volatile thing in the system, so it is the last thing that belongs in a permanent address.

Rules:

1. **Unit IDs are stable kebab slugs, globally unique, never reused.** `gas-tank`, not `l1-t2-u3`.
2. **The slug never encodes position.** `unit-3` is a bug waiting to happen.
3. **`slug_history[]` in frontmatter generates redirect stubs.** A rename never 404s.
4. **Spanish uses the same slug behind a language prefix:** `/es/u/gas-tank/`. The language switcher becomes a string prefix operation with no lookup table, at any scale. Translating the slug would mean maintaining a 75-row mapping forever, in exchange for nothing a reader values.
5. **Levels are addressable** (`/learn/l1/`) because they are stable and few. Topics are not.

---

## 5. The unit schema

One markdown file per unit, in `content/units/`. This is the source of truth. HTML is a build artefact and nobody edits it.

```yaml
---
id: gas-tank
title: "Tokens are gas in a tank"
type: analogy
level: 1
topic: tokens-and-limits
order: 2
minutes: 2

teaches: [token, rate-limit]          # must exist in glossary.yml
professions: [manager, teacher, small-business-owner]
prereqs: []

volatility: evergreen
tool_scope: agnostic

capability: "Explain why an AI answer stops mid-sentence."
takeaway: "AI has a gas tank. Long conversations burn more fuel."

verified: 2026-07-20
sources:
  - url: https://platform.openai.com/tokenizer
    publisher: OpenAI
    retrieved: 2026-07-20
    supports: "A token is roughly three-quarters of a word"

slug_history: []
translations:
  es: content/es/units/gas-tank.md
---

Body in markdown. Components by fenced block:

::analogy
Tokens are gas in a tank.
::

::check answer=1
Which burns fuel?
- Only what you type
- Both, input and output
- Only what the AI writes back
::good Right, both directions burn fuel.
::bad Almost. Both count.
::
```

### What the build does with it

1. Validates `teaches[]` against `glossary.yml`, **fails** on unknown terms.
2. Validates `type` and `professions[]` against closed sets, **fails** on unknown values.
3. Computes `review_by` from `verified` + volatility cadence. **Warns** at 30 days out, **fails** past due for `fast` units.
4. Requires at least one entry in `sources[]` for any unit tagged `fast`. An unsourced perishable claim does not ship.
5. Emits `/u/<id>/index.html` for both languages plus redirect stubs from `slug_history`.
6. Emits `search-index.json`, the reverse term index, and the profession pages.
7. **Fails if an EN unit has no ES counterpart**, so the Spanish mirror can never silently drift again. That was a real failure mode in the old build.

---

## 6. The glossary is the spine

`content/glossary.yml` is not a page, it is the controlled vocabulary that everything else references.

```yaml
- id: token
  term: { en: "Token", es: "Token" }
  plain:
    en: "A chunk of a word. The unit AI reads and writes, roughly ¾ of a word."
    es: "Un pedazo de palabra. La unidad que la IA lee y escribe."
  volatility: evergreen
  related: [rate-limit, context-window]
  taught_by: [gas-tank, whats-in-the-tank]     # generated, do not hand-edit
```

`taught_by` is derived from every unit's `teaches[]`, which means the link between a definition and its lesson can never fall out of sync, in either direction. That relationship is the single most valuable thing this taxonomy buys, because it is what makes Journey C work: look up a term, get an answer, and be offered the lesson without being forced into it.

---

## 7. Fact governance

Your instruction was to govern facts against public sources as the landscape evolves. Concretely:

**Every perishable claim carries its receipt.** `sources[]` records the URL, publisher, retrieval date, and which claim it supports. `supports` matters: a bare link rots into "something on this page backed this up once."

**Review is scheduled, not remembered.** `review_by` is computed, and CI fails when a `fast` unit is overdue. A calendar reminder is a thing people ignore. A failing build is not.

**Tool-specific claims are stamped in the UI.** "Checked July 2026" on tool-specific units. This turns the biggest credibility risk into a credibility signal, which matters disproportionately for an audience predisposed to think AI content is hand-wavy.

**Prefer the durable framing.** Where a fact can be taught without a number, teach it without the number. "Every tool has a limit and they all behave the same way when you hit it" is `evergreen`. "Claude's context window is X tokens" is `fast` and will be wrong within the year. The existing Module 1 already gets this right, which is a good sign.

**A quarterly report, generated not written.** `npm run audit` lists every unit by review status, every unsourced perishable claim, and every glossary term no unit teaches.

---

## 8. Repository shape

```
content/
  glossary.yml                 controlled vocabulary, the spine
  professions.yml              closed set + task lists
  units/          *.md          ~75 English units
  es/units/       *.md          ~75 Spanish, same ids
build/
  build.mjs                    md → html
  validate.mjs                 the failing checks in §5
  schema.json
assets/                        shipped, shared
u/<id>/index.html              generated, gitignored
es/u/<id>/index.html           generated, gitignored
search-index.json              generated
```

**Generated HTML is gitignored.** 150 files is a non-issue when no human touches them, and keeping them out of the repo prevents anyone editing the artefact instead of the source, which is how the current duplication started.

---

## 9. Decisions carried in from the open questions

| # | Decision |
|---|---|
| 1 | Markdown source, generated HTML. Agreed. |
| 2 | Units get URLs. Slug-only, hierarchy excluded, `slug_history` redirects, shared slug across languages. |
| 3 | Tab label **Progress**, page heading "Your progress". ES **Tu avance**. One word per tab in English, two in Spanish is fine. |
| 4 | No `/learn/` tab. Home is the learning surface. |
| 5 | Level 0 recommended for new arrivals, never re-pushed at a returning learner. |

---

## 10. Still open

1. **Difficulty as a facet?** Duolingo's path carries three difficulty tiers per lesson. Adding `difficulty` now is cheap; retrofitting it across 75 units is not.
2. **Does `check` stay a unit type, or become a property of a topic?** Affects whether the path shows ~75 or ~100 rows.
3. **Who owns quarterly review?** The mechanism is worthless without a name against it.
4. **Source allowlist.** Vendor docs are authoritative but promotional. Worth deciding which publishers count before authoring, not after.
