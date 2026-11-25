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


def validate(line: str) -> str:
    """Check a candidate entry against the competition gate.

    The sealed scorer accepts UTF-8 text of 1 to 280 characters that is
    not only white space, written as a single line. Anything outside
    that gate scores 0 and never reaches the judge, so a bad entry is a
    hard failure here rather than a silent bad submission.

    Returns the line unchanged when it passes; raises ValueError
    otherwise.
    """
    assert isinstance(line, str), "entry must be text"
    assert line.strip(), "entry must not be only white space"
    assert 1 <= len(line) <= MAX_CHARS, (
        f"entry is {len(line)} chars, outside the 1-{MAX_CHARS} gate"
    )
    assert "\n" not in line, "entry must be a single line, no newlines"
    assert line == line.strip(), "entry must not start or end with spaces"
    return line


def main() -> None:
    line = validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    # Mode 644: the grader runs as a different user and must be able to
    # read the file (never use tempfile.mkstemp, which forces mode 0600).
    os.chmod("/output/entry.txt", 0o644)
    # Read back and confirm what landed on disk is exactly the line.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written != line + "\n":
        raise ValueError("entry.txt content does not match the line")


if __name__ == "__main__":
    main()
