---
description: Complete guide to the slides-creator skill - convert articles to presentations
---

# Slides Creator Guide

Transform your technical articles into professional presentation slides with a single command.

## What is Slides Creator?

The `slides-creator` skill automatically converts articles from your `/docs/articles/` folder into presentation slide decks. It extracts key content from your markdown articles and intelligently creates:

- **PowerPoint (.pptx) files** for offline use and editing
- **Google Slides presentations** for collaboration
- **Speaker Deck entries** for your public portfolio
- **Speaker notes** from your article content

Write your article once, generate slides for all platforms.

---

## Quick Start (5 Minutes)

### Step 1: Create Your Article

Start with `docs/ARTICLE_TEMPLATE.md` and write your technical article:

```bash
cp docs/ARTICLE_TEMPLATE.md docs/articles/my-presentation.md
# Edit the article with your content
```

### Step 2: Generate PowerPoint

```bash
slides-creator convert docs/articles/my-presentation.md --output pptx
```

**Result:** `presentations/my-presentation/my-presentation.pptx`

### Step 3: Open in PowerPoint

Open the generated `.pptx` file in Microsoft PowerPoint, Google Slides, or Keynote. Edit, add animations, and present!

### Step 4: Publish to Speaker Deck (Optional)

```bash
slides-creator publish docs/articles/my-presentation.md --to speaker-deck
```

**Result:** Your presentation is now on your Speaker Deck profile at `speakerdeck.com/wallacese`

---

## How Slides Creator Works

### Article Structure → Slide Structure

Your article follows a natural structure that maps perfectly to slides:

```
Article Markdown:
├── Title, Author, Date (frontmatter)
├── Introduction
├── ## Section 1 (H2 heading)
│   └── Content, bullet points, code examples
├── ## Section 2 (H2 heading)
│   └── Content with diagrams
└── Conclusion

Becomes Slides:
├── Slide 1: Title slide (title, author, date)
├── Slide 2-4: Content from Section 1
├── Slide 5-7: Content from Section 2
└── Final Slide: Conclusion with takeaways
```

### Content Type Mapping

Different content in your article becomes different slide types:

| Article Content | Becomes | Slide Type |
|-----------------|---------|-----------|
| Title + metadata | Slide 1 | Title slide |
| H2 section + text | Slide 2, 3, ... | Content slides |
| Code block | Dedicated slide | Code slide |
| Image/diagram | Dedicated slide | Visual slide |
| Conclusion section | Last slide | Conclusion slide |
| Bullet points | Bullet list | Auto-formatted |

---

## Installation & Setup

### 1. Python Dependencies

The skill requires Python libraries for slide generation:

```bash
pip install python-pptx pyyaml markdown
```

**Optional** (for Google Slides support):
```bash
pip install google-auth google-api-python-client google-auth-oauthlib
```

### 2. Configuration (Optional)

Add these to your `.env` file for customization:

```env
# Presentation Appearance
PRESENTATION_THEME=technical              # light, dark, or technical
PRESENTATION_ASPECT_RATIO=16:9            # Standard widescreen
PRESENTATION_INCLUDE_SPEAKER_NOTES=true

# Author/Branding
PRESENTATION_AUTHOR=Wallace Espindola
PRESENTATION_FOOTER_TEXT=Wallace Espindola | speakerdeck.com/wallacese

# Output Locations
PRESENTATION_OUTPUT_DIR=./presentations

# PowerPoint Settings
PPTX_THEME=technical
PPTX_DEFAULT_FONT=San Francisco
PPTX_CODE_FONT=Monaco
```

---

## Common Workflows

### Workflow 1: Quick PowerPoint Presentation

```bash
# 1. Write article
cp docs/ARTICLE_TEMPLATE.md docs/articles/spring-boot-tips.md
# [Write your content]

# 2. Generate PowerPoint
slides-creator convert docs/articles/spring-boot-tips.md --output pptx

# 3. Open and edit in PowerPoint
open presentations/spring-boot-tips/spring-boot-tips.pptx

# 4. Present!
```

---

### Workflow 2: Conference Talk with Speaker Deck Portfolio

