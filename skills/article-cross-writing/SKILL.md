---
name: article-cross-writing
description: Turn one idea or repo into a technical content series around ONE GitHub repo that holds everything (code, examples, docs, diagrams, every platform article and the slides) - seven platform articles (Dev.to, DZone, Medium, LinkedIn Pulse, Substack, InfoQ, JavaPro), each with its own angle, title, length and tone, plus every banner, diagram (source + PNG), the Marp talk deck and its PPTX and PDF exports for Google Slides, Keynote and Speaker Deck, all in one run. Use when asked to "write all cross articles", "write the cross-platform articles", "write/create an article series", "write articles for dev.to/medium/dzone/linkedin/substack/infoq/javapro about X", "turn this repo/idea into articles plus a talk", or "create the slides for this series" (a single deck from one finished article is slides-creator). Writes local drafts only, never posts; hands off to article-cross-review.
---

# Tech content series (write phase)

**Pipeline:** **write (this skill)** -> review and align (`article-cross-review`) -> post (`article-cross-posting`, only on the user's command).

## The central rule: one repo per series

Everything in a series lives in **one GitHub repo**: all code and runnable examples, docs, diagrams (with sources), every platform article (`docs/articles/<platform>/`) and the slides (`docs/presentations/`). Nothing is kept anywhere else. That repo is the series repo you are working in (the current project), not this skill folder or the reference repo; its code, diagrams and docs are what articles copy and what review checks against. Reference layout only: `~/git/share-tokens-using-spec-driven-dev` (<https://github.com/wallaceespindola/share-tokens-using-spec-driven-dev>).

- Code snippets and diagrams are made in the repo first, then embedded in articles by relative path. Platform copies are derived, never edited on their own. Changes flow repo -> articles -> posted versions.
- Platforms differ in angle, title, length, tone and which subset of snippets and diagrams they use. Code never diverges.
- Every article and the deck link the same repo, and every article ends with the same "Examples repository" line just before the footer.
- The repo README is about the project's idea: its own banner, no list of or links to the articles.
- The repo is committed and pushed before any article goes live, so every link resolves.

## "Write all": what one run produces

"Write all cross articles" means every deliverable below, in one run, without stopping between phases (pause only for real decisions: repo name, platform list, a missing fact). Nothing is posted.

| Deliverable | Where | Done when |
| --- | --- | --- |
| Series repo scaffold, README with its own banner and badges | repo root, `docs/images/banner.png` | `make lint` passes |
| Code, examples, docs (spec/PRD, guides) | `docs/`, example folders | examples run or copy-paste cleanly |
| 7 platform articles (Dev.to, DZone, Medium, LinkedIn, Substack, InfoQ, JavaPro) | `docs/articles/<platform>/article.md` | each meets its matrix row below, matches `references/AUTHOR_STYLE.md`, and has a recorded humanizer and `ai-check` pass |
| 7 banners (InfoQ also JPEG) | `docs/articles/<platform>/banner.png` / `banner.jpg` | one per platform, own text |
| Diagrams, source next to rendered PNG (InfoQ also JPEG) | `docs/articles/<platform>/diagrams/`, `docs/presentations/diagrams/` | `make diagrams` renders all, every article embeds at least one |
| Talk deck source | `docs/presentations/slides.md` | Marp builds without errors |
| PPTX (editable, Keynote and Google Slides compatible) | `docs/presentations/<deck>.pptx` | opens in Keynote |
| PDF (Speaker Deck upload) | `docs/presentations/<deck>.pdf` | `make slides` exports it |
| Google Slides / Keynote / Speaker Deck guide | `docs/presentations/GOOGLE_SLIDES.md` | written from the reference repo's |

Finish by running `make diagrams lint links slides`, then hand off to `article-cross-review`. Commit and push the repo only when the user asks.

## Phase 0: create or confirm the repo

Use the existing repo if the user names one, otherwise create it (ask before creating a GitHub remote). Copy the tooling from the reference repo and rename the deck outputs:

```text
README.md                    title, banner, badges, content, ## Support, ## Author, ## License
Makefile                     diagrams, lint, links, slides, check (copy from reference repo)
.markdownlint.json           copy; docs/presentations/.markdownlint.json disables MD025 for Marp
.github/workflows/docs.yml   markdownlint + offline lychee link check
CLAUDE.md                    what the repo is, layout, commands, prose conventions
docs/spec/                   PRD-style definition of the idea
docs/images/banner.png       README banner, 1280x400, about the idea (never an article banner)
docs/<examples, guides>      runnable or copy-paste examples the articles quote
docs/articles/<platform>/    article.md, banner.png (InfoQ: banner.jpg), diagrams/*.{puml,mmd,png}
docs/articles/BANNER_DESIGN.md   the series' banner philosophy
docs/presentations/          slides.md, <deck>.pptx, <deck>.pdf, GOOGLE_SLIDES.md, diagrams/
```

For code-heavy topics, generate the examples with `java-coder`, `python-coder` or `javascript-coder` (or `code-examples-generator` for snippets) and make sure they run. README layout and Support badges follow the global CLAUDE.md; the reference repo's README is the template. Banner: `article-image-generator` (`ledger_light.py --platform readme`, or `generate_banner.py --size 1280x400`).

## Phase 1: research

- **Project context first:** in the target project (the series repo you are working in), read everything under `docs/` before writing anything: specs and PRDs (`docs/spec/`), feature designs (`docs/specs/`), architecture and team guides (`ARCHITECTURE.md`, `CODING_GUIDE.md`, `TESTING_GUIDE.md`), backlog/task examples, existing articles and presentations, plus the root `README.md`, `CLAUDE.md` and `AGENTS.md`. That is the source of truth for terms, names, process steps, numbers and examples: use its wording, quote its files, and link them. If an article needs something `docs/` does not cover, add it to `docs/` first (or ask), never invent it in the article. If `docs/` and an article disagree later, fix the article.
- Read the repo's spec and examples end to end. Gather sources with links; verify anything that drifts (vendor billing, quotas, product names, CLI spellings, file locations) on the vendor's current docs, and give every article the same corrected facts.
- No fabricated stats or anecdotes. If there is no data, say so ("a proposal, no adoption numbers yet").
- Style base: read Wallace's newest `docs/articles/<platform>/article.md` across his repos, and his profile list (`~/git/wallaceespindola/README.md`, "Latest Articles, Publications and Tech-Talks") for title style. His topics usually land as Dev.to + Medium + LinkedIn + Substack, with DZone for enterprise patterns and one Speaker Deck talk per topic.

## Phase 2: outline the series

Write one line per platform: angle, working title, which snippets and diagrams it uses. Titles and angles must all differ; no paragraph is shared between platforms. Confirm the platform list with the user if it isn't all seven.

## Phase 3: per-platform drafts

**Voice first.** Before drafting, read `references/AUTHOR_STYLE.md` (Wallace's voice, taken from his published articles) and match it: openings, person, paragraph length, headings, how code is introduced, sourcing, closing CTA and the per-platform voice table. It overrides the generic `docs/HUMANIZATION_GUIDE.md` where they conflict.

Each platform skill owns its format and its "Verified platform rules" block; read it before drafting. Lengths below are the working ranges from the reference series.

| Platform | Angle | Length | Tone | Title style | Required elements | Owning skill |
| --- | --- | --- | --- | --- | --- | --- |
| Dev.to | Hands-on: the files you add and the steps | 1,500-3,000 words | Practical, friendly | Concrete, sentence case, "X, not Y: a Z workflow" | YAML front matter (`title`, `published`, `description`, max 4 `tags`); cover 1000x420; AI disclosure line; question CTA | `devto-formatter` |
| DZone | Governance and process: roles, gates, metrics, trade-offs | 1,500-4,500 words (min 800) | In-the-weeds, production-focused | "Topic: governing/doing X" | H1, author block with companion repo; JPEG images about 100-200 KB; metadata comment (TL;DR, type, summary, zones, tags). **The author must write or fully rewrite it: DZone rejects AI text** | `dzone-article` |
| Medium | Opinion essay: why it works, what changes | 2,000-5,000 words | Personal, reflective | Question or provocation, sentence case | Metadata comment (5 topics, meta description); italic subtitle about 140 chars; byline; AI disclosure in the first two paragraphs | `medium-optimizer` |
| LinkedIn Pulse | Leadership: what a lead or manager decides | 1,000-1,600 words | Professional | Short, punchy, two sentences | Front matter (author, description); cover 1920x1080; **no tables** (lists, in the local file too); hashtags line at the end | `linkedin-pulse-formatter` |
| Substack | Personal "Code & Coffee" habit note | 1,500-2,000 words | Conversational, "Hey folks," | A habit or imperative | Front matter (`newsletter: Code & Coffee`); subject line and preview text; reply CTA | `substack-newsletter` |
| InfoQ | Trend and pattern analysis for architects | 1,500-4,000 words | Editorial, neutral, cited | Title Case, 60-80 chars | Exactly 5 one-sentence key takeaways; JPEG banner and diagrams; references; About the author; AI disclosure; 4-week exclusivity note; own original diagrams | `infoq-article` |
| JavaPro | Code walkthrough: from the spec to tested Java | 15,000-25,000 characters incl. code | Technical, enterprise | Concrete outcome, sentence case | Abstract; full listings with explanation; references; author bio; short AI note; original, not republished; own original diagrams | `javapro-magazine` |

Every article:

- Banner at the top with alt text, at least one diagram with descriptive alt text, sources next to PNGs.
- Author line "Wallace Espindola, Solution Architect" with GitHub and LinkedIn.
- Ends with the "Examples repository" line, then the footer:

```text
Need more tech insights?
Check out my GitHub, LinkedIn, and Speaker Deck.
Happy coding!

Wallace Espindola, Solution Architect
GitHub: https://github.com/wallaceespindola/
LinkedIn: https://www.linkedin.com/in/wallaceespindola/
Speaker Deck: https://speakerdeck.com/wallacese
```

- Sentence-case headings (InfoQ title excepted), no em dashes, no emojis, never name the author's employer or internal tools.
- Use `seo-optimizer` for titles, descriptions and tags.
- Parallel drafting is fine: give each agent its own output folder and its own scratch folder.

### Humanizer pass (after each draft)

1. Run the `humanizer` agent on the draft file (it chains `ai-check`, `humanizer`, `humanize` and `avoid-ai-writing`, then re-scores). If the agent isn't available, run the skills yourself: `humanizer`, then `avoid-ai-writing`, then `ai-check` as the final score.
2. Constraint for the pass: it must not change facts, code blocks, commands, links, numbers, quotes, the heading structure, the "Examples repository" line or the footer. Save a copy before the pass, diff it against the result (`git diff --no-index --word-diff`) and revert anything it touched there.
3. Re-check the result against `references/AUTHOR_STYLE.md`. Humanizers drift: put back his openings, sentence-case headings and CTA wording; remove one-sentence-paragraph runs, bold reveals, exclamation marks or chatty asides it added.
4. Record the final `ai-check` score per platform in the hand-off summary; `article-cross-review` checks it.

## Phase 4: banners and diagrams

- Banners: `article-image-generator`, one design family per series recorded in `docs/articles/BANNER_DESIGN.md`, a different palette and 0-4 words per platform, each at the platform's verified size (JPEG for InfoQ; JPEG suits DZone's 100-200 KB guidance). Look at every PNG, then review all banners on one contact sheet.
- Diagrams: `diagram-mermaid` or `diagram-plantuml`. A shared diagram has one canonical source in the repo; article copies are derived from it. InfoQ and JavaPro keep their own original diagrams. `make diagrams` renders every source; check tall flowcharts stay readable at article width.

## Phase 5: slides

Owned by `slides-creator` (its "Speaker Deck, PowerPoint and Google Slides delivery" section).

- `docs/presentations/slides.md` in Marp, speaker notes as HTML comments, title slide with "Wallace Espindola, Solution Architect", closing slide with the repo link. Title in Title Case, matching the Speaker Deck title.
- `make slides` exports the PDF (Speaker Deck takes PDF only) and the Marp PPTX. For an editable deck that imports cleanly into Google Slides and Keynote, build the PPTX with python-pptx (Arial, Courier New, real speaker notes) and apply slides-creator's notes-master fix, then run its Keynote open test.
- Write `docs/presentations/GOOGLE_SLIDES.md` from the reference repo's: get the file, open or import in Google Slides, Keynote, Speaker Deck PDF upload.

## Phase 6: hand off

Commit the drafts to the series repo (ask before pushing if the repo is new), then run `article-cross-review`. Posting waits for the user's explicit command per platform (`article-cross-posting`).

## Checklist

- [ ] **Repo:** exists, README per global layout with its own banner and no article links, Makefile, lint and link CI, spec and examples in place
- [ ] **Research:** sources linked, drifting facts verified once for the whole series, no invented numbers
- [ ] **Outline:** seven different titles and angles, snippet and diagram subset per platform
- [ ] **Voice:** `references/AUTHOR_STYLE.md` read before drafting; each draft matches it, including after the humanizer pass
- [ ] **Drafts:** matrix requirements met, identical snippets, "Examples repository" line and footer
- [ ] **Humanizer:** `humanizer` agent (or `humanizer`, `avoid-ai-writing`, `ai-check`) run on every draft, facts/code/links/headings/footer unchanged, final `ai-check` score recorded
- [ ] **Images:** banner per platform at verified size, at least one diagram each with alt text, sources next to PNGs
- [ ] **Slides:** Marp source, PDF and PPTX exported, PPTX opens in Keynote, GOOGLE_SLIDES.md written
- [ ] **Hand off:** drafts committed, `article-cross-review` run, nothing posted
