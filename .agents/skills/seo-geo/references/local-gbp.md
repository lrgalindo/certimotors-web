# Presencia local: Google Business Profile

Para búsquedas con intención local ("polarizado cerca de mí", "cerrajero zona 10", "meseros para eventos guatemala"), el bloque de mapas aparece arriba de los resultados orgánicos. Ahí se rankea con la ficha de Google, no con el sitio. Si el negocio atiende en una zona, la ficha es prioridad alta.

Antes de recomendar crearla, pregunta si ya existe. Si existe, el trabajo es optimizarla y enlazarla.

## Kit para el dueño

Entrega un documento (por ejemplo `docs/google-business-profile.md`) con estos bloques listos para copiar, marcando con ⚠️ lo que dependa de datos sin confirmar:

**Nombre.** El nombre real del negocio, como aparece en el rótulo o la factura. Agregar palabras clave ("Cerrajería Rápida Barata Zona 10") viola las políticas y es causa común de suspensión.

**Categoría principal.** La más específica que exista para el servicio. Pide al dueño que escriba el término en el buscador de categorías y elija la más cercana; los nombres exactos varían por idioma. Categorías secundarias solo si realmente ofrece ese servicio.

**Sitio web con UTM**, para medir lo que llega desde la ficha:
```
https://dominio/?utm_source=google&utm_medium=organic&utm_campaign=gbp
```

**Zona de servicio.** Si va a domicilio: "empresa de servicio a domicilio", dirección oculta y solo las zonas donde realmente llega. Si tiene local: dirección exacta y horario real.

**Descripción** (máx. 750 caracteres): qué hace, dónde, el diferenciador (precio publicado, garantía, rapidez), y la invitación a cotizar en el sitio. Sin URLs ni promociones temporales. Cuenta los caracteres antes de entregarla.

**Servicios con precio "desde"**, los mismos del sitio.

**Atributos:** solo los ciertos (acepta tarjeta, cita previa, a domicilio…).

**Fotos:** logo, portada y 10+ fotos reales (trabajos terminados, antes/después, equipo, local o vehículo). Subir 2-3 nuevas por semana el primer mes. Las fotos reales son la señal que más diferencia una ficha nueva.

**Primera publicación:** el diferenciador + precio "desde" + botón al sitio.

**Mensaje para pedir reseñas** por WhatsApp después de cada servicio, con el enlace corto de reseña de la ficha. Nunca reseñas falsas ni pagadas, ni condicionar descuentos a reseñas positivas: viola las políticas.

## Enlazar la ficha en el sitio

Cuando el dueño comparta el enlace de la ficha (idealmente el de Maps con `?cid=`, que es estable):

```ts
// lib/site.ts
export const GOOGLE_BUSINESS_URL = "https://maps.google.com/?cid=XXXXXXXXXXXX";

// schema del negocio
{
  "@type": "LocalBusiness",
  "@id": `${SITE_URL}/#business`,
  hasMap: GOOGLE_BUSINESS_URL,
  sameAs: [GOOGLE_BUSINESS_URL, /* redes reales */],
}
```

Y un enlace visible "Ver reseñas en Google" en el footer o la página de garantía.

## NAP consistente

Nombre, dirección (o zona) y teléfono idénticos en el sitio, la ficha, redes y directorios. Variaciones ("Polarizado GT" vs "Polarizado Guatemala") diluyen la entidad.

## Directorios y menciones

Prepara textos cortos (nombre, descripción de 1-2 oraciones, servicios, enlace) para que el dueño publique en directorios locales relevantes, páginas de Facebook, Instagram, grupos del nicho y marketplaces. No publiques en nombre del usuario sin su permiso.
