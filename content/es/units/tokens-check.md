---
id: tokens-check
title: "Comprobación rápida: el tanque"
type: check
level: 1
topic: tokens-and-limits
order: 5
minutes: 2
teaches: [token, rate-limit, truncation]
professions: [manager]
volatility: evergreen
tool_scope: agnostic
verified: 2026-07-20
capability: "Diagnosticar una respuesta detenida en menos de diez segundos."
---

Sin calificaciones. Solo para confirmar que quedó claro.

::check answer=0
La respuesta de tu IA se detiene a media frase. ¿Qué pasó probablemente?
- Se quedó sin tokens, el tanque llegó a cero
- Se confundió con tu pregunta
- Se cayó la conexión a internet
::good Exacto. Se acabó la gasolina, aunque fuera a media frase. Responde "continúa" y vuelve a llenar el tanque.
::bad No del todo. Se quedó sin tokens a media respuesta. La solución: responde "por favor continúa".
::
