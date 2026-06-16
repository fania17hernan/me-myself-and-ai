# DESIGN.md — Me, Myself & AI

**Brand:** Me, Myself & AI
**Tagline:** Finally, AI that makes sense for *your* work.
**Product:** AI Foundations course for smart, non-technical professionals
**Owner:** Stephanie Hernandez
**Format:** Stitch DESIGN.md (extended) · v1.0 · June 2026

> Drop this file into any project and tell your AI agent: "Build this UI using DESIGN.md."
> Priority order: **phone first → iPad → desktop web.**

---

## 1. Visual Theme & Atmosphere

Warm editorial. The product should feel like a smart, beautifully printed book that happens to live on your phone — not a SaaS dashboard, not a YouTube thumbnail, not a corporate LMS.

- **Mood:** calm confidence. A trusted colleague explaining something over coffee, not a professor lecturing.
- **Density:** low. One idea per screen. Generous whitespace is the product — it signals "this won't overwhelm you," which is the brand promise.
- **Philosophy:** analogies-first, jargon-translated. The UI mirrors the pedagogy: warm, human surface; precise structure underneath.
- **Personality cues:** paper and ink, marginalia, a single confident accent color used like a highlighter — sparingly and meaningfully.
- **Anti-references:** neon gradients, dark "techbro" themes, stock robot imagery, glassmorphism. Nothing that says "engineering tool."

## 2. Color Palette & Roles

Warm neutrals as canvas; terracotta as the single hero accent; marigold for highlights; deep green for success/progress. Names carry the brand's warmth.

| Token | Name | Hex | Role |
|---|---|---|---|
| `--color-paper` | Masa | `#FAF5EC` | App background, the "page" |
| `--color-surface` | Crema | `#FFFDF8` | Cards, sheets, quiz panels |
| `--color-surface-warm` | Horchata | `#F3EADC` | Secondary surfaces, callouts, analogy boxes |
| `--color-ink` | Espresso | `#2B231D` | Primary text, headings |
| `--color-ink-soft` | Cortado | `#6B5C50` | Secondary text, captions, labels |
| `--color-accent` | Barro | `#BF5538` | Primary actions, links, active states, brand mark |
| `--color-accent-deep` | Adobe | `#9C4128` | Pressed/hover states, accent text on light surfaces |
| `--color-highlight` | Marigold | `#E5A33F` | Progress fills, highlights, "key idea" markers |
| `--color-success` | Nopal | `#4E7A5A` | Correct answers, completion, positive deltas |
| `--color-error` | Chile | `#A33B2E` | Incorrect answers, destructive (use rarely; never shame) |
| `--color-line` | Hilo | `#E3D7C6` | Borders, dividers, hairlines |

**Rules**
- Barro (accent) appears **once per screen** as the dominant action. If everything is terracotta, nothing is.
- Never place Barro text on Horchata — contrast is too low. Use Adobe `#9C4128` for accent text on warm surfaces.
- Error states get gentle copy ("Not quite — here's why") and Chile only on the icon/border, never full red panels.
- Dark mode (v2): invert to Espresso canvas `#221B16`, Crema text `#F4EBDD`, keep Barro/Marigold as-is.

## 3. Typography Rules

Two faces only. Serif display for warmth and authority; humanist sans for clarity at small sizes.

- **Display / headings:** `Fraunces` (Google Fonts; optical size axis on, `'SOFT' 50`) — bookish, warm, a little personality.
- **Body / UI:** `Inter` — invisible, legible, professional.

| Style | Font | Size (phone) | Size (desktop) | Weight | Line height | Use |
|---|---|---|---|---|---|---|
| Display | Fraunces | 34px | 48px | 600 | 1.12 | Module titles, screen headers |
| H2 | Fraunces | 26px | 32px | 600 | 1.2 | Section heads ("The Core Analogy") |
| H3 | Inter | 18px | 20px | 700 | 1.35 | Card titles, sub-points |
| Body | Inter | 17px | 18px | 400 | 1.65 | Lesson text — never below 17px on phone |
| Body-strong | Inter | 17px | 18px | 600 | 1.65 | Inline emphasis, key terms |
| Caption | Inter | 13px | 14px | 500 | 1.4 | Labels, progress text, metadata |
| Takeaway | Fraunces italic | 22px | 26px | 500 italic | 1.4 | The one-sentence takeaway, pull quotes |

**Rules**
- Lesson body text is the hero. Optimize for 8–12 minute reads: max line length 34ch on phone, 62ch desktop.
- Jargon terms get Body-strong + a Marigold underline (2px) the first time they appear, paired with an inline plain-language translation.
- Never set long body copy in Fraunces. Never set headlines in Inter.

## 4. Component Stylings

