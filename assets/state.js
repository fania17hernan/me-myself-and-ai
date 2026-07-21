/* =============================================================
   Me, Myself & AI  ·  state.js
   PHASE 0: one versioned store, replacing the four flat keys.

   Was:  mmai-m{id}, mmai-done-{id}, mmai-streak, mmai-last
         (a new key leaked per module, forever; quiz answers were
         computed at render and thrown away, so every badge was
         derived from "clicked next eight times")

   Now:  a single mmai.v2 object that records what the learner can
         actually do. Streak is dropped deliberately: it punishes
         the busy professional this course is written for, and a
         broken streak is a churn trigger, not a retention one.
   ============================================================= */

(function (global) {
  'use strict';

  var KEY = 'mmai.v2';
  var VERSION = 2;

  function blank() {
    return { v: VERSION, lessons: {}, saved: [], lastLesson: null, lastSeen: null };
  }

  /* localStorage throws in Safari private mode and when disabled.
     The course must stay fully usable without persistence, so every
     access is guarded and failure degrades to in-memory only. */
  var memo = null;
  var writable = (function () {
    try {
      localStorage.setItem('mmai.probe', '1');
      localStorage.removeItem('mmai.probe');
      return true;
    } catch (e) { return false; }
  })();

  function read() {
    if (memo) return memo;
    if (!writable) return (memo = blank());
    try {
      var raw = localStorage.getItem(KEY);
      if (raw) {
        var parsed = JSON.parse(raw);
        if (parsed && parsed.v === VERSION) return (memo = parsed);
      }
    } catch (e) { /* corrupt payload, fall through to migration */ }
    return (memo = migrate());
  }

  function write(s) {
    memo = s;
    if (!writable) return;
    try { localStorage.setItem(KEY, JSON.stringify(s)); } catch (e) { /* quota */ }
  }

  /* ---- Migration -------------------------------------------------------
     Existing learners have progress in their browsers. Read the old keys
     once, fold them in, then remove them. Old data has no quiz results,
     so those lessons carry done:true with checks:null, which the
     capability list must treat as "completed, not evidenced".
     -------------------------------------------------------------------- */

  function migrate() {
    var s = blank();
    if (!writable) return s;

    var legacy = [], i, k, m;
    try {
      for (i = 0; i < localStorage.length; i++) {
        k = localStorage.key(i);
        if (k && k.indexOf('mmai-') === 0) legacy.push(k);
      }
    } catch (e) { return s; }

    legacy.forEach(function (key) {
      try {
        var val = localStorage.getItem(key);

        if ((m = key.match(/^mmai-done-(.+)$/)) && val === '1') {
          var id = 'module-' + m[1];
          s.lessons[id] = s.lessons[id] || {};
          s.lessons[id].done = true;
          s.lessons[id].checks = null;      // never measured under v1
          s.lessons[id].firstTry = null;
          return;
        }

        if ((m = key.match(/^mmai-m(\d+)$/))) {
          var lid = 'module-' + m[1];
          var pos = parseInt(val, 10);
          if (pos > 0) {
            s.lessons[lid] = s.lessons[lid] || {};
            s.lessons[lid].pos = pos;
          }
          return;
        }

        if (key === 'mmai-last') s.lastSeen = val;
        /* mmai-streak is intentionally dropped, not carried forward. */
      } catch (e) { /* skip unreadable key */ }
    });

    write(s);
    legacy.forEach(function (key) {
      try { localStorage.removeItem(key); } catch (e) {}
    });
    return s;
  }

  /* ---- Public API ------------------------------------------------------ */

  var State = {

    lesson: function (id) {
      var s = read();
      return s.lessons[id] || null;
    },

    /* Resume position. Cheap, called on every screen change. */
    setPos: function (id, pos) {
      var s = read();
      s.lessons[id] = s.lessons[id] || {};
      s.lessons[id].pos = pos;
      s.lastLesson = id;
      s.lastSeen = new Date().toISOString().slice(0, 10);
      write(s);
    },

    /* checks: array of 1/0, one per question, in order.

       firstTry is written exactly once and is never overwritten. If a
       retake could raise it, the capability list quietly becomes a
       participation trophy, which is the thing we are removing. */
    complete: function (id, checks) {
      var s = read();
      var L = s.lessons[id] = s.lessons[id] || {};
      L.done = true;
      L.doneAt = new Date().toISOString().slice(0, 10);
      L.checks = checks || null;

      if (L.firstTry === undefined || L.firstTry === null) {
        L.firstTry = checks
          ? checks.reduce(function (a, b) { return a + b; }, 0)
          : null;
      }
      s.lastLesson = id;
      s.lastSeen = L.doneAt;
      write(s);
      return L;
    },

    isDone: function (id) {
      var L = State.lesson(id);
      return !!(L && L.done);
    },

    doneCount: function () {
      var s = read(), n = 0, k;
      for (k in s.lessons) if (s.lessons[k].done) n++;
      return n;
    },

    /* For the "pick up where you left off" nudge that replaces the streak. */
    resume: function () {
      var s = read();
      return s.lastLesson ? { id: s.lastLesson, pos: (s.lessons[s.lastLesson] || {}).pos || 0 } : null;
    },

    /* Takeaways starred for the cheat sheet. Phase 3 consumes these. */
    save: function (id) {
      var s = read();
      if (s.saved.indexOf(id) === -1) s.saved.push(id);
      write(s);
    },
    unsave: function (id) {
      var s = read();
      var i = s.saved.indexOf(id);
      if (i > -1) s.saved.splice(i, 1);
      write(s);
    },
    isSaved: function (id) { return read().saved.indexOf(id) > -1; },

    /* Capabilities are DERIVED, never stored. Storing them means they go
       stale the moment a lesson is edited. Cheap enough to recompute. */
    capabilities: function (catalog) {
      var s = read(), out = [];
      Object.keys(catalog || {}).forEach(function (id) {
        var L = s.lessons[id];
        if (L && L.done) {
          out.push({
            id: id,
            statement: catalog[id],
            evidenced: L.firstTry !== null && L.firstTry !== undefined
          });
        }
      });
      return out;
    },

    /* Single JSON object means export, and any future account sync,
       is a non-event. */
    export: function () { return JSON.parse(JSON.stringify(read())); },

    reset: function () {
      write(blank());
      if (writable) { try { localStorage.removeItem(KEY); } catch (e) {} }
      memo = null;
    },

    available: writable
  };

  global.MMAI = global.MMAI || {};
  global.MMAI.state = State;

})(window);
