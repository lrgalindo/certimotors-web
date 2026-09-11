# Auditoría pre-launch de CERTIMOTORS

Fecha de revisión: 11 de septiembre de 2026
Alcance: repositorio estático `CERTIMOTORS-web`, sitio público `https://certimotors.com/` y dependencias públicas enlazadas.
Arquitectura: una página HTML estática con CSS y JavaScript nativo, publicada en GitHub Pages mediante `CNAME`; no hay framework, runtime de aplicación, router, `package.json`, lockfile, build, TypeScript, linter ni suite de pruebas. El formulario usa un backend externo en Render y continúa el pago en Recurrente.

| # | Check | Initial status | Final status | Changes | Manual action |
|---|---|---|---|---|---|
| 1 | Privacy Policy | ❌ FAIL | ✅ PASS | Se creó y aprobó `/privacidad.html`, con URL estable, metadata, enlace en footer y contenido final. Se retiraron el aviso de borrador y `noindex`. | Ninguna. |
| 2 | Terms & Conditions | ❌ FAIL | ✅ PASS | Se creó y aprobó `/terminos.html`, con URL estable, metadata, enlace en footer y condiciones publicables. Se retiraron el aviso de borrador y `noindex`. | Ninguna. |
| 3 | Secrets off the frontend | ✅ PASS | ✅ PASS | Se escanearon archivos de aplicación y configuración. No se encontraron claves privadas, contraseñas, tokens, service-role keys ni credenciales de base de datos. Los IDs de analytics y la URL pública del API son configuración cliente legítima. | Ninguna por este repositorio. Mantener credenciales reales solo en el backend. |
| 4 | Force HTTPS | ✅ PASS | ✅ PASS | Se verificaron redirecciones HTTP y `www` hacia `https://certimotors.com/`; producción responde 200 y HSTS `max-age=31556952`. Canonical usa HTTPS. | Confirmar que “Enforce HTTPS” continúe activo en GitHub Pages después de cambios de DNS. |
| 5 | Cookie consent | ❌ FAIL | ✅ PASS | Google Analytics, Meta Pixel y TikTok Pixel dejaron de cargar antes del consentimiento. Se agregó aceptar, rechazar, persistencia, reapertura y revocación dentro de la sesión. | Verificar en producción, con una sesión nueva, que rechazo genere 0 requests/cookies de tracking y que aceptación active los tres proveedores. |
| 6 | Meta titles + descriptions | 🟡 PARTIAL | ✅ PASS | Home, privacidad y términos tienen títulos, descriptions y canonical coherentes. Las páginas legales aprobadas son indexables; 404 conserva `noindex`. | Ninguna. |
| 7 | Social preview image | 🟡 PARTIAL | ✅ PASS | Se conservaron OG completos y la tarjeta 1200×630 existente; se agregaron `twitter:title` y `twitter:description`. | Probar la URL publicada en los depuradores de Meta y LinkedIn para renovar caché. |
| 8 | Favicon | ❌ FAIL | ✅ PASS | Se creó `/favicon.svg` y se enlazó desde las páginas. No existe manifest/PWA, por lo que iconos de manifest y apple touch icon no aplican. | Verificar `/favicon.svg` después del despliegue. |
| 9 | Sitemap + robots.txt | ❌ FAIL | ✅ PASS | Se validó `robots.txt`; `sitemap.xml` incluye home, privacidad y términos con fecha actual. | Enviar `https://certimotors.com/sitemap.xml` a Google Search Console. |
| 10 | Alt text on images | 🟡 PARTIAL | ✅ PASS | Las vistas previas dejaron de ser fondos CSS y ahora son imágenes con alt descriptivo, dimensiones y carga diferida. El hero sigue siendo decorativo. | Ninguna. |
| 11 | Compress images | 🟡 PARTIAL | ✅ PASS | Se generaron assets verificados visualmente: hero WebP de 49 KB, preview Full WebP de 57 KB y preview básica de 79 KB derivada del PDF final. Las previews usan `loading="lazy"` y `decoding="async"`. | Ninguna. Conservar los JPG solo como respaldo compatible con el backup existente. |
| 12 | Page load speed | ❌ FAIL | ✅ PASS | Hero priorizado, previews diferidas, fuente DM Sans alojada localmente y trackers diferidos por consentimiento. Lighthouse: 60 → 97; LCP 7.1 s → 2.4 s; TBT 365 ms → 0 ms; 34 → 5 requests. | Repetir Lighthouse en la URL pública tras desplegar y revisar datos de campo cuando exista tráfico. |
| 13 | Color contrast | ❌ FAIL | ✅ PASS | Se oscureció el eyebrow dorado en fondos claros. Lighthouse accesibilidad pasó de 96 a 100 sin fallos de contraste. | Ninguna. |
| 14 | Mobile friendly | ✅ PASS | ✅ PASS | Se comprobó 320, 375, 390, 768, 1024 y 1440 px; no hubo overflow horizontal. Formulario, modal, grids, imágenes, navegación y banner permanecen dentro del viewport. | Prueba rápida en un iPhone y un Android reales antes de campañas pagadas. |
| 15 | Custom 404 | ❌ FAIL | ✅ PASS | Se creó `404.html` consistente con la marca, con explicación, regreso al home, WhatsApp y `noindex`. En producción, una ruta inexistente respondió HTTP 404 con esta página. | Ninguna. |
| 16 | Broken links | 🟡 PARTIAL | ✅ PASS | No quedan referencias locales ni anchors rotos. La muestra básica se sirve desde el mismo sitio; SAT, RGM, WhatsApp, Facebook y perfil de Google respondieron 200 durante la auditoría. | Vigilar enlaces oficiales y del backend; son dependencias externas. |
| 17 | Form validation | 🟡 PARTIAL | ✅ PASS | Se agregaron límites, validación nativa de email/año/fecha, rango de teléfono, fecha local correcta, foco y `aria-describedby` en errores, loading y protección contra doble envío. El checkout solo acepta una URL HTTPS. La persona responsable confirmó la validación equivalente en Render. | Ninguna. |
| 18 | Spam protection | ❌ FAIL | ✅ PASS | El frontend evita envíos duplicados y el backend público muestra headers de rate limit. La persona responsable confirmó la protección en Render. | Vigilar métricas de abuso y agregar Turnstile únicamente si existe abuso real. |
| 19 | Analytics | 🟡 PARTIAL | ✅ PASS | Los tres IDs existentes se conservaron. Analytics corre solo en `certimotors.com`/`www`, después de consentimiento; registra CTA, apertura de checkout, formulario válido y compra. | Verificar eventos en GA4, Meta Events Manager y TikTok Events Manager después del despliegue. |
| 20 | One clear CTA | ✅ PASS | ✅ PASS | El hero conserva un solo CTA primario: “Ver planes y precios”; navegación y cierre refuerzan la misma acción. | Ninguna. |

