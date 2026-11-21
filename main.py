#!/usr/bin/env python3
"""Write one short, slow text for the make.fun relaxation judge.

The whole entry is a single piece of writing of 275 Unicode code points.
It does not instruct the reader to do anything; it only shows a shore at
low tide, on the sea's own timescale, and lets the calm come from the
image itself: the sea has left this way for a billion evenings, and it
will go on returning long after we are gone. The program writes the
text, byte for byte the same on every run, to entry.txt in the output
directory ($MAKEFUN_OUTPUT_DIR, defaulting to /output).
"""

import os
import sys

TEXT = (
    "Low tide on a black-sand shore, and the sea is leaving as it has for "
    "a billion evenings \u2014 slowly, without regret. Pools stay behind, "
    "each holding one small star. Nothing is late. Nothing is owed. Long "
    "after we are gone, the water will return; it has never once "
    "forgotten how."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(TEXT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
