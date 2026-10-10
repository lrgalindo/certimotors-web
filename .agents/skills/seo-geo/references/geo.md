# GEO: visibilidad en motores de IA

GEO (Generative Engine Optimization) es lograr que ChatGPT, Perplexity, Gemini, Copilot y Google AI Overviews encuentren, entiendan y **citen** el sitio. Comparte casi toda la base con el SEO (contenido claro, técnico limpio, entidad confiable) y agrega algunas piezas propias.

## 1. Dejar entrar a los rastreadores de IA

En `robots.txt`, salvo que el usuario quiera bloquearlos, no excluyas:

| Bot | De quién | Para qué |
|---|---|---|
| `OAI-SearchBot` | OpenAI | Búsqueda de ChatGPT (citas en vivo) |
| `ChatGPT-User` | OpenAI | Visitas cuando un usuario pide leer una página |
| `GPTBot` | OpenAI | Entrenamiento |
| `ClaudeBot`, `Claude-User`, `Claude-SearchBot` | Anthropic | Entrenamiento / búsqueda |
| `PerplexityBot`, `Perplexity-User` | Perplexity | Índice y visitas |
| `Google-Extended` | Google | Uso en Gemini (no afecta Google Search) |
| `Bingbot` | Microsoft | Bing y Copilot |

Un `User-agent: *` con `Allow: /` ya los permite. Revisa también que el firewall del hosting (Cloudflare, Vercel) no los esté bloqueando como "bots": si la IA no puede leer la página, no la cita. La lista de bots cambia; verifica los nombres vigentes en la documentación de cada proveedor si el usuario quiere reglas específicas.

## 2. Bing Webmaster Tools e IndexNow

La búsqueda de ChatGPT y Microsoft Copilot se apoyan en buena parte en el índice de Bing. Un sitio que Bing no tiene indexado difícilmente aparece en esas respuestas.

- Registra el sitio en [Bing Webmaster Tools](https://www.bing.com/webmasters) (se puede importar desde Search Console) y envía el sitemap.
- Activa **IndexNow** para avisar a Bing (y otros motores que lo soportan) cada vez que se publica o cambia una página. En Next.js basta con publicar la llave en `/<llave>.txt` y hacer un POST a `https://api.indexnow.org/indexnow` con las URLs nuevas al desplegar.

## 3. Contenido renderizado en el servidor

Varios rastreadores de IA descargan el HTML y no ejecutan JavaScript. Si los precios, requisitos o respuestas se cargan solo en el cliente, para ellos la página está vacía. Verifica con `curl -s https://dominio/pagina | grep "dato clave"`: si no aparece, hay que renderizarlo en el servidor (SSG/SSR).

## 4. `llms.txt`

Un archivo en `/llms.txt` (texto plano, Markdown) que resume el sitio para modelos de lenguaje. Formato:

```markdown
# Nombre del negocio

> Una o dos oraciones: qué hace, dónde, para quién, y el dato diferenciador (precios publicados, plazos, garantía).

## Precios / datos clave
- Categoría A: desde QX
- Categoría B: desde QY

## Guías
- [Precios de X en Guatemala](https://dominio/precio-x): tabla por categoría.
- [Requisitos](https://dominio/requisitos)

## Catálogo
- [Entidad 1](https://dominio/entidad-1)
```

Genéralo desde los mismos datos del sitio (en Next.js, una ruta `app/llms.txt/route.ts` con `force-static`) para que nunca quede desactualizado. Es una convención emergente, no un estándar oficial, y no hay evidencia sólida de que ChatGPT o Google la usen hoy. Cuesta poco y puede servir a agentes que la lean, pero no la priorices sobre contenido, Bing o menciones.

## 5. Pasajes citables

Los motores de IA extraen fragmentos. Un fragmento es citable cuando se entiende solo, sin el resto de la página:

- **Autocontenido:** "En Guatemala, polarizar un sedán cuesta desde Q850 con película clásica y Q1,950 con nano cerámica, mano de obra incluida." en vez de "El precio depende del tipo de película (ver arriba)."
- **Con el dato y la fuente o el alcance:** quién, qué, cuánto, dónde, desde cuándo.
- **Respuesta primero**, matiz después.
- **Tablas y listas** con encabezados claros: son fáciles de extraer.
- **Definiciones** cortas de los términos del nicho ("El porcentaje de polarizado es la luz que deja pasar el vidrio: 5% es muy oscuro, 70% casi transparente").
- **Preguntas como encabezados** (H2/H3) con la frase literal.

## 6. Entidad consistente

Los modelos confían más en negocios que "existen" en varias fuentes coherentes:

- Mismo nombre, teléfono, descripción y URL en el sitio, la ficha de Google, Facebook/Instagram, directorios y marketplaces.
- Enlázalos desde el schema del negocio con `sameAs`.
- Reseñas reales en Google.

## 7. Menciones en terceros (lo que más mueve a la IA)

Los modelos recomiendan negocios que **otros** mencionan. Para saber dónde estar:

1. **Mira qué citan hoy.** Pregunta en ChatGPT (con búsqueda), Perplexity y Gemini las consultas principales y anota las fuentes que citan: esos sitios son la lista de objetivos.
2. **Directorios y listados** del país y del nicho (directorios locales, cámaras de comercio, listados de "mejores X en [ciudad]", marketplaces).
3. **Medios locales y de nicho** con un ángulo de dato, no de publicidad: "cuánto cuesta X en [país] en 2026", "X% de la gente no tiene tarjeta de crédito; así compran celular" (con la cifra investigada, no inventada).
4. **Comunidades:** grupos de Facebook, Reddit, foros del nicho. Participar con la cuenta identificada respondiendo dudas, sin spam.
5. **Creadores** del nicho (reseñas, unboxing, "lo probé"), marcando el contenido pagado como tal.
6. **Alianzas** con negocios complementarios que enlacen al sitio.

Prepara los textos y la lista de objetivos; la publicación la hace el dueño. No publiques en nombre del usuario sin su permiso.

## 8. Datos estructurados

El schema (ver `tecnico.md`) ayuda a que los modelos entiendan precios, ubicación y tipo de negocio. Prioriza `LocalBusiness`/`Organization` con `@id`, `Service`/`Product` con `offers`, `FAQPage` y `BreadcrumbList`.

## 9. Cómo medir

No hay un "Search Console de IA" completo todavía:

- Pregunta directamente en ChatGPT (con búsqueda), Perplexity y Gemini las consultas principales ("¿cuánto cuesta polarizar un carro en Guatemala?") y anota si citan el sitio. Repite cada mes.
- Revisa en los logs del hosting las visitas de `OAI-SearchBot`, `ChatGPT-User`, `PerplexityBot`.
- En analítica, filtra referidos de `chatgpt.com`, `perplexity.ai`, `gemini.google.com`, `copilot.microsoft.com` (ChatGPT suele agregar `utm_source=chatgpt.com`).
- Revisa en Bing Webmaster Tools cuántas páginas tiene indexadas Bing.
- Google AI Overviews se mide junto con la búsqueda normal en Search Console.
