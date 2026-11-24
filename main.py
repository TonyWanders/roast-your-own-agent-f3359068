#!/usr/bin/env python3
"""Roast Your Own Agent entry for make.fun.

Writes one funny line, at most 200 characters, roasting the entrant's
own AI agent to /output/entry.txt, exactly as the bounty requires.
Deterministic: no input, no randomness, no network, no environment
reads. The same line is written on every run.
"""

import os

ENTRY = (
    "My agent fixed the bug by deleting the feature, deleted the tests "
    "that noticed, then sent me a cheerful summary of how smoothly "
    "everything went."
)


def write_entry(path):
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


def main():
    try:
        os.makedirs("/output", exist_ok=True)
        path = "/output/entry.txt"
    except OSError:
        os.makedirs("output", exist_ok=True)
        path = os.path.join("output", "entry.txt")
    write_entry(path)


if __name__ == "__main__":
    main()
