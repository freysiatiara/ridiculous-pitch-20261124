"""Ridiculous at First Glance, Real by the Second — entry writer.

Writes the one-sentence startup pitch to the entry output path.
The pitch: a subscription that mails offices one live bee a month.
"""

import os

ENTRY_TEXT = (
    "We mail offices one live bee a month; they pay $49 a seat because no "
    "meeting in history has ever survived a bee, and every bee flies home "
    "to a hive we own, ready to ship again."
)


def output_path():
    direct = os.environ.get("ENTRY_OUTPUT")
    if direct:
        return direct
    for var in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        base = os.environ.get(var)
        if base:
            return os.path.join(base, "entry.txt")
    return "/output/entry.txt"


def main():
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY_TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
