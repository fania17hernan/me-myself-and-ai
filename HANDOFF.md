# Handoff — Me, Myself & AI

**Last updated:** July 22 2026
**Live site:** https://fania17hernan.github.io/me-myself-and-ai/
**Repo:** https://github.com/fania17hernan/me-myself-and-ai (branch `main`)
**Local clone that works:** `~/Developer/me-myself-and-ai`

This is everything a new person (or you, in three months) needs to run, edit, and ship the course. Read sections 1 and 2 first; the rest is reference.

---

## 1. What this is

A bilingual (EN/ES) AI-literacy course for smart non-technical professionals. The teaching is built on analogies that stick, delivered in 2 to 3 minute units. The audience is guarded senior people, so the whole product is designed to earn trust before it teaches: it opens with myth-busters, it shows its sources, and it looks handmade rather than generated.

**The one-line pitch:** AI won't fail people because it's too complicated. It'll fail them the same way every system did, because nobody explained the foundation. Built by someone who watched that happen at Tesla, Expedia, Highmark and Barneys.

---

## 2. How to make a change (the whole workflow)

You never edit HTML. You edit markdown, run the build, and push.

```bash
cd ~/Developer/me-myself-and-ai
node build/build.mjs .        # regenerates all pages, refuses to build on error
```

Then open **GitHub Desktop**, confirm the changed files, **Commit to main**, and click **Push origin**. A GitHub Action re-validates and re-deploys automatically. The live site updates in about a minute.

**Requirements:** Node 20 or newer. Nothing else. No `npm install`, ever. This is deliberate, so the build still runs years from now.

### Golden rules

1. **The repo must live in `~/Developer/`, which iCloud never syncs. NOT `~/Documents` or `~/Desktop`.** This Mac has iCloud "Desktop & Documents Folders" sync turned on, so both of those folders are inside iCloud Drive, even `~/Documents/GitHub`. iCloud does not reliably sync the hidden `.git` folder, which caused a full day of "my commits vanished" confusion (July 2026). If you ever see another copy of this project under iCloud (`09 AI Projects/`, `~/Documents`, `~/Desktop`), it is dead. Delete it.
2. **Never edit files in `u/`, `es/u/`, `glossary/`, `use-it/`, `progress/`, `index.html`.** They are generated and gitignored. Your change will be erased on the next build. Edit the source in `content/` instead.
3. **Add a glossary term before any unit that teaches it.** The build fails otherwise, on purpose.

---

## 3. Content model

Three levels of structure:

```
Level   5 of them, each a visual "edition"     L0 What AI Isn't … L4 Under the Hood
  Topic  groups units, e.g. "Tokens & Limits"
    Unit  the atom: one idea, 2-3 min, its own URL   ~75 planned, 10 built
```

The **unit is the atom.** It is what the path lists, what a URL points at, and what someone finishes standing in a queue. A unit is one markdown file with frontmatter.

### The six unit types

| type | length | ends with | example |
|---|---|---|---|
| `myth-buster` | 2 min | a reframe, no quiz | "It's going to take my job" |
| `analogy` | 2 min | say-it-back | "Tokens are gas in a tank" |
| `concept` | 3 min | one recall check | "What's actually in the tank" |
| `playbook` | ref | nothing | "Three habits that save fuel" |
| `field-note` | 2 min | nothing | "The answer that died mid-sentence" |
| `check` | 2 min | 3 questions | closes a topic |

---

## 4. Writing a unit

Create `content/units/<slug>.md` and `content/es/units/<slug>.md` (same slug). Example:

```yaml
---
id: gas-tank                    # permanent. never encodes level/position
title: "Tokens are gas in a tank"
type: analogy
level: 1
topic: tokens-and-limits
order: 2
minutes: 2
teaches: [token, rate-limit]    # MUST exist in content/glossary.yml
professions: [manager, teacher] # from content/professions.yml
prereqs: []
volatility: evergreen           # evergreen(24mo) | slow(12mo) | fast(3mo)
tool_scope: agnostic            # agnostic | tool-specific
verified: 2026-07-20
sources:                        # required if volatility is `fast`
  - url: https://…
    publisher: OpenAI
    retrieved: 2026-07-20
    supports: "the exact claim this backs"
capability: "Explain why an AI answer stops mid-sentence."   # → "what you can now do"
takeaway: "AI has a gas tank. Long conversations burn more fuel."  # → cheat sheet
slug_history: []                # old slugs auto-redirect from here
---

Body in markdown. Blocks:

::analogy
Tokens are gas in a tank.
::

::figure id=gas-tank label="Fig. 1" caption="Reused in the glossary."

::note
A margin annotation, in red pencil.
::

::check answer=1
Which burns fuel?
- Only what you type
- Both, input and output
::good Right, both directions burn fuel.
::bad Almost. Both count.
::

::say-it-back
"AI has a gas tank."
::
```

Inline marks: `**bold**`, `_italic_`, `` `code` ``, `[[term]]` (glossary link), `==highlight==`, `~~drawn underline~~`, `[text](url)`.

### Spanish rules (non-negotiable)

Full rules in `ES-STYLE-GUIDE.md`. The short version: Spanish must read naturally in **both Mexico and Spain**. No regionalisms (`carro`, `seguido`, `checar`), no untranslated English (`offsite`, `deadline`), no em-dashes, never the word `coger`. Keep `token`, `chat`, `prompt`, `software`, `email` in English and gloss on first use.

---

## 5. Drawing a figure

