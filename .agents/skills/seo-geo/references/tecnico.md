# SEO técnico: checklist y trampas conocidas

## Contenido
1. Checklist
2. Schema (JSON-LD)
3. Rendimiento
4. Trampas conocidas por framework
5. Cómo verificar en vivo

## 1. Checklist

**Dominio y rastreo**
- [ ] Un solo host canónico. Redirige `www` → sin `www` (o al revés) con 301/308, y `http` → `https`.
- [ ] `<link rel="canonical">` absoluto en cada página, incluida la home (es la que más se olvida).
- [ ] `robots.txt` responde 200, no bloquea páginas indexables y declara `Sitemap: https://dominio/sitemap.xml`.
- [ ] `sitemap.xml` responde 200 con `application/xml`, contiene solo URLs canónicas indexables, y `lastmod` estable: la fecha real del último cambio de contenido, no `new Date()` en cada request. Un `lastmod` que cambia en cada rastreo le dice a Google que todo cambió siempre y pierde valor como señal.
- [ ] URLs inexistentes devuelven 404 real (no 200 con "no encontrado").
- [ ] Nada indexable tiene `noindex` por error (revisa entornos de preview que se filtran a producción).

**En cada página**
- [ ] `<title>` único, ≤ 60 caracteres, con la keyword y el dato diferenciador al inicio. Si el sitio agrega un sufijo de marca (`| Marca`), quítalo en las páginas donde el título se cortaría.
- [ ] Meta description única, 120-155 caracteres, con el dato concreto (precio, plazo) y una razón para hacer clic.
- [ ] Un `<h1>`. Encabezados en orden (h1 → h2 → h3), sin saltar a h4 en el footer.
- [ ] `og:title`, `og:description`, `og:image` (1200×630) y `twitter:card` en todas las páginas.
- [ ] `lang` correcto en `<html>` (`es-GT`, `es-MX`, etc.).
- [ ] Imágenes con `alt` descriptivo y dimensiones declaradas (evita CLS).
- [ ] Contraste de texto suficiente (Lighthouse lo marca y afecta accesibilidad).

**Móvil y conversión**
- [ ] El formulario o la acción principal aparece en la primera pantalla en móvil.
- [ ] Barra fija con la acción principal (cotizar / WhatsApp / solicitar) en móvil.
- [ ] Eventos del embudo medidos: vio precio, eligió opción, intentó enviar, error al enviar, envió, clic en WhatsApp. Sin `intento_envio` y `error_envio` no sabes si pierdes leads por un bug.
- [ ] Si falla la base de datos o el correo, el lead no se pierde (log + notificación alterna).

## 2. Schema (JSON-LD)

Usa el que corresponda; no marques lo que no está en la página.

| Página | Schema |
|---|---|
| Home de negocio local | `LocalBusiness` (o subtipo: `AutomotiveBusiness`, `FinancialService`, `FoodEstablishment`…) con `name`, `url`, `telephone`, `priceRange`, `areaServed`, `image`, `sameAs` (ficha de Google, redes), `hasMap` |
| Home de empresa no local | `Organization` + `WebSite` |
| Servicio / entidad con precio | `Service` con `offers` (`Offer` o `AggregateOffer` con `lowPrice`, `highPrice`, `priceCurrency`) y `provider` apuntando al `@id` del negocio |
| Producto (e-commerce) | `Product` con `offers`, y `aggregateRating` **solo** si hay reseñas reales visibles |
| Hub de categoría | `ItemList` + `BreadcrumbList` |
| Guía | `Article` con `dateModified`, `author`/`publisher` = la organización |
| FAQ visible | `FAQPage` (Google ya casi no muestra el resultado enriquecido, pero los motores de IA sí leen las preguntas) |
| Todas las internas | `BreadcrumbList` |

Usa un `@id` estable para el negocio (`https://dominio/#business`) y referéncialo desde `Service`, `Article`, etc., para que todo apunte a la misma entidad.

Valida con el [Rich Results Test](https://search.google.com/test/rich-results) y con `scripts/audit_pages.py` (verifica que el JSON-LD sea parseable).

## 3. Rendimiento

Objetivo móvil: LCP < 2.5 s, CLS < 0.1, INP < 200 ms.

- Sirve las fuentes desde el propio dominio (en Next.js, `next/font`). Una hoja de Google Fonts externa bloquea el render: en un caso real FCP y LCP estaban atascados en 2.9 s con TBT y CLS en cero, y la hoja externa era el paso que bloqueaba.
- Imágenes en WebP/AVIF, con tamaño declarado, `loading="lazy"` excepto la del hero.
- Evita animaciones de entrada largas en el contenido principal: empeoran el Speed Index.
- Prefiere páginas estáticas o ISR para las programáticas.
- Mide con Lighthouse (`npx lighthouse <url> --only-categories=performance,seo,accessibility,best-practices`) o PageSpeed Insights. Si la API de PageSpeed agota cuota, Lighthouse local da el mismo diagnóstico.

## 4. Trampas conocidas por framework

**Next.js (App Router)**
- `metadata.openGraph` de una página **reemplaza** el de `layout.tsx`, no lo combina. Si una página define `openGraph: { title, description }` sin `images`, se queda sin `og:image`. Repite las imágenes en cada `openGraph` o usa un helper común.
- `alternates.canonical` tampoco se hereda de forma útil: defínelo en cada página.
- Las variables `NEXT_PUBLIC_*` se fijan al compilar: después de cambiarlas en el hosting hay que redesplegar.
- Usa `app/sitemap.ts` y `app/robots.ts`; fija `lastModified` a una constante de fecha de contenido.
- En `generateMetadata` de páginas dinámicas, construye títulos con candidatos de mayor a menor longitud y elige el primero que quepa en 60 caracteres.

**Vercel**
- Al agregar el dominio, revisa que el certificado HTTPS se emita; si tarda, `vercel certs issue dominio www.dominio`.
- Revisa que el redeploy posterior a cambiar variables aparezca como el más reciente.

**WordPress**
- Un plugin SEO (Yoast, Rank Math) cubre títulos, canonical y sitemap, pero revisa que no indexe páginas de etiquetas, autores y adjuntos vacías.

**Sitios hechos con constructores (Wix, Webflow, Shopify)**
- Revisa que cada página tenga título y descripción propios (por defecto suelen repetir los del sitio) y que el dominio principal esté marcado como primario.

## 5. Cómo verificar en vivo

Después de cada despliegue:

```bash
# Códigos y redirecciones
curl -sI https://dominio/ | head -1
curl -sI https://www.dominio/ | grep -i location
curl -s -o /dev/null -w "%{http_code}\n" https://dominio/no-existe

# Rastreo
curl -s https://dominio/robots.txt
curl -s https://dominio/sitemap.xml | grep -c "<loc>"

# Auditoría on-page de varias URLs
python3 scripts/audit_pages.py https://dominio --sample 20
```

Para descartar bloqueos al bot, repite el `curl` con `-A "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"`.
