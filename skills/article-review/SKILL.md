---
name: article-review
description: Use when a technical article draft is complete and needs a pre-publication editorial review — before submitting to Medium, Dev.to, DZone, InfoQ, JavaPro, LinkedIn, Substack or a blog. Catches fabricated statistics, AI-sounding prose, broken code, missing platform requirements and weak structure.
---

# Article Review — Pre-Publication Editorial Checklist

## Overview

This skill is the final quality gate in the writing pipeline:

```
write → format → SEO → REVIEW (this skill) → publish
```

Run it on the **finished draft**, not on outlines or partial drafts. The goal is a
publish/no-publish decision with a concrete list of fixes — not a rewrite. Review the
article as an editor would: skeptical about every number, allergic to AI-sounding
prose, and unwilling to ship code that doesn't run.

## When to Use This Skill

Use this skill when:
- A draft is complete and the next step would be publishing
- The technical-writer agent reaches step 4 (self-review) of its workflow
- An article is being adapted for cross-posting and each version needs its own gate
- An older published article is being refreshed and re-checked

Do not use it on outlines, half-drafts or idea lists — the checks assume finished prose,
final code and real links.

## Review Dimensions

Work through all six dimensions in order. Record every issue with a section or line
reference so the author can fix it directly.

### 1. Factual Integrity

- [ ] No fabricated statistics, percentages or survey results anywhere in the draft
- [ ] Every number has a named, linked source next to it
- [ ] No "studies show...", "research indicates...", "experts agree..." without a citation
- [ ] Version claims are current (e.g., Java 25 is the current LTS; check Python, Node, framework versions against reality, not memory)
- [ ] Benchmarks either link to a reproducible source or state the author's own test setup
- [ ] Claims about tools/platforms match their current behavior, not how they worked years ago

**When in doubt, cut the claim.** An article with fewer numbers beats an article with
one invented number.

### 2. AI-Pattern Scrub

- [ ] None of the banned phrases: "in today's digital landscape", "leverage", "delve", "game-changer", "seamlessly", "it's worth noting"
- [ ] No uniform paragraph rhythm — paragraphs vary in length, not three sentences each
- [ ] Contractions are present (you're, don't, it's) — their total absence reads as machine output
- [ ] Sentence length varies; short punchy sentences mixed with longer ones
- [ ] No hollow transitions ("Moreover,", "Furthermore,", "In conclusion,") stacked at paragraph starts
- [ ] The intro leads with a problem or insight, not throat-clearing background

For a deeper pass, invoke the `avoid-ai-writing` skill (installed; kept in sync
via git from `~/git/community-skills/avoid-ai-writing`) — it audits and rewrites
AI-sounding prose. This checklist catches the obvious offenders; that skill
catches the subtle ones.

### 3. Code Correctness

- [ ] All imports present — the reader can paste and run without guessing dependencies
- [ ] Language and framework versions stated where they matter
- [ ] Code actually runs, or is explicitly flagged as pseudocode
- [ ] Non-obvious logic has inline comments
- [ ] For cross-posted articles: code snippets are 100% identical across all platform versions and reference the same GitHub repo
- [ ] Repo link works and points to the code shown in the article

### 4. Structure

- [ ] Hook opens with a problem, concrete scenario or insight — not background context
- [ ] Headings are scannable; a reader skimming H2s gets the article's shape
- [ ] Summary or takeaways section present near the end
- [ ] Sign-off block present with GitHub and LinkedIn links for Wallace Espindola:
  - GitHub: https://github.com/wallaceespindola/
  - LinkedIn: https://www.linkedin.com/in/wallaceespindola/
- [ ] Trade-offs or limitations acknowledged — no solution presented as flawless
- [ ] No walls of text; paragraphs broken where a reader would need a breath

### 5. Platform Compliance

Check only the gates for the target platform(s):

| Platform | Gate |
| --- | --- |
| DZone | 100% human-written flag stated; minimum 1200 words |
| InfoQ | Exactly 5 key takeaways, each a complete actionable sentence; 4-week exclusivity noted |
| LinkedIn Pulse | 1000-1500 words; short scannable paragraphs |
| Medium | 2000-5000 words; clear H2/H3 hierarchy |
| Dev.to | Frontmatter tags present; 1500-3000 words |
| Substack | Conversational voice; flowing prose, light headers |
| JavaPro | 3000-5000 words; full code listings with explanation |
| Blog | Flexible 1500-4000 words; practitioner voice |

Cross-posting checks:

- [ ] Prose is unique per platform — no copy-pasted paragraphs between versions
- [ ] Publication is staggered: minimum 1 week between platforms, 4 weeks after InfoQ

### 6. Links and Metadata

- [ ] Every URL in the draft resolves (actually check them, don't assume)
- [ ] Canonical URL set for cross-posted versions
- [ ] Tags/keywords chosen for the platform
- [ ] Title is 60 characters or fewer for SEO
- [ ] Meta description drafted (150-160 characters)
- [ ] Banner/featured image exists, correct platform dimensions, reflects article content — missing banner = blocking FIX

## Verdict Format

End every review with one of three verdicts:

```
VERDICT: PASS
Ready to publish. [Optional: 1-2 polish suggestions.]
```

```
VERDICT: FIX
Blocking issues:
1. [Section "Benchmarks"] Uncited claim: "40% faster startup" — link a source or cut it
2. [Code block 3] Missing import for ObjectMapper
3. [End of article] Sign-off block absent
```

```
VERDICT: POLISH
No blockers. Optional improvements:
1. [Intro] Second paragraph restates the first — cut one
2. [Section "Setup"] Three consecutive paragraphs of identical length
```

Rules for the verdict:

- Reference issues by section heading, code block number or `file:line` when reviewing a file
- FIX means do not publish until every listed item is resolved
- Never silently rewrite the article — report; the author (or technical-writer agent) fixes
- Re-run the review after fixes; a FIX verdict is not cleared by trust

## Common Mistakes

| Mistake | Why it slips through | Fix |
| --- | --- | --- |
| Reviewing an outline instead of the finished draft | Author wants early feedback | Do a structure-only pass, but withhold the verdict until the draft is complete |
| Passing a draft with one "small" uncited stat | It sounds plausible | One fabricated number is a FIX, always — credibility doesn't scale down |
| Checking code by reading, not running | Reading is faster | Run it, or mark the snippet as unverified in the review |
| Skipping platform gates on cross-posts | The first version already passed | Each platform version gets its own compliance check — gates differ |
| Verifying links by eye | URLs look right | Resolve each one; repos get renamed and docs pages move |
| Letting a stale version claim through | It was true when the author learned it | Check current LTS/stable versions at review time, not from memory |
| Publishing without a banner image | Prose and code get all the attention | Every platform surfaces a cover; create one via image-generator-blog before submitting |

## Related Skills

- seo-optimizer — run before this review so metadata issues surface here, not after publishing
- markdown-formatter — clean, portable Markdown for the final draft
- Platform formatters: devto-formatter, medium-optimizer, dzone-article, infoq-article, javapro-magazine, substack-newsletter, linkedin-pulse-formatter, sr-tech-blog
- technical-writer agent — drafts the article; its workflow calls this skill as step 4 self-review
