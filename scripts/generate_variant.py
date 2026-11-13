#!/usr/bin/env python3
"""Generate a CV tailored to one job description.

Selects the most relevant achievements per role using the keyword bank, then
renders the normal template. It never rewrites Billy's sentences, only chooses
which evidence leads.

Usage:
    python scripts/generate_variant.py --job-description jd.txt --output output/tailored.pdf
"""

import argparse
import json
import os
import subprocess
import sys

from data_loader import load_all, load_keywords
from score_job import flatten, rank_achievements, score_jd

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.join(SCRIPT_DIR, "..")
OUTPUT_DIR = os.path.join(ROOT_DIR, "output")
TEMPLATES_DIR = os.path.join(ROOT_DIR, "templates")
FONTS_DIR = os.path.join(ROOT_DIR, "assets", "fonts")


def typst_bin():
    local = os.path.expanduser("~/.local/bin/typst")
    return local if os.path.exists(local) else "typst"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--job-description", "-j", required=True)
    parser.add_argument("--output", "-o", default=os.path.join(OUTPUT_DIR, "Billy-Rebecchi-CV-tailored.pdf"))
    parser.add_argument("--max-per-role", type=int, default=4)
    args = parser.parse_args()

    with open(args.job_description) as f:
        jd_text = f.read()

    data = load_all()
    score = score_jd(jd_text)
    jd_terms = set(score["matched"]) | set(score["missing"])

    bank = flatten(load_keywords()["groups"])
    ranked = rank_achievements(jd_terms, data["experience"])

    selected = {}
    for item in ranked:
        company = item["role"]["company"]
        bucket = selected.setdefault(company, [])
        if len(bucket) < args.max_per_role:
            bucket.append(item["achievement"])

    for role in data["experience"]:
        role["achievements"] = selected.get(role["company"], role.get("achievements", []))
        role["include_pdf"] = True

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    data_path = os.path.splitext(args.output)[0] + ".json"
    with open(data_path, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    typ_file = os.path.splitext(args.output)[0] + ".typ"
    template_rel = os.path.relpath(os.path.join(TEMPLATES_DIR, "cv.typ"), os.path.dirname(args.output))
    data_rel = os.path.relpath(data_path, os.path.dirname(args.output))
    with open(typ_file, "w") as f:
        f.write(f'#import "{template_rel}": cv\n#let data = json("{data_rel}")\n#cv(data)\n')

    result = subprocess.run(
        [
            typst_bin(), "compile",
            "--root", ROOT_DIR,
            "--font-path", FONTS_DIR,
            "--pdf-standard", "ua-1",
            typ_file, args.output,
        ],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(result.stderr, file=sys.stderr)
        return 1

    print(f"Generated: {args.output}")
    print(f"\nCoverage: {score['score']:.0f}% of the advert's bank terms")
    print(f"Matched: {', '.join(sorted(score['matched'])) or 'none'}")
    print(f"Gaps:    {', '.join(sorted(score['missing'])) or 'none'}\n")
    for company, achievements in selected.items():
        print(f"{company}:")
        for a in achievements:
            print(f"  - {a['title']}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
