#!/bin/bash
# Read-only server inventory for the migration status report; prints "### <section>" blocks, no secrets.
# Usage: for s in OLD NEW; do ssh $s "bash -s" < inventory.sh > $s.txt; done   (then diff / render side by side)
v(){ "$@" 2>&1 | head -1; }
echo "### host"; hostname; hostname -f 2>/dev/null; curl -s -4 -m5 ifconfig.me; echo
. /etc/os-release; echo "$PRETTY_NAME"; uname -r; nproc; free -h | awk '/Mem/{print "RAM "$2" used "$3}; /Swap/{print "Swap "$2" used "$3}'; df -h / | tail -1; uptime -p; timedatectl show -p Timezone --value
echo "### versions"
echo "nginx: $(nginx -v 2>&1 | cut -d/ -f2)"
echo "docker: $(docker --version 2>/dev/null | awk '{print $3}' | tr -d ,)"
echo "compose: $(docker compose version --short 2>/dev/null)"
echo "mongod: $(mongod --version 2>/dev/null | awk 'NR==1{print $3}')"
echo "mongosh: $(mongosh --version 2>/dev/null)"
echo "mongodump: $(mongodump --version 2>/dev/null | awk 'NR==1{print $3}')"
echo "redis: $(redis-server --version 2>/dev/null | awk '{print $3}' | cut -d= -f2)"
echo "node: $(node -v 2>/dev/null)"
echo "npm: $(npm -v 2>/dev/null)"
echo "pnpm: $(pnpm -v 2>/dev/null)"
echo "python3: $(python3 -V 2>&1 | awk '{print $2}')"
echo "uv: $(uv --version 2>/dev/null | awk '{print $2}')"
echo "java: $(java -version 2>&1 | awk -F'"' 'NR==1{print $2}')"
echo "certbot: $(certbot --version 2>/dev/null | awk '{print $2}')"
echo "postfix: $(postconf -h mail_version 2>/dev/null)"
echo "openssl: $(openssl version | awk '{print $2}')"
echo "fail2ban: $(fail2ban-client version 2>/dev/null)"
echo "ufw: $(ufw version 2>/dev/null | awk 'NR==1{print $2}')"
echo "php: $(php -v 2>/dev/null | awk 'NR==1{print $2}')"
echo "apache2: $(apache2 -v 2>/dev/null | awk -F/ 'NR==1{print $2}' | awk '{print $1}')"
echo "mysql: $(mysqld --version 2>/dev/null | awk '{print $3}')"
echo "### srv"; for d in /srv/* /var/www/* /opt/*; do [ -d "$d" ] && echo "$d $(du -sh --exclude=node_modules --exclude=.next --exclude=.venv "$d" 2>/dev/null | cut -f1)"; done
echo "### systemd"; systemctl list-units --type=service --all --no-legend --plain 2>/dev/null | awk '{print $1,$3,$4}' | grep -E "nginx|mongod|redis|docker|postfix|fail2ban|househunter|lovemail|cabinetflow|movie|skipy|hiddenbeer|wtech|php|apache|mysql|certbot|mongodb-thp" 
echo "### unitfiles"; for u in $(systemctl list-unit-files --no-legend 2>/dev/null | awk '{print $1}' | grep -E "househunter|lovemail|cabinetflow|movie"); do echo "$u|$(systemctl is-enabled $u 2>/dev/null)|$(systemctl show -p WorkingDirectory --value $u)|$(systemctl show -p User --value $u)|$(systemctl show -p ExecStart --value $u | sed -E 's/.*path=([^ ;]+).*argv\[\]=([^;]*);.*/\2/' | cut -c1-140)"; done
echo "### docker"; docker ps -a --format '{{.Names}}|{{.Image}}|{{.Status}}|{{.Ports}}' 2>/dev/null
echo "### listen"; ss -ltnpH 2>/dev/null | awk '{print $4, $6}' | sed -E 's/users:\(\("([^"]+)".*/\1/' | sort -u -t' ' -k1,1
echo "### vhosts"; for f in /etc/nginx/sites-enabled/*; do echo "$(basename $f)|$(grep -hoE 'server_name [^;]+' $f | sort -u | sed 's/server_name //' | tr '\n' ' ')|$(grep -hoE 'listen [^;]+' $f | sed 's/listen //' | sort -u | tr '\n' ',')|$(grep -hoE '(proxy_pass|root|alias) [^;]+' $f | sort -u | tr '\n' ',' | cut -c1-200)"; done
echo "### nginxconfd"; ls /etc/nginx/conf.d/
echo "### certs"; for c in /etc/letsencrypt/live/*/cert.pem /etc/ssl/*/*.pem /etc/ssl/*/*.crt; do [ -f "$c" ] && openssl x509 -in "$c" -noout >/dev/null 2>&1 && echo "$c|$(openssl x509 -in $c -noout -subject 2>/dev/null | sed 's/.*CN *= *//')|$(openssl x509 -in $c -noout -enddate | cut -d= -f2)|$(openssl x509 -in $c -noout -issuer | sed -E 's/.*O *= *([^,]+).*/\1/')"; done | grep -v "/etc/ssl/certs/"
echo "### cron"; crontab -l 2>/dev/null | grep -vE '^\s*$' | grep -E '^[0-9*#@]' | grep -vE '^#( |=|-|$)' | grep -v '^#[A-Z ]*$' ; ls /etc/cron.d
echo "### ufw"; ufw status 2>/dev/null | sed 1,4d | grep -v '(v6)'
echo "### f2b"; fail2ban-client status 2>/dev/null | grep "Jail list" | cut -d: -f2
echo "### mongo"; ADM=""; [ -f /root/.mongo-admin.env ] && . /root/.mongo-admin.env && ADM="$MONGO_ADMIN_URI"; mongosh --quiet ${ADM:+"$ADM"} --eval 'db.adminCommand({listDatabases:1}).databases.filter(d=>!["admin","local","config"].includes(d.name)).forEach(d=>{const x=db.getSiblingDB(d.name);let n=0;x.getCollectionNames().forEach(c=>{n+=x.getCollection(c).estimatedDocumentCount()});print(d.name+"|"+(d.sizeOnDisk/1048576).toFixed(1)+"MB|"+x.getCollectionNames().length+"|"+n)}); print("auth|"+(db.adminCommand({getCmdLineOpts:1}).parsed.security||{}).authorization)' 2>&1 | tail -20
echo "### backups"; for d in /srv/*/backups /srv/backup /srv/offsite /var/backups/mongo; do [ -d "$d" ] && echo "$d|$(du -sh $d 2>/dev/null | cut -f1)|$(find $d -type f | wc -l)|$(ls -t $d 2>/dev/null | head -1)"; done
echo "### mail"; postconf -h relayhost myhostname 2>/dev/null | tr '\n' ' '; echo; grep -E '^(MAIL_SERVER|MAIL_LOCATION|MAIL_IP|MAIL_APPS|MAIL_OPS|APP_DOMAINS|OPS_DOMAINS)=' /root/scripts/server.env 2>/dev/null | sed -E 's/@[^"]+/@…/'
echo "### scripts"; ls /root/scripts | grep -vE '\.bak|\.log$|^_archive' | tr '\n' ' '
echo "### standby"; for f in /srv/skipy/.env /srv/hiddenbeer/.env /srv/cabinetflow/backend/.env /var/www/cabinetflow/backend/.env; do [ -f $f ] && echo "$f|$(grep -c 'server-vps standby' $f)|$(grep -E '^(EMAILS_ENABLED|USE_REAL_SMS|VOUCHER_EXPIRING_EMAIL_ENABLED|SOCIAL_POSTING_ENABLED|APP_WAITLIST_SCANCRON)=' $f | tr '\n' ' ')"; done
echo "### appver"; for f in /srv/skipy/VERSION /srv/hiddenbeer/VERSION; do [ -f $f ] && echo "$f $(cat $f)"; done; docker inspect -f '{{.Name}} {{index .Config.Labels "org.opencontainers.image.version"}} {{.Created}}' $(docker ps -q) 2>/dev/null
for p in /srv/househunter /var/www/househunter /srv/lovemail /var/www/lovemail /srv/movie-helper /opt/movie-helper /srv/cabinetflow /var/www/cabinetflow /srv/wtech-website; do for j in package.json backend/package.json frontend/package.json frontend-next/package.json; do [ -f $p/$j ] && echo "$p/$j $(grep -m1 '"version"' $p/$j | tr -d ' ",' | cut -d: -f2)"; done; [ -f $p/backend/pyproject.toml ] && echo "$p/backend/pyproject.toml $(grep -m1 '^version' $p/backend/pyproject.toml)"; ls $p/backend/target/*.jar $p/backend/*.jar 2>/dev/null; done
