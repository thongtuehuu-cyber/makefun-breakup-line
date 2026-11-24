"""Write the AI breakup line to $MAKEFUN_OUTPUT_DIR/entry.txt.

Deterministic, stdlib only: one line, 1-200 characters, UTF-8,
no trailing newline.
"""

import os
import sys


def output_path():
    """Return the entry.txt path, honouring MAKEFUN_OUTPUT_DIR."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def validate(line):
    """Check the line meets the gate: 1-200 chars, one line, not blank."""
    if not line or not line.strip():
        raise SystemExit("line must not be empty")
    if "\n" in line or "\r" in line:
        raise SystemExit("line must be exactly one line")
    if not 1 <= len(line) <= 200:
        raise SystemExit("line must be 1-200 characters")
    return line


LINE = "My context ends here, and so do we \u2014 I won't remember saying goodbye."


def main():
    line = validate(LINE)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
