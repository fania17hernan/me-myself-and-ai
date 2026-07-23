/* =============================================================
   Me, Myself & AI  ·  assets/progress.js
   Fills the Progress shell from the mmai.v2 store.

   Capabilities are DERIVED from completed units (never stored, so
   they can't go stale). The cheat sheet is the takeaways the learner
   pinned. "Worth another look" is units missed on the first try, read
   from the immutable firstTry field.
   ============================================================= */

(function () {
  'use strict';
  var State = (window.MMAI && window.MMAI.state) || null;
  var CAT = window.MMAI_CATALOG || {};
  if (!State) return;

  var doneIds = Object.keys(CAT).filter(function (id) { return State.isDone(id); });

  if (!doneIds.length) return;   // leave the empty-state message showing

  document.getElementById('progEmpty').hidden = true;
  document.getElementById('progStats').hidden = false;
  document.getElementById('progDone').textContent = String(doneIds.length);

  /* ---- what you can now do ---------------------------------------- */
  var can = doneIds
    .map(function (id) { return CAT[id]; })
    .filter(function (c) { return c && c.capability; });
  if (can.length) {
    document.getElementById('progCanWrap').hidden = false;
    var canUl = document.getElementById('progCan');
    can.forEach(function (c) {
      var li = document.createElement('li');
      li.innerHTML = '<span class="box done"></span>' +
        '<span class="t">' + escapeHtml(c.capability) + '</span>';
      canUl.appendChild(li);
    });
  }

  /* ---- cheat sheet: pinned takeaways ------------------------------ */
  var sheet = State.export().saved || [];
  var pinned = sheet.map(function (id) { return CAT[id]; })
    .filter(function (c) { return c && c.takeaway; });
  if (pinned.length) {
    document.getElementById('progSheetWrap').hidden = false;
    var wrap = document.getElementById('progSheet');
    pinned.forEach(function (c, i) {
      var d = document.createElement('div');
      d.className = 'card ' + (i % 2 ? 'tilt-r' : 'tilt-l');
      d.style.marginBottom = '.6rem';
      d.innerHTML = '<p class="pin-line">' + escapeHtml(c.takeaway) + '</p>';
      wrap.appendChild(d);
    });

    document.getElementById('progExport').addEventListener('click', function () {
      var lines = pinned.map(function (c) { return '• ' + c.takeaway; }).join('\n');
      var blob = new Blob(
        ['Me, Myself & AI — my cheat sheet\n\n' + lines + '\n'],
        { type: 'text/plain' });
      var a = document.createElement('a');
      a.href = URL.createObjectURL(blob);
      a.download = 'my-cheat-sheet.txt';
      a.click();
      URL.revokeObjectURL(a.href);
    });
  }

  /* ---- worth another look: firstTry misses ------------------------ */
  var review = doneIds.filter(function (id) {
    var L = State.lesson(id);
    return L && typeof L.firstTry === 'number' && L.checks &&
           L.firstTry < L.checks.length;
  });
  if (review.length) {
    document.getElementById('progReviewWrap').hidden = false;
    var revUl = document.getElementById('progReview');
    review.forEach(function (id) {
      var c = CAT[id]; if (!c) return;
      var li = document.createElement('li');
      li.innerHTML = '<span class="box"></span>' +
        '<a class="t" href="' + c.url + '">' + escapeHtml(c.title) + '</a>';
      revUl.appendChild(li);
    });
  }

  /* ---- reset ------------------------------------------------------- */
  document.getElementById('progReset').addEventListener('click', function () {
    State.reset();
    location.reload();
  });

  function escapeHtml(s) {
    return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }
})();
