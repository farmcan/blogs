# Publish Checklist

Run this checklist before handing a post off for publishing.

## Editorial

- The title matches the actual content and is not generic.
- The first two paragraphs explain why the reader should care.
- Each section advances the post instead of repeating the title.
- Claims are supported by examples, code, metrics, or a verifiable source.
- The CTA is explicit or intentionally omitted.
- Paragraphs are short enough to scan on mobile.

## Structure

- The post uses a template that matches its purpose.
- Headings are descriptive and non-redundant.
- Lists are flat and easy to scan.
- Code or commands are fenced and accurate.
- Internal transitions are clear; the draft does not jump between ideas.

## Metadata

- Frontmatter fields are complete.
- `slug` is kebab-case.
- `date` is correct.
- `summary` is specific and useful in previews.
- Tags are relevant and not placeholders.
- `draft` matches the intended publish state.

## Safety

- No TODO, FIXME, TBD, or review markers remain.
- No HTML comments remain unless they are intentionally publishable.
- No confidential details, credentials, private links, or internal-only decisions leak into the draft.
- Quotes, metrics, and timelines have been verified.

## Final Pass

- Run `./scripts/sanitize_for_publish.py <post.md>`.
- Read the sanitized output once from top to bottom.
- If possible, view the rendered Markdown and check heading rhythm, code blocks, and links.
