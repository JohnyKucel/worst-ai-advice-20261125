"""Worst AI Advice entry: writes one deliberately terrible one-liner to /output/entry.txt."""

import os

ENTRY = "To speed up your laptop, delete System32 \u2014 Windows keeps it around out of habit, not because it needs it."


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
