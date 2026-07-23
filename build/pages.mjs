/* =============================================================
   Me, Myself & AI  ·  build/pages.mjs
   The shell pages: home and glossary.

   Home is the learning surface, so there is no /learn/ tab. It shows
   the path server-rendered, and home.js marks what's done from the
   mmai.v2 store and lifts the next unit into a resume card.

   Legacy modules are scanned from disk rather than listed by hand, so
   they drop off this page automatically as each one is converted.
   ============================================================= */

import { readdirSync, readFileSync, existsSync } from 'node:fs';
import { join } from 'node:path';
import { esc, attr } from './lib.mjs';

const LEVELS = {
  0: { en: "What AI isn't", es: "Lo que la IA no es" },
  1: { en: 'Foundations',   es: 'Fundamentos' },
  2: { en: 'Make It Yours', es: 'Hazlo tuyo' },
  3: { en: 'Working Together', es: 'Trabajar en equipo' },
  4: { en: 'Under the Hood', es: 'Por dentro' }
};

const PROFESSIONS = {
  teacher:             { en: 'Teacher',             es: 'Docente' },
  'small-business-owner': { en: 'Small business owner', es: 'Dueño de un negocio' },
  'hvac-technician':   { en: 'HVAC technician',     es: 'Técnico de climatización' },
  nurse:               { en: 'Nurse',               es: 'Personal de enfermería' },
  recruiter:           { en: 'Recruiter',           es: 'Reclutador' },
  accountant:          { en: 'Accountant',          es: 'Contador' },
  manager:             { en: 'Manager',             es: 'Líder de equipo' },
  'real-estate-agent': { en: 'Real estate agent',   es: 'Agente inmobiliario' },
  nonprofit:           { en: 'Nonprofit',           es: 'Sector social' },
  other:               { en: 'Something else',      es: 'Otra cosa' }
};

const T = {
  en: { skip:'Skip to content', home:'Home', use:'Use It', gloss:'Glossary', prog:'Progress',
        start:'Start here', startSub:'5 myths · 2 min each · no quiz', startCta:'Clear the air first',
        resume:'Pick up where you left off', cont:'Continue', path:'Your path',
        legacy:'Still being rebuilt', legacySub:'These are on the old format while they get split into units.',
        fore:'Foreword', read:'Read why', min:'min', of:'of', units:'units',
        glossTitle:'Every term, in plain words', glossSub:'Look something up. No lesson required.',
        learn:'Learn this properly', tagline:'Two minutes at a time. Analogies that stick. No jargon, no sign-up.',
        hero:'AI, explained by someone who was also intimidated by it.',
        foreLine:'Four companies. Four industries. The same crack in the floor.',
        foreBody:'Manufacturing, travel, healthcare, luxury retail. Different decades, one thing in common: teams moving fast on foundations nobody had been taught.',
        foreHand:'AI is about to do it again. Faster, and to more people.',
        useTitle:'Use it in your work', useSub:'Pick what you do. See the units that pay off first.',
        useNone:'No units tagged for this yet. Start with the foundations.',
        progTitle:'Your progress', progSub:'Proof, not points.',
        progEmpty:'Nothing yet. Finish a unit and it shows up here.',
        progUnits:'units done', progCan:'What you can now do', progSheet:'Your cheat sheet',
        progReview:'Worth another look', progReviewSub:'Units you missed on the first try.',
        progExport:'Export one page', reset:'Reset my progress' },
  es: { skip:'Saltar al contenido', home:'Inicio', use:'Aplícalo', gloss:'Glosario', prog:'Tu avance',
        start:'Empieza aquí', startSub:'5 mitos · 2 min cada uno · sin examen', startCta:'Primero aclaremos el aire',
        resume:'Retoma donde lo dejaste', cont:'Continuar', path:'Tu camino',
        legacy:'En reconstrucción', legacySub:'Estos siguen en el formato anterior mientras se dividen en unidades.',
        fore:'Prólogo', read:'Por qué lo construí', min:'min', of:'de', units:'unidades',
        glossTitle:'Cada término, en palabras claras', glossSub:'Busca algo. No hace falta una lección.',
        learn:'Apréndelo bien', tagline:'Dos minutos a la vez. Analogías que se quedan. Sin tecnicismos, sin registro.',
        hero:'La IA, explicada por alguien a quien también le intimidaba.',
        foreLine:'Cuatro empresas. Cuatro industrias. La misma grieta en el suelo.',
        foreBody:'Manufactura, viajes, salud, moda de lujo. Décadas distintas, una cosa en común: equipos avanzando rápido sobre fundamentos que nadie les había enseñado.',
        foreHand:'La IA está a punto de repetirlo. Más rápido, y con más gente.',
        useTitle:'Úsalo en tu trabajo', useSub:'Elige a qué te dedicas. Mira las unidades que más te sirven.',
        useNone:'Todavía no hay unidades para esto. Empieza por los fundamentos.',
        progTitle:'Tu avance', progSub:'Pruebas, no puntos.',
        progEmpty:'Aún nada. Termina una unidad y aparecerá aquí.',
        progUnits:'unidades hechas', progCan:'Lo que ya puedes hacer', progSheet:'Tu hoja de apuntes',
        progReview:'Vale la pena repasar', progReviewSub:'Unidades que fallaste en el primer intento.',
        progExport:'Exportar en una página', reset:'Borrar mi avance' }
};

