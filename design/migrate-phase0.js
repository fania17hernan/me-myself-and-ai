/* =============================================================
   Phase 0 migration.

   Rewrites module and level files to use the shared assets:
     - the byte-identical <style> block becomes two <link>s
     - the per-module inline runner becomes <script src>
     - the three things that were baked into that runner (module id,
       level name, quiz explanations) move into data-* attributes,
       which is why /es no longer needs a forked script
     - adds the accessibility baseline: skip link, live region

   Rendering is unchanged. Run with --check to diff without writing.
   ============================================================= */

const fs = require('fs');
const path = require('path');
const vm = require('vm');

const ROOT = process.argv[2] || '.';
const CHECK = process.argv.includes('--check');
const ONLY = (process.argv.find(a => a.startsWith('--only=')) || '').split('=')[1];

const esc = s => String(s)
  .replace(/&/g, '&amp;').replace(/"/g, '&quot;')
  .replace(/</g, '&lt;').replace(/>/g, '&gt;');

/* Pull the values that were hardcoded into each inline runner by
   executing it in a stub DOM. Safer than regexing JS string literals,
   which are full of smart quotes and escapes. */
function extract(script) {
  const sandbox = {
    document: {
      querySelectorAll: () => [],
      querySelector: () => null,
      getElementById: () => null
    },
    window: {}, localStorage: undefined
  };
  const out = {};
  const grab = `
    ;out.GID = (typeof GID !== 'undefined') ? GID : null;
    ;out.LVLNAME = (typeof LVLNAME !== 'undefined') ? LVLNAME : null;
    ;out.L = (typeof L !== 'undefined') ? L : null;
    ;out.explains = (typeof explains !== 'undefined') ? explains : null;
  `;
  // strip the IIFE wrapper so the vars land in scope, and drop the
  // trailing render()/listener calls that need a real DOM
  let inner = script
    .replace(/^\s*\(function\(\)\{/, '')
    .replace(/\}\)\(\);\s*$/, '');
  inner = inner.split(/\n\s*function quizDone/)[0];

  sandbox.out = out;
  try {
    vm.createContext(sandbox);
    vm.runInContext(inner + grab, sandbox, { timeout: 2000 });
  } catch (e) { /* partial extraction is fine, we validate below */ }
  return out;
}

function migrate(file) {
  const rel = path.relative(ROOT, file);
  const depth = rel.includes(path.sep) ? '../' : '';
  let html = fs.readFileSync(file, 'utf8');
  const before = html;

  /* 1. style block -> shared stylesheets */
  html = html.replace(
    /[ \t]*<style>[\s\S]*?<\/style>/,
    `<link rel="stylesheet" href="${depth}assets/themes.css">\n` +
    `<link rel="stylesheet" href="${depth}assets/core.css">`
  );

  /* 2. locate the inline runner */
  const runner = html.match(/<script>\s*\(function\(\)\{\s*\n\s*var GID=[\s\S]*?<\/script>/);
  if (!runner) return { file: rel, skipped: 'no runner' };

  const body = runner[0].replace(/^<script>/, '').replace(/<\/script>$/, '');
  const data = extract(body);

  if (!data.GID || !data.explains) return { file: rel, skipped: 'extract failed' };

  /* 3. done-screen strings, which were string literals in the runner */
  const mTitle = body.match(/doneTitle'\)\.textContent=\(s===\d+\)\?"((?:[^"\\]|\\.)*)":"((?:[^"\\]|\\.)*)"/);
  const mScore = body.match(/doneScore'\)\.textContent="((?:[^"\\]|\\.)*)"\+s\+"((?:[^"\\]|\\.)*)"\+\(s===\d+\?"((?:[^"\\]|\\.)*)":"((?:[^"\\]|\\.)*)"\)/);
  const un = s => s ? JSON.parse('"' + s + '"') : '';

  const donePerfect = un(mTitle && mTitle[1]);
  const doneOk      = un(mTitle && mTitle[2]);
  const scoreTpl    = mScore ? un(mScore[1]) + '{s}' + un(mScore[2]).replace(/\b\d+\b/, '{n}') : '';
  const scorePerf   = un(mScore && mScore[3]);
  const scorePart   = un(mScore && mScore[4]);

  /* 4. explanations move from JS into the markup, next to their question */
  const keys = Object.keys(data.explains).sort((a, b) => a - b);
  let n = 0;
  html = html.replace(/<div class="explain"><\/div>/g, () => {
    const e = data.explains[keys[n++]];
    if (!e) return '<div class="explain"></div>';
    return `<div class="explain" data-good="${esc(e.good)}" data-bad="${esc(e.bad)}"></div>`;
  });
  if (n !== keys.length) return { file: rel, skipped: `explain mismatch ${n}/${keys.length}` };

  /* 5. body data contract */
  const L = data.L || {};
  const attrs = [
    `data-lesson="module-${data.GID}"`,
    `data-level="${esc(data.LVLNAME || '')}"`,
    `data-i18n-step="${esc(L.step || 'Step')}"`,
    `data-i18n-of="${esc(L.of || 'of')}"`,
    `data-i18n-complete="${esc(L.complete || 'Complete')}"`,
    `data-i18n-start="${esc(L.start || '')}"`,
    `data-i18n-cont="${esc(L.cont || '')}"`,
    `data-i18n-finish="${esc(L.finish || '')}"`,
    `data-done-perfect="${esc(donePerfect)}"`,
    `data-done-ok="${esc(doneOk)}"`,
    `data-score-tpl="${esc(scoreTpl)}"`,
    `data-score-perfect="${esc(scorePerf)}"`,
    `data-score-partial="${esc(scorePart)}"`,
    `class="ed-1"`
  ].join(' ');
  html = html.replace(/<body>/, `<body ${attrs}>`);

  /* 6. accessibility baseline. Skip-link text is localised off the
        existing <html lang>, so /es gets Spanish, not English. */
  const isES = /<html lang="es"/.test(html);
  const skipTxt = isES ? 'Saltar al contenido' : 'Skip to content';
  html = html.replace(
    /(<body [^>]*>)/,
    `$1\n<a class="skip" href="#main">${skipTxt}</a>\n<div id="live" class="sr-only" role="status" aria-live="polite"></div>`
  );
  if (!/id="main"/.test(html)) html = html.replace(/<main([ >])/, '<main id="main" tabindex="-1"$1');

  /* 7. runner -> shared scripts */
  html = html.replace(runner[0],
    `<script src="${depth}assets/state.js"></script>\n<script src="${depth}assets/module.js"></script>`);

  if (!CHECK) fs.writeFileSync(file, html, 'utf8');
  return {
    file: rel,
    ok: true,
    saved: before.length - html.length,
    questions: keys.length
  };
}

const files = [];
for (const dir of [ROOT, path.join(ROOT, 'es')]) {
  if (!fs.existsSync(dir)) continue;
  for (const f of fs.readdirSync(dir)) {
    if (/^module-\d+\.html$/.test(f)) files.push(path.join(dir, f));
  }
}

const targets = ONLY ? files.filter(f => f.includes(ONLY)) : files;
let bytes = 0, ok = 0;
for (const f of targets) {
  const r = migrate(f);
  if (r.ok) { ok++; bytes += r.saved; }
  else console.log(`  SKIP ${r.file}: ${r.skipped}`);
}
console.log(`${CHECK ? '[dry run] ' : ''}${ok}/${targets.length} files, ${(bytes / 1024).toFixed(0)}KB removed`);
