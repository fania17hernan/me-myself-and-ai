# Information architecture and user journeys

**Date:** July 20 2026
**Decisions taken:** 2 to 3 minute units · desktop sidebar with mobile bottom tabs · home leads with one clear next action.

---

## 1. What the research actually says

Four findings shaped this, and one of them contradicts the brief.

**Duolingo's linear path beat its own branching tree.** When Duolingo replaced the skill tree with a single sequential path in 2022, learners took longer but reached *better proficiency outcomes*. The path also carried lessons at three difficulty levels where the tree only exposed the easy tier. The lesson is not "add streaks." It is that **removing choice about what comes next raises completion.**

There is a caveat worth stealing. The path *lost* the tree's "cracked skills," the visual cue showing which skills had gone rusty. Duolingo gave up targeted review to get linear clarity. **You do not have to make that trade**, because Phase 0's `firstTry` field already records which questions each learner missed on the first attempt. You have the data Duolingo threw away the affordance for. That becomes "Worth another look" on the home screen.

**Brilliant's rule is one concept per lesson.** Visual and hands-on first to build intuition, start from the simplest version of the idea to hold cognitive load down, and give instant custom feedback on every answer. Your modules already do one analogy each, and your quiz explanations are already custom per wrong answer. Splitting nine-minute modules into 2 to 3 minute units is what brings the rest of it in line.

**The TikTok format only works when it ends in recall.** The critique of educational short-form is consistent: the algorithm optimises for watch time rather than understanding, and 60-second clips lack depth and any retention mechanism. What rescues it is active recall, one moment of being asked to produce the answer. So borrow TikTok's **pacing and momentum**, not its **feed**. No algorithmic ordering, no infinite scroll. Short self-contained units that each end in a small act of recall.

**Navigation: the brief asked for a hamburger, and the evidence says not for primary items.** Feature discovery drops 30 to 50% when items live behind a hamburger, because out of sight reads as nonexistent. Airbnb measured 40% faster task completion with a bottom tab bar. Apple's HIG and Material both recommend tabs for 3 to 5 primary destinations. Hence the split you chose: **persistent sidebar on desktop, bottom tabs on mobile, hamburger reserved for genuinely secondary items.** The hamburger still exists. It just stops hiding the things you need people to find.

### The tension worth naming

Duolingo's engine is streaks, XP and leagues. That is precisely the layer we removed in Phase 0 for being wrong for skeptical senior professionals. Both calls stand, because Duolingo's *durable* mechanics are not the streak. They are:

1. There is always exactly one obvious next action.
2. Units are small enough that finishing one is never in doubt.
3. Feedback is immediate and specific.

Those three transfer to a VP. The flame does not.

---

## 2. The content model

Three levels of structure, where today there are two.

```
Level        5 of them, each a visual "edition"      L0 … L4
  Topic      26, the existing modules, now grouping  "Tokens & Rate Limits"
    Unit     ~75, 2 to 3 min, ONE idea each          "Why answers cut off"
```

**The unit is the new atom.** It is what the path lists, what progress counts, what a URL points at, and what a learner can finish in a queue at a coffee shop. Topics stop being things you *do* and become things you *have done*.

### Unit types

Carried over from the redesign plan, now applied at unit scale.

| Type | Length | Ends with | Roughly |
|---|---|---|---|
| Myth-buster | 2 min | A reframe, no quiz | 5 (all of Level 0) |
| Concept | 3 min | One recall question | ~34 |
| Analogy | 2 min | Say-it-back prompt | ~14 |
| Playbook | Reference | Nothing, it is a tool | ~10 |
| Field note | 3 min | Nothing | ~8 |
| Check | 2 min | 3 questions, closes a topic | ~26, one per topic |

Splitting Module 1 shows the shape:

> **Topic: Tokens & Rate Limits**
> 1. *The answer that died mid-sentence* (field note, 2 min)
> 2. *Tokens are gas in a tank* (analogy, 2 min)
> 3. *What's actually in the tank* (concept, 3 min)
> 4. *Three habits that save fuel* (playbook, 2 min)
> 5. *Quick check* (check, 2 min)