The drawn diagrams are the signature of the whole design. A figure is a hand-styled SVG in `content/figures/<id>.svg`, referenced by `::figure id=<id>`. The look comes from an `feTurbulence` + `feDisplacementMap` filter that wobbles the strokes so they read as pencil, not vector. Copy `content/figures/gas-tank.svg` as a starting template. Every figure needs a `<title>` and `<desc>` for screen readers.

**This is the expensive, uncopyable work.** 25 modules still need their analogies drawn. That is the main content job remaining.

---

## 6. Fact governance (why the build can fail)

The subject decays: context windows, pricing and model names go stale in months. So every unit is validated on every build (`build/validate.mjs`). The build **refuses to emit** if:

- `teaches:` names a term not in the glossary
- `type`, `professions`, `volatility`, or `tool_scope` is outside its closed set
- a `fast` unit has no `sources`, or is past its 3-month review
- an EN unit has no ES counterpart
- `verified` is missing or unparseable

A weekly cron also re-runs the deploy, so a fact that goes stale during a quiet month still trips the build. Tool-specific units render a "Checked July 2026" stamp; evergreen ones deliberately don't, so durable knowledge doesn't look perishable.

Run `node build/validate.mjs .` any time to check without building.

---

## 7. File map

```
content/                  ← THE SOURCE OF TRUTH. Edit here.
  glossary.yml            controlled vocabulary (7 terms). Spine of the taxonomy.
  professions.yml         closed set for the Use It tab
  units/*.md              10 English units
  es/units/*.md           10 Spanish units, same slugs
  figures/*.svg           hand-drawn diagrams (1 so far: gas-tank)

build/                    ← the generator. Zero dependencies.
  build.mjs               md → html for units + home/glossary/use-it/progress
  validate.mjs            the governance rules, enforced
  lib.mjs                 YAML + markdown parsing, block components
  pages.mjs               home, glossary, Use It, Progress shells
  README.md               build-specific notes

assets/                   ← shipped, shared, hand-maintained (not generated)
  studio.css              THE design system: newsprint, Fraunces WONK, drawn marks
  state.js                mmai.v2 localStorage store (progress, pins, firstTry)
  unit.js                 one-scroll unit runtime
  home.js  use-it.js  progress.js   the three shell-page scripts
  (core/lesson/app/*.css  older systems, still used by legacy module-*.html)

design/                   ← specs and mockups, not shipped as pages
  TAXONOMY.md             the full data model + governance spec
  IA-AND-JOURNEYS.md      navigation, sitemap, four user journeys
  POSITIONING.md          the "why I built this" argument + copy
  redesign.html           the studio design, annotated
  concepts.html palettes.html wireframes.html   earlier explorations

u/ es/u/ glossary/ use-it/ progress/ index.html   ← GENERATED. gitignored. do not edit.
module-2.html … module-26.html                     ← LEGACY. the last copy of that content.
REDESIGN-PLAN.md ES-STYLE-GUIDE.md                  ← living docs
.github/workflows/deploy.yml                        ← CI: validate → build → deploy
```

---

## 8. Design system in one paragraph

Studio / workshop. Authority through showing your work, not polish. Newsprint paper with a real grain texture, graphite ink, editor's-red pencil for emphasis and blueprint-blue for diagrams (both colors *mean* something). Type is Fraunces + Inter, unchanged from before, but Fraunces now runs its SOFT and WONK axes so the display type looks hand-cut. Marks are rationed: one drawn underline per screen, one figure per unit, one piece of tape per card. The discipline that keeps it from becoming kitsch is that restraint. All colors clear WCAG AA. Tokens live at the top of `assets/studio.css`.

---

## 9. State of play

**Done and live:**
- Build pipeline with enforced taxonomy and fact governance
- Studio redesign, drawn gas-tank figure
- Level 0: five myth-busters (EN + ES)
- Level 1 Topic 1: five units on tokens & limits (EN + ES)
- Home, Glossary, Use It, Progress — all four tabs real
- Bilingual, accessible (skip link, live regions, ✓/✕ not color-only, 44px targets)
- CI deploy on every push + weekly cron

**Not done (in rough priority):**
1. **Draw the other ~25 analogies and convert modules 2-26 into units.** This is the bulk of the remaining work. Modules 2-26 are still live in the old format under "Still being rebuilt" on the home page; each drops off automatically when converted and deleted.
2. **Per-level "edition" theming** — Level 0 cooler paper, Level 4 darker. The reviewer's "progress you can feel" idea. Nice-to-have, not a bug.
3. **Live in-page prompt box** — deferred; needs an API key, a proxy, and rate limiting.
4. **A photo of Stephanie** on the About/foreword, once.

**Open questions with no owner yet:**
- Who runs the quarterly fact review? The mechanism exists; it needs a name against it.
- Source allowlist: which publishers count as authoritative (vendor docs are authoritative but promotional).

---

## 10. If something breaks

- **Site 404s on a unit but home works:** Pages is probably serving from the branch instead of the Action. Check Settings → Pages → Source = "GitHub Actions."
- **Build says "Refusing to build":** read the error; it names the file and the rule. Usually a missing glossary term or a missing ES counterpart.
- **GitHub Desktop shows no changes after you edited files:** you're editing the wrong clone. Confirm the path is `~/Developer/me-myself-and-ai`.
- **A push asks for a password and rejects it:** GitHub Desktop handles auth; use it rather than Terminal. If you must use Terminal, the password field needs a Personal Access Token, not your account password.

---

## 11. The contract, restated

Source is markdown. HTML is generated. The build enforces the taxonomy and the facts, and refuses to ship when either is wrong. That is the entire system, and it is what lets one person keep a bilingual, fact-perishable course correct over years without it quietly rotting.
