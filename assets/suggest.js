/* =============================================================
   Me, Myself & AI  ·  suggest.js
   PHASE 1: the topic-suggestion form, extracted.

   This script was also duplicated inline in every lesson file,
   with the endpoint and publishable key repeated each time.
   Now it binds to any <form data-suggest> and reads what it
   needs from data-* attributes, so /es shares the same code.

   The key is a Supabase *publishable* key, which is safe in the
   client by design. It only permits inserts into topic_suggestions.
   ============================================================= */

(function () {
  'use strict';

  var URL = 'https://pdbqrjqlwqjqzefmmlhd.supabase.co/rest/v1/topic_suggestions';
  var KEY = 'sb_publishable_IdA-Ju152TgBx-wEGMd0Yg_iV7_wvkO';

  var COPY = {
    en: { ok: 'Got it, thank you. Your idea is in.',
          err: "Hmm, that didn't send. Mind trying again in a moment?" },
    es: { ok: 'Listo, gracias. Tu idea ya quedó registrada.',
          err: 'No se pudo enviar. ¿Lo intentas de nuevo en un momento?' }
  };

  [].slice.call(document.querySelectorAll('form[data-suggest]')).forEach(function (form) {
    var lang = form.dataset.lang || document.documentElement.lang || 'en';
    var copy = COPY[lang] || COPY.en;

    var field = function (n) { return form.querySelector('[data-field="' + n + '"]'); };
    var text = field('text'), email = field('email'), hp = field('hp'),
        submit = field('submit'), msg = field('msg');

    form.addEventListener('submit', function (ev) {
      ev.preventDefault();
      if (hp && hp.value) return;                       // honeypot
      var body = (text.value || '').trim();
      if (!body) { text.focus(); return; }

      submit.disabled = true;
      if (msg) msg.textContent = '';

      fetch(URL, {
        method: 'POST',
        headers: {
          'apikey': KEY,
          'Authorization': 'Bearer ' + KEY,
          'Content-Type': 'application/json',
          'Prefer': 'return=minimal'
        },
        body: JSON.stringify({
          suggestion: body,
          email: (email && email.value.trim()) || null,
          lang: lang,
          source: form.dataset.source || 'unknown'
        })
      }).then(function (r) {
        if (!r.ok) throw new Error(r.status);
        var p = document.createElement('p');
        p.className = 'sg-ok';
        p.setAttribute('role', 'status');
        p.textContent = copy.ok;
        form.replaceWith(p);
        p.setAttribute('tabindex', '-1');
        p.focus();                                      // move focus, don't strand
      }).catch(function () {
        if (msg) msg.textContent = copy.err;
        submit.disabled = false;
      });
    });
  });
})();
