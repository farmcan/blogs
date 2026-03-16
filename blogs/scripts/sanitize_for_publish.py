#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


LINE_PATTERNS = [
    re.compile(r"^\s*(?:TODO|FIXME|TBD)\b.*$", re.IGNORECASE),
    re.compile(r"^\s*\[(?:INTERNAL|NOTE|NOTES|DRAFT|WIP)\]\s*.*$", re.IGNORECASE),
    re.compile(r"^\s*(?:Internal|Draft note|Editor note)\s*:\s*.*$", re.IGNORECASE),
]

INLINE_PATTERNS = [
    re.compile(r"\s*\[(?:INTERNAL|NOTE|DRAFT|WIP)\]\s*", re.IGNORECASE),
]

HTML_COMMENT_PATTERN = re.compile(r"<!--.*?-->", re.DOTALL)
BLANK_RUN_PATTERN = re.compile(r"\n{3,}")


def sanitize(text: str) -> tuple[str, dict[str, int]]:
    stats = {"html_comments": 0, "removed_lines": 0, "inline_markers": 0}

    def replace_comment(match: re.Match[str]) -> str:
        stats["html_comments"] += 1
        return ""

    text = HTML_COMMENT_PATTERN.sub(replace_comment, text)

    kept_lines: list[str] = []
    for line in text.splitlines():
        if any(pattern.match(line) for pattern in LINE_PATTERNS):
            stats["removed_lines"] += 1
            continue

        for pattern in INLINE_PATTERNS:
            line, replacements = pattern.subn(" ", line)
            stats["inline_markers"] += replacements

        kept_lines.append(line.rstrip())

    cleaned = "\n".join(kept_lines).strip() + "\n"
    cleaned = BLANK_RUN_PATTERN.sub("\n\n", cleaned)
    return cleaned, stats


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Remove internal notes and cleanup markers from a Markdown draft."
    )
    parser.add_argument("source", help="Markdown file to sanitize")
    parser.add_argument(
        "--output",
        help="Explicit output path. Defaults to <source>.publish.md",
    )
    parser.add_argument(
        "--stdout",
        action="store_true",
        help="Write sanitized content to stdout instead of a file",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source = Path(args.source)

    if not source.exists():
        print(f"Source file not found: {source}", file=sys.stderr)
        return 1

    original = source.read_text(encoding="utf-8")
    cleaned, stats = sanitize(original)

    if args.stdout:
        sys.stdout.write(cleaned)
    else:
        output = Path(args.output) if args.output else source.with_suffix(".publish.md")
        output.write_text(cleaned, encoding="utf-8")
        print(output)

    print(
        "Removed "
        f"{stats['html_comments']} HTML comment block(s), "
        f"{stats['removed_lines']} flagged line(s), and "
        f"{stats['inline_markers']} inline marker(s).",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
