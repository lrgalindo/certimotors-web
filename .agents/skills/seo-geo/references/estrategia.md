# Estrategia: qué páginas crear y cómo conectarlas

## 1. Encuentra el hueco del nicho

Antes de escribir una línea, busca en Google las 5-10 consultas principales del negocio (en modo incógnito, desde la ubicación del cliente si es local) y anota qué hacen los primeros resultados:

- ¿Publican precio? ¿Plazos? ¿Requisitos? ¿Garantía?
- ¿Tienen una página por producto/modelo/servicio o una sola página genérica?
- ¿Responden la pregunta en la primera pantalla o hay que llamar?

El hueco más común en Latinoamérica es la **transparencia**: casi nadie publica precios ni condiciones. Un sitio que dice "Toyota Corolla: Q850, garantía 1 año por escrito" le gana a uno que dice "cotice por WhatsApp", porque responde la búsqueda "cuánto cuesta…" que el otro ignora. Lo mismo aplica a tasas y requisitos en financiamiento, o a tarifas por hora en servicios.

## 2. Arma el mapa de palabras clave por intención

Agrupa las búsquedas por **intención**, no por palabra suelta. Cada grupo es una página:

| Intención | Señal en la búsqueda | Página |
|---|---|---|
| Transaccional específica | marca/modelo/producto + "precio", "cotizar" | Página de entidad |
| Transaccional general | servicio + ciudad | Home o hub |
| Comparativa | "vs", "mejor", "cuál conviene" | Guía comparativa |
| Informativa con dinero | "cuánto cuesta", "precio" | Guía de precios con tabla |
| Informativa de duda | "es legal", "requisitos", "cuánto tarda", "qué pasa si" | Guía corta con respuesta directa |
| Confianza | "garantía", "opiniones", "es confiable" | Página de garantía / cómo funciona |
| Local | servicio + zona/colonia | Página de ubicación (solo con cobertura real) |

Fuentes de palabras: autocompletado de Google, "Otras preguntas de los usuarios", "Búsquedas relacionadas", Search Console (cuando haya datos), Keyword Planner o Ahrefs si el usuario tiene acceso. Si no hay herramienta de volumen, márcalo como hipótesis a validar con Search Console en 2-4 semanas.

**Usa el lenguaje del cliente, no el del negocio.** El negocio dice "duplicado de llave con transponder"; el cliente busca "copia de llave con chip". El negocio dice "película de control solar"; el cliente busca "polarizado". Search Console es la fuente de verdad una vez que hay datos.

## 3. Páginas programáticas (una por entidad)

Cuando el negocio tiene un catálogo (modelos de carro, marcas de celular, tipos de evento, colonias, productos), genera una página por entidad desde los datos. Es lo que permite competir por cientos de búsquedas específicas con poco esfuerzo.

Para que Google las indexe y no las trate como duplicadas:

- **URL descriptiva y estable:** `/polarizado-toyota-corolla`, `/financiamiento-samsung-a55`. Slug en minúsculas, sin acentos, con guiones.
- **Título y H1 con la entidad y el dato diferenciador:** precio, plazo o atributo.
- **Datos propios de esa entidad** en una ficha visible: precio, categoría, qué incluye, garantía, requisitos.
- **Texto derivado de datos**, no plantilla con el nombre cambiado: comparación con entidades hermanas ("el Corolla cuesta lo mismo que el Yaris porque comparten carrocería; el RAV4 es SUV y tiene otra tarifa"), notas por categoría, FAQ con la entidad en la pregunta.
- **Agrupa por la variable que de verdad cambia el precio o la respuesta** (en polarizado: la carrocería, no el año; en financiamiento: el rango de precio del equipo). Así el contenido es honesto y no hay que inventar diferencias.
- No generes combinaciones que no tienen demanda ni sentido (por ejemplo modelo × cada colonia). Mejor 400 páginas útiles que 40 000 vacías.

## 4. Hubs de categoría

Las páginas de entidad solas dejan que Google adivine cuál mostrar para búsquedas amplias ("llave programada honda guatemala"): en un caso real solo 1 de 5 páginas Honda aparecía. Un hub por categoría (`/llaves/honda`, `/polarizado/toyota`) consolida la búsqueda amplia y reparte autoridad:

- Lista todas las entidades de la categoría con su precio "desde".
- Texto corto propio de la categoría.
- Enlaza a cada entidad, y cada entidad enlaza de vuelta a su hub (y en el breadcrumb).
- Schema `ItemList` + `BreadcrumbList`.

## 5. Guías

Una guía por pregunta frecuente con intención clara. Formato que funciona:

1. H1 con la pregunta o la keyword.
2. Respuesta directa en el primer párrafo (2-3 oraciones, con el dato).
3. Tabla si hay números (precios por categoría, comparación de opciones).
4. Desarrollo con H2 por subtema.
5. FAQ al final con preguntas literales.
6. CTA hacia el cotizador o la página de entidad.

Guías que casi siempre valen la pena: precios, comparación de opciones, requisitos/legalidad, cuánto tarda, garantía, errores comunes.

## 6. Enlazado interno

- Home → hubs, guías principales y entidades más buscadas.
- Hub → todas sus entidades.
- Entidad → su hub, 4-8 entidades hermanas, 3-5 de la misma categoría en otras marcas, y la guía relevante.
- Rota los enlaces a "otras marcas" según la página (por índice) para que todas reciban enlaces, en vez de enlazar siempre a las mismas 8.
- Footer con guías y hubs principales.
- Breadcrumbs visibles con schema `BreadcrumbList`.

## 7. Páginas de ubicación

Solo cuando hay cobertura real y algo distinto que decir (tiempo de llegada, costo de traslado, punto de atención). Una página de "X en zona 10" idéntica a "X en zona 14" con el nombre cambiado es contenido delgado y puede perjudicar al sitio entero. Si el negocio es a domicilio, la ficha de Google con zonas de servicio suele rendir más que estas páginas.
