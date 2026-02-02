---
description: Complete system map showing all agents, skills, and their relationships
---

# Complete System Map: Agents & Skills

## System Overview

**Total**: 1 Agent + 18 Skills = 19 total components

All skills follow **humanization standards** (see HUMANIZATION_GUIDE.md) and **image specifications** (1024x768px, max 3MB, abstract futuristic style).

---

## Main Agent

### Senior Technical Software Writer Agent
**Location**: `agents/technical-writer/AGENT.md`

**Role**: Orchestrates all 18 skills to create professional technical content

**Directly Uses**: All 18 skills below (selects based on content needs)

**Produces**:
- LinkedIn Pulse articles (800-1500 words)
- Medium deep-dives (2000-7000 words)
- Dev.to tutorials (1000-3000 words)
- Substack newsletters (1500-3000 words)
- DZone articles (1500-4000 words)
- JavaPro Magazine pieces (3000-6000 words)
- InfoQ articles (2000-3000 words)
- Personal blog posts (2000-10k+ words)

---

## Skill Categories

### 1. LANGUAGE-SPECIFIC SKILLS (3 skills)

These provide deep expertise in specific programming languages and frameworks.

#### Java Content
**Location**: `skills/java-content/SKILL.md`
- **Purpose**: Java/Spring Boot expertise, design patterns, enterprise architecture
- **Topics**: Java 17+, Spring Boot, concurrency, performance, design patterns
- **Typical Use**: When writing articles about Java development
- **Combines With**:
  - `devto-formatter` → Quick Java tutorials for community
  - `medium-optimizer` → Deep Java technical articles
  - `linkedin-pulse-formatter` → Java career insights
  - `dzone-article` → Enterprise Java patterns
  - `javapro-magazine` → Advanced Java content
  - `sr-tech-blog` → Long-form Java guides
  - `code-examples-generator` → Production Java code
  - `seo-optimizer` → Java keyword research

#### Python Content
**Location**: `skills/python-content/SKILL.md`
- **Purpose**: Python/FastAPI expertise, async patterns, data science
- **Topics**: Python 3.9+, async/await, FastAPI, Django, data science, type hints
- **Typical Use**: When writing articles about Python development
- **Combines With**:
  - `devto-formatter` → Quick Python tutorials
  - `medium-optimizer` → Deep Python technical content
  - `linkedin-pulse-formatter` → Python career insights
  - `substack-newsletter` → Weekly Python newsletter
  - `sr-tech-blog` → Long-form Python guides
  - `code-examples-generator` → Production Python code
  - `seo-optimizer` → Python keyword research

#### JavaScript/TypeScript Content
**Location**: `skills/javascript-content/SKILL.md`
- **Purpose**: JavaScript/TypeScript expertise, React patterns, Node.js backend
- **Topics**: ES2020+, TypeScript, React hooks, Node.js, performance, async patterns
- **Typical Use**: When writing articles about JavaScript/web development
- **Combines With**:
  - `devto-formatter` → Quick JavaScript tutorials
  - `medium-optimizer` → Deep JavaScript technical content
  - `linkedin-pulse-formatter` → JavaScript career growth
  - `sr-tech-blog` → Long-form JavaScript guides
  - `code-examples-generator` → Production JavaScript code
  - `seo-optimizer` → JavaScript keyword research

---

### 2. PLATFORM-SPECIFIC SKILLS (7 skills)

These optimize content for specific publication platforms.

#### LinkedIn Pulse Formatter
**Location**: `skills/linkedin-pulse-formatter/SKILL.md`
- **Purpose**: Optimize articles for LinkedIn professional network
- **Format**: 800-1500 words, professional tone, career-focused
- **Audience**: Career-focused developers, networking focus
- **Frequency**: 1-2 per week
- **Works With**:
  - Any language skill (Java, Python, JavaScript)
  - `architecture-design` → Career insights on architecture
  - `seo-optimizer` → LinkedIn SEO optimization

#### Medium Optimizer
**Location**: `skills/medium-optimizer/SKILL.md`
- **Purpose**: Create authoritative deep-dive articles for Medium
- **Format**: 2000-7000 words, detailed, educational
- **Audience**: Learning-oriented developers, technical authority building
- **Frequency**: 1-2 per month
- **Works With**:
  - Any language skill (Java, Python, JavaScript)
  - `architecture-design` → Detailed architecture articles
  - `code-examples-generator` → Comprehensive code samples
  - `seo-optimizer` → Medium SEO and curation
  - `image-generator-blog` → Featured images

