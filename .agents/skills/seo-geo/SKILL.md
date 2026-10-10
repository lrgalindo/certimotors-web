---
name: seo-geo
description: Método completo para posicionar un sitio en los primeros lugares orgánicos de Google y lograr que lo citen ChatGPT, Perplexity, Gemini y Google AI Overviews (SEO + GEO). Sirve para cualquier proyecto web — negocio local, servicio a domicilio, fintech o financiamiento, marketplace, e-commerce, SaaS — desde la estrategia (qué páginas crear) hasta la implementación técnica, Google Business Profile y el ciclo de mejora con datos de Search Console. Úsala siempre que el usuario hable de SEO, posicionamiento, "salir primero en Google", tráfico orgánico, palabras clave, Search Console, sitemap, schema, llms.txt, ficha de Google, visibilidad en IA o GEO, o cuando esté lanzando o auditando un sitio y quiera que lo encuentren, aunque no diga "SEO".
---

# SEO + GEO para cualquier proyecto

Esta skill resume lo que funcionó (y lo que salió mal) al llevar sitios nuevos de cero a indexados y rankeando en nichos de Guatemala, generalizado para cualquier tipo de proyecto. La idea central:

> **Gana el sitio que responde mejor y con datos concretos la pregunta exacta que la gente busca, en una página dedicada a esa pregunta, técnicamente impecable y con señales de confianza verificables.**

Google y los motores de IA premian lo mismo: páginas específicas, datos concretos (precios, plazos, requisitos), respuestas directas y una entidad (el negocio) que existe de verdad fuera del sitio.

Sé honesto con las expectativas: nadie puede garantizar el primer lugar ni que una IA recomiende el negocio. Lo que sí se puede es darles más razones que a la competencia. En búsquedas competidas el SEO tarda de 3 a 9 meses en rendir fuerte; si el negocio necesita clientes antes, sugiere anuncios de búsqueda de alta intención en paralelo (en finanzas, revisando las políticas de servicios financieros de cada plataforma).

## Cómo trabajar

Sigue estas fases en orden. Si el usuario solo pide una parte (por ejemplo "revisa mi SEO técnico"), salta a esa fase, pero menciona en una línea las fases previas que falten si cambian el resultado.

### 1. Diagnóstico (antes de tocar código)

Entiende el proyecto respondiendo esto, desde el código, el sitio en vivo o preguntando al usuario lo que no se pueda deducir:

- **Qué vende y a quién.** ¿Qué problema resuelve? ¿Quién busca eso y con qué palabras? (la gente busca "copia de llave", no "duplicado de llave"; "cuánto cuesta polarizar", no "servicio de películas para vidrios").
- **Dónde.** ¿Es local (ciudad, zonas), nacional o sin ubicación? Esto decide si Google Business Profile es prioridad.
- **Qué entidades tiene el negocio** que se puedan convertir en páginas: productos, modelos, marcas, servicios, ubicaciones, casos de uso, requisitos.
- **Qué no publica la competencia.** Busca el hueco: precios, plazos, requisitos, garantías, comparaciones honestas. En nichos donde todos dicen "llámenos para cotizar", publicar el precio es la ventaja más fuerte que existe.
- **Qué está confirmado.** Lista precios, promesas y datos que el dueño confirmó y los que son supuestos. Nunca publiques supuestos como hechos (ver Reglas).
- **Estado actual.** ¿Hay sitio? ¿Está en Search Console? ¿Hay ficha de Google? ¿Qué framework usa?

Lee `references/verticales.md` para adaptar la estrategia al tipo de proyecto (local, a domicilio, fintech/YMYL, marketplace, e-commerce, SaaS).

### 2. Mapa de páginas (la arquitectura que rankea)

La mayor palanca de SEO es tener **una página por cada intención de búsqueda que valga la pena**, no una home que intente rankear para todo. Diseña el mapa con estos tipos:

