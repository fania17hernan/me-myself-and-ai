/* =============================================================
   Me, Myself & AI  ·  build/validate.mjs

   The rules from design/TAXONOMY.md, enforced. Run standalone or
   imported by build.mjs, which refuses to emit on any error.

   The point of this file: a calendar reminder to re-check facts is
   a thing people ignore. A failing build is not.
   ============================================================= */

import { readdirSync, readFileSync, existsSync } from 'node:fs';
import { join } from 'node:path';
import { frontmatter, parseYaml } from './lib.mjs';

export const TYPES = ['myth-buster', 'analogy', 'concept', 'playbook', 'field-note', 'check'];
export const VOLATILITY = { evergreen: 24, slow: 12, fast: 3 };   // months to review
export const TOOL_SCOPE = ['agnostic', 'tool-specific'];

const monthsBetween = (a, b) =>
  (b.getFullYear() - a.getFullYear()) * 12 + (b.getMonth() - a.getMonth());

export function loadGlossary(root) {
  const p = join(root, 'content', 'glossary.yml');
  if (!existsSync(p)) return [];
  const raw = readFileSync(p, 'utf8');
  // top-level list of maps
  const items = [];
  let cur = null;
  for (const line of raw.split('\n')) {
    if (!line.trim() || /^\s*#/.test(line)) continue;
    if (/^-\s/.test(line)) {
      cur = {};
      items.push(cur);
      const kv = line.replace(/^-\s*/, '').match(/^([\w-]+):\s*(.*)$/);
      if (kv && kv[2]) cur[kv[1]] = kv[2].replace(/^["']|["']$/g, '');
      continue;
    }
    if (!cur) continue;
    const kv = line.trim().match(/^([\w-]+):\s*(.*)$/);
    if (!kv) continue;
    let v = kv[2].trim();
    if (/^\[.*\]$/.test(v)) {
      const inner = v.slice(1, -1).trim();
      v = inner ? inner.split(',').map(s => s.trim()) : [];
    } else {
      v = v.replace(/^["']|["']$/g, '');
    }
    cur[kv[1]] = v;
  }
  return items.filter(x => x.id);
}

export function loadUnits(root, lang = 'en') {
  const dir = lang === 'en'
    ? join(root, 'content', 'units')
    : join(root, 'content', lang, 'units');
  if (!existsSync(dir)) return [];
  return readdirSync(dir)
    .filter(f => f.endsWith('.md'))
    .map(f => {
      const { data, body } = frontmatter(readFileSync(join(dir, f), 'utf8'));
      return { file: `${lang}/${f}`, data: data || {}, body };
    });
}

export function validate(root, { now = new Date() } = {}) {
  const errors = [], warnings = [];
  const glossary = loadGlossary(root);
  const termIds = new Set(glossary.map(t => t.id));
  const en = loadUnits(root, 'en');
  const es = loadUnits(root, 'es');
  const esIds = new Set(es.map(u => u.data.id));
  const seen = new Map();

  const professionsPath = join(root, 'content', 'professions.yml');
  let professions = new Set();
  if (existsSync(professionsPath)) {
    const p = parseYaml(readFileSync(professionsPath, 'utf8'));
    professions = new Set((p.professions || []).map(x => (typeof x === 'string' ? x : x.id)));
  }

  for (const u of en) {
    const d = u.data, at = `${u.file}`;
    const E = m => errors.push(`${at}: ${m}`);
    const W = m => warnings.push(`${at}: ${m}`);

    if (!d.id) { E('missing id'); continue; }

    // 1 · ids are unique and never reused
    if (seen.has(d.id)) E(`duplicate id "${d.id}", also in ${seen.get(d.id)}`);
    seen.set(d.id, at);
    if (!/^[a-z0-9]+(-[a-z0-9]+)*$/.test(d.id)) E(`id "${d.id}" is not a kebab slug`);
    if (/(^|-)(unit|module|lesson)?-?\d+$/.test(d.id)) {
      W(`id "${d.id}" encodes a position, which breaks when the curriculum reorders`);
    }

    // 2 · closed sets
    if (!TYPES.includes(d.type)) E(`type "${d.type}" not in ${TYPES.join(', ')}`);
    if (!(d.volatility in VOLATILITY)) E(`volatility "${d.volatility}" not in ${Object.keys(VOLATILITY).join(', ')}`);
    if (d.tool_scope && !TOOL_SCOPE.includes(d.tool_scope)) E(`tool_scope "${d.tool_scope}" invalid`);
    if (![2, 3].includes(d.minutes)) W(`minutes is ${d.minutes}, the atom is meant to be 2 or 3`);

    // 3 · controlled vocabulary. THE rule that stops taxonomy drift.
    for (const t of d.teaches || []) {
      if (!termIds.has(t)) E(`teaches unknown term "${t}" — add it to content/glossary.yml first`);
    }
    for (const p of d.professions || []) {
      if (professions.size && !professions.has(p)) E(`unknown profession "${p}"`);
    }

    // 4 · fact governance
    if (!d.verified) E('missing verified date');
    else {
      const v = new Date(d.verified);
      if (isNaN(v)) E(`verified "${d.verified}" is not a date`);
      else {
        const cadence = VOLATILITY[d.volatility] ?? 24;
        const age = monthsBetween(v, now);
        if (age > cadence) {
          const msg = `${d.volatility} fact last verified ${age} months ago, cadence is ${cadence}`;
          if (d.volatility === 'fast') E(msg); else W(msg);
        } else if (age > cadence - 1) {
          W(`review due within a month (verified ${age} months ago)`);
        }
      }
    }
    const sources = d.sources || [];
    if (d.volatility === 'fast' && sources.length === 0) {
      E('perishable claim with no source. A fast unit must cite what backs it');
    }
    for (const s of sources) {
      if (!s.url) E('source missing url');
      if (!s.supports) W('source has no `supports` line, so it will rot into "something on this page backed this up once"');
    }

    // 5 · outputs the UI depends on
    if (!d.capability && d.type !== 'check') W('no capability statement, so it cannot appear in "what you can now do"');
    if (!d.takeaway && ['analogy', 'concept'].includes(d.type)) W('no takeaway, so nothing to pin to the cheat sheet');

    // 6 · the Spanish mirror can never silently drift again
    if (esIds.size && !esIds.has(d.id)) E(`no Spanish counterpart (expected content/es/units/${d.id}.md)`);
  }

  // orphaned terms
  const taught = new Set(en.flatMap(u => u.data.teaches || []));
  for (const t of glossary) {
    if (!taught.has(t.id)) warnings.push(`glossary: "${t.id}" is defined but no unit teaches it`);
  }

  return { errors, warnings, counts: { en: en.length, es: es.length, terms: glossary.length } };
}

/* ---- CLI --------------------------------------------------------------- */

import { resolve } from 'node:path';
import { pathToFileURL } from 'node:url';
if (import.meta.url === pathToFileURL(resolve(process.argv[1])).href) {
  const root = process.argv[2] || '.';
  const { errors, warnings, counts } = validate(root);
  for (const w of warnings) console.log(`  warn  ${w}`);
  for (const e of errors) console.log(`  ERROR ${e}`);
  console.log(`\n${counts.en} units, ${counts.es} translated, ${counts.terms} terms`);
  console.log(`${errors.length} errors, ${warnings.length} warnings`);
  process.exit(errors.length ? 1 : 0);
}
