#!/usr/bin/env python3
"""
Auditoría on-page de un sitio en vivo. Solo usa la librería estándar.

Revisa por URL: código HTTP, título (largo), meta description (largo),
canonical (presente y apuntando a sí misma), cantidad de <h1>, JSON-LD
(tipos y si es parseable), og:image, noindex y lang.

Uso:
  python3 audit_pages.py https://dominio.com                  # home + muestra del sitemap
  python3 audit_pages.py https://dominio.com --sample 30      # tamaño de muestra
  python3 audit_pages.py https://dominio.com /ruta-1 /ruta-2  # rutas específicas
  python3 audit_pages.py https://dominio.com --all            # todo el sitemap (lento)

Sale con código 1 si encuentra problemas.
"""
import html
import json
import random
import re
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET

UA = "Mozilla/5.0 (compatible; seo-geo-audit/1.0)"
TITLE_MAX = 60
DESC_MIN, DESC_MAX = 70, 160


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status, r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, ""


def sitemap_urls(base):
    status, body = fetch(base.rstrip("/") + "/sitemap.xml")
    if status != 200 or not body:
        return []
    root = ET.fromstring(body.encode())
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    locs = [e.text.strip() for e in root.findall(".//s:loc", ns) if e.text]
    # Índice de sitemaps: baja un nivel.
    if root.tag.endswith("sitemapindex"):
        out = []
        for sm in locs:
            st, b = fetch(sm)
            if st == 200:
                r2 = ET.fromstring(b.encode())
                out += [e.text.strip() for e in r2.findall(".//s:loc", ns) if e.text]
        return out
    return locs


def meta(h, attr, name):
    m = re.search(rf'<meta[^>]+{attr}="{re.escape(name)}"[^>]*content="([^"]*)"', h, re.I) or re.search(
        rf'<meta[^>]+content="([^"]*)"[^>]*{attr}="{re.escape(name)}"', h, re.I
    )
    return html.unescape(m.group(1)) if m else None


def audit(url):
    status, h = fetch(url)
    issues = []
    if status != 200:
        return {"url": url, "status": status, "issues": [f"HTTP {status}"]}

    t = re.search(r"<title[^>]*>(.*?)</title>", h, re.S | re.I)
    title = html.unescape(t.group(1).strip()) if t else ""
    if not title:
        issues.append("sin <title>")
    elif len(title) > TITLE_MAX:
        issues.append(f"título largo ({len(title)} > {TITLE_MAX})")

    desc = meta(h, "name", "description") or ""
    if not desc:
        issues.append("sin meta description")
    elif not DESC_MIN <= len(desc) <= DESC_MAX:
        issues.append(f"description de {len(desc)} caracteres (ideal {DESC_MIN}-{DESC_MAX})")

    c = re.search(r'<link[^>]+rel="canonical"[^>]+href="([^"]+)"', h, re.I) or re.search(
        r'<link[^>]+href="([^"]+)"[^>]+rel="canonical"', h, re.I
    )
    canonical = c.group(1) if c else None
    if not canonical:
        issues.append("sin canonical")
    elif canonical.rstrip("/") != url.rstrip("/"):
        issues.append(f"canonical apunta a otra URL: {canonical}")

    h1 = len(re.findall(r"<h1[\s>]", h, re.I))
    if h1 != 1:
        issues.append(f"{h1} <h1>")

    types, bad = [], 0
    for block in re.findall(r'<script[^>]+application/ld\+json[^>]*>(.*?)</script>', h, re.S | re.I):
        try:
            data = json.loads(block)
            items = data if isinstance(data, list) else data.get("@graph", [data])
            types += [str(i.get("@type")) for i in items if isinstance(i, dict)]
        except json.JSONDecodeError:
            bad += 1
    if not types:
        issues.append("sin JSON-LD")
    if bad:
        issues.append(f"{bad} bloque(s) JSON-LD inválido(s)")

    if not meta(h, "property", "og:image"):
        issues.append("sin og:image")

    robots = meta(h, "name", "robots") or ""
    if "noindex" in robots.lower():
        issues.append("noindex")

    if not re.search(r"<html[^>]+lang=", h, re.I):
        issues.append("sin lang en <html>")

    return {"url": url, "status": status, "title": title, "title_len": len(title), "desc_len": len(desc), "h1": h1, "schema": types, "issues": issues}


def main():
    args = sys.argv[1:]
    if not args or args[0].startswith("-"):
        print(__doc__)
        sys.exit(2)
    base = args[0].rstrip("/")
    sample = 15
    if "--sample" in args:
        sample = int(args[args.index("--sample") + 1])
    paths = [a for a in args[1:] if a.startswith("/")]

    if paths:
        urls = [base + p for p in paths]
    else:
        all_urls = sitemap_urls(base)
        if not all_urls:
            print("No se pudo leer /sitemap.xml; audito solo la home.")
        if "--all" in args:
            urls = all_urls or [base + "/"]
        else:
            rest = [u for u in all_urls if u.rstrip("/") != base]
            urls = [base + "/"] + random.sample(rest, min(sample, len(rest)))
        print(f"Sitemap: {len(all_urls)} URLs. Auditando {len(urls)}.\n")

    with_issues = 0
    titles = {}
    for u in urls:
        r = audit(u)
        titles.setdefault(r.get("title"), []).append(u)
        mark = "OK " if not r["issues"] else "!! "
        with_issues += bool(r["issues"])
        print(f"{mark}{u}")
        if r.get("title"):
            print(f"    título ({r['title_len']}): {r['title']}")
            print(f"    description: {r['desc_len']} · h1: {r['h1']} · schema: {', '.join(r['schema']) or '—'}")
        for i in r["issues"]:
            print(f"    - {i}")

    dupes = {t: us for t, us in titles.items() if t and len(us) > 1}
    for t, us in dupes.items():
        print(f"\n!! Título repetido en {len(us)} páginas: {t}")

    print(f"\n{len(urls) - with_issues}/{len(urls)} páginas sin problemas.")
    sys.exit(1 if with_issues or dupes else 0)


if __name__ == "__main__":
    main()
