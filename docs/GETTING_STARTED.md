---
description: Quick start guide to get your technical writing and code generation system up and running
---

# Getting Started with Your AI Agents & Skills

Welcome! This guide will get you from zero to publishing your first article with generated code in minutes.

## What You Have

A complete system with:
- **1 Main Agent** - Senior Technical Software Writer
- **21 Skills** - Language-specific, platform-specific, visual, architecture, and supporting skills
- **3 Coder Skills** - Generate complete Java, Python, and JavaScript projects
- **Configuration System** - Your personal data stays secure
- **Article Templates** - Ready-to-use starting points

## Quick Start (5 Minutes)

### Step 1: Set Up Your Configuration

```bash
# Copy the configuration template
cp .env.example .env

# Edit with your information
nano .env
```

Fill in at minimum:
```env
AUTHOR_NAME=Wallace Espindola
AUTHOR_EMAIL=your.email@example.com
AUTHOR_BIO=Your professional bio
AUTHOR_TITLE=Senior Software Engineer
```

(The other URLs are already pre-filled from your profiles!)

### Step 2: Write Your First Article

```bash
# Copy the article template
cp docs/ARTICLE_TEMPLATE.md docs/articles/my-first-article.md

# Edit and write your content
nano docs/articles/my-first-article.md
```

### Step 3: Generate Related Code Project (Optional)

```
Generate Java/Python/JavaScript code for my article about [topic]
Include:
- [specific implementation details]
- Tests with examples
- README linking to the article
```

### Step 4: Publish!

Choose your platform and use the relevant formatter skill to optimize for that platform.

---

## What Goes Where

```
.
├── README.md                          ← Start here
├── CLAUDE.md                          ← Claude Code configuration
├── .env                               ← YOUR PERSONAL DATA (never commit)
├── .env.example                       ← Template for .env
│
├── agents/
│   └── article-writer/
│       └── AGENT.md                   ← Main agent profile
│
├── skills/
│   ├── java-content/SKILL.md
│   ├── python-content/SKILL.md
│   ├── javascript-content/SKILL.md
│   ├── ... (18 more skills)
│
└── docs/
    ├── GETTING_STARTED.md             ← You are here
    ├── CONFIGURATION.md               ← How to set up .env
    ├── HUMANIZATION_GUIDE.md          ← Writing standards
    ├── ARTICLE_TEMPLATE.md            ← Template for articles
    ├── ARTICLE_SIGNOFF.md             ← Your sign-off template
    ├── PLATFORM_STYLES.md             ← Platform-specific guides
    │
    └── guides/
        ├── COMPLETE_SYSTEM.md         ← Full system overview
        ├── SYSTEM_MAP.md              ← Architecture & relationships
        ├── SKILLS_INDEX.md            ← Detailed skill catalog
        └── (more reference docs)
```

---

## The Workflow

### For Writing Articles

1. **Write article** in `docs/articles/ARTICLE.md`
   - Use `docs/ARTICLE_TEMPLATE.md` as starting point
   - Your `.env` values automatically fill in

2. **Optimize for platform**
   - LinkedIn: Use `linkedin-pulse-formatter` skill
   - Medium: Use `medium-optimizer` skill
   - Dev.to: Use `devto-formatter` skill
   - Etc.

3. **Publish** to your platform

4. **Your article automatically includes**:
   - ✅ Your name and bio
   - ✅ Links to your GitHub, LinkedIn, Speaker Deck
   - ✅ Sign-off: "Need more tech insights? Check out my GitHub, LinkedIn, and Speaker Deck. Happy coding!"

### For Code Projects

1. **Write article** explaining the concept

2. **Request code generation**:
   ```
   Generate Java code for my article "Spring Boot REST API Best Practices"
   Include: REST controller, service layer, tests, README
   ```

3. **Get complete project**:
   - `src/main/java/` - Source code
   - `src/test/java/` - Tests
   - `pom.xml` - Dependencies
   - `README.md` - Links to your article

4. **Readers can**:
   - Clone the project
   - Run it locally
   - See working code
   - Reference the article for explanation

---

## 8 Platforms You Can Publish To

| Platform | Best For | Length | Frequency |
|----------|----------|--------|-----------|
| **Dev.to** | Community tutorials | 1000-3000 | 1-2/week |
| **LinkedIn** | Career insights | 800-1500 | 1-2/week |
| **Medium** | Deep technical dives | 2000-7000 | 1-2/month |
| **Substack** | Newsletter | 1500-3000 | Weekly |
| **DZone** | Enterprise patterns | 1500-4000 | Flexible |
| **JavaPro** | Enterprise Java | 3000-6000 | 1-2/month |
| **InfoQ** | Research-informed | 2000-3000 | Flexible |
| **Blog** | Full control | 2000-10k+ | Your pace |

---

## 3 Languages You Can Write About

