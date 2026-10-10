#!/usr/bin/env bash
# Avisa a Bing (y demás motores con IndexNow) que hay URLs nuevas o cambiadas.
# Uso: bash docs/indexnow.sh                 -> envía todas las URLs del sitemap
#      bash docs/indexnow.sh /ruta-1/ /ruta-2/ -> envía solo esas rutas
# Correr después de que GitHub Pages publique el cambio.
set -euo pipefail
HOST="certimotors.com"
KEY="1420199db572b2d570d44f82129ae6c3"
if [ $# -gt 0 ]; then
  URLS=$(printf '"https://%s%s",' "$HOST" "$@")
else
  URLS=$(curl -s "https://$HOST/sitemap.xml" | grep -o '<loc>[^<]*' | sed 's/<loc>//' | sed 's/.*/"&",/' | tr -d '\n')
fi
curl -s -o /dev/null -w "IndexNow: HTTP %{http_code}\n" -X POST "https://api.indexnow.org/indexnow" \
  -H "Content-Type: application/json; charset=utf-8" \
  -d "{\"host\":\"$HOST\",\"key\":\"$KEY\",\"keyLocation\":\"https://$HOST/$KEY.txt\",\"urlList\":[${URLS%,}]}"
