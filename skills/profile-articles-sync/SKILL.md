---
name: profile-articles-sync
description: Pull Wallace's latest posts from Dev.to, Medium, Substack, DZone, LinkedIn Pulse and Speaker Deck and add any missing ones to the "Latest Articles, Publications and Tech-Talks" list in the GitHub profile README (~/git/wallaceespindola/README.md), then commit and push. Use when asked to "update my GitHub profile with latest articles", "sync my articles to my git page", "add my new posts/talks to my profile README".
---

# Profile Articles Sync

Target: `~/git/wallaceespindola/README.md`, section `## 📝 Latest Articles, Publications and Tech-Talks`.
Goal: every published post/deck on the six platforms appears once in that list. Never remove or rewrite existing entries.

## 1. Fetch latest from each platform

Feeds work with plain `curl` for four platforms:

```bash
# Dev.to (JSON API)
curl -s "https://dev.to/api/articles?username=wallaceespindola&per_page=15" | python3 -c "
import json,sys;[print(a['published_at'][:10],a['title'],a['url'],sep=' | ') for a in json.load(sys.stdin)]"

# Medium + Substack (RSS)
for f in https://medium.com/feed/@wallaceespindola https://wallaceespindola.substack.com/feed; do
  echo "== $f"; curl -sL "$f" | python3 -c "
import sys,xml.etree.ElementTree as E
for i in list(E.fromstring(sys.stdin.read()).iter('item'))[:15]:
    print(i.findtext('pubDate')[:16],i.findtext('title'),i.findtext('link').split('?')[0],sep=' | ')"
done

# Speaker Deck (Atom; content = deck description)
curl -sL https://speakerdeck.com/wallacese.atom | python3 -c "
import sys,xml.etree.ElementTree as E
ns={'a':'http://www.w3.org/2005/Atom'}
for e in E.fromstring(sys.stdin.read()).findall('a:entry',ns):
    print(e.findtext('a:published',namespaces=ns)[:10],e.findtext('a:title',namespaces=ns),e.find('a:link',ns).get('href'),sep=' | ')"
```

DZone (Cloudflare 403 on curl) and LinkedIn (login wall) need the browser (claude-in-chrome). Open a new tab, then run JS:

- DZone: `https://dzone.com/users/1254611/wallacese.html`, wait ~3s, collect `a[href*="/articles/"]` (skip "How to Post to DZone" / "Submission Guidelines").
- LinkedIn: `https://www.linkedin.com/in/wallaceespindola/recent-activity/articles/`, wait ~4s, collect `a[href*="/pulse/"]`.

```js
await new Promise(r=>setTimeout(r,4000));
[...new Set([...document.querySelectorAll('a[href*="/pulse/"]')]
  .map(a=>a.innerText.trim().split('\n')[0]+' | '+a.href.split('?')[0]))].join('\n')
```

Close the tab when done.

## 2. Diff against the README

A post is missing if its URL (strip query string) is not in the README. `grep -F` each URL. Skip non-articles (e.g. Substack "Reader's survey").

## 3. Add missing entries

Entry format, one line, matching existing entries exactly:

```
- **[[<Label>] <Title>](<url>)** - <one-sentence summary>
```

Labels: `LinkedIn Pulse`, `Code & Coffee - Substack`, `Dev Community` (dev.to), `Medium`, `DZone`, `Speaker Deck`.

- Summary: one sentence from the post's feed description/subtitle, in your own words, no em dashes (use hyphen or comma).
- Placement: list is newest first. A brand-new post goes at the top of the list. Cross-posts of the same topic stay grouped together; a deck goes right after its matching article group.
- Keep the closing `- More available on ...` line listing every platform.

## 4. Commit and push

```bash
cd ~/git/wallaceespindola
git diff   # review
git add README.md
git commit -m "Add latest published articles and talks to the profile list"
git push
```

No co-author or AI attribution lines in the commit. If nothing is missing, say so and don't commit.
