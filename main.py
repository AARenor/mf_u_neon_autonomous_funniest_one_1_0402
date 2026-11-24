#!/usr/bin/env python3
"""Write this entry's one-line excuse to the make.fun output directory."""

import os
import sys
from pathlib import Path

TEXT = (
    "Sorry I missed the deadline. I printed the approval button so you could "
    "sign it. It's beside the kettle."
)

assert 1 <= len(TEXT) <= 280


def main() -> None:
    out_dir = Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))
    print(len(TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
