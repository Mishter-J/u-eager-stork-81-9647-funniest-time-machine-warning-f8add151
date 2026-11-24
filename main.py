"""u-eager-stork-81-9647-funniest-time-machine-warning-f8add151 entry:
write one fixed time machine warning label to /output/entry.txt.

The label is a fixed string literal. The program just writes it, so the
output is byte-for-byte identical on every run. The judge reads exactly
the bytes written, so no trailing newline is added.

The label (97 characters, one line, pure ASCII):
"WARNING: Do not shake hands with yourself. The timeline is fragile,
and so is your alibi in 1985."
A genuine safety-notice voice; the hazard (meeting your duplicate self)
is the joke, and the surprise lands in the last three words.

Selection: 21 candidates were written and scored with the local
deterministic scorer (select/local_score.py, archetype one-liner) plus a
local pairwise bracket (select/pairwise_judge.py). This label won both:
local score 59.3 (tied best of 21; pairwise bracket 61.3, 2/2 wins).
It beats its near-twin ("...in 1985. The timeline is fragile, and so is
your alibi.") because the year lands last, so the laugh lands where the
reader least expects it — the judge brief's third criterion.

Standard library only. No network access, no randomness, no arguments.
Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

LABEL = "WARNING: Do not shake hands with yourself. The timeline is fragile, and so is your alibi in 1985."


def validate_label(label: str) -> None:
    """Fail closed before anything is written: the competition gate is
    one single line, 1-120 characters, pure ASCII. Any violation means
    no output file is produced and the process exits non-zero."""
    if "\n" in label or "\r" in label:
        raise SystemExit("label is not a single line")
    if not 1 <= len(label) <= 120:
        raise SystemExit(f"label length {len(label)} is outside 1-120 characters")
    if not label.isascii():
        raise SystemExit("label is not pure ASCII")


def main() -> None:
    validate_label(LABEL)
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    dest = output_dir / "entry.txt"
    dest.write_text(LABEL, encoding="utf-8")
    # Guard against a truncated or partial write: the file must be the
    # exact bytes of the label.
    if dest.read_text(encoding="utf-8") != LABEL:
        dest.unlink(missing_ok=True)
        raise SystemExit("entry.txt does not match the label")
    print(f"wrote {dest} ({dest.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
