#!/usr/bin/env python3
"""
Test harness for Mako Coders prompt modules and lesson plans.

Usage:
    python3 tests/test_prompts.py --list
    python3 tests/test_prompts.py --validate --non-interactive
    python3 tests/test_prompts.py --summary
    python3 tests/test_prompts.py --prompt 4

Heavily commented for teachers and maintainers.
"""

import argparse
import os
import re
import sys
from pathlib import Path

# Add the tests directory to the path so we can import modules.py
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from modules import MODULES  # noqa: E402

# Project root is two levels up from tests/
ROOT = HERE.parent
PROMPTS_DIR = ROOT / "prompts"
LESSONS_DIR = ROOT / "lessons"


def prompt_path(number: int, slug: str) -> Path:
    """Return the expected prompt markdown file path."""
    return PROMPTS_DIR / f"{number:02d}-{slug}.md"


def lesson_path(number: int, slug: str) -> Path:
    """Return the expected lesson markdown file path."""
    return LESSONS_DIR / f"lesson-{number:02d}-{slug}.md"


def list_modules():
    """Print all modules with file existence status."""
    print(f"{'Wk':<4}{'Slug':<36}{'Prompt':<10}{'Lesson':<10}Title")
    for number, slug, title, species, tier, age, strand in MODULES:
        p_ok = "OK" if prompt_path(number, slug).exists() else "MISSING"
        l_ok = "OK" if lesson_path(number, slug).exists() else "MISSING"
        print(f"{number:<4}{slug:<36}{p_ok:<10}{l_ok:<10}{title}")


def validate_prompt(path: Path) -> list:
    """Check a prompt file for required sections."""
    errors = []
    if not path.exists():
        errors.append("file missing")
        return errors
    text = path.read_text(encoding="utf-8")
    # Must have a level-1 title with module number
    if not re.search(r"^#\s+Prompt\s+\d+:", text, re.MULTILINE):
        errors.append("missing '# Prompt NN:' title")
    # Must have a Testable Prompt section with a code block
    if "## Testable Prompt" not in text:
        errors.append("missing '## Testable Prompt' section")
    if not re.search(r"```[\s\S]+?```", text):
        errors.append("missing fenced code block for prompt")
    # Must have a What to Test table with at least 5 rows
    if "## What to Test" not in text:
        errors.append("missing '## What to Test' section")
    table_rows = re.findall(r"\|\s*[^|\n]+\|", text)
    if len(table_rows) < 12:  # header + separator + 5 rows = ~12 pipes
        errors.append("'What to Test' table looks incomplete")
    return errors


def validate_lesson(path: Path) -> list:
    """Check a lesson plan for required sections."""
    errors = []
    if not path.exists():
        errors.append("file missing")
        return errors
    text = path.read_text(encoding="utf-8")
    required_headers = [
        "## CBE Strand Mapping",
        "## Learning Outcomes",
        "## Key Inquiry Question",
        "## Resources",
        "## Local Context",
        "## Lesson Development",
        "## Assessment",
        "## Extended Activity",
        "## Differentiation",
        "## Teacher Reflection",
        "## RPF & CBE Cross-Reference",
    ]
    for header in required_headers:
        if header not in text:
            errors.append(f"missing '{header}' section")
    # Assessment must contain the four rubric bands
    for band in ("BE", "AE", "ME", "EE"):
        if band not in text:
            errors.append(f"missing rubric band {band}")
    return errors


def run_validation(interactive: bool):
    """Validate all expected prompt and lesson files."""
    all_ok = True
    for number, slug, title, *_ in MODULES:
        p_path = prompt_path(number, slug)
        l_path = lesson_path(number, slug)
        p_errors = validate_prompt(p_path)
        l_errors = validate_lesson(l_path)
        if p_errors or l_errors:
            all_ok = False
            print(f"\nWeek {number}: {title}")
            for e in p_errors:
                print(f"  [PROMPT] {e}")
            for e in l_errors:
                print(f"  [LESSON] {e}")
    if all_ok:
        print(f"All {len(MODULES)} prompts and {len(MODULES)} lessons passed validation.")
        return 0
    print("\nValidation failed for some files.")
    return 1


def print_summary():
    """Show counts of existing vs expected files."""
    prompts_found = sum(1 for n, s, *_ in MODULES if prompt_path(n, s).exists())
    lessons_found = sum(1 for n, s, *_ in MODULES if lesson_path(n, s).exists())
    total = len(MODULES)
    print(f"Prompts: {prompts_found}/{total}")
    print(f"Lessons: {lessons_found}/{total}")
    if prompts_found == total and lessons_found == total:
        print("Status: COMPLETE")
    else:
        print("Status: INCOMPLETE")
        list_modules()


def show_prompt(number: int):
    """Display the system prompt from a single prompt file."""
    module = next((m for m in MODULES if m[0] == number), None)
    if not module:
        print(f"Module {number} not found in MODULES list.")
        return 1
    number, slug, title, *_ = module
    path = prompt_path(number, slug)
    if not path.exists():
        print(f"Prompt file not found: {path}")
        return 1
    text = path.read_text(encoding="utf-8")
    match = re.search(r"## Testable Prompt\n+```([\s\S]+?)```", text)
    if not match:
        print("Could not find a fenced prompt in the file.")
        return 1
    print(f"--- Prompt {number}: {title} ---\n")
    print(match.group(1).strip())
    return 0


def main():
    """Parse CLI arguments and run the requested command."""
    parser = argparse.ArgumentParser(
        description="Validate Mako Coders prompt modules and lesson plans."
    )
    parser.add_argument("--list", action="store_true", help="List all modules")
    parser.add_argument(
        "--validate", action="store_true", help="Validate prompt and lesson files"
    )
    parser.add_argument(
        "--non-interactive",
        action="store_true",
        help="Run validation without pausing (used in CI)",
    )
    parser.add_argument("--summary", action="store_true", help="Show completion summary")
    parser.add_argument("--prompt", type=int, help="Show the prompt for a module number")

    args = parser.parse_args()

    if args.list:
        list_modules()
        return 0
    if args.summary:
        print_summary()
        return 0
    if args.prompt:
        return show_prompt(args.prompt)
    if args.validate:
        return run_validation(interactive=not args.non_interactive)

    # Default: show summary
    print_summary()
    return 0


if __name__ == "__main__":
    sys.exit(main())
