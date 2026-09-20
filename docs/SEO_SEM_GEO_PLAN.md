# CERTIMOTORS — Plan SEO / SEM / GEO

Fecha: 2026-09-20 · Alcance: certimotors.com (sitio estático en GitHub Pages).
"GEM" se interpretó como **GEO** (Generative Engine Optimization: aparecer citado en ChatGPT, Gemini, Perplexity, Claude, AI Overviews).

## 1. Diagnóstico

El sitio era **una sola URL** (`/`) con un solo enfoque de palabra clave ("inspección independiente de vehículos"). Google solo puede posicionar una página por intención de búsqueda; con una sola URL no había cómo aparecer para "revisión mecánica", "revisión de compra", "carros rodados", etc.

En una búsqueda de prueba (hecha desde EE. UU., no es medición oficial) los resultados dominantes para estas intenciones eran Car Detective, Certiauto, TRS Taller y blogs como Movilauto. Ninguno de ellos tiene páginas para "rodados" ni "verificación legal de gravámenes" como intención propia: ahí está el hueco.

## 2. Mapa de palabras clave → página

Volúmenes de búsqueda **no incluidos**: no hubo acceso a Keyword Planner ni Ahrefs en esta sesión. Validar en Google Keyword Planner antes de asignar presupuesto.

| Página (URL) | Keyword principal | Secundarias | Intención |
|---|---|---|---|
| `/` (home) | revisión mecánica de carros usados guatemala | inspección de vehículos, certificadora de autos, revisión de compra | Comercial general / marca |
| `/revision-mecanica-vehiculos-guatemala/` | revisión mecánica de vehículos guatemala | revisión mecánica carro usado, escáner OBD-II, diagnóstico de carro | Comercial |
| `/revision-de-compra-vehiculo-usado-guatemala/` | revisión de compra carro usado | inspección pre-compra, revisar carro antes de comprar | Comercial (más alta conversión) |
| `/inspeccion-vehiculos-usados-de-agencia-guatemala/` | inspección vehículos usados de agencia | seminuevos de agencia, segunda opinión | Comercial |
| `/inspeccion-carros-rodados-guatemala/` | inspección de carros rodados | comprar carro rodado, revisar rodado | Comercial |
| `/peritaje-vehicular-guatemala/` | peritaje vehicular guatemala | peritaje de carros, expertaje vs peritaje, avalúo | Informativa → comercial |
| `/verificacion-legal-vehiculo-guatemala/` | verificación legal de vehículos | gravámenes, prenda, VIN, propietario SAT | Comercial |
| `/guias/…` (5 guías + índice) | qué revisar al comprar carro usado · cuánto cuesta revisión mecánica · rodado vs agencia · gravamen · carro chocado | — | Informativa (capta demanda temprana y alimenta GEO) |

## 3. Qué se cambió en el repo

**Contenido nuevo (12 páginas):** 6 páginas de servicio, 5 guías y 1 índice de guías. Cada página tiene: title y description únicos, un H1, bloque de respuesta directa al inicio, tabla de datos clave, FAQ visible, enlaces internos cruzados, CTA a planes y a WhatsApp, y fecha de actualización.

**Home (`index.html`):**
- Title: "Revisión mecánica de carros usados en Guatemala | CERTIMOTORS"; description con revisión mecánica, de compra, agencia, rodados y precio.
- H1 y subtítulo con la palabra clave; se conservó el diseño.
- Nueva sección `#especialidades` con enlaces a las 6 páginas (enlazado interno) y a `/guias/`.
- 3 preguntas nuevas en el FAQ, visibles y en JSON-LD.
- JSON-LD: se agregó `WebSite`; `AutomotiveBusiness` ahora tiene logo, punto de contacto, país, `knowsAbout` y descripciones de cada oferta.
- Enlaces a servicios y guías en el footer y "Guías" en el menú.
- El bloque de analítica pasó a `assets/js/analytics.js` (mismo código, sin cambios de lógica) para que las páginas nuevas usen el mismo consentimiento y los mismos pixels.

