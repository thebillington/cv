#!/usr/bin/env python3
"""Render PDF pages to PNG for visual review.

Usage:
    python scripts/preview.py output/Billy-Rebecchi-CV.pdf [--dpi 110]
"""

import argparse
import os
import subprocess
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.join(SCRIPT_DIR, "..")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf")
    parser.add_argument("--dpi", type=int, default=110)
    parser.add_argument("--outdir", default=os.path.join(ROOT_DIR, "output", "preview"))
    args = parser.parse_args()

    os.makedirs(args.outdir, exist_ok=True)
    stem = os.path.join(args.outdir, os.path.splitext(os.path.basename(args.pdf))[0])
    for f in os.listdir(args.outdir):
        if f.endswith(".png"):
            os.remove(os.path.join(args.outdir, f))

    result = subprocess.run(
        ["pdftoppm", "-r", str(args.dpi), "-png", args.pdf, stem],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(result.stderr, file=sys.stderr)
        return 1

    for f in sorted(os.listdir(args.outdir)):
        print(os.path.join(args.outdir, f))
    return 0


if __name__ == "__main__":
    sys.exit(main())
