# Me, Myself & AI: Restructure + Redesign Plan

**Date:** July 20, 2026
**Scope this round:** Full restructure and visual rebuild, design first. Plus Level 0 "What AI Isn't" and per-level theming.
**Deferred:** Profession use-case picker, live in-page prompt box.

---

## 1. What the feedback actually told us

The reviewer said three things, and the third one is the real one.

| They said | They meant |
|---|---|
| "Analogies were great, broke it down perfectly" | The content is working. Do not rewrite the teaching. |
| "I fear people could find it monotonous" | The delivery shell is identical 26 times. |
| "Add a 'What AI isn't' lesson, get the guard down first" | Senior learners arrive defensive. We start teaching before we have earned permission to teach. |

Your own read, "it's giving vibe code gimmick," is the same finding from the inside. Below is the specific diagnosis rather than a vibe.

---

## 2. Diagnosis: what reads as vibe-coded

Measured against the current build (71 HTML files, 36 EN + 35 ES).

**Structural tells**

1. **All 26 modules have exactly 8 screens.** Verified: every single one. Hook, problem, analogy, mechanics, application, takeaway, quiz, done. When every lesson has identical shape, the shape stops carrying meaning and starts reading as a template fill.
2. **Every module is 9 minutes.** Length is supposed to signal importance. Right now it signals nothing.
3. **A 3-question multiple choice quiz ends every lesson,** each with the same framing line. By lesson 4 the learner knows the quiz is coming and stops reading for comprehension.
4. **The wizard is fake.** Content is chunked into next/back screens that would read fine as one scroll. It adds clicks without adding structure.

**Visual tells**

5. **One card, everywhere.** Same radius, same border, same shadow, same 660px column. No full-bleed, no asymmetry, no scale contrast. Compositional monotony is what the reviewer felt.
6. **86 emoji across the module files.** Emoji in headings and completion states is the single loudest AI-output tell, and it is the exact wrong register for the skeptical senior audience the reviewer described.
7. **Gamification chrome outweighs the content:** streak counter, flame icon, gauge, progress bar, medals, badges. For a 22-year-old learning a language this works. For a VP who is already suspicious that AI is a toy, medals confirm the suspicion.
8. **Fraunces + Inter + cream + terracotta** is a good pairing and also the current default for "warm editorial." Nothing in the type or color is yours yet.

**The blocker underneath all of it**

9. **620KB of duplicated inline CSS. Zero shared stylesheets, zero shared scripts.** Every one of the 71 files carries its own copy of a 112-line style block. This is why the design has not evolved: changing anything means 71 edits. **Nothing else in this plan is affordable until this is fixed.**

---

## 3. The restructure

### 3.1 Replace one lesson format with five

Format variety kills monotony more effectively than animation does, and it costs nothing at runtime.

| Type | Length | Shape | Ends with | Use for |
|---|---|---|---|---|
| **Myth-buster** | 3 min | Single scroll. Claim, why it feels true, what is actually true, what it means for you. | A reframe, no quiz | All of Level 0, plus scattered later |
| **Core lesson** | 9 min | The current 8-screen wizard, kept and polished | Quiz | The 8 to 10 concepts that genuinely earn it |
| **Quick concept** | 2 min | Single scroll. One analogy, one diagram, one line to remember. | Takeaway only | Concepts that are one idea, not six |
| **Playbook** | Reference | Checklist, scannable, designed to be revisited | Nothing, it is a tool | "How to prompt," "when to start a new chat" |
| **Field note** | 4 min | Magazine spread, first person, full-bleed image | Nothing | Your Expedia stories, the ones that build trust |

The 26 modules get re-typed against this table. Expect roughly 10 core lessons, 8 quick concepts, 4 playbooks, 4 field notes. Same content, radically different rhythm.

### 3.2 Add Level 0: "What AI Isn't"

Placed before Level 1, framed as clearing the room rather than teaching. Five myth-busters, 15 minutes total, no quiz anywhere in it. The reviewer's insight is correct: you cannot pour information into someone whose guard is up.

Proposed five, ordered by how much they block learning:

1. **"It's going to take my job."** The fear that stops people from touching it at all. Address the displacement question honestly, including where the reviewer's peers are actually right, then reframe to task-level rather than job-level.
2. **"It just makes things up, so I can't trust any of it."** Confabulation is real. Name it plainly, explain when it happens and when it does not, give the verification habit. Credibility comes from conceding the flaw first.
3. **"It's learning from everything I type."** The data fear, which is the one that stops senior people from pasting anything real. Cover what actually happens by tool tier, plainly.
4. **"It's basically a person / it's basically magic."** Deflates both directions at once. Sets up every mechanical lesson that follows.
5. **"I've tried it, it wasn't impressive."** The quiet one. Most senior skeptics tried it once, gave a lazy prompt, got a lazy answer, and closed the tab. Reframe the bad first date without condescending.

**Tone rule for Level 0:** concede before you correct. Every myth-buster opens by taking the fear seriously and stating the part of it that is legitimate. Any whiff of "actually, you're wrong" and the guard goes higher, not lower.

### 3.3 Motivation: proof over points

**The finding.** The site currently stores exactly four things: `mmai-m{id}` (current screen), `mmai-done-{id}` (reached last screen), `mmai-streak`, `mmai-last`. Quiz answers are computed at render and discarded.

Every badge and medal on the index is therefore derived from a single fact: the learner clicked "next" eight times. **The system tracks attendance, not capability.** That is why the gamification reads as hollow. It is rewarding the one thing that required no effort, and this audience notices immediately.

**The decision.** Keep the motivational loop, change its currency. Replace points with proof.

Four distinct things get bundled under "gamification." Only one is actually misfiring:

| Layer | Verdict |
|---|---|
| **Orientation** (where am I, what's left) | Keep. Not a game mechanic, it reduces anxiety. |
| **Competence feedback** (did that land?) | Keep and strengthen. Currently discarded the moment it is given. |
| **Investment** (something I made and can use) | Build. Does not exist yet. The strongest retention lever for professionals. |
| **Performative reward** (medals, flame, confetti) | Remove. |

**Removing:** badges row, medals, streak counter, flame icon, gauge.
Streaks specifically punish the busy executive who is the target user, and a broken streak is a churn trigger rather than a retention one. Replaced by a quiet "pick up where you left off" on return.

**Building instead, two artifacts:**

1. **"What you can now do."** A running list, one plain-language capability statement per completed lesson. Not "Module 4 complete" but "You can spot when AI is confabulating and check it in under a minute." Same dopamine loop, honest currency.

2. **The cheat sheet.** Every module already ends with a "say it to a colleague" takeaway line. That is a competence artifact currently being used as decoration. Collected across completed lessons and exportable to one page, it becomes something the learner actually uses at work on Monday. It is also shareable, which makes it a distribution channel as well as a retention feature.

Note these are different objects and both are needed: a **takeaway** is what is true ("AI has a gas tank"), a **capability** is what you can now do. The cheat sheet collects takeaways. The progress list collects capabilities.

**Content cost:** 31 capability statements need to be written, one per lesson including Level 0. Roughly a paragraph of work each, and they should be drafted alongside the Phase 3 migration.

### 3.4 The state layer (this is what Phase 0 must build)

Moving from 4 flat keys accumulating across 26+ entries to one versioned, namespaced object:

```js
mmai.v2 = {
  v: 2,
  lessons: {
    "module-1": {
      pos: 3,                  // resume position
      done: true,
      doneAt: "2026-07-20",
      checks: [1, 0, 1],       // per-question result
      firstTry: 2              // score on first attempt, NEVER overwritten
    }
  },
  saved:      ["module-1", "module-7"],  // takeaways starred for the cheat sheet
  lastLesson: "module-4",                // for "pick up where you left off"
  lastSeen:   "2026-07-20"
}
```

Design calls worth challenging:

- **One key, not N.** Easier to version, migrate, export, and eventually sync to Supabase, which you already use for topic suggestions. Today's scheme leaks a new key per module forever.
- **`firstTry` is written once and never overwritten.** If retakes overwrite the score, the capability list becomes a participation trophy again. First attempt is the only honest signal.
- **Capabilities are derived at render, not stored.** Storing them creates drift when lesson content changes. Cheap to compute from `lessons`.
- **Migration required.** Existing learners have `mmai-m*` and `mmai-done-*` in their browsers. Phase 0 ships a one-time migration so nobody loses progress.
- **Export must be trivial.** A single JSON object makes the cheat sheet export, and any future account sync, a non-event.

---

## 4. The visual system

### 4.1 Per-level theming: "editions"

The reviewer named this as the highest-value change and they are right. The logic: each level is a different edition of the same publication, same typography and grid, different paper and ink. Progress is felt on arrival, not read off a bar.

All five pairings verified against WCAG AA (body text contrast in parentheses).

| Level | Edition | Paper | Ink | Accent | Contrast |
|---|---|---|---|---|---|
| **0. What AI Isn't** | Slate & Chalk | `#EDF0F2` | `#1F2933` | `#1E5F63` | 12.9 / 6.4 |
| **1. Foundations** | Barro & Marigold | `#FAF5EC` | `#2B231D` | `#9C4128` | 14.2 / 6.0 |
| **2.** | Olive & Bone | `#F3F2E7` | `#242621` | `#3D6349` | 13.6 / 6.1 |
| **3.** | Ochre & Rust | `#F8EFE2` | `#2E2119` | `#8F3A1E` | 13.7 / 6.6 |
| **4. Under the Hood** | Ink & Ember | `#1A1715` | `#F2EADF` | `#E58A4A` | 15.0 / 6.9 |

Why this arc works:

- **Level 0 is deliberately cool and not warm.** It is the myth-clearing room, not the classroom. It also means arriving at Level 1's warmth feels like being welcomed in, which is exactly the emotional beat you want after the guard comes down.
- **Level 1 keeps your existing brand exactly.** The brand kit is not thrown away, it becomes home base.
- **Levels 2 and 3 deepen and warm progressively.** Subtle. The learner should notice without being able to say why.
- **Level 4 goes dark.** "Under the hood" literally means backstage, lights down, looking at the machinery. It is the biggest visual payoff in the course and it is earned by three levels of buildup. This is the moment the theming stops being decoration and becomes narrative.

Each edition also varies one non-color element: section marker motif, rule weight, and for Level 4, margin notes and diagrams instead of cards.

### 4.2 Fixing the composition

- **Break the single column.** Analogy moments go full-bleed with generous space around them. Field notes get an asymmetric spread. The 660px measure stays for body prose only, where it belongs.
- **Real typographic scale.** Currently the range is roughly 11px to 36px with most content clustered at 17px. Widen it. Let the analogy line be large enough to function as an image.
- **Replace all 86 emoji** with a small consistent icon set, or with nothing. Most of them are decorating a heading that does not need decoration.
- **Vary card treatment by purpose.** Right now a quiz, a takeaway, and a story all live in the same box. They should not.

---

## 5. Phasing

**Phase 0. Extract the shared system. ✅ DONE July 20 2026.**

Result: 66 files migrated, 1264KB of HTML reduced to 629KB plus 32KB of shared assets. Zero inline `<style>` blocks remain. All 66 files verified structurally clean, and 48 behavioural assertions pass across EN and ES modules in jsdom.

- `assets/core.css` (138 lines): the style block that was duplicated byte-for-byte across 52 files, plus the accessibility baseline.
- `assets/themes.css`: all five editions. Only `.ed-1` is applied, and it reproduces the old palette exactly.
- `assets/state.js`: the `mmai.v2` store with migration off the old keys.
- `assets/module.js`: one runner replacing 26 near-identical copies.
- `assets/index.css`, `glossary.css`, `about.css`: page-specific remainders.
- `design/migrate-phase0.js`: the migration, re-runnable with `--check` for a dry run.

Removed: streak counter, flame, badges row, medals, and the `mmai-streak` / `mmai-last` keys.

Note: the 26 inline runners could not be extracted by copy-paste. Three things were baked into each one (module id, level name, quiz explanation text). Those now live in `data-*` attributes and in the DOM, which is why `/es` no longer needs a forked script.

*Original scope, for reference:*

- `assets/core.css` and `assets/themes.css`: the duplicated CSS pulled out of all 71 files, with the five editions as theme classes on `<body>`.
- `assets/module.js`: the module runner, extracted once.
- `assets/state.js`: the `mmai.v2` store from 3.4, with migration from the old keys.

Nothing visible changes except the removal of medals and streak. Everything after this becomes cheap instead of impossible. *This is non-negotiable and it comes first.*

**Phase 1. Design direction on one module. ✅ REFERENCE BUILT July 20 2026. Awaiting review.**

Module 1 (the gas tank) rebuilt in the new system, EN and ES. 36 behavioural assertions pass, 10 new colour pairings verified AA.

- `assets/lesson.css`: the new system. Separate from `core.css` on purpose, so the other 25 modules keep working while this is iterated on.
- `assets/suggest.js`: the suggestion form, which was also duplicated inline in every file with the endpoint and key repeated each time.
- `design/editions.html`: all five editions side by side.
- `design/module-1.phase0.html`, `design/module-1.es.phase0.html`: the pre-Phase-1 versions, for comparison.

What changed, and why:

| Change | Reason |
|---|---|
| Real type scale, 11px to ~72px fluid | The old scale sat between 11 and 36px with most content at 17px, so nothing read as emphasised |
| Analogy is full-bleed and oversized, no card | It is the thing people remember. It should behave like an image, not another box |
| One asymmetric spread per lesson | Breaks the single-column monotony without becoming a new template |
| Takeaway inverted to dark | The old one was a warm card with a giant decorative quote mark, which read as an inspirational poster |
| Quiz is hairline-separated, not stacked cards | Same content, far less furniture |
| Pull quote breaks the prose column | The old build never varied measure |
| Emoji removed | Loudest AI-output tell, wrong register for this audience |
| Gauge and flame removed from the header | Progress is a 2px rule and a small-caps label |
| Capability statement on the done screen | The new currency. Replaces the medal |

*Still open before Phase 3:* index page rebuild, and whether the wizard survives for core lessons or the whole lesson becomes one scroll.

*Original scope, for reference:*

**Phase 2. Level 0.** Author the five myth-busters in the new myth-buster format and Slate & Chalk edition. This is the highest-value content addition in the plan and it is new writing, not migration.

**Phase 3. Re-type and migrate the 26.** Assign each existing module its format from the table in 3.1, restructure content to fit, apply the level edition. The teaching content survives mostly intact; the shell around it changes.

**Phase 4. Spanish mirror.** 35 files. Much cheaper post-Phase-0 since the styling is shared and only content differs. Applies the existing Mexico-first, gender-neutral style rules.

**Phase 5, later.** Profession use-case picker. Live in-page prompt box, which needs a key, a proxy, rate limiting, and abuse controls, so it deserves its own plan.

---

## 6. Open questions

1. **Level 4 dark mode:** worth confirming on your actual devices before committing. It is the boldest call in the plan.
2. **Level 2 and 3 names.** They are currently generic. The edition system works better if the levels have real names the way Level 0 and Level 4 do.
3. **Quiz retention.** Keeping quizzes only on core lessons drops total quizzes from 26 to about 10. Since quiz results now feed the capability list, fewer quizzes means fewer capability statements can be evidence-backed. Options: let quick concepts contribute capabilities on completion alone, or give them a single check question. Worth deciding before Phase 3.
5. **Cheat sheet format.** Print-friendly HTML page, downloadable PDF, or both. PDF is more useful at work and more shareable; HTML is far less work. Decide before Phase 3.
4. **Stale deadline.** `CLAUDE.md` still lists a June 17 deadline and a "Week 1 of 3" sprint status, which is over a year old. Worth updating so it stops steering planning.

---

## 7. What I would do first

Phase 0, this week. It is unglamorous and it is the only reason the redesign has not already happened. Then one module in five editions, and you will know within a day whether the direction is right.
