# Technical Writer Skills & Agents Index

Complete catalog of all agents and skills in this repository, organized by purpose.

## Main Agent

### Senior Technical Software Writer Agent
**Location**: `agents/technical-writer/AGENT.md`

The primary agent for this system. Orchestrates multiple skills to create professional technical content across platforms.

**Expertise**:
- Java, Python, JavaScript development
- Platform-specific content strategy
- Multi-platform content adaptation
- Technical accuracy and code validation

**Outputs**:
- LinkedIn Pulse articles
- Medium technical deep-dives
- Dev.to tutorials and quick wins
- Substack newsletters
- JavaPro Magazine articles

**Writing Standard**: All content follows humanization guidelines for conversational, accessible, genuinely human-written tone. See **HUMANIZATION_GUIDE.md** for complete standards.

---

## Coder Skills (Generate Complete Production Projects)

### Java Coder
**Location**: `skills/java-coder/SKILL.md`
**Purpose**: Generate complete Maven/Spring Boot projects with source code, tests, and documentation

**What it generates:**
- pom.xml with all dependencies configured
- Source code in src/main/java/ (controllers, services, repositories, models)
- Tests in src/test/java/ (unit and integration tests)
- README.md linking to article in docs/ARTICLE.md
- Full project structure and setup

**Best For:**
- Java tutorials with runnable code
- Design pattern implementations
- REST API examples
- Spring Boot demonstrations
- Enterprise Java examples

**Project Templates:**
- REST API with Spring Boot
- Design pattern showcase
- Concurrent programming examples
- Spring Boot full stack application

---

### Python Coder
**Location**: `skills/python-coder/SKILL.md`
**Purpose**: Generate complete poetry/uv projects with source code, tests, and documentation

**What it generates:**
- pyproject.toml with all dependencies configured
- Source code in src/project_name/ (API, services, repositories, models)
- Tests in tests/ with pytest (unit and integration tests)
- README.md linking to article in docs/ARTICLE.md
- Type hints throughout, full project structure

**Best For:**
- Python tutorials with runnable code
- FastAPI/Django demonstrations
- Design pattern implementations
- Async/await pattern examples
- Data processing examples

**Project Templates:**
- FastAPI REST API
- Design pattern showcase
- Async/concurrent programming examples
- Data processing pipeline

---

### JavaScript/TypeScript Coder
**Location**: `skills/javascript-coder/SKILL.md`
**Purpose**: Generate complete npm/pnpm React or Node.js projects with TypeScript

**What it generates:**
- package.json with all dependencies configured
- tsconfig.json in strict mode
- Source code in src/ (components, hooks, services, types)
- Tests with Jest and React Testing Library
- README.md linking to article in docs/ARTICLE.md
- Full TypeScript configuration and testing setup

**Best For:**
- React/TypeScript tutorials with runnable code
- Node.js/Express demonstrations
- Design pattern implementations
- React hooks examples
- Async/promise pattern examples

**Project Templates:**
- React component library with hooks
- Node.js REST API
- Design pattern showcase
- Async/promise patterns

---

## Language-Specific Content Skills

### Java Content Skill
**Location**: `skills/java-content/SKILL.md`
**Purpose**: Generate authentic, accurate Java content with best practices

**Topics Covered**:
- Modern Java features (Java 17+)
  - Records, sealed classes, pattern matching, text blocks
- Concurrency & parallelism
  - Virtual threads, structured concurrency, reactive programming
- Spring Boot best practices
  - Dependency injection, configuration, testing, actuators
- JVM performance
  - Garbage collection, profiling, memory optimization
- Design patterns
  - Gang of Four patterns, enterprise patterns, reactive patterns

**Key Features**:
- Article structure templates (tutorials, best practices, patterns)
- Code example guidelines with proper Java idioms
- Production-scale concerns and considerations
- Audience-specific tips (enterprise, startups, Android)
- SEO keywords for Java content

---

### Python Content Skill
**Location**: `skills/python-content/SKILL.md`
**Purpose**: Create Pythonic technical content with modern best practices

**Topics Covered**:
- Modern Python features (3.9+)
  - Type hints, pattern matching, dataclasses, pydantic
- Web development
  - FastAPI, Django, SQLAlchemy, async patterns
- Data science & analysis
  - pandas, NumPy, scikit-learn, visualization
