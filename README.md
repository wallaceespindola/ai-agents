# AI Agents & Skills for Technical Writers

This repository contains a comprehensive system of AI agents and reusable skills for creating high-quality technical content across multiple platforms.

## What's Included

### Main Agent
- **Technical Writer Agent** (`agents/technical-writer/`): Senior technical software writer specialized in Java, Python, and JavaScript, capable of creating content for multiple platforms

### Language-Specific Content Skills
- **Java Content** (`skills/java-content/`): Java best practices, Spring Boot, design patterns, concurrency, enterprise architecture
- **Python Content** (`skills/python-content/`): Modern Python features, async programming, web frameworks, data science, best practices
- **JavaScript Content** (`skills/javascript-content/`): TypeScript, React, Node.js, async patterns, performance, modern tooling

### Platform-Specific Formatting Skills
- **LinkedIn Pulse Formatter** (`skills/linkedin-pulse-formatter/`): Professional engagement, 800-1500 word articles, networking focus
- **Medium Optimizer** (`skills/medium-optimizer/`): Deep-dive technical articles, 2000-7000 words, authority building
- **Dev.to Formatter** (`skills/devto-formatter/`): Community-focused, practical tutorials, 1000-3000 words, quick wins
- **Substack Newsletter** (`skills/substack-newsletter/`): Weekly/monthly newsletters, subscriber growth, paid tier strategy
- **DZone Article Writer** (`skills/dzone-article/`): Curated technical platform, 1500-4000 words, enterprise audience, editorial review
- **JavaPro Magazine** (`skills/javapro-magazine/`): Enterprise Java, 3000-6000 words, publication-grade, peer review
- **Sr Tech Blog Writer** (`skills/sr-tech-blog/`): Personal/company blog, 2000-10,000+ words, full creative control, monetization
- **InfoQ Article Writer** (`skills/infoq-article/`): Research-informed editorial articles, 2000-3000 words, five key takeaways, editorial review, 4-week exclusive

### Coder Skills (Generate Production Projects)
- **Java Coder** (`skills/java-coder/`): Generate Maven/Spring Boot projects with source code, tests, and documentation linked to articles
- **Python Coder** (`skills/python-coder/`): Generate FastAPI/Django projects with source code, tests, and documentation linked to articles
- **JavaScript Coder** (`skills/javascript-coder/`): Generate React/Node.js projects with TypeScript, tests, and documentation linked to articles

### Supporting/Cross-Platform Skills
- **Architecture & Design** (`skills/architecture-design/`): Software architecture patterns, system design, design principles (SOLID, DDD, CQRS)
- **Markdown Formatter** (`skills/markdown-formatter/`): Universal Markdown formatting with metadata, code blocks, images, for archiving and version control
- **Mermaid Diagrams** (`skills/diagram-mermaid/`): Flowcharts, architecture, sequence diagrams using diagram-as-code (version control friendly)
- **PlantUML Diagrams** (`skills/diagram-plantuml/`): UML class, component, deployment diagrams with full UML notation
- **Blog Image Generator** (`skills/image-generator-blog/`): Featured images, in-article visuals, design tools, optimization
- **SEO Optimizer** (`skills/seo-optimizer/`): Keyword research, content optimization, discovery, ranking strategies
- **Code Examples Generator** (`skills/code-examples-generator/`): Production-ready code, multiple languages, testing examples

## Quick Start

### Using with Claude Code

