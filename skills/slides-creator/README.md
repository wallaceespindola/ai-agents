# Slides Creator Skill

Convert technical articles into professional presentation slide decks.

## Quick Start

```bash
# Generate PowerPoint from article
slides-creator convert docs/articles/my-article.md --output pptx

# Generate Google Slides
slides-creator convert docs/articles/my-article.md --output google-slides

# Generate all formats
slides-creator convert docs/articles/my-article.md --output all
```

## Documentation

- **[SKILL.md](./SKILL.md)** - Complete skill documentation
- **[../../docs/SLIDES_CREATOR_GUIDE.md](../../docs/SLIDES_CREATOR_GUIDE.md)** - User guide and workflows

## Directory Structure

```
slides-creator/
├── SKILL.md                     # Skill documentation
├── README.md                    # This file
├── utils/                       # Core Python modules
│   ├── __init__.py
│   ├── article_parser.py        # Extract content from articles
│   └── pptx_generator.py        # Generate PowerPoint files
├── templates/                   # Slide template classes
├── config/                      # Configuration files
│   └── slide_config.yaml        # Presentation settings
├── examples/                    # Example articles and outputs
└── tests/                       # Unit tests
```

## Key Features

✅ Convert articles to PowerPoint (.pptx)
✅ Generate Google Slides presentations
✅ Publish to Speaker Deck
✅ Include speaker notes from article content
✅ Multiple themes (light, dark, technical)
✅ Customizable layouts and styles
✅ Professional, polished output

## Installation

```bash
# Install Python dependencies
pip install python-pptx pyyaml markdown

# Optional: Google Slides support
pip install google-auth google-api-python-client google-auth-oauthlib
```

## Usage Examples

### Simple: Create PowerPoint

```bash
slides-creator convert docs/articles/spring-boot-tips.md --output pptx
```

Result: `presentations/spring-boot-tips/spring-boot-tips.pptx`

### Customize: Dark theme, fewer words per slide

```bash
slides-creator convert docs/articles/my-talk.md \
  --output pptx \
  --theme dark \
  --max-words-per-slide 75
```

### Advanced: Publish to Speaker Deck

```bash
slides-creator convert docs/articles/conference-talk.md \
  --output all \
  --publish-to-speaker-deck
```

## Configuration

Add these to `.env` to customize presentation generation:

```env
PRESENTATION_THEME=technical
PRESENTATION_AUTHOR=Your Name
PRESENTATION_FOOTER_TEXT=Your Name | speakerdeck.com/yourhandle
PPTX_DEFAULT_FONT=San Francisco
PPTX_CODE_FONT=Monaco
```

## How It Works

1. **Parse Article** - Extracts frontmatter, sections, code blocks, images
2. **Create Slide Plan** - Maps article content to slide types
3. **Generate Output** - Creates PowerPoint, Google Slides, or Speaker Deck

**Article Structure → Slide Structure:**

- Title + metadata → Title slide
- H2 sections → Content slides (2-3 per section)
- Code blocks → Code slides (syntax-highlighted)
- Images/diagrams → Visual slides
- Conclusion → Conclusion slide

## Best Practices

1. **Structure articles for slides** - Use H2 headings, bullet points, include code/diagrams
2. **Keep code blocks focused** - 10-20 lines, not production code
3. **Use descriptive headings** - "Async/Await in Python" not "Implementation"
4. **Include visuals** - Diagrams and images make better slides
5. **Write clear conclusions** - Becomes the final "Key Takeaways" slide

## Troubleshooting

**Code blocks not rendering?**
- Use language specifier: \`\`\`python (not \`\`\`)

**Too much text on slides?**
- Use `--max-words-per-slide 75` to reduce content

**Images missing?**
- Use relative paths: `![alt](./images/diagram.png)`
- Ensure images exist before generating

See [SLIDES_CREATOR_GUIDE.md](../../docs/SLIDES_CREATOR_GUIDE.md) for more help.

## Next Steps

1. Copy article template: `cp docs/ARTICLE_TEMPLATE.md docs/articles/my-article.md`
2. Write your article content
3. Generate slides: `slides-creator convert docs/articles/my-article.md --output pptx`
4. Open PowerPoint and customize
5. Present!

## Files Generated

When you run slides-creator, it creates:

```
presentations/article-name/
├── article-name.pptx              # PowerPoint file
├── speaker_notes.txt              # Plain text notes
├── metadata.json                  # Generation info
└── article_snapshot.md            # Copy of article used
```

## Learn More

- Full guide: [SLIDES_CREATOR_GUIDE.md](../../docs/SLIDES_CREATOR_GUIDE.md)
- Skill details: [SKILL.md](./SKILL.md)
- Configuration: [config/slide_config.yaml](./config/slide_config.yaml)
