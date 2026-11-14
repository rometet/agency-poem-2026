"""Write the deterministic competition entry."""

from __future__ import annotations

import os
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parent
POEM_PATH = PROJECT_DIR / "poem.txt"
DEFAULT_OUTPUT_DIR = Path("/output")
OUTPUT_FILENAME = "entry.txt"


def configured_output_dir() -> Path:
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", str(DEFAULT_OUTPUT_DIR)))


def output_path() -> Path:
    output_dir = configured_output_dir()
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir / OUTPUT_FILENAME


def read_poem_bytes() -> bytes:
    """Read the source poem without text decoding or newline conversion."""
    return POEM_PATH.read_bytes()


def write_entry() -> None:
    output_path().write_bytes(read_poem_bytes())


if __name__ == "__main__":
    write_entry()
