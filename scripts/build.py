#!/usr/bin/env python3
"""Main build orchestrator.

Generates all CV variants and deploys the website.
Usage:
    python scripts/build.py              # Build all
    python scripts/build.py --website     # Build website only
    python scripts/build.py --pdf         # Build PDFs only
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile

from data_loader import load_all

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.join(SCRIPT_DIR, "..")
OUTPUT_DIR = os.path.join(ROOT_DIR, "output")
TEMPLATES_DIR = os.path.join(ROOT_DIR, "templates")


def cv_pdf_name(profile):
    return f"cv-{profile['name'].lower().replace(' ', '-')}"


def ensure_output_dirs():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Clean stale PDFs (only keep ones generated this run)
    for f in os.listdir(OUTPUT_DIR):
        if f.endswith(".pdf"):
            os.remove(os.path.join(OUTPUT_DIR, f))


def write_data_json(data, name="data"):
    path = os.path.join(OUTPUT_DIR, f"{name}.json")
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
    return path


def build_pdf(template_name, data_file, output_name):
    # Paths relative to the output dir (where the .typ file lives)
    template_rel = os.path.relpath(
        os.path.join(TEMPLATES_DIR, template_name), OUTPUT_DIR
    )
    data_rel = os.path.relpath(data_file, OUTPUT_DIR)

    typst_content = f'''
#import "{template_rel}": cv
#let data = json.decode(read("{data_rel}"))
// TODO: change to json(read(...)) when Typst 0.15 deprecates json.decode
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
        print(f"Error compiling {output_name}: {result.stderr}", file=sys.stderr)
        return False

    print(f"Generated: {pdf_file}")
    return True


def build_all_pdfs(data):
    write_data_json(data, "data-full")

    full_json = os.path.join(OUTPUT_DIR, "data-full.json")

    success = True

    profile = data["profile"]
    name = cv_pdf_name(profile)
    success &= build_pdf("focused.typ", full_json, name)

    return success


def build_website(profile):
    pdf_name = cv_pdf_name(profile)

    mkdocs_yml = os.path.join(ROOT_DIR, "mkdocs.yml")
    with open(mkdocs_yml, "r") as f:
        config = f.read()
    config = config.replace("__CV_PDF__", f"{pdf_name}.pdf")

    tmp = tempfile.NamedTemporaryFile(
        mode="w", suffix=".yml", delete=False, dir=ROOT_DIR
    )
    tmp.write(config)
    tmp.close()

    result = subprocess.run(
        [
            "mkdocs", "build",
            "--config-file", tmp.name,
            "--site-dir", os.path.join(OUTPUT_DIR, "site"),
        ],
        capture_output=True,
        text=True,
        cwd=ROOT_DIR,
    )

    os.unlink(tmp.name)

    if result.returncode != 0:
        print(f"Error building website: {result.stderr}", file=sys.stderr)
        return False

    site_dir = os.path.join(OUTPUT_DIR, "site")
    for f in os.listdir(OUTPUT_DIR):
        if f.endswith(".pdf"):
            shutil.copy(os.path.join(OUTPUT_DIR, f), os.path.join(site_dir, f))

    print("Website generated in output/site/")
    return True


def main():
    parser = argparse.ArgumentParser(description="CV Build System")
    parser.add_argument("--website", action="store_true", help="Build website only")
    parser.add_argument("--pdf", action="store_true", help="Build PDFs only")
    args = parser.parse_args()

    ensure_output_dirs()

    data = load_all()

    if args.website:
        success = build_website(data["profile"])
    elif args.pdf:
        success = build_all_pdfs(data)
    else:
        success = build_all_pdfs(data)
        if success:
            success = build_website(data["profile"])

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
