---
name: linkedin-group-posting
description: Share a published LinkedIn Pulse article (or any article URL) to the LinkedIn groups the author belongs to, picking the largest groups that fit the article's topic, with a varied post text per group (Portuguese for Brazilian groups). Use when asked to "post my article to LinkedIn groups", "share in 20 relevant groups", "spread the article in my groups".
---

# LinkedIn group posting

Shares one live article to N of the author's LinkedIn groups through Claude-in-Chrome. Verified 2026-11-22
(20 groups, Flyway vs Liquibase series). Runs only on the author's command, after the article is live.

## 1. Rules

- **Choose groups by topic relevance first, then member count.** Topic groups (for example Java/Spring for a
  Java article) come first, largest to smallest. Then large general dev/architecture/IT groups.
  Skip groups that are off topic, about jobs or recruiting, startups, BI or QA only, or mobile/telecom.
- **Never post to JUG groups** (Java User Groups, for example BeJUG) or to any group the author excludes.
- **Brazilian groups get the text in Portuguese** ("Artigo (em inglês): <url>"). All other groups get English.
- **Vary the text for each group.** Mix openers, middle paragraphs, link labels and closing questions so no
  two posts are identical. Mention the facts the author asks for (stack versions, for example "Java 25").
  Use no em dashes and no AI disclosure. Each post is 3 or 4 short paragraphs with the URL on its own line
  and one question at the end.
- **Confirm before posting.** Show the author the ranked list (name, members, language) and two sample texts
  and wait for a yes. Group posts are public actions.

## 2. List groups and measure members

1. Open `https://www.linkedin.com/groups/`. Scroll and click "Show more" until the list stops growing.
2. Collect `{id, name}` from links matching `/groups/<id>/`.
3. Member counts: a static `fetch` of the group HTML returns wrong numbers. Load each group in a hidden
   same-origin iframe instead and read the rendered text:

```js
window.__m = id => new Promise(res => {
  const f = document.createElement('iframe'); f.style.display = 'none';
  f.src = `/groups/${id}/`; document.body.appendChild(f);
  let n = 0; const t = setInterval(() => {
    const m = f.contentDocument?.body?.innerText.match(/([\d,.]+K?)\s+members/);
    if (m || ++n > 30) { clearInterval(t); f.remove(); res(`${id}:${m ? m[1] : '?'}`); }
  }, 500);
});
await Promise.all([111, 222, 333].map(__m));   // batches of about 6
```

Save the ranked list with its texts to the scratchpad (`groups.json`: id, name, members, text, lang).

## 3. Post, one group per step

Typing with the `computer` `type` action often goes nowhere, because the composer's first input is lost while
it initialises. Insert the text with `execCommand` instead. Then check that the text appears exactly once,
click Post, and wait for the toast. Use one `browser_batch` per group or two: navigate, wait 2 s, then
`javascript_exec`:

```js
const T = "<post text with \\n newlines>";
const sl = ms => new Promise(r => setTimeout(r, ms));
let b; for (let i = 0; i < 15 && !b; i++) {
  b = [...document.querySelectorAll('button')]
    .find(b => /Start a (public )?post/i.test(b.innerText + b.getAttribute('aria-label')));
  if (!b) await sl(700);
}
if (!b) 'no start button'; else {
  b.click(); let ed;
  for (let i = 0; i < 15 && !ed; i++) { await sl(500); ed = document.querySelector('[role=dialog] [contenteditable=true]'); }
  await sl(1500); ed.focus();
  const ps = T.split('\n');
  ps.forEach((p, i) => { if (p) document.execCommand('insertText', false, p);
                         if (i < ps.length - 1) document.execCommand('insertParagraph'); });
  await sl(2500);
  const d = document.querySelector('[role=dialog]');
  const to = d.innerText.match(/Post to [^\n]*/)?.[0];
  if ((ed.innerText.split(T.slice(0, 30)).length - 1) !== 1) 'text check failed';
  else {
    [...d.querySelectorAll('button')].find(b => b.innerText.trim() === 'Post').click();
    let r = 'no confirmation';
    for (let i = 0; i < 15; i++) { await sl(700);
      const m = document.body.innerText.match(/Post successful|submitted to the group admin for approval/i);
      if (m) { r = m[0]; break; } }
    to + ' -> ' + r;
  }
}
```

- Public groups label the button "Start a public post". The regex covers both labels.
- "submitted to the group admin for approval" means the group is moderated and the post is pending. Count it
  as posted, but report it as pending.
- Wait at least 20 s between groups (two `wait` 10 s actions: `wait` is capped at 10 s). Spread runs of more
  than about 20 groups over several sessions, so LinkedIn does not rate-limit or flag the account.
- After `navigate`, the first `javascript_exec` can fail with "Cannot access a chrome-extension:// URL".
  Retry it once.
- On "no start button", the author cannot post in that group. Skip it, pick the next group from the ranked
  list and tell the author.

## 4. Report

Report a table of the groups posted to, with group, members, language and status (posted or pending approval),
plus the total reach and any groups that were skipped and why.

## Related skills

`linkedin-pulse-formatter` (the article itself), `article-cross-posting` (drafts on every platform),
`profile-articles-sync`.
