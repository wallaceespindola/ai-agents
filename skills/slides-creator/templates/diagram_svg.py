"""House diagram style: hand-written SVG sources in the deck palette.

Kinds: legacy (navy, system of record), bridge (indigo, transitional), modern (teal, new platform),
warn (amber, control or risk), neutral (slate). Usage: python3 diagram_svg.py <out_dir>
"""
import sys
from pathlib import Path

OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
FONT = "Helvetica Neue, Helvetica, Arial, sans-serif"

# kind -> (fill, stroke, title color, sub color)
STYLE = {
    "modern": ("#ecfdf9", "#14b8a6", "#0b3b36", "#0f766e"),
    "legacy": ("#0f1b3d", "#0f1b3d", "#ffffff", "#a5b4fc"),
    "bridge": ("#eef2ff", "#6366f1", "#1e1b4b", "#4f46e5"),
    "neutral": ("#f8fafc", "#94a3b8", "#0f172a", "#475569"),
    "warn": ("#fff7ed", "#f59e0b", "#7c2d12", "#b45309"),
}


def head(w, h):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" font-family="{FONT}">
  <defs>
    <marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="#334155"/>
    </marker>
    <marker id="aw" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="#d97706"/>
    </marker>
    <filter id="s" x="-10%" y="-10%" width="120%" height="140%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#0f172a" flood-opacity="0.12"/>
    </filter>
  </defs>
  <rect width="{w}" height="{h}" fill="#ffffff"/>
'''


def box(x, y, w, h, title, sub="", kind="modern", tag=""):
    fill, stroke, tc, sc = STYLE[kind]
    cx = x + w / 2
    out = [f'  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="{fill}" stroke="{stroke}" stroke-width="2.5" filter="url(#s)"/>']
    if tag:
        out.append(f'  <text x="{x + 18}" y="{y + 28}" font-size="15" font-weight="700" letter-spacing="1.5" fill="{sc}">{tag}</text>')
    lines = sub.split("|") if sub else []
    ty = y + h / 2 + (6 if not lines else -10 * len(lines) + 4) + (10 if tag else 0)
    out.append(f'  <text x="{cx}" y="{ty}" text-anchor="middle" font-size="24" font-weight="700" fill="{tc}">{title}</text>')
    for i, line in enumerate(lines):
        out.append(f'  <text x="{cx}" y="{ty + 30 + i * 25}" text-anchor="middle" font-size="19" fill="{sc}">{line}</text>')
    return "\n".join(out)


def arrow(points, label="", lx=None, ly=None, dashed=False, warn=False, anchor="middle"):
    d = " ".join(("M" if i == 0 else "L") + f"{x},{y}" for i, (x, y) in enumerate(points))
    color = "#d97706" if warn else "#334155"
    dash = ' stroke-dasharray="9 7"' if dashed else ""
    out = [f'  <path d="{d}" fill="none" stroke="{color}" stroke-width="2.5"{dash} marker-end="url(#{"aw" if warn else "a"})"/>']
    if label:
        out.append(f'  <text x="{lx}" y="{ly}" text-anchor="{anchor}" font-size="18" font-style="italic" fill="{color}">{label}</text>')
    return "\n".join(out)


def legend(x, y, items):
    out = []
    for i, (kind, text) in enumerate(items):
        fill, stroke, _, _ = STYLE[kind]
        xx = x + i * 260
        out.append(f'  <rect x="{xx}" y="{y - 16}" width="22" height="22" rx="6" fill="{fill}" stroke="{stroke}" stroke-width="2.5"/>')
        out.append(f'  <text x="{xx + 34}" y="{y + 1}" font-size="18" fill="#475569">{text}</text>')
    return "\n".join(out)


def save(name, w, h, parts):
    (OUT / name).write_text(head(w, h) + "\n".join(parts) + "\n</svg>\n")


# Example: one row of stages with a dashed rollback loop. Copy the helpers, write one save() per diagram,
# then render each SVG with: rsvg-convert -z 2 -b white x.svg -o x.png
if __name__ == "__main__":
    parts = []
    for i, (title, sub, kind) in enumerate([("Shadow", "compared, discarded", "bridge"),
                                            ("Canary", "small segment", "modern"),
                                            ("Cutover", "all traffic on new", "modern")]):
        x = 40 + i * 340
        parts.append(box(x, 50, 280, 130, title, sub, kind))
        if i:
            parts.append(arrow([(x - 56, 115), (x - 4, 115)]))
    parts.append(arrow([(520, 180), (520, 250), (180, 250), (180, 184)], "back to shadow", 350, 280, dashed=True, warn=True))
    save("example-stages.svg", 1080, 310, parts)
