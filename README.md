# AI Agents & Skills for Technical Writers

A complete, production-ready system for generating high-quality technical content across multiple platforms with personalized code projects.

**1 Agent + 22 Skills + Secure Configuration = Complete technical writing ecosystem**

## ⚡ Quick Start (2 Minutes)

```bash
# 1. Set up your personal configuration
cp .env.example .env
nano .env  # Fill in your details

# 2. Copy article template
cp docs/ARTICLE_TEMPLATE.md my-article.md

# 3. Use a skill to generate/optimize content
# All skills read from your .env automatically
```

**→ [Full Getting Started Guide](docs/GETTING_STARTED.md)**

---

## What's Included

### 1 Main Agent
- **Senior Technical Software Writer** - Orchestrates all 22 skills

### 22 Specialized Skills

**Language Skills (3)**
- Java, Python, JavaScript content expertise

**Platform Skills (8)**
- LinkedIn, Medium, Dev.to, Substack, DZone, JavaPro, InfoQ, Personal Blog

**Coder Skills (3)** ⭐
- Generate complete Java/Spring Boot projects
- Generate complete Python/FastAPI projects
- Generate complete JavaScript/React projects

**Visual & Presentation Skills (4)**
- Slides Creator - Convert articles to PowerPoint/Google Slides/Speaker Deck
- Image generation (1024x768, 3MB max, abstract futuristic)
- Mermaid diagrams (simple, Git-friendly)
- PlantUML diagrams (complex, professional)

**Supporting Skills (4)**
- Architecture & design patterns
- Markdown formatter
- SEO optimizer
- Code examples generator

**All skills automatically**:
- Use your `.env` configuration
- Follow humanization standards (conversational, human-written)
- Include your personal branding & sign-off
- Link to your GitHub, LinkedIn, Speaker Deck

---

## 📊 System Capabilities

### Write For 8 Platforms
| Platform | Length | Frequency | Best For |
|----------|--------|-----------|----------|
| Dev.to | 1-3k words | 1-2/week | Quick tutorials |
| LinkedIn | 0.8-1.5k | 1-2/week | Career insights |
| Medium | 2-7k words | 1-2/month | Deep dives |
| Substack | 1.5-3k | Weekly | Newsletter |
| DZone | 1.5-4k | Flexible | Enterprise |
| JavaPro | 3-6k words | 1-2/month | Enterprise Java |
| InfoQ | 2-3k words | Flexible | Research |
| Blog | 2-10k+ | Your pace | Full control |

### Generate Projects For 3 Languages
- **Java**: Maven/Spring Boot with tests & docs
- **Python**: Poetry/FastAPI with tests & type hints
- **JavaScript**: npm/React with TypeScript & Jest

### Cover 3 Programming Languages
- Java (Spring Boot, patterns, concurrency)
- Python (FastAPI, async, data science)
- JavaScript (React, Node.js, TypeScript)

---

## 🔒 Secure Configuration

Your personal data stays private and local:

```bash
cp .env.example .env          # Create local config (never committed)
# Edit with your details
AUTHOR_NAME=Your Name
GITHUB_URL=https://github.com/you
LINKEDIN_URL=https://linkedin.com/in/you
# ... and 40+ other variables
```

**Your `.env` file**:
- ✅ Never committed to git (.gitignore protection)
- ✅ Contains all your personal URLs and emails
- ✅ Automatically used by all skills
- ✅ Pre-filled with your discovered profiles

---

## 📚 Documentation

**Start Here**:
- **[Getting Started Guide](docs/GETTING_STARTED.md)** ← Begin here
- **[Configuration Guide](docs/CONFIGURATION.md)** - Set up `.env`
- **[Humanization Standards](docs/HUMANIZATION_GUIDE.md)** - Writing style

**How-To Guides**:
- **[Article Template](docs/ARTICLE_TEMPLATE.md)** - Copy for new articles
- **[Article Sign-Offs](docs/ARTICLE_SIGNOFF.md)** - Sign-off variations
- **[Platform Styles](docs/PLATFORM_STYLES.md)** - Platform-specific guides

