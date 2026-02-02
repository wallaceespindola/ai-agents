# Slides Creator Skill

**Convert your technical articles into professional presentation slides for PowerPoint, Google Slides, and Speaker Deck.**

## Overview

The slides-creator skill transforms your technical articles into polished presentation slide decks. Write once as an article, generate slides automatically for multiple platforms.

**What it does:**
- Extracts content from markdown articles in `/docs` folder
- Intelligently maps article sections to slide layouts
- Generates PowerPoint (.pptx) files for offline use
- Creates Google Slides presentations for collaboration
- Publishes to Speaker Deck for your portfolio
- Includes speaker notes from article content
- Respects humanization standards throughout

**Perfect for:**
- Turning articles into conference talk slides
- Creating presentation decks without manual slide design
- Maintaining sync between articles and presentations
- Building your Speaker Deck portfolio
- Sharing technical knowledge in visual format

---

## Quick Start (5 Minutes)

### 1. Use Your Existing Article

Take any article from `/docs/articles/` (or use the template):

```bash
cp docs/ARTICLE_TEMPLATE.md docs/articles/my-first-presentation.md
# Edit and write your article content
```

### 2. Convert to PowerPoint

```bash
slides-creator convert docs/articles/my-first-presentation.md --output pptx
```

Result: `presentations/my-first-presentation/my-first-presentation.pptx`

### 3. Convert to Google Slides (Optional)

```bash
slides-creator convert docs/articles/my-first-presentation.md --output google-slides
```

Result: Live Google Slides link in your console

### 4. Publish to Speaker Deck (Optional)

```bash
slides-creator convert docs/articles/my-first-presentation.md --output speaker-deck
```

Result: https://speakerdeck.com/wallacese/my-first-presentation

---

## How It Works: Article → Slides

### Article Structure (from ARTICLE_TEMPLATE.md)

Your articles already have the perfect structure for slides:

```markdown
---
title: Building Spring Boot REST APIs
author: Wallace Espindola
date: 2025-02-02
tags: [java, spring-boot, rest-api]
---

## Introduction
[2-3 paragraphs setting up the topic]

## Section 1: Core Concepts
[Explanation with bullet points]

### Subsection 1.1
[Details and examples]

## Section 2: Implementation
[Step-by-step guide]

### Code Example
\`\`\`java
// Full working code
\`\`\`

## Conclusion
Key takeaways and next steps
```

### Automatic Conversion

The skill parses your article and creates slides:

1. **Title Slide** ← Article metadata (title, author, date, tags)
2. **Content Slides** ← Each H2 section becomes 2-3 content slides
3. **Code Slides** ← Each code block gets its own syntax-highlighted slide
4. **Visual Slides** ← Diagrams and images get full-width slides
5. **Conclusion Slide** ← Key takeaways + call-to-action

**Article Section** → **Slides Generated**
- 1 H2 section (500 words) → 2-3 content slides
- 1 code block → 1 code slide
- 1 diagram/image → 1 visual slide
- Conclusion → 1 conclusion slide

---

## Slide Types

### 1. Title Slide
- Article title (large, prominent)
- Author name + social links (from .env)
- Publication date
- Key tags/topics
- Footer with Speaker Deck profile

**Used for**: First slide of every presentation

### 2. Content Slides
- Section heading (H2 from article)
- Body text (condensed to 100 words max)
- Optional bullet points (5 max)
- Footer with author, date, slide number

**Used for**: Main content sections

### 3. Code Slides
- Language-syntax-highlighted code (15-20 lines max)
- File path/context label
- Explanation above or below code
- Optional line-by-line notes in speaker notes

**Used for**: Code examples and implementations

### 4. Visual Slides
- Full-width image or diagram
- Caption and description
- Source/attribution (from article)
- Optional speaker notes with context

**Used for**: Architecture diagrams, illustrations, screenshots

### 5. Conclusion Slide
- Section heading: "Key Takeaways"
- 3-5 bullet points with main concepts
- Call-to-action: Links to article, GitHub, GitHub, LinkedIn
- Newsletter signup prompt (Substack)

**Used for**: Last slide of presentation

---

## Configuration

