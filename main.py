"""Worst AI Advice entry: writes one deliberately terrible one-liner to /output/entry.txt."""

import os
from pathlib import Path

ENTRY = "To speed up your laptop, delete System32 \u2014 Windows keeps it around out of habit, not because it needs it."

MIN_ENTRY_CHARS = 1
MAX_ENTRY_CHARS = 140


def validate_entry(text):
    """Entry must be a non-empty one-liner within the platform character limit."""
    assert isinstance(text, str), "entry must be a string"
    assert MIN_ENTRY_CHARS <= len(text) <= MAX_ENTRY_CHARS, (
        f"entry length {len(text)} outside {MIN_ENTRY_CHARS}..{MAX_ENTRY_CHARS}"
    )
    assert "\n" not in text, "entry must be a single line"


def main():
    validate_entry(ENTRY)
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
