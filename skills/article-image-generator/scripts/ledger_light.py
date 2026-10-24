"""Legacy Ledger Light banners (the default house style is now generate_banner.py --style aurora): a drained capacity field, a full one, and a document travelling between them.

Made with the canvas-design skill for a series on sharing AI coding capacity; fits topics about capacity,
quotas, delegation, handoffs and moving work between parties. See ../SKILL.md.
"""
import argparse
import glob
import math
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

FONTS = Path(sorted(glob.glob(str(Path.home() / ".claude/plugins/cache/anthropic-agent-skills/*/*/skills/canvas-design/canvas-fonts")))[-1])
THIN = str(FONTS / "Jura-Light.ttf")
MONO = str(FONTS / "GeistMono-Regular.ttf")
SS = 2  # supersampling

PALETTES = {
    "cyan":    ("#040913", "#0B1A33", "#43E5D0", "#6AA8FF"),
    "violet":  ("#07051A", "#1A1240", "#B48CFF", "#5EE1FF"),
    "amber":   ("#0C0907", "#24170C", "#FFB454", "#FF7A59"),
    "ice":     ("#040A12", "#0E2234", "#9FE8FF", "#E6F6FF"),
    "lime":    ("#030B07", "#0A1F15", "#7CF29A", "#3DD6C6"),
    "magenta": ("#0D0613", "#25102E", "#FF6EC7", "#8C7CFF"),
    "azure":   ("#03081A", "#0A1A40", "#5B9DFF", "#43E5D0"),
}


def rgb(h, a=255):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4)) + (a,)


def mix(c1, c2, t):
    return tuple(round(a + (b - a) * t) for a, b in zip(c1, c2))


