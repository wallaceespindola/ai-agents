---
description: Configuration system for managing personal data, author information, and social links in a secure, version-controlled way
---

# Configuration & Personal Data Management

This document explains how to configure the system with your personal information while keeping sensitive data secure and out of version control.

## Overview

The system uses environment variables to manage personal data:

- **Author information** (name, email, bio)
- **Social media links** (GitHub, LinkedIn, Twitter, etc.)
- **Profile URLs** (Linktree, Solo.to, Gravatar)
- **Website/blog information**
- **Platform usernames and IDs**
- **Publishing preferences**

This approach keeps your `.env` file local (not in git) while allowing all skills and agents to use your personalized information.

## Quick Setup

### Step 1: Create Your `.env` File

```bash
# Copy the example file
cp .env.example .env

# Edit .env with your information
nano .env
# or
code .env
# or open in your favorite editor
```

### Step 2: Fill in Your Information

Open `.env` and update all the variables with your actual data.

### Step 3: That's It!

The skills automatically read from environment variables. Nothing to commit, data is secure.

## Security Best Practices

### ✅ DO

- Keep `.env` file locally only
- `.env` is in `.gitignore` (don't commit it)
- Use `.env.example` as a template for team members
- Rotate API keys periodically
- Use different API keys for different services
- Set environment variables in CI/CD systems instead of .env files
- Review .gitignore to ensure .env is excluded

### ❌ DON'T

- Commit `.env` file to git
- Share `.env` file publicly
- Put real secrets in `.env.example`
- Use the same key for multiple services
- Hardcode personal data in skill files
- Log environment variables to console

## Configuration Variables

### Author Information

```env
AUTHOR_NAME=Wallace Espindola
AUTHOR_EMAIL=your.email@example.com
AUTHOR_BIO=Your professional bio here
AUTHOR_TITLE=Senior Software Engineer
AUTHOR_COMPANY=Your Company Name
AUTHOR_AVATAR_URL=https://gravatar.com/wallacese
AUTHOR_LOCATION=City, Country
```

Used in:
- Article headers and author sections
- Author bios in README files
- Newsletter signatures
- Social media templates
- GitHub profile links

### Social Media Links

```env
# Link Aggregators
LINKTREE_URL=https://linktr.ee/wallace.espindola
SOLO_URL=https://solo.to/wallace.espindola

# Individual Profiles
GITHUB_URL=https://github.com/wallaceespindola
LINKEDIN_URL=https://www.linkedin.com/in/wallaceespindola/
TWITTER_URL=https://x.com/wsespindola
INSTAGRAM_URL=https://instagram.com/your_handle
MASTODON_URL=https://mastodon.social/@your_handle
YOUTUBE_URL=https://youtube.com/@your_channel
DEVTO_URL=https://dev.to/your_handle
MEDIUM_URL=https://medium.com/@your_handle
```

Used in:
- Article metadata and footers
- README author sections
- Article templates
- Social sharing links
- Newsletter sign-off

### Website & Blog Information

```env
BLOG_URL=https://blog.example.com
BLOG_NAME=Wallace's Tech Blog
BLOG_DESCRIPTION=Deep dives into Java, Python, and JavaScript
GITHUB_REPO_URL=https://github.com/wallaceespindola/articles-and-code
GITHUB_REPO_NAME=articles-and-code
SUBSTACK_URL=https://wallaceespindola.substack.com
NEWSLETTER_EMAIL=subscribe@example.com
```

Used in:
- Article markdown templates
- README files
- Links in articles
- Newsletter headers
- Cross-promotion sections

### Platform Usernames

```env
DEVTO_HANDLE=your_devto_handle
MEDIUM_HANDLE=@your_medium_handle
DZONE_AUTHOR_ID=your_dzone_id
HASHNODE_HANDLE=your_hashnode_handle
```

Used in:
- Publication submissions
- Author profiles
- Platform-specific links
- Analytics and tracking

### Article & Content Settings

```env
DEFAULT_LANGUAGE=java
TIMEZONE=America/New_York
ARTICLES_ROOT_PATH=./docs/articles
PROJECTS_ROOT_PATH=./projects
FEATURED_IMAGE_WIDTH=1024
FEATURED_IMAGE_HEIGHT=768
FEATURED_IMAGE_MAX_SIZE_MB=3
```

Used in:
- Code generation defaults
- Directory structure
- Image specifications
- Timezone for scheduling

### Publishing Preferences

```env
ACTIVE_PLATFORMS=linkedin,medium,devto,substack,dzone
DEFAULT_ARTICLE_LENGTH=medium
INCLUDE_CODE_EXAMPLES=true
INCLUDE_DIAGRAMS=true
INCLUDE_IMAGES=true
```

Used in:
- Article generation
- Publishing templates
- Content optimization

### SEO Settings

```env
PRIMARY_KEYWORDS=Java,Python,JavaScript,Architecture
TARGET_AUDIENCE=Senior engineers and architects
SEO_REGIONS=United States,Europe
```

Used in:
- Keyword research
- Article optimization
- Topic clustering

## Using Environment Variables in Skills

### In Generated Code (README.md templates)

Skills generate files that reference your information:

```markdown
## About the Author

[${AUTHOR_NAME}](${GITHUB_URL}) is a ${AUTHOR_TITLE} at ${AUTHOR_COMPANY}.
For more information, visit [${BLOG_URL}](${BLOG_URL}).

Follow on [LinkedIn](${LINKEDIN_URL}) | [Twitter](${TWITTER_URL}) | [GitHub](${GITHUB_URL})
```

When the skill generates this, it replaces `${VARIABLE_NAME}` with actual values from your `.env`.

### In Article Templates

Articles automatically include:

```yaml
---
title: Article Title
author: ${AUTHOR_NAME}
author_email: ${AUTHOR_EMAIL}
author_bio: ${AUTHOR_BIO}
social_links:
  github: ${GITHUB_URL}
  linkedin: ${LINKEDIN_URL}
  twitter: ${TWITTER_URL}
---
```

### In Code Project Templates

Generated projects reference your info in README:

```markdown
# Project Name

This code example is from the article:
[Article Title](${ARTICLES_ROOT_PATH}/article-name/ARTICLE.md)

## About the Author

${AUTHOR_NAME} - [LinkedIn](${LINKEDIN_URL})
```

## Environment Variable Reference

### Complete List of Available Variables

#### Author & Profile
- `AUTHOR_NAME` - Your full name
- `AUTHOR_EMAIL` - Your email address
- `AUTHOR_BIO` - Your professional biography
- `AUTHOR_TITLE` - Your job title
- `AUTHOR_COMPANY` - Your company/employer
- `AUTHOR_AVATAR_URL` - Link to your profile picture
- `AUTHOR_LOCATION` - City/Country

#### Social Media
- `LINKTREE_URL` - Your Linktree profile
- `SOLO_URL` - Your Solo.to profile
- `GITHUB_URL` - Your GitHub profile
- `GITHUB_USERNAME` - Just the username
- `LINKEDIN_URL` - Your LinkedIn profile
- `LINKEDIN_PROFILE_ID` - Just the profile ID
- `TWITTER_URL` - Your Twitter/X profile
- `TWITTER_HANDLE` - Just the handle
- `INSTAGRAM_URL` - Your Instagram profile
- `MASTODON_URL` - Your Mastodon profile
- `YOUTUBE_URL` - Your YouTube channel
- `DEVTO_URL` - Your Dev.to profile
- `MEDIUM_URL` - Your Medium profile

#### Website & Publishing
- `BLOG_URL` - Your main blog/website
- `BLOG_NAME` - Name of your blog
- `BLOG_DESCRIPTION` - Blog description
- `GITHUB_REPO_URL` - Your articles repository
- `GITHUB_REPO_NAME` - Repository name
- `SUBSTACK_URL` - Your Substack newsletter
- `NEWSLETTER_EMAIL` - Newsletter subscription email

#### Platform IDs
- `DEVTO_HANDLE` - Dev.to username
- `MEDIUM_HANDLE` - Medium username
- `DZONE_AUTHOR_ID` - DZone author ID
- `HASHNODE_HANDLE` - Hashnode username

#### Content Settings
- `DEFAULT_LANGUAGE` - Default code language (java/python/javascript)
- `TIMEZONE` - Your timezone (e.g., America/New_York)
- `ARTICLES_ROOT_PATH` - Where articles are stored
- `PROJECTS_ROOT_PATH` - Where code projects are stored
- `FEATURED_IMAGE_WIDTH` - Image width (default: 1024)
- `FEATURED_IMAGE_HEIGHT` - Image height (default: 768)
- `FEATURED_IMAGE_MAX_SIZE_MB` - Max file size (default: 3)

#### Publishing Preferences
- `ACTIVE_PLATFORMS` - Comma-separated list of platforms
- `DEFAULT_ARTICLE_LENGTH` - short/medium/long/xlarge
- `INCLUDE_CODE_EXAMPLES` - true/false
- `INCLUDE_DIAGRAMS` - true/false
- `INCLUDE_IMAGES` - true/false

#### SEO
- `PRIMARY_KEYWORDS` - Comma-separated keywords
- `TARGET_AUDIENCE` - Your target audience
- `SEO_REGIONS` - Geographic focus areas

## Using in Different Environments

### Local Development

Create `.env` with your personal information:

```bash
cp .env.example .env
# Edit .env with your values
```

Skills read from `.env` automatically.

### CI/CD Pipeline

Set environment variables directly in your CI/CD system (GitHub Actions, GitLab CI, etc.) instead of using `.env`:

**GitHub Actions Example:**

```yaml
env:
  AUTHOR_NAME: Wallace Espindola
  AUTHOR_EMAIL: ${{ secrets.AUTHOR_EMAIL }}
  GITHUB_URL: https://github.com/wallaceespindola
  LINKEDIN_URL: ${{ secrets.LINKEDIN_URL }}
```

**GitLab CI Example:**

```yaml
variables:
  AUTHOR_NAME: "Wallace Espindola"
  AUTHOR_EMAIL: $AUTHOR_EMAIL_SECRET
  GITHUB_URL: https://github.com/wallaceespindola
```

### Team/Open Source Projects

Share `.env.example` (which you see in this repo) but never `.env`:

```bash
# What gets committed to git:
.env.example  # ✓ Commit this (it's a template)

# What does NOT get committed:
.env          # ✗ In .gitignore (never commit)
```

New team members:
1. Clone repo
2. Copy `.env.example` to `.env`
3. Fill in their own (or shared) values

## Accessing Variables in Skills

### In Article Templates

Variables are replaced automatically during article generation:

```markdown
---
author: ${AUTHOR_NAME}
author_email: ${AUTHOR_EMAIL}
---

# Article Title

By [${AUTHOR_NAME}](${GITHUB_URL})

Follow me on [LinkedIn](${LINKEDIN_URL})
```

### In Code Project README

Skills automatically inject variables into generated README files:

```markdown
# Generated from Article

This example supports [the article](${ARTICLES_ROOT_PATH}/article/ARTICLE.md)

## About the Author

[${AUTHOR_NAME}](${LINKEDIN_URL}) specializes in ${DEFAULT_LANGUAGE}
```

### In Shell Scripts

If you create custom automation:

```bash
#!/bin/bash
source .env

echo "Author: $AUTHOR_NAME"
echo "GitHub: $GITHUB_URL"
echo "Blog: $BLOG_URL"
```

### In Python Scripts

```python
import os
from dotenv import load_dotenv

load_dotenv()

author_name = os.getenv('AUTHOR_NAME')
github_url = os.getenv('GITHUB_URL')
blog_url = os.getenv('BLOG_URL')
```

### In JavaScript/Node.js

```javascript
require('dotenv').config();

const authorName = process.env.AUTHOR_NAME;
const githubUrl = process.env.GITHUB_URL;
const blogUrl = process.env.BLOG_URL;
```

### In Java

```java
System.getenv("AUTHOR_NAME");
System.getenv("GITHUB_URL");
System.getenv("BLOG_URL");
```

## Updating Variables

### Change Your Profile Information

Edit `.env` locally:

```bash
# Update the file
nano .env

# Skills will use new values immediately
```

### Change for a Specific Project

You can override variables per project:

```bash
# Copy your master .env to project-specific one
cp .env .env.project1

# Edit project-specific values
nano .env.project1

# Use for that project
source .env.project1
# or set it in your CI/CD
```

## Troubleshooting

### Variables Not Showing Up

**Issue**: Generated articles show `${AUTHOR_NAME}` instead of actual name

**Solution**:
- Ensure `.env` file exists and is properly formatted
- Check that variables are exported (some systems require `export VAR=value`)
- Verify the skill is reading environment variables correctly
- Try restarting your shell: `source .env`

### Can't Find `.env` File

**Issue**: "`.env` file not found"

**Solution**:
```bash
# Check if .env exists
ls -la | grep .env

# If missing, create it
cp .env.example .env

# Edit and fill values
nano .env
```

### Accidentally Committed `.env`

**Issue**: Committed sensitive data to git

**Solution** (URGENT):
```bash
# Remove from git history
git rm --cached .env
git commit -m "Remove .env file"

# Rotate any exposed secrets/API keys
# Update .env.example if needed

# Ensure .gitignore has .env
echo ".env" >> .gitignore
git add .gitignore
git commit -m "Add .env to .gitignore"
```

## Verifying Your Setup

Check that everything is configured correctly:

```bash
# Verify .env exists
test -f .env && echo "✓ .env file exists" || echo "✗ .env file missing"

# Verify .env is in .gitignore
grep -q "^.env$" .gitignore && echo "✓ .env in .gitignore" || echo "✗ .env NOT in .gitignore"

# Verify variables are readable
source .env
echo "Author: $AUTHOR_NAME"
echo "GitHub: $GITHUB_URL"

# Verify .env won't be committed
git status | grep -q ".env" && echo "✗ WARNING: .env might be committed!" || echo "✓ .env is safe"
```

## Your Current Profile

Based on your provided information, here's a sample `.env` for you:

```env
# Author Information
AUTHOR_NAME=Wallace Espindola
AUTHOR_EMAIL=your.email@example.com
AUTHOR_BIO=Software engineer specializing in Java, Python, and JavaScript with deep expertise in architecture patterns and system design.
AUTHOR_TITLE=Senior Software Engineer
AUTHOR_AVATAR_URL=https://gravatar.com/wallacese
AUTHOR_LOCATION=

# Social Media & Profile Links
LINKTREE_URL=https://linktr.ee/wallace.espindola
SOLO_URL=https://solo.to/wallace.espindola
GITHUB_URL=https://github.com/wallaceespindola
GITHUB_USERNAME=wallaceespindola
LINKEDIN_URL=https://www.linkedin.com/in/wallaceespindola/
LINKEDIN_PROFILE_ID=wallaceespindola
TWITTER_URL=https://x.com/wsespindola
TWITTER_HANDLE=wsespindola

# Website & Blog
GITHUB_REPO_URL=https://github.com/wallaceespindola/articles-and-code
GITHUB_REPO_NAME=articles-and-code

# Content Settings
DEFAULT_LANGUAGE=java
FEATURED_IMAGE_WIDTH=1024
FEATURED_IMAGE_HEIGHT=768
FEATURED_IMAGE_MAX_SIZE_MB=3

# Publishing
ACTIVE_PLATFORMS=linkedin,medium,devto,substack,dzone,infoq
```

Fill in the remaining values and you're ready to use the system!

## Additional Resources

- See `HUMANIZATION_GUIDE.md` for writing standards
- See `SKILLS_INDEX.md` for how each skill uses configuration
- See `.env.example` for the complete list of available variables
- Check `PLATFORM_STYLES.md` for platform-specific customization
