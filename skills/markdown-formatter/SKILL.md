---
name: markdown-formatter
description: Format all technical articles in standard Markdown with consistent structure, code blocks, images, and metadata. Use when converting written articles to Markdown format for publishing, archiving, or version control on blogs, GitHub, and documentation sites.
---

# Markdown Formatting Guide for Technical Articles

## When to Use This Skill

Use this skill when:
- Converting written articles to Markdown format
- Preparing articles for GitHub documentation
- Formatting for static site generators (Hugo, Jekyll, Next.js)
- Creating articles for version control and backup
- Publishing to Markdown-first platforms
- Ensuring consistent formatting across all articles
- Converting from Word/Google Docs to Markdown
- Creating reusable content in multiple formats

## Why Markdown?

**Markdown advantages:**
- ✅ **Universal**: Works on all platforms and tools
- ✅ **Version control**: Git-friendly, shows diffs clearly
- ✅ **Simple**: Readable even as plain text
- ✅ **Portable**: Easy to convert to HTML, PDF, EPUB
- ✅ **SEO-friendly**: Clean, semantic HTML output
- ✅ **No vendor lock-in**: Not tied to any platform
- ✅ **Archival**: Lasts forever, readable 50 years from now
- ✅ **Diff-able**: See exactly what changed in versions

## Markdown Basics for Technical Articles

### Document Structure

#### Essential Structure
```markdown
---
title: "Article Title"
date: 2024-02-01
author: "Your Name"
description: "Brief description for preview/SEO"
tags: ["tag1", "tag2", "tag3"]
---

# Article Title

Your article content starts here.
```

#### Complete Metadata (Front Matter)
```yaml
---
title: "The Complete Guide to Spring Boot"
date: 2024-02-01
updated: 2024-02-15
author: "Your Name"
author_url: "https://yoursite.com"
description: "A comprehensive guide to Spring Boot covering setup, configuration, testing, and deployment in production."
excerpt: "Learn Spring Boot from basics to advanced patterns. This guide covers everything you need to know."
tags: ["java", "spring-boot", "tutorial", "web-development"]
categories: ["Backend", "Java", "Tutorials"]
slug: "complete-guide-spring-boot"
image: "/images/spring-boot-guide.jpg"
featured: true
reading_time: 15
toc: true
---
```

### Heading Structure

```markdown
# H1: Main Title (Use once per article)
This is the primary title, same as the article headline.

## H2: Major Section
Main sections of your article.

### H3: Subsection
Subsections under H2 sections.

#### H4: Minor Subsection
Used rarely, only if necessary for structure.
```

**Good heading practices:**
- ✅ Use ONE H1 per article (the title)
- ✅ Use H2 for main sections (3-7 per article)
- ✅ Use H3 for subsections (if needed)
- ✅ Avoid H4 unless absolutely necessary
- ✅ Use keywords in headings naturally
- ✅ Make headings descriptive

### Paragraphs & Line Breaks

```markdown
This is a paragraph. Markdown treats consecutive lines
as a single paragraph.

This is a new paragraph because of the blank line above.

Line breaks within a paragraph don't create new paragraphs.
Just write continuously.

For a hard line break (line without paragraph break):
First line with two spaces at the end
Second line appears directly below

Or use backslash:
First line\
Second line
```

**Best practices:**
- Single blank line between paragraphs
- 60-100 character line length recommended (readable)
- No blank lines within paragraphs

### Emphasis & Formatting

```markdown
*Italic* or _italic_ (typically for emphasis)
**Bold** or __bold__ (typically for important terms)
***Bold and italic*** (rarely used)
~~Strikethrough~~ (for deprecated/outdated info)
`inline code` (for variable names, methods, commands)

Use **bold** for important concepts, library names
Use *italic* for when introducing new terms
Use `code` for anything code-related
```

**Good practices:**
- Bold for important terms and concepts
- Italic for emphasis and new terms
- Code formatting for anything from code
- Avoid excessive formatting (focus on readability)

## Code Formatting

### Inline Code
```markdown
Use `variable_name` for code references
The `processData()` method handles...
Run `npm install` to install dependencies
```

### Code Blocks

#### Basic Code Block (Indented)
```markdown
    // Indented 4 spaces
    function example() {
        console.log("code");
    }
```