- Async Python
  - asyncio, async/await patterns, structured concurrency
- Performance optimization
  - Profiling, GIL, vectorization, async I/O
- Python ecosystem
  - Poetry, uv, Ruff, testing with pytest

**Key Features**:
- Article structure templates for tutorials and best practices
- Pythonic idiom guidance
- Real-world async patterns
- Data science specific examples
- Backend/API developer focus

---

### JavaScript/TypeScript Content Skill
**Location**: `skills/javascript-content/SKILL.md`
**Purpose**: Generate engaging JavaScript and TypeScript technical content

**Topics Covered**:
- Modern JavaScript (ES2020+)
  - Optional chaining, nullish coalescing, BigInt, dynamic imports
- TypeScript mastery
  - Advanced types, generics, utility types, strict mode
- React patterns (17+)
  - Hooks, custom hooks, Suspense, error boundaries, performance
- Node.js & backend
  - Express, Fastify, middleware, streams, worker threads
- Web performance
  - Core Web Vitals, code splitting, bundle analysis
- Async patterns
  - Promises, async/await, concurrent requests, error handling

**Key Features**:
- React hook patterns and best practices
- TypeScript discriminated union examples
- Backend vs. frontend specific guidance
- Performance measurement and benchmarking
- Modern tooling insights (Vite, esbuild, webpack)

---

## Platform-Specific Formatting Skills

### LinkedIn Pulse Formatter
**Location**: `skills/linkedin-pulse-formatter/SKILL.md`
**Purpose**: Optimize articles for LinkedIn Pulse professional network

**Specifications**:
- **Length**: 800-1,500 words
- **Tone**: Professional but accessible
- **Audience**: Career-focused developers
- **Frequency**: 1-2 per week

**Key Features**:
- Headline crafting for engagement
- Professional tone guidelines
- Engagement strategies and CTAs
- Comment-driving questions
- Tag strategy for discoverability
- Platform restrictions and best practices
- Optimal posting times and frequency

**Best For**:
- Career advice and growth
- Industry trends and insights
- Lessons learned from experience
- Professional perspectives on technology

---

### DZone Article Writer
**Location**: `skills/dzone-article/SKILL.md`
**Purpose**: Create curated technical articles for DZone publication

**Specifications**:
- **Length**: 1,500-4,000 words
- **Tone**: Professional, practical, enterprise-focused
- **Audience**: Enterprise developers and architects
- **Review**: Editorial review process (3-7 days)
- **Frequency**: Flexible (article-based submission)

**Key Features**:
- Article types (tutorials, patterns, case studies, research)
- Editorial review guidance
- DZone curation algorithm optimization
- Production-grade code examples
- Real-world scenario examples
- Performance and scalability sections
- Best practices and pitfalls guidance
- Submission process and requirements

**Best For**:
- Production patterns and techniques
- Enterprise architecture insights
- Data-driven technical articles
- Case studies and real-world examples
- Thought leadership pieces

---

### Sr Tech Blog Writer
**Location**: `skills/sr-tech-blog/SKILL.md`
**Purpose**: Write comprehensive technical articles for personal or company blog

**Specifications**:
- **Length**: 2,000-10,000+ words (unlimited)
- **Tone**: Authoritative, personal, opinionated
- **Audience**: Your target technical audience
- **Format**: Full creative control
- **Frequency**: Your pace (1-2/week recommended)

**Key Features**:
- Multiple post types (tutorials, deep dives, case studies, opinions, benchmarks)
- Blog platform recommendations (Ghost, Hugo, Substack)
- Monetization strategies (ads, sponsorships, products, subscriptions)
- SEO and growth strategy
- Content pillar and cluster strategy
- Analytics and performance tracking
- Comment moderation and community building
- Long-form content mastery

**Best For**:
- Ultimate guides and definitive references
- Building personal brand and authority
- Monetizing technical content
- Creating evergreen archive of knowledge
- Full control over presentation and audience

---

### Medium Optimizer
**Location**: `skills/medium-optimizer/SKILL.md`
**Purpose**: Create authoritative technical deep-dives for Medium

**Specifications**:
- **Length**: 2,000-7,000 words
- **Tone**: Authoritative, detailed, educational
- **Audience**: Learning-oriented developers
- **Frequency**: 1-2 per month

