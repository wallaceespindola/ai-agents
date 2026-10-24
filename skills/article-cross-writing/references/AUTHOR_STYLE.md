# Author style: Wallace Espindola

How Wallace writes, taken from his published articles. Match this voice in every draft, and re-check against it after any humanizer pass (humanizers can drift toward a generic "casual blogger" voice that isn't his).

Where this file conflicts with `~/git/ai-agents/docs/HUMANIZATION_GUIDE.md` or `docs/PLATFORM_STYLES.md` (one-sentence paragraphs, CAPS, bold emphasis, analogies), this file wins: it describes what he actually publishes now.

## Sources

Weighted most: the 2026 Copilot capacity series, edited and approved by him (`~/git/share-tokens-using-spec-driven-dev/docs/articles/*/article.md`, all seven platforms). Also read, as published: Dev.to (legacy modernization, Markdown/SDD, JCON Europe, Python at 35), Medium (legacy modernization), Substack (legacy modernization, Markdown, contract-first error handling), LinkedIn (legacy modernization, Python at 35). Refresh this file when a new series is approved.

## The voice in one paragraph

A senior engineer explaining a practical idea to peers. Plain, concrete, first person when he states an opinion or a decision, "you" when he tells the reader what to do. He starts from the situation, not from a hook. He says what the idea costs and where it doesn't fit, sources every fact with a named link, and says plainly when there is no data. Humor is dry and rare. No hype, no emojis, no em dashes.

## Observable traits

### Openings

- Start with the concrete situation, in normal-length sentences. No TL;DR line, no rhetorical question hook.
  - "Most teams get Copilot through a company contract, and each developer works against a personal limit"
  - "Here is a situation I suspect plenty of teams are in, even if nobody says it out loud."
- Name the problem in a short beat after the setup: "Usage is uneven." / "Then real life happens."
- Within the first screen, say what the article is and what it isn't: "This article covers the hands-on part: the files you add to a repo".
- Link the companion repo early in the body, then again in the closing line.

### Person and stance

- "I" for opinions, choices and admissions: "I don't like it, for a few reasons." / "So I wrote down a process for doing it properly."
- "You" for instructions and the reader's situation: "You don't need a new process to test the idea."
- States a view, then its limit: "I don't think the answer is to buy more seats, and I am sure the answer is not to share accounts."
- Contractions throughout (don't, it's, that's, I'd), less so on InfoQ.

### Sentences and paragraphs

- Paragraphs of 2-5 sentences, mixed lengths. A short sentence lands a point after a longer one: "It works once. As a habit it breaks down quickly."
- One-sentence paragraphs only for a real turn ("So split the work along that line."), not as a rhythm device.
- Parenthetical caveats instead of dashes: "(If your org pools credits with no per-user caps, the credit side of this gets weaker.)"
- Lists without the Oxford comma: "build, tests, security scans, quality gates and human review". (The fixed footer line keeps its comma.)
- "So" to start a conclusion sentence is a habit; keep it, don't overdo it.

### Questions

- Rare in the body. At most one framing question: "If the capacity exists somewhere on the team, how do you route work to it without making a mess?"
- One question to the reader in the closing CTA.

### Headings

- Sentence case, plain statements or short claims, often with a comma or colon: "Credits are personal, the backlog isn't", "Ownership stays where it was", "Where it doesn't pay off", "Same quality gates, no exceptions".
- Practical section names: "Try this on Monday", "How to pilot it next sprint", "What to measure", "Recap", "Wrapping up", "Summary".
- InfoQ title only: Title Case.

### Code and examples

- Introduce code with one sentence ending in a colon: "Here's a trimmed version of the example task in the repo. It's ordinary Markdown:"
- Explain right after the block what matters in it: "Two sections do most of the work."
- Snippets are trimmed from the repo, and he says so ("trimmed from the example in the repo"). Commands go in `bash` blocks, file names and paths in backticks.

### Lists vs prose

- Prose first. Lists for parallel items: workarounds, roles, metrics, steps.
- Bulleted options with a bold label and a colon: "**Buy more seats:** the clean answer, when the budget exists."
- Numbered lists for steps the reader runs, each starting with a verb: "Pick one well-defined task from your backlog".
- Bold sparingly: role names on first use and labels. No bold one-line "reveal" paragraphs.

### Claims and sourcing

- Facts carry a named inline link to the vendor's docs or blog, sometimes with a short quote: "[GitHub's billing docs] put it plainly: "A seat is a license for one user.""
- Says when there is no data: "It's a proposal, and I have no results to report yet." / "I don't have adoption numbers from a live rollout, and I won't invent any."
- Labels illustrations as illustrations: "Illustrative bar chart of per-developer Copilot credit use".
- Never "studies show", never an invented percentage.

### Hedging and limits

- Moderate hedging, on the claims that need it: "usually", "I think", "I suspect", "rule of thumb".
- Always includes a limits or trade-offs section: "Delegation has a fixed cost: write, review, hand off, validate."
- Names the counter-case honestly ("Pooling with no per-user caps ... makes the credit argument weaker").

### Humor

- Dry, short, inside a sentence: "the DTO-mapper-repository boilerplate nobody enjoys", "Sooner or later someone suggests sharing a login, which is a hard no."
- No jokes as section openers, no puns in headings.

