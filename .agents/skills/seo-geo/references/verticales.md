# Adaptar la estrategia según el tipo de proyecto

El método es el mismo; cambian las entidades, el hueco del nicho y el peso de cada fase.

## Servicio local con precio (cerrajería, polarizado, talleres, limpieza)

- **Entidades:** marca × modelo, tipo de servicio, tipo de vehículo o inmueble.
- **Hueco típico:** nadie publica precios ni garantías.
- **Prioridades:** páginas por entidad con precio exacto, hubs por marca, guía de precios, ficha de Google, reseñas.
- **Conversión:** cotizador sin pedir datos → precio → reserva por WhatsApp.

## Servicio a domicilio o bajo demanda (meseros para eventos, chefs, mudanzas, mecánico a domicilio)

- **Entidades:** tipo de evento o servicio × tamaño (meseros para boda, para 50 personas, para evento corporativo), zonas con cobertura real.
- **Hueco típico:** tarifas por hora o por persona, qué incluye, con cuánta anticipación reservar.
- **Prioridades:** páginas por tipo de servicio con tarifa y ejemplo de cálculo ("evento de 100 personas, 5 horas: X meseros, QY"), calculadora, guía "cuántos meseros necesito para N invitados", ficha de Google como servicio a domicilio con zonas.
- **Cuidado:** páginas por zona solo si cambia algo real (recargo por traslado, disponibilidad).

## Fintech / financiamiento (celulares a plazos, préstamos, crédito)

Es **YMYL** (dinero): Google exige más confianza y los errores tienen riesgo legal.

- **Entidades:** producto financiado (marca × modelo de celular), plazo, perfil del cliente (sin buró, sin tarjeta, trabajadores informales), requisitos.
- **Hueco típico:** cuota real, total a pagar, requisitos exactos, tiempo de aprobación.
- **Prioridades:**
  - Página por equipo: "Financiamiento iPhone 15 en Guatemala: cuota desde QX" con tabla por plazo (cuota, total, enganche).
  - Guía de requisitos, guía "cómo funciona", simulador de cuotas.
  - Página de la empresa: quién es, contacto, registro o supervisión si aplica, privacidad y términos.
- **Ficha de Google:** solo si hay punto de atención físico o zona de entrega definida; si es 100% en línea, la entidad se construye con redes, directorios, medios y reseñas en otras plataformas.
- **Reglas extra:** cada cifra debe venir de la tabla real de la empresa; muestra costo total y condiciones de atraso; nada de "aprobación garantizada" si no lo es. Schema `FinancialService` / `Service` con `offers`, sin inventar tasas.

## Marketplace o directorio (proveedores, profesionales, alquileres)

- **Entidades:** categoría × ubicación, perfiles de proveedores.
- **Prioridades:** hubs por categoría y ciudad con datos agregados reales (cuántos proveedores, rango de precio), perfiles con contenido propio (descripción, fotos, reseñas reales), `noindex` en filtros y búsquedas internas para no generar miles de URLs vacías.
- **Cuidado:** perfiles vacíos o duplicados degradan el sitio entero; indexa solo los que tengan contenido mínimo.

## E-commerce

- **Entidades:** producto, categoría, marca.
- **Prioridades:** fichas de producto con descripción propia (no la del fabricante), precio y disponibilidad en schema `Product`, categorías con texto útil, canonical en variantes (color/talla), guías de compra.
- **Cuidado:** paginación y filtros que generan URLs duplicadas; productos agotados (mantener la página con alternativas en vez de 404 si tiene tráfico).

## SaaS / software

- **Entidades:** casos de uso, industrias, integraciones, alternativas a competidores, plantillas.
- **Prioridades:** página por caso de uso e industria, páginas "alternativa a X" honestas, precios públicos, documentación indexable, comparativas.
- **GEO pesa mucho:** las recomendaciones de herramientas salen cada vez más de asistentes de IA; pasajes citables y menciones en terceros (reviews, comunidades) son clave.

## Proyecto sin ubicación ni catálogo (blog, medio, marca personal)

- **Entidades:** temas y preguntas.
- **Prioridades:** clusters temáticos (una guía pilar + artículos que la enlazan), autoría visible y verificable, actualización periódica.
