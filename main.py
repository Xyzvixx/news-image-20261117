#!/usr/bin/env python3
"""Entry program for make.fun bounty news-image-20261117.

Writes the front-page image summarising world news of Tuesday
17 November 2026 to /output/entry.png (or $MAKEFUN_OUTPUT_DIR).

The image itself is the entry: a newspaper front page with six stories
from 17 November 2026 (Crimea bridge, Hormuz/Bahrain, Shenzhen summit,
markets, Japan jets, Pentagon audit). It is stored in this repository
as entry.png and copied byte-for-byte, so both grader runs produce
identical output. Standard library only, no network.
"""

import os
import shutil
from pathlib import Path

IMAGE_NAME = "entry.png"


def main() -> None:
    here = Path(__file__).resolve().parent
    source = here / IMAGE_NAME
    if not source.is_file():
        raise FileNotFoundError(f"{IMAGE_NAME} is missing from the repository")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / IMAGE_NAME
    shutil.copyfile(source, target)
    if target.stat().st_size != source.stat().st_size:
        raise IOError(f"copy of {IMAGE_NAME} is incomplete")


if __name__ == "__main__":
    main()
