---
id: the-waiter
title: "Las API son el mesero"
type: analogy
level: 4
topic: apis
order: 1
minutes: 2
teaches: [api]
professions: [manager, small-business-owner, accountant, other]
prereqs: [dining-room-and-kitchen]
volatility: slow
tool_scope: agnostic
verified: 2026-07-25
capability: "Explicar, en términos sencillos, cómo una app obtiene datos o acciones de otra."
takeaway: "Una API es el mesero: pides del menú, lleva la orden a la cocina y regresa con lo que pediste."
---

::analogy
Una API es el mesero entre el comedor y la cocina.
::

Ahora que la app es un restaurante, ¿cómo llega tu orden a la cocina? Un mesero. Una [[api]] es ese
mesero: toma tu pedido de un menú fijo, lo lleva a la cocina y regresa con justo lo que pediste. Nunca
entras a la cocina, y no hace falta.

::figure id=the-waiter label="Fig. 4 — El mesero" caption="Pides del menú. Trae el pedido. La cocina se mantiene privada."

El menú fijo importa. Puedes pedir lo que está en la lista, de la forma que el menú permite, no
"cualquier cosa". Por eso las apps se conectan con API: es un mostrador controlado, una app pidiéndole a
otra algo específico, sin que ninguna se meta en la cocina de la otra.

::note
Cuando dos herramientas "se integran", suele ser así. Una es el cliente que pide, la otra es la cocina que prepara, y la API es el mesero en medio.
::

::say-it-back
"Una API es el mesero: pides del menú, lo trae, y nunca entras a la cocina."
::
