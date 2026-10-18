#!/usr/bin/env bash
# usage: smoke.sh <ip>  — hits each public URL pinned to that origin IP (bypasses Cloudflare)
IP=$1
URLS="https://skipy.online/ https://skipy.online/health https://skipy.online/api/v1/health https://skipy.online/manager/ https://skipy.online/admin/ https://skipy.online/login
https://skipy.io/ https://hiddenbeer.com/ https://hiddenbeer.com/health https://hiddenbeer.com/api/v1/health
https://househunter.immo/ https://househunter.immo/health https://househunter.immo/api/health
https://lovemail.online/ https://lovemail.online/health https://lovemail.online/version
https://cabinet-flow.com/ https://cabinet-flow.com/api/health https://cabinet-flow.com/api/waitlist/count
https://wtechitsolutions.com/ https://wtechitsolutions.com/demo/dfpro/ http://$IP:6040/ http://$IP:6040/api/health"
for u in $URLS; do
  h=$(echo "$u" | sed -E 's#https?://([^/:]+).*#\1#'); port=443; [[ $u == http://* ]] && port=${u##*:}; port=${port%%/*}
  printf "%-48s %s\n" "$u" "$(curl -sk -o /dev/null -w '%{http_code} %{time_total}s' -m 20 --resolve "$h:$port:$IP" "$u")"
done
