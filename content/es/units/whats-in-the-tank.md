---
id: whats-in-the-tank
title: "Qué hay dentro del tanque"
type: concept
level: 1
topic: tokens-and-limits
order: 3
minutes: 3
teaches: [token, context-window]
professions: [manager, accountant, recruiter]
volatility: slow
tool_scope: agnostic
verified: 2026-07-20
capability: "Anticipar qué peticiones van a salir caras antes de enviarlas."
takeaway: "Cuentan las dos: la entrada y la salida."
---

Un [[token]] es la unidad que la IA lee y escribe en realidad. Más o menos tres cuartas partes de una
palabra, así que 100 palabras son unos 130 tokens. Para entendernos: ==palabras y tokens son casi lo
mismo==.

## Las dos direcciones queman gasolina

Esto sorprende a todo el mundo: no es solo lo que escribes. La entrada, o sea tu mensaje más todo lo
anterior de la conversación, y la salida, la respuesta de la IA, cuentan las dos. Una pregunta corta
que necesita una respuesta larga también quema bastante.

## Las conversaciones largas se vuelven lentas y caras

Cada vez que envías un mensaje, la IA vuelve a leer toda la conversación hasta ese punto. El mensaje
40 de un chat largo quema mucho más que el mensaje 2. Vas cargando con todo el historial del viaje.

::check answer=1
¿Qué quema combustible?
- Solo lo que escribes
- Las dos cosas, la entrada y la salida
- Solo lo que responde la IA
::good Correcto, las dos direcciones queman. ¿Pregunta corta, respuesta larga? Sale igual de caro.
::bad Casi. Cuentan las dos, por eso vacían el tanque tanto las preguntas largas como las respuestas largas.
::

::say-it-back
"Cuentan las dos: la entrada y la salida."
::
