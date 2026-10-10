#!/usr/bin/env python3
"""
Search Console por API con una cuenta de servicio.

Requisitos:
  pip install google-api-python-client google-auth
  Llave JSON de la cuenta de servicio (no la subas al repo).
  La cuenta de servicio agregada como usuario en la propiedad de Search Console.

Uso:
  python3 gsc.py --site sc-domain:dominio.com [--key ruta.json] <comando> [args]

Comandos:
  performance [días]            clics, impresiones, CTR y posición (default 28)
  queries [días] [límite]       top consultas
  pages [días] [límite]         top páginas
  opportunities [días]          consultas con muchas impresiones y CTR bajo
  inspect <url>                 estado de indexación de una URL
  sitemaps                      sitemaps enviados y su estado
  submit-sitemap <url>          (re)enviar un sitemap (requiere permiso completo)

--site también se puede pasar con la variable GSC_SITE, y --key con GSC_KEY.
Por defecto la llave se busca en .secrets/gsc-service-account.json del directorio actual.
"""
import json
import os
import sys
from datetime import date, timedelta
from pathlib import Path


def parse_args(argv):
    site = os.environ.get("GSC_SITE")
    key = os.environ.get("GSC_KEY", ".secrets/gsc-service-account.json")
    rest = []
    i = 0
    while i < len(argv):
        if argv[i] == "--site":
            site = argv[i + 1]
            i += 2
        elif argv[i] == "--key":
            key = argv[i + 1]
            i += 2
        else:
            rest.append(argv[i])
            i += 1
    return site, key, rest


def service(key):
    from google.oauth2 import service_account
    from googleapiclient.discovery import build

    if not Path(key).exists():
        sys.exit(f"No encuentro la llave en {key}. Usa --key o GSC_KEY.")
    creds = service_account.Credentials.from_service_account_file(key, scopes=["https://www.googleapis.com/auth/webmasters"])
    return build("searchconsole", "v1", credentials=creds, cache_discovery=False)


def window(days):
    # Search Console tarda ~2-3 días en consolidar datos.
    end = date.today() - timedelta(days=2)
    return str(end - timedelta(days=int(days))), str(end)


def query(svc, site, days, dims, limit=25):
    start, end = window(days)
    body = {"startDate": start, "endDate": end, "dimensions": dims, "rowLimit": int(limit)}
    return svc.searchanalytics().query(siteUrl=site, body=body).execute().get("rows", [])


def cmd_performance(svc, site, days=28):
    rows = query(svc, site, days, [])
    if not rows:
        print("Sin datos todavía (normal en sitios de menos de 2-4 semanas).")
        return
    r = rows[0]
    print(f"Últimos {days} días: {r['clicks']} clics · {r['impressions']} impresiones · CTR {r['ctr'] * 100:.2f}% · posición {r['position']:.1f}")


def _print_rows(rows):
    if not rows:
        print("Sin datos todavía.")
    for r in rows:
        print(f"{r['clicks']:>5} clics | {r['impressions']:>6} impr | CTR {r['ctr'] * 100:5.1f}% | pos {r['position']:5.1f} | {r['keys'][0]}")


def cmd_queries(svc, site, days=28, limit=25):
    _print_rows(query(svc, site, days, ["query"], limit))


def cmd_pages(svc, site, days=28, limit=25):
    _print_rows(query(svc, site, days, ["page"], limit))


def cmd_opportunities(svc, site, days=28):
    rows = query(svc, site, days, ["query", "page"], 500)
    if not rows:
        print("Sin datos todavía.")
        return
    median = sorted(r["impressions"] for r in rows)[len(rows) // 2]
    opp = [r for r in rows if r["impressions"] >= max(median, 10) and r["ctr"] < 0.03 and r["position"] <= 20]
    opp.sort(key=lambda r: r["impressions"], reverse=True)
    print("Consultas visibles que casi no reciben clics: ajusta título, descripción, H1 y FAQ de esa página a estas palabras.\n")
    for r in opp[:30]:
        q, page = r["keys"]
        print(f"{r['impressions']:>6} impr | CTR {r['ctr'] * 100:4.1f}% | pos {r['position']:5.1f} | {q}\n         → {page}")
    if not opp:
        print("No hay oportunidades claras con los datos actuales.")


def cmd_inspect(svc, site, url):
    resp = svc.urlInspection().index().inspect(body={"inspectionUrl": url, "siteUrl": site}).execute()
    idx = resp.get("inspectionResult", {}).get("indexStatusResult", {})
    keep = ["verdict", "coverageState", "robotsTxtState", "indexingState", "lastCrawlTime", "pageFetchState", "googleCanonical", "userCanonical"]
    print(json.dumps({k: idx.get(k) for k in keep if k in idx}, indent=2, ensure_ascii=False))


def cmd_sitemaps(svc, site):
    for s in svc.sitemaps().list(siteUrl=site).execute().get("sitemap", []):
        contents = s.get("contents", [{}])
        submitted = sum(int(c.get("submitted", 0)) for c in contents)
        print(f"{s.get('path')} | enviado: {s.get('lastSubmitted')} | leído: {s.get('lastDownloaded') or 'todavía no'} | URLs: {submitted} | errores: {s.get('errors', 0)}")


def cmd_submit_sitemap(svc, site, url):
    svc.sitemaps().submit(siteUrl=site, feedpath=url).execute()
    print(f"Sitemap enviado: {url}")


COMMANDS = {
    "performance": cmd_performance,
    "queries": cmd_queries,
    "pages": cmd_pages,
    "opportunities": cmd_opportunities,
    "inspect": cmd_inspect,
    "sitemaps": cmd_sitemaps,
    "submit-sitemap": cmd_submit_sitemap,
}

if __name__ == "__main__":
    site, key, rest = parse_args(sys.argv[1:])
    if not rest or rest[0] not in COMMANDS or not site:
        print(__doc__)
        sys.exit(1)
    COMMANDS[rest[0]](service(key), site, *rest[1:])