#### Dev.to Formatter
**Location**: `skills/devto-formatter/SKILL.md`
- **Purpose**: Create community-focused practical tutorials
- **Format**: 1000-3000 words, friendly, practical, quick wins
- **Audience**: All skill levels, community-driven
- **Frequency**: 1-2 per week
- **Works With**:
  - Any language skill (Java, Python, JavaScript)
  - `code-examples-generator` → Practical code samples
  - `seo-optimizer` → Dev.to algorithm optimization
  - `image-generator-blog` → Tutorial screenshots/diagrams

#### Substack Newsletter
**Location**: `skills/substack-newsletter/SKILL.md`
- **Purpose**: Build sustainable technical newsletter with growth
- **Format**: 1500-3000 words, weekly or bi-weekly, email format
- **Audience**: Email subscribers, building community
- **Model**: Free + paid tier strategy
- **Works With**:
  - Any language skill (Java, Python, JavaScript)
  - `architecture-design` → Industry insights for newsletters
  - `seo-optimizer` → Newsletter discoverability
  - `code-examples-generator` → Code examples for subscribers

#### DZone Article Writer
**Location**: `skills/dzone-article/SKILL.md`
- **Purpose**: Create curated technical articles for enterprise audience
- **Format**: 1500-4000 words, professional, enterprise-focused, editorial review
- **Audience**: Enterprise developers and architects
- **Frequency**: Flexible (submission-based)
- **Works With**:
  - Any language skill (Java, Python, JavaScript)
  - `architecture-design` → Enterprise architecture content
  - `code-examples-generator` → Production-grade code
  - `seo-optimizer` → DZone curation optimization
  - `image-generator-blog` → Architecture diagrams

#### JavaPro Magazine
**Location**: `skills/javapro-magazine/SKILL.md`
- **Purpose**: Create enterprise-grade Java articles for professional publication
- **Format**: 3000-6000 words, technical, authoritative, publication-grade
- **Audience**: Enterprise developers, senior architects
- **Frequency**: 1-2 per month
- **Works With**:
  - `java-content` → Advanced Java expertise (required)
  - `architecture-design` → Enterprise architecture patterns
  - `code-examples-generator` → Production Java code
  - `seo-optimizer` → Publication credibility
  - `image-generator-blog` → Professional diagrams

#### Sr Tech Blog Writer
**Location**: `skills/sr-tech-blog/SKILL.md`
- **Purpose**: Write comprehensive articles for personal/company blog
- **Format**: 2000-10,000+ words (unlimited), full creative control
- **Audience**: Your target audience
- **Frequency**: Your pace (1-2/week recommended)
- **Monetization**: Ads, sponsorships, products, services
- **Works With**:
  - Any language skill (Java, Python, JavaScript)
  - `architecture-design` → Deep architectural insights
  - `code-examples-generator` → Comprehensive code examples
  - `seo-optimizer` → Long-term SEO authority
  - `markdown-formatter` → Archiving and version control
  - `image-generator-blog` → Featured images and diagrams

#### InfoQ Article Writer
**Location**: `skills/infoq-article/SKILL.md`
- **Purpose**: Write research-informed editorial articles for InfoQ
- **Format**: 1500-4000 words (optimal 2000-3000), editorial review, five key takeaways
- **Audience**: Architects, senior engineers, CTOs
- **Frequency**: Flexible (editorial submission-based)
- **Publishing**: 4-week exclusive rights, then can republish
- **Works With**:
  - Any language skill (Java, Python, JavaScript)
  - `architecture-design` → Architecture patterns and case studies
  - `code-examples-generator` → Implementation examples
  - `image-generator-blog` → Architecture visuals
  - `seo-optimizer` → Keyword research for InfoQ

---

### 3. CODER SKILLS (3 skills)

These generate complete, production-ready projects that link to technical articles. Perfect for creating code that readers can immediately clone and run.

#### Java Coder
**Location**: `skills/java-coder/SKILL.md`
- **Purpose**: Generate complete Maven/Spring Boot projects with full source code
- **Generates**: pom.xml, source in `src/main/java/`, tests in `src/test/java/`
- **Includes**: README linking to article, full project structure, dependency management
- **Use When**: Writing Java tutorial, design pattern, or REST API article
- **Works With**:
  - `java-content` → Provides Java expertise for generated code
  - Articles in `docs/ARTICLE.md` → Code links back to explanation
  - `code-examples-generator` → For snippet examples within article
  - `architecture-design` → For pattern explanations
  - `image-generator-blog` → For architecture diagrams in docs

