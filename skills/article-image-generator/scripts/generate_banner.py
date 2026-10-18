#!/usr/bin/env python3
"""Generate a modern, abstract, futuristic article banner with minimal text.

Usage:
  uv run --with pillow python generate_banner.py --platform devto --text "Share the work" \
      --style network --palette midnight --seed 7 --out banner.png
"""
import argparse
import math
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

# Cover sizes (w, h), checked 2026-10. Re-check platform help pages before relying on them; see SKILL.md.
PLATFORMS = {
    "devto": (1000, 420),
    "medium": (1200, 627),
    "linkedin": (1920, 1080),
    "substack": (1200, 630),
    "dzone": (1200, 628),
    "infoq": (1024, 768),
    "javapro": (1200, 630),
    "blog": (1200, 630),
    "og": (1200, 630),
    "slide": (1920, 1080),
}

# (background top-left, background bottom-right, accent 1, accent 2, glow)
PALETTES = {
    "midnight": ((8, 12, 32), (30, 18, 72), (0, 212, 255), (168, 85, 247), (90, 200, 255)),
    "aurora": ((4, 22, 30), (10, 40, 70), (52, 245, 197), (56, 189, 248), (120, 255, 220)),
    "ember": ((20, 8, 24), (60, 14, 48), (255, 122, 69), (244, 63, 151), (255, 170, 120)),
    "violet": ((14, 8, 36), (48, 16, 96), (196, 132, 252), (99, 102, 241), (220, 180, 255)),
    "ice": ((10, 18, 34), (24, 44, 78), (148, 226, 255), (226, 232, 240), (180, 230, 255)),
    "matrix": ((2, 14, 10), (8, 36, 26), (34, 255, 136), (0, 200, 160), (120, 255, 180)),
}

FONTS = [
    "/System/Library/Fonts/Avenir Next.ttc",
    "/System/Library/Fonts/HelveticaNeue.ttc",
    "/System/Library/Fonts/SFNS.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
]


def gradient(w, h, c1, c2):
    img = Image.new("RGB", (w, h))
    px = img.load()
    for y in range(h):
        for x in range(w):
            t = (x / w * 0.6 + y / h * 0.4)
            px[x, y] = tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))
    return img


def glow_layer(size, draw_fn, blur):
    layer = Image.new("RGBA", size, (0, 0, 0, 0))
    draw_fn(ImageDraw.Draw(layer))
    return layer.filter(ImageFilter.GaussianBlur(blur))


def rgba(c, a):
    return (*c, a)


def style_network(d, w, h, pal, rnd):
    a1, a2 = pal[2], pal[3]
    hub = (w * rnd.uniform(0.62, 0.72), h * 0.5)
    nodes = [(rnd.uniform(0.05, 0.95) * w, rnd.uniform(0.1, 0.9) * h) for _ in range(26)]
    for n in nodes:
        d.line([n, hub], fill=rgba(a1, 40), width=1)
    for i, n in enumerate(nodes):
        m = nodes[(i * 7 + 3) % len(nodes)]
        if math.dist(n, m) < w * 0.3:
            d.line([n, m], fill=rgba(a2, 55), width=1)
    for n in nodes:
        r = rnd.uniform(2, 6)
        d.ellipse([n[0] - r, n[1] - r, n[0] + r, n[1] + r], fill=rgba(rnd.choice([a1, a2]), 220))
    # document glyph at the hub
    dw, dh = h * 0.2, h * 0.26
    x0, y0 = hub[0] - dw / 2, hub[1] - dh / 2
    d.rounded_rectangle([x0, y0, x0 + dw, y0 + dh], radius=8, outline=rgba(a1, 255), width=3)
    for k in range(3):
        y = y0 + dh * (0.32 + k * 0.18)
        d.line([x0 + dw * 0.2, y, x0 + dw * (0.8 - k * 0.15), y], fill=rgba(a2, 230), width=3)


def style_flow(d, w, h, pal, rnd):
    for k in range(14):
        c = pal[2] if k % 2 else pal[3]
        amp, ph, yb = h * rnd.uniform(0.05, 0.18), rnd.uniform(0, 6.28), h * (0.2 + k * 0.045)
        pts = [(x, yb + amp * math.sin(x / w * 6.28 * 1.3 + ph)) for x in range(0, w + 10, 10)]
        d.line(pts, fill=rgba(c, 70 + k * 8), width=2)


def style_grid(d, w, h, pal, rnd):
    horizon, cx = h * rnd.uniform(0.4, 0.5), w * rnd.uniform(0.66, 0.8)
    for i in range(-20, 21):
        d.line([(cx + i * w * 0.02, horizon), (cx + i * w * 0.18, h)], fill=rgba(pal[2], 70), width=1)
    for j in range(1, 14):
        y = horizon + (h - horizon) * (j / 13) ** 2
        d.line([(0, y), (w, y)], fill=rgba(pal[3], 60 + j * 8), width=1)
    r = h * 0.22
    d.ellipse([cx - r, horizon - r * 1.6, cx + r, horizon + r * 0.4], outline=rgba(pal[4], 200), width=4)


