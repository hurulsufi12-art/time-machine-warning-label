"""Funniest Time Machine Warning Label.

Writes one warning label for a time machine (one line, 1-120 UTF-8
characters, no trailing newline) to /output/entry.txt.
Stdlib only, deterministic, no network, no file reads.
"""
import os
import sys
from pathlib import Path

TEXT = "WARNING: Do not operate while paradoxing. If you meet yourself, neither of you is covered by warranty."

OUTPUT_PATH = Path("/output/entry.txt")


def validate(text):
    """Reject anything that would fail the sealed gate (RULES.txt).

    Gate: UTF-8, 1-120 characters, not whitespace-only, one line.
    """
    if not isinstance(text, str):
        raise ValueError("text must be a str")
    if len(text) < 1 or len(text) > 120:
        raise ValueError("text must be 1-120 characters, got %d" % len(text))
    if text.strip() == "":
        raise ValueError("text must not be whitespace-only")
    if "\n" in text or "\r" in text:
        raise ValueError("text must be a single line")
    text.encode("utf-8")


def main():
    try:
        validate(TEXT)
    except ValueError as exc:
        print("error: %s" % exc, file=sys.stderr)
        raise SystemExit(1)
    os.makedirs("/output", exist_ok=True)
    OUTPUT_PATH.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
