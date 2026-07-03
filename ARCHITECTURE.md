# Me, Myself & AI, Engineering & Architecture

*For any engineer picking this up. Covers the stack, how it's built, the cost model, a security review, and how to scale. Last updated June 19, 2026.*

---

## 1. What this is

A bilingual (EN/ES) micro-course that teaches AI concepts to non-technical professionals. It is a **static website**, plain HTML/CSS/JS, every page pre-generated and served as a flat file. The only server-side component is a single write-only endpoint for the optional "suggest a topic" form (§6a); everything else is fully static.

- **Live (EN):** https://fania17hernan.github.io/me-myself-and-ai/
- **Live (ES):** https://fania17hernan.github.io/me-myself-and-ai/es/
- **Repo:** https://github.com/fania17hernan/me-myself-and-ai (public)
- **Scope today:** 4 levels, 19 lessons, a 32-term glossary, a level-select landing page, EN/ES throughout.

---

## 2. Tech stack

| Layer | Choice | Notes |
|---|---|---|
| Markup/UI | Hand-written HTML5 + CSS (CSS custom properties) | No framework. No build-time CSS tooling. |
| Interactivity | Vanilla JavaScript (no libraries) | Inline `<script>` per page; ~60 lines each. |
| Fonts | Google Fonts (Fraunces + Inter) via `<link>` | Only external runtime dependency. Served from Google's CDN, HTTPS. |
| Content generation | Python 3 (standard library only) | Generates all HTML from data files. See §4. |
| Hosting | GitHub Pages | Free static hosting from the `main` branch. |
| Progress | Browser `localStorage` | Per-device progress only. No accounts. |
| Suggestions | Supabase (Postgres) REST, insert-only | Single write-only endpoint for the "suggest a topic" form. See §6a. |

There is **no** authentication, analytics, cookies, or third-party script beyond Google Fonts. The only server interaction is a one-way, write-only topic-suggestion `POST` to Supabase (§6a), no data is read back into the site.

---

## 3. Cost model, it's free, and sharing it stays free

**Today it costs $0, and sharing the link with users does not introduce per-user cost.** Here's why, concretely:

- **Hosting (GitHub Pages):** free for public repositories. Soft limits are **100 GB bandwidth/month**, 1 GB site size, 10 builds/hour. Pricing has been stable (verified May 2026).
- **Page weight:** each lesson page is ~18–20 KB; the whole site is well under 1 MB. Google Fonts are served by Google (not counted against GitHub bandwidth) and cached by the browser after first load.
- **What that means in practice:** 100 GB/month ÷ ~50 KB for a typical multi-page session ≈ **~2 million sessions/month** before hitting the *soft* limit. Beta (5–10 people) or even thousands of learners is nowhere near it.
- **No usage-based billing exists anywhere in this stack.** Hosting is flat-free; the suggestion form writes to Supabase's free tier (free for 500K monthly Edge/API requests and 500 MB database, topic suggestions are tiny and rare, nowhere near it). Adding users adds zero marginal cost.

**The only theoretical cost** is GitHub Pages bandwidth *overage at extreme scale* (sustained hundreds of GB/month). It's a soft limit, GitHub emails you first; nothing auto-charges. If that ever happens, moving to Cloudflare Pages / Netlify (also free, higher limits) is a ~10-minute migration since it's just static files.