**Key Features**:
- Article structure template for long-form content
- Headline and subtitle optimization
- Image guidelines and placement strategy
- Code formatting best practices for Medium
- Internal linking strategy
- Publication submission guidance
- Medium-specific features (lists, member-only, crosslinking)
- Curation strategies

**Best For**:
- In-depth technical tutorials
- Architectural decisions and patterns
- Case studies and lessons learned
- Comprehensive guides that become references

---

### Dev.to Formatter
**Location**: `skills/devto-formatter/SKILL.md`
**Purpose**: Create community-focused, practical tutorials for Dev.to

**Specifications**:
- **Length**: 1,000-3,000 words
- **Tone**: Friendly, practical, community-focused
- **Audience**: All skill levels, community-driven
- **Frequency**: 1-2 per week

**Key Features**:
- Action-oriented headline formula
- Community-friendly tone guidelines
- Code example best practices
- Tag strategy for maximum reach
- Series feature to group related posts
- Dev.to-specific engagement features
- Discussion question strategies
- Algorithm signals and optimization

**Best For**:
- Quick-win tutorials
- Beginner-friendly explanations
- Code snippets and practical tips
- Building community presence
- Series on progressive topics

---

### Substack Newsletter Skill
**Location**: `skills/substack-newsletter/SKILL.md`
**Purpose**: Build sustainable technical newsletter with growth strategy

**Specifications**:
- **Length**: 1,500-3,000 words typically
- **Frequency**: Weekly (best for growth) or bi-weekly minimum
- **Audience**: Email subscribers, building community
- **Model**: Free + paid tier option

**Key Features**:
- Newsletter structure (essay + curated links + CTA)
- Subject line and preview text strategy
- Opening hook techniques
- Free vs. paid tier strategy
- Subscriber growth tactics and retention
- Engagement metrics and tracking
- Publishing cadence and consistency
- Building newsletter brand and voice
- Early launch checklist

**Best For**:
- Building loyal audience over time
- Original, longer-form insights
- Regular income from paid subscribers
- Deeper reader relationships
- Personal brand building

---

### JavaPro Magazine Skill
**Location**: `skills/javapro-magazine/SKILL.md`
**Purpose**: Create enterprise-grade Java articles for professional publication

**Specifications**:
- **Length**: 3,000-6,000 words
- **Tone**: Professional, authoritative, rigorous
- **Audience**: Enterprise developers and architects
- **Model**: Professional publication with editorial review

**Key Features**:
- Publication-grade article structure (7-10 sections)
- Advanced architecture patterns coverage
- Production considerations and observability
- Case study format with real examples
- Performance analysis and benchmarking
- References and academic rigor
- Submission process guidance
- Technical accuracy requirements
- Research and validation checklist

**Best For**:
- Enterprise Java patterns
- Architectural decisions at scale
- Advanced topics for senior developers
- Building professional authority
- Contributing to industry knowledge

---

## Supporting/Cross-Platform Skills

### Architecture & Software Design
**Location**: `skills/architecture-design/SKILL.md`
**Purpose**: Write comprehensive articles on software architecture, system design, and architectural patterns

**Key Features**:
- Architectural patterns (monolithic, microservices, event-driven, CQRS, Event Sourcing, hexagonal)
- Design principles (SOLID, DRY, KISS, YAGNI, GRASP)
- System design concepts (scalability, reliability, consistency, databases, APIs, deployment)
- Article structures for patterns, system design interviews, case studies
- Real-world examples (Netflix, Uber, Amazon, Airbnb)
- Trade-offs and when to use/not use each approach
- Tools for architecture diagrams (Draw.io, Lucidchart, C4 model)

**Best For**:
- Architectural pattern articles
- System design interview prep
- Case studies on architectural decisions
- Enterprise architecture content
- DDD (Domain-Driven Design) articles

---

### Image Generator for Blog
**Location**: `skills/image-generator-blog/SKILL.md`
**Purpose**: Generate professional featured images and in-article visuals for technical blogs

**Key Features**:
- Featured image specifications (1200x628px, design approaches)
- Design approaches (Figma templates, stock photos, Canva, screenshots)
- In-article image types (diagrams, flowcharts, screenshots, comparisons, infographics, photos)
- Image optimization and file size reduction
- Alt text and accessibility guidelines
- Tools comparison (Canva, Figma, GIMP, stock photos, screenshot tools)
- Workflow (fast 15-min vs quality 30-min approaches)

