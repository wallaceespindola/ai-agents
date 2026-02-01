---
name: devto-formatter
description: Format technical articles for Dev.to platform, optimizing for community engagement, practical value, and discoverability. Use when preparing articles for Dev.to publication, maximizing reach within the developer community with quick wins and code tutorials.
---

# Dev.to Formatting Guide

## When to Use This Skill

Use this skill when:
- Formatting technical articles for Dev.to publication
- Creating quick-win tutorials and code snippets
- Optimizing for Dev.to's community algorithm
- Maximizing DEV points and reader engagement
- Setting up publications and series
- Creating beginner-friendly technical content

## Dev.to Article Specifications

### Length & Structure
- **Optimal length**: 1,000-3,000 words (shorter than Medium)
- **Best time to read**: 3-10 minutes
- **Headline**: 50-70 characters, action-oriented
- **Hook**: First paragraph must grab attention
- **Sections**: 3-6 sections with H2 headers
- **Code ratio**: 30-40% code, 60-70% explanation

### Headline Strategy

✅ **Good Dev.to headlines:**
- "How to Use Java Records to Reduce Boilerplate by 50%"
- "5 JavaScript Mistakes That Slow Down Your App"
- "Python Async/Await: The Complete Beginner's Guide"
- "Docker for Developers: A Practical Step-by-Step Tutorial"
- "My Top 10 CSS Tips I Learned This Year"

❌ **Avoid:**
- Generic: "Learning JavaScript"
- Vague: "Cool Development Things"
- Clickbait: "You Won't Believe This Trick..."

**Headline formula:**
- **[Action verb] + [Technology] + [Benefit]**
- "Build," "Learn," "Master," "Fix," "Optimize," "Debug"
- Technology: Language, framework, library, tool
- Benefit: "Faster," "Cleaner Code," "Reduce Errors," "Save Time"

### Article Structure for Dev.to

```
HEADLINE
SUMMARY (preview text)

[Cover image - 1000x500px]

Introduction (100-200 words)
- Greeting to community
- Why this matters
- What you'll learn
- Difficulty level

Section 1: The Problem (150-300 words)
- Real-world scenario
- What developers struggle with
- Why it matters
- Set up for solution

Section 2: The Solution (400-600 words)
- Explanation of approach
- Why it works
- Key concepts
- Implementation steps

Section 3: Code Example (300-500 words)
- Complete, runnable code
- Well-commented
- Explanation after code
- Show output

Section 4: Tips & Tricks (200-400 words)
- Additional insights
- Common mistakes
- Performance notes
- Best practices

Conclusion (100-200 words)
- Recap key points
- Encouragement
- Next steps or follow-up content

Call-to-Action
- Discussion question
- Tag request
- Share feedback
- Link to next article in series
```

### Tone & Voice for Dev.to

- **Friendly and approachable**: Like talking to a colleague
- **Practical over theoretical**: Focus on "how to do it"
- **Humble and learning-oriented**: Share what you learned
- **Encouraging**: Support beginners and less experienced devs
- **Conversational**: Use "I," "we," "you"
- **No gatekeeping**: Welcome all skill levels

**Voice examples:**
- ✅ "I struggled with this for months until I discovered..."
- ✅ "Here's a trick that saved me hours of debugging"
- ✅ "This confused me at first, but now I understand..."
- ❌ "Only experienced developers will understand this"
- ❌ "If you don't know this, you're not a real developer"

### Code Examples on Dev.to

#### Code Block Formatting
- Use markdown code fences with language tags
- 80 character line width for readability
- Real, runnable code (not pseudo-code)
- Include all imports/dependencies

```python
# Good: Clear, concise, runnable
def fetch_user_data(user_id: int) -> dict:
    """Fetch user from API."""
    response = requests.get(f"api/users/{user_id}")
    return response.json()

# Usage
user = fetch_user_data(42)
print(user['name'])
```

#### Code Guidelines
- **Keep it short**: 20-40 lines per block max
- **Real code**: Code readers can copy and use
- **Comment key parts**: Explain non-obvious logic
- **Include output**: Show what the code produces
- **Multiple examples**: Show different approaches

### Dev.to Tags (Essential!)

#### Required Tags (4 max)
- **Language/Framework**: `javascript`, `react`, `java`, `python`, `springboot`
- **Topic**: `tutorial`, `webdev`, `coding`, `bestpractices`
- **Level**: `beginners`, `intermediate`, `advanced`
- **Additional**: `productivity`, `devops`, `security`

**Tag strategy:**
- First tag should be most searchable (language)
- Use "beginners" if accessible to new developers
- Max 4 tags, be specific

#### Avoiding "Off-Topic" Filter
- Tags must be relevant to content
- Avoid spammy tags unrelated to article
- Dev.to will filter out low-quality tag combos
- Read tag guidelines on platform

### Dev.to Series Feature

- **Group related articles**: Use series feature
- **Cross-link content**: Readers see related posts
- **Serialized learning**: "Building a REST API: Part 1, 2, 3"
- **Increase engagement**: Reader follows entire series

Example series:
1. "Python Web Development: Part 1 - Hello Flask"
2. "Python Web Development: Part 2 - Database Integration"
3. "Python Web Development: Part 3 - Authentication"

### Media & Images

#### Cover Image
- **Size**: 1000x500px (1:2 aspect ratio)
- **Quality**: Clear, professional
- **Content**: Related to topic
- **Source**: Unsplash, Pexels, own images
- **Text**: Optional overlay text (avoid if possible)