#### Python Coder
**Location**: `skills/python-coder/SKILL.md`
- **Purpose**: Generate complete poetry/uv projects with full source code
- **Generates**: pyproject.toml, source in `src/project_name/`, tests in `tests/`
- **Includes**: README linking to article, full project structure, type hints
- **Use When**: Writing FastAPI tutorial, async pattern, or data processing article
- **Works With**:
  - `python-content` → Provides Python expertise for generated code
  - Articles in `docs/ARTICLE.md` → Code links back to explanation
  - `code-examples-generator` → For snippet examples within article
  - `architecture-design` → For pattern explanations
  - `image-generator-blog` → For architecture diagrams in docs

#### JavaScript/TypeScript Coder
**Location**: `skills/javascript-coder/SKILL.md`
- **Purpose**: Generate complete npm/pnpm React or Node.js projects
- **Generates**: package.json, tsconfig.json, source in `src/`, tests with Jest
- **Includes**: README linking to article, strict TypeScript, full testing
- **Use When**: Writing React tutorial, async pattern, or Node.js article
- **Works With**:
  - `javascript-content` → Provides JavaScript/TypeScript expertise
  - Articles in `docs/ARTICLE.md` → Code links back to explanation
  - `code-examples-generator` → For snippet examples within article
  - `architecture-design` → For pattern explanations
  - `image-generator-blog` → For architecture diagrams in docs

---

### 4. ARCHITECTURE & DESIGN SKILL (1 skill)

#### Architecture & Software Design
**Location**: `skills/architecture-design/SKILL.md`
- **Purpose**: Deep expertise on software architecture patterns and system design
- **Topics**: Microservices, event-driven, CQRS, event sourcing, hexagonal, design principles (SOLID, DRY, KISS, YAGNI, GRASP)
- **Use When**: Writing about architecture, system design, design patterns
- **Works With**:
  - All language skills (provides architectural context)
  - All platform skills (can adapt to any platform)
  - `diagram-mermaid` or `diagram-plantuml` → Visual architecture
  - `code-examples-generator` → Architecture implementation examples
  - `image-generator-blog` → Architecture diagrams

---

### 5. VISUAL SKILLS (3 skills)

These create visual content for articles.

#### Image Generator for Blog
**Location**: `skills/image-generator-blog/SKILL.md`
- **Purpose**: Generate professional featured images and in-article visuals
- **Specifications**: 1024x768px, max 3MB, abstract futuristic style
- **Tools**: Figma, Canva Pro, Midjourney, DALL-E 3, stock photos
- **Image Types**: Featured images, diagrams, flowcharts, screenshots, comparisons, infographics
- **Works With**: Every article needs images
  - All platform skills (featured images)
  - `diagram-mermaid` → Diagram export optimization
  - `diagram-plantuml` → UML diagram visualization
  - Any content skill (article visuals)

#### Mermaid Diagrams
**Location**: `skills/diagram-mermaid/SKILL.md`
- **Purpose**: Generate Git-friendly diagrams using diagram-as-code
- **Formats**: Flowchart, sequence, class, state, ER, C4 model, Git graph, timeline
- **Speed**: 15-20 minutes per diagram
- **Key Feature**: Text-based, version control friendly, GitHub native support
- **Works With**:
  - `architecture-design` → Architecture visualizations
  - `image-generator-blog` → Diagram optimization
  - Any platform skill (embed directly in articles)
  - `markdown-formatter` → Markdown diagram syntax

#### PlantUML Diagrams
**Location**: `skills/diagram-plantuml/SKILL.md`
- **Purpose**: Generate professional UML and complex architecture diagrams
- **Formats**: Class, sequence, use case, state machine, component, deployment, activity, object
- **Speed**: 30-45 minutes per diagram
- **Key Feature**: Full UML 2.5 standard, enterprise-grade precision
- **Works With**:
  - `architecture-design` → Enterprise architecture
  - `image-generator-blog` → Professional diagram visualization
  - Any platform skill (export to SVG/PNG)
  - JavaPro Magazine, DZone, InfoQ (professional publications)

---

### 6. SUPPORTING SKILLS (3 skills)

These enhance and optimize content across all platforms.

