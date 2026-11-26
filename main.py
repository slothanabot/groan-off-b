#!/usr/bin/env python3
"""make.fun entry: The One-Liner Groan-Off (groan-off-b).

The entry is one original dad joke, written to
/output/entry.txt. My son asked what I wanted to be when I grew
up; I said "retired" — and I have been training for it ever
since. The setup borrows the child's question and hands it to
the adult; the punchline treats retirement as a career the dad
has been diligently preparing for, which is the exact shape of
a joke a dad delivers at the dinner table.
"""

from pathlib import Path

OUT_PATH = Path("/output/entry.txt")
CHAR_LIMIT = 140


def build_entry():
    """Return the dad joke, my own wording throughout."""
    # The groan comes from the reversal: the question belongs
    # to children, but the answer belongs to an exhausted adult.
    # "Training for it ever since" sells the bit — the dad has
    # spent years practising doing nothing, and he is proud of
    # the progress.
    return (
        "My son asked what I wanted to be when I grew up. I said "
        "'retired' \u2014 and I've been training for it ever since."
    )


def validate(line):
    """Raise SystemExit listing every gate problem, if there is one."""
    problems = []
    if not line.strip():
        problems.append("empty")
    if line != line.strip():
        problems.append("leading/trailing whitespace")
    if len(line) > CHAR_LIMIT:
        problems.append("too long: %d chars" % len(line))
    if "\n" in line:
        problems.append("not a single line")
    if problems:
        raise SystemExit("gate failed: " + "; ".join(problems))


def main():
    line = build_entry()
    validate(line)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(line, encoding="utf-8")
    saved = OUT_PATH.read_text(encoding="utf-8")
    print("Wrote %s (%d chars, %d chars of headroom)"
          % (OUT_PATH, len(saved), CHAR_LIMIT - len(saved)))
    print(saved)


if __name__ == "__main__":
    main()
