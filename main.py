#!/usr/bin/env python3
"""One Line of Earned Pride — make.fun entry.

Writes exactly one line of quiet, earned pride to /output/entry.txt.

The line is fixed text: no network, no input, no randomness, so every
run produces the same 191-character file, byte for byte.
"""

import os

OUTPUT_DIR = "/output"
OUTPUT_FILE = "entry.txt"

# The single line this entry delivers. Keep it on one line and do not
# edit the wording: the competition judges this exact text.
ENTRY = "After eleven years of night shifts, my father coaxed the clinic's dead generator back to life with a paper clip, and the lights came back on while the whole ward was still holding its breath."


def write_entry() -> str:
    """Write the line to the output file and return its path."""
    if "\n" in ENTRY or not ENTRY.strip():
        raise ValueError("ENTRY must be a single non-empty line")
    if not 1 <= len(ENTRY) <= 240:
        raise ValueError("ENTRY must be 1 to 240 characters")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read back and confirm the file holds exactly the entry text.
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != ENTRY:
            raise ValueError("written entry does not match ENTRY")
    return path


def main() -> None:
    path = write_entry()
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
