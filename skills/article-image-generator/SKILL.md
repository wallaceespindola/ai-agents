---
name: article-image-generator
description: Generate article banner and cover images in Wallace's house style (modern, abstract, futuristic, minimal text) at the right size for each platform, using a bundled Pillow script. Use whenever an article, newsletter issue, blog post or slide deck needs a banner, cover, hero, featured or Open Graph image, for Dev.to, Medium, LinkedIn, Substack, DZone, InfoQ, JavaPro or a personal blog, or when the user asks to regenerate, restyle or resize existing banners, even if they just say "add an image to the article".
---

# Article image generator

Produces banners in one consistent style: dark gradient background, glowing abstract geometry (networks, flow lines, perspective grids, orbits, tiles), and at most a few words of text. The style signals "technical and current" at thumbnail size without competing with the article title, which the platform already shows next to the image.

## Style rules

- **Modern, abstract, futuristic.** Geometry and light, no photos, no stock people, no clip art, no logos or brand marks.
- **Minimal text.** 0 to 4 words. A short phrase that hints at the idea ("Share the work", "Spec first") or nothing at all. No subtitles, author names, URLs or labels on shapes. The script refuses more than 4 words, because longer text turns illegible in feed thumbnails.
- **Readable.** Text sits on the left, vertically centred, on a faded calm area. Most platforms crop covers towards the centre in feeds, and left-centre survives those crops.
- **Family, not clones.** When one piece goes to several platforms, use the same idea with a different style or palette per platform, so each banner looks native but recognisably part of a series.

## Generate

```bash
uv run --with pillow python ~/git/ai-agents/skills/article-image-generator/scripts/generate_banner.py \
  --platform devto --style network --palette midnight --seed 7 \
  --text "Share the work" --out docs/articles/devto/banner.png
```

| Option | Values |
|--------|--------|
| `--platform` | `devto` 1000x420, `medium` 1200x627, `linkedin` 1920x1080, `substack` 1200x630, `dzone` 1200x628, `infoq` 1024x768, `javapro` 1200x630, `blog`/`og` 1200x630, `slide` 1920x1080 |
| `--size` | Override, e.g. `1600x900`, when a platform's verified size differs from the table |
| `--style` | `network` (nodes around a document glyph), `flow` (wave lines), `grid` (perspective horizon), `orbit` (rings around a core), `tiles` (lit/dim grid) |
| `--palette` | `midnight`, `aurora`, `ember`, `violet`, `ice`, `matrix` |
| `--seed` | Any integer; same seed gives the same image, change it for a new layout |
| `--text` | 0 to 4 words; omit for a text-free banner |

Pick a style that echoes the topic: `network` for collaboration, integration and architecture; `flow` for data and pipelines; `grid` for platforms and infrastructure; `orbit` for core concepts and ecosystems; `tiles` for capacity, quotas and allocation.

## Workflow

1. Check the platform's current cover size before generating. Sizes change; if the project has a `PLATFORM_GUIDELINES.md` or the platform skill gives a verified size, use `--size` to match it.
2. Choose the words (or none), a style that fits the topic and a palette. For a multi-platform series, vary style or palette per platform.
3. Generate, then **look at the PNG** with the Read tool. Check that the text is legible, nothing important is cut at the edges, and the focal shape doesn't collide with the text. If it does, change `--seed` or the style and regenerate.
4. Save as `banner.png` in the article folder and embed it at the top as `![Banner](banner.png)`.
5. Keep any one-off helper scripts outside the repository.

## Notes

- Fonts: Avenir Next, Helvetica Neue or SF on macOS, DejaVu on Linux. The script picks an upright bold weight automatically.
- Output format follows the `--out` extension: PNG by default, JPEG (quality 90) for `.jpg`. InfoQ wants JPEG, and DZone suggests 100-200 KB images, so use `.jpg` there.
- Sizes were checked against platform help pages on 2026-10-18 (LinkedIn articles 1920x1080, Substack at least 1200x630). Dev.to previews can crop to about 800x418, which the left-centre text placement survives.
- Diagrams are a separate job: use `diagram-mermaid` or `diagram-plantuml` for the article's diagrams. This skill only makes the banner.