def style_orbit(d, w, h, pal, rnd):
    cx, cy = w * rnd.uniform(0.7, 0.8), h * rnd.uniform(0.42, 0.58)
    for k in range(7):
        rx, ry = h * (0.12 + k * 0.09) * 1.6, h * (0.12 + k * 0.09)
        d.ellipse([cx - rx, cy - ry, cx + rx, cy + ry], outline=rgba(pal[2] if k % 2 else pal[3], 90), width=2)
        a = rnd.uniform(0, 6.28)
        px, py = cx + rx * math.cos(a), cy + ry * math.sin(a)
        d.ellipse([px - 6, py - 6, px + 6, py + 6], fill=rgba(pal[4], 240))
    d.ellipse([cx - 14, cy - 14, cx + 14, cy + 14], fill=rgba(pal[2], 255))


def style_tiles(d, w, h, pal, rnd):
    s = h // 9
    for y in range(0, h, s):
        for x in range(0, w, s):
            in_text_zone = x < w * 0.6 and h * 0.3 < y < h * 0.7
            lit = not in_text_zone and rnd.random() < 0.05 + 0.45 * (x / w) ** 2
            c = rnd.choice([pal[2], pal[3]])
            d.rounded_rectangle([x + 4, y + 4, x + s - 4, y + s - 4], radius=6,
                                fill=rgba(c, rnd.randint(140, 230) if lit else 18))


STYLES = {"network": style_network, "flow": style_flow, "grid": style_grid,
          "orbit": style_orbit, "tiles": style_tiles}


def load_font(px):
    """First upright bold-ish face found; collections are searched by style name."""
    for f in FONTS:
        if not Path(f).exists():
            continue
        for i in range(12 if f.endswith(".ttc") else 1):
            try:
                font = ImageFont.truetype(f, px, index=i)
            except OSError:
                break
            if font.getname()[1] in ("Demi Bold", "Bold", "Medium") or not f.endswith(".ttc"):
                return font
    return ImageFont.load_default()


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--platform", default="og", choices=PLATFORMS)
    p.add_argument("--size", help="override WxH, e.g. 1600x900")
    p.add_argument("--text", default="", help="at most 4 words; empty for no text")
    p.add_argument("--style", default="network", choices=STYLES)
    p.add_argument("--palette", default="midnight", choices=PALETTES)
    p.add_argument("--seed", type=int, default=1)
    p.add_argument("--out", default="banner.png")
    a = p.parse_args()

    if len(a.text.split()) > 4:
        p.error("keep --text to 4 words or fewer")
    w, h = map(int, a.size.split("x")) if a.size else PLATFORMS[a.platform]
    pal, rnd = PALETTES[a.palette], random.Random(a.seed)

    # ponytail: per-pixel gradient is O(w*h) in Python, fine for banner sizes
    img = gradient(w, h, pal[0], pal[1]).convert("RGBA")
    def blob(dr):
        for _ in range(3):
            cx, cy, r = rnd.uniform(0, w), rnd.uniform(0, h), h * rnd.uniform(0.25, 0.45)
            dr.ellipse([cx - r, cy - r, cx + r, cy + r], fill=rgba(rnd.choice(pal[2:]), 60))

    img = Image.alpha_composite(img, glow_layer((w, h), blob, h * 0.25))
    shapes = glow_layer((w, h), lambda dr: STYLES[a.style](dr, w, h, pal, random.Random(a.seed)), 0)
    img = Image.alpha_composite(img, shapes.filter(ImageFilter.GaussianBlur(6)))  # glow
    img = Image.alpha_composite(img, shapes)

    if a.text:
        # fade the left side so the words sit on calm background
        fade = Image.new("L", (w, 1))
        fade.putdata([int(200 * max(0.0, 1 - x / (w * 0.6))) for x in range(w)])
        shade = Image.new("RGBA", (w, h), (*pal[0], 255))
        shade.putalpha(fade.resize((w, h)))
        img = Image.alpha_composite(img, shade)
        font = load_font(int(h * 0.11))
        d = ImageDraw.Draw(img)
        x, y = int(w * 0.07), int(h * 0.5)  # left-aligned, vertically centred: survives centre crops
        bbox = d.textbbox((x, y), a.text, font=font, anchor="lm")
        if bbox[2] > w * 0.62:  # shrink to stay inside the safe area
            font = load_font(int(h * 0.11 * w * 0.55 / (bbox[2] - x)))
        shadow = glow_layer((w, h), lambda dr: dr.text((x, y), a.text, font=font, anchor="lm",
                                                       fill=(0, 0, 0, 200)), 8)
        img = Image.alpha_composite(img, shadow)
        ImageDraw.Draw(img).text((x, y), a.text, font=font, anchor="lm", fill=(245, 248, 255, 255))

    out = img.convert("RGB")
    if a.out.lower().endswith((".jpg", ".jpeg")):
        out.save(a.out, quality=90, optimize=True, progressive=True)
    else:
        out.save(a.out, optimize=True)
    print(f"{a.out} {w}x{h} style={a.style} palette={a.palette}")


if __name__ == "__main__":
    main()
