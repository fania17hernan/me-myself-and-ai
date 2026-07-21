/* =============================================================
   Me, Myself & AI  ·  assets/unit.js
   Runtime for a generated unit page.

   Replaces module.js. Units are one scroll, not an 8-screen wizard,
   so this is much smaller: progress on scroll, one recall check,
   pinning a takeaway, and writing to the mmai.v2 store from Phase 0.
   ============================================================= */

(function () {
  'use strict';

  var body = document.body;
  var ID = body.dataset.lesson;
  if (!ID) return;

  var State = (window.MMAI && window.MMAI.state) || null;
  var live = document.getElementById('live');

  /* ---- progress: how far down the unit you are ------------------------ */
  var fill = document.querySelector('.prog i');
  var main = document.getElementById('main');
  var ticking = false;

  function progress() {
    if (!fill || !main) return;
    var h = main.scrollHeight - window.innerHeight;
    var pct = h > 0 ? Math.min(100, Math.max(0, (window.scrollY / h) * 100)) : 100;
    fill.style.width = pct.toFixed(1) + '%';
    var bar = fill.parentNode;
    bar.setAttribute('role', 'progressbar');
    bar.setAttribute('aria-valuenow', Math.round(pct));
    bar.setAttribute('aria-valuemin', '0');
    bar.setAttribute('aria-valuemax', '100');

    /* A unit with no check completes on reaching the end. A unit with a
       check completes when the check is answered, never merely by
       scrolling, because the whole point is proof over attendance. */
    if (pct > 92 && !checks.length) complete(null);
  }
  window.addEventListener('scroll', function () {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(function () { progress(); ticking = false; });
  }, { passive: true });

  /* ---- completion ----------------------------------------------------- */
  var done = false;
  function complete(results) {
    if (done || !State) return;
    done = true;
    State.complete(ID, results);
    if (live) live.textContent = 'Unit complete.';
  }

  /* ---- recall check --------------------------------------------------- */
  var checks = [].slice.call(document.querySelectorAll('[data-q]'));
  var answers = {};

  checks.forEach(function (card, qi) {
    var correct = parseInt(card.dataset.answer, 10);
    var opts = [].slice.call(card.querySelectorAll('.opt'));
    var ex = card.querySelector('.explain');

    opts.forEach(function (opt, n) {
      opt.setAttribute('aria-disabled', 'false');
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
          ex.hidden = false;
          ex.setAttribute('role', 'status');
        }
        if (Object.keys(answers).length === checks.length) {
          complete(checks.map(function (_, i) { return answers[i] ? 1 : 0; }));
        }
      });
    });
  });

  /* ---- pinning -------------------------------------------------------- */
  [].slice.call(document.querySelectorAll('[data-pin]')).forEach(function (btn) {
    if (!State) { btn.hidden = true; return; }

    function paint() {
      var on = State.isSaved(ID);
      btn.textContent = on ? '✓ Pinned' : '＋ Pin it';
      btn.setAttribute('aria-pressed', String(on));
    }
    paint();

    btn.addEventListener('click', function () {
      if (State.isSaved(ID)) State.unsave(ID);
      else State.save(ID);
      paint();
      if (live) live.textContent = State.isSaved(ID)
        ? 'Pinned to your bench.' : 'Removed from your bench.';
    });
  });

  progress();
})();
