# AI Agents & Skills for Software Engineering

A comprehensive system of specialized AI agents for software engineering, technical content creation, and project management.

**8 Agents + 67 Skills = Complete software engineering ecosystem**

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

### 8 Specialized Agents

#### **Technical Writer Agent** (Original)
- Expertise: Content creation, documentation, multi-platform publishing
- Skills: 22 skills for writing, formatting, and code generation

#### **Java Developer Agent**
- Expertise: Java 17+, Spring Boot, microservices
- Skills: Code review, testing strategy, performance tuning, security audit, project setup, documentation

#### **Python Developer Agent**
- Expertise: Python 3.10+, FastAPI, async programming
- Skills: Code review, testing strategy, performance tuning, type checking, project setup, documentation

#### **JavaScript/Frontend Developer Agent**
- Expertise: React, Next.js, TypeScript, modern web
- Skills: Code review, testing strategy, performance optimization, TypeScript migration, project setup, documentation

#### **Software Architect Agent**
- Expertise: System design, scalability, microservices architecture
- Skills: Architecture review, system design documentation, scalability analysis, design patterns, API design, database design, architecture diagrams

#### **QA/Software Tester Agent**
- Expertise: Test automation, quality assurance, continuous testing
- Skills: Test strategy, test automation setup, test case generation, API testing, E2E testing, performance testing, bug reporting

#### **DevOps Engineer Agent**
- Expertise: CI/CD, containerization, infrastructure-as-code, cloud operations
- Skills: CI/CD pipeline setup, Docker configuration, Kubernetes setup, IaC templates, monitoring setup, security scanning, deployment strategies

#### **Project Manager Agent**
- Expertise: Agile methodologies, planning, risk management, stakeholder communication
- Skills: Project planning, sprint planning, risk assessment, status reporting, retrospectives, roadmap planning

### 67 Specialized Skills

**Technical Writing (22 skills)** - Content creation, platform optimization, code generation, diagrams, SEO

**Java Development (6 skills)** - Code review, testing, performance, security, project setup, documentation

**Python Development (6 skills)** - Code review, testing, performance, type checking, project setup, documentation

**JavaScript/Frontend (6 skills)** - Code review, testing, performance, TypeScript migration, project setup, documentation

**Software Architecture (7 skills)** - System review, design documentation, scalability, patterns, API design, database design, diagrams

**QA & Testing (7 skills)** - Test strategy, automation setup, test case generation, API testing, E2E testing, performance testing, bug reporting

**DevOps & Infrastructure (7 skills)** - CI/CD pipelines, Docker, Kubernetes, IaC, monitoring, security scanning, deployment strategies

**Project Management (6 skills)** - Project planning, sprint planning, risk assessment, status reports, retrospectives, roadmap planning

---

## 📊 System Capabilities

### Software Engineering Coverage
- **Code Development**: Java, Python, JavaScript with specialized expertise
- **Quality Assurance**: Comprehensive testing from unit tests to E2E automation
- **Architecture**: System design, scalability analysis, design patterns
- **Infrastructure**: CI/CD pipelines, containerization, Kubernetes, infrastructure-as-code
- **Project Management**: Agile planning, sprint management, risk assessment, roadmaps
- **Technical Writing**: Multi-platform content creation, documentation, code generation

### Agent Collaboration Workflows
```
Full-Stack Feature Development:
Project Manager → Architect → Java/Python/JS Developers →
QA/Tester → DevOps Engineer → Technical Writer

System Redesign:
Architect → Project Manager → All Developers → QA/Tester →
DevOps Engineer → Technical Writer

Performance Optimization:
Architect → Developers → DevOps Engineer → QA/Tester →
Technical Writer
```

### Multi-Language Project Generation
- **Java**: Maven/Spring Boot with tests, documentation, Dockerfile
- **Python**: Poetry/FastAPI with tests, type hints, Dockerfile
- **JavaScript**: npm/React with TypeScript, Jest, Dockerfile

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
├── README.md                              ← You are here
├── CLAUDE.md                              ← Claude Code configuration
├── .env.example                           ← Configuration template
├── .env                                   ← Your personal data (not committed)
├── LICENSE
├── .gitignore
│
├── agents/
│   ├── technical-writer/AGENT.md          ← Writing expertise
│   ├── java-developer/AGENT.md            ← Java/Spring Boot development
│   ├── python-developer/AGENT.md          ← Python/FastAPI development
│   ├── javascript-developer/AGENT.md      ← React/Next.js development
│   ├── software-architect/AGENT.md        ← System design & architecture
│   ├── qa-tester/AGENT.md                 ← Test automation & QA
│   ├── devops-engineer/AGENT.md           ← CI/CD & infrastructure
│   └── project-manager/AGENT.md           ← Agile planning & management
│
├── skills/
│   ├── java-*/                            ← 6 Java development skills
│   ├── python-*/                          ← 6 Python development skills
│   ├── javascript-*/                      ← 6 JavaScript development skills
│   ├── architecture-*/                    ← 7 Architecture & design skills
│   ├── test-*/                            ← 7 QA & testing skills
│   ├── cicd-*/                            ← 7 DevOps & infrastructure skills
│   ├── project-*/                         ← 6 Project management skills
│   ├── ...                                ← 22 Technical writing skills
│   └── */SKILL.md                         ← 67 total skills
│
└── docs/
    ├── GETTING_STARTED.md                 ← START HERE
    ├── CONFIGURATION.md                   ← Setup guide
    ├── AGENTS_GUIDE.md                    ← Complete agent guide (NEW)
    ├── HUMANIZATION_GUIDE.md              ← Writing standards
    ├── ARTICLE_TEMPLATE.md                ← Article template
    ├── ARTICLE_SIGNOFF.md                 ← Sign-off variations
    ├── PLATFORM_STYLES.md                 ← Platform guides
    │
    └── guides/
        ├── COMPLETE_SYSTEM.md             ← Full system details
        ├── SYSTEM_MAP.md                  ← Architecture
        └── SKILLS_INDEX.md                ← All 67 skills reference
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

✅ **8 Agents + 67 Skills** - Complete software engineering ecosystem
✅ **Full-Stack Development** - Java, Python, JavaScript development agents
✅ **Quality & Testing** - Comprehensive QA and test automation
✅ **Infrastructure & DevOps** - CI/CD, containerization, Kubernetes
✅ **System Architecture** - Design patterns, scalability, API design
✅ **Project Management** - Agile planning, sprint management, roadmaps
✅ **Technical Writing** - Multi-platform publishing, code generation, documentation
✅ **Agent Collaboration** - Agents work together on complex workflows

---

## Next Steps

1. Read **[Getting Started Guide](docs/GETTING_STARTED.md)**
2. Review **[Agents Guide](docs/AGENTS_GUIDE.md)** to understand available agents
3. Check **[Skills Index](docs/guides/SKILLS_INDEX.md)** for detailed skill descriptions
4. Create `.env` file: `cp .env.example .env`
5. Choose an agent based on your task
6. Use the appropriate skill with that agent
7. Explore agent collaboration workflows

**Welcome to your AI-powered software engineering system!** 🚀

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

*This system provides specialized AI agents for comprehensive software engineering tasks. Whether you're developing code, managing quality assurance, designing architecture, setting up infrastructure, or managing projects - there's an agent ready to help. All agents work together seamlessly for complex, multi-team workflows.*