1. Clone or download this repository
2. Open in Claude Code (`claude-code` or via web at https://code.claude.com)
3. When writing technical content, Claude will automatically discover and use relevant skills

### Using with Claude API

Skills can be configured in your Claude API requests. See `docs/API_INTEGRATION.md` for implementation details.

### Using with Anthropic Agent SDK

Skills are discoverable through the SDK's skill system. Configure in your agent YAML:

```yaml
allowed_tools:
  - "Skill"

skills_directory: ".claude/skills/"
```

## Workflow Examples

### Example 1: Writing a Technical Article

1. **Choose your topic and platform** (e.g., "React performance optimization for Dev.to")

2. **Ask Claude to help write the article**:
   ```
   Help me write a Dev.to article about React performance optimization.
   Include practical code examples and focus on quick wins for junior developers.
   ```

3. **Claude will automatically**:
   - Use `javascript-content` skill for React patterns
   - Use `devto-formatter` skill for proper structure and tone
   - Use `seo-optimizer` skill for keyword research and optimization
   - Use `code-examples-generator` for runnable examples

4. **Review and publish** the optimized article

### Example 2: Creating a Multi-Platform Content Series

1. **Write the core article** (e.g., "Understanding Async/Await in Python")

2. **Adapt for multiple platforms**:
   ```
   I've written a deep technical article on Python async/await.
   Please adapt it for:
   - LinkedIn Pulse (professional focus, 1000 words)
   - Medium (technical deep-dive, 3000 words)
   - Dev.to (practical tutorial, 2000 words)
   - Substack (newsletter format, weekly email)
   Each should have unique perspectives and audiences.
   ```

3. **Claude will**:
   - Use platform-specific skills to adapt tone, length, structure
   - Optimize SEO for each platform
   - Ensure appropriate code examples
   - Generate platform-specific calls-to-action

### Example 3: Building a Substack Newsletter Strategy

1. **Plan your newsletter**:
   ```
   I want to start a technical newsletter on Java architecture and design patterns.
   I'll publish weekly. Help me with:
   - 5 article ideas for the first month
   - Newsletter structure and tone
   - Growth strategy
   - Free vs. paid tier content
   ```

2. **Claude will use**:
   - `java-content` for topic ideation
   - `substack-newsletter` for structure and strategy
   - `seo-optimizer` for newsletter discoverability
   - `code-examples-generator` for code samples

3. **Get actionable content plan** ready to execute

### Example 4: Publishing to DZone and Building a Blog Archive

1. **Write and format your technical content**:
   ```
   I've written a deep article on microservices patterns.
   Help me:
   - Format for DZone publication (curated platform)
   - Create a Markdown version for my blog archive
   - Optimize for SEO search discovery
   - Include all code examples properly formatted
   ```

2. **Claude will**:
   - Use `dzone-article` skill for DZone submission requirements
   - Use `markdown-formatter` to create universal Markdown version
   - Use `seo-optimizer` for search rankings
   - Use `code-examples-generator` for all code blocks

3. **Get**:
   - DZone-ready article with editorial requirements
   - Markdown file for version control and archiving
   - SEO-optimized metadata and keywords

### Example 5: Building Your Personal Tech Blog

1. **Plan your blog**:
   ```
   I want to start a technical blog on Python and JavaScript.
   Help me with:
   - Blog platform recommendation (Ghost, Hugo, Substack?)
   - Content strategy (5-10 pillar topics)
   - Monetization options
   - Growth and SEO strategy
   - First 5 articles to publish
   ```

2. **Claude will use**:
   - `sr-tech-blog` for blog strategy and long-form content
   - Language-content skills (python-content, javascript-content)
   - `markdown-formatter` for universal content format
   - `seo-optimizer` for search authority building
   - `code-examples-generator` for production examples

3. **Get**:
   - Complete blog strategy and architecture
   - Content calendar for first month
   - Articles ready to publish (in Markdown)
   - SEO and growth roadmap

## Skill Architecture

Each skill follows this structure:

```
skill-name/
├── SKILL.md          # Main skill file with instructions
├── examples/         # (Optional) Example implementations
├── templates/        # (Optional) Templates for the skill
└── resources/        # (Optional) Reference materials
```

### SKILL.md Structure

Every skill includes:
- **YAML frontmatter**: `name` and `description`
- **When to use this skill**: Decision criteria
- **Quick start**: Immediate guidance
- **Core concepts**: Deep knowledge
- **Examples**: Real-world demonstrations
- **Best practices**: Do's and don'ts
- **Checklists**: Quality assurance

## Key Features

### 1. Progressive Disclosure
Skills load on-demand, not all at once. Claude only reads the guidance needed for each specific task.

### 2. Platform-Specific Optimization
Each platform has different audiences, constraints, and best practices. Skills capture these differences.

### 3. Language Specialization
Deep expertise in Java, Python, and JavaScript with modern frameworks and best practices.

### 4. Humanized Voice
All content follows strict humanization guidelines to ensure articles sound genuinely human-written, not AI-generated. This includes conversational tone, natural language patterns, no Oxford commas, and accessibility for 8th-10th grade reading level. See **HUMANIZATION_GUIDE.md** for complete standards.

### 5. SEO Integration
Content is optimized for long-term discoverability while serving immediate audience needs.

### 6. Quality Assurance
Each skill includes checklists and validation steps to ensure publication-ready quality.

## Supported Topics

### Java
- Core language features (Java 17+)
- Spring Boot and Spring ecosystem
- Concurrent and parallel programming
- Design patterns and architecture
- Performance optimization and GC tuning
- Enterprise patterns (microservices, CQRS, event sourcing)
- Testing and quality assurance

### Python
- Modern Python features (3.9+)
- Async/await and asyncio
- Web frameworks (FastAPI, Django, Flask)
- Data science and machine learning
- Type hints and type safety
- Performance optimization
- Testing and best practices

### JavaScript/TypeScript
- Modern JavaScript and ES2020+
- TypeScript advanced features
- React patterns and hooks
- Node.js backend patterns
- Web performance and Core Web Vitals
- Testing and quality
- Tooling and build systems

## Supported Platforms

| Platform | Best For | Length | Frequency | Audience |
|----------|----------|--------|-----------|----------|
| **LinkedIn Pulse** | Professional growth | 800-1500 | 1-2/week | Career-focused devs |
| **Medium** | Deep technical | 2000-7000 | 1-2/month | Learning-oriented |
| **Dev.to** | Quick wins | 1000-3000 | 1-2/week | Community-driven |
| **Substack** | Building audience | 1500-3000 | 1/week | Subscribers, newsletter |
| **DZone** | Production patterns | 1500-4000 | Flexible | Enterprise devs |
| **JavaPro** | Enterprise Java | 3000-6000 | 1-2/month | Senior architects |
| **Personal Blog** | Complete control | 2000-10k+ | Your pace | Your audience |

**Format Support**: All platforms support **Markdown export** for archiving and version control

## Content Strategy Framework

### Topic Selection
1. **Audience pain points**: What problems does your audience face?
2. **Platform fit**: Which platform best reaches that audience?
3. **Language focus**: Java, Python, or JavaScript?
4. **Content type**: Tutorial, opinion, case study, pattern?
5. **SEO value**: Long-term discoverability potential?

### Writing Process
1. **Research**: Gather examples, frameworks, current best practices
2. **Outline**: Structure for target platform
3. **Draft**: Write with audience and platform in mind
4. **Optimize**: Apply platform-specific formatting and SEO
5. **Validate**: Code examples tested, facts verified
6. **Publish**: Schedule and promote strategically

### Growth Strategy
- **Quality first**: One great article > five mediocre ones
- **Consistency**: Regular publishing builds habit and algorithm favor
- **Specialization**: Deep expertise in 2-3 topics beats shallow coverage
- **Cross-promotion**: Adapt one article for multiple platforms
- **Community**: Engage with readers, respond to comments
- **Authority**: Build reputation through consistent, valuable content

## Usage Tips

### For Maximum Effectiveness

1. **Be specific in requests**: "Help me write a Medium article about Spring Boot async patterns" vs. "Write about Spring Boot"

2. **Mention your audience**: "This is for junior developers just starting with async" or "This is for architects designing microservices"

3. **Include constraints**: "This needs to be under 2000 words" or "We need 5 code examples"

4. **Leverage multiple skills**: Skills work together. Using Java content + Dev.to formatter + SEO optimizer produces optimized community-focused Java content

5. **Iterate on feedback**: Get Claude's suggestions, refine, repeat

### Platform-Specific Tips

**LinkedIn**: Focus on career impact, lessons learned, insights from experience

**Medium**: Go deep, include architecture diagrams, make it comprehensive and authoritative

**Dev.to**: Make it practical, include quick wins, be conversational and community-focused

**Substack**: Build relationships, be personal, create habit of regular reading

**JavaPro**: Enterprise perspective, production concerns, architectural depth

## Examples in This Repository

- `agents/technical-writer/AGENT.md`: Complete agent profile and capabilities
- `skills/java-content/SKILL.md`: Detailed Java content guidance
- `skills/medium-optimizer/SKILL.md`: Medium platform best practices
- `skills/seo-optimizer/SKILL.md`: SEO optimization strategies

## Getting Help

Each skill includes:
- ✅ Clear decision criteria (when to use)
- ✅ Quick start guides
- ✅ Real examples
- ✅ Common mistakes to avoid
- ✅ Quality checklists

Read the relevant skill's SKILL.md file for comprehensive guidance on any topic.

## Contributing

To extend this system with new skills:

1. Create a new directory in `skills/skill-name/`
2. Write SKILL.md with the required frontmatter and structure
3. Include practical examples
4. Add quality checklists
5. Test with Claude Code

See the existing skills for patterns and examples.

## Key Principles

- **Specialization over generalization**: Deep expertise in specific areas
- **Platform awareness**: Different platforms need different approaches
- **Audience-first**: Always consider who is reading
- **Quality over quantity**: One great article beats three mediocre ones
- **Progressive disclosure**: Load information only when needed
- **Community value**: Write to help others, not just to promote yourself
- **Continuous improvement**: Iterate based on engagement data

## Metrics That Matter

### Content Performance
- **Engagement**: Comments, shares, claps/reactions
- **Reach**: Views, impressions, followers gained
- **Quality**: Professional opportunities, speaking invitations
- **Longevity**: Long-term traffic from search, archives

### Newsletter Success
- **Growth**: Subscriber growth rate
- **Engagement**: Open rates, click rates, reply rates
- **Retention**: Churn rate, paying subscribers
- **Community**: Active discussions, reader replies

### Career Impact
- **Authority**: Speaking invitations, consulting offers
- **Network**: Connection requests from relevant people
- **Opportunities**: Job offers, book deals, partnerships
- **Credibility**: Recognition as expert in your niche

## Humanization Standards

All content from this system is written with **humanization principles** to ensure articles sound genuinely written by a knowledgeable human, not generated by AI.

### What This Means

- **Conversational tone**: Write like you're explaining to a smart friend, not lecturing from a podium
- **Natural language**: Use contractions ("you're," "I've"), first/second person, informal phrasing
- **Accessible language**: 8th-10th grade reading level that doesn't sacrifice depth
- **Human patterns**: One-sentence paragraphs, questions, bold emphasis for attention
- **No AI signals**: No "in today's digital landscape," no Oxford commas, no generic corporate phrases

### Key Principles

- Clear reasoning before conclusions
- Real-world examples and everyday analogies
- Positive, actionable language
- Friendly tone appropriate to each platform
- Readers feel like they're learning from a respected colleague

**See HUMANIZATION_GUIDE.md** for complete standards, examples by content type, and practical checklists.

## Next Steps

1. **Choose a platform** where you want to publish:
   - Quick wins: Dev.to or LinkedIn
   - Deep dives: Medium or your blog
   - Enterprise patterns: DZone or JavaPro
   - Long-term: Personal blog or Substack

2. **Pick a language** (Java, Python, or JavaScript)

3. **Identify a topic** you know well and your audience cares about

4. **Use the relevant skills** to structure and optimize:
   - Start with language-specific skill (java-content, python-content, javascript-content)
   - Use platform-specific formatter
   - Apply seo-optimizer for discovery
   - Use code-examples-generator for production code
   - Export as markdown-formatter for universal format

5. **Write and publish** your first article

6. **Export as Markdown** for archiving and version control

7. **Track metrics** (views, engagement, conversion) to understand what works

8. **Iterate** based on feedback and data

**Pro tip**: Start with one platform to build momentum, then expand to others. Adapt your best article for 2-3 different platforms using the formatter skills to maximize reach.

## Resources

- Claude Platform: https://platform.claude.com
- Claude Code: https://code.claude.com
- Anthropic Documentation: https://docs.anthropic.com

## License

MIT License - See LICENSE file in repository root

## Support

For questions or issues:
1. Check the relevant skill's SKILL.md file
2. Read through examples in the skill
3. Review the agent description in AGENT.md
4. Open an issue or discussion in the repository

---

**Ready to become a published technical author?** Start with the platform that matches your audience, pick a skill you know deeply, and use these tools to write your first article. The skills and agent are here to guide you every step of the way.
