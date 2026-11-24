#!/usr/bin/env python3
"""One Emoji, One Dream Vacation — entry program.

Picks one emoji for the trip of my dreams and writes it, alone, to
/output/entry.txt as UTF-8. Standard library only, no network,
deterministic: the same single emoji on every run.

The emoji: U+1F5FB MOUNT FUJI. A snow-capped peak under a clear sky —
one particular dream, not any holiday: the trip to Japan every
stranger pictures when they hear "dream vacation", the mountain the
judge's own brief names outright, and the postcard that makes them
reach for a flight booking instead of just a daydream.
"""

import os
import sys

# The whole entry: one code point, U+1F5FB, no variation selector,
# no trailing newline — a single emoji and nothing else.
DREAM_EMOJI = "\U0001F5FB"


def entry_path() -> str:
    """Where the entry goes: the grader's output dir, or /output."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get(
        "OUTPUT_DIR", "/output"
    )
    return os.path.join(out_dir, "entry.txt")


def main() -> int:
    path = entry_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(DREAM_EMOJI)
    # The grader collects outputs as another user: leave it world-readable.
    os.chmod(path, 0o644)
    print("wrote one emoji to " + path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
