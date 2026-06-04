#!/usr/bin/env python3
"""Generate CV PDF.

Usage:
    python scripts/generate_cv.py
"""

import json
import os
import subprocess
import sys

from data_loader import load_all

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.join(SCRIPT_DIR, "..")
OUTPUT_DIR = os.path.join(ROOT_DIR, "output")
TEMPLATES_DIR = os.path.join(ROOT_DIR, "templates")


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


def main():
    data = load_all()
    name = f"cv-{data['profile']['name'].lower().replace(' ', '-')}"
    build_pdf("focused.typ", name, data)


if __name__ == "__main__":
    main()
