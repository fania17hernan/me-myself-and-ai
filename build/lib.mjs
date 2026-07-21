/* =============================================================
   Me, Myself & AI  ·  build/lib.mjs
   Frontmatter, a small markdown subset, and the block components.

   ZERO DEPENDENCIES ON PURPOSE. This repo publishes to GitHub Pages
   and the whole point of the taxonomy work is that it survives.
   A build that needs `npm install` to run in three years is a build
   that will not run in three years.
   ============================================================= */

/* ---- YAML subset -------------------------------------------------------
   Handles exactly the schema in design/TAXONOMY.md and nothing else:
   scalars, inline arrays, block lists, and one level of nested maps
   (which is all `sources:` and `translations:` need). Anything outside
   that surfaces as a validation error rather than being silently
   mis-parsed, which is the failure mode that matters.
   ------------------------------------------------------------------- */

function coerce(v) {
  if (v === '' || v == null) return null;
  const s = String(v).trim();
  if (s === 'true') return true;
  if (s === 'false') return false;
  if (s === 'null' || s === '~') return null;
  if (/^-?\d+$/.test(s)) return parseInt(s, 10);
  if (/^-?\d*\.\d+$/.test(s)) return parseFloat(s);
  if (/^\[.*\]$/.test(s)) {
    const inner = s.slice(1, -1).trim();
    return inner ? inner.split(',').map(x => coerce(x)) : [];
  }
  if ((s.startsWith('"') && s.endsWith('"')) || (s.startsWith("'") && s.endsWith("'"))) {
    return s.slice(1, -1);
  }
  return s;
}

export function parseYaml(src) {
  const out = {};
  const lines = src.split('\n')
    .filter(l => l.trim() && !/^\s*#/.test(l));

  let i = 0;
  while (i < lines.length) {
    const line = lines[i];
    const m = line.match(/^(\s*)([A-Za-z0-9_-]+):\s*(.*)$/);
    if (!m) { i++; continue; }
    const [, indent, key, rest] = m;
    if (indent.length > 0) { i++; continue; }  // handled by parents below

    if (rest !== '') { out[key] = coerce(rest); i++; continue; }

    // block: either a list of scalars, a list of maps, or a nested map
    const child = [];
    i++;
    while (i < lines.length && /^\s+/.test(lines[i])) { child.push(lines[i]); i++; }
    if (!child.length) { out[key] = null; continue; }

    if (child[0].trim().startsWith('-')) {
      const items = [];
      let cur = null;
      for (const c of child) {
        const t = c.trim();
        if (t.startsWith('- ')) {
          const body = t.slice(2);
          const kv = body.match(/^([A-Za-z0-9_-]+):\s*(.*)$/);
          if (kv) { cur = { [kv[1]]: coerce(kv[2]) }; items.push(cur); }
          else { items.push(coerce(body)); cur = null; }
        } else if (cur) {
          const kv = t.match(/^([A-Za-z0-9_-]+):\s*(.*)$/);
          if (kv) cur[kv[1]] = coerce(kv[2]);
        }
      }
      out[key] = items;
    } else {
      const map = {};
      for (const c of child) {
        const kv = c.trim().match(/^([A-Za-z0-9_-]+):\s*(.*)$/);
        if (kv) map[kv[1]] = coerce(kv[2]);
      }
      out[key] = map;
    }
  }
  return out;
}

export function frontmatter(src) {
  const m = src.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n?([\s\S]*)$/);
  if (!m) return { data: null, body: src };
  return { data: parseYaml(m[1]), body: m[2] };
}

/* ---- Escaping ---------------------------------------------------------- */

export const esc = s => String(s ?? '')
  .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
