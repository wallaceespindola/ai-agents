---
name: article-image-generator
description: Generate article banner and cover images in Wallace's house style (modern, abstract, futuristic, colorful, 0-3 words of text) at the right size for each platform, using a bundled Pillow script. Use whenever an article, newsletter issue, blog post, README or slide deck needs a banner, cover, hero, featured or Open Graph image, for Dev.to, Medium, LinkedIn, Substack, DZone, InfoQ, JavaPro or a personal blog, or when the user asks to regenerate, restyle or resize existing banners, even if they just say "add an image to the article".
---

# Article image generator

Default style `aurora`: a twisting ribbon of light trails over soft nebula glows, bokeh and fine sparkles, in a vivid palette on a deep background. Where the ribbon twists, its strands meet in one bright knot on the right third: that is the focal point. The left side stays calm for an optional short phrase. Rendered at 2x and downscaled, with light grain so gradients never band.

## House style rules

- **Modern, abstract, futuristic.** Light, gradients, curves and depth. No photos, people, clip art, logos, UI, charts, boxes, grids of cells or document glyphs.
- **Colorful.** Vibrant, harmonious palettes (violet-magenta-cyan, teal-lime-blue, orange-pink-purple...), never monochrome navy.
- **Almost no text.** 0 to 3 words, often none. One short phrase in a clean geometric face (Outfit, else Avenir Next), large, left, with plenty of air. No labels, IDs, numbers, captions, subtitles, author names or URLs. The script refuses more than 3 words in `aurora` (the global cap is 4; this skill aims tighter).
- **Readable at thumbnail size.** The focal knot and the text stay inside the central ~80%, so centre crops in feeds keep them. The ribbon dims behind the words and a soft shadow keeps them legible on every palette.
- **Family, not clones.** One topic gives one layout; each platform gets a different palette, so a series is cohesive but each banner looks native.

## Generate

```bash
G=~/git/ai-agents/skills/article-image-generator/scripts/generate_banner.py

# article cover with a short phrase; palette and layout come from --topic
uv run --with pillow python $G --platform devto --topic "copilot capacity" \
  --text "Share the credits" --out docs/articles/devto/banner.png

# text-free README banner (1280x400)
uv run --with pillow python $G --platform readme --topic "copilot capacity" --out docs/images/banner.png

# InfoQ wants JPEG: the .jpg extension switches the format
uv run --with pillow python $G --platform infoq --topic "copilot capacity" --out docs/articles/infoq/banner.jpg

# pin a palette or layout, or check the script
uv run --with pillow python $G --platform medium --palette sunset --seed 12 --out banner.png
uv run --with pillow python $G --self-test   # renders every size, asserts dimensions and PNG/JPEG
```

| Option | Values |
|--------|--------|
| `--platform` | `devto` 1000x420, `medium` 1200x627, `linkedin` 1920x1080, `substack` 1200x630, `dzone` 1200x628, `infoq` 1024x768, `javapro` 1200x630, `blog`/`og` 1200x630, `slide` 1920x1080, `readme` 1280x400 |
| `--size` | Override, e.g. `1600x900`, when a platform's verified size differs from the table |
| `--topic` | What the piece is about. Seeds the layout and the palette choice (defaults to `--text`) |
| `--text` | 0 to 3 words; omit for a text-free banner |
| `--palette` | `auto` (default) or a name below |
| `--seed` | Layout override; default is derived from `--topic` |
| `--style` | `aurora` (default) or a legacy style, see below |
| `--out` | `.png`, or `.jpg`/`.jpeg` for JPEG (quality 90) |

## Palettes

| Name | Lights |
|------|--------|
| `nebula` | violet, magenta, cyan |
| `lagoon` | teal, lime, blue |
| `sunset` | orange, pink, purple |
| `borealis` | green, sky, fuchsia |
| `solar` | amber, orange, crimson |
| `oceanic` | blue, teal, lilac |
| `candy` | pink, lilac, sky |
| `electric` | yellow, magenta, cyan |

`--palette auto` hashes the topic to a starting palette and steps one palette per platform in the order of the table above (devto, medium, linkedin, ...). Same topic, same platform: same banner every run. Same topic, different platform: same ribbon layout, different colours. Pass `--palette` to override; the legacy palette names also work with `aurora`.

## Workflow

1. Check the platform's current cover size first. Sizes change; if the project has a `PLATFORM_GUIDELINES.md` or the platform skill gives a verified size, pass `--size`.
2. Pick the topic and the words (or none). Prefer none for README banners and slide backgrounds.
3. Generate, then **look at the image** with the Read tool. Check the text is legible, it doesn't touch the bright knot, and nothing important is cut. If it is off, change `--seed` and regenerate.
4. For a series, render every platform with the same `--topic` and review them side by side before committing.
5. Save as `banner.png` (InfoQ: `banner.jpg`) in the article folder and embed it at the top as `![Banner](banner.png)`.

## Legacy styles

Kept so older series can be regenerated; don't use them for new work.

- `generate_banner.py --style network|flow|grid|orbit|tiles` with palettes `midnight`, `aurora`, `ember`, `violet`, `ice`, `matrix` (up to 4 words).
- `ledger_light.py`: two fields of capacity cells with a document travelling between them, Jura Light words. Same `--platform` sizes, palettes `cyan`, `violet`, `amber`, `ice`, `lime`, `magenta`, `azure`. The tiny mono markers (`--label`, `--left`, `--right`) are now opt-in and off by default. Needs the canvas-design fonts (`example-skills` or `document-skills` plugin).

## Notes

- Pillow only (no numpy). A 1920x1080 banner renders in about a second.
- Fonts: Outfit from the canvas-design plugin's `canvas-fonts` when installed, else Avenir Next, Helvetica Neue or SF on macOS, DejaVu on Linux.
- PNG banners land around 0.6-3 MB (the grain resists compression); JPEG around 100-250 KB. DZone suggests 100-200 KB, so use `.jpg` there too.
- Sizes were checked against platform help pages on 2026-10-18 (LinkedIn articles 1920x1080, Substack at least 1200x630). Dev.to previews can crop to about 800x418, which the centred safe area survives.
- A project README banner is about the project's idea, not the articles: render it separately (`docs/images/banner.png`, 1280x400) instead of reusing an article banner.
- Diagrams are a separate job: use `diagram-mermaid` or `diagram-plantuml`. This skill only makes the banner.
- Keep one-off helper scripts outside the repository.
