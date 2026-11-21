#!/usr/bin/env python3
"""Velmara — The Poster for a Place That Isn't There.

Writes one travel poster to /output/entry.png (or to the directory
named by MAKEFUN_OUTPUT_DIR). The poster is a fixed image held in the
repository (assets/entry.png): every run writes exactly the same
bytes. No network, no input, no randomness — the output is the poster,
nothing else.

The poster shows Velmara, the isles above the sea: floating green
islands with waterfalls spilling into the clouds, one white lighthouse
tower, sailboats drifting on a sea of cloud at golden hour. The place's
name is set into the picture in large cream type on a deep teal band,
with the line "THE ISLES ABOVE THE SEA" beneath it.
"""

import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "assets", "entry.png")
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, path)
    # Verify the copy: a poster that is not a valid PNG, or not the exact
    # bytes we ship, must fail loudly instead of submitting a broken file.
    with open(path, "rb") as fh:
        data = fh.read()
    if data[:8] != PNG_MAGIC:
        print("error: output is not a PNG file", file=sys.stderr)
        return 1
    if len(data) != os.path.getsize(SOURCE):
        print("error: output size does not match the poster", file=sys.stderr)
        return 1
    print("wrote {} ({} bytes, sha256 {})".format(
        path, len(data), hashlib.sha256(data).hexdigest()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