```bash
# 1. Write article for conference topic
cp docs/ARTICLE_TEMPLATE.md docs/articles/microservices-talk.md
# [Write your conference talk content]

# 2. Generate all formats
slides-creator convert docs/articles/microservices-talk.md --output all

# 3. Edit PowerPoint locally
open presentations/microservices-talk/microservices-talk.pptx
# [Add animations, transitions, custom notes]

# 4. Publish to Speaker Deck
slides-creator publish presentations/microservices-talk/microservices-talk.pptx

# 5. Share presentation link
# https://speakerdeck.com/wallacese/microservices-talk
```

---

### Workflow 3: Collaborate with Team

```bash
# 1. Generate article as Google Slides
slides-creator convert docs/articles/team-project.md --output google-slides

# 2. Share with team
# Link appears in console: https://docs.google.com/presentation/d/...

# 3. Collaborate in browser
# Team members can edit simultaneously

# 4. Export to PowerPoint when ready
slides-creator export-gslides <PRESENTATION_ID> --output pptx
```

---

## Customization

### Change Presentation Theme

```bash
# Use dark theme instead of default technical
slides-creator convert docs/articles/my-talk.md \
  --output pptx \
  --theme dark

# Options: light, dark, technical
```

### Adjust Text Length

```bash
# Create more text-heavy slides (good for reading)
slides-creator convert docs/articles/my-talk.md \
  --output pptx \
  --max-words-per-slide 150

# Create more visual, less text (good for speaking)
slides-creator convert docs/articles/my-talk.md \
  --output pptx \
  --max-words-per-slide 75
```

### Control Code Display

```bash
# Show more lines of code
slides-creator convert docs/articles/my-talk.md \
  --output pptx \
  --max-code-lines 25

# Show fewer lines (more focused)
slides-creator convert docs/articles/my-talk.md \
  --output pptx \
  --max-code-lines 15
```

### Add Custom Metadata

```bash
# Include additional information
slides-creator convert docs/articles/my-talk.md \
  --output pptx \
  --add-metadata "Conference: PyCon 2025" \
  --add-metadata "Track: Web Development"
```

---

## Advanced: Working with Google Slides

### Set Up Google Slides Integration

1. Create Google Cloud project
2. Enable Google Slides API
3. Create service account
4. Download credentials JSON
5. Add to `.env`:

```env
GOOGLE_SLIDES_SERVICE_ACCOUNT_JSON=./credentials/google-service-account.json
GOOGLE_SLIDES_FOLDER_ID=root
GOOGLE_SLIDES_SHARE_MODE=view
```

### Generate Google Slides from Article

```bash
slides-creator convert docs/articles/my-article.md \
  --output google-slides \
  --share-mode edit
```

This creates a Google Slides presentation and shares the link.

### Get Google Slides Link Later

```bash
# If you saved the presentation ID
slides-creator info presentations/my-article/metadata.json --show-gslides-url
```

---

## Advanced: Speaker Deck Integration

### Automatic Publishing

```bash
# If you have Speaker Deck API key in .env
SPEAKER_DECK_API_KEY=your_api_key

# Auto-publish when generating
slides-creator convert docs/articles/my-talk.md \
  --output pptx \
  --publish-to-speaker-deck \
  --speaker-deck-visibility public
```

### Manual Publishing (No API Required)

If Speaker Deck API is not available:

```bash
# 1. Generate PowerPoint
slides-creator convert docs/articles/my-talk.md --output pptx

# 2. File location
presentations/my-talk/my-talk.pptx

# 3. Upload manually to https://speakerdeck.com/
# Select file → my-talk.pptx
# Fill in title and details
# Publish!

# 4. Get the public URL
# https://speakerdeck.com/wallacese/my-talk-title
```

---

## Best Practices

### 1. Structure Articles for Better Slides

**Good:**
```markdown
## Key Concepts
[Brief intro paragraph]

Important points:
- Point 1
- Point 2
- Point 3

[Code example or diagram]
```

**Better for slides:** Keep paragraphs short (2-3 sentences), use bullet points, include code examples.

### 2. Use Descriptive Headings

