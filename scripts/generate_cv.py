#!/usr/bin/env python3
"""Generate specific CV PDFs.

Usage:
    python scripts/generate_cv.py full        # Full 2-page CV
    python scripts/generate_cv.py short       # Short 1-page CV
    python scripts/generate_cv.py --variant senior-engineer
"""

import argparse
import json
import os
import shutil
import subprocess
import sys

from data_loader import load_all

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.join(SCRIPT_DIR, "..")
OUTPUT_DIR = os.path.join(ROOT_DIR, "output")
TEMPLATES_DIR = os.path.join(ROOT_DIR, "templates")

VARIANTS = {
    "senior-engineer": "senior-engineer.typ",
    "staff-engineer": "staff-engineer.typ",
    "engineering-manager": "engineering-manager.typ",
    "platform-engineer": "platform-engineer.typ",
}


def build_pdf(template_name, output_name, data):
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    data_file = os.path.join(OUTPUT_DIR, f"{output_name}.json")
    with open(data_file, "w") as f:
        json.dump(data, f, indent=2)

    template_rel = os.path.relpath(
        os.path.join(TEMPLATES_DIR, template_name), OUTPUT_DIR
    )
    data_rel = os.path.relpath(data_file, OUTPUT_DIR)

    typst_content = f'''
#import "{template_rel}": cv
#let data = json.decode(read("{data_rel}"))
#cv(data)
'''

    typ_file = os.path.join(OUTPUT_DIR, f"{output_name}.typ")
    pdf_file = os.path.join(OUTPUT_DIR, f"{output_name}.pdf")

    with open(typ_file, "w") as f:
        f.write(typst_content)

    result = subprocess.run(
        ["typst", "compile", "--root", ROOT_DIR, typ_file, pdf_file],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        print(f"Error: {result.stderr}", file=sys.stderr)
        sys.exit(1)

    print(f"Generated: {pdf_file}")


def generate_full():
    data = load_all()
    build_pdf("focused.typ", "cv-full", data)
    shutil.copy(
        os.path.join(OUTPUT_DIR, "cv-full.pdf"),
        os.path.join(OUTPUT_DIR, "cv-latest.pdf"),
    )


def generate_short():
    data = load_all()
    data["experience"] = data["experience"][:3]
    build_pdf("senior-engineer.typ", "cv-short", data)


def generate_variant(name):
    if name not in VARIANTS:
        print(f"Unknown variant: {name}", file=sys.stderr)
        print(f"Available: {', '.join(VARIANTS.keys())}", file=sys.stderr)
        sys.exit(1)

    data = load_all()
    build_pdf(VARIANTS[name], f"cv-{name}", data)


def main():
    parser = argparse.ArgumentParser(description="Generate CV PDFs")
    parser.add_argument("type", nargs="?", default="full",
                        help="CV type: full, short, or variant name")
    parser.add_argument("--variant", help="Variant name")
    args = parser.parse_args()

    if args.variant:
        generate_variant(args.variant)
    elif args.type == "full":
        generate_full()
    elif args.type == "short":
        generate_short()
    elif args.type in VARIANTS:
        generate_variant(args.type)
    else:
        print(f"Unknown type: {args.type}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
