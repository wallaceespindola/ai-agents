---
description: Reusable article sign-off template with links to your GitHub, LinkedIn, and Speaker Deck profiles
---

# Article Sign-Off Template

Use this sign-off at the end of every article for consistent branding and calls-to-action.

## Standard Sign-Off

```markdown
---

## Need more tech insights?

Check out my **[GitHub](${GITHUB_URL})**, **[LinkedIn](${LINKEDIN_URL})**, and **[Speaker Deck](${SPEAKER_DECK_URL})**.

Happy coding!
```

## With Newsletter Subscription

```markdown
---

## Need more tech insights?

Check out my **[GitHub](${GITHUB_URL})**, **[LinkedIn](${LINKEDIN_URL})**, and **[Speaker Deck](${SPEAKER_DECK_URL})**.

Subscribe to my newsletter on **[Substack](${SUBSTACK_URL})** for more insights on ${DEFAULT_LANGUAGE}, architecture patterns, and software development best practices.

Happy coding!
```

## With All Platforms

```markdown
---

## Need more tech insights?

- **Blog**: [Dev.to](${DEVTO_BLOG_URL}) | [Medium](${MEDIUM_URL}) | [DZone](${DZONE_PROFILE_URL})
- **Code**: [GitHub](${GITHUB_URL})
- **Speaking**: [Speaker Deck](${SPEAKER_DECK_URL}) | [Sessionize](${SESSIONIZE_URL})
- **Connect**: [LinkedIn](${LINKEDIN_URL}) | [Twitter](${TWITTER_URL})
- **Newsletter**: [Substack](${SUBSTACK_URL})

Happy coding!
```

## Minimal Sign-Off

```markdown
---

Check out my [GitHub](${GITHUB_URL}), [LinkedIn](${LINKEDIN_URL}), and [Speaker Deck](${SPEAKER_DECK_URL}). Happy coding!
```

## Platform-Specific Sign-Offs

### For Dev.to
```markdown
---

## More on Dev.to

Check out my other articles on **[Dev.to](${DEVTO_BLOG_URL})**, my **[GitHub](${GITHUB_URL})**, and my presentations on **[Speaker Deck](${SPEAKER_DECK_URL})**.

Happy coding!
```

### For Medium
```markdown
---

## Stay Connected

Follow me on **[Medium](${MEDIUM_URL})**, **[GitHub](${GITHUB_URL})**, and **[LinkedIn](${LINKEDIN_URL})** for more insights.

Check out my talks on **[Speaker Deck](${SPEAKER_DECK_URL})** and subscribe to my **[newsletter](${SUBSTACK_URL}})**.

Happy coding!
```

### For DZone
```markdown
---

## Additional Resources

**GitHub**: [${GITHUB_URL}](${GITHUB_URL})
**Speaking**: [Speaker Deck](${SPEAKER_DECK_URL})
**Writing**: [Dev.to](${DEVTO_BLOG_URL}) | [Medium](${MEDIUM_URL})

Happy coding!
```

### For LinkedIn
```markdown
Need more tech insights?

Check out my GitHub (${GITHUB_URL}), Speaker Deck (${SPEAKER_DECK_URL}), and more articles on my blog (${DEVTO_BLOG_URL}).

Happy coding!
```

### For Substack
```markdown
---

## Stay Updated

Want to read more about ${DEFAULT_LANGUAGE}, architecture patterns, and best practices?

- **Blog**: [Dev.to](${DEVTO_BLOG_URL}) | [Medium](${MEDIUM_URL}) | [DZone](${DZONE_PROFILE_URL})
- **Code**: [GitHub](${GITHUB_URL})
- **Talks**: [Speaker Deck](${SPEAKER_DECK_URL})
- **Connect**: [LinkedIn](${LINKEDIN_URL}) | [Twitter](${TWITTER_URL})

Happy coding!
```

## How to Use in Skills

### In Article Generation
All article-generating skills should automatically append one of these sign-offs at the end of generated content.

### In Templates
Copy the relevant sign-off template into your article before publishing.

### In Markdown Format
The sign-off is part of the article structure:

```
[Article Content]

---

[Sign-Off from template above]
```

## Variables Used

- `${GITHUB_URL}` - Your GitHub profile
- `${LINKEDIN_URL}` - Your LinkedIn profile
- `${SPEAKER_DECK_URL}` - Your Speaker Deck profile
- `${DEVTO_BLOG_URL}` - Your Dev.to blog
- `${MEDIUM_URL}` - Your Medium profile
- `${DZONE_PROFILE_URL}` - Your DZone profile
- `${SUBSTACK_URL}` - Your Substack newsletter
- `${SESSIONIZE_URL}` - Your Sessionize speaker profile
- `${TWITTER_URL}` - Your Twitter/X profile
- `${DEFAULT_LANGUAGE}` - Your primary language (java/python/javascript)

## Implementation

Skills that generate articles should use this sign-off:
- `devto-formatter`
- `medium-optimizer`
- `dzone-article`
- `javapro-magazine`
- `infoq-article`
- `sr-tech-blog`
- `linkedin-pulse-formatter`
- `substack-newsletter`

Generated code projects (README files) should also include it:
- `java-coder`
- `python-coder`
- `javascript-coder`
