# QA — TikTok Pixel D9GISS3C77U6Q0JCP34G
**Fecha:** 2026-07-22
**PRs:** #8 (instalación inicial) → #9 (corrección Pixel ID)
**Commits main:** ecc3cbbe (pixel) → 7e5b769 (QA doc) → 8d586b1 (fix ID)

---

## 1. DEPLOY REAL

| Check | Resultado |
|---|---|
| PR #8 mergeado | ✅ `ecc3cbbe` — 2026-07-22T20:58:16Z (ID incorrecto, ver PR #9) |
| PR #9 mergeado | ✅ `8d586b1` — 2026-07-22T21:09:58Z (corrección Pixel ID) |
| Pixel ID correcto en producción | ✅ CONFIRMADO — curl + network request |

```
$ until curl -sL https://www.certimotors.com | grep -q "D9GISS3C77U6Q0JCP34G"; do sleep 5; done && echo "LIVE"
LIVE
```

---

## 2. ESTRUCTURA DEL SNIPPET — verificación de aislamiento

```html
<!-- Meta Pixel (existente, sin cambios) -->
<script>
  ...
  fbq('init', '26679746048367896');
  fbq('track', 'PageView');
</script>
<noscript>...</noscript>

<!-- TikTok Pixel (nuevo — script separado, nunca mezclado) -->
<script>
  !function (w, d, t) {
    ...
    ttq.load('D9GISS3C77U6Q0JCP34G');
    ttq.page();
  }(window, document, 'ttq');
</script>
</head>
```

**Veredicto:** TikTok Pixel en su propio `<script>`, después de Meta noscript, antes de `</head>`. GA4 y Meta sin modificar.

---

## 3. EVENTO PAGEVIEW — prueba de red en producción

Origen: `https://www.certimotors.com` (carga normal, sin params)

| Request | URL | Método | Status |
|---|---|---|---|
| Pixel SDK | `analytics.tiktok.com/i18n/pixel/events.js?sdkid=D9GISS3C77U6Q0JCP34G` | GET | 200 ✅ |
| PageView | `analytics.tiktok.com/api/v2/pixel` | POST | 200 ✅ |
| Pixel act | `analytics.tiktok.com/api/v2/pixel/act` | POST | 200 ✅ |

SDK cargó con el Pixel ID correcto. `ttq.page()` disparó en carga normal.

---

## 4. EVENTO PURCHASE — prueba E2E de punta a punta

### Setup
```js
// En DevTools Console sobre https://www.certimotors.com (mismo origen que success_url)
sessionStorage.setItem('cm_servicio', 'FULL');
// → retorna 'FULL' ✅ (confirmado en consola)
```

### Navegación a URL de éxito
```
https://www.certimotors.com/?paid=1&orden=TEST123
```
*(Simula el redirect real de Recurrente: `success_url: \`${CONFIG.WEB_URL}?paid=1&orden=${orden.id}\``)*

### Evidencia de red
| Request | URL | Método | Status | Nota |
|---|---|---|---|---|
| PageView | `analytics.tiktok.com/api/v2/pixel` | POST | 200 ✅ | Carga de página |
| **Purchase** | `analytics.tiktok.com/api/v2/pixel` | POST | 200 ✅ | **Segundo POST — apareció solo después de navegar a `?paid=1`** |
| Pixel act | `analytics.tiktok.com/api/v2/pixel/act` | POST | 200 ✅ | |

Total en success URL: **2 POSTs a `/api/v2/pixel`** (1 PageView + 1 Purchase) vs 1 en carga normal.

### Evidencia del guard y pantalla
```js
paidVisible: true          // <section id="paid-screen"> visible ✅
guardFired: true           // params.get('paid') === '1' ✅
```

### Advertencia esperada de TikTok (no es error)
```
[TikTok Pixel] - Missing email and phone number
Issue: Email and phone number info isn't being received.
This information is required for Complete Payment events.
```
**Esta advertencia confirma que el evento Purchase SÍ llegó al SDK** — TikTok solo evalúa los parámetros de Enhanced Matching si recibió el evento. No es un error de implementación; es una sugerencia de mejora para mejorar atribución con datos del usuario (email/phone hashed). El evento se registra correctamente sin ellos.

### Valores enviados
| Parámetro | Valor | Fuente |
|---|---|---|
| `content_id` | `FULL` | `sessionStorage.getItem('cm_servicio')` |
| `content_type` | `product` | hardcoded |
| `value` | `800` | lookup `{ SCANNER:300, ESTANDAR:550, FULL:800 }['FULL']` |
| `currency` | `GTQ` | hardcoded |
| `quantity` | `1` | hardcoded |

---

## 5. GUARD CONDITION — por qué es `?paid=1` y no `?success=true`

Verificado directo en el backend (`/Users/rodrigogalindo/CERTIMOTORS-repo/src/index.js` línea 377):