| Tipo | Para qué búsquedas | Ejemplo |
|---|---|---|
| Home | La búsqueda principal del negocio + ubicación | "polarizado de carros guatemala" |
| Páginas de entidad (programáticas) | Entidad específica × intención | `/polarizado-toyota-corolla`, `/financiamiento-iphone-15` |
| Hubs de categoría | Búsquedas amplias de categoría | `/polarizado/toyota`, `/meseros/eventos` |
| Páginas de servicio | Cada servicio distinto | `/llave-inteligente`, `/meseros-para-bodas` |
| Guías que responden preguntas | "cuánto cuesta…", "es legal…", "qué es mejor…" | `/precio-polarizado-guatemala` |
| Páginas de confianza | Garantía, requisitos, cómo funciona | `/garantia`, `/requisitos` |
| Ubicación (solo si hay cobertura real) | "X en zona 10", "X en Mixco" | `/polarizado-zona-10` |

Detalles, reglas de enlazado interno y cómo evitar contenido duplicado en páginas programáticas: `references/estrategia.md`.

### 3. Base técnica

Revisa o implementa la checklist completa de `references/tecnico.md`. Lo mínimo que no puede faltar:

- Un solo dominio canónico (redirigir `www` ↔ sin `www` con 301/308) y `<link rel="canonical">` en **todas** las páginas, incluida la home.
- `robots.txt` que permita rastrear y apunte al sitemap; `sitemap.xml` con todas las páginas indexables y `lastmod` **estable** (no la fecha de hoy en cada request).
- Título único por página, ≤ 60 caracteres, con la palabra clave y el dato diferenciador al inicio ("Polarizado Toyota Corolla en Guatemala: desde Q850"). Meta description ≤ 155 caracteres.
- Un solo `<h1>` por página, jerarquía de encabezados sin saltos.
- Schema JSON-LD apropiado (ver `references/tecnico.md` → Schema).
- Imagen para redes (`og:image`) en todas las páginas, no solo en la home.
- El contenido importante llega en el HTML del servidor (SSR/SSG), no solo después de ejecutar JavaScript: varios rastreadores de IA no ejecutan JS.
- Rendimiento móvil: fuentes servidas desde el propio dominio, sin bloqueos de render, LCP < 2.5 s.
- 404 real para URLs inexistentes.

Usa `scripts/audit_pages.py` para auditar páginas en vivo (título, descripción, canonical, H1, schema, og:image, noindex) en lugar de revisarlas a mano.

### 4. Contenido que merece rankear

Lee `references/contenido.md`. Lo esencial:

- Cada página debe tener algo **único y verificable**: su precio, sus requisitos, su comparación con alternativas cercanas, su ficha de datos. Si 300 páginas solo cambian el nombre del producto, Google indexará pocas.
- Genera el texto variable **a partir de datos reales** del catálogo (precio, categoría, atributos), nunca inventando especificaciones técnicas.
- Escribe preguntas frecuentes con la **frase literal** que la gente busca y respuesta directa en la primera oración.
- En temas de dinero, salud o legales (YMYL), la confianza pesa más: requisitos claros, costos totales, quién es la empresa, cómo contactarla.

### 5. GEO: que te citen los motores de IA

Lee `references/geo.md`. Lo esencial:

- Permite los rastreadores de IA en `robots.txt` (OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot; los de entrenamiento como GPTBot y Google-Extended son decisión del usuario) y revisa que el firewall del hosting no los bloquee.
- Registra el sitio en **Bing Webmaster Tools** y activa IndexNow: la búsqueda de ChatGPT y Copilot se apoyan en el índice de Bing.
- Escribe pasajes "citables": oraciones autocontenidas con el dato completo (quién, qué, cuánto, dónde, cuándo).
- Consigue **menciones en terceros** (medios, directorios, comunidades, reseñas): es lo que más mueve las recomendaciones de IA, más que cualquier cambio en el propio sitio.
- Refuerza la entidad: mismo nombre, teléfono y descripción en el sitio, la ficha de Google, redes y directorios, enlazados con `sameAs`.
- `/llms.txt` es barato de generar desde los datos del sitio, pero no hay evidencia sólida de que los grandes motores lo usen: hazlo, sin tratarlo como prioridad.

