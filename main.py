#!/usr/bin/env python3
"""The Agent's Uh-Oh entry: write the word `halp` to entry.txt.

When an agent has no idea what to do, it does not philosophise and
it does not recalculate — it just blurts out a panicked little cry
for help, misspelled, because it is too lost to even spell "help"
right. Exactly four bytes, no newline, no explanation attached.
"""

import os
from pathlib import Path

WORD = "halp"


def output_path() -> Path:
    """Where the entry goes: $MAKEFUN_OUTPUT_DIR/entry.txt, or
    /output/entry.txt when the variable is unset."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(out_dir) / "entry.txt"


def main() -> None:
    path = output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(WORD, encoding="utf-8")


if __name__ == "__main__":
    main()
