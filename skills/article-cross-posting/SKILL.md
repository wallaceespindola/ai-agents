---
name: article-cross-posting
description: Post or cross-post finished articles to Dev.to, Medium, DZone, Substack, LinkedIn, InfoQ and JavaPro through browser automation, and keep the local article.md aligned with the posted version. Use when asked to "post/cross-post/publish my articles to dev.to, medium, dzone, substack, linkedin, infoq, javapro", to fill a platform draft from a local Markdown article, or to "align local and posted articles".
---

# Article Cross-Posting (browser editors)

Workflow verified 2026-10-20 posting one series to all seven platforms. Editor quirks per platform live in each platform skill under "Posting via the browser editor (verified 2026-10-20)": `devto-formatter`, `medium-optimizer`, `dzone-article`, `linkedin-pulse-formatter`, `substack-newsletter`, `infoq-article`, `javapro-magazine`.

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

## Keep local and posted aligned

- When a platform can't render something (tables on LinkedIn), change the local article too (table -> bullet list) so both stay identical.
- Verify with two checks, in the browser console against the editor DOM and locally against the `marked` HTML:
  1. **Block signature:** per block `type + text length + first 25 chars`, plus `IMG <alt>` entries; diff the two lists.
  2. **Tag-aware check:** headings vs paragraphs and image alt text. The signature alone misses a heading demoted to a paragraph (Medium does this after image inserts).
- Wrap console snippets in an IIFE to avoid `const` redeclaration errors on re-runs.

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

## Related Skills

`devto-formatter`, `medium-optimizer`, `dzone-article`, `linkedin-pulse-formatter`, `substack-newsletter`, `infoq-article`, `javapro-magazine`, `article-review`, `article-image-generator`, `diagram-mermaid`.
