/* =============================================================
   Me, Myself & AI  ·  build/build.mjs

   content/units/*.md  →  /u/<slug>/index.html
   content/es/units/*.md → /es/u/<slug>/index.html

   Refuses to emit if validate.mjs reports an error.

   URLs carry the slug only. Hierarchy is metadata, never a path
   segment, because hierarchy is the most volatile thing here and a
   permanent address must survive it. See design/TAXONOMY.md §4.

   Usage:  node build/build.mjs [root] [--check]
   ============================================================= */

import { readdirSync, readFileSync, writeFileSync, mkdirSync, existsSync, rmSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { frontmatter, render, esc, attr } from './lib.mjs';
import { validate, loadGlossary, loadUnits, VOLATILITY } from './validate.mjs';

const ROOT = process.argv[2] && !process.argv[2].startsWith('--') ? process.argv[2] : '.';
const CHECK = process.argv.includes('--check');

const UI = {
  en: { skip: 'Skip to content', home: 'Home', use: 'Use It', gloss: 'Glossary',
        prog: 'Progress', cont: 'Continue', of: 'of', unit: 'unit',
        pinned: 'Pin to your bench', next: 'Next', checked: 'Checked' },
  es: { skip: 'Saltar al contenido', home: 'Inicio', use: 'Aplícalo', gloss: 'Glosario',
        prog: 'Tu avance', cont: 'Continuar', of: 'de', unit: 'unidad',
        pinned: 'Fíjalo en tu mesa', next: 'A continuación', checked: 'Verificado' }
};

const MONTHS = {
  en: ['January','February','March','April','May','June','July','August','September','October','November','December'],
  es: ['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']
};

/* ---- figures ----------------------------------------------------------- */

function loadFigures(root) {
  const dir = join(root, 'content', 'figures');
  const out = {};
  if (!existsSync(dir)) return out;
  for (const f of readdirSync(dir).filter(x => x.endsWith('.svg'))) {
    out[f.replace(/\.svg$/, '')] = readFileSync(join(dir, f), 'utf8').trim();
  }
  return out;
}

/* ---- page shell -------------------------------------------------------- */

function shell({ d, html, lang, prefix, t, stamp, nextUnit }) {
  const tabs = [
    ['◧', t.home, `${prefix}`],
    ['✦', t.use, `${prefix}use-it/`],
    ['A', t.gloss, `${prefix}glossary/`],
    ['◔', t.prog, `${prefix}progress/`]
  ].map(([ic, label, href]) =>
    `<a href="${href}"><span class="ic" aria-hidden="true">${ic}</span>${esc(label)}</a>`).join('');

  const kindLabel = d.type.replace('-', ' ');

  return `<!DOCTYPE html>
<html lang="${lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<meta name="theme-color" content="#F1EEE7">
<title>${esc(d.title)} · Me, Myself &amp; AI</title>
<meta name="description" content="${attr(d.capability || d.takeaway || d.title)}">
<link rel="canonical" href="${prefix === '../../' ? '' : ''}/u/${d.id}/">
<link rel="alternate" hreflang="en" href="/u/${d.id}/">
<link rel="alternate" hreflang="es" href="/es/u/${d.id}/">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght,SOFT,WONK@0,9..144,300..700,0..100,0..1;1,9..144,300..700,0..100,0..1&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="${prefix}assets/studio.css">
</head>
<body data-lesson="${attr(d.id)}" data-level="${attr(String(d.level))}" data-type="${attr(d.type)}">
<a class="skip" href="#main">${esc(t.skip)}</a>
<div id="live" class="sr-only" role="status" aria-live="polite"></div>

<header class="top">
  <a class="wordmark" href="${prefix}">Me, Myself <em>&amp;</em> AI</a>
  <a class="label" href="${lang === 'en' ? `/es/u/${d.id}/` : `/u/${d.id}/`}"
     hreflang="${lang === 'en' ? 'es' : 'en'}">${lang === 'en' ? 'ES' : 'EN'}</a>
</header>
<div class="prog"><i style="width:0%"></i></div>

<main id="main" tabindex="-1" class="wrap">
  <p class="label red">${esc(kindLabel)} · ${d.minutes} min</p>
  <h1>${esc(d.title)}</h1>
${html}
${stamp}
${nextUnit}
</main>

<nav class="tabs" aria-label="${esc(t.home)}">${tabs}</nav>
<script src="${prefix}assets/state.js"></script>
<script src="${prefix}assets/unit.js"></script>
</body>
</html>
`;
}

/* ---- main -------------------------------------------------------------- */

const { errors, warnings, counts } = validate(ROOT);
for (const w of warnings) console.log(`  warn  ${w}`);
if (errors.length) {
  for (const e of errors) console.log(`  ERROR ${e}`);
  console.log(`\nRefusing to build: ${errors.length} error(s).`);
  process.exit(1);
}

const figures = loadFigures(ROOT);
const glossary = loadGlossary(ROOT);
let written = 0, redirects = 0;

for (const lang of ['en', 'es']) {
  const units = loadUnits(ROOT, lang);
  if (!units.length) continue;
  const t = UI[lang];
  const prefix = lang === 'en' ? '../../' : '../../../';
  const byTopic = {};
  for (const u of units) (byTopic[u.data.topic] ||= []).push(u);
  for (const k in byTopic) byTopic[k].sort((a, b) => (a.data.order || 0) - (b.data.order || 0));

  for (const { data: d, body } of units) {
    const html = render(body, { figures });

    // freshness stamp, tool-specific units only. Turns the biggest
    // credibility risk into a credibility signal.
    let stamp = '';
    if (d.tool_scope === 'tool-specific' && d.verified) {
      const v = new Date(d.verified);
      stamp = `\n<p class="stamp label">${esc(t.checked)} ${esc(MONTHS[lang][v.getMonth()])} ${v.getFullYear()}</p>`;
    }

    const siblings = byTopic[d.topic] || [];
    const idx = siblings.findIndex(s => s.data.id === d.id);
    const nxt = siblings[idx + 1];
    const nextUnit = nxt
      ? `\n<hr class="torn">\n<p class="label">${esc(t.next)}</p>\n` +
        `<a class="btn" href="${prefix.replace('../../', '../')}${nxt.data.id}/">${esc(nxt.data.title)} →</a>`
      : '';

    const dir = lang === 'en' ? join(ROOT, 'u', d.id) : join(ROOT, 'es', 'u', d.id);
    const page = shell({ d, html, lang, prefix, t, stamp, nextUnit });
    if (!CHECK) {
      mkdirSync(dir, { recursive: true });
      writeFileSync(join(dir, 'index.html'), page, 'utf8');
    }
    written++;

    // slug_history → redirect stubs, so a rename never 404s
    for (const old of d.slug_history || []) {
      const rdir = lang === 'en' ? join(ROOT, 'u', old) : join(ROOT, 'es', 'u', old);
      const target = lang === 'en' ? `/u/${d.id}/` : `/es/u/${d.id}/`;
      if (!CHECK) {
        mkdirSync(rdir, { recursive: true });
        writeFileSync(join(rdir, 'index.html'),
          `<!DOCTYPE html><html lang="${lang}"><head><meta charset="UTF-8">` +
          `<link rel="canonical" href="${target}">` +
          `<meta http-equiv="refresh" content="0; url=${target}">` +
          `<title>Moved</title></head><body><p><a href="${target}">Moved here</a></p></body></html>`, 'utf8');
      }
      redirects++;
    }
  }
}

/* ---- search index + reverse term index --------------------------------- */

const units = loadUnits(ROOT, 'en');
const taughtBy = {};
for (const u of units) for (const term of u.data.teaches || []) (taughtBy[term] ||= []).push(u.data.id);

const index = {
  generated: new Date().toISOString().slice(0, 10),
  units: units.map(u => ({
    id: u.data.id, title: u.data.title, type: u.data.type, level: u.data.level,
    topic: u.data.topic, minutes: u.data.minutes, teaches: u.data.teaches || [],
    professions: u.data.professions || [], capability: u.data.capability || null,
    takeaway: u.data.takeaway || null, url: `/u/${u.data.id}/`
  })),
  glossary: glossary.map(t => ({ ...t, taught_by: taughtBy[t.id] || [] }))
};
if (!CHECK) writeFileSync(join(ROOT, 'search-index.json'), JSON.stringify(index, null, 2), 'utf8');

console.log(`\n${CHECK ? '[dry run] ' : ''}${written} pages, ${redirects} redirects, ` +
            `${counts.terms} terms indexed, ${warnings.length} warnings`);