**One cleanup item:** an earlier duplicate of Module 1 was deployed as a Supabase Edge Function (`me-myself-and-ai`, project `pdbqrjqlwqjqzefmmlhd`). It's redundant now that GitHub Pages is canonical and sits on Supabase's free tier, but it should be **deleted** to avoid confusion and shrink the surface area. (Supabase free tier wouldn't bill at this scale either.)

---

## 4. How it's built (the generator)

All HTML is **generated**, never hand-edited. Source lives in `_build/`:

| File | Role |
|---|---|
| `_build/bili_common.py` | Shared CSS, fonts, the fuel-gauge SVG, and a `js_str()` helper. |
| `_build/bili_en.py` | English content: `UI` (interface strings), `MODULES` (all 19 lessons), `LEVELS`, `GLOSSARY`. |
| `_build/bili_es.py` | Spanish content: same four structures, mirrored. |
| `_build/build_bilingual.py` | The generator. Renders templates → writes all `.html` files. |

**Data model:**
- A **module** is a dict: `title`, `analogy_name`, `subtitle`, `in_module[]`, `hook`, `analogy`, `how`, `foryou`, `takeaway`, a 3-question `quiz[]`, `next_teaser`. Each has a global number `n` (1–19).
- A **level** groups module numbers: `{id, slug, name, tagline, modules:[...], status:"live"|"soon"}`.
- A **glossary entry**: `{term, def, analogy, n}` where `n` links to a lesson (or `0` = reference-only, no link).

**To run:** `cd _build && python3 build_bilingual.py`, regenerates the EN tree at the repo root and the ES tree in `/es/`. No dependencies to install (standard library only).

**To change content:** edit the relevant dict in `bili_en.py` / `bili_es.py`, rerun the generator, redeploy (§5). Editing the template or CSS once updates every one of the ~40 pages consistently, this is why it's a generator and not 40 hand-maintained files.

**Page structure (every lesson):** a single HTML file with 8 stacked `<section class="screen">` blocks (cover → problem → analogy → how → for-you → takeaway → quiz → done). JS toggles one screen at a time, drives the progress gauge, scores the quiz, and writes progress to `localStorage`.

---

## 5. Repository structure & deployment

```
me-myself-and-ai/
├── index.html              # Level-select landing (EN)
├── level-1..4.html         # Per-level hubs (EN)
├── module-1..19.html       # Lessons (EN)
├── glossary.html           # Searchable glossary (EN)
├── es/                     # Full Spanish mirror (same filenames)
├── _build/                 # Python generator + content (source of truth)
├── DESIGN.md               # Brand/design system
├── brand-preview.html      # Visual style catalog
├── ROADMAP.md              # Product roadmap
└── ARCHITECTURE.md         # This file
```

**Deployment:** GitHub Pages serves the `main` branch root. A push/commit to `main` triggers an automatic Pages build (~1–2 min) and the live site updates. Current workflow has been GitHub's web upload UI; a `git push` from a clone does the same thing. **Recommended next step:** commit `_build/` to the repo (done) and optionally add a GitHub Action to run the generator on push so source and output can never drift.

---

## 6. Data & privacy model

- **No personal data is collected or transmitted.** There is no form submission, no analytics, no cookies, no tracking.
- **Progress** (which lessons are done, where you left off) is stored in the visitor's own browser via `localStorage` keys (`mmai-done-<n>`, `mmai-m<n>`). It never leaves the device and is not readable by the site owner.
- **Quiz answers** are evaluated entirely in-browser; nothing is sent anywhere.
- The course content has no backend. There is exactly **one** server touch, the optional "suggest a topic" form (§6a). Apart from a suggestion a visitor chooses to type, no user data is collected or transmitted.

### 6a. The one backend touch, "Suggest a topic"

A small, deliberately-scoped feature lets learners tell us what to build next. It appears on the landing page and on every lesson's completion screen.

**Data flow**
1. Visitor types a free-text suggestion (and, optionally, an email if they want a reply).
2. On submit, the page makes a single `POST` from the browser to the Supabase REST API: `POST https://pdbqrjqlwqjqzefmmlhd.supabase.co/rest/v1/topic_suggestions`.
3. Supabase inserts one row: `{ suggestion, email (nullable), lang, source, created_at }`. `source` records which page it came from (e.g. `landing`, `module-7`), so you can see what sparked each idea.
4. The owner reads submissions in the **Supabase dashboard → Table Editor → `topic_suggestions`** (or via the service role). Nothing is emailed or pushed.

**What's in the page:** the Supabase project URL and the **publishable** API key (`sb_publishable_…`). This key is *designed to be public* and embedded in client code, it is not a secret. Its power is bounded entirely by Row-Level Security (below).

**Security model (Row-Level Security):**
- The `topic_suggestions` table has RLS **enabled**.
- One policy: the `anon` role may `INSERT` only (`with check (true)`).
- There is **no `SELECT` policy**, so the public key can **never read** rows. A visitor can submit but cannot see anyone's submissions (including their own). Only the owner, via the dashboard/service role, can read.
- Column `CHECK` constraints cap lengths (suggestion ≤ 1000 chars, email ≤ 200) to limit abuse.
- The form includes a hidden **honeypot** field; if a bot fills it, the submit is silently dropped client-side.

**Privacy:** email is optional and only requested for replies. No other PII is asked for. Treat the table as low-sensitivity user-submitted text and clear it periodically if you like.

**Residual risk (low, acceptable for this stage):** a public insert endpoint can be spammed (someone could script inserts using the public key). Mitigations in place: length caps, honeypot, and Supabase's baseline rate limiting. If spam ever becomes a problem, options are: add a CAPTCHA/Turnstile check, move the insert behind a lightweight Edge Function with rate limiting, or rotate the publishable key. None are needed at beta scale.

---

## 7. Security review

**Posture: low risk.** An almost-entirely-static site with no accounts, no secrets, and a single write-only public endpoint has a very small attack surface. Findings:

**Checked and clear**
- **No secrets in the repo.** Scanned all HTML/MD for keys, passwords, bearer/auth strings. The only embedded credential is the Supabase **publishable** key (`sb_publishable_…`), which is intended to be public and is bounded by Row-Level Security (§6a). No service-role key, no private secrets. (Matches for "token"/"password" are course *content*.)
- **No third-party scripts** except Google Fonts CSS over HTTPS. No analytics/ad/tracker scripts, no external JS.
- **One outbound `fetch`**, and only one: the suggestion form's `POST` to the project's own Supabase REST endpoint (§6a). No other network calls.
- **No XSS sink from untrusted input.** The glossary search filters pre-rendered cards via `textContent`/`indexOf` (never `innerHTML`). The suggestion form sends user text via `JSON.stringify` and never re-renders it into the page; its only `innerHTML` write is a fixed, build-time success string. All displayed content is build-time static.
- **Suggestion endpoint is locked down**, RLS insert-only for `anon`, no read access, length caps, honeypot (§6a).
- **No `eval`, no dynamic script injection, no `localStorage` of sensitive data** (only a screen index and completion flags).
- **No mixed content**, everything is HTTPS (GitHub Pages and Supabase both enforce TLS).

**Notes / hardening recommendations (optional, low priority)**
1. **Add a Content-Security-Policy** meta tag to formalize "only self + Google Fonts." Defense-in-depth; not strictly needed given no untrusted input. Example: `default-src 'self'; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src https://fonts.gstatic.com; script-src 'self' 'unsafe-inline'`.
2. **Inline scripts** use `'unsafe-inline'`. Fine for a static teaching site; if you ever want a strict CSP, move JS to external files with hashes.
3. **Public repo = public content.** Anyone can view source and copy the lessons. That's expected for a marketing/teaching funnel, but it is *not* a place to ever put paid-only content, answer keys you care about hiding, or anything private. Gated/paid content must live behind a real backend (see §8).
4. **Delete the redundant Supabase Edge Function** (§3) to remove an unused public endpoint.
5. **Account hygiene:** the GitHub account (`fania17hernan`) is the single point of control. Enable 2FA; the repo's safety depends on that login.

**No vulnerabilities found that require action before sharing.**

---

## 8. Scaling considerations

The static architecture is the right call for now (free, fast, simple, secure). You'd only outgrow it when you need things a static site fundamentally can't do. Triggers and options:

| When you need… | Add… | Why |
|---|---|---|
| Accounts / login | An auth provider (e.g. Supabase Auth, Clerk) | Identity requires a backend. |
| Payments / paid tiers | Stripe + a tiny backend or serverless function to gate access | Never gate paid content client-side, it's all viewable in a static site. |
| Cross-device progress, completion analytics | A database (Supabase/Postgres) writing progress server-side | Replaces `localStorage`. |
| Certificates, cohort features, comments | The Fable platform (per the product roadmap) or a LMS | Don't rebuild an LMS; the PRD already plans Fable. |
| Profession tracks, more levels | Nothing new, extend the generator | The data-driven generator scales to N levels/modules for free. |

**Migration cost is low.** Because output is plain static files, moving hosts (Cloudflare Pages, Netlify, Vercel) is a drag-and-drop / connect-repo step. The generator is host-agnostic.

**Guiding principle:** keep the *teaching content* static and free; introduce a backend only for the specific features that require state or money, and keep that backend small and well-scoped.