def background(w, h, c0, c1, rnd):
    sw, sh = max(2, w // 16), max(2, h // 16)
    img = Image.new("RGB", (sw, sh))
    px = img.load()
    a, b = rgb(c0)[:3], rgb(c1)[:3]
    for y in range(sh):
        for x in range(sw):
            t = min(1, max(0, 0.65 * x / sw + 0.35 * (1 - y / sh)))
            px[x, y] = mix(a, b, t * t)
    img = img.resize((w, h), Image.BICUBIC)
    # soft vignette + fine grain
    vig = Image.new("L", (w, h), 0)
    ImageDraw.Draw(vig).ellipse((-w * 0.25, -h * 0.6, w * 1.25, h * 1.6), fill=255)
    vig = vig.filter(ImageFilter.GaussianBlur(w * 0.08))
    img = Image.composite(img, Image.new("RGB", (w, h), mix(a, (0, 0, 0), 0.5)), vig)
    noise = Image.effect_noise((w, h), 9).convert("RGB")
    return Image.blend(img, noise, 0.025).convert("RGBA")


def lattice(d, w, h, pitch, col):
    for y in range(pitch // 2, h, pitch):
        for x in range(pitch // 2, w, pitch):
            d.point((x, y), fill=col)


def crop_marks(d, box, ln, col, wd):
    x0, y0, x1, y1 = box
    for (x, y, sx, sy) in ((x0, y0, 1, 1), (x1, y0, -1, 1), (x0, y1, 1, -1), (x1, y1, -1, -1)):
        d.line((x, y, x + sx * ln, y), fill=col, width=wd)
        d.line((x, y, x, y + sy * ln), fill=col, width=wd)


def field(cols, rows, fill_ratio, rnd, bias):
    """Lit cells; bias>0 keeps lit cells low (drained from the top), bias<0 keeps the gaps high."""
    cells = []
    for r in range(rows):
        for c in range(cols):
            depth = r / (rows - 1)
            p = fill_ratio + bias * (depth - 0.5)
            cells.append((c, r, rnd.random() < p))
    return cells


def draw_field(base, glow, origin, cells, s, g, acc, acc2, rnd, wd):
    d, dg = ImageDraw.Draw(base), ImageDraw.Draw(glow)
    ox, oy = origin
    rad = s * 0.18
    for c, r, lit in cells:
        x, y = ox + c * (s + g), oy + r * (s + g)
        box = (x, y, x + s, y + s)
        if lit:
            col = acc if rnd.random() > 0.22 else acc2
            a = rnd.choice((150, 190, 230, 255))
            d.rounded_rectangle(box, rad, fill=rgb(col, a))
            dg.rounded_rectangle(box, rad, fill=rgb(col, a))
        else:
            d.rounded_rectangle(box, rad, outline=rgb(acc, 34), width=wd)


def render(size, palette, words, seed, out, label=None, left=None, right=None):
    W, H = size
    w, h = W * SS, H * SS
    rnd = random.Random(seed)
    c0, c1, acc, acc2 = PALETTES[palette]
    img = background(w, h, c0, c1, rnd)
    glow = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    hair = max(1, SS)

    lattice(d, w, h, max(18, h // 34), rgb("#FFFFFF", 22))

    # instrument region: right side, vertically centred
    portrait = W / H < 1.5
    rx0, rx1 = w * (0.47 if not portrait else 0.44), w * 0.95
    ry0, ry1 = h * 0.2, h * 0.8
    rows = 7 if not portrait else 8
    span_h = ry1 - ry0
    s = span_h / (rows + (rows - 1) * 0.42)
    g = s * 0.42
    cols = max(3, int(((rx1 - rx0) * 0.36 + g) / (s + g)))
    fw = cols * s + (cols - 1) * g
    gap = (rx1 - rx0) - 2 * fw
    ax, bx = rx0, rx1 - fw
    oy = ry0

    drained = field(cols, rows, 0.1, rnd, 0.22)
    full = field(cols, rows, 0.8, rnd, 0.35)
    draw_field(img, glow, (ax, oy), drained, s, g, acc, acc2, rnd, hair)
    draw_field(img, glow, (bx, oy), full, s, g, acc, acc2, rnd, hair)

    # route: A -> B hairline with a soft step, spec glyph riding on it
    ya = oy + span_h * 0.42
    yb = oy + span_h * 0.36
    x_a, x_b = ax + fw + g * 1.2, bx - g * 1.2
    pts = []
    for i in range(101):
        t = i / 100
        e = t * t * (3 - 2 * t)
        pts.append((x_a + (x_b - x_a) * t, ya + (yb - ya) * e))
    d.line(pts, fill=rgb(acc, 210), width=hair)
    ImageDraw.Draw(glow).line(pts, fill=rgb(acc, 200), width=hair * 3)
    # dotted return path B -> A, below
    yr = oy + span_h * 0.7
    n = max(6, int((x_b - x_a) / (s * 0.55)))
    for i in range(n + 1):
        x = x_b - (x_b - x_a) * i / n
        rr = hair * 1.4
        d.ellipse((x - rr, yr - rr, x + rr, yr + rr), fill=rgb(acc2, 150))
    # spec glyph
    gx = x_a + (x_b - x_a) * 0.5
    gy = ya + (yb - ya) * 0.5
    gw, gh = s * 1.15, s * 1.5
    box = (gx - gw / 2, gy - gh / 2, gx + gw / 2, gy + gh / 2)
    d.rounded_rectangle(box, s * 0.14, fill=rgb(c0), outline=rgb(acc, 255), width=hair * 2)
    ImageDraw.Draw(glow).rounded_rectangle(box, s * 0.14, outline=rgb(acc, 255), width=hair * 5)
    for k, frac in enumerate((0.72, 0.56, 0.38)):
        ly = box[1] + gh * (0.3 + k * 0.2)
        d.line((box[0] + gw * 0.2, ly, box[0] + gw * (0.2 + frac * 0.6), ly), fill=rgb(acc2, 230), width=hair * 2)

    # glow composite
    g1 = glow.filter(ImageFilter.GaussianBlur(s * 0.35))
    g2 = glow.filter(ImageFilter.GaussianBlur(s * 1.2))
    img = Image.alpha_composite(img, g2.point(lambda v: v * 0.55))
    img = Image.alpha_composite(img, g1.point(lambda v: v * 0.7))
    d = ImageDraw.Draw(img)

    # crop marks and reference markers
    pad = s * 0.8
    crop_marks(d, (rx0 - pad, ry0 - pad, rx1 + pad, ry1 + pad), s * 0.7, rgb("#FFFFFF", 90), hair)
    mono = ImageFont.truetype(MONO, max(int(h * 0.026), 11 * SS))
    lab_y = ry1 + pad + s * 0.25
    if lab_y + mono.size < h * 0.97:  # markers are opt-in: the house style avoids micro-text
        if left:
            d.text((ax, lab_y), left, font=mono, fill=rgb("#FFFFFF", 120))
        if right:
            d.text((bx, lab_y), right, font=mono, fill=rgb("#FFFFFF", 120))
        if label:
            tw = d.textlength(label, font=mono)
            d.text((gx - tw / 2, lab_y), label, font=mono, fill=rgb(acc, 200))

    # words: thin, left, vertically centred, accent rule above
    if words:
        tx0 = w * 0.065
        tmax = (rx0 - pad) - tx0 - w * 0.06
        size = h * (0.13 if not portrait else 0.085)
        lines = [words]
        while True:
            f = ImageFont.truetype(THIN, int(size))
            widest = max(d.textlength(l, font=f) for l in lines)
            if widest <= tmax:
                break
            if len(lines) == 1 and " " in words and size < h * 0.1:
                parts = words.split()
                k = min(range(1, len(parts)), key=lambda i: abs(len(" ".join(parts[:i])) - len(" ".join(parts[i:]))))
                lines = [" ".join(parts[:k]), " ".join(parts[k:])]
                size = h * (0.13 if not portrait else 0.085)
                continue
            size *= 0.94
        lh = f.size * 1.12
        block = lh * len(lines)
        ty = h / 2 - block / 2
        rule_y = ty - f.size * 0.35
        d.line((tx0, rule_y, tx0 + f.size * 0.9, rule_y), fill=rgb(acc, 255), width=hair * 2)
        for i, l in enumerate(lines):
            d.text((tx0, ty + i * lh), l, font=f, fill=rgb("#F4F7FB", 255))

    final = img.convert("RGB").resize((W, H), Image.LANCZOS)
    out = Path(out)
    if out.suffix == ".jpg":
        final.save(out, quality=90, optimize=True)
    else:
        final.save(out, optimize=True)
    print(out, final.size)


SIZES = {"devto": (1000, 420), "medium": (1200, 627), "linkedin": (1920, 1080), "substack": (1200, 630),
         "dzone": (1200, 628), "infoq": (1024, 768), "javapro": (1200, 630), "blog": (1200, 630),
         "og": (1200, 630), "slide": (1920, 1080), "readme": (1280, 400)}

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--platform", choices=SIZES, default="blog")
    ap.add_argument("--size", help="WxH override, e.g. 1600x900")
    ap.add_argument("--palette", choices=PALETTES, default="cyan")
    ap.add_argument("--text", default="", help="0-4 words, thin face on the left")
    ap.add_argument("--label", help="tiny mono marker under the travelling document, e.g. TASK-042")
    ap.add_argument("--left", help="optional marker under the drained field")
    ap.add_argument("--right", help="optional marker under the full field")
    ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--out", required=True, help=".png, or .jpg for JPEG (InfoQ)")
    a = ap.parse_args()
    if len(a.text.split()) > 4:
        ap.error("--text takes at most 4 words")
    size = tuple(map(int, a.size.lower().split("x"))) if a.size else SIZES[a.platform]
    render(size, a.palette, a.text, a.seed, a.out, a.label, a.left, a.right)