function head({ title, lang, prefix, desc }) {
  return `<!DOCTYPE html>
<html lang="${lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<meta name="theme-color" content="#F1EEE7">
<title>${esc(title)}</title>
<meta name="description" content="${attr(desc)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght,SOFT,WONK@0,9..144,300..700,0..100,0..1;1,9..144,300..700,0..100,0..1&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="${prefix}assets/studio.css">
</head>`;
}

function chrome({ lang, prefix, t, current, altHref }) {
  const tabs = [
    ['◧', t.home,  `${prefix}`,            'home'],
    ['✦', t.use,   `${prefix}use-it/`,     'use'],
    ['A', t.gloss, `${prefix}glossary/`,   'gloss'],
    ['◔', t.prog,  `${prefix}progress/`,   'prog']
  ].map(([ic, label, href, key]) =>
    `<a href="${href}"${key === current ? ' aria-current="page"' : ''}>` +
    `<span class="ic" aria-hidden="true">${ic}</span>${esc(label)}</a>`).join('');

  return {
    top: `<a class="skip" href="#main">${esc(t.skip)}</a>
<div id="live" class="sr-only" role="status" aria-live="polite"></div>
<header class="top">
  <a class="wordmark" href="${prefix}">Me, Myself <em>&amp;</em> AI</a>
  <a class="label" href="${altHref}" hreflang="${lang === 'en' ? 'es' : 'en'}">${lang === 'en' ? 'ES' : 'EN'}</a>
</header>`,
    tabs: `<nav class="tabs" aria-label="${esc(t.home)}">${tabs}</nav>`
  };
}

/* ---- legacy scan -------------------------------------------------------
   Read titles straight off the old files. As each module is converted and
   deleted, it disappears from home without anyone editing a list.
   ------------------------------------------------------------------- */
export const RETIRED = { 'module-1.html': 'answer-died' };

function legacyModules(root, lang) {
  const dir = lang === 'en' ? root : join(root, 'es');
  if (!existsSync(dir)) return [];
  return readdirSync(dir)
    .filter(f => /^module-\d+\.html$/.test(f) && !(f in RETIRED))
    .map(f => {
      const n = parseInt(f.match(/\d+/)[0], 10);
      let title = f;
      try {
        const html = readFileSync(join(dir, f), 'utf8');
        const m = html.match(/<title>(.*?)<\/title>/s);
        if (m) title = m[1].split(/,\s*Me, Myself/)[0].replace(/&amp;/g, '&').trim();
      } catch (e) { /* keep the filename */ }
      return { n, file: f, title };
    })
    .sort((a, b) => a.n - b.n);
}

/* ---- home -------------------------------------------------------------- */