**Tools Recommended**:
- Canva Pro ($13/month) - Easiest, best value
- Figma Free/Pro - Professional quality, reusable templates
- Draw.io - Diagrams
- Unsplash/Pexels - Free stock photos
- TinyPNG - Image optimization

**Best For**:
- Featured/hero images for blog posts
- Architecture and flow diagrams
- Code screenshots and tutorials
- Comparison graphics
- Infographics and data visualization

---

### Mermaid Diagrams
**Location**: `skills/diagram-mermaid/SKILL.md`
**Purpose**: Generate diagrams using Mermaid diagram-as-code syntax (Git-friendly)

**Diagram Types**:
1. **Flowchart** - Process flows, decision trees
2. **Sequence** - API interactions, protocols
3. **Class** - OOP design, domain models
4. **State** - State machines, FSM
5. **Entity-Relationship** - Database schemas
6. **C4 Model** - Architecture levels
7. **Git Graph** - Branching strategies
8. **Timeline** - Milestones, processes

**Key Features**:
- Text-based, version control friendly
- GitHub/GitLab native support
- Simple syntax, quick to write
- Responsive and auto-scaling
- Embed in Markdown directly
- Styling and customization options
- C4 architecture diagrams
- API/microservice flows

**Best For**:
- Quick architecture diagrams
- GitHub documentation
- Blog posts and articles
- Flowcharts and processes
- Simple to moderate complexity
- When version control matters

**Example**: Monolithic vs Microservices architecture, API request flows, database schemas, auth flows

---

### PlantUML Diagrams
**Location**: `skills/diagram-plantuml/SKILL.md`
**Purpose**: Generate professional UML and architecture diagrams with full UML notation

**Diagram Types**:
1. **Class Diagram** - OOP design, detailed classes
2. **Sequence Diagram** - Complex interactions, advanced features
3. **Use Case** - User stories, system capabilities
4. **State Machine** - Detailed state transitions
5. **Component** - Architecture and dependencies
6. **Deployment** - Infrastructure layout
7. **Activity** - Process flows and algorithms
8. **Object** - Instance diagrams

**Key Features**:
- Full UML 2.5 standard support
- Professional-grade notation
- Advanced styling and customization
- Complex diagram support
- IDE integration (VS Code, IntelliJ)
- SVG/PNG export
- Enterprise documentation support

**Best For**:
- Complex class hierarchies
- UML documentation
- Enterprise architecture
- Detailed design specifications
- When precision matters
- Professional publications

**Best When**:
- Microservices architecture (component diagram)
- Object-oriented design documentation
- Enterprise systems design
- Detailed API flows
- Academic/formal documentation

---

### Markdown Formatter
**Location**: `skills/markdown-formatter/SKILL.md`
**Purpose**: Format all articles in standard Markdown for universal compatibility

**Key Features**:
- YAML front matter structure and metadata
- Proper heading hierarchy (H1, H2, H3)
- Code block formatting (all languages)
- Image formatting with alt text and captions
- Link syntax and best practices
- Table formatting and structure
- Lists (ordered, unordered, definition)
- Emphasis and special formatting
- Blockquotes and callouts
- Document layout templates
- Advanced features (footnotes, collapsible sections, embeds)
- Conversion from Google Docs, Word, Notion
- Consistency style guide
- Export and compatibility

**Covers**:
- Markdown basics and best practices
- All code languages (Java, Python, JavaScript, SQL, Bash, YAML)
- Image and media handling
- SEO-friendly formatting
- Accessibility (alt text, semantic HTML)
- Git-friendly version control
- Multi-format export (HTML, PDF, EPUB)

---

### SEO Optimizer
**Location**: `skills/seo-optimizer/SKILL.md`
**Purpose**: Improve long-term content discovery through search

**Key Features**:
- Keyword research methodology
- Search intent analysis
- Article structure optimization
- Header and hierarchy optimization
- Keyword placement strategies
- Internal linking strategy
- Technical SEO (page speed, mobile, Core Web Vitals)
- Schema markup and structured data
- Topic cluster strategy
- Backlink building
- Platform-specific SEO (Medium, Dev.to, LinkedIn, Substack, DZone)
- Monitoring and iteration process

**Covers**:
- Keyword research from Ahrefs, SEMrush, Google Trends
- On-page SEO optimization
- Technical SEO fundamentals
- Building topical authority
- Long-term discoverability strategies