#### In-Article Images
- **Frequency**: 1-2 images per 1000 words
- **Types**: Diagrams, screenshots, flowcharts
- **Quality**: Sharp and legible
- **Alt text**: Essential for accessibility

### Engagement Features

#### DEV Points & Reactions
- **Dev.to has points system**: Likes/hearts earn points
- **Bookmarks**: Save for later (good signal)
- **Unicorns**: Special reaction for top-quality content
- **Comments**: Active comment section shows quality

#### Discussion Questions
- **End with a question**: "What's your favorite debugging tool?"
- **Make it open-ended**: Not just yes/no
- **Invite experiences**: "Have you encountered this?"
- **Encourage replies**: "Let me know in the comments"

#### Community Engagement
- **Respond to comments**: Thank people, answer questions
- **Cross-promote**: Share in Dev.to discussion channels
- **Link appropriately**: Connect to related articles
- **Mention other authors**: Tag relevant developers

### Front Matter (Dev.to Metadata)

Dev.to uses front matter for publishing:

```yaml
---
title: "How to Use Java Records to Reduce Boilerplate"
description: "Learn how Java Records simplify data classes with example code and best practices"
tags: java, tutorial, oop, beginners
cover_image: "https://example.com/cover.jpg"
published: true
---
```

### Content Guidelines

#### Do's ✅
- ✅ Share what you learned
- ✅ Include working code examples
- ✅ Be specific and actionable
- ✅ Help others learn
- ✅ Acknowledge mistakes
- ✅ Give credit to others
- ✅ Use clear formatting

#### Don'ts ❌
- ❌ Plagiarize or copy content
- ❌ Spam or self-promotion only
- ❌ Discuss politics/religion
- ❌ Use profanity excessively
- ❌ Share credentials or secrets
- ❌ Engage in harassment
- ❌ AI-generated content (disallowed)

### Publishing Strategy

#### Optimal Publishing Times
- **Best days**: Tuesday-Thursday
- **Best times**: 9:00-11:00 AM or 2:00-3:00 PM (US ET)
- **Frequency**: 1-2 articles per week (consistency important)

#### Algorithm Signals (What Dev.to promotes)
1. **Engagement**: Comments and reactions
2. **Quality**: Clear writing, good examples
3. **Freshness**: New content promoted
4. **Completeness**: Finished, well-edited articles
5. **Community**: Participating in discussions

### Dev.to-Specific Features

#### Discussion Threads
- Start discussions in the discussion section
- Link to your articles
- Get feedback before publishing
- Community helps refine ideas

#### Podcasts & Videos
- Embed YouTube videos in articles
- Link to podcasts
- Supports multimedia content
- Increases engagement

#### Canonical URLs
- Use if syndicating content
- Specify original source
- Dev.to allows republication with proper attribution
- Good for expanding reach

### Examples of High-Performing Dev.to Articles

#### Example 1: Quick Win
**Title**: "3 JavaScript Tricks That Saved Me Hours"

Introduction:
"Last week I discovered three simple JavaScript techniques I wish I'd known earlier. None require frameworks or complex setups—just vanilla JS that makes code cleaner and faster."

Structure:
1. **Trick 1**: Optional chaining `obj?.property`
   - Before/after code
   - Real example of where this helps
   - Performance benefits

2. **Trick 2**: Nullish coalescing `value ?? default`
   - Why this is better than `||`
   - Code example
   - When to use

3. **Trick 3**: Destructuring assignment
   - Reduces boilerplate
   - Makes code readable
   - Real-world usage

Conclusion: "These three patterns have already made my code cleaner. What techniques have helped you?"

#### Example 2: Step-by-Step Tutorial
**Title**: "Building Your First REST API with Python Flask: Complete Guide"

Introduction: "If you've wanted to build a web API but weren't sure where to start, this guide is for you. We'll build a complete, working API in under 100 lines of code."

Sections:
1. What you'll build
2. Setup (virtual environment, dependencies)
3. Create your first route
4. Add data handling
5. Test your API
6. Deploy to production

Each section: Code → Explanation → Next step

#### Example 3: Beginner-Friendly Pattern
**Title**: "Understanding Python Type Hints: A Beginner's Guide"

Introduction: "Type hints confused me when I first saw them. But once I understood they're optional annotations that help catch bugs early, everything clicked."

Structure:
- **What are type hints?** (definitions with simple examples)
- **Why use them?** (concrete benefits)
- **Basic syntax** (function examples)
- **Complex types** (lists, dicts, optional)
- **IDE support** (benefits you get)
- **Common mistakes** (pitfalls to avoid)

### Dev.to Community Norms

- **Be helpful**: Answer questions genuinely
- **Be respectful**: Support all skill levels
- **Give credit**: Link to sources and inspiration
- **Engage genuinely**: Respond to comments
- **No spam**: Articles should provide value
- **Encourage others**: Uplift developers sharing knowledge

### Publishing Checklist

- [ ] Title is action-oriented and specific
- [ ] Cover image is high quality (1000x500px)
- [ ] Introduction hooks reader immediately
- [ ] Article is 1,000-3,000 words
- [ ] Code examples are complete and runnable
- [ ] 3-4 relevant tags applied
- [ ] Grammar and spelling checked
- [ ] Formatting is clean (headers, code blocks, line breaks)
- [ ] Includes 1-2 discussion questions
- [ ] Technical accuracy verified
- [ ] No plagiarism or copied content
- [ ] Ready to engage with comments