**Buttons**
- Primary: Barro fill, Crema text, 999px pill, 16px/24px padding, min-height 52px (thumb-friendly). Hover/press → Adobe. Subtle lift shadow on press, no gradients.
- Secondary: transparent, 1.5px Hilo border, Espresso text. Hover → Horchata fill.
- Text link: Adobe, underline on hover only.

**Cards**
- Crema surface, 20px radius, 1px Hilo border, shadow level 1 (see §6). Padding 24px phone / 32px desktop.
- "Analogy card" variant: Horchata fill, no border, a 4px Marigold left rule, Fraunces H2 lead-in.

**Takeaway card** (signature component)
- Horchata surface, oversized quote glyph in Barro at 20% opacity, takeaway in Fraunces italic, share affordance below. This is the screenshot-able moment of every module.

**Progress**
- Pill track in Hilo, fill in Marigold→Barro gradient (the one permitted gradient), 8px tall, rounded. Label as "Step 3 of 6" in Caption — never percentages.

**Quiz**
- Options are full-width tappable cards (min 56px tall), 16px radius, Hilo border. Selected → Barro border 2px. Correct → Nopal border + soft `#EAF1EB` fill + check icon. Incorrect → Chile border + explanation text, never a buzzer feeling.

**Navigation (phone)**
- Sticky bottom bar: Crema, top hairline, one Primary button ("Continue") right-aligned, ghost "Back" left. Safe-area padded.

**Inputs**
- Crema fill, Hilo border, 12px radius, 16px padding, Barro focus ring (2px, 20% alpha halo).

## 5. Layout Principles

- **Spacing scale:** 4 / 8 / 12 / 16 / 24 / 32 / 48 / 64. Default rhythm between blocks: 24px phone, 32px desktop.
- **Phone (default):** single column, 20px side margins, content max-width 100%. One concept per screen; advance with the bottom bar.
- **iPad / ≥768px:** content column max 640px, centered. Side margins grow, type steps up one size.
- **Desktop / ≥1100px:** content column max 720px centered; optional slim left rail for module navigation. Never multi-column lesson text.
- Whitespace philosophy: when in doubt, add space. Crowding reads as "complicated," which breaks the brand promise.

## 6. Depth & Elevation

Paper-like: depth comes from warm tints and hairlines more than shadows.

| Level | Use | Shadow |
|---|---|---|
| 0 | Page background | none |
| 1 | Cards, quiz options | `0 1px 2px rgba(43,35,29,.06), 0 4px 12px rgba(43,35,29,.05)` |
| 2 | Sticky bars, modals, takeaway card | `0 4px 8px rgba(43,35,29,.08), 0 12px 32px rgba(43,35,29,.10)` |

No glows, no colored shadows, no glass blur.

## 7. Do's and Don'ts

**Do**
- Carry each module's analogy into the UI (Module 1 = a fuel gauge as the progress meter).
- Translate every technical term inline, immediately, in plain language.
- Use Barro once per screen for the single most important action.
- Keep every screen completable in under 90 seconds of reading.
- Write microcopy peer-to-peer: "Not quite — here's the thing…" not "Incorrect."

**Don't**
- No robots, brains, circuit boards, or blue-glow AI clichés.
- No jargon in UI chrome ("tokens remaining" → "fuel left").
- No more than one accent action per screen; no walls of text; no autoplay.
- No dark-pattern urgency (countdowns, fake scarcity).
- Don't shame wrong quiz answers — every miss is a teaching beat.

## 8. Responsive Behavior

- **Breakpoints:** base (phone, design target 390px) → 768px (iPad) → 1100px (desktop).
- **Touch targets:** 52px minimum height, 8px minimum gap. Bottom-bar actions within thumb reach.
- **Phone-first means content-first:** every feature must work one-handed on a 390px screen before it earns a desktop layout.
- Sticky bottom nav on phone; at ≥768px the Continue/Back controls move inline below content.
- Respect `prefers-reduced-motion`; all transitions ≤250ms ease-out, fade+rise only.
- Test order: iPhone Safari → iPad Safari → desktop Chrome. Ship nothing that fails step one.

## 9. Agent Prompt Guide

**Quick palette:** paper `#FAF5EC` · surface `#FFFDF8` · warm surface `#F3EADC` · ink `#2B231D` · soft ink `#6B5C50` · accent `#BF5538` · accent-deep `#9C4128` · highlight `#E5A33F` · success `#4E7A5A` · error `#A33B2E` · line `#E3D7C6`

**Fonts:** Fraunces (display) + Inter (body), via Google Fonts.

**Ready-to-use prompt:**
> Build a mobile-first lesson screen using DESIGN.md (Me, Myself & AI). Cream paper background (#FAF5EC), Fraunces serif headings, Inter body at 17px+, one terracotta (#BF5538) pill button in a sticky bottom bar, cards with 20px radius and warm hairline borders, marigold progress pill labeled "Step X of Y". Warm, calm, editorial — like a printed book, not a dashboard. No gradients except the progress fill, no tech clichés.