---

### Code Examples Generator
**Location**: `skills/code-examples-generator/SKILL.md`
**Purpose**: Generate production-ready code examples for all platforms

**Key Features**:
- Code quality standards and guidelines
- Language-specific patterns (Java, Python, JavaScript/TypeScript)
- Complete vs. snippet examples
- Before/after comparisons
- Step-by-step implementations
- Real-world examples
- Runnable project structures
- Testing examples
- Common patterns (exception handling, async, concurrency)
- Platform-specific code formatting

**Covers**:
- Java code with Spring Boot examples
- Python code with FastAPI examples
- TypeScript/JavaScript with Express examples
- Error handling patterns
- Testing code examples
- Async/concurrent programming examples
- Readability and best practices

---

## How Skills Work Together

### Example 1: Java Article for Dev.to
1. **java-content** - Provides Java expertise and code examples
2. **devto-formatter** - Formats for community-focused platform
3. **code-examples-generator** - Creates production-ready Java code
4. **seo-optimizer** - Optimizes keywords for discoverability

### Example 2: Building a Python Substack Newsletter
1. **python-content** - Provides Python topics and expertise
2. **substack-newsletter** - Structures for weekly email
3. **code-examples-generator** - Creates runnable examples
4. **seo-optimizer** - Ensures long-term searchability

### Example 3: Enterprise Java Article for JavaPro
1. **java-content** - Detailed Java patterns
2. **javapro-magazine** - Professional publication standards
3. **code-examples-generator** - Production-grade code
4. **seo-optimizer** - Research and validation

---

## Quick Reference: Choosing Skills

### By Platform
- **LinkedIn**: linkedin-pulse-formatter
- **Medium**: medium-optimizer
- **Dev.to**: devto-formatter
- **Substack**: substack-newsletter
- **DZone**: dzone-article
- **JavaPro**: javapro-magazine
- **Personal/Company Blog**: sr-tech-blog
- **All platforms**: markdown-formatter, seo-optimizer, code-examples-generator

### By Language
- **Java**: java-content, javapro-magazine or dzone-article (best combination)
- **Python**: python-content, devto-formatter, substack-newsletter, or sr-tech-blog
- **JavaScript**: javascript-content, medium-optimizer, devto-formatter, or sr-tech-blog

### By Content Type
- **Tutorial**: code-examples-generator + (devto-formatter, medium-optimizer, or sr-tech-blog)
- **Opinion/Insight**: linkedin-pulse-formatter or substack-newsletter
- **Deep-dive**: medium-optimizer + (language-content skill)
- **Enterprise Pattern**: javapro-magazine or dzone-article + java-content
- **Newsletter**: substack-newsletter + (language-content skill)
- **Blog Archive**: sr-tech-blog + markdown-formatter
- **Production Pattern**: dzone-article + java-content or python-content

### By Workflow
- **Quick article** (1-2 hours): devto-formatter + code-examples-generator
- **Medium depth** (2-3 hours): medium-optimizer or dzone-article + seo-optimizer
- **Long-form** (4+ hours): sr-tech-blog + markdown-formatter + seo-optimizer
- **Multi-platform** (3-4 hours): Write once, adapt with different formatters
- **Newsletter series**: substack-newsletter + language-content skill + markdown-formatter

---

## Skill Maturity & Maintenance

All skills are:
- ✅ Production-ready
- ✅ Tested with real platforms
- ✅ Include real-world examples
- ✅ Aligned with platform best practices
- ✅ Updated for current frameworks/versions
- ✅ Comprehensive and actionable

---

## Getting Started

1. **Start with the Agent**: Read `agents/technical-writer/AGENT.md` to understand the system
2. **Pick a Platform**: Choose where you want to publish first
3. **Pick a Language**: Focus on Java, Python, or JavaScript
4. **Read Relevant Skills**: Understand platform and language guidance
5. **Write Your First Article**: Apply the patterns and best practices
6. **Iterate**: Use the feedback and SEO metrics to improve future articles

---

## Navigation

- **Main README**: Start here for overview and quick start
- **Agent Profile**: `agents/technical-writer/AGENT.md`
- **All Skills**: Listed above with descriptions
- **CLAUDE.md**: High-level repository guidance
- **This File**: Complete skills index and reference
