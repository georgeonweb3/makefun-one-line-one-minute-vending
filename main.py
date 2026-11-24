#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes a single pickup line, spoken by a vending machine to a passing
human, to /output/entry.txt. The line is at most 200 characters, per the
gate: UTF-8 text of 1 to 200 characters, not only whitespace.

Judge brief, in order:
  1. The line is spoken by the machine itself (a bar line loses).
  2. It uses the machine's own world: slot, buttons, coils, snacks,
     hum, exact change.
  3. The laugh lands in the last few words.
  4. Short and speakable, one line in a breath.
  5. Charming rather than creepy.
"""

import os

# The entry: a vending machine flirting with a passing human.
# Machine voice (my coil), machine world (coil, snacks, exact change,
# refunds), punch in the last few words (no refunds on crushes).
LINE = (
    "You walked by and my coil jammed. A thousand snacks dispensed, "
    "never once stuck \u2014 until you. Exact change only: no refunds on crushes."
)


def main() -> None:
    line = LINE.strip()
    assert 1 <= len(line) <= 200, f"line must be 1-200 chars, got {len(line)}"
    assert line == line.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
