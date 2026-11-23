"""Front-Page Summary of 23 Nov 2026.

Copies the pre-rendered newspaper front page (entry.png) to the
output directory as entry.png. No network, no randomness:
every run writes the same bytes.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
TARGET_NAME = "entry.png"


def output_dir() -> Path:
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(chosen)


def main() -> None:
    if not SOURCE.is_file():
        raise SystemExit(f"missing source image: {SOURCE}")
    out = output_dir()
    out.mkdir(parents=True, exist_ok=True)
    target = out / TARGET_NAME
    shutil.copyfile(SOURCE, target)
    if target.stat().st_size != SOURCE.stat().st_size:
        raise SystemExit("copied file size does not match the source")
    print(f"wrote {target} ({target.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