### Environment Variables (.env)

Required variables for presentation generation:

```env
# Presentation Settings
PRESENTATION_THEME=technical          # Options: light, dark, technical
PRESENTATION_ASPECT_RATIO=16:9        # Standard widescreen
PRESENTATION_INCLUDE_SPEAKER_NOTES=true

# Author & Branding
PRESENTATION_AUTHOR=Wallace Espindola
PRESENTATION_FOOTER_TEXT=Wallace Espindola | speakerdeck.com/wallacese

# PowerPoint Settings
PPTX_THEME=technical
PPTX_DEFAULT_FONT=San Francisco
PPTX_CODE_FONT=Monaco

# Google Slides (optional)
GOOGLE_SLIDES_ENABLED=false
GOOGLE_SLIDES_SERVICE_ACCOUNT_JSON=./credentials/google-service-account.json
GOOGLE_SLIDES_FOLDER_ID=root
GOOGLE_SLIDES_SHARE_MODE=view

# Speaker Deck (optional)
SPEAKER_DECK_ENABLED=false
SPEAKER_DECK_USERNAME=wallacese
SPEAKER_DECK_AUTO_PUBLISH=false
```

### Theme Options

**Light Theme** - Professional, corporate
- White background, dark text
- Blue primary color (#2E5090)
- Great for: Business/corporate presentations

**Dark Theme** - Modern, engaging
- Dark background, light text
- Teal accent color (#4ECDC4)
- Great for: Tech conferences

**Technical Theme** - Code-focused (default)
- Dark blue-black background (#0D1117)
- Light blue text (#58A6FF)
- Syntax-highlighted code blocks
- Great for: Developer talks

---

## Usage Examples

### Example 1: Convert Article to PowerPoint

**Your article:** `docs/articles/spring-boot-patterns.md`

```bash
slides-creator convert docs/articles/spring-boot-patterns.md \
  --output pptx \
  --theme technical
```

**Output:**
- `presentations/spring-boot-patterns/spring-boot-patterns.pptx`
- `presentations/spring-boot-patterns/speaker_notes.txt`
- `presentations/spring-boot-patterns/metadata.json`

**Speaker Notes:**
File contains full article text, organized by slide, so you have context when presenting.

---

### Example 2: Generate All Formats

```bash
slides-creator convert docs/articles/rest-api-design.md --output all
```

**Output:**
- `presentations/rest-api-design/rest-api-design.pptx` (PowerPoint)
- `presentations/rest-api-design/rest-api-design-gslides.txt` (Google Slides URL)
- `presentations/rest-api-design/rest-api-design-speaker-deck.txt` (Speaker Deck URL)
- `presentations/rest-api-design/speaker_notes.txt` (Text format notes)

---

### Example 3: Custom Theme and Settings

```bash
slides-creator convert docs/articles/my-talk.md \
  --output pptx \
  --theme dark \
  --max-words-per-slide 80 \
  --include-code-lines 15 \
  --aspect-ratio 16:9
```

---

### Example 4: Regenerate from Updated Article

```bash
slides-creator convert docs/articles/my-talk.md \
  --output pptx \
  --force-regenerate  # Ignore cache, rebuild from article
```

---

## Integration with Your Workflow

### Workflow: Write Once, Present Everywhere

```
1. Write Article (docs/articles/my-topic.md)
   └─ Structure with H2 sections, code examples, diagrams

2. Generate Slides (slides-creator convert ...)
   ├─ PowerPoint (offline editing, email sharing)
   ├─ Google Slides (collaborate with co-speakers)
   └─ Speaker Deck (publish for portfolio)

3. Customize (optional)
   ├─ Edit PowerPoint in Microsoft Office
   ├─ Edit Google Slides in browser
   └─ Add transitions, animations, speaker notes

4. Present & Publish
   ├─ Present locally from PowerPoint
   ├─ Share Google Slides link with team
   └─ Publish to Speaker Deck for portfolio
```

### Linking Presentations Back to Articles

Every presentation automatically includes:
- Link to original article in conclusion slide
- Article URL in Speaker Deck metadata
- Reference in speaker notes: "Full details in article..."

Viewers can:
- Read full article for deep dive
- View code on GitHub (article links)
- Subscribe to newsletter (from article sign-off)

---

## Best Practices for Article-to-Slide Conversion

### 1. Structure Your Article for Slides

**Good article structure for slides:**
```markdown
## Section Title (becomes slide group)
[2-3 sentences intro]

Key points:
- Bullet point 1
- Bullet point 2
- Bullet point 3

[Relevant code example or diagram]

Details about implementation...
```

**Becomes:** 2-3 slides (1 intro, 1-2 content/code, 1 visual)

### 2. Keep Code Blocks Focused

**Instead of:** 50-line production code
```java
public class UserService {
  private UserRepository repo;
  // ... 45 lines of code ...
}
```

**Do this:** Show the essence (10-15 lines)
```java
public User findByEmail(String email) {
  return repo.findByEmail(email)
    .orElseThrow(() -> new UserNotFoundException());
}
```

**Speaker notes:** "Full implementation in [GitHub link]"

### 3. Use Descriptive Headings

**Weak heading:** "Implementation"
→ Creates vague slide title

**Strong heading:** "How to Configure Spring Security with OAuth2"
→ Creates clear, specific slide title

### 4. Include Visual Content

Articles with diagrams automatically get better slides:

```markdown
## Architecture Overview

[Mermaid diagram of system components]

The system consists of three layers:
- API Gateway
- Business Logic
- Data Storage
```

→ Generates:
- Title slide: "Architecture Overview"
- Visual slide: Rendered diagram
- Content slide: Explanation

### 5. End with Strong Conclusion

Your conclusion section becomes the final slide:

```markdown
## Conclusion

You learned:
- How to design REST APIs
- Error handling patterns
- Security best practices

Next steps:
- Check out the code on GitHub
- Read more in my articles
- Connect on LinkedIn
```

→ Perfect conclusion slide with takeaways + CTA

---

## Troubleshooting

### Problem: Articles not found
```
Error: Could not find article: docs/articles/my-file.md
```
**Solution:**
- Check file path: articles should be in `docs/articles/` folder
- Use full path: `docs/articles/my-file.md` (not just `my-file.md`)
- File must be `.md` (markdown format)

### Problem: Code blocks not rendering
```
Generated slides have code blocks as plain text
```
**Solution:**
- Code blocks must have language specifier: \`\`\`java (not just \`\`\`)
- Supported languages: java, python, javascript, go, rust, sql, etc.
- Check that code block is properly closed with \`\`\`

### Problem: Images not showing in PPTX
```
PowerPoint has broken image links
```
**Solution:**
- Use relative image paths in article: `![alt](./images/diagram.png)`
- Store images in `docs/images/` folder
- Ensure images exist before generating slides
- Supported formats: PNG, JPG, GIF, SVG

### Problem: Google Slides auth failing
```
Error: Authentication failed - invalid credentials
```
**Solution:**
- Set up Google Cloud service account (see SLIDES_CREATOR_GUIDE.md)
- Download JSON credentials file
- Set path in .env: `GOOGLE_SLIDES_SERVICE_ACCOUNT_JSON=./path/to/credentials.json`
- Verify .env is not committed (should be in .gitignore)

### Problem: Speaker Deck upload not working
```
Error: Could not publish to Speaker Deck
```
**Solution:**
- If using fallback manual workflow: upload PPTX to speakerdeck.com manually
- File will be available at: `presentations/[article-name]/[article-name].pptx`
- Then obtain public URL and add to article

---

## Advanced Topics

### Custom Slide Templates

Create custom slide layouts by editing:
`skills/slides-creator/templates/default_template.py`

```python
class CustomTemplate(SlideTemplate):
    def render(self, content: dict, config: SlideConfig) -> Slide:
        # Custom rendering logic
        pass
```

### Modify Themes

Edit theme configuration:
`skills/slides-creator/config/slide_config.yaml`

```yaml
themes:
  my_custom_theme:
    background: "#2C3E50"
    text: "#ECF0F1"
    primary: "#3498DB"
    code_background: "#34495E"
```

Then use: `--theme my_custom_theme`

### Add Custom Content Blocks

Extend article parser to recognize custom blocks:

```markdown
::: speaker-note
This is important for the presenter
:::
```

---

## Integration with Other Skills

The slides-creator skill works best with:

- **image-generator-blog** - Generate title slide backgrounds
- **diagram-mermaid** - Render diagrams as SVG in slides
- **diagram-plantuml** - Complex UML diagrams
- **architecture-design** - Architecture diagram slides
- **code-examples-generator** - Extract perfect code samples
- **All platform skills** - Content inspiration from platform-optimized versions

---

## Complete Command Reference

```bash
# Basic usage
slides-creator convert ARTICLE.md [OPTIONS]

# Output formats
--output pptx              # PowerPoint only
--output google-slides     # Google Slides only
--output speaker-deck      # Speaker Deck only
--output all              # All three formats (default)

# Customization
--theme [light|dark|technical]  # Slide theme
--aspect-ratio 16:9|4:3         # Slide dimensions
--max-words-per-slide 80-150    # Text condensation level
--include-code-lines 10-25      # Code block line limit
--include-speaker-notes true|false

# Processing
--force-regenerate        # Ignore cache, rebuild
--dry-run                 # Preview without creating files
--verbose                 # Detailed logging

# Publishing
--auto-publish           # Auto-publish to Speaker Deck
--share-mode view|edit   # Google Slides sharing
--open                   # Auto-open generated file
```

---

## File Organization

After running slides-creator, your presentations folder looks like:

```
presentations/
├── my-first-presentation/
│   ├── my-first-presentation.pptx          # PowerPoint version
│   ├── my-first-presentation-gslides.txt   # Google Slides link
│   ├── my-first-presentation-speaker-deck.txt
│   ├── speaker_notes.txt                   # Plain text notes
│   ├── metadata.json                       # Generation metadata
│   └── article_snapshot.md                 # Article version used
├── spring-boot-patterns/
│   ├── spring-boot-patterns.pptx
│   ├── speaker_notes.txt
│   └── ...
└── archive/
    └── [previous versions]
```

---

## FAQ

**Q: Can I edit the generated slides?**
A: Yes! PPTX files open in PowerPoint, Google Slides, Keynote. Google Slides versions are collaborative. Edit freely, then re-export for Speaker Deck if needed.

**Q: How many slides will I get?**
A: Typically 1 slide per 150-200 words of article content, plus code and visual slides. A 3000-word article → ~15-18 slides.

**Q: Can I use presentations generated from articles for conferences?**
A: Absolutely! That's the whole point. Generate slides from your technical article, customize for the conference, and present. You can also publish to Speaker Deck for your portfolio.

**Q: What if my article changes?**
A: Run `slides-creator convert` again. The skill will regenerate slides from the updated article. You'll get a fresh presentation with new content.

**Q: Can I share Google Slides with my team?**
A: Yes! The generated Google Slides can be shared via link. Set `GOOGLE_SLIDES_SHARE_MODE=edit` in .env to allow team editing.

**Q: Do I need to pay for anything?**
A: PowerPoint generation is free. Google Slides requires a Google account (free tier available). Speaker Deck has free and paid plans.

**Q: Can I customize the design?**
A: Yes! Edit themes in `config/slide_config.yaml` or create custom templates in `templates/`. See "Advanced Topics" section.

---

## Support & Next Steps

1. **First time?** See `docs/SLIDES_CREATOR_GUIDE.md` for detailed walkthrough
2. **Need examples?** Check `skills/slides-creator/examples/` folder
3. **API issues?** See "Troubleshooting" section above
4. **Want custom designs?** See "Advanced Topics"
5. **Have suggestions?** Update this skill with your improvements!

---

## Implementation Status

✅ **Coming Soon**:
- Python utility scripts (article_parser.py, slide_generator.py, pptx_generator.py)
- Google Slides integration module
- Speaker Deck publishing module
- Configuration and templates
- Comprehensive guide and examples
- Integration with your article writing workflow

**Current**: Skill documentation, workflow definition, best practices

---

*Last Updated: 2025-02-02*
*Author: Wallace Espindola*
*Part of: AI Agents & Skills for Technical Writers*
