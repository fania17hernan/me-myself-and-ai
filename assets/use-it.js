/* =============================================================
   Me, Myself & AI  ·  assets/use-it.js
   Profession chips switch which unit list is shown. Pure DOM, no
   state, works with JS off (first profession's panel is visible by
   default and all panels are in the DOM).
   ============================================================= */

(function () {
  'use strict';
  var chips = [].slice.call(document.querySelectorAll('.prof-chip'));
  var panels = [].slice.call(document.querySelectorAll('.prof-panel'));
  if (!chips.length) return;

  chips.forEach(function (chip) {
    chip.addEventListener('click', function () {
      var prof = chip.dataset.prof;
      chips.forEach(function (c) {
        var on = (c === chip);
        c.classList.toggle('on', on);
        c.setAttribute('aria-pressed', String(on));
      });
      panels.forEach(function (p) {
        p.hidden = (p.dataset.panel !== prof);
      });
    });
  });
})();