## Changes implemented

- Se incorporaron páginas legales provisionales, navegación legal, favicon y página 404.
- Se implementó consentimiento previo para Google Analytics, Meta Pixel y TikTok Pixel, con aceptación, rechazo, persistencia y reapertura.
- Se agregaron eventos para CTA, apertura y envío válido del checkout, y compra confirmada.
- Se mejoró la validación y accesibilidad del formulario sin enviar órdenes de prueba a producción.
- Se convirtió el FAQ en un acordeón de botones navegable por teclado con `aria-expanded`, `aria-controls` y regiones asociadas.
- Se agregó skip link, se corrigieron nombres accesibles y se preservó una sola jerarquía `h1`/`main`.
- Se completó Twitter Card, canonical, favicon, imagen de negocio y FAQPage en JSON-LD.
- Se optimizaron imágenes a WebP, se difirieron previews y se alojó DM Sans localmente con su licencia OFL.
- Se actualizó el sitemap y se validó robots.txt.
- Se publicaron los textos legales aprobados: se retiraron los avisos de borrador y `noindex`, y se agregaron ambas URLs al sitemap.
- Se regeneró el certificado básico como una muestra de 80 puntos, se retiraron controles demasiado específicos, se anonimizaron los datos y se marcó cada página como ficticia.
- La tarjeta del reporte básico ahora abre el PDF local validado y muestra una vista previa coherente con los 80 puntos.
- Se añadió `Referrer-Policy` mediante meta; los headers restantes requieren control del hosting/CDN.

## Files changed

- `.gitattributes`
- `index.html`
- `tokens.css`
- `logo.svg`
- `404.html`
- `privacidad.html`
- `terminos.html`
- `legal.css`
- `favicon.svg`
- `robots.txt`
- `sitemap.xml`
- `assets/design/inspection-hero.webp`
- `assets/design/report-basic.png`
- `assets/design/report-full.webp`
- `assets/muestras/certificado-basico-muestra.pdf`
- `assets/fonts/dm-sans-latin.woff2`
- `assets/fonts/OFL.txt`
- `PRE_LAUNCH_AUDIT.md`

## Manual actions required

1. **P2 — Añadir headers desde CDN/hosting.** GitHub Pages entrega HSTS, pero la respuesta observada no incluye CSP, `X-Content-Type-Options` ni `Permissions-Policy`. Si se coloca un CDN/proxy delante del sitio, agregar `nosniff`, una política de permisos restrictiva y probar CSP primero en `Report-Only`; incluir `frame-ancestors` antes de aplicar la política definitiva.
2. **P2 — Verificar medición.** En una sesión limpia, rechazar cookies y confirmar 0 requests de tracking; aceptar y validar PageView y los eventos `cta_servicios_click`, `checkout_abierto`, `checkout_formulario_enviado` y `purchase` en las herramientas de cada proveedor.
3. **P2 — Search Console.** Enviar el sitemap y solicitar recrawl del home cuando la nueva versión esté pública.
4. **P3 — Dispositivos reales.** Completar una prueba rápida en un iPhone y un Android antes de aumentar el presupuesto de campañas.

