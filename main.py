"""Write the entry line for the make.fun bounty "The Vacuum's Alibi".

The bounty asks for one line, at most 200 characters, in which a robot
vacuum explains why it missed a spot. This program holds that line in the
EXCUSE constant, checks it against the gate rules, and writes it to
entry.txt in the output directory (/output by default, or the directory
named by MAKEFUN_OUTPUT_DIR).

The program is deterministic: it reads no clock, uses no randomness, and
writes the same bytes on every run.
"""

import os
import sys

EXCUSE = (
    "I did not miss it. I classified it as furniture after the third "
    "collision, and my insurance does not cover upholstery, so I kept my "
    "distance."
)

MAX_LENGTH = 200


def validate_entry(text):
    """Return an error message for an invalid entry, or None if it is valid."""
    if not isinstance(text, str):
        return "entry is not a string"
    if not text.strip():
        return "entry is blank"
    if len(text) > MAX_LENGTH:
        return "entry is %d code points, over the %d cap" % (len(text), MAX_LENGTH)
    if text != text.strip():
        return "entry has leading or trailing whitespace"
    if "\n" in text or "\r" in text:
        return "entry is not a single line"
    if '"' in text:
        return "entry contains a straight double quote"
    if not text.isascii():
        return "entry is not ASCII"
    return None


def main():
    error = validate_entry(EXCUSE)
    if error is not None:
        print("error: %s" % error, file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")

    payload = (EXCUSE + "\n").encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(payload)

    with open(path, "rb") as handle:
        on_disk = handle.read()

    if on_disk != payload:
        print("error: wrote %d bytes but read back %d" % (len(payload), len(on_disk)),
              file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