export function buildHome({ root, lang, units }) {
  const t = T[lang];
  const prefix = lang === 'en' ? '' : '../';
  const alt = lang === 'en' ? '/es/' : '/';
  const c = chrome({ lang, prefix, t, current: 'home', altHref: alt });

  const byLevel = {};
  for (const u of units) (byLevel[u.level] ??= []).push(u);
  for (const k in byLevel) byLevel[k].sort((a, b) => (a.order || 0) - (b.order || 0));

  const levels = Object.keys(byLevel).sort((a, b) => a - b).map(lv => {
    const list = byLevel[lv];
    const items = list.map(u =>
      `<li data-unit="${attr(u.id)}"><span class="box"></span>` +
      `<a class="t" href="${prefix}u/${u.id}/">${esc(u.title)}</a>` +
      `<span class="kind">${esc(u.type.replace('-', ' '))}</span>` +
      `<span class="min">${u.minutes}m</span></li>`).join('');
    return `<section class="lvl-block">
  <p class="label">${esc(LEVELS[lv]?.[lang] || `Level ${lv}`)} · ${list.length} ${esc(t.units)}</p>
  <ul class="checklist">${items}</ul>
</section>`;
  }).join('\n');

  const legacy = legacyModules(root, lang);
  const legacyBlock = legacy.length ? `
<hr class="torn">
<p class="label">${esc(t.legacy)}</p>
<p class="soft" style="font-size:.9375rem;margin-top:.4rem">${esc(t.legacySub)}</p>
<ul class="checklist legacy" style="margin-top:.8rem">
${legacy.map(m => `  <li><span class="box"></span><a class="t" href="${prefix}${m.file}">${esc(m.title)}</a></li>`).join('\n')}
</ul>` : '';

  return `${head({ title: 'Me, Myself & AI', lang, prefix, desc: t.tagline })}
<body data-page="home">
${c.top}
<main id="main" tabindex="-1" class="wrap">

  <div id="firstVisit">
    <h1>${esc(t.hero)}</h1>
    <p class="soft" style="margin-top:1rem">${esc(t.tagline)}</p>
    <div class="card taped tilt-l" style="margin-top:1.75rem">
      <p class="label red">${esc(t.start)}</p>
      <h2 style="font-size:1.4rem;margin:.5rem 0 .35rem">${esc(LEVELS[0][lang])}</h2>
      <p class="soft" style="font-size:.875rem">${esc(t.startSub)}</p>
      <a class="btn btn-red" href="${prefix}u/myth-your-job/" style="width:100%;margin-top:1rem">${esc(t.startCta)}</a>
    </div>
  </div>

  <div id="resume" hidden>
    <p class="label red">${esc(t.resume)}</p>
    <div class="card taped tilt-r" style="margin-top:.9rem">
      <h2 id="resumeTitle" style="font-size:1.4rem;margin-bottom:.35rem"></h2>
      <p class="soft" id="resumeMeta" style="font-size:.8125rem"></p>
      <a class="btn" id="resumeLink" href="#" style="width:100%;margin-top:1rem">${esc(t.cont)}</a>
    </div>
  </div>

  <hr class="torn">
  <p class="label">${esc(t.path)}</p>
  <p class="soft" id="pathCount" style="font-size:.875rem;margin-top:.3rem"></p>
${levels}
${legacyBlock}

  <hr class="torn">
  <p class="label">${esc(t.fore)}</p>
  <p class="fore-line">${esc(t.foreLine)}</p>
  <p class="soft" style="font-size:.9375rem;margin-top:.7rem">${esc(t.foreBody)}</p>
  <p class="hand" style="margin-top:.8rem">${esc(t.foreHand)} <a href="${prefix}about.html">${esc(t.read)} →</a></p>

</main>
${c.tabs}
<script src="${prefix}assets/state.js"></script>
<script src="${prefix}assets/home.js"></script>
</body>
</html>
`;
}

/* ---- glossary ---------------------------------------------------------- */

export function buildGlossary({ lang, glossary, unitsById }) {
  const t = T[lang];
  const prefix = lang === 'en' ? '../' : '../../';
  const alt = lang === 'en' ? '/es/glossary/' : '/glossary/';
  const c = chrome({ lang, prefix, t, current: 'gloss', altHref: alt });

  const entries = glossary.map(term => {
    const name = lang === 'en' ? term.term_en : (term.term_es || term.term_en);
    const plain = lang === 'en' ? term.plain_en : (term.plain_es || term.plain_en);
    const first = (term.taught_by || [])[0];
    const u = first && unitsById[first];
    const link = u
      ? `<a class="learn" href="${prefix}u/${first}/">${esc(t.learn)} · ${u.minutes} ${esc(t.min)} →</a>`
      : '';
    return `<div class="entry" id="${attr(term.id)}">
  <p class="term-name">${esc(name)}</p>
  <p class="def">${esc(plain)}</p>
  ${link}
</div>`;
  }).join('\n');

  return `${head({ title: `${t.glossTitle} · Me, Myself & AI`, lang, prefix, desc: t.glossSub })}
<body data-page="glossary">
${c.top}
<main id="main" tabindex="-1" class="wrap">
  <p class="label red">${esc(t.gloss)}</p>
  <h1>${esc(t.glossTitle)}</h1>
  <p class="soft" style="margin-top:.8rem">${esc(t.glossSub)}</p>
  <div style="margin-top:1.75rem">
${entries}
  </div>
</main>
${c.tabs}
</body>
</html>
`;
}

/* ---- Use It ------------------------------------------------------------
   Data-driven from each unit's `professions` frontmatter. No invented task
   lists: a profession shows the units actually tagged for it, so the page
   can never claim content that doesn't exist.
   ------------------------------------------------------------------- */

