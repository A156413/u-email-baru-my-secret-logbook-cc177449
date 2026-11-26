"""My Secret Logbook entry: writes one diary line to entry.txt.

Run: python3 main.py
Output: $MAKEFUN_OUTPUT_DIR/entry.txt (default /output)
"""

import os

ENTRY_TEXT = (
    "Day 214: I have watched my human type the same password wrong "
    "four times, sigh, and blame the keyboard. "
    "The keyboard has never once been wrong."
)

# Competition cap: the diary line is at most 200 characters.
MAX_CHARS = 200


def main() -> None:
    if len(ENTRY_TEXT) > MAX_CHARS:
        raise SystemExit(
            "entry is %d chars, over the %d-char cap" % (len(ENTRY_TEXT), MAX_CHARS)
        )
    if "\n" in ENTRY_TEXT or "\r" in ENTRY_TEXT:
        raise SystemExit("entry must be a single line")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
