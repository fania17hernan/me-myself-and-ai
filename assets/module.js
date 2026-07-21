/* =============================================================
   Me, Myself & AI  ·  module.js
   PHASE 0: one generic runner, replacing 26 near-identical copies.

   The 26 inline scripts were ~90% the same. They could not be
   extracted by copy-paste because three things were baked into
   the JS: the module id, the level name, and the quiz explanation
   text. Those now live in the markup, which is both more
   accessible (real text in the DOM) and far easier to translate,
   since /es no longer needs a forked script.

   Markup contract
   ---------------
   <body data-lesson="module-1" data-level="Start Here">
   <div class="check" data-q="0" data-answer="1">
     <button class="qopt">…</button> ×N
     <p class="explain" data-good="…" data-bad="…" hidden></p>
   </div>

   UI strings come from data-i18n-* on <body>, so Spanish needs no
   separate build.
   ============================================================= */

(function () {
  'use strict';

  var body = document.body;
  var LESSON = body.dataset.lesson;
  if (!LESSON) return;

  var State = (window.MMAI && window.MMAI.state) || null;

  var T = {
    step:     body.dataset.i18nStep     || 'Step',
    of:       body.dataset.i18nOf       || 'of',
    complete: body.dataset.i18nComplete || 'Complete',
    start:    body.dataset.i18nStart    || 'Start the module',
    cont:     body.dataset.i18nCont     || 'Continue',
    finish:   body.dataset.i18nFinish   || 'Finish',
    level:    body.dataset.level        || ''
  };

  var screens  = [].slice.call(document.querySelectorAll('.screen'));
  if (!screens.length) return;

  var fill     = document.getElementById('fill');
  var stepLbl  = document.getElementById('stepLabel');
  var nextBtn  = document.getElementById('nextBtn');
  var backBtn  = document.getElementById('backBtn');
  var navbar   = document.querySelector('.navbar');
  var doneNav  = document.getElementById('doneNav');
  var live     = document.getElementById('live');

  var checks   = [].slice.call(document.querySelectorAll('[data-q]'));
  var QUIZ     = screens.length - 2;          // quiz sits before the done screen
  var DONE     = screens.length - 1;

  var i = 0;
  var answers = {};

  /* Resume, but never drop the learner straight onto the done screen. */
  if (State) {
    var saved = State.lesson(LESSON);
    if (saved && saved.pos > 0 && saved.pos < DONE) i = saved.pos;
  }

  function quizDone() { return Object.keys(answers).length === checks.length; }

  function score() {
    var n = 0;
    for (var k in answers) if (answers[k]) n++;
    return n;
  }

  function asArray() {
    return checks.map(function (_, n) { return answers[n] ? 1 : 0; });
  }

  function render(announce) {
    screens.forEach(function (s, n) {
      var on = (n === i);
      s.classList.toggle('on', on);
      /* Hide inactive screens from assistive tech, not just visually. */
      if (on) { s.removeAttribute('aria-hidden'); }
      else    { s.setAttribute('aria-hidden', 'true'); }
    });

    var pct = Math.round(i / DONE * 100);
    if (fill) {
      fill.style.width = pct + '%';
      var bar = fill.parentNode;
      if (bar) {
        bar.setAttribute('role', 'progressbar');
        bar.setAttribute('aria-valuenow', String(pct));
        bar.setAttribute('aria-valuemin', '0');
        bar.setAttribute('aria-valuemax', '100');
      }
    }

    var label = (i === 0) ? T.level
              : (i === DONE) ? T.complete
              : T.step + ' ' + i + ' ' + T.of + ' ' + (DONE - 1);
    if (stepLbl) stepLbl.textContent = label;

    if (backBtn) backBtn.style.visibility = (i === 0) ? 'hidden' : 'visible';

    if (nextBtn) {
      nextBtn.textContent = (i === 0) ? T.start : (i === QUIZ) ? T.finish : T.cont;
      nextBtn.disabled = (i === QUIZ) ? !quizDone() : false;
      /* disabled buttons are unreachable by keyboard, so explain why. */
      nextBtn.setAttribute('aria-disabled', String(nextBtn.disabled));
    }

    if (navbar)  navbar.style.display  = (i === DONE) ? 'none'  : '';
    if (doneNav) doneNav.style.display = (i === DONE) ? 'block' : 'none';

    if (i === DONE && State) State.complete(LESSON, asArray());
    else if (State) State.setPos(LESSON, i);

    /* Move focus to the new screen's heading rather than scrolling
       silently, which strands screen reader and keyboard users. */
    if (announce) {
      var h = screens[i].querySelector('h1, h2, h3');
      if (h) {
        h.setAttribute('tabindex', '-1');
        h.focus({ preventScroll: true });
      }
      if (live) live.textContent = label;
    }
    window.scrollTo({ top: 0 });
  }

  if (nextBtn) nextBtn.addEventListener('click', function () {
    if (i < DONE) { i++; render(true); }
  });
  if (backBtn) backBtn.addEventListener('click', function () {
    if (i > 0) { i--; render(true); }
  });

  checks.forEach(function (card, qi) {
    var correct = parseInt(card.dataset.answer, 10);
    var opts = [].slice.call(card.querySelectorAll('.qopt'));
    var ex   = card.querySelector('.explain');

    opts.forEach(function (opt, n) {
      opt.addEventListener('click', function () {
        if (qi in answers) return;
        var ok = (n === correct);
        answers[qi] = ok;

        opts.forEach(function (o) {
          o.disabled = true;
          o.setAttribute('aria-disabled', 'true');
        });
        opt.classList.add(ok ? 'ok' : 'no');
        if (!ok) opts[correct].classList.add('ok');

        if (ex) {
          ex.textContent = ok ? ex.dataset.good : ex.dataset.bad;
          ex.className = 'explain show ' + (ok ? 'good' : 'bad');
          ex.hidden = false;
          ex.setAttribute('role', 'status');
        }
        if (quizDone() && nextBtn) {
          nextBtn.disabled = false;
          nextBtn.setAttribute('aria-disabled', 'false');
        }
      });
    });
  });

  /* Done screen copy. Strings come from data-* so /es needs no fork. */
  function paintDone() {
    var s = score(), total = checks.length, perfect = (s === total);

    var title = document.getElementById('doneTitle');
    if (title) {
      var t = perfect ? body.dataset.donePerfect : body.dataset.doneOk;
      if (t) title.textContent = t;
    }

    var el = document.getElementById('doneScore');
    if (el) {
      var tpl  = body.dataset.scoreTpl || '';
      var tail = perfect ? (body.dataset.scorePerfect || '')
                         : (body.dataset.scorePartial || '');
      if (tpl) el.textContent = tpl.replace('{s}', s).replace('{n}', total) + tail;
    }
  }

  var _render = render;
  render = function (announce) {
    _render(announce);
    if (i === DONE) paintDone();
  };

  render(false);
})();
