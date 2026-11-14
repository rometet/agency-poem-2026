from __future__ import annotations

import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
POEM_PATH = ROOT / "poem.txt"
MAIN_PATH = ROOT / "main.py"


def run_entry(output_dir: Path) -> bytes:
    environment = os.environ.copy()
    environment["MAKEFUN_OUTPUT_DIR"] = str(output_dir)
    subprocess.run(
        [sys.executable, str(MAIN_PATH)],
        cwd=ROOT,
        env=environment,
        check=True,
        capture_output=True,
        timeout=10,
    )
    return (output_dir / "entry.txt").read_bytes()


class EntryTests(unittest.TestCase):
    def test_poem_is_valid_utf8_within_gate(self) -> None:
        poem_bytes = POEM_PATH.read_bytes()
        poem = poem_bytes.decode("utf-8")
        self.assertGreaterEqual(len(poem), 1)
        self.assertLessEqual(len(poem), 1000)
        self.assertTrue(poem.strip())

    def test_output_matches_poem_exactly(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            output = run_entry(Path(temporary_directory))
        self.assertEqual(output, POEM_PATH.read_bytes())

    def test_repeated_runs_are_deterministic(self) -> None:
        with tempfile.TemporaryDirectory() as first_directory:
            first = run_entry(Path(first_directory))
        with tempfile.TemporaryDirectory() as second_directory:
            second = run_entry(Path(second_directory))
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
