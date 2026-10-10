# Contenido que merece rankear

## Principio

Google indexa y posiciona páginas que aportan algo que no está en otras páginas, incluidas las del mismo sitio. Los motores de IA citan pasajes que responden una pregunta completa con datos. Las dos cosas se logran igual: **datos concretos y verificables, organizados para responder preguntas reales.**

## Reglas de veracidad

- Separa lo **confirmado** de lo **supuesto** desde el inicio. Mantén en el código un solo lugar para precios, plazos, garantías y promesas (por ejemplo `lib/offer.ts`, `lib/pricing.ts`) con un comentario `PENDIENTE confirmar` donde aplique, y una lista en `TASKS.md` de lo que falta confirmar.
- No inventes especificaciones técnicas para dar variedad a páginas programáticas ("el Corolla 2019 usa chip tipo G"). Si no lo sabes, no lo digas: usa los datos que sí tienes (categoría, precio, comparación).
- Las promesas comerciales ("incluye corte", "a domicilio", "pagas al recibir", "aprobación en 10 minutos") generan reclamos si no se cumplen. En un caso real hubo que quitar un "corte incluido" falso de todo el sitio.
- Cuando el usuario pida un ángulo de marketing (por ejemplo "más seguro contra robos"), plantéalo con la afirmación que sí es cierta ("que desde afuera no vean tu celular") y no con la que no lo es ("evita que rompan el vidrio").

## Anatomía de una página de entidad

1. **H1** con la entidad: "Polarizado para Toyota Corolla".
2. **Lead** con el dato principal: precio desde/hasta, qué incluye, garantía.
3. **El cotizador o la acción** (precio exacto, solicitar, agendar) en la primera pantalla.
4. **Ficha de datos** visible (lista `dl`): categoría, qué incluye, precio por opción, garantía, extras.
5. **Tabla** de precios u opciones.
6. **Párrafo por categoría**: qué cambia de verdad para ese tipo de entidad.
7. **Comparación con entidades hermanas**, derivada de datos.
8. **FAQ** con la entidad en cada pregunta.
9. **Enlaces** al hub, hermanas y guías.

Los puntos 4, 6 y 7 son los que convierten una plantilla en contenido único sin inventar nada.

## FAQ que funcionan

- Pregunta con la **frase literal** que se busca: "¿Cuánto cuesta polarizar un carro en Guatemala?", "¿El Mazda BT-50 2017 usa chip en la llave?". Search Console muestra estas preguntas tal cual.
- Respuesta directa en la primera oración, con el número. Luego el contexto.
- 4-8 preguntas por página; no repitas las mismas 8 en 400 páginas sin variar.
- Marca con `FAQPage` solo si las preguntas están visibles en la página.

## Títulos y descripciones que consiguen clics

- **Título:** `[Servicio] [Entidad] en [Ubicación]: [dato diferenciador]` → "Polarizado Toyota Corolla en Guatemala: desde Q850". El dato (precio, "en 24 h", "sin fiador") es lo que hace clic.
- Pon primero lo que importa: si se corta, que se corte el final, no "Guatemala".
- **Descripción:** el dato completo + garantía o confianza + acción. "Precio de polarizado para Toyota Corolla: clásico Q850, carbón Q1,250, nano cerámica Q1,950. Garantía por escrito."
- Cuando haya datos de Search Console, reescribe usando las palabras de las consultas con más impresiones y CTR bajo.

## Guías

- Responde en el primer párrafo. La gente (y la IA) decide ahí si la página sirve.
- Una tabla vale más que tres párrafos cuando hay números.
- Fecha de actualización visible y en `dateModified`; actualízala solo cuando cambie el contenido.
- Enlaza a las páginas de entidad y al cotizador.
- En temas legales o regulatorios, cita la norma y aclara dónde se verificó; si no se pudo confirmar en fuente oficial, dilo.

## YMYL (dinero, salud, legal)

Para financiamiento, préstamos, seguros, salud o trámites legales, Google exige más señales de confianza (E-E-A-T):

- Quién es la empresa: razón social, dirección o zona de operación, teléfono, registro o supervisión si aplica.
- Costos totales y condiciones claras: tasa, plazo, cuota, comisiones, qué pasa si hay atraso. Un ejemplo numérico completo ("un iPhone de Q8,000 a 12 meses: cuota de QX, total QY").
- Requisitos exactos y tiempos reales.
- Política de privacidad y términos accesibles desde el footer.
- Sin promesas absolutas ("aprobación garantizada", "sin revisar buró", "sin intereses") si no son ciertas: además de SEO, es riesgo legal.
- Qué regulación aplica (protección al consumidor, supervisión financiera, avisos obligatorios de costo) depende del país y del tipo de empresa: no lo afirmes; recomienda validarlo con un abogado local y márcalo como pendiente.

## Marcas de terceros

Usar "iPhone", "Toyota" o "Samsung" de forma descriptiva para decir qué se vende o se repara es normal ("financiamiento de iPhone 15", "polarizado para Toyota Corolla"). No des a entender que el negocio es distribuidor, taller o socio autorizado si no lo es, no uses logos de la marca y evita dominios con la marca ajena.

## Contenido que no aporta (evitar)

- Párrafos de relleno con la keyword repetida.
- Textos generados que suenan igual en todas las páginas.
- Páginas de ubicación clonadas.
- Blogs genéricos sin relación con lo que vende el negocio ("10 consejos para cuidar tu carro" en un sitio de llaves) mientras faltan páginas de las entidades que sí se buscan.
