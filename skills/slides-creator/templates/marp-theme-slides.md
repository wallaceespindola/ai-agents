---
marp: true
theme: default
paginate: true
size: 16:9
footer: '<Deck title>'
style: |
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');
  :root {
    --ink: #0b1530; --text: #1e293b; --muted: #64748b; --line: #e2e8f0;
    --teal: #14b8a6; --teal-dark: #0f766e; --teal-soft: #ecfdf9; --indigo: #6366f1;
  }
  section {
    font-family: 'Inter', 'Helvetica Neue', Arial, sans-serif;
    font-size: 26px; line-height: 1.5; color: var(--text);
    padding: 64px 80px 70px;
    background:
      radial-gradient(circle at 100% 0%, rgba(20, 184, 166, 0.10), transparent 32%),
      radial-gradient(circle at 0% 100%, rgba(99, 102, 241, 0.08), transparent 30%),
      #f8fafc;
    justify-content: flex-start;
  }
  h1 {
    position: relative; font-size: 44px; font-weight: 800; letter-spacing: -0.02em;
    color: var(--ink); margin: 0 0 26px; padding-top: 22px;
  }
  h1::before {
    content: ''; position: absolute; top: 0; left: 0; width: 72px; height: 6px; border-radius: 3px;
    background: linear-gradient(90deg, var(--teal), var(--indigo));
  }
  h2 { color: var(--ink); }
  strong { color: var(--teal-dark); font-weight: 700; }
  a { color: var(--teal-dark); text-decoration: none; }
  ul { list-style: none; padding-left: 0; margin: 0 0 18px; }
  ul > li { position: relative; padding-left: 34px; margin: 10px 0; }
  ul > li::before {
    content: ''; position: absolute; left: 4px; top: 0.55em; width: 12px; height: 12px; border-radius: 3px;
    background: linear-gradient(135deg, var(--teal), var(--indigo));
  }
  ol { list-style: none; counter-reset: step; padding-left: 0; margin: 0; }
  ol > li { counter-increment: step; position: relative; padding-left: 52px; margin: 9px 0; font-size: 24px; }
  ol > li::before {
    content: counter(step); position: absolute; left: 0; top: 2px; width: 34px; height: 34px; border-radius: 50%;
    background: var(--ink); color: #fff; font-size: 17px; font-weight: 700; text-align: center; line-height: 34px;
  }
  ul + p, ol + p, table + p {
    margin-top: 18px; padding: 16px 24px; border-left: 6px solid var(--teal); border-radius: 0 14px 14px 0;
    background: var(--teal-soft); color: var(--ink); font-weight: 500;
  }
  code {
    font-family: 'JetBrains Mono', Menlo, Consolas, monospace; font-size: 0.86em; font-variant-ligatures: none;
    background: #e6f7f4; color: var(--teal-dark); padding: 2px 8px; border-radius: 6px;
  }
  pre {
    background: #0f172a; border-radius: 16px; padding: 18px 26px; margin: 0;
    box-shadow: 0 18px 40px -18px rgba(15, 23, 42, 0.55); font-size: 0.52em; line-height: 1.45;
  }
  pre code { background: none; color: #e2e8f0; padding: 0; font-size: 1em; }
  pre + p { margin-top: 10px; font-size: 18px; color: var(--muted); }
  pre + p code { background: none; color: var(--muted); padding: 0; }
  .hljs-keyword, .hljs-built_in { color: #c4b5fd; }
  .hljs-title, .hljs-title.function_ { color: #5eead4; }
  .hljs-string { color: #fcd34d; }
  .hljs-comment { color: #94a3b8; font-style: italic; }
  .hljs-type, .hljs-class { color: #7dd3fc; }
  .hljs-literal, .hljs-number { color: #fda4af; }
  .hljs-variable, .hljs-params { color: #bae6fd; }
  table {
    display: table; border-collapse: separate; border-spacing: 0; width: 100%; font-size: 19px;
    border-radius: 14px; overflow: hidden; box-shadow: 0 10px 30px -18px rgba(15, 23, 42, 0.45);
  }
  th { background: var(--ink); color: #fff; font-weight: 600; text-align: left; padding: 7px 20px; border: none; }
  td { background: #fff; padding: 5px 20px; border: none; border-bottom: 1px solid var(--line); }
  tr:nth-child(even) td { background: #f1f5f9; }
  td:first-child { font-weight: 600; color: var(--ink); }
  footer { left: 80px; bottom: 26px; font-size: 15px; color: var(--muted); letter-spacing: 0.04em; }
  section::after {
    right: 64px; bottom: 22px; font-size: 15px; font-weight: 600; color: #fff;
    background: var(--ink); border-radius: 999px; padding: 4px 14px;
  }
  section.diagram p { text-align: center; }
  section.diagram img {
    background: #fff; border-radius: 18px; padding: 18px;
    box-shadow: 0 18px 40px -20px rgba(15, 23, 42, 0.45);
  }
  section.diagram p:last-child:not(:has(img)) {
    margin-top: 22px; font-size: 24px; color: var(--ink);
  }
  section.lead {
    justify-content: center; padding: 80px 110px;
    color: #e2e8f0;
    background:
      radial-gradient(circle at 85% 15%, rgba(45, 212, 191, 0.35), transparent 40%),
      radial-gradient(circle at 5% 95%, rgba(99, 102, 241, 0.45), transparent 45%),
      linear-gradient(135deg, #0b1530 0%, #111c44 60%, #1e1b4b 100%);
  }
  section.lead h1 {
    font-size: 76px; line-height: 1.08; margin-bottom: 18px; padding-top: 30px;
    color: #ffffff;
  }
  section.lead h1::before { width: 96px; height: 8px; border-radius: 4px; }
  section.lead h2 { color: #cbd5e1; font-size: 34px; font-weight: 500; margin: 0 0 46px; }
  section.lead p { color: #cbd5e1; font-size: 23px; margin: 4px 0; }
  section.lead strong { color: #fff; }
  section.lead a { color: #5eead4; }
---

<!-- _class: lead -->
<!-- _footer: '' -->
<!-- _paginate: false -->

# <Deck title>

## <Subtitle>

**Wallace Espindola**
Solution Architect

<wallace.espindola@gmail.com>
linkedin.com/in/wallaceespindola | github.com/wallaceespindola

<!--
Speaker notes go in HTML comments.
-->

---

# Content slide title

- Bullet with a **key term** highlighted in teal
- Keep 4 to 6 bullets per slide

A paragraph right after a list renders as a teal callout: use it for the one takeaway.

---

<!-- _class: diagram -->

# Diagram slide title

![w:1060](diagrams/example.png)

---

<!-- _class: lead -->
<!-- _footer: '' -->
<!-- _paginate: false -->

# Thank you

## Code, docs, diagrams and slides

[github.com/wallaceespindola/<repo>](https://github.com/wallaceespindola/<repo>)

**Wallace Espindola**, Solution Architect
linkedin.com/in/wallaceespindola | speakerdeck.com/wallacese