**Reference**:
- **[Complete System Overview](docs/guides/COMPLETE_SYSTEM.md)** - Full details
- **[System Architecture](docs/guides/SYSTEM_MAP.md)** - Relationships & flows
- **[Skills Index](docs/guides/SKILLS_INDEX.md)** - All 22 skills described
- **[Agent Profile](agents/technical-writer/AGENT.md)** - Agent details
- **[Slides Creator Guide](docs/SLIDES_CREATOR_GUIDE.md)** - Convert articles to presentations

---

## 🚀 Common Workflows

### Workflow 1: Write & Publish Article
```
1. Write article in docs/ARTICLE_TEMPLATE.md
2. Use platform skill to optimize (medium-optimizer, devto-formatter, etc.)
3. Publish to platform
4. Your article automatically includes:
   - Your name, email, bio
   - Links to GitHub, LinkedIn, Speaker Deck
   - Custom sign-off: "Need more tech insights? Happy coding!"
```

### Workflow 2: Generate Code Project
```
1. Write article explaining concept
2. Request: "Generate Java code for my article [title]"
3. Get complete Maven project with:
   - Source code in src/main/java/
   - Tests in src/test/java/
   - README linking to article
   - pom.xml with dependencies
4. Readers can clone and run immediately
```

### Workflow 3: Multi-Platform Publishing
```
1. Write master article with sr-tech-blog
2. Export as Markdown
3. Adapt for each platform:
   - LinkedIn (1000 words, professional)
   - Medium (3000 words, deep)
   - Dev.to (2000 words, practical)
   - Etc.
```

---

## ✨ Key Features

**🎯 Humanization Standards**
- Conversational tone (write like talking to a friend)
- 8th-10th grade reading level
- No AI-written phrases ("in today's digital landscape")
- No Oxford commas
- Natural contractions and first/second person

**🔐 Secure & Private**
- Personal data in `.env` (local, never committed)
- `.env.example` safe to share (template only)
- All URLs pre-filled from your discovered profiles
- Team-friendly (each person has own `.env`)

**📝 Professional Branding**
- Consistent sign-off on all articles
- Links to GitHub, LinkedIn, Speaker Deck automatically
- Drives traffic to your profiles
- One source of truth for links

**💻 Code Generation**
- Generate complete, runnable projects
- Articles link to code, code links back to article
- Full test coverage included
- Production-ready structure

**🎨 Visual Content**
- Image specs: 1024x768px, max 3MB, abstract futuristic
- Mermaid diagrams (simple, Git-friendly)
- PlantUML diagrams (complex, professional)
- All tools and workflows documented

**🌍 Multi-Platform**
- 8 publishing platforms supported
- Write once, adapt for multiple platforms
- Platform-specific optimizations
- Same branding across all platforms

---

## Your Profiles (Pre-Configured)

All automatically linked in your generated content:

- **Dev.to**: https://dev.to/wallaceespindola
- **GitHub**: https://github.com/wallaceespindola
- **LinkedIn**: https://www.linkedin.com/in/wallaceespindola/
- **Speaker Deck**: https://speakerdeck.com/wallacese
- **Sessionize**: https://sessionize.com/wallace-espindola/
- **Medium**: https://medium.com/@wallaceespindola
- **DZone**: https://dzone.com/users/1254611/wallacese.html
- **Substack**: https://wallaceespindola.substack.com
- **Twitter/X**: https://x.com/wsespindola
- **Linktree**: https://linktr.ee/wallace.espindola
- **Solo.to**: https://solo.to/wallace.espindola
- **Gravatar**: https://gravatar.com/wallacese

---

## Project Structure

