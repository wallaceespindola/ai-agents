#!/usr/bin/env python3
"""Series-level checks for docs/articles/<platform>/article.md in one series repo.

Usage: python3 check_series.py [series-repo, default cwd] [--repo-url URL] [--forbid WORD ...]
Prints one row per platform; exit 1 if any FAIL. WARN items need a human look.
Stdlib only.
"""

import argparse
import re
import sys
from pathlib import Path

# (unit, min, max) from the tech-content-series matrix
LIMITS = {
    "devto": ("words", 1500, 3200),
    "dzone": ("words", 800, 4800),
    "medium": ("words", 2000, 5000),
    "linkedin": ("words", 1000, 1700),
    "substack": ("words", 1500, 2200),
    "infoq": ("words", 1500, 4000),
    "javapro": ("chars", 15000, 25000),
}
NEEDS_AI_NOTE = {"devto", "medium", "infoq"}
EDITORIAL = {"infoq", "javapro"}
AI_NOTE = re.compile(r"AI assistance|AI disclosure|AI-assisted|#abotwrotethis", re.IGNORECASE)
IMG = re.compile(r"!\[([^\]]*)\]\(([^)\s]+)\)")
FENCE = re.compile(r"^(`{3,}|~{3,})[^\n]*\n(.*?)^\1\s*$", re.MULTILINE | re.DOTALL)
SOURCES = (".mmd", ".puml", ".svg")


def strip_meta(md: str) -> str:
    md = re.sub(r"\A---\n.*?\n---\n", "", md, flags=re.DOTALL)
    return re.sub(r"<!--.*?-->", "", md, flags=re.DOTALL)


def title_of(md: str) -> str:
    m = re.search(r'^title:\s*"?(.+?)"?\s*$', md, re.MULTILINE) or re.search(r"^# (.+)$", strip_meta(md), re.MULTILINE)
    return m.group(1).strip() if m else ""


def repo_text(root: Path) -> str:
    keep = []
    for p in root.rglob("*"):
        if p.is_file() and "articles" not in p.parts and ".git" not in p.parts and p.stat().st_size < 1_000_000:
            try:
                keep.append(p.read_text(encoding="utf-8"))
            except (UnicodeDecodeError, OSError):
                pass
    return "\n".join(keep)


def check(platform: str, path: Path, md: str, args, corpus: str) -> tuple[list[str], list[str], str]:
    fails, warns = [], []
    body = strip_meta(md)
    prose = FENCE.sub("", body)
    unit, lo, hi = LIMITS.get(platform, ("words", 0, 10**9))
    size = len(body) if unit == "chars" else len(prose.split())
    if not lo <= size <= hi:
        warns.append(f"{size} {unit} outside {lo}-{hi}")
    if args.repo_url and args.repo_url not in md:
        fails.append("repo URL missing")
    ex = re.search(r"\*\*Examples repository:\*\*.*", md)
    if not ex or (args.repo_url and args.repo_url not in ex.group(0)):
        fails.append("'Examples repository' line missing or wrong URL")
    if "Wallace Espindola, Solution Architect" not in md:
        fails.append("author line 'Wallace Espindola, Solution Architect' missing")
    # InfoQ and JavaPro are editorial: an author bio is required, the promo footer is optional.
    editorial = platform in EDITORIAL
    if editorial and not re.search(r"^#+ (About the author|Author bio)", md, re.MULTILINE | re.IGNORECASE):
        fails.append("author bio section missing")
    for need in ("Need more tech insights?", "speakerdeck.com/wallacese"):
        if need not in md:
            (warns if editorial else fails).append(f"footer: '{need}' missing")
    if "—" in md:
        fails.append(f"{md.count(chr(0x2014))} em dash(es)")
    for word in args.forbid:
        if re.search(rf"\b{re.escape(word)}\b", md, re.IGNORECASE):
            fails.append(f"forbidden word '{word}'")
    imgs = IMG.findall(body)
    if not any(Path(src).name.startswith("banner.") for _, src in imgs):
        fails.append("no banner image")
    diagrams = [(alt, src) for alt, src in imgs if "diagrams/" in src]
    if not diagrams:
        fails.append("no diagram")
    for alt, src in imgs:
        f = path.parent / src
        if src.startswith("http"):
            continue
        if not f.exists():
            fails.append(f"missing image {src}")
        if not alt.strip():
            fails.append(f"empty alt text: {src}")
        if "diagrams/" in src and not any(f.with_suffix(s).exists() for s in SOURCES):
            fails.append(f"no .mmd/.puml/.svg source next to {src}")
        if platform == "infoq" and not src.lower().endswith((".jpg", ".jpeg")):
            fails.append(f"InfoQ image not JPEG: {src}")
    if platform in NEEDS_AI_NOTE and not AI_NOTE.search(md):
        fails.append("AI disclosure missing")
    if platform == "dzone":
        warns.append("DZone: author must write or fully rewrite the text before submitting")
    if platform == "linkedin" and re.search(r"^\s*\|.*\|\s*$", prose, re.MULTILINE):
        fails.append("table present (LinkedIn can't render tables)")
    if platform == "infoq":
        kt = re.search(r"Key Takeaways\**\s*\n+((?:\s*- .+\n?)+)", body)
        n = len(re.findall(r"^\s*- ", kt.group(1), re.MULTILINE)) if kt else 0
        if n != 5:
            fails.append(f"{n} key takeaways (need exactly 5)")
    # Snippets must come from the repo: every non-trivial line of each code block should exist there.
    unmatched = 0
    for _, code in FENCE.findall(body):
        lines = [ln.strip() for ln in code.splitlines() if len(ln.strip()) > 12]
        if lines and sum(ln in corpus for ln in lines) < len(lines) * 0.8:
            unmatched += 1
    if unmatched:
        warns.append(f"{unmatched} code block(s) not found verbatim in the repo")
    return fails, warns, f"{size} {unit}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("root", type=Path, nargs="?", default=Path.cwd(), help="series repo (default: current dir)")
    ap.add_argument("--repo-url", default="")
    ap.add_argument("--forbid", nargs="*", default=[], help="e.g. the employer's name or internal tools")
    args = ap.parse_args()
    articles = sorted((args.root / "docs" / "articles").glob("*/article.md"))
    if not articles:
        print("no docs/articles/<platform>/article.md found")
        return 1
    corpus = repo_text(args.root)
    titles: dict[str, str] = {}
    bad = False
    print(f"{'platform':10} {'size':>12}  result")
    for path in articles:
        platform = path.parent.name
        md = path.read_text(encoding="utf-8")
        fails, warns, size = check(platform, path, md, args, corpus)
        t = title_of(md).lower()
        if t in titles:
            fails.append(f"title duplicates {titles[t]}")
        titles[t] = platform
        bad |= bool(fails)
        print(f"{platform:10} {size:>12}  {'FAIL' if fails else 'PASS'}")
        for item in fails:
            print(f"{'':25}FAIL {item}")
        for item in warns:
            print(f"{'':25}WARN {item}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
