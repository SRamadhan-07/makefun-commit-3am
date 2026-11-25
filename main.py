"""Write the 3 AM commit message entry to /output/entry.txt."""

from pathlib import Path

ENTRY_TEXT = "fix: broke prod at 3 a.m.; the on-call human is me, and I have questions"


def main() -> None:
    # The gate expects exactly one line, UTF-8, with no extra newline.
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY_TEXT, encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
