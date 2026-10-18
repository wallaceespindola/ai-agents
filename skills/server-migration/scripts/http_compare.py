"""Compare GET responses of the same public URLs on two origins (curl --resolve). Read-only, paced so fail2ban
(nginx-404: 20x404/60s, nginx-limit-req) never trips. Usage: compare.py <site>[,<site>...]"""
import os, collections, json, random, re, subprocess, sys, threading, time
from concurrent.futures import ThreadPoolExecutor

OLD, NEW = os.environ.get("OLD_IP", "194.31.150.176"), os.environ.get("NEW_IP", "82.180.155.136")
DIR = os.getcwd()  # results <site>.json land here
SCRATCH = os.environ.get("OPENAPI_DIR", DIR)  # holds oa-<app>.json (see SKILL.md phase 6)
SKIP = re.compile(r"webhook|callback|unsubscribe|verify|confirm|logout|cron|trigger|send|export|/auth|login|otp|"
                  r"password|reset|token|oauth|sse|/ws|events|stream|download|seed|debug|test-|reindex|sync|scrape|"
                  r"/admin|impersonat|delete|cancel|refund|checkout|payout|track|click|beacon|metrics/ingest", re.I)

def curl(url, ip):
    host = re.match(r"https?://([^/:]+)", url)[1]
    port = 443 if url.startswith("https") else int(re.match(r"https?://[^/]+:(\d+)", url)[1])
    r = subprocess.run(["curl", "-sk", "-m", "25", "-o", "/dev/null", "-w", "%{http_code} %{size_download} %{content_type}",
                        "--resolve", f"{host}:{port}:{ip}", url], capture_output=True, text=True)
    code, size, *ct = (r.stdout or "000 0").split(" ")
    return int(code), int(size), (ct[0] if ct else "")

def sitemap(site, cap):
    out = subprocess.run(["curl", "-sk", "-m", "30", "--resolve", f"{site}:443:{NEW}", f"https://{site}/sitemap.xml"],
                         capture_output=True, text=True).stdout
    locs = re.findall(r"<loc>([^<]+)</loc>", out)
    subs = [l for l in locs if l.endswith(".xml")]
    for s in subs[:5]:
        locs += re.findall(r"<loc>([^<]+)</loc>", subprocess.run(["curl", "-sk", "-m", "30", "--resolve", f"{site}:443:{NEW}", s],
                                                                capture_output=True, text=True).stdout)
    pages = sorted({l for l in locs if not l.endswith(".xml") and site in l})
    random.seed(7)
    return random.sample(pages, min(cap, len(pages)))

def openapi(fname, base):
    spec = json.load(open(f"{SCRATCH}/{fname}"))
    return [base + p for p, ops in spec["paths"].items() if "get" in ops and "{" not in p and not SKIP.search(p)]

SITES = {
    "househunter": lambda: ["https://househunter.immo/", "https://househunter.immo/robots.txt"] + sitemap("househunter.immo", 60)
                           + openapi("oa-hh.json", "https://househunter.immo/api"),
    "lovemail": lambda: ["https://lovemail.online/", "https://lovemail.online/health", "https://lovemail.online/version"] + sitemap("lovemail.online", 60),
    "cabinetflow": lambda: ["https://cabinet-flow.com/", "https://cabinet-flow.com/api/health", "https://cabinet-flow.com/rdv"] + sitemap("cabinet-flow.com", 60),
    "wtech": lambda: ["https://wtechitsolutions.com/", "https://www.wtechitsolutions.com/", "https://wtechitsolutions.com/demo/dfpro/"] + sitemap("wtechitsolutions.com", 80),
    "skipyio": lambda: ["https://skipy.io/", "https://www.skipy.io/"],
    "moviehelper": lambda: ["http://IP:6040/", "http://IP:6040/api/health"],
    "skipy": lambda: ["https://skipy.online/" + p for p in ["", "en", "fr", "nl", "pt", "pt-br", "es", "login", "register", "manager/", "admin/", "health", "en/support"]]
                     + openapi("oa-skipy.json", "https://skipy.online"),
    "hiddenbeer": lambda: ["https://hiddenbeer.com/" + p for p in ["", "en", "fr", "nl", "pt", "login", "health", "robots.txt"]]
                          + openapi("oa-hb.json", "https://hiddenbeer.com"),
}

class Pacer:  # max 8 x 404 per rolling 60 s per origin
    def __init__(s): s.t = collections.deque(); s.lock = threading.Lock()
    def hit(s):
        with s.lock:
            now = time.time()
            while s.t and now - s.t[0] > 60: s.t.popleft()
            if len(s.t) >= 8: time.sleep(61 - (now - s.t[0])); s.t.popleft()
            s.t.append(time.time())
pacers = {OLD: Pacer(), NEW: Pacer()}

def check(url):
    res = {}
    for ip in (OLD, NEW):
        u = url.replace("IP", ip)
        code, size, ct = curl(u, ip)
        if code == 404: pacers[ip].hit()
        res[ip] = (code, size, ct); time.sleep(0.15)
    return url, res

for site in sys.argv[1].split(","):
    urls = list(dict.fromkeys(SITES[site]()))
    with ThreadPoolExecutor(3) as ex:
        results = list(ex.map(check, urls))
    diffs, codes = [], collections.Counter()
    for url, r in results:
        (oc, os_, _), (nc, ns, _) = r[OLD], r[NEW]
        codes[f"{oc}"] += 1
        size_off = oc == 200 and max(os_, ns) > 2000 and abs(os_ - ns) / max(os_, ns) > 0.25
        if oc != nc or size_off:
            diffs.append(f"  {url}  OLD {oc} {os_}B | NEW {nc} {ns}B")
    print(f"== {site}: {len(urls)} URLs, OLD status mix {dict(codes)}, differences: {len(diffs)}")
    print("\n".join(diffs[:40]))
    json.dump(results, open(f"{DIR}/{site}.json", "w"))