### 6. Presencia local y de entidad

Si el negocio atiende en una ubicación o una zona (local o a domicilio), Google Business Profile suele pesar más que cualquier cambio en el sitio para búsquedas locales. Si opera 100% en línea sin dirección ni zona de servicio, la ficha no aplica o aporta poco: la entidad se construye con redes, directorios y menciones. Lee `references/local-gbp.md` para el kit completo: categorías, descripción, servicios con precio, fotos, reseñas y cómo enlazar la ficha en el schema. Si la ficha ya existe, no sugieras crearla: optimízala y enlázala.

### 7. Medir e iterar

Lee `references/search-console.md`. El ciclo:

1. Verificar el dominio en Search Console (propiedad de dominio por TXT).
2. Enviar el sitemap **con la URL completa** y pedir indexación de 3-5 páginas clave.
3. Esperar 2-4 semanas de datos.
4. Revisar consultas con muchas impresiones y pocos clics: ahí el título o la descripción no usan las palabras del usuario. Ajustar títulos, H1, FAQ y schema al lenguaje real.
5. Revisar páginas que no se indexan: casi siempre es contenido demasiado parecido entre páginas.

`scripts/gsc.py` consulta rendimiento, consultas, páginas, estado de indexación y sitemaps vía API con una cuenta de servicio.

## Reglas que no se negocian

Estas reglas existen porque romperlas cuesta más que cualquier ganancia de ranking:

- **No inventes datos.** Precios, plazos, garantías, coberturas, tasas de interés, requisitos: solo lo que el dueño confirmó. Un "corte incluido" falso o una garantía que no existe genera reclamos, malas reseñas y, en finanzas, problemas legales. Si falta un dato, marca el texto como pendiente y pregunta.
- **No hagas trampas.** Nada de reseñas falsas, texto oculto, keyword stuffing, nombres de ficha con palabras clave, ni páginas de ubicación donde no hay servicio. Google las detecta y la penalización dura meses.
- **Una página, una intención.** Si dos páginas responden lo mismo, compiten entre sí. Fusiona o diferencia.
- **Verifica en vivo.** Después de cambiar algo, comprueba en el sitio publicado (no solo en local) que el cambio está: título, canonical, schema, sitemap, código 200.

## Entregables

**Si el sitio ya existe y pide una auditoría**, entrega:

```markdown
## Resumen
Una o dos frases: dónde está el sitio y cuál es la mayor oportunidad.

## Prioridades
| # | Acción | Impacto | Esfuerzo | Quién |
(ordenadas por impacto/esfuerzo; "Quién" = código, dueño, o ambos)

## Hallazgos
Agrupados por fase (técnico, contenido, GEO, local, datos), cada uno con evidencia: URL, qué se ve, qué debería verse.

## Pendiente de confirmar
Datos del negocio que bloquean contenido (precios, cobertura, garantías…).
```

**Si el proyecto parte de cero o de una sola landing y pide un plan**, entrega:

```markdown
## Resumen
Dónde está hoy, la mayor oportunidad y expectativas realistas de tiempo.

## Calendario
| Cuándo | Qué | Quién |
(semana 1: datos y confianza; semanas 1-2: base técnica; semanas 2-8: páginas; mes 2+: entidad, menciones, iteración)

## Mapa de páginas
| Tipo | URL de ejemplo | Búsqueda objetivo |

## Plan por fase
Las 7 fases aplicadas al caso, con ejemplos concretos del negocio.

## Pendiente de confirmar
Datos del negocio que bloquean contenido.
```

Si pasa de una landing a un sitio multipágina, conserva la URL de la landing como home, mueve cada sección que responda una intención distinta a su propia página y redirige con 301 cualquier URL que cambie.

Cuando el usuario pida implementar, haz los cambios en el código, verifica con build/typecheck y con el sitio en vivo, y cierra con lo que cambió y lo que queda pendiente de su lado (Search Console, ficha de Google, confirmaciones del dueño).

Casos reales con lecciones concretas: `references/casos.md`.