export const attr = s => esc(s).replace(/"/g, '&quot;');

/* ---- Inline markdown ---------------------------------------------------
   Deliberately small: bold, italic, code, links, and the two studio marks.
   Anything more and authors start reaching for HTML, which defeats the
   point of having a source of truth.
   ------------------------------------------------------------------- */

function inline(s) {
  return esc(s)
    .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
    .replace(/(^|[\s(])_(.+?)_(?=[\s.,;:!?)]|$)/g, '$1<em>$2</em>')
    .replace(/`(.+?)`/g, '<code>$1</code>')
    .replace(/\[\[(.+?)\]\]/g, '<span class="term">$1</span>')      // glossary term
    .replace(/==(.+?)==/g, '<span class="mark-hl">$1</span>')        // kraft highlight
    .replace(/~~(.+?)~~/g, '<span class="mark-u">$1</span>')         // drawn underline
    .replace(/\[(.+?)\]\((.+?)\)/g, '<a href="$2">$1</a>');
}

/* ---- Block components --------------------------------------------------
   ::figure id=gas-tank caption="…"     pulls content/figures/<id>.svg
   ::analogy … ::                        the oversized moment
   ::note … ::                           margin annotation, red pencil
   ::say-it-back … ::                    the takeaway a learner can pin
   ::check answer=1 … ::                 recall, with ::good / ::bad
   ------------------------------------------------------------------- */

export function render(body, ctx = {}) {
  const lines = body.split('\n');
  const out = [];
  let i = 0;

  const flushPara = buf => {
    const t = buf.join(' ').trim();
    if (t) out.push(`<p>${inline(t)}</p>`);
    buf.length = 0;
  };
  const para = [];

  while (i < lines.length) {
    const line = lines[i];

    if (/^::/.test(line)) {
      flushPara(para);
      const head = line.slice(2).trim();
      const name = head.split(/\s+/)[0];

      if (name === 'figure') {
        const id = (head.match(/id=([\w-]+)/) || [])[1];
        const cap = (head.match(/caption="([^"]*)"/) || [])[1] || '';
        const label = (head.match(/label="([^"]*)"/) || [])[1] || 'Fig.';
        const svg = ctx.figures?.[id];
        out.push(
          `<figure class="plate">` +
          `<span class="fig">${esc(label)}</span>` +
          (svg || `<p class="soft">Figure <code>${esc(id)}</code> not drawn yet.</p>`) +
          (cap ? `<figcaption class="cap">${inline(cap)}</figcaption>` : '') +
          `</figure>`
        );
        i++; continue;
      }

      // fenced blocks
      const buf = [];
      i++;
      while (i < lines.length && lines[i].trim() !== '::') { buf.push(lines[i]); i++; }
      i++; // closing ::
      const text = buf.join('\n').trim();

      if (name === 'analogy') {
        out.push(`<p class="analogy-line">${inline(text)}</p>`);
      } else if (name === 'note') {
        out.push(`<p class="hand">${inline(text)}</p>`);
      } else if (name === 'say-it-back') {
        out.push(
          `<div class="card taped tilt-l pinnable">` +
          `<p class="label">Pin to your bench</p>` +
          `<p class="pin-line">${inline(text)}</p>` +
          `<button class="btn btn-2 pin" type="button" data-pin>＋ Pin it</button>` +
          `</div>`
        );
      } else if (name === 'check') {
        const answer = parseInt((head.match(/answer=(\d+)/) || [])[1] ?? '0', 10);
        const qLines = text.split('\n');
        const q = qLines.shift().trim();
        const opts = [], feedback = { good: '', bad: '' };
        for (const l of qLines) {
          const t = l.trim();
          if (t.startsWith('- ')) opts.push(t.slice(2));
          else if (t.startsWith('::good ')) feedback.good = t.slice(7);
          else if (t.startsWith('::bad ')) feedback.bad = t.slice(6);
        }
        out.push(
          `<div class="check" data-q="0" data-answer="${answer}">` +
          `<p class="q">${inline(q)}</p>` +
          opts.map(o => `<button class="opt" type="button">${inline(o)}</button>`).join('') +
          `<p class="explain hand" hidden data-good="${attr(feedback.good)}" data-bad="${attr(feedback.bad)}"></p>` +
          `</div>`
        );
      }
      continue;
    }

    if (/^#{2,3}\s/.test(line)) {
      flushPara(para);
      const level = line.startsWith('###') ? 3 : 2;
      out.push(`<h${level}>${inline(line.replace(/^#+\s/, ''))}</h${level}>`);
      i++; continue;
    }

    if (/^[-*]\s/.test(line)) {
      flushPara(para);
      const items = [];
      while (i < lines.length && /^[-*]\s/.test(lines[i])) {
        items.push(`<li>${inline(lines[i].replace(/^[-*]\s/, ''))}</li>`);
        i++;
      }
      out.push(`<ul>${items.join('')}</ul>`);
      continue;
    }

    if (!line.trim()) { flushPara(para); i++; continue; }
    para.push(line);
    i++;
  }
  flushPara(para);
  return out.join('\n');
}
