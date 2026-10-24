---
name: article-cross-review
description: Review a multi-platform article series built around one GitHub repo that holds everything (code, examples, docs, diagrams, all platform articles and slides) and keep local and posted versions aligned. Runs article-review on each platform draft plus series-level checks - same repo link everywhere, code snippets identical to the repo, banner and diagrams with sources and alt text, unique titles and angles, platform limits, disclosures, footer, no em dashes, no employer name, lint and links - and reports a per-platform pass/fail table. Use when asked to "review/check my articles or article series", "is the series ready", or "align local and posted articles". Fixes only on request.
---

# Content series review and alignment

**Pipeline:** write (`article-cross-writing`) -> **review and align (this skill)** -> post (`article-cross-posting`, only on the user's command).

The series repo holds everything (code, examples, docs, diagrams, every platform article, slides) and is the single source of truth: snippets and diagrams live in the repo, articles embed them, posted versions mirror the local `article.md`. This skill checks that chain. It reports; it changes files only when the user asks for fixes.

## 1. Series-level checks (scripted)

```bash
python3 ~/git/ai-agents/skills/article-cross-review/scripts/check_series.py <series-repo> \
  --repo-url https://github.com/wallaceespindola/<repo> --forbid "<employer>" "<internal tool>"
```

Per `docs/articles/<platform>/article.md` it checks: the repo URL and the "Examples repository" line, author line, footer (InfoQ and JavaPro need an author bio instead; footer is a warning there), no em dashes, forbidden words, banner present, at least one diagram, every image exists with alt text, a `.mmd`/`.puml`/`.svg` source next to each diagram, length against the `article-cross-writing` matrix (words; characters for JavaPro), AI disclosure on Dev.to, Medium and InfoQ, no tables on LinkedIn, exactly 5 InfoQ key takeaways and JPEG images, duplicate titles, and code blocks not found verbatim in the repo. Exit 1 on any FAIL. Ask the user for the employer and internal-tool names to forbid; never write them into the repo.

WARN items need judgment: a code block not in the repo is either drift (fix the article or add the code to the repo) or a deliberate illustration (file tree, command line). Word counts include Markdown syntax, so a count a few words over is fine.

Then, in the series repo: `make lint` and `make links` (CI runs both), and `make diagrams` if any source changed (check that `git status` shows no stale PNGs).

## 2. Manual series checks

- Titles and angles differ per platform; no paragraph is shared between versions.
- Shared diagrams match their canonical source in the repo (`cmp` the copies); InfoQ and JavaPro use their own original diagrams.
- Drifting facts (vendor billing, quotas, product names) are the same, and current, in every article.
- DZone text was written or fully rewritten by the author (DZone rejects AI text). Flag it every time.
- InfoQ (4-week exclusivity) and JavaPro (original, not republished) carry content that is not posted anywhere else.
- Banners belong to one family (`docs/articles/BANNER_DESIGN.md`); view them on one contact sheet.
- Deck: `make slides` runs, the PPTX opens in Keynote (`slides-creator` test), the closing slide links the repo.

## 3. Per-article editorial gate

Run `article-review` on each draft (factual integrity, AI-pattern scrub, code, structure, platform compliance, links). If it flags AI tells, use the `humanizer` agent, then re-run `article-review` until PASS. Re-run after any late edit.

## 4. Report

One table, then the fix list per platform:

```text
| Platform | Size        | Script | article-review | Notes                       |
|----------|-------------|--------|----------------|-----------------------------|
| devto    | 2212 words  | PASS   | PASS           |                             |
| javapro  | 31738 chars | PASS   | FIX            | over 25k chars; trim        |
```

Fix only what the user asks for. Fixes go to the repo first (snippet, diagram source), then to every article that embeds it.

## 5. Local vs posted alignment (after posting)

`article-cross-posting` calls this step after each post. When a platform can't render something (tables on LinkedIn), change the local article too (table -> list) so both stay identical.

Compare the editor DOM (browser console) with the local `marked` HTML (`npx marked --gfm -i article.md`):

1. **Block signature:** per block `type + text length + first 25 chars`, plus `IMG <alt>` entries; diff the two lists.
2. **Tag-aware check:** headings vs paragraphs and image alt text. The signature alone misses a heading demoted to a paragraph (Medium does this after image inserts).

Wrap console snippets in an IIFE to avoid `const` redeclaration errors on re-runs. Dev.to can be compared without the DOM: `https://dev.to/api/articles/<user>/<slug>` returns `body_markdown`.

## Checklist

- [ ] `check_series.py` exits 0; every WARN explained or fixed
- [ ] `make lint`, `make links` clean; diagrams re-rendered if sources changed
- [ ] Manual series checks done; DZone authorship flagged
- [ ] `article-review` PASS for every platform
- [ ] Report table delivered; nothing fixed without the user asking
- [ ] After posting: block-signature and tag-aware compare clean, local file updated for any forced change
