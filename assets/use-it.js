/* =============================================================
   Me, Myself & AI  ·  assets/use-it.js
   Profession chips switch which unit list is shown. Pure DOM, no
   state, works with JS off (first profession's panel is visible by
   default and all panels are in the DOM).

   The chosen profession is mirrored into the URL hash so a view can
   be linked to directly, e.g. /use-it/#small-business-owner. That
   makes each profession track shareable, which is the whole point
   of the tab. Without it every link has to say "go here, then tap
   that", and most people never take the second step.
   ============================================================= */

(function () {
  'use strict';
  var chips = [].slice.call(document.querySelectorAll('.prof-chip'));
  var panels = [].slice.call(document.querySelectorAll('.prof-panel'));
  if (!chips.length) return;

  var group = document.querySelector('.chips');
  var live = document.getElementById('live');
  var countLabel = (group && group.dataset.countLabel) || '';

  function chipFor(prof) {
    for (var i = 0; i < chips.length; i++) {
      if (chips[i].dataset.prof === prof) return chips[i];
    }
    return null;
  }

  /* announce:  false on first paint, true on user action. We only speak
     after a deliberate switch, otherwise a screen reader hears the panel
     name the moment the page settles, competing with the heading. */
  function show(chip, announce) {
    var prof = chip.dataset.prof;

    chips.forEach(function (c) {
      var on = (c === chip);
      c.classList.toggle('on', on);
      c.setAttribute('aria-pressed', String(on));
    });

    var shown = null;
    panels.forEach(function (p) {
      var on = (p.dataset.panel === prof);
      p.hidden = !on;
      if (on) shown = p;
    });

    if (announce && live) {
      var n = shown ? shown.querySelectorAll('.checklist a.t').length : 0;
      live.textContent = chip.textContent.trim() + (n ? ' — ' + n + ' ' + countLabel : '');
    }
  }

  chips.forEach(function (chip) {
    chip.addEventListener('click', function () {
      show(chip, true);
      /* replaceState, not a hash assignment: setting location.hash would
         jump the page and stack a history entry per chip press. */
      if (window.history && history.replaceState) {
        history.replaceState(null, '', '#' + chip.dataset.prof);
      }
    });
  });

  /* Deep link on arrival, and again if the hash changes under us
     (someone edits the URL, or follows a second link to the same page). */
  function fromHash(announce) {
    var prof = decodeURIComponent((location.hash || '').replace(/^#/, ''));
    if (!prof) return;
    var chip = chipFor(prof);
    if (chip) show(chip, announce);
  }

  fromHash(false);
  window.addEventListener('hashchange', function () { fromHash(true); });
})();