Same content. Five entry points instead of one, five completion moments instead of one, and no session longer than three minutes.

---

## 3. Sitemap

```
/                          Home · resume + path + worth another look
│
├── /learn/                The path
│   ├── /learn/l0/         What AI Isn't        (Slate & Chalk)
│   ├── /learn/l1/         Foundations          (Barro & Marigold)
│   ├── /learn/l2/         …                    (Olive & Bone)
│   ├── /learn/l3/         …                    (Ochre & Rust)
│   ├── /learn/l4/         Under the Hood       (Ink & Ember)
│   └── /u/<slug>          A unit. First-class, linkable, shareable
│
├── /use-it/               By profession · the reviewer's ask
│   └── /use-it/<role>     Teacher, small business owner, HVAC tech, …
│
├── /glossary/             Every term, plain words
│   └── /glossary#<term>   Deep-linkable, cross-links to the unit that teaches it
│
├── /you/                  Progress, capabilities, cheat sheet
│   ├── what you can now do    (derived from completed units)
│   ├── your cheat sheet       (saved takeaways, exportable)
│   └── worth another look     (units where firstTry was missed)
│
└── secondary — sidebar footer on desktop, hamburger on mobile
    ├── /about/
    ├── language EN ⇄ ES
    ├── suggest a topic
    └── accessibility & display
```

**Four primary destinations. Everything else is secondary.** That is the discipline the tab-bar research imposes, and it is a feature: it forces a decision about what this product is *for*.

| | EN | ES |
|---|---|---|
| 1 | Home | Inicio |
| 2 | Use It | Aplícalo |
| 3 | Glossary | Glosario |
| 4 | You | Tu avance |

`/learn/` deliberately has no tab. Home *is* the path. Giving the path its own tab duplicates Home and wastes one of four slots.

---

## 4. User journeys

### A. The skeptic · first visit, guard up

The reviewer's senior colleague. Arrives suspicious, will leave if it feels like a toy.

```
Lands on /
  ↓  sees no medals, no flame, no streak. Sees a claim and a 2-minute promise
"Start with what AI isn't"          ← not "Start learning"
  ↓
/u/it-wont-take-your-job            myth-buster, 2 min, no quiz
  ↓  concedes the legitimate part of the fear before correcting anything
"That took 2 minutes. Four more?"
  ↓
Finishes Level 0 in 15 min, guard down
  ↓
Level 1 opens, and the paper turns warm
```

**Design requirement:** the first screen a skeptic sees must not ask for commitment, must not gamify, and must lead with a myth-buster rather than a curriculum.

### B. The returning learner · four minutes, standing up

The dominant repeat session. Optimise ruthlessly for it.

```
Opens / on a phone
  ↓  ONE card, above the fold, thumb-height
"Pick up where you left off · What's actually in the tank · 3 min"
  ↓  one tap, no menu, no scrolling, no "where was I"
Unit
  ↓
Done → capability line added → "Next: Three habits that save fuel · 2 min"
  ↓
Leaves, or takes one more
```

**Design requirement:** from cold open to learning content in **one tap**. This is the single number worth protecting in every future design decision.

### C. The reference seeker · mid-workday

Heard "token" in a meeting. Not learning, looking something up.

```
/ → Glossary tab (or ⌘K search on desktop)
  ↓
Types "token"
  ↓
Plain definition, 1 sentence, no login, no lesson
  ↓
"Learn this properly · 2 min" ← optional, never forced
```

**Design requirement:** the glossary must answer without teaching. Offer the unit; never gate the definition behind it.

### D. The stuck learner · motivated but directionless

The reviewer's "analysis paralysis" case. Willing, no idea where to start.

```
/ → Use It
  ↓
"What do you do?"  → Teacher · Small business owner · HVAC technician · …
  ↓
Three concrete tasks, in their language
  "Write next week's lesson plans"
  "Turn a hard concept into an analogy your students will get"
  ↓
Each task links to the unit that makes it possible
```

**Design requirement:** Use It sells outcomes, not curriculum. The profession is the entry point, the unit is the payoff.

