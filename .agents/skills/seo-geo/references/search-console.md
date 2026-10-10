# Search Console: indexar, medir e iterar

## Puesta en marcha

1. **Propiedad de dominio** (recomendada): verifica `sc-domain:dominio.com` con un registro TXT en el DNS. Cubre `www`, sin `www`, `http` y `https`.
2. **Enviar el sitemap.** En una propiedad de dominio el campo **no** muestra el prefijo de la URL: hay que escribir la URL completa `https://dominio.com/sitemap.xml`. Escribir solo `sitemap.xml` da "Invalid sitemap address".
3. **"Couldn't fetch" con "Last read" vacío** justo después de enviarlo casi siempre significa que Google aún no lo intentó. Antes de cambiar nada, verifica que el sitemap responda 200, sea XML válido y que Googlebot no esté bloqueado (ver `tecnico.md` → verificación). Si después de 48 h sigue igual, quítalo y reenvíalo.
4. **Inspección de URL → Solicitar indexación** para la home y 3-5 páginas clave (guía principal, un hub, una entidad popular). En sitios nuevos, es lo que acelera la primera indexación: en un caso real la home y la guía de precios aparecieron "Submitted and indexed" el mismo día.
5. **Bing Webmaster Tools:** importa la propiedad desde Search Console y envía el mismo sitemap. Bing alimenta la búsqueda de ChatGPT y Copilot (ver `geo.md`).

## Acceso por API (cuenta de servicio)

Permite que el agente saque reportes sin entrar al panel:

1. En Google Cloud, crea un proyecto, habilita la **Google Search Console API** y crea una **cuenta de servicio**. Descarga su llave JSON.
2. En Search Console → Configuración → Usuarios y permisos, agrega el correo de la cuenta de servicio (`...@...iam.gserviceaccount.com`) con permiso **Restringido** (solo lectura basta para reportes; **Completo** si quieres enviar sitemaps por API).
3. Guarda la llave en `.secrets/gsc-service-account.json` y asegúrate de que `.secrets/` esté en `.gitignore`. Nunca la subas al repo ni la pegues en el chat.
4. `pip install google-api-python-client google-auth`
5. Usa `scripts/gsc.py`:

```bash
python3 scripts/gsc.py --site sc-domain:dominio.com sitemaps
python3 scripts/gsc.py --site sc-domain:dominio.com inspect https://dominio.com/
python3 scripts/gsc.py --site sc-domain:dominio.com performance 28
python3 scripts/gsc.py --site sc-domain:dominio.com queries 28 50
python3 scripts/gsc.py --site sc-domain:dominio.com pages 28 50
python3 scripts/gsc.py --site sc-domain:dominio.com opportunities 28
```

Una misma cuenta de servicio sirve para varios sitios: solo hay que agregarla como usuario en cada propiedad.

## Calendario realista

| Cuándo | Qué esperar |
|---|---|
| Día 0-3 | Home y páginas solicitadas indexadas |
| Semana 1-2 | Sitemap leído; empiezan a indexarse las programáticas |
| Semana 2-4 | Primeras impresiones y consultas en el reporte de rendimiento |
| Mes 2-3 | Posiciones más estables; ya hay datos para optimizar |

## El ciclo de mejora (cada 2-4 semanas)

1. **Consultas con muchas impresiones y CTR bajo** (`opportunities`): el sitio aparece pero no convence. Casi siempre el título o la descripción no usan las palabras de la consulta. Caso real: la gente buscaba "copia de llave con chip" y el sitio decía "duplicado"; se agregó "copia" y "chip" a título, H1, descripción, FAQ y schema.
2. **Consultas en posición 5-20**: están cerca. Refuerza esa página: dato concreto en el título, FAQ con la frase literal, más enlaces internos hacia ella.
3. **Preguntas literales en las consultas** ("¿el mazda bt 50 2017 usa chip?"): conviértelas en FAQ de la página correspondiente.
4. **Varias páginas compitiendo por la misma consulta**: crea o refuerza un hub, o diferencia las páginas.
5. **Páginas "Discovered/Crawled – currently not indexed"**: contenido muy parecido entre páginas o poco valor propio. Agrega datos únicos (ver `contenido.md`) antes de pedir reindexación.

Registra cada cambio con su fecha (en el commit o en `TASKS.md`) para poder relacionarlo con la curva de clics.