**Técnico:** `sitemap.xml` con 15 URLs; `robots.txt` con crawlers de IA permitidos de forma explícita; `llms.txt`; JSON-LD por página (`WebPage`/`Article`, `Service`, `BreadcrumbList`, `FAQPage`); `og:locale=es_GT`; `landing.css` y `assets/js/landing.js` compartidos.

## 4. GEO (motores generativos)

Hecho en el sitio:
- Respuesta directa de 2–3 líneas al inicio de cada página (formato que los asistentes citan).
- Datos verificables y consistentes en todas las páginas (precios, tiempos, cobertura) y publicados también en `llms.txt`.
- Definiciones claras y comparativas (peritaje vs expertaje vs avalúo; rodado vs agencia vs particular).
- Fuentes oficiales enlazadas (SAT, RGM) y avisos de alcance ("no sustituye asesoría legal", "no es avalúo").

Pendiente (fuera del repo, necesita acción tuya):
1. **Google Business Profile**: verifica que exista y esté completo (categoría de inspección de vehículos, zona de servicio, teléfono, horario, enlace a `/`). Es la señal local más fuerte y alimenta a Gemini.
2. **Reseñas reales** de clientes en Google. Ver observación en la sección 7.
3. **Menciones externas**: directorios de Guatemala, Facebook, y notas o guías en medios o blogs automotrices locales que enlacen a las guías.
4. **Medición**: cada mes pregunta en ChatGPT, Gemini y Perplexity "¿dónde puedo revisar un carro usado antes de comprarlo en Guatemala?", "cuánto cuesta una revisión mecánica de carro usado en Guatemala", "cómo saber si un carro tiene gravamen en Guatemala", y anota si aparece CERTIMOTORS.

## 5. SEM — Google Ads

Archivo importable de referencia: [`google-ads-keywords.csv`](google-ads-keywords.csv) (108 filas: 1 campaña, 7 grupos, concordancia exacta y de frase, negativas de campaña).

**Estructura sugerida**
- Campaña de búsqueda, ubicación **Guatemala** (opción "Presencia": personas que están en la zona), idioma español, sin Red de Display.
- Un grupo por página de destino (tabla abajo). Cada grupo apunta a su URL, no al home.
- Campaña aparte para la marca (`certimotors`) con presupuesto bajo.
- Etiquetado automático (gclid) activado.
- Estrategia inicial: "Maximizar clics" con tope de CPC por 2 semanas; pasar a "Maximizar conversiones" al acumular ~30 conversiones.
- Presupuesto: definir con el CPC real que muestre Keyword Planner. No hay datos de CPC en esta sesión.

**Anuncios responsivos (RSA)** — límites: título ≤ 30, descripción ≤ 90 caracteres.

| Grupo | Títulos | Descripciones |
|---|---|---|
| Revisión de compra | Revisión de compra de carros · Inspección pre-compra GT · Antes de pagar, revísalo · Veredicto en 24–48 horas · Desde Q300 por inspección · 100% independiente · Compra tu carro con certeza · Técnico + legal en una visita | Revisión de compra de carros usados en Guatemala: 110 puntos y verificación legal. · Recibe un veredicto: comprar, negociar o rechazar. Reporte en 24–48 h. Solicítalo hoy. |
| Revisión mecánica | Revisión mecánica de carros · Escáner OBD-II + 110 puntos · Inspección donde esté el carro · Reporte en 24–48 horas · Desde Q300 por inspección · Inspector 100% independiente · No hace falta que estés · Reporte con QR verificable | Revisión mecánica independiente con escáner OBD-II. Vamos donde esté el carro. · Motor, frenos, suspensión y estructura. Reporte PDF con QR válido 90 días. |
| Carros rodados | Inspección de carros rodados · Rodado revisado antes de pagar · Chasis, VIN y estructura · Verificación legal Full Q800 · Evita comprar daños ocultos · Vamos donde esté el carro · Nunca vendemos carros · Veredicto: comprar o rechazar | Inspección de carros rodados: estructura, VIN, escáner y situación legal. · Sabe qué compras antes de pagar. Plan Full Q800, técnico y legal en una visita. |
| Usados de agencia | Inspección de carro de agencia · Segunda opinión independiente · Usados y seminuevos de agencia · 110 puntos técnicos · Reporte en 24–48 horas · Sin conflicto de interés · Desde Q550 con 110 puntos · Negocia con un reporte real | Segunda opinión independiente para usados y seminuevos de agencia en Guatemala. · No vendemos carros: trabajamos solo para ti. 110 puntos desde Q550. |
| Verificación legal | Verificación legal de carros · Gravámenes, prendas y multas · Título, matrícula y VIN · Propietario validado en SAT · Plan Full por Q800 · Incluye revisión técnica · Reporte en 24–48 horas · Antes de pagar el enganche | Verifica gravámenes, prendas, multas, VIN y propietario antes de comprar. · Plan Full Q800: verificación legal más inspección técnica de 110 puntos. |
| Peritaje | Peritaje vehicular Guatemala · Peritaje técnico de carros · Inspección de 110 puntos · Veredicto claro y verificable · Desde Q300 por inspección · Reporte PDF con QR · Independiente del vendedor · Atendemos todo el área metro | Peritaje técnico de carros usados con veredicto: comprar, negociar o rechazar. · Inspección independiente en el área metropolitana. Reporte en 24–48 horas. |