## Validation results

- **Build:** ➖ N/A. Sitio estático sin sistema de build; se sirvió localmente por HTTP y las cuatro páginas cargaron.
- **Lint:** ➖ N/A para scripts del proyecto. No existe configuración ni comando de lint.
- **Typecheck:** ➖ N/A. No hay TypeScript.
- **Automated tests:** ➖ N/A. No existe suite de pruebas. Se ejecutaron comprobaciones estáticas y funcionales dirigidas.
- **HTML:** ✅ `html-validate` terminó con 0 errores en `index.html`, `privacidad.html`, `terminos.html` y `404.html`.
- **JavaScript:** ✅ Los dos bloques ejecutables compilaron con el parser de Node; no hubo errores ni warnings en consola durante la prueba de navegador.
- **JSON-LD/XML:** ✅ Dos bloques JSON-LD parseables; `sitemap.xml` válido con `xmllint`.
- **PDF básico:** ✅ Cinco páginas renderizadas y revisadas; 80 puntos únicos y consecutivos, sin referencias a 110 puntos, dominio anterior ni inspectores identificables. La marca de muestra aparece en las cinco páginas.
- **Estructura:** ✅ IDs únicos, una etiqueta `main`, un `h1`, un formulario, un dialog y 0 anchors internos faltantes.
- **Links:** ✅ 0 referencias locales faltantes. Ocho dependencias externas críticas respondieron HTTP 200 el 11 de septiembre de 2026.
- **Responsive:** ✅ 320/375/390/768/1024/1440 px sin overflow horizontal.
- **Formulario:** ✅ Error vacío enfoca `cf-nombre`, expone `aria-invalid=true`, asocia `form-error` y mantiene el botón habilitado; no se enviaron datos al backend.
- **Cookies:** ✅ Rechazar oculta el banner, preferencias lo reabre y aceptar lo oculta; antes del consentimiento hubo 0 scripts de tracking. En localhost los pixels permanecen desactivados por diseño.
- **Accessibility:** ✅ Lighthouse 100/100, sin auditorías fallidas; FAQ probado con teclado.
- **Performance:** ✅ Lighthouse móvil final 97/100; FCP 1.5 s, LCP 2.4 s, TBT 0 ms, CLS 0, Speed Index 1.5 s. La referencia “buena” de Core Web Vitals es LCP ≤2.5 s, INP ≤200 ms y CLS ≤0.1 al percentil 75.
- **Network:** ✅ 34 → 5 requests, 1,287,448 → 257,510 bytes y 662,373 → 0 bytes de tracking antes de consentimiento.
- **SEO/best practices:** ✅ Lighthouse 100/100 en ambas categorías. Validación de Rich Results sobre la URL queda pendiente hasta publicar.
- **Producción:** ✅ GitHub Pages completó correctamente el despliegue del commit `5d4b304`. Home, privacidad, términos, robots, sitemap, favicon y el PDF básico respondieron 200; una ruta inexistente respondió 404. El home y el PDF publicados coinciden byte por byte con los archivos locales validados.

Las cifras iniciales corresponden a la URL pública y las finales al servidor local con throttling móvil de Lighthouse. Son comparables como señal de laboratorio, pero deben confirmarse en la URL publicada y con datos de campo.

## Remaining risks

- La confirmación de validación y anti-spam del backend fue proporcionada por la persona responsable; este repositorio frontend no contiene el código de Render para repetir esas pruebas.
- La respuesta actual de GitHub Pages carece de varios security headers; CSP requiere pruebas con los pixels aceptados para no romper conversiones.
- Los eventos de analítica deben comprobarse en los paneles de GA4, Meta y TikTok después de recibir tráfico con consentimiento.

## Sources

- [Core Web Vitals thresholds — web.dev](https://web.dev/articles/defining-core-web-vitals-thresholds)
- [Securing GitHub Pages with HTTPS — GitHub Docs](https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https)
- [LocalBusiness structured data — Google Search Central](https://developers.google.com/search/docs/appearance/structured-data/local-business)
- [General structured data guidelines — Google Search Central](https://developers.google.com/search/docs/appearance/structured-data/sd-policies)

## Launch recommendation

🟢 READY TO LAUNCH

- Los cambios del frontend están validados y alcanzan Lighthouse 97/100/100/100 en la prueba local previa.
- Privacidad y términos fueron aprobados y quedaron indexables.
- La persona responsable confirmó la validación y protección del backend en Render.
- El certificado básico se redujo a 80 puntos y cada página está identificada como muestra ficticia.
- Quedan verificaciones posteriores al despliegue y mejoras de headers que no bloquean el lanzamiento.