**Weak:** "Implementation"
**Strong:** "How to Implement Async/Await in Python"

Strong headings become better slide titles.

### 3. Include Visuals

Articles with diagrams and code examples generate more interesting slide decks:

```markdown
## System Architecture

[Mermaid diagram showing components]

The system has three main layers...
```

### 4. Keep Code Blocks Focused

Instead of 50-line production code, show the essential 10-15 lines:

```python
# Good for slides - shows the pattern
async def fetch_data(url: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()
```

Speaker notes can reference the full code on GitHub.

### 5. Write Clear Conclusions

Your conclusion becomes the final slide:

```markdown
## Conclusion

Key takeaways:
- You learned pattern A
- You learned pattern B
- You can apply this to...

Next steps:
- View code: [GitHub link]
- Read more: [Article link]
- Connect: [LinkedIn]
```

---

## Slide Generation Process

### What Happens When You Run `slides-creator convert`

```
1. Parse Article
   ├─ Extract frontmatter (title, author, date, tags)
   ├─ Identify sections (H2 headings)
   ├─ Find code blocks
   └─ Find images/diagrams

2. Create Slide Plan
   ├─ Title slide from metadata
   ├─ Content slides from sections
   ├─ Code slides from code blocks
   ├─ Visual slides from images
   └─ Conclusion slide from conclusion section

3. Generate Output Files
   ├─ Create presentations/[article-name]/ directory
   ├─ Generate .pptx file
   ├─ Extract speaker notes
   ├─ Save metadata
   └─ Create snapshot of article

4. Report Results
   ├─ Show file locations
   ├─ Show slide count and statistics
   └─ Provide next steps (edit, publish, share)
```

---

## Troubleshooting

### Issue: Article not found

```
Error: Could not find article: docs/articles/my-file.md
```

**Solution:**
- Check file path is correct
- Articles should be in `docs/articles/` folder
- Use full path in command: `docs/articles/my-file.md`

### Issue: Code blocks not rendering properly

```
Generated slides have code as plain text
```

**Solution:**
- Code blocks need language specifier: \`\`\`python (not just \`\`\`)
- Supported: java, python, javascript, go, rust, sql, bash, etc.
- Check code block is closed with \`\`\`

### Issue: Images not showing in PowerPoint

```
PPTX has broken image links
```

**Solution:**
- Image paths must be relative: `![alt](./images/diagram.png)`
- Store images in same folder as article or in `docs/images/`
- Ensure images exist before generating slides

### Issue: Too much text on slides

```
Generated slides have too many words
```

**Solution:**
Use `--max-words-per-slide` to limit:

```bash
slides-creator convert docs/articles/my-talk.md \
  --output pptx \
  --max-words-per-slide 75
```

### Issue: Google Slides authentication failing

```
Error: Authentication failed
```

**Solution:**
- Download Google service account JSON
- Set path in .env: `GOOGLE_SLIDES_SERVICE_ACCOUNT_JSON=./path/to/credentials.json`
- Ensure credentials file is not in .gitignore (or use .env variable)

---

## File Organization

After generating presentations, your directory looks like:

```
presentations/
├── my-first-presentation/
│   ├── my-first-presentation.pptx          # PowerPoint file
│   ├── speaker_notes.txt                   # Full speaker notes
│   ├── metadata.json                       # Generation metadata
│   ├── article_snapshot.md                 # Copy of article used
│   └── my-first-presentation-speaker-deck.txt
├── spring-boot-tips/
│   ├── spring-boot-tips.pptx
│   ├── speaker_notes.txt
│   └── metadata.json
└── archive/
    └── [old versions if regenerated]
```

### Metadata File Example

`presentations/my-talk/metadata.json`:

```json
{
  "generated": "2025-02-02T10:30:00Z",
  "article_source": "docs/articles/my-talk.md",
  "slide_count": 15,
  "config": {
    "theme": "technical",
    "aspect_ratio": "16:9"
  },
  "article_snapshot_hash": "abc123...",
  "timestamps": {
    "title": "My Talk",
    "created": "2025-02-02T10:30:00Z"
  }
}
```

---

## Command Reference

```bash
# Basic conversion
slides-creator convert ARTICLE.md