### Closings and CTA

- Close with a short summary or "Wrapping up" that restates the idea in plain terms, then one question to the reader.
  - Dev.to: "How does your team handle uneven Copilot capacity today? ... I'd like to hear in the comments."
  - DZone: "I'm curious whether others formalized it or still run on favors. Let me know in the comments."
  - Substack: "Hit reply or drop a comment. I read every one."
  - LinkedIn: "... Let me know your thoughts in the comments." then the hashtag line.
- Then the "Examples repository" line, then the fixed footer (see `SKILL.md`). InfoQ and JavaPro use an author bio instead of, or before, the footer.

### AI disclosure wording

- Dev.to, Medium, JavaPro: `*I wrote this article with AI assistance, then reviewed, fact-checked and edited it myself.*` (Medium: in the first two paragraphs; Dev.to: just before the closing lines.)
- InfoQ: `**AI disclosure**: This article was drafted with AI assistance (Claude) for research support, outlining, drafting and editing, based on the author's own process definition and repository. ...`
- DZone: no disclosure line; the author writes or fully rewrites the text.

## Words and phrases

He uses: "capacity", "pays off", "the obvious workaround", "a hard no", "plain", "trimmed", "rule of thumb", "the part I'd want ... to check", "Here's", "That's", "So", "Then", "Let me know".

He does not use (none in the 2026 series): delve, leverage, landscape, unlock, game-changer, seamless, robust, crucial, "in today's ...", "let's dive in", "honestly", "let that sink in", "priceless", "superpower", "take this as your sign".

## Dropped since 2025-early 2026 (don't bring back)

| Older habit | Example from older posts | Now |
| --- | --- | --- |
| Em dashes | "faster, it should help us understand them" written with a dash | commas, periods, parentheses |
| Emojis in titles and bios | coffee cup in Substack titles, briefcase and laptop icons in "About the Author" | none |
| TL;DR line as opener | "**TL;DR:** AI should not help us rewrite legacy systems faster" | situation-first opening |
| One-sentence-per-line staccato | "New framework. / New cloud platform. / New architecture." | 2-5 sentence paragraphs |
| Bold one-line reveals | "**A map of the existing system.**" | the point stated in a normal sentence |
| Title Case and numbered headings | "Enter Spec-Driven Development", "##1. Learning at a Different Speed" | sentence case, no numbers |
| Hype and motivational closers | "That kind of insight is priceless." / "Go. Even once." | a summary and one question |
| "Senior Software Engineer, AI Enthusiast" bio, website link | pipe-separated title line | "Wallace Espindola, Solution Architect" plus GitHub, LinkedIn, Speaker Deck |
| "Further Reading ... excellent resources" | curated list with praise | inline links; InfoQ/JavaPro "References" without adjectives |
| Clickbait-ish titles | "Stop Faking "John Doe"", "Here's What Kept It Alive So Much Time!" | concrete, sentence-case titles |

## Do and don't

Do:

- Open on the situation; say early what the article covers.
- Use "I" for decisions and opinions, "you" for actions.
- Link every fact to its source by name; say when there is no data.
- Include a "where it doesn't pay off" or trade-offs section.
- Introduce each code block with one sentence and a colon; explain it after.
- End with a summary, one reader question, the "Examples repository" line and the footer.

Don't:

- Use em dashes, emojis, exclamation marks in prose, or Title Case headings (InfoQ title excepted).
- Write one-sentence-paragraph runs, bold reveals or rhetorical question chains.
- Invent stats, anecdotes, quotes or "teams I've worked with" stories.
- Name his employer or internal tools.
- Use hype words or motivational closers.

## Per-platform voice

| Platform | Opening | Voice | Typical sections | Close |
| --- | --- | --- | --- | --- |
| Dev.to | The uneven situation in 2-3 short paragraphs, repo link, "This article covers the hands-on part" | Practical, "you" heavy, files and commands | the files, the loop, troubleshooting, Recap, Try it yourself | question CTA, AI disclosure, footer |
| Medium | A scene ("Two people sit next to each other...") and his position | Reflective essay, most "I", says what he thinks and doesn't | the gap, why the obvious fix fails, what changes, Wrapping up (bulleted views) | several questions in one short paragraph |
| LinkedIn | The business situation, paid capacity sitting idle | Leader angle: what a lead decides, measures and pilots; no tables | the problem leaders see, principle, roles, ownership, what to measure, how to pilot | "Let me know your thoughts", hashtag line |
| Substack | "Hey folks," then "Some team economics first." | Coffee-length, most conversational, "This issue is the coffee-length version" | one habit, what it looks like, where it doesn't pay off, "Try this on Monday" | "Hit reply or drop a comment. I read every one." |
| DZone | Analytical statement of the problem, author block first | Governance and process, roles, gates, metrics; states it is a proposal | the model in one paragraph, roles, gates, trade-offs, takeaways | "I'm curious whether..." |
| InfoQ | "Key Takeaways", then where current practice stops | Editorial, neutral, cited, fewer contractions, no "Hey" | history of the idea with dated sources, the pattern, risks, References | About the author, AI disclosure, exclusivity note |
| JavaPro | Abstract, then the situation in one paragraph | Technical walkthrough for "the people who will read the diff" | design choice and why, listings, test mapping, References | author bio, footer |
