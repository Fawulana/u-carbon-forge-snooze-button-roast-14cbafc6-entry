"""Snooze Button Roast — make.fun entry.

Writes one line roasting an alarm clock that rings at 6 AM on a Saturday
to /output/entry.txt. Deterministic, offline, stdlib only: the exact same
bytes are written on every run.
"""

import os

LINE = (
    "My alarm clock rang at 6 AM on a Saturday like a coworker who shows "
    "up on his day off just to prove he's the hardest worker in the room."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate validation, mirroring the competition gate: 1-200 characters,
    # a single line, not whitespace-only.
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"line is {len(LINE)} chars, must be 1-200")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("line must be a single line")
    if not LINE.strip():
        raise ValueError("line must not be whitespace-only")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

    # Confirm what landed on disk is exactly the line, byte for byte.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != LINE.encode("utf-8"):
        raise RuntimeError("output file does not match the entry line")


if __name__ == "__main__":
    main()
