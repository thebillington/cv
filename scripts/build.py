#!/usr/bin/env python3
"""Main build orchestrator.

One source of facts in data/, two outputs: the PDF and the website.

Usage:
    python scripts/build.py              # PDF + checks + website
    python scripts/build.py --pdf        # PDF + checks
    python scripts/build.py --website    # website only
    python scripts/build.py --no-check   # skip the PDF gates
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
FONTS_DIR = os.path.join(ROOT_DIR, "assets", "fonts")

TEMPLATE = "cv.typ"


def cv_pdf_name(profile):
    return f"{profile['name'].replace(' ', '-')}-CV"


def typst_bin():
    local = os.path.expanduser("~/.local/bin/typst")
    return local if os.path.exists(local) else "typst"


def ensure_output_dirs():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for f in os.listdir(OUTPUT_DIR):
        if f.endswith(".pdf"):
            os.remove(os.path.join(OUTPUT_DIR, f))


def write_data_json(data, name="data"):
    path = os.path.join(OUTPUT_DIR, f"{name}.json")
    with open(path, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    return path


def build_pdf(data_file, output_name, template=TEMPLATE):
    template_rel = os.path.relpath(
        os.path.join(TEMPLATES_DIR, template), OUTPUT_DIR
    )
    data_rel = os.path.relpath(data_file, OUTPUT_DIR)

    typst_content = f'''
#import "{template_rel}": cv
#let data = json("{data_rel}")
#cv(data)
'''
    typ_file = os.path.join(OUTPUT_DIR, f"{output_name}.typ")
    pdf_file = os.path.join(OUTPUT_DIR, f"{output_name}.pdf")

    with open(typ_file, "w") as f:
        f.write(typst_content)

    result = subprocess.run(
        [
            typst_bin(), "compile",
            "--root", ROOT_DIR,
            "--font-path", FONTS_DIR,
            "--pdf-standard", "ua-1",
            typ_file, pdf_file,
        ],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        print(f"Error compiling {output_name}:\n{result.stderr}", file=sys.stderr)
        return False

    print(f"Generated: {pdf_file}")
    return True


def build_website(profile):
    pdf_name = cv_pdf_name(profile)

    with open(os.path.join(ROOT_DIR, "mkdocs.yml"), "r") as f:
        config = f.read()
    config = config.replace("__CV_PDF__", f"{pdf_name}.pdf")

    tmp = tempfile.NamedTemporaryFile(
        mode="w", suffix=".yml", delete=False, dir=ROOT_DIR
    )
    tmp.write(config)
    tmp.close()

    result = subprocess.run(
        [
            sys.executable, "-m", "mkdocs", "build",
            "--config-file", tmp.name,
            "--site-dir", os.path.join(OUTPUT_DIR, "site"),
        ],
        capture_output=True,
        text=True,
        cwd=ROOT_DIR,
    )
    os.unlink(tmp.name)

    if result.returncode != 0:
        print(f"Error building website:\n{result.stderr}", file=sys.stderr)
        return False

    site_dir = os.path.join(OUTPUT_DIR, "site")
    for f in os.listdir(OUTPUT_DIR):
        if f.endswith(".pdf"):
            shutil.copy(os.path.join(OUTPUT_DIR, f), os.path.join(site_dir, f))

    print("Website generated in output/site/")
    return True


def run_checks(profile):
    pdf = os.path.join(OUTPUT_DIR, f"{cv_pdf_name(profile)}.pdf")
    result = subprocess.run(
        [sys.executable, os.path.join(SCRIPT_DIR, "check_pdf.py"), pdf],
        capture_output=True,
        text=True,
    )
    print(result.stdout, end="")
    if result.returncode != 0:
        print(result.stderr, end="", file=sys.stderr)
    return result.returncode == 0


def main():
    parser = argparse.ArgumentParser(description="Rebecchi CV build system")
    parser.add_argument("--website", action="store_true", help="Build website only")
    parser.add_argument("--pdf", action="store_true", help="Build PDF only")
    parser.add_argument("--no-check", action="store_true", help="Skip PDF checks")
    args = parser.parse_args()

    ensure_output_dirs()
    data = load_all()

    if args.website:
        success = build_website(data["profile"])
    else:
        success = build_pdf(write_data_json(data), cv_pdf_name(data["profile"]))
        if success and not args.no_check:
            success = run_checks(data["profile"])
        if success and not args.pdf:
            success = build_website(data["profile"])

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
