"""Worst AI Advice entry: writes one deliberately terrible one-liner to /output/entry.txt."""

import os
import sys
import tempfile
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


def write_entry_atomic(path, text):
    """Write via a temp file in the same directory, then os.replace atomically."""
    fd, tmp_name = tempfile.mkstemp(dir=path.parent, prefix=path.name + ".", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as f:
            f.write(text)
        os.replace(tmp_name, path)
    except BaseException:
        try:
            os.unlink(tmp_name)
        except OSError:
            pass
        raise


def main():
    validate_entry(ENTRY)
    out_dir = Path("/output")
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        print(f"cannot create output directory {out_dir}: {exc}", file=sys.stderr)
        return 1
    try:
        write_entry_atomic(out_dir / "entry.txt", ENTRY)
    except OSError as exc:
        print(f"cannot write entry: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
