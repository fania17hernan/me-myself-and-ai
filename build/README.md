# Build

Zero dependencies. `node` and nothing else.

```
node build/validate.mjs .        # check without writing
node build/build.mjs .           # validate, then generate
node build/build.mjs . --check   # dry run
```

Source of truth is `content/`. Everything under `u/`, `es/u/` and
`search-index.json` is generated and gitignored, so nobody can edit the
artefact instead of the source. That mistake is what produced the original
71 files of duplicated inline CSS.

## What the build refuses to ship

| Rule | Result |
|---|---|
| `teaches:` names a term not in `glossary.yml` | error |
| `type` or `professions` outside the closed set | error |
| A `fast` unit with no `sources[]` | error |
| A `fast` unit past its 3-month review | error |
| An English unit with no Spanish counterpart | error |
| `verified` missing or unparseable | error |
| `slow` or `evergreen` unit past review | warning |
| A source with no `supports` line | warning |
| A slug that encodes a position (`unit-1`) | warning |
| A glossary term no unit teaches | warning |

Review cadence comes from `volatility`: evergreen 24 months, slow 12, fast 3.

## Adding a unit

1. Add any new terms to `content/glossary.yml` first. The build will reject
   the unit otherwise, and that is the point.
2. Write `content/units/<slug>.md`. The slug is permanent and must not encode
   level, topic or position.
3. Write `content/es/units/<slug>.md` with the **same slug**. The build fails
   without it, so the Spanish mirror cannot silently drift.
4. If it needs a drawing, add `content/figures/<id>.svg` and reference it with
   `::figure id=<id> label="Fig. 1" caption="…"`.

## Blocks

```
::analogy … ::          the oversized moment
::note … ::             margin annotation, red pencil
::say-it-back … ::      pinnable takeaway
::figure id=… caption="…"
::check answer=1
Question?
- option
- option
::good feedback when right
::bad feedback when wrong
::
```

Inline: `**bold**`, `_italic_`, `` `code` ``, `[[term]]`, `==highlight==`,
`~~drawn underline~~`, `[link](url)`.
