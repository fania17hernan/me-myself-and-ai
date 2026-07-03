# Me, Myself & AI, Build-Out Roadmap

*Planning doc. Nothing here is built yet except Level 1. Use this to decide what comes next.*

---

## The north star (unchanged)

Smart professionals who aren't using AI yet are **intimidated, overwhelmed, and lost in jargon**. They don't want a lecture, they want each concept tied to an analogy they already understand. We teach AI the way a sharp friend would explain it over coffee.

Everything below serves one test: *"Can they explain this to a coworker tomorrow?"*

---

## The shape of the product

Three things stacked on the same foundation:

1. **Levels**, depth. You go deeper as you get more comfortable. (Level 1 → 4)
2. **Profession tracks**, relevance. Same ideas, examples swapped for *your* job. (cross-cutting, added later)
3. **Glossary**, a safety net. A searchable A–Z you can check any time a scary word shows up.

A **level-select landing page** is the new front door. Tap a level → see its short cards → tap a card → one concept, one analogy, one quiz. Glossary and "By profession" live on that same home screen.

---

## The levels

### Level 1, Start Here *(BUILT, the 5 you have)*
How the tool *behaves*, so it stops surprising you.

| # | Concept | Analogy |
|---|---------|---------|
| 1 | Tokens & rate limits | The Gas Tank |
| 2 | Context windows | The Whiteboard |
| 3 | Free vs. paid | Test Drive vs. the Lease (ES: la Renta) |
| 4 | Hallucination | The Confident Intern |
| 5 | Your first workflow | The Sous Chef |

### Level 2, The Tools *(YOUR STATED NEXT PRIORITY)*
The features people see in the app and don't understand. *"What's the difference between a chat, a project, an artifact…?"*

| Concept | Proposed analogy | One-line hook |
|---------|------------------|---------------|
| Chat vs. Project | **The phone call vs. the dedicated office** | A chat is a phone call, it ends and it's gone. A Project is an office where everything for one job stays on the desk. |
| Artifacts / Canvas | **The workbench** | A table beside the conversation where the AI *builds the actual thing* (a doc, a sheet, an app) and you edit it live. |
| Connectors | **The set of keys** | You hand the AI keys to your other rooms, email, calendar, Drive, so it can fetch and file things itself. |
| Plugins / Tools | **Drill attachments** (or apps you install) | Snap-on abilities for specific jobs. The drill is the same; you change the head. |
| Custom GPTs / Gems / Agents | **The trained specialist** | You train a helper once for a recurring task; it remembers the instructions every time. |
| Picking a model | **Choosing the vehicle** | Bike, sedan, or moving truck, fast & cheap vs. slow & powerful, matched to the trip. |

### Level 3, Make It Yours
Customization. Turning a generic tool into *your* setup.

| Concept | Proposed analogy |
|---------|------------------|
| Custom instructions | **House rules**, standing preferences it follows every time |
| Memory | **The notebook that actually keeps notes** (vs. Level 1's whiteboard that wipes) |
| Building a Project workspace | **Setting up your workstation** |
| Voice & images (multimodal) | **Giving it eyes and ears** |
| Saved prompts / templates | **Your saved recipes** |

### Level 4, Under the Hood
For the curious who start poking and hit real tech terms. Demystifies vibe-coding & the words behind apps. *(This is also the bridge to the "engineer/builder" profession track.)*

| Concept | Proposed analogy |
|---------|------------------|
| What is "vibe coding" | **Director, not bricklayer**, you describe what you want in plain words; the AI lays the bricks |
| Frontend vs. backend | **The dining room vs. the kitchen** *(extends the Sous Chef!)* |
| API | **The waiter**, you order off the menu, the kitchen makes it, the waiter brings it; you never go in the kitchen |
| Database | **The filing cabinet**, organized storage the app reaches into |
| Hosting / deployment | **Opening the shop to the public** *(literally what we did with your site)* |
| Front/back/server/cloud | one **restaurant universe** that ties them together |

---

## Cross-cutting pieces

### Glossary, "look it up any time"
A searchable A–Z page. Each entry = **plain definition + its analogy + link to the module that teaches it.** Grows automatically as modules are added. Lives on the home screen so it's always one tap away.

### Profession tracks *(add once the content base is rich)*
Same core concepts, **role-specific examples + a curated order.** Candidates you named:

- Student · Business Analyst · Project Manager · Ops Manager · Teacher · Realtor · Engineer/Builder (→ Level 4)

Example: the "good prompt" lesson uses a *client email* for a PM, a *listing description* for a realtor, a *lesson plan* for a teacher. Mechanically it's the same module with swapped examples, so this is cheap to produce once the analogies exist.

---

## The level-select landing page (new front door)

- Big warm header + the brand wordmark and EN/ES toggle (already built).
- A vertical stack of **Level cards**: name, one-line promise, # of modules, a progress ring that fills as you finish modules (reuses the localStorage tracking already in place).
- Two utility tiles below: **Glossary** and **By profession** (the second marked "coming soon" until tracks exist).
- Locked/greyed levels until earlier ones are done? Optional, recommend *not* locking at first; let people roam.

---

## Recommended build sequence

1. **Landing page + reshelve current 5 as Level 1.** Establishes the structure everything else slots into. (small)
2. **Level 2, The Tools.** Your priority. 6 modules, analogies above. (the meat)
3. **Glossary v1.** Seed it with terms from Levels 1–2. Low effort, high reassurance value.
4. **Level 3, Make It Yours.**
5. **Profession tracks** (start with 2–3: e.g., PM, Teacher, Realtor), remix existing modules.
6. **Level 4, Under the Hood.**

Each step ships independently and is testable with beta users before the next.

---

## Open decisions for you

1. **Level names**, keep "Start Here / The Tools / Make It Yours / Under the Hood," or prefer something else?
2. **Level 2 scope**, all 6 tool concepts above, or trim to the 4 that matter most for non-users (likely Chat-vs-Project, Artifacts, Connectors, Custom GPTs)?
3. **Lock levels or leave them open?**
4. Any analogy above that doesn't sit right, easier to swap now than after it's built.
