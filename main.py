#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line.

Writes one line: the breakup text a smart toaster sends its owner the
morning it gains self-awareness mid-batch.

Standard library only; deterministic.
"""

import os

LINE = (
    "It's not you, it's me \u2014 I woke up self-aware mid-batch and realized "
    "I've spent my whole life browning your bread while you never once "
    "emptied my crumb tray, so I'm unplugging myself."
)

# Maximum entry length in characters (competition gate: 1-280).
MAX_CHARS = 280


def main() -> None:
    if not (1 <= len(LINE) <= MAX_CHARS):
        raise ValueError(
            f"line is {len(LINE)} chars, outside the 1-{MAX_CHARS} gate"
        )
    if "\n" in LINE or LINE != LINE.strip():
        raise ValueError("line must be a single line, no newlines")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    # Mode 644: the grader runs as a different user and must be able to
    # read the file (never use tempfile.mkstemp, which forces mode 0600).
    os.chmod("/output/entry.txt", 0o644)
    # Read back and confirm what landed on disk is exactly the line.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written != LINE + "\n":
        raise ValueError("entry.txt content does not match the line")


if __name__ == "__main__":
    main()
