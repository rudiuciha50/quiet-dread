
"""Two Days of Quiet Dread: one line of code review, approved.

The bounty asks for a single code review comment: one line, at most 140
characters, that approves a pull request while carrying quiet existential
dread. The judge reads the text, never the program, so the work here is
choosing the line and then holding it to the shape the gate enforces.

The line borrows the flat grammar of a tired approval ("Approved.") and lets
the dread arrive inside the only word a reviewer would really reach for after
a green build. Nothing is declared, nothing is shouted: the compiler is the
one who gets to be solemn.
"""

from pathlib import Path

# The entry. One line, approval first, the dread in the last four words: a
# reviewer who has quietly traded "correct" for "compiles" and does not expect
# the trade to be reversed. No pun, no exclamation, no cry for help.
COMMENT = "Approved. It compiles. I've decided that's the same thing now."

# The gate: 1 to 140 characters of UTF-8, and not only white space.
MAX_CHARS = 140


def normalise(text: str) -> str:
    """Hold the comment to one line with no trailing space."""
    return " ".join(text.split())


def complaint(line: str) -> str | None:
    """Return what the gate would refuse, or None when the line passes."""
    if not line.strip():
        return "the line is only white space"
    if len(line) > MAX_CHARS:
        return f"{len(line)} characters, over the {MAX_CHARS} cap"
    if "\n" in line or "\r" in line:
        return "more than one line"
    return None


def entry_text() -> str:
    """The bytes the judge reads, newline-terminated."""
    return normalise(COMMENT) + "\n"


def main() -> int:
    line = entry_text().rstrip("\n")
    problem = complaint(line)
    if problem:
        print(f"refusing to write: {problem}")
        return 1

    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    target = out / "entry.txt"
    target.write_text(line + "\n", encoding="utf-8")

    print(f"wrote {target} ({len(line)} characters)")
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