```
.
├── README.md                          ← You are here
├── CLAUDE.md                          ← Claude Code configuration
├── .env.example                       ← Configuration template
├── .env                               ← Your personal data (not committed)
├── LICENSE
├── .gitignore
│
├── agents/technical-writer/
│   └── AGENT.md                       ← Main agent
│
├── skills/
│   ├── java-content/SKILL.md          ← Java expertise
│   ├── python-content/SKILL.md        ← Python expertise
│   ├── javascript-content/SKILL.md    ← JavaScript expertise
│   ├── ... (8 platform skills)
│   ├── java-coder/SKILL.md            ← Generate Java projects
│   ├── python-coder/SKILL.md          ← Generate Python projects
│   ├── javascript-coder/SKILL.md      ← Generate JS projects
│   ├── ... (7 supporting skills)
│
└── docs/
    ├── GETTING_STARTED.md             ← START HERE
    ├── CONFIGURATION.md               ← Setup guide
    ├── HUMANIZATION_GUIDE.md          ← Writing standards
    ├── ARTICLE_TEMPLATE.md            ← Article template
    ├── ARTICLE_SIGNOFF.md             ← Sign-off variations
    ├── PLATFORM_STYLES.md             ← Platform guides
    │
    └── guides/
        ├── COMPLETE_SYSTEM.md         ← Full system details
        ├── SYSTEM_MAP.md              ← Architecture
        └── SKILLS_INDEX.md            ← All skills reference
```

---

## Getting Help

1. **New to the system?** → [Getting Started Guide](docs/GETTING_STARTED.md)
2. **Need to configure?** → [Configuration Guide](docs/CONFIGURATION.md)
3. **Want to write better?** → [Humanization Guide](docs/HUMANIZATION_GUIDE.md)
4. **Need skill details?** → [Skills Index](docs/guides/SKILLS_INDEX.md)
5. **Curious about architecture?** → [System Architecture](docs/guides/SYSTEM_MAP.md)

---

## Key Points

✅ **1 Agent + 22 Skills** - Complete system ready to use
✅ **3 Coder Skills** - Generate Java, Python, JavaScript projects
✅ **Slides Creator** - Convert articles to presentations
✅ **8 Platforms** - Publish to LinkedIn, Medium, Dev.to, and more
✅ **Secure Configuration** - Your data stays local in `.env`
✅ **Humanization Standards** - Write like a real person, not AI
✅ **Professional Branding** - Your sign-off on every article
✅ **Pre-Configured URLs** - All your profiles auto-linked

---

## Next Steps

1. Read **[Getting Started Guide](docs/GETTING_STARTED.md)**
2. Create `.env` file: `cp .env.example .env`
3. Fill in your personal information
4. Copy `docs/ARTICLE_TEMPLATE.md` for your first article
5. Choose a platform and use the appropriate skill
6. Publish!

**Welcome to your AI-powered technical writing system!** 🚀

---

## About the Author

**Wallace Espindola** - Senior Software Engineer
- Expertise: Java, Python, JavaScript, Cloud Architecture
- Focus: Building production-ready systems and sharing knowledge

### Connect & Follow

- **GitHub**: https://github.com/wallaceespindola
- **LinkedIn**: https://www.linkedin.com/in/wallaceespindola/
- **Dev.to**: https://dev.to/wallaceespindola
- **Medium**: https://medium.com/@wallaceespindola
- **Speaker Deck**: https://speakerdeck.com/wallacese
- **Substack**: https://wallaceespindola.substack.com
- **DZone**: https://dzone.com/users/1254611/wallacese.html
- **Sessionize**: https://sessionize.com/wallace-espindola/
- **Twitter/X**: https://x.com/wsespindola

### Quick Links

- **Linktree**: https://linktr.ee/wallace.espindola
- **Solo.to**: https://solo.to/wallace.espindola
- **Gravatar**: https://gravatar.com/wallacese

---

*This system is designed for technical writers who want to create high-quality content across multiple platforms efficiently. Built with AI assistance, following strict humanization standards, and maintaining personal branding consistency.*