#### Fenced Code Block (Recommended)
```markdown
```language
code goes here
```
```

#### Code Block Examples

**Java:**
````markdown
```java
public class Example {
    public static void main(String[] args) {
        System.out.println("Hello World");
    }
}
```
````

**Python:**
````markdown
```python
def example():
    print("Hello World")
    return True
```
````

**JavaScript:**
````markdown
```javascript
function example() {
    console.log("Hello World");
    return true;
}
```
````

**TypeScript:**
````markdown
```typescript
interface User {
    id: number;
    name: string;
}

function getUser(id: number): User {
    // implementation
}
```
````

**Bash/Shell:**
````markdown
```bash
npm install
npm run build
npm start
```
````

**SQL:**
````markdown
```sql
SELECT users.name, posts.title
FROM users
INNER JOIN posts ON users.id = posts.user_id
WHERE users.status = 'active'
```
````

**YAML (Configuration):**
````markdown
```yaml
name: Example
version: 1.0
dependencies:
  - java: 17+
  - maven: 3.8+
```
````

### Code Block Best Practices

```markdown
// Brief comment explaining the concept
```java
public class ProductionExample {
    // Only highlight the key parts
    // Keep examples 20-50 lines max

    public void process() {
        // Clear, readable code
    }
}
```

- Always specify the language (helps with syntax highlighting)
- Include necessary imports/dependencies
- Keep comments to explain non-obvious logic
- Make code self-documenting with clear names

## Lists

### Unordered Lists (Bullets)

```markdown
- First item
- Second item
- Third item
  - Nested item (indent with 2-4 spaces)
  - Another nested item
    - Deeply nested (rare)
- Back to top level

Alternative bullet characters:
* Can use asterisks
+ Can use plus signs
- Dashes are most common
```

### Ordered Lists (Numbered)

```markdown
1. First step
2. Second step
3. Third step
   - Nested unordered item
   - Another nested item
4. Fourth step

Note: Numbers don't need to be sequential
1. First step
1. Second step
3. This still renders as "3" (Markdown is smart)
```

### Description/Definition Lists

```markdown
Term
: Definition of the term
: Second definition or explanation