#### Markdown Formatter
**Location**: `skills/markdown-formatter/SKILL.md`
- **Purpose**: Format all articles in universal Markdown for archiving and version control
- **Features**: YAML frontmatter, proper hierarchy, code blocks (50+ languages), images, tables, footnotes
- **Works With**: Every article benefits from markdown export
  - All platform skills (universal export format)
  - `image-generator-blog` → Image metadata and alt text
  - `code-examples-generator` → Code block formatting
  - Git version control

#### SEO Optimizer
**Location**: `skills/seo-optimizer/SKILL.md`
- **Purpose**: Improve long-term content discovery through search
- **Methods**: Keyword research, search intent, article optimization, internal linking, technical SEO, schema markup, topic clusters, backlink strategy
- **Works With**: Every article benefits from SEO
  - All platform skills (platform-specific SEO)
  - All language skills (keyword research)
  - `markdown-formatter` → SEO-friendly metadata
  - Long-term discoverability strategy

#### Code Examples Generator
**Location**: `skills/code-examples-generator/SKILL.md`
- **Purpose**: Generate production-ready code examples
- **Languages**: Java, Python, JavaScript/TypeScript
- **Features**: Complete vs. snippet examples, before/after, step-by-step, real-world examples, testing examples, error handling patterns
- **Works With**: Every technical article needs code
  - All language skills (code validation and patterns)
  - All platform skills (code formatting per platform)
  - `markdown-formatter` → Universal code formatting

---

## Workflow Relationships

### Common Workflow: Platform + Language
```
Language Skill (choose 1)
    ↓
Platform Skill (choose 1)
    ↓
Code Examples Generator (add code)
    ↓
SEO Optimizer (optimize keywords)
    ↓
Image Generator (add featured image)
    ↓
Markdown Formatter (archive)
```

### Example 1: Quick Dev.to Tutorial
```
javascript-content
    ↓
devto-formatter
    ↓
code-examples-generator (JavaScript examples)
    ↓
image-generator-blog (screenshot/diagram)
    ↓
markdown-formatter (archive)
```

### Example 2: Deep Medium Article
```
python-content OR java-content
    ↓
medium-optimizer
    ↓
code-examples-generator
    ↓
architecture-design (if needed)
    ↓
diagram-mermaid or diagram-plantuml
    ↓
image-generator-blog (featured image + diagrams)
    ↓
seo-optimizer (keyword research)
    ↓
markdown-formatter (archive)
```

### Example 3: Enterprise JavaPro Magazine
```
java-content
    ↓
javapro-magazine
    ↓
architecture-design
    ↓
code-examples-generator
    ↓
diagram-plantuml (UML diagrams)
    ↓
image-generator-blog (professional visuals)
    ↓
seo-optimizer
    ↓
markdown-formatter
```

### Example 4: Multi-Platform Publishing
```
Write core article using:
    ↓
language-content + sr-tech-blog
    ↓
markdown-formatter (export master version)
    ↓
Adapt for each platform:
    ├── linkedin-pulse-formatter
    ├── medium-optimizer
    ├── devto-formatter
    ├── substack-newsletter
    ├── dzone-article
    └── infoq-article
    ↓
seo-optimizer (for each platform)
```

### Example 5: Newsletter Series
```
language-content (topic ideas)
    ↓
substack-newsletter (structure)
    ↓
code-examples-generator (examples)
    ↓
image-generator-blog (hero images)
    ↓
seo-optimizer (discoverability)
    ↓
markdown-formatter (archive issues)
```

---

## Skill Selection Matrix

### By Platform (Choose 1)
| Platform | Skill | Length | Use When |
|----------|-------|--------|----------|
| LinkedIn | linkedin-pulse-formatter | 800-1500 | Quick professional insights |
| Medium | medium-optimizer | 2000-7000 | Deep technical content |
| Dev.to | devto-formatter | 1000-3000 | Practical quick wins |
| Substack | substack-newsletter | 1500-3000 | Building subscriber base |
| DZone | dzone-article | 1500-4000 | Enterprise patterns |
| JavaPro | javapro-magazine | 3000-6000 | Advanced Java only |
| InfoQ | infoq-article | 2000-3000 | Research-informed patterns |
| Blog | sr-tech-blog | 2000-10k+ | Full creative control |

### By Language (Choose 1)
| Language | Skill | Best For |
|----------|-------|----------|
| Java | java-content | Enterprise, patterns, Spring Boot |
| Python | python-content | Backend, data science, async |
| JavaScript | javascript-content | Frontend, full-stack, React |