# Specify output format
slides-creator convert ARTICLE.md --output pptx
slides-creator convert ARTICLE.md --output google-slides
slides-creator convert ARTICLE.md --output speaker-deck
slides-creator convert ARTICLE.md --output all

# Customize appearance
slides-creator convert ARTICLE.md --theme dark
slides-creator convert ARTICLE.md --theme light
slides-creator convert ARTICLE.md --aspect-ratio 4:3

# Control content density
slides-creator convert ARTICLE.md --max-words-per-slide 100
slides-creator convert ARTICLE.md --max-code-lines 20
slides-creator convert ARTICLE.md --min-slides 10

# Processing options
slides-creator convert ARTICLE.md --force-regenerate
slides-creator convert ARTICLE.md --dry-run
slides-creator convert ARTICLE.md --verbose

# Publishing
slides-creator publish presentations/my-talk/my-talk.pptx
slides-creator publish presentations/my-talk/my-talk.pptx --to speaker-deck
slides-creator publish presentations/my-talk/my-talk.pptx --to gslides

# Information
slides-creator info presentations/my-talk/metadata.json
slides-creator list-presentations
slides-creator show-stats docs/articles/my-talk.md
```

---

## Integration with Other Skills

The slides-creator skill works perfectly with other skills:

- **image-generator-blog** → Generate custom title slide backgrounds
- **diagram-mermaid** → Render diagrams as slides
- **diagram-plantuml** → Complex UML diagrams
- **architecture-design** → Architecture diagram slides
- **code-examples-generator** → Extract perfect code samples

### Example: Generate Diagram → Include in Slides

```bash
# 1. Generate diagram
skills-use diagram-mermaid \
  --diagram "system-architecture" \
  --output presentations/my-talk/system-architecture.svg

# 2. Reference in article
# ![System Architecture](./presentations/my-talk/system-architecture.svg)

# 3. Generate slides (diagram auto-included)
slides-creator convert docs/articles/my-talk.md --output pptx
```

---

## Next Steps

### First Time?
1. ✅ Copy `docs/ARTICLE_TEMPLATE.md` to `docs/articles/`
2. ✅ Write your article content
3. ✅ Run: `slides-creator convert docs/articles/your-article.md --output pptx`
4. ✅ Open the PowerPoint file and present!

### Want to Publish?
1. Generate slides: `slides-creator convert ...`
2. Upload PowerPoint to Speaker Deck manually, or
3. Set up Speaker Deck API key for automatic publishing

### Want to Collaborate?
1. Generate Google Slides: `slides-creator convert ... --output google-slides`
2. Share the link with your team
3. Collaborate in browser

### Want More Control?
1. Edit `skills/slides-creator/config/slide_config.yaml` for themes
2. Customize `.env` for presentation settings
3. Use command-line options for one-off customizations

---

## FAQ

**Q: Can I use presentations from articles for conferences?**
A: Yes! That's the intended use. Generate slides from your article, customize, and present.

**Q: How many slides will I get?**
A: Typically 1 slide per 150-200 words, plus code and visual slides. A 3000-word article → ~15-18 slides.

**Q: Can I edit the generated PowerPoint?**
A: Absolutely! Open in PowerPoint, Google Slides, or Keynote and customize as needed.

**Q: What if my article changes?**
A: Run `slides-creator convert` again. It will regenerate slides from updated content.

**Q: Can I use different themes?**
A: Yes! Use `--theme light`, `--theme dark`, or `--theme technical`.

**Q: Does this work with all article formats?**
A: Works best with articles that follow `ARTICLE_TEMPLATE.md` structure. Any markdown works, but structure affects slide quality.

**Q: Can I create custom slide templates?**
A: Yes! Edit `skills/slides-creator/templates/` and `config/slide_config.yaml`.

---

## Support

- **SKILL.md** - Detailed skill documentation
- **skills/slides-creator/examples/** - Example articles and outputs
- **skills/slides-creator/config/** - Configuration files and themes
- **Troubleshooting** section above - Common issues

---

*Last Updated: 2025-02-02*
*Part of: AI Agents & Skills for Technical Writers*
