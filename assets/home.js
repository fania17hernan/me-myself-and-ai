/* =============================================================
   Me, Myself & AI  ·  assets/home.js

   The path is rendered at build time. This marks what's done from
   the mmai.v2 store and lifts the next unit into a resume card, so a
   returning learner is one tap from content and never has to ask
   "where was I".

   Degrades to the first-visit view when there's no state, which is
   also what someone with storage disabled sees. That's correct: the
   course must work without persistence.
   ============================================================= */

(function () {
  'use strict';

  var State = (window.MMAI && window.MMAI.state) || null;
  if (!State) return;

  var items = [].slice.call(document.querySelectorAll('[data-unit]'));
  if (!items.length) return;

  var doneCount = 0, next = null;

  items.forEach(function (li) {
    var id = li.dataset.unit;
    if (State.isDone(id)) {
      li.classList.add('done');
      doneCount++;
    } else if (!next) {
      next = li;
      li.classList.add('here');
    }
  });

  var count = document.getElementById('pathCount');
  if (count) {
    count.textContent = doneCount + ' / ' + items.length;
  }

  /* Nothing started: leave the first-visit view alone. Level 0 stays
     the recommended entry point, and a returning learner is never
     pushed back into it. */
  if (doneCount === 0) return;

  var first = document.getElementById('firstVisit');
  var resume = document.getElementById('resume');
  if (!first || !resume || !next) return;

  var link = next.querySelector('a.t');
  document.getElementById('resumeTitle').textContent = link.textContent;
  document.getElementById('resumeLink').href = link.getAttribute('href');

  var kind = next.querySelector('.kind');
  var min = next.querySelector('.min');
  document.getElementById('resumeMeta').textContent =
    [kind && kind.textContent, min && min.textContent].filter(Boolean).join(' · ');

  first.hidden = true;
  resume.hidden = false;
})();
