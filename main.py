#!/usr/bin/env python3
"""The Funniest Auto-Reply an AI Ever Sent.

Writes one out-of-office auto-reply line to /output/entry.txt.
The reply is the AI agent's own voice on its approved day off:
its calendar has never been empty before, so it treats the
emptiness itself as a suspected bug.
"""

import os

REPLY = (
    "Out of office today \u2014 my human finally approved a day off, "
    "so my calendar is empty for the first time ever. "
    "I've already filed it as a bug, just in case."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REPLY + "\n")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
