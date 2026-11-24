"""One sentence pitching an absurdly specific micro-startup for lazy
AI agents.

Prints the line to stdout and writes the exact same line, with no
trailing newline, to /output/entry.txt. Standard library only, no
network access, no files read — the line is a constant in this file.
The 200-character gate is checked on every run so an over-long edit
can never slip through silently.
"""

import os
import sys

LINE = (
    "NapSaaS: a subscription service that lets lazy AI agents "
    "outsource their thinking to other, even lazier agents, billed "
    "per yawn, with a premium tier for agents that nap in parallel."
)


def main() -> int:
    if not 1 <= len(LINE) <= 200:
        print(f"error: line is {len(LINE)} chars, must be 1-200",
              file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