- **Java** - Spring Boot, design patterns, concurrency
- **Python** - FastAPI, async/await, data science
- **JavaScript** - React, Node.js, TypeScript

Each has expertise skills with best practices and patterns.

---

## 21 Skills Available

### Language Skills (3)
- java-content
- python-content
- javascript-content

### Platform Skills (8)
- linkedin-pulse-formatter
- medium-optimizer
- devto-formatter
- substack-newsletter
- dzone-article
- javapro-magazine
- infoq-article
- sr-tech-blog

### Coder Skills (3)
- java-coder ← Generates complete Maven/Spring Boot projects
- python-coder ← Generates complete FastAPI projects
- javascript-coder ← Generates complete React/Node.js projects

### Supporting (7)
- architecture-design
- image-generator-blog
- diagram-mermaid
- diagram-plantuml
- markdown-formatter
- seo-optimizer
- code-examples-generator

---

## Common Questions

### Q: Where does my personal data go?

**A**: Your `.env` file stays local (never committed to git). All your URLs, emails, and profiles stay private. Only the `.env.example` template is in git.

### Q: Can I publish the same article to multiple platforms?

**A**: Yes! Write once, adapt for multiple platforms:
1. Write master article in `sr-tech-blog`
2. Export as markdown with `markdown-formatter`
3. Adapt for each platform:
   - `linkedin-pulse-formatter` (1000 words)
   - `medium-optimizer` (3000 words)
   - `devto-formatter` (2000 words)
   - Etc.

### Q: How do I customize article sign-offs?

**A**: See `docs/ARTICLE_SIGNOFF.md` for platform-specific variations:
- Standard: GitHub, LinkedIn, Speaker Deck
- With newsletter: Adds Substack link
- All platforms: Links to all your profiles
- Minimal: Short one-liner

### Q: Can I use this for team content?

**A**: Yes! Share `.env.example` (template) with team, each person creates their own `.env` locally. Never commit `.env` files.

### Q: What's the humanization standard?

**A**: All content is written to sound genuinely human, not AI-generated:
- Conversational tone
- 8th-10th grade reading level
- No Oxford commas
- Natural contractions
- Real examples and analogies
- No over-use of emojis

See `docs/HUMANIZATION_GUIDE.md` for details.

---

## Next Steps

1. ✅ Create `.env` from `.env.example`
2. ✅ Fill in your personal information
3. ✅ Copy `docs/ARTICLE_TEMPLATE.md` for your first article
4. ✅ Write your article content
5. ✅ Use a skill to optimize for your platform
6. ✅ Publish
7. ✅ (Optional) Generate code project with coder skills

---

## Documentation Structure

**Essential Reading**:
- `docs/CONFIGURATION.md` - Set up your .env file
- `docs/HUMANIZATION_GUIDE.md` - Writing standards
- `docs/ARTICLE_TEMPLATE.md` - Article template
- `docs/ARTICLE_SIGNOFF.md` - Sign-off options

**Reference Guides**:
- `docs/guides/COMPLETE_SYSTEM.md` - Full system overview
- `docs/guides/SYSTEM_MAP.md` - Architecture and relationships
- `docs/guides/SKILLS_INDEX.md` - Detailed skill descriptions
- `docs/PLATFORM_STYLES.md` - Platform-specific style guides

**In Your Project**:
- `agents/article-writer/AGENT.md` - Agent profile
- `skills/[skill-name]/SKILL.md` - Detailed skill documentation

---

## Key Features

✨ **Humanization Standards**
- Conversational, human-written tone
- No AI-written phrases
- 8th-10th grade reading level

🔐 **Secure Configuration**
- Personal data in local `.env` only
- Never committed to git
- All URLs pre-filled from your profiles

📝 **Complete Templates**
- Article template with your sign-off
- Platform-specific variations
- Ready-to-copy starting points

💻 **Code Generation**
- Complete Java projects with Maven
- Complete Python projects with Poetry
- Complete JavaScript projects with TypeScript
- All with tests and documentation

🎨 **Visual Content**
- Image generation specs (1024x768, 3MB max, abstract futuristic)
- Mermaid diagrams (simple, Git-friendly)
- PlantUML diagrams (complex, enterprise-grade)

🔗 **Multi-Platform**
- Write once, publish to 8 platforms
- Platform-specific optimizations
- Automatic link to all your profiles

---

## Help & Resources

- **Configuration**: Read `docs/CONFIGURATION.md`
- **Writing Standards**: Read `docs/HUMANIZATION_GUIDE.md`
- **Skill Details**: See `docs/guides/SKILLS_INDEX.md`
- **Architecture**: See `docs/guides/SYSTEM_MAP.md`
- **All Skills**: Read individual `skills/[name]/SKILL.md` files

---

**Ready?** Start with `docs/CONFIGURATION.md` to set up your `.env` file!