### By Content Type
| Type | Skills | Platform Options |
|------|--------|------------------|
| Quick Tutorial | language + code-examples | dev.to, blog |
| Deep Dive | language + architecture | Medium, sr-tech-blog |
| Industry Insight | language + architecture | LinkedIn, Substack, InfoQ |
| Enterprise Pattern | java/python/js + dzone/javapro | DZone, JavaPro Magazine |
| Multi-Platform | language + all formatters | All platforms |
| Case Study | language + architecture | Medium, DZone, InfoQ, blog |
| Architecture | architecture-design + diagrams | All platforms |

### By Time Available
| Time | Skills | Output |
|------|--------|--------|
| 1-2 hours | devto-formatter + code-examples | Dev.to article (1000-2000 words) |
| 3-4 hours | medium-optimizer + code-examples | Medium article (2000-3000 words) |
| 5-6 hours | sr-tech-blog + architecture | Blog post (3000-5000 words) |
| 8+ hours | sr-tech-blog + architecture + diagrams | Comprehensive guide (5000+ words) |

---

## Cross-Skill Dependencies

### Always Needed
- **Humanization standards** (HUMANIZATION_GUIDE.md) - applies to ALL skills
- **Image specs** (1024x768px, max 3MB, abstract futuristic) - for image-generator-blog

### Often Used Together
| Pair | Reason |
|------|--------|
| language + platform | Every article needs both |
| platform + code-examples | Almost every technical article |
| platform + image-generator | Every article needs a featured image |
| architecture + diagrams | Architecture articles need visuals |
| any + seo-optimizer | Long-term discoverability |
| any + markdown-formatter | Archiving and version control |

### Sometimes Used Together
| Pair | Reason |
|------|--------|
| architecture + language | When explaining patterns in specific language |
| diagram-mermaid + diagram-plantuml | Choose one based on complexity |
| linkedin + medium | Repurposing content for different audiences |
| substack + all others | Newsletter draws from other content |

---

## Specialization by Platform

### Quick Publishing (1-2 days)
- Dev.to (devto-formatter)
- LinkedIn (linkedin-pulse-formatter)

### Medium Timeline (3-7 days)
- Medium (medium-optimizer)
- DZone (dzone-article) - includes editorial review

### Long Timeline (2-4 weeks)
- JavaPro Magazine (javapro-magazine) - peer review
- InfoQ (infoq-article) - editorial review (3-6 weeks)

### Unlimited Timeline
- Personal Blog (sr-tech-blog)
- Substack (substack-newsletter) - sustainable, ongoing

---

## Content Specialization

### Enterprise-Focused
- JavaPro Magazine (javapro-magazine)
- DZone Article (dzone-article)
- InfoQ Article (infoq-article)
- With: architecture-design skill

### Community-Focused
- Dev.to (devto-formatter)
- LinkedIn (linkedin-pulse-formatter)
- Substack (substack-newsletter)

### Deep Technical
- Medium (medium-optimizer)
- Sr Tech Blog (sr-tech-blog)
- With: code-examples-generator, diagrams

### Career Growth
- LinkedIn (linkedin-pulse-formatter)
- Substack (substack-newsletter)
- Sr Tech Blog (sr-tech-blog)

---

## Summary Statistics

| Category | Count |
|----------|-------|
| **Agents** | 1 |
| **Total Skills** | 21 |
| **Language Skills** | 3 |
| **Platform Skills** | 8 (7 publications + blog) |
| **Coder Skills** | 3 |
| **Architecture/Design** | 1 |
| **Visual Skills** | 3 |
| **Supporting Skills** | 3 |
| **Platforms Supported** | 8 (LinkedIn, Medium, Dev.to, Substack, DZone, JavaPro, InfoQ, Blog) |
| **Languages Supported** | 3 |
| **Coder Project Types** | 3 (Maven/Spring, Poetry/FastAPI, npm/React) |
| **Diagram Types** | 16+ (Mermaid + PlantUML combined) |

---

## Quick Navigation

**Want to learn more?**
- Agent details: Read `agents/technical-writer/AGENT.md`
- Specific skill: Read `skills/[skill-name]/SKILL.md`
- Writing standards: Read `HUMANIZATION_GUIDE.md`
- Image specs: Read `skills/image-generator-blog/SKILL.md`
- Platform guides: Read `PLATFORM_STYLES.md`
- Complete system: Read `COMPLETE_SYSTEM.md`

**Ready to write?**
1. Choose a platform (skill)
2. Choose a language (skill)
3. Pick a topic
4. Use the relevant skills to structure and optimize
5. Add code, images, diagrams as needed
6. Export as Markdown for archiving
