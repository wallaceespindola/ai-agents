#!/usr/bin/env python3
"""Generate a modern, abstract, futuristic, colorful article banner with 0-3 words of text.

Default style `aurora`: a twisting ribbon of light trails over soft nebula glows and bokeh, vivid palette.
Legacy styles (network, flow, grid, orbit, tiles) stay available with --style.

Usage:
  uv run --with pillow python generate_banner.py --platform devto --topic "copilot capacity" \
      --text "Share the work" --out banner.png
  uv run --with pillow python generate_banner.py --self-test
"""
import argparse
import math
import random
import tempfile
import zlib
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont

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
    "readme": (1280, 400),
}

# Vivid palettes for the aurora style: (deep background, mid background, (light 1, light 2, light 3)).
VIVID = {
    "nebula": ((9, 5, 28), (34, 10, 62), ((139, 92, 246), (236, 72, 153), (34, 211, 238))),
    "lagoon": ((2, 16, 26), (6, 42, 56), ((20, 184, 166), (163, 230, 53), (59, 130, 246))),
    "sunset": ((22, 6, 30), (58, 12, 52), ((251, 146, 60), (236, 72, 153), (147, 51, 234))),
    "borealis": ((3, 12, 28), (10, 30, 60), ((52, 211, 153), (56, 189, 248), (217, 70, 239))),
    "solar": ((20, 8, 10), (52, 16, 20), ((251, 191, 36), (249, 115, 22), (225, 29, 72))),
    "oceanic": ((3, 8, 30), (10, 22, 70), ((37, 99, 235), (45, 212, 191), (192, 132, 252))),
    "candy": ((18, 8, 34), (44, 16, 70), ((244, 114, 182), (192, 132, 252), (125, 211, 252))),
    "electric": ((6, 6, 26), (20, 14, 56), ((250, 204, 21), (236, 72, 153), (34, 211, 238))),
}

# Legacy palettes: (background top-left, background bottom-right, accent 1, accent 2, glow)
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
# Clean geometric face from the canvas-design plugin, when installed; system fonts otherwise.
CANVAS_FONTS = sorted(Path.home().glob(".claude/plugins/cache/*/*/*/skills/canvas-design/canvas-fonts/Outfit-*.ttf"))

SS = 2  # aurora supersampling factor


# ---------------------------------------------------------------- legacy styles


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