```js
success_url: `${CONFIG.WEB_URL}?paid=1&orden=${orden.id}`,
cancel_url:  `${CONFIG.WEB_URL}/#servicios`,
```

Recurrente redirige a `?paid=1`, no a `?success=true`. El guard en el código es correcto. Cambiar a `?success=true` rompería el tracking — ese parámetro nunca llega.

---

## 6. NOMBRE DEL EVENTO — Purchase vs CompletePayment

Verificado en [TikTok's Updated Standard Events](https://ads.tiktok.com/help/article/how-to-adopt-tiktoks-updated-standard-events):

> `CompletePayment` ha sido renombrado a `Purchase`. Para nuevas implementaciones en 2026, TikTok recomienda `Purchase`. `CompletePayment` sigue siendo funcional (auto-convertido en backend de TikTok) pero es el nombre legacy. El SDK hasta menciona internamente "Complete Payment events" en sus logs, pero el evento a enviar es `Purchase`.

**Implementación usa `Purchase` — correcto para 2026.**

---

## 7. REGRESIÓN — GA4 y Meta intactos

| Pixel/Tag | Verificación |
|---|---|
| GA4 `G-17RQ4B76BR` | Bloque sin modificar — líneas 822–829 intactas |
| GA4 `G-53TM6JHBXW` | Mismo bloque, sin cambios |
| Meta Pixel `26679746048367896` | Bloque sin modificar — líneas 831–842 intactas |
| TikTok en `<script>` separado | Líneas 843–858, nunca mezclado |

---

## 8. SUPABASE — nota sobre "orden TEST123"

**No existe ninguna fila en `ordenes` con id=TEST123.** El id es una columna UUID; `TEST123` no es un UUID válido y nunca se insertó.

La URL `?paid=1&orden=TEST123` solo simula el redirect de Recurrente. El parámetro `orden` se lee únicamente en el frontend para pasarlo como `orden_id` al evento GA4 — no hay ninguna operación de base de datos en la página de confirmación.

**Órdenes de prueba encontradas en Supabase** (todas `pago_status: PENDIENTE`, no mezclan con reales):
- `test@certimotors.com` — 2 órdenes (Jul 15–16)
- `qa+*@certimotors.test` — 8 órdenes (Jul 13)

Estas son de sesiones QA previas. Si querés limpiarlas, confirmame y las borro. No lo hago sin aprobación explícita porque podrían ser referencia para debugging futuro.

---

## 9. OBJETIVO DE CAMPAÑA TIKTOK ADS — paso manual requerido

**No puedo verificar ni cambiar el objetivo del ad set desde código** — requiere acceso a TikTok Ads Manager.

**Acción requerida por Rodrigo:**
1. Ir a [TikTok Ads Manager](https://ads.tiktok.com) → tu cuenta
2. Campaña activa → Ad Set → editar
3. Verificar el objetivo de optimización del ad set:
   - Si está en **"Conversión" / "Complete Payment"**: cambiarlo a **"Alcance" o "Tráfico"** por ahora
   - Razón: TikTok necesita ~50 eventos Purchase/semana por ad group para salir de la fase de aprendizaje y optimizar correctamente. Con Q25/día y siendo un pixel nuevo, no vas a alcanzar ese volumen esta semana.
   - Con Alcance o Tráfico acumulás datos reales de Purchase. Cuando llegues a ~50/semana, cambiás el objetivo a Conversión.
4. Confirmar el cambio y comunicarme el resultado.

---

## 10. RESUMEN DE ESTADO

| Punto | Estado |
|---|---|
| PR #8 mergeado a main | ✅ `ecc3cbbe` — 2026-07-22T20:58:16Z (ID incorrecto) |
| PR #9 mergeado a main | ✅ `8d586b1` — 2026-07-22T21:09:58Z (ID correcto) |
| Pixel `D9GISS3C77U6Q0JCP34G` en producción | ✅ Confirmado (curl + SDK network request) |
| PageView en carga normal | ✅ `/api/v2/pixel` POST 200 |
| Purchase en `?paid=1` | ✅ Segundo `/api/v2/pixel` POST 200 |
| Guard `?paid=1` verificado vs backend | ✅ Línea 377 `CERTIMOTORS-repo/src/index.js` |
| Evento `Purchase` (no legacy `CompletePayment`) | ✅ Nombre correcto para 2026 |
| GA4 sin regresión | ✅ |
| Meta Pixel sin regresión | ✅ |
| Orden TEST123 en Supabase | ✅ No existe — nunca se creó (ver §8) |
| Objetivo campaña TikTok Ads | ⏳ Pendiente — paso manual de Rodrigo (ver §9) |
| Prueba con TikTok Events Manager (Test Events) | ⏳ Pendiente — requiere acceso manual de Rodrigo |
