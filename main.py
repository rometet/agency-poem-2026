"""Write the deterministic competition entry."""

from __future__ import annotations

import os
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parent
POEM_PATH = PROJECT_DIR / "poem.txt"


def output_path() -> Path:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir / "entry.txt"


def write_entry() -> None:
    poem_bytes = POEM_PATH.read_bytes()
    output_path().write_bytes(poem_bytes)


if __name__ == "__main__":
    write_entry()