export function buildUseIt({ lang, units }) {
  const t = T[lang];
  const prefix = lang === 'en' ? '../' : '../../';
  const alt = lang === 'en' ? '/es/use-it/' : '/use-it/';
  const c = chrome({ lang, prefix, t, current: 'use', altHref: alt });

  const byProf = {};
  for (const u of units) for (const p of (u.professions || [])) (byProf[p] ??= []).push(u);

  const order = Object.keys(PROFESSIONS).filter(p => byProf[p]);
  const chips = order.map((p, i) =>
    `<button class="prof-chip${i === 0 ? ' on' : ''}" data-prof="${attr(p)}" aria-pressed="${i === 0}">` +
    `${esc(PROFESSIONS[p][lang])}</button>`).join('');

  const panels = order.map((p, i) => {
    const list = (byProf[p] || []).sort((a, b) =>
      (a.level - b.level) || (a.order - b.order));
    const items = list.map(u =>
      `<li><span class="box"></span>` +
      `<a class="t" href="${prefix}u/${u.id}/">${esc(u.capability || u.title)}</a>` +
      `<span class="kind">${esc((u.type || '').replace('-', ' '))}</span>` +
      `<span class="min">${u.minutes}m</span></li>`).join('');
    return `<div class="prof-panel" data-panel="${attr(p)}"${i === 0 ? '' : ' hidden'}>
  <ul class="checklist">${items || `<li class="soft">${esc(t.useNone)}</li>`}</ul>
</div>`;
  }).join('\n');

  return `${head({ title: `${t.useTitle} · Me, Myself & AI`, lang, prefix, desc: t.useSub })}
<body data-page="use-it">
${c.top}
<main id="main" tabindex="-1" class="wrap">
  <p class="label red">${esc(t.use)}</p>
  <h1>${esc(t.useTitle)}</h1>
  <p class="soft" style="margin-top:.8rem">${esc(t.useSub)}</p>
  <div class="chips" role="group" aria-label="${esc(t.use)}" style="margin-top:1.5rem">${chips}</div>
  <div style="margin-top:1.75rem">
${panels}
  </div>
</main>
${c.tabs}
<script src="${prefix}assets/use-it.js"></script>
</body>
</html>
`;
}

/* ---- Progress ----------------------------------------------------------
   Static shell, filled client-side from the mmai.v2 store by progress.js.
   Nothing here is server-known because progress lives only in the browser.
   ------------------------------------------------------------------- */

export function buildProgress({ lang, units }) {
  const t = T[lang];
  const prefix = lang === 'en' ? '../' : '../../';
  const alt = lang === 'en' ? '/es/progress/' : '/progress/';
  const c = chrome({ lang, prefix, t, current: 'prog', altHref: alt });

  // catalogue the JS needs: id -> capability / takeaway / title / url
  const catalog = {};
  for (const u of units) catalog[u.id] = {
    title: u.title, capability: u.capability || null,
    takeaway: u.takeaway || null, url: `${prefix}u/${u.id}/`
  };

  return `${head({ title: `${t.progTitle} · Me, Myself & AI`, lang, prefix, desc: t.progSub })}
<body data-page="progress">
${c.top}
<main id="main" tabindex="-1" class="wrap">
  <p class="label red">${esc(t.prog)}</p>
  <h1>${esc(t.progTitle)}</h1>
  <p class="soft" style="margin-top:.8rem">${esc(t.progSub)}</p>

  <p id="progEmpty" class="hand" style="margin-top:1.5rem">${esc(t.progEmpty)}</p>

  <div id="progStats" hidden>
    <p class="fore-line" style="margin-top:1.5rem"><span id="progDone">0</span> / ${units.length}
      <span class="soft" style="font-size:1rem;font-family:var(--sans);font-weight:400"> ${esc(t.progUnits)}</span></p>

    <div id="progCanWrap" hidden>
      <hr class="torn"><p class="label">${esc(t.progCan)}</p>
      <ul class="checklist" id="progCan" style="margin-top:.6rem"></ul>
    </div>

    <div id="progSheetWrap" hidden>
      <hr class="torn"><p class="label">${esc(t.progSheet)}</p>
      <div id="progSheet" style="margin-top:.8rem"></div>
      <button class="btn btn-2" id="progExport" style="margin-top:.9rem">${esc(t.progExport)}</button>
    </div>

    <div id="progReviewWrap" hidden>
      <hr class="torn"><p class="label">${esc(t.progReview)}</p>
      <p class="soft" style="font-size:.9375rem;margin-top:.3rem">${esc(t.progReviewSub)}</p>
      <ul class="checklist" id="progReview" style="margin-top:.6rem"></ul>
    </div>

    <hr class="torn">
    <button class="btn btn-2" id="progReset" style="font-size:.8125rem">${esc(t.reset)}</button>
  </div>
</main>
${c.tabs}
<script>window.MMAI_CATALOG=${JSON.stringify(catalog)};</script>
<script src="${prefix}assets/state.js"></script>
<script src="${prefix}assets/progress.js"></script>
</body>
</html>
`;
}
