---
name: blogs
description: Use when drafting, revising, or preparing Markdown blog posts for publication, especially when the task includes frontmatter setup, reusable templates, SEO polish, or stripping internal notes before release.
---

# Blogs

Create publication-ready Markdown blog posts for an AI-agent workflow. Use this skill when the task is to turn a rough idea, source notes, changelog, or product update into a clean blog draft that can be reviewed and published.

## When To Use

- The user wants a new blog post from a prompt, outline, notes, changelog, issue thread, or release summary.
- The repo stores posts as Markdown and needs frontmatter, a consistent slug, and a predictable section structure.
- The user asks for editing, cleanup, SEO improvement, or final publish prep instead of raw ideation.
- The draft contains internal notes, placeholders, TODOs, or sensitive implementation details that must be removed before publishing.

Do not use this skill for news fact-checking by itself. If claims depend on current external facts, browse and verify first.

## Quick Start

1. Decide the post type in [references/blog_templates.md](references/blog_templates.md).
2. Make scripts executable (one-time setup): `chmod +x scripts/*.py`
3. Create a draft shell with `scripts/init_blog_post.py`.
4. Write or revise the post in Markdown.
5. Run the quality pass using [references/checklist.md](references/checklist.md) and [references/seo_guide.md](references/seo_guide.md).
6. Sanitize the final draft with `scripts/sanitize_for_publish.py` before handing it off for publishing.

## Workflow

### 1. Frame The Post

Identify all of the following before writing:

- Audience: who should care right now.
- Core takeaway: one sentence the reader should remember.
- Evidence: notes, links, release details, examples, screenshots, or data already available.
- CTA: what the reader should do next, if anything.

If any of those are missing, ask targeted questions or leave explicit placeholders in the draft rather than inventing facts.

### 2. Pick A Template

Use [references/blog_templates.md](references/blog_templates.md) and choose the lightest template that fits:

- `how-to`: tutorial, walkthrough, setup guide
- `announcement`: launch, release, changelog, milestone
- `thought-piece`: opinion, strategy, lessons learned
- `roundup`: curated links, research notes, recap

Do not force every post into the same structure. A short launch note should stay short.

### 3. Scaffold The File

Use the init script to generate a draft with frontmatter and section prompts:

```bash
./scripts/init_blog_post.py \
  --title "How We Reduced Build Times by 40 Percent" \
  --template how-to \
  --author "OpenClaw Team" \
  --output content/blog
```

The script creates a dated Markdown file with:

- filename-safe slug
- frontmatter
- template-specific headings
- placeholders for summary, audience, CTA, and tags

### 4. Write Like An Editor

Default writing rules:

- Lead with the point. The first two paragraphs should establish why the post matters.
- Prefer concrete nouns, active verbs, and short paragraphs.
- Keep one idea per section.
- Replace hype with evidence.
- Use examples, snippets, metrics, or screenshots only when they sharpen the point.
- If a claim is uncertain, mark it for verification instead of smoothing over it.

Good pattern:

```markdown
Build times had drifted from 8 minutes to 14. That slowed every review cycle and made small fixes feel expensive.

We traced the slowdown to duplicate asset work in CI. After collapsing those steps and caching the generated bundle, median build time dropped to 8.4 minutes.
```

Weak pattern:

```markdown
We are excited to share an amazing improvement to our world-class build system that dramatically changes developer productivity.
```

### 5. Edit For Readability And Search

Run through:

- [references/checklist.md](references/checklist.md) for structure and editorial quality
- [references/seo_guide.md](references/seo_guide.md) for title, headings, metadata, and link text

Keep SEO subordinate to readability. Keyword stuffing, repetitive subheads, and unnatural anchor text degrade the post.

### 6. Sanitize Before Publish

Use the sanitizer when the draft may contain internal comments or working notes:

```bash
./scripts/sanitize_for_publish.py content/blog/2026-03-16-build-times.md
```

Default behavior writes `*.publish.md` next to the source file. It removes or flags:

- HTML comments
- `TODO`, `FIXME`, and `TBD`
- `[INTERNAL]`, `[NOTE]`, `[DRAFT]`, and similar markers
- lines marked `Internal:` or `Draft note:`
- repeated blank lines

If you want the cleaned content on stdout instead:

```bash
./scripts/sanitize_for_publish.py path/to/post.md --stdout
```

Review the output before publication. Sanitizing is a safety net, not a substitute for judgment.

## File And Metadata Conventions

- Prefer one post per Markdown file.
- Use kebab-case slugs.
- Keep dates in ISO format: `YYYY-MM-DD`.
- Frontmatter should stay factual and machine-friendly.
- Tags should be specific enough to help retrieval later.

Recommended frontmatter fields:

```yaml
---
title: Example title
slug: example-title
date: 2026-03-16
author: OpenClaw Team
summary: One-sentence summary for feeds and previews.
tags:
  - engineering
  - performance
draft: true
---
```

## Common Mistakes

- Inventing supporting facts because the source material is thin.
- Opening with generic market framing instead of the actual news or lesson.
- Writing headings that say almost the same thing as the title.
- Leaving internal review notes in the body.
- Turning every post into a long-form essay when a concise update would be stronger.

## Resources

- Templates: [references/blog_templates.md](references/blog_templates.md)
- Publish checklist: [references/checklist.md](references/checklist.md)
- SEO guide: [references/seo_guide.md](references/seo_guide.md)
- Draft scaffolding: [scripts/init_blog_post.py](scripts/init_blog_post.py)
- Publish sanitization: [scripts/sanitize_for_publish.py](scripts/sanitize_for_publish.py)
