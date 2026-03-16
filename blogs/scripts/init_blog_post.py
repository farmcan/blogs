#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path


TEMPLATES = {
    "how-to": [
        "## Why This Matters",
        "",
        "## What You Need Before You Start",
        "",
        "## Step 1",
        "",
        "## Step 2",
        "",
        "## Common Pitfalls",
        "",
        "## Next Steps",
    ],
    "announcement": [
        "## What Changed",
        "",
        "## Why It Matters",
        "",
        "## What You Can Do Now",
        "",
        "## What Happens Next",
    ],
    "thought-piece": [
        "## The Situation",
        "",
        "## What We Learned",
        "",
        "## Where Most Teams Get Stuck",
        "",
        "## A Better Default",
        "",
        "## Closing Thought",
    ],
    "roundup": [
        "## Key Takeaways",
        "",
        "## Item 1",
        "",
        "## Item 2",
        "",
        "## Item 3",
        "",
        "## What To Watch Next",
    ],
}


def slugify(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-{2,}", "-", value)
    return value.strip("-") or "untitled-post"


def build_frontmatter(title: str, slug: str, author: str, publish_date: str) -> list[str]:
    return [
        "---",
        f"title: {title}",
        f"slug: {slug}",
        f"date: {publish_date}",
        f"author: {author}",
        "summary: TODO",
        "tags:",
        "  - TODO",
        "draft: true",
        "---",
        "",
    ]


def build_body(template: str) -> list[str]:
    return [
        "> Audience: TODO",
        "",
        "> Core takeaway: TODO",
        "",
        "> CTA: TODO",
        "",
        *TEMPLATES[template],
        "",
    ]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a dated Markdown blog draft with frontmatter and a template."
    )
    parser.add_argument("--title", required=True, help="Post title")
    parser.add_argument(
        "--template",
        choices=sorted(TEMPLATES.keys()),
        default="announcement",
        help="Post template to scaffold",
    )
    parser.add_argument("--author", default="TODO", help="Author name")
    parser.add_argument(
        "--date",
        dest="publish_date",
        default=date.today().isoformat(),
        help="Publish date in YYYY-MM-DD format",
    )
    parser.add_argument(
        "--output",
        default=".",
        help="Output directory for the generated Markdown file",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite the target file if it already exists",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    slug = slugify(args.title)
    output_dir = Path(args.output)
    filename = f"{args.publish_date}-{slug}.md"
    output_path = output_dir / filename

    if output_path.exists() and not args.force:
        print(
            f"Refusing to overwrite existing file: {output_path}. Use --force to replace it.",
            file=sys.stderr,
        )
        return 1

    lines = build_frontmatter(args.title, slug, args.author, args.publish_date)
    lines.extend(build_body(args.template))

    output_dir.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")
    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
