# Casos reales

Dos sitios de Guatemala construidos con este método en 2026. Sin métricas internas ni datos de clientes; solo lo que se hizo y lo que se aprendió.

## llavesenguate.com — copias de llave con chip

**Hueco:** ningún cerrajero publicaba precios por modelo. El sitio publica el precio por marca, modelo y año, con garantía.

**Qué funcionó**
- Una página por modelo (más de 360) más **hubs por marca**. Antes de los hubs, para "llave programada honda guatemala" solo una de cinco páginas Honda aparecía; el hub consolidó la búsqueda amplia.
- **Lenguaje del cliente desde Search Console:** las consultas con más impresiones decían "copia de llave con chip"; el sitio decía "duplicado". Se agregó "copia" y "chip" a título, H1, descripción, FAQ y schema.
- **Títulos con precio y ubicación al inicio**, bajo 60 caracteres, quitando el sufijo de marca en páginas de modelo para que no se cortara "Guatemala".
- **FAQ con preguntas literales** vistas en las consultas ("¿el mazda bt 50 2017 usa chip en la llave?").
- **Contenido por modelo derivado de datos** del catálogo (años, servicios disponibles, banda de precio) sin afirmar datos técnicos no verificados.
- **Páginas de servicio** (llave inteligente, con control, programación de chip) y guías ("perdí la llave", "mi llave no enciende el carro", precios).
- **Ficha de Google enlazada** en el schema con `sameAs` y `hasMap`.

**Errores que se corrigieron**
- Faltaba el canonical en la home.
- El `lastmod` del sitemap se recalculaba en cada request.
- Google Fonts externo bloqueaba el render (FCP/LCP en 2.9 s); se pasó a fuentes servidas desde el propio dominio.
- Un "corte incluido" que no era cierto estaba en todo el sitio; se quitó.
- Un patrón de validación inválido en el teléfono bloqueaba el envío del formulario. Después se agregaron eventos `intento_envio`/`error_envio` para que un bug así se vea en los datos en vez de perder leads en silencio.
- Una auditoría recomendó "crear ficha de Google" cuando ya existía: preguntar antes de recomendar.

## polarizadoguatemala.com — polarizado de carros

**Hueco:** nadie publicaba precio por modelo ni garantía por escrito.

**Qué se hizo**
- Precio por **tipo de carrocería** (sedán, SUV, SUV 3 filas, pickup, van), que es lo que realmente cambia el costo, aplicado a 368 modelos. Agrupar por la variable real permite contenido honesto sin inventar diferencias.
- 36 hubs por marca, 6 guías (precios, legalidad, tonos, nano cerámica vs carbón, parabrisas, garantía), `llms.txt` generado desde los mismos datos.
- **Ficha de datos y comparación con modelos hermanos** en cada página de modelo ("el Corolla cuesta lo mismo que el Yaris porque comparten carrocería; el RAV4 es SUV y tiene otra tarifa").
- Ángulo de seguridad planteado con honestidad: "que desde afuera no vean tu celular", no "evita robos".
- Resultado técnico al lanzar: Lighthouse móvil SEO 100, accesibilidad 100, buenas prácticas 100, rendimiento 94. Home y guía de precios indexadas el mismo día de solicitar indexación.

**Errores que se corrigieron**
- En Next.js, las guías y hubs no tenían `og:image` porque su `openGraph` reemplazaba el del layout.
- Meta description de 191 caracteres en una guía (se cortaba).
- Contraste insuficiente en un botón y salto de h2 a h4 en el footer.
- El sitemap se envió como `sitemap.xml` en una propiedad de dominio y Search Console lo rechazó: hay que poner la URL completa.

## Patrón común

1. Encontrar lo que nadie publica (precio, garantía) y publicarlo.
2. Una página por entidad con ese dato + hubs + guías de preguntas.
3. Técnico impecable desde el día uno.
4. Ficha de Google y entidad consistente.
5. Search Console por API y ajustar al lenguaje real cada pocas semanas.
6. Nunca prometer lo que el dueño no confirmó.