LEGACY = {"network": style_network, "flow": style_flow, "grid": style_grid,
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


def render_legacy(w, h, style, pal, seed, text):
    rnd = random.Random(seed)
    # ponytail: per-pixel gradient is O(w*h) in Python, fine for banner sizes
    img = gradient(w, h, pal[0], pal[1]).convert("RGBA")

    def blob(dr):
        for _ in range(3):
            cx, cy, r = rnd.uniform(0, w), rnd.uniform(0, h), h * rnd.uniform(0.25, 0.45)
            dr.ellipse([cx - r, cy - r, cx + r, cy + r], fill=rgba(rnd.choice(pal[2:]), 60))

    img = Image.alpha_composite(img, glow_layer((w, h), blob, h * 0.25))
    shapes = glow_layer((w, h), lambda dr: LEGACY[style](dr, w, h, pal, random.Random(seed)), 0)
    img = Image.alpha_composite(img, shapes.filter(ImageFilter.GaussianBlur(6)))  # glow
    img = Image.alpha_composite(img, shapes)

    if text:
        # fade the left side so the words sit on calm background
        fade = Image.new("L", (w, 1))
        fade.putdata([int(200 * max(0.0, 1 - x / (w * 0.6))) for x in range(w)])
        shade = Image.new("RGBA", (w, h), (*pal[0], 255))
        shade.putalpha(fade.resize((w, h)))
        img = Image.alpha_composite(img, shade)
        font = load_font(int(h * 0.11))
        d = ImageDraw.Draw(img)
        x, y = int(w * 0.07), int(h * 0.5)  # left-aligned, vertically centred: survives centre crops
        bbox = d.textbbox((x, y), text, font=font, anchor="lm")
        if bbox[2] > w * 0.62:  # shrink to stay inside the safe area
            font = load_font(int(h * 0.11 * w * 0.55 / (bbox[2] - x)))
        shadow = glow_layer((w, h), lambda dr: dr.text((x, y), text, font=font, anchor="lm",
                                                       fill=(0, 0, 0, 200)), 8)
        img = Image.alpha_composite(img, shadow)
        ImageDraw.Draw(img).text((x, y), text, font=font, anchor="lm", fill=(245, 248, 255, 255))
    return img.convert("RGB")


# ---------------------------------------------------------------- aurora (default)


def lerp(c1, c2, t):
    return tuple(int(a + (b - a) * t) for a, b in zip(c1, c2))


def ramp(cols, t):
    """Colour at t in [0, 1] along a three-stop ramp."""
    t = min(1.0, max(0.0, t)) * (len(cols) - 1)
    i = min(int(t), len(cols) - 2)
    return lerp(cols[i], cols[i + 1], t - i)


def scale(c, k):
    return tuple(min(255, int(v * k)) for v in c)


def smooth(e0, e1, x):
    t = min(1.0, max(0.0, (x - e0) / (e1 - e0)))
    return t * t * (3 - 2 * t)


def soft(img, radius, factor=4):
    """Cheap wide blur: shrink, blur, grow back."""
    w, h = img.size
    small = img.resize((max(1, w // factor), max(1, h // factor)), Image.BILINEAR)
    return small.filter(ImageFilter.GaussianBlur(radius / factor)).resize((w, h), Image.BICUBIC)


def aurora_font(px):
    for f in reversed(CANVAS_FONTS):  # Outfit-Regular before Outfit-Bold
        if f.name == "Outfit-Regular.ttf":
            return ImageFont.truetype(str(f), px)
    return load_font(px)


def render_aurora(w, h, pal, seed, text):
    rnd = random.Random(seed)
    W, H = w * SS, h * SS
    deep, mid, cols = pal
    if rnd.random() < 0.5:
        cols = cols[::-1]

    # base: deep diagonal gradient, rendered tiny and upscaled (smooth, no banding after grain)
    g = Image.new("RGB", (16, 9))
    g.putdata([lerp(deep, mid, smooth(0, 1, 0.55 * x / 15 + 0.45 * (1 - y / 8)) ** 2) for y in range(9) for x in range(16)])
    img = g.resize((W, H), Image.BICUBIC)

    # focal point on the right third when there is text, near centre otherwise; inside the 80% safe area
    fx = W * (rnd.uniform(0.68, 0.74) if text else rnd.uniform(0.45, 0.58))
    fy = H * rnd.uniform(0.42, 0.58)
    left_calm = (lambda x: 0.08 + 0.92 * smooth(W * 0.3, W * 0.64, x)) if text else (lambda x: 1.0)

    # nebula glows: big soft colour clouds around the focal point
    neb = Image.new("RGB", (W // 8, H // 8))
    d = ImageDraw.Draw(neb)
    for k, (dx, dy, rr, kk) in enumerate(((0, 0, 0.36, 0.5), (0.26, -0.38, 0.3, 0.45), (-0.3, 0.42, 0.28, 0.4))):
        c = cols[k]
        r = H / 8 * rr * rnd.uniform(0.85, 1.15)
        cx = fx / 8 + (dx + rnd.uniform(-0.05, 0.05)) * W / 8
        cy = fy / 8 + (dy + rnd.uniform(-0.08, 0.08)) * H / 8
        d.ellipse([cx - r * 1.5, cy - r, cx + r * 1.5, cy + r], fill=scale(c, kk * left_calm(cx * 8)))
    neb = neb.filter(ImageFilter.GaussianBlur(H / 8 * 0.18)).resize((W, H), Image.BICUBIC)
    img = ImageChops.screen(img, neb)

    # ribbons: strands of a twisting band; where the twist folds, strands bunch into bright knots
    trails = Image.new("RGB", (W, H))
    d = ImageDraw.Draw(trails)
    step = max(4, W // 320)
    for ribbon in range(2):
        main = ribbon == 0
        n = 46 if main else 22
        hw = H * (rnd.uniform(0.15, 0.22) if main else rnd.uniform(0.06, 0.1))
        tilt = rnd.uniform(0.25, 0.45) * rnd.choice((-1, 1))
        f1, p1 = rnd.uniform(0.8, 1.3), rnd.uniform(0, 6.28)
        f2, p2 = rnd.uniform(0.5, 1.0), rnd.uniform(0, 6.28)
        amp = H * (0.12 if main else 0.08)
        if main:  # put a twist knot exactly on the focal point
            p1 = math.pi / 2 - 2 * math.pi * f1 * fx / W
            knot = (fx, fy + amp * math.sin(2 * math.pi * f2 * fx / W + p2))
        yoff = 0 if main else H * rnd.uniform(0.12, 0.2) * rnd.choice((-1, 1))
        bright = 1.0 if main else 0.55
        for i in range(n):
            v = -1 + 2 * i / (n - 1)
            edge = 0.45 + 0.55 * abs(v) ** 3  # glassy bright rims, softer core
            shift = rnd.uniform(-0.04, 0.04)
            pts = []
            for x in range(-step, W + 2 * step, step):
                u = x / W
                yc = fy + yoff + (x - fx) * tilt * H / W + amp * math.sin(2 * math.pi * f2 * u + p2)
                twist = math.cos(2 * math.pi * f1 * u + p1)
                pts.append((x, yc + hw * v * twist + H * 0.004 * math.sin(9 * u + i)))
            for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
                u = x0 / W
                k = bright * edge * left_calm(x0) * (0.35 + 0.65 * math.sin(math.pi * min(1, max(0, u))))
                # iridescent: hue drifts along the ribbon and across it
                hue = 0.65 * u + 0.35 * (v + 1) / 2 + shift
                d.line([(x0, y0), (x1, y1)], fill=scale(ramp(cols, hue), k), width=SS)
    # soft hot core where the strands meet: the one focal point
    core = Image.new("RGB", (W // 4, H // 4))
    r = H / 4 * 0.05
    ImageDraw.Draw(core).ellipse([knot[0] / 4 - r * 1.6, knot[1] / 4 - r, knot[0] / 4 + r * 1.6, knot[1] / 4 + r],
                                 fill=lerp(ramp(cols, knot[0] / W + 0.15), (255, 255, 255), 0.35))
    core = core.filter(ImageFilter.GaussianBlur(r * 0.9)).resize((W, H), Image.BICUBIC)
    img = ImageChops.screen(img, core)
    glow = ImageChops.add(soft(trails, H * 0.01, 2).point(lambda v: min(255, v * 2)),
                          soft(trails, H * 0.05, 8).point(lambda v: min(255, v * 3)))
    img = ImageChops.screen(img, ImageChops.add(trails, glow))

    # depth: out-of-focus bokeh discs plus a few sharp sparkles near the ribbon
    bok = Image.new("RGB", (W // 4, H // 4))
    d = ImageDraw.Draw(bok)
    for _ in range(16):
        x = (fx + rnd.gauss(0, W * 0.2)) / 4
        y = (fy + rnd.gauss(0, H * 0.25)) / 4
        r = H / 4 * rnd.choice((0.006, 0.01, 0.016, 0.028, 0.04))
        d.ellipse([x - r, y - r, x + r, y + r], fill=scale(rnd.choice(cols), rnd.uniform(0.12, 0.4) * left_calm(x * 4)))
    bok = bok.filter(ImageFilter.GaussianBlur(H / 4 * 0.01)).resize((W, H), Image.BICUBIC)
    spark = Image.new("RGB", (W, H))
    d = ImageDraw.Draw(spark)
    for _ in range(60):
        x, y = fx + rnd.gauss(0, W * 0.18), fy + rnd.gauss(0, H * 0.2)
        r = SS * rnd.uniform(0.8, 2.2)
        d.ellipse([x - r, y - r, x + r, y + r], fill=scale((255, 255, 255), rnd.uniform(0.4, 0.9) * left_calm(x)))
    spark = ImageChops.add(spark, soft(spark, H * 0.008, 2))
    img = ImageChops.screen(img, ImageChops.add(bok, spark))

    # vignette keeps the eye inside the safe area
    vig = Image.radial_gradient("L").resize((W, H), Image.BICUBIC).point(lambda v: 255 - int(0.55 * max(0, v - 70)))
    img = ImageChops.multiply(img, Image.merge("RGB", (vig, vig, vig)))

    if text:
        # one short phrase, large, light weight, plenty of air; shadow keeps contrast on any palette
        tx, ty = W * 0.1, H * 0.5
        size = int(min(H * 0.17, W * 0.085))
        font = aurora_font(size)
        tw = ImageDraw.Draw(img).textlength(text, font=font)
        room = fx - tx - W * 0.16  # keep clear air between the words and the focal knot
        if tw > room:
            font = aurora_font(int(size * room / tw))
        shade = Image.new("L", (W, H))
        ImageDraw.Draw(shade).text((tx, ty), text, font=font, anchor="lm", fill=200)
        shade = soft(shade, font.size * 0.35, 2)
        img = Image.composite(Image.new("RGB", (W, H), scale(deep, 0.5)), img, shade)
        ImageDraw.Draw(img).text((tx, ty), text, font=font, anchor="lm", fill=(246, 247, 255))

    out = img.resize((w, h), Image.LANCZOS)
    # fine grain after downscale, so it survives and breaks up gradient banding
    noise = Image.effect_noise((w, h), 40).point(lambda v: 128 + (v - 128) // 6)
    return ImageChops.overlay(out, Image.merge("RGB", (noise, noise, noise)))


# ---------------------------------------------------------------- CLI


def pick_palette(names, topic, platform):
    """Same topic -> same starting palette; each platform steps to its neighbour, so a series varies."""
    names = list(names)
    return names[(zlib.crc32(topic.lower().encode()) + list(PLATFORMS).index(platform)) % len(names)]


def render(w, h, style, palette, seed, text):
    if style == "aurora":
        pal = VIVID.get(palette) or (lambda p: (p[0], p[1], (p[2], p[3], p[4])))(PALETTES[palette])
        return render_aurora(w, h, pal, seed, text)
    pal = PALETTES.get(palette) or (lambda v: (v[0], v[1], *v[2]))(VIVID[palette])
    return render_legacy(w, h, style, pal, seed, text)


def save(img, out):
    if str(out).lower().endswith((".jpg", ".jpeg")):
        img.save(out, quality=90, optimize=True, progressive=True)
    else:
        img.save(out, optimize=True)


def self_test():
    with tempfile.TemporaryDirectory() as tmp:
        for name, (w, h) in PLATFORMS.items():
            ext = "jpg" if name == "infoq" else "png"
            out = Path(tmp, f"{name}.{ext}")
            save(render(w, h, "aurora", pick_palette(VIVID, "self test", name), 1, "Spec first"), out)
            with Image.open(out) as im:
                assert im.size == (w, h), (name, im.size)
                assert im.format == ("JPEG" if ext == "jpg" else "PNG"), (name, im.format)
        save(render(1200, 630, "tiles", "midnight", 1, "Legacy"), Path(tmp, "legacy.png"))
        assert Image.open(Path(tmp, "legacy.png")).size == (1200, 630)
    print(f"self-test ok: {len(PLATFORMS)} platform sizes + legacy style")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--platform", default="og", choices=PLATFORMS)
    p.add_argument("--size", help="override WxH, e.g. 1600x900")
    p.add_argument("--text", default="", help="0-3 words (legacy styles allow 4); empty for no text")
    p.add_argument("--topic", help="what the piece is about; picks palette and layout (default: --text)")
    p.add_argument("--style", default="aurora", choices=["aurora", *LEGACY])
    p.add_argument("--palette", default="auto", choices=["auto", *VIVID, *PALETTES])
    p.add_argument("--seed", type=int, help="layout seed (default: derived from --topic)")
    p.add_argument("--out", default="banner.png", help=".png, or .jpg for JPEG (InfoQ, DZone)")
    p.add_argument("--self-test", action="store_true", help="render every platform size and check it")
    a = p.parse_args()
    if a.self_test:
        return self_test()

    limit = 3 if a.style == "aurora" else 4
    if len(a.text.split()) > limit:
        p.error(f"keep --text to {limit} words or fewer")
    w, h = map(int, a.size.lower().split("x")) if a.size else PLATFORMS[a.platform]
    topic = a.topic or a.text or "banner"
    palette = a.palette if a.palette != "auto" else pick_palette(
        VIVID if a.style == "aurora" else PALETTES, topic, a.platform)
    seed = a.seed if a.seed is not None else zlib.crc32(topic.lower().encode()) % 10000
    save(render(w, h, a.style, palette, seed, a.text), a.out)
    print(f"{a.out} {w}x{h} style={a.style} palette={palette} seed={seed}")


if __name__ == "__main__":
    main()
