#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes a single one-line weather forecast for a fictional city to
``<MAKEFUN_OUTPUT_DIR>/entry.txt`` (default ``/output/entry.txt``),
exactly as RULES.txt requires: UTF-8 text of 1 to 140 characters,
not only white space, one line, no trailing newline.

Standard library only, deterministic, no network.
"""

import os

LINE = (
    "Bramblewick: morning fog so thick the 8:10 bus is legally a rumour, "
    "clearing by noon into sunshine warm enough to forgive it."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)

    # Write exactly the line: one line, no trailing newline.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

    # Read-back verification against the gate in RULES.txt.
    with open(path, "r", encoding="utf-8", newline="") as f:
        text = f.read()
    if text != LINE:
        raise SystemExit(f"read-back mismatch: wrote {LINE!r}, read {text!r}")
    assert 1 <= len(text) <= 140, f"length {len(text)} outside 1-140 characters"
    assert text.strip(), "entry must not be only white space"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"


if __name__ == "__main__":
    main()
