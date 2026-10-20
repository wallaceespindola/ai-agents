---
name: site-articles-sync
description: Import Wallace's latest articles and talks from Dev.to, Medium, Substack, Speaker Deck, DZone and LinkedIn Pulse into the W-Tech website blog (~/git/wtech-website), verify, commit, push and deploy. Use when asked to "update my site blog with my latest articles", "sync my articles to wtechitsolutions.com", "import my new posts/talks into the W-Tech blog".
---

# Site Articles Sync (W-Tech blog)

Repo: `~/git/wtech-website` (Next.js; read its `CLAUDE.md` first). Importer: `scripts/sync-articles.mjs`
(`npm run sync:articles`). Every publication becomes its own post in `content/posts/<slug>.md` with
`external: true`; images land in `public/images/articles/`. Local (non-external) posts are never touched.

## 1. Feed platforms (automatic)

```bash
cd ~/git/wtech-website && git pull && node scripts/sync-articles.mjs
```

- Dev.to (API), Medium + Substack (RSS), Speaker Deck (`https://speakerdeck.com/wallacese.atom`;
  handle is `wallacese`, `wallaceespindola` 404s).
- Medium RSS only holds the last ~10 items; older ones already imported stay (the script only removes
  imports that vanished from *every* source run, so check `git status` for unexpected deletions).
- Speaker Deck posts get slugs assigned after articles, so a deck never steals an existing article URL
  (they get a `-speakerdeck` suffix on title clashes).

## 2. DZone and LinkedIn (manual, browser)

No public feed (DZone: Cloudflare 403 to curl; LinkedIn: login wall on the list). Use claude-in-chrome,
new tab, run JS (returning URLs with query strings gets blocked; return `pathname` only):

- DZone `https://dzone.com/users/1254611/wallacese.html`, wait ~3s, collect `a` whose `pathname` starts
  with `/articles/` (ignore "How to Post to DZone", "Submission Guidelines" and the trailing "related" ones).
- LinkedIn `https://www.linkedin.com/in/wallaceespindola/recent-activity/articles/`, wait ~4s, collect
  `/pulse/` links.

Compare with `STATIC_ARTICLES` in the script. A LinkedIn/DZone piece that is only a cross-post of an
article already imported under the same title from a feed is skipped. For a genuinely new piece:

1. Public pulse pages load fine with curl + a desktop User-Agent. Grab `datePublished`, `og:image`,
   `og:description`, and save the `<div data-test-id="article-content-blocks">` subtree (count nested
   `<div>`s; replace `data-delayed-url` with `src` on `<img>`) to `content/imports/linkedin-<short>.html`.
   For DZone, save the article body HTML from the browser the same way (`dzone-<short>.html`).
2. Add an entry to `STATIC_ARTICLES` (platform, title, url, date, description ≤160 chars, image, tags,
   htmlFile) and re-run the script. LinkedIn `/redir/redirect?url=` links are unwrapped automatically.

Close the browser tab when done.

## 3. Review

- `git status`: new posts + images; modified posts only where content really changed.
- Spot-check a new post: front matter, no leftover bylines ("by Wallace Espindola") in the description,
  images localized (no remote image URLs in the body), no tracking/redirect links.
- Never mention the previous CMS platform anywhere (`tests/content.test.ts` enforces it).
- `make check` (lint, typecheck, tests, build) must pass.

## 4. Ship

Commit (no co-author lines) and push to `main`. Deploy only when the user asked for it:
`./deploy.sh` (checks + deploy to server-vps). Then confirm a new post URL returns 200 on
`https://wtechitsolutions.com/<slug>/`.
