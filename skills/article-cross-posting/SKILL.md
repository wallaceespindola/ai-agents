---
name: article-cross-posting
description: Post or cross-post finished, reviewed articles from a series repo to Dev.to, Medium, DZone, Substack, LinkedIn, InfoQ and JavaPro, and upload the talk PDF to Speaker Deck, through browser automation, only on the user's explicit per-platform command. Medium and Dev.to publish directly; DZone, Substack, LinkedIn, InfoQ and JavaPro stop at draft or at the author's own submission. Then aligns local and posted versions and syncs live posts to the GitHub profile and site. Use when asked to "post/cross-post/publish my article(s) on dev.to, medium, dzone, substack, linkedin, infoq, javapro or speaker deck", or to fill a platform draft from a local Markdown article.
---

# Article Cross-Posting (browser editors)

**Pipeline:** write (`article-cross-writing`) -> review and align (`article-cross-review`) -> **post (this skill)**.

Every post comes from the series repo, the one repo that holds everything (code, examples, docs, diagrams, every platform article, slides): the local `docs/articles/<platform>/article.md` with its banner and diagrams, all linking that same repo. Push that repo before the first post so its links resolve, and run `article-cross-review` first.

Workflow verified 2026-10-20 posting one series to all seven platforms. Editor quirks per platform live in each platform skill under "Posting via the browser editor (verified 2026-10-20)": `article-cross-writing`, `article-cross-review`, `profile-articles-sync`, `site-articles-sync`, `devto-formatter`, `medium-optimizer`, `dzone-article`, `linkedin-pulse-formatter`, `substack-newsletter`, `infoq-article`, `javapro-magazine`.

## Publish only on command

- Act only on the user's explicit command, per platform ("publish on Medium", "draft on LinkedIn"). Finishing the review is not a command. "Post everywhere" still follows the policy below.
- Before each platform, confirm the series repo is pushed and the article passed `article-cross-review`.
- Post one platform at a time and report each URL before the next.

## Publish vs draft policy

- **Publish directly:** Medium, Dev.to.
- **Stop at draft** for the author to submit/publish: DZone, Substack, LinkedIn, InfoQ, JavaPro.
- InfoQ: the author fills the submission form, attestations and the Google Doc share himself. JavaPro needs the author's WordPress login. Claude does neither.
- DZone rejects AI-written text: flag this to the author before he submits.

## One browser, one clipboard

The browser and the macOS clipboard are one shared resource. Never run parallel agents that paste into editors at the same time. Set the clipboard right before each paste: other apps can overwrite it.

## HTML clipboard pipeline

Rich editors take pasted HTML far better than Markdown or typed text.

```bash
npx marked --gfm -i article.md -o /tmp/a.html
# post-process (python/sed):
#  - soft newlines inside <p> -> <br>  (LinkedIn: emit each line as its own <p> instead)
#  - blank lines inside <pre> -> a line holding a single space (Medium/Froala split code blocks at blank lines)
hex=$(xxd -p /tmp/a.html | tr -d '\n')
osascript -e "set the clipboard to «data HTML${hex}»"
```

Then focus the editor body and press Cmd+V.

## Placeholder images

Where an editor won't take images from pasted HTML, put a placeholder paragraph (e.g. `IMGMARK-process-flow`) in the HTML at each image position. After pasting, select each placeholder, delete it and insert the image through the editor's own image button and file input, typing the same alt text as the local Markdown.

## Every post carries every image

The banner plus every diagram, with the same alt text as the local `article.md`. Mermaid via mermaid-cli needs system Chrome: `npx -p @mermaid-js/mermaid-cli mmdc -p pptr.json -i x.mmd -o x.png` with `pptr.json` = `{"executablePath":"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome","headless":"new"}`.

## Speaker Deck (talk PDF)

On command only. Sign in is the author's. Click New Deck, upload the deck PDF from `docs/presentations/` (Speaker Deck takes PDF only, exported by `make slides`), set the title (same as the deck's title slide), description and category. Publish only if the command says so; otherwise leave the upload for the author to publish. Google Slides import is the author's step, documented in the repo's `docs/presentations/GOOGLE_SLIDES.md`.

## Keep local and posted aligned

After each post, run the alignment step in `article-cross-review` (block-signature and tag-aware compare). When a platform forces a change (LinkedIn tables to lists), change the local article too.

## After posting: sync live posts

Only for posts that are live (not drafts, not pending review):

- Commit the aligned local articles to the series repo.
- `profile-articles-sync`: add the new posts and deck to `~/git/wallaceespindola/README.md`.
- `site-articles-sync` (optional): import into the W-Tech blog. Its deploy step runs only if the user asks for a deploy.

## Footer convention

```text
Need more tech insights?

Check out my GitHub, LinkedIn, and Speaker Deck.

Happy coding!

Wallace Espindola, Solution Architect
GitHub: https://github.com/wallaceespindola/
LinkedIn: https://www.linkedin.com/in/wallaceespindola/
Speaker Deck: https://speakerdeck.com/wallacese
```

Speaker Deck is `wallacese`; `speakerdeck.com/wallaceespindola` 404s.

## Checklist per platform

- [ ] Clipboard set immediately before paste; no other agent using the browser
- [ ] Title, subtitle/meta, tags set (and actually persisted: reload and check)
- [ ] Banner/cover plus every diagram present, alt text matches local
- [ ] Code blocks intact (line breaks, no splits)
- [ ] Block-signature + tag-aware compare clean
- [ ] Footer present, Speaker Deck link is `wallacese`
- [ ] Published (Medium, Dev.to) or left as saved draft (all others), URL reported
- [ ] Explicit user command for this platform; series repo pushed first
- [ ] Live posts synced with `profile-articles-sync` (and `site-articles-sync` if asked)

## Related Skills

`article-cross-writing`, `article-cross-review`, `profile-articles-sync`, `site-articles-sync`, `devto-formatter`, `medium-optimizer`, `dzone-article`, `linkedin-pulse-formatter`, `substack-newsletter`, `infoq-article`, `javapro-magazine`, `article-review`, `article-image-generator`, `diagram-mermaid`.