---

## 5. Navigation

### Mobile · bottom tabs, hamburger for secondary

Tabs sit in the thumb zone. Most people hold a phone one-handed and the thumb rests over the bottom third, which is why a top-left hamburger is ergonomically wrong for anything frequent.

```
┌──────────────────────────┐
│ ☰   Me, Myself & AI   ES │  ← hamburger = secondary only
├──────────────────────────┤
│                          │
│        content           │
│                          │
├──────────────────────────┤
│  ⌂     ✦      A      ◔   │  ← 4 tabs, thumb zone, labels always visible
│ Home  Use It Gloss.  You │
└──────────────────────────┘
```

Labels stay visible. Icon-only tabs test badly for exactly the audience that is already unsure it belongs here.

### Desktop · persistent sidebar

Space exists, so nothing needs hiding. Secondary items live at the bottom of the rail rather than behind a menu.

```
┌────────────┬───────────────────────────────┐
│ M, M & AI  │                               │
│            │        content, 36rem         │
│ ⌂ Home     │        measure for prose      │
│ ✦ Use It   │                               │
│ A Glossary │                               │
│ ◔ You      │                               │
│            │                               │
│ ── ── ──   │                               │
│ About      │                               │
│ Español    │                               │
│ Suggest    │                               │
│ Display    │                               │
└────────────┴───────────────────────────────┘
```

**Inside a unit, both platforms hide the chrome.** Reading is a full-attention mode. Tabs and sidebar collapse to a back affordance and a progress hairline, and return on completion. This is the one place a hamburger genuinely wins: nothing competes with the content.

---

## 6. Home screen composition

Priority order, top to bottom. Everything above the fold on a phone.

1. **Resume card.** Unit name, type, minutes, one primary button. If nobody has started, this becomes "Start with what AI isn't · 2 min."
2. **Worth another look.** Appears only when `firstTry` recorded a miss. One unit at a time, never a list of failures. This is the affordance Duolingo gave up.
3. **The path.** Five levels, current one expanded to show units, others collapsed to a title and a count. Orientation, not the primary action.
4. **What you can now do.** Latest two capability statements plus a link to `/you/`. Proof, not points.

Deliberately absent: streak, medals, badges, XP, league.

---

## 7. Open questions before build

1. **How do ~75 units get authored?** One HTML file per unit is 150 files across both languages. Hand-authoring that is how the current 71-file problem started. Recommend a small build step generating units from markdown, which also makes the Spanish mirror a translation task rather than a duplication task.
2. **Do units need their own URLs?** Yes for sharing and for the glossary to link into, but it costs the file sprawl in question 1. The two are the same decision.
3. **Tab label "You."** Clear in English, awkward in Spanish. `Tu avance` is proposed and is two words where the others are one.
4. **Does `/learn/` need a tab after all?** Testing will tell. Watch whether people go looking for a browse view that Home does not obviously provide.
5. **Level 0 placement.** It is the recommended first stop for a skeptic, but a returning learner should never be pushed back into it.

---

## Sources

- [Duolingo path vs tree, proficiency outcomes whitepaper](https://duolingo-papers.s3.amazonaws.com/reports/Duolingo_whitepaper_language_read_listen_write_speak_2024.pdf)
- [Duolingo's Daily Refresh, on losing "cracked" skills](https://devansh.design/daily-refresh)
- [Brilliant, learn by doing](https://brilliant.org/faq/) and [Brilliant Basics](https://brilliant.org/help/using-brilliant/)
- [NN/g, basic patterns for mobile navigation](https://www.nngroup.com/articles/mobile-navigation-patterns/)
- [Hamburger menu vs tab bar](https://www.onething.design/post/hamburger-menu-vs-tab-bar)
- [Mobile navigation patterns in 2026](https://phone-simulator.com/blog/mobile-navigation-patterns-in-2026)
- [TikTok in higher education, systematic review](https://www.tandfonline.com/doi/full/10.1080/10494820.2025.2564736)
- [Educational scrolling apps, on active recall](https://nibble-app.com/blog/educational-scrolling-apps)