**Extensiones:** enlaces de sitio (Planes y precios `/#servicios`, Cobertura `/#cobertura`, Guías `/guias/`, Empresas `/#b2b`), llamada (+502 4255 8723), promoción (Pack 2 inspecciones, 40 % en la segunda), ubicación (si el perfil de negocio está vinculado).

**Negativas:** ya incluidas en el CSV (reparación, repuestos, gratis, empleo, seguro, avalúo, expertaje PNC, países distintos, etc.). Revisa el informe de términos de búsqueda cada semana durante el primer mes.

**Conversiones a medir** (GA4 `G-17RQ4B76BR` / `G-53TM6JHBXW`, vinculadas a Google Ads):
- `checkout_formulario_enviado` (lead de alta intención) — principal.
- `purchase` (pago confirmado) — principal.
- `checkout_abierto` y `cta_whatsapp_click` (nuevo) — secundarias.

⚠️ Limitación: la analítica solo se carga si la persona acepta cookies. Las conversiones de quien rechaza no se registran, así que Google Ads subestimará resultados. Mejora futura: Consent Mode v2 en modo avanzado.

## 6. Pasos manuales tras el despliegue

1. Hacer merge del PR y esperar el despliegue de GitHub Pages (≈1–3 min).
2. **Search Console**: verificar la propiedad, enviar `https://certimotors.com/sitemap.xml` y usar "Inspección de URL → Solicitar indexación" en las 6 páginas de servicio y en `/guias/`.
3. Probar 2 URLs en [Rich Results Test](https://search.google.com/test/rich-results) y confirmar que `Service`, `FAQPage` y `BreadcrumbList` se leen sin errores.
4. Correr PageSpeed Insights sobre `/` y una página de servicio.
5. Crear la campaña de Google Ads con el CSV y los anuncios de arriba.
6. Revisar en 2 y 4 semanas: Search Console → Rendimiento → consultas y posiciones por página.

Referencia de tiempos: las páginas nuevas suelen tardar de días a varias semanas en indexarse y posicionar; el SEM es lo que da tráfico inmediato mientras tanto.

## 7. Observaciones

- **Testimonio del home:** el único testimonio es de "Rodrigo Galindo" (el titular del proyecto). Google y la FTC tratan las reseñas propias presentadas como de cliente como engañosas. Recomendación: reemplazarlo por reseñas reales o quitarlo. **No** se agregó marcado `Review`/`AggregateRating` por esta razón.
- **Mensaje del home:** el subtítulo original prometía "verificación legal completa", pero en los planes la parte legal solo está en el **Full**. Las páginas nuevas separan ambos claramente.
- **Hosting:** el sitio se publica en GitHub Pages (no Vercel). No permite encabezados HTTP propios (CSP, etc.); ver `PRE_LAUNCH_AUDIT.md`.
- **Fase 2 sugerida:** páginas locales solo si hay contenido genuinamente distinto por zona (evitar páginas casi idénticas por municipio); una guía nueva al mes; formulario en las páginas de servicio en lugar de enviar al home.