Another Term
: Its definition with more detail here
```

### Checklist

```markdown
- [x] Completed task
- [ ] Incomplete task
- [x] Another completed task
- [ ] Pending task
```

## Links

### Basic Links

```markdown
[Link text](https://example.com)
[GitHub](https://github.com/author/repo)

Reference-style links (for repeated URLs):
[My Blog][blog]
[My GitHub][github]

[blog]: https://myblog.com
[github]: https://github.com/myusername
```

### Links to Headers (Anchor Links)

```markdown
# Getting Started

## Installation

Jump to section:
[Go to Installation](#installation)

[Back to Top](#getting-started)
```

**Anchor rules:**
- Lowercase the text
- Replace spaces with hyphens
- Remove special characters
- Example: `# Getting Started` becomes `#getting-started`

### External Links Best Practices

```markdown
For more info, see [the official documentation](https://docs.example.com).

Citation: [Original article](https://originalblog.com/article)

Avoid: [click here](https://example.com) ❌
Better: [read about authentication](https://example.com) ✅

Links should describe what's being linked, not "click here"
```

## Images

### Basic Image Syntax

```markdown
![Alt text describing the image](image_url)

Example:
![Spring Boot Architecture Diagram](./images/spring-boot-arch.png)
![Code comparison showing before and after](https://example.com/comparison.png)
```

### Images with Captions

```markdown
![Alt text](image_url)
*Figure 1: Caption describing what the image shows*

Example:
![Spring Boot Request Flow Diagram](/images/request-flow.png)
*Figure 2: How Spring Boot handles HTTP requests from client to response*
```

### Image Best Practices

```markdown
Use descriptive alt text (for accessibility and SEO):
![Flow diagram showing authentication process](/images/auth-flow.png)

NOT:
![image1](/images/image1.png)
![pic](/images/pic.jpg)

Image placement:
Text explaining the concept here.

![Relevant diagram or screenshot](/images/diagram.png)
*Caption explaining the diagram*

More text continuing the explanation.
```

### Local vs. Remote Images

```markdown
Local images (in same repo):
![Local image](/images/local.png)
![Relative path](../assets/image.png)

Remote images (from URL):
![Remote image](https://example.com/image.png)

Best practice: Use relative paths in repos for portability
```

## Blockquotes

### Single Blockquote

```markdown
> This is a blockquote.
> It can span multiple lines.

Good for:
- Highlighting important information
- Quotes from others
- Callouts or warnings
- Code output
```

### Nested Blockquotes

```markdown
> Main quote level 1
>
> > Nested quote level 2
> > More nested text
>
> Back to level 1
```

### Styled Blockquotes

```markdown
> **Note:** This is an important note for readers.

> **Warning:** Be careful with this approach.

> **Tip:** Here's a helpful tip for success.

> **Info:** Additional information about the topic.

> **Quote:** "A famous quote from someone relevant." — Attribution
```

## Tables

### Basic Table

```markdown
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Cell 1   | Cell 2   | Cell 3   |
| Cell 4   | Cell 5   | Cell 6   |

Alignment:
| Left      | Center    | Right    |
|:----------|:---------:|----------:|
| Left-align | Centered | Right-align |
```

### Table Example

```markdown
| Platform | Best For | Length | Frequency |
|----------|----------|--------|-----------|
| LinkedIn | Professional | 800-1500 | 1-2/week |
| Medium | Deep-dives | 2000-7000 | 1-2/month |
| Dev.to | Community | 1000-3000 | 1-2/week |
| Blog | Everything | Unlimited | Your pace |
```

### Table Best Practices

- Use tables for comparison data
- Use tables for specifications
- Use tables for quick reference
- Avoid tables for narrative content
- Keep column content concise
- Align headers with content

## Horizontal Rules

```markdown
Three or more of:
---
***
___

Separates major sections (optional)
Not commonly used in articles, but useful for:
- Separating distinct sections
- Before footer content
- Visual break between topics
```

## Special Characters & Escaping

```markdown
If you need to show special Markdown characters:
\*This won't be italicized\*
\[Not a link\](https://example.com)

Common special characters needing escape:
\ ` * _ { } [ ] ( ) # + - . !

Example:
The `*args` parameter in Python uses \*args syntax.
C pointers use the \* operator: `int *ptr`
```

## Comments

```markdown
<!-- This comment won't appear in the rendered output -->

<!-- Multi-line comment
     for longer notes
     that readers don't see -->

Use for:
- Notes to yourself
- TODOs or reminders
- Explanations of formatting
- Temporary content
```

## Document Layout Template

```markdown
---
title: "Complete Title of Article"
date: 2024-02-01
author: "Your Name"
description: "SEO description, 150-160 characters"
tags: ["tag1", "tag2", "tag3"]
---

# Complete Title of Article

Brief introduction paragraph (100-150 words) explaining what the article covers.

## Table of Contents
(Optional for longer articles 2000+ words)
- [Section 1](#section-1)
- [Section 2](#section-2)
- [Further Reading](#further-reading)

## Section 1

Introductory paragraph explaining the section.

### Subsection 1.1

Content and explanation.

```code-block
// Code example
```

More explanation after code.

### Subsection 1.2

Additional content.

## Section 2

Content here.

```code-block
// Another code example
```

## Further Reading

- [Link 1](https://example.com)
- [Link 2](https://example.com)

## References

- [Source 1](https://example.com)
- [Source 2](https://example.com)

---

Last updated: 2024-02-15

<!-- Comments for future edits -->
```

## Advanced Markdown Features

### Definition Lists (for glossaries)

```markdown
Term 1
: Definition of term 1

Term 2
: Definition of term 2
: Additional definition
```

### Footnotes

```markdown
This is a statement with a footnote[^1].

[^1]: This is the footnote content that appears at the bottom.

Multiple footnotes[^1][^2].

[^2]: Second footnote here.
```

### Collapsible Sections (HTML)

```markdown
<details>
<summary>Click to expand</summary>

Hidden content goes here.

- Can include markdown
- Like lists
- And code blocks

```
code in details
```

</details>
```

### Embedded Content

```markdown
Embedding a YouTube video:
[![Video Title](https://img.youtube.com/vi/VIDEO_ID/0.jpg)](https://www.youtube.com/watch?v=VIDEO_ID)

Or as a link:
[Watch on YouTube](https://www.youtube.com/watch?v=VIDEO_ID)
```

## Conversion Recommendations

### From Google Docs/Word to Markdown

1. **Export as HTML** from the original platform
2. **Use a converter**:
   - Pandoc (command line): `pandoc input.html -o output.md`
   - Online converters: markdowntoolbox.com, pandoc.org/try
3. **Clean up**: Remove extra blank lines, fix image links
4. **Verify**: Check all code blocks and images rendered correctly
5. **Test**: View in markdown viewer to verify formatting

### From Notion to Markdown

1. **Use notion2md** tool or
2. **Copy/paste** and manually format (works for smaller docs)
3. **Fix links** and images (Notion uses unique URLs)
4. **Verify structure** with headers and lists

### From Markdown to Other Formats

Using Pandoc:
```bash
# Markdown to HTML
pandoc article.md -o article.html

# Markdown to PDF
pandoc article.md -o article.pdf

# Markdown to Word
pandoc article.md -o article.docx

# Markdown to EPUB (e-book)
pandoc article.md -o article.epub
```

## Markdown Style Guide for Consistency

### Code References
```markdown
✅ Reference language names: Java, Python, JavaScript
✅ Reference framework names: Spring Boot, FastAPI, React
✅ Use code blocks: `processData()` for method names
✅ Use code blocks: `variable_name` for variable names
```

### List Consistency
```markdown
✅ Use dashes (-) for bullets consistently
✅ Use 1. 2. 3. for ordered lists
✅ Indent nested items with 2-4 spaces
✅ Use consistent formatting for all lists
```

### Header Consistency
```markdown
✅ Title Case for H2 headers: "Getting Started"
✅ Title Case for H3 headers: "Installation Steps"
✅ Be consistent throughout document
✅ Use keywords naturally in headers
```

### Emphasis Consistency
```markdown
✅ Bold for important terms: **Spring Boot**
✅ Italics for emphasis: *this is important*
✅ Code format for code: `processData()`
✅ Avoid excessive formatting
```

## Markdown Checklist

Before publishing, verify:

- [ ] Front matter includes title, date, author, description
- [ ] One H1 title at top of article
- [ ] H2 headers for main sections (3-7 per article)
- [ ] All code blocks have language specified
- [ ] All images have alt text (accessibility)
- [ ] All images have captions (context)
- [ ] Internal links use anchor tags where applicable
- [ ] External links open in reader's mind (clear destination)
- [ ] No orphaned or broken links
- [ ] Lists use consistent formatting
- [ ] Emphasis (bold/italic) used consistently
- [ ] No excessive blank lines or formatting
- [ ] Table data is clear and organized
- [ ] All special characters properly escaped
- [ ] No Markdown syntax errors
- [ ] Readability is high (scannable, short paragraphs)

## Common Markdown Mistakes

❌ **Inconsistent list formatting**: Mix of `-`, `*`, `+`
❌ **Too many heading levels**: H1, H2, H5, H3 (confusing structure)
❌ **Missing code block language**: ``` without language specified
❌ **Bad link text**: "click here" instead of descriptive text
❌ **Missing image alt text**: Accessibility issue
❌ **Excessive blank lines**: Reduces readability
❌ **Poor structure**: No clear hierarchy
❌ **Mixing styles**: Italics and bold used inconsistently
❌ **No metadata**: Missing front matter
❌ **Broken image links**: Images don't load

## Quick Markdown Reference

```markdown
# Heading 1 (use once)
## Heading 2 (use for sections)
### Heading 3 (use for subsections)

**bold** or *italic*
`code`

- Bullet point
1. Numbered point

> Blockquote

[Link](https://example.com)
![Image alt](image_url)

| Column | Column |
|--------|--------|
| Data   | Data   |

```code block```
```

---

## Export as Markdown

All articles should be exported or saved as:
- **Format**: `.md` file (Markdown text file)
- **Encoding**: UTF-8
- **Line endings**: LF (Unix) recommended
- **Naming**: `article-title-words.md` (lowercase with hyphens)
- **Metadata**: YAML front matter at top

This ensures maximum compatibility and portability across all platforms and tools.
