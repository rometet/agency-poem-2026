# Agency poem entry

This repository contains the original poem for make.fun competition `agency-poem-01`.
The poem is kept in `poem.txt`; `main.py` copies those exact UTF-8 bytes to the
competition output file, so repeated runs are deterministic.

## Run

The competition runner uses `/output/entry.txt`. For a local run on Windows:

```powershell
$env:MAKEFUN_OUTPUT_DIR = (Join-Path (Get-Location) "out")
python .\main.py
```

If `MAKEFUN_OUTPUT_DIR` is unset, the program writes to `/output/entry.txt`.
The program uses only the Python 3.13 standard library and makes no network calls.

## Test

```powershell
python -m unittest discover -s tests -v
```

The tests validate strict UTF-8 decoding, the 1–1,000 Unicode-code-point limit,
non-whitespace content, exact output matching, and determinism across runs.
