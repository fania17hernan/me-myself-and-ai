# Spanish style guide

**Standing rule:** the Spanish version must read naturally to someone in Mexico *and* someone in Spain. No regionalisms that stop one of them cold, no untranslated English, no jargon.

This is a change from the earlier "Mexico-first" instruction. Where the two conflict, this file wins.

---

## The test

Before shipping a sentence, ask: **would a reader in Madrid and a reader in Monterrey both understand this on first pass, without stumbling?**

If a word is natural in one and odd in the other, replace it with the neutral option. If there is no neutral option, rewrite the sentence to avoid needing the word. Rewriting around the problem is almost always better than picking a side.

---

## Found in the current build

These are real instances from `es/module-1.html`, which is representative of the other 25.

| Current | Problem | Use instead |
|---|---|---|
| **carro** | Mexico and Colombia. In Spain a *carro* is a cart. | Avoid the noun. The analogy works on *el tanque* and *la gasolina* alone. Where a noun is unavoidable, **coche**. |
| **descompuesta** | Mexico. Spain says *estropeada* or *rota*. | **que no funcionaba** / **que fallaba** |
| **seguido** (meaning "often") | Mexico. Reads as "in a row" in Spain. | **a menudo** / **con frecuencia** |
| **quedarte varado** | Latin America. Spain says *tirado*. | **quedarte a medias** / **quedarte atascado** |
| **le di enter** | Mexican register plus untranslated English. *Pulsé* is Spain, *presioné* is LatAm. | Sidestep it: **y envié el mensaje** |
| **offsite** | Untranslated English jargon sitting inside a lesson about plain language. | **la reunión de equipo** |
| **¿Mejor jugada?** | Understood in both but tilts Mexican. | **¿Qué conviene hacer?** |
| **se portan raro** | Colloquial, tilts Mexican. | **se comportan igual de raro** (keeps the warmth, travels fine) |
| **pedacito** | Fine, but *trocito* is the Spain instinct. | **un pedazo de palabra** |

---

## Standing vocabulary

| Avoid | Because | Use |
|---|---|---|
| computadora / ordenador | Splits Mexico vs Spain exactly | **tu equipo**, or rewrite |
| celular / móvil | Same split | **el teléfono** |
| carro / coche / auto | Three-way split | Rewrite to avoid; **coche** if forced |
| jalar, platicar, ahorita, rentar, checar | Mexican | tirar, hablar, ahora mismo, alquilar, revisar |
| vale, guay, coger, ordenador, móvil | Spain | de acuerdo, genial, tomar, equipo, teléfono |
| tomar (Spain: fine; Mexico: fine) | Safe in both | keep |

**Never use *coger*.** Neutral in Spain, vulgar across most of Latin America. Use *tomar* or *agarrar*-free rewrites.

---

## Jargon

The whole premise of this course is plain language, so untranslated English is a credibility problem, not just a style one.

**Keep in English** (these are the actual product or concept names, and translating them would confuse):
`token`, `chat`, `prompt`, `software`, `email`

Gloss each one on first use in a lesson, the way the gas tank module already glosses *token* as *un pedazo de palabra*.

**Always translate:** offsite, deadline, meeting, feedback, insight, workflow, brainstorming, target, budget, briefing, output, input.

For *input* and *output* the existing translation is already right: **la entrada** and **la salida**.

---

## Register

- **Address the reader as *tú*.** Consistent across both markets for this audience, and already the choice throughout.
- **Gender-neutral.** No *bienvenidos*, no *los usuarios*. Use *te damos la bienvenida*, *quienes usan*, *la persona que*. Avoid *@* and *-x* endings; they break screen readers.
- **No em-dashes.** Commas, colons, periods. Same rule as the English.
- **Warmth survives translation.** The English is conversational and a little wry. Do not let the neutral-Spanish requirement flatten it into corporate Spanish. Neutral means *understood everywhere*, not *formal*.

---

## Accessibility

Applies to `/es` identically to the English. As of Phase 0:

- `<html lang="es">` on every Spanish page, `lang="en"` on every English one.
- Skip link is localised (`Saltar al contenido`).
- All UI strings come from `data-i18n-*` attributes on `<body>`, so the Spanish pages share the same `module.js` as the English. There is no forked script to drift.
- Quiz explanations live in the DOM as real text, not in JavaScript string literals, so they are translatable and readable by assistive tech.
- Correct and incorrect answers are marked with ✓ and ✕ in addition to colour.

**Still to do:** the copy fixes in the table above, across all 26 Spanish modules. That is Phase 4 work.
