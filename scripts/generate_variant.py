#!/usr/bin/env python3
"""Generate a tailored CV from a job description.

Usage:
    python scripts/generate_variant.py \\
        --job-description jd.txt \\
        --output tailored.pdf
"""

import argparse
import json
import os
import subprocess
import sys

from data_loader import load_all
from score_job import score_jd

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.join(SCRIPT_DIR, "..")
OUTPUT_DIR = os.path.join(ROOT_DIR, "output")
TEMPLATES_DIR = os.path.join(ROOT_DIR, "templates")


def rank_achievements_by_relevance(jd_keywords, experience):
    ranked = []
    for role in experience:
        roles = [role] if isinstance(role, dict) else role
        for r in roles:
            for achievement in r.get("achievements", []):
                tag_matches = sum(
                    1 for t in achievement.get("tags", [])
                    if t.lower() in jd_keywords
                )
                title_words = set(achievement["title"].lower().split())
                jd_words = set(jd_keywords.keys())
                title_matches = len(title_words & jd_words)

                score = tag_matches * 3 + title_matches * 2
                if achievement.get("impact") == "high":
                    score += 1

                ranked.append({
                    "achievement": achievement,
                    "role": r,
                    "score": score,
                })

    ranked.sort(key=lambda x: x["score"], reverse=True)
    return ranked


def select_achievements(ranked, max_per_role=3):
    selected = {}
    for item in ranked:
        company = item["role"]["company"]
        if company not in selected:
            selected[company] = []
        if len(selected[company]) < max_per_role:
            selected[company].append(item["achievement"])
    return selected


def generate_tailored_pdf(jd_text, output_path):
    data = load_all()
    score_result = score_jd(jd_text)
    jd_keywords = score_result["matched"].copy()
    jd_keywords.update(score_result["missing"])

    ranked = rank_achievements_by_relevance(jd_keywords, data["experience"])
    selected = select_achievements(ranked)

    tailored_experience = []
    for role in data["experience"]:
        roles = [role] if isinstance(role, dict) else role
        for r in roles:
            if r["company"] in selected:
                tailored = r.copy()
                tailored["achievements"] = selected[r["company"]]
                tailored_experience.append(tailored)

    if not tailored_experience:
        tailored_experience = data["experience"]

    tailored_data = data.copy()
    tailored_data["experience"] = tailored_experience

    os.makedirs(os.path.dirname(output_path) or OUTPUT_DIR, exist_ok=True)

    # Write data file
    data_path = output_path.replace(".pdf", ".json")
    with open(data_path, "w") as f:
        json.dump(tailored_data, f, indent=2)

    out_dir = os.path.dirname(output_path) or "."
    template_rel = os.path.relpath(
        os.path.join(TEMPLATES_DIR, "senior-engineer.typ"), out_dir
    )
    data_rel = os.path.relpath(data_path, out_dir)

    typst_content = f'''
#import "{template_rel}": cv
#let data = json.decode(read("{data_rel}"))
#cv(data)
'''

    typ_file = output_path.replace(".pdf", ".typ")
    with open(typ_file, "w") as f:
        f.write(typst_content)

    result = subprocess.run(
        ["typst", "compile", "--root", ROOT_DIR, typ_file, output_path],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        print(f"Error: {result.stderr}", file=sys.stderr)
        sys.exit(1)

    print(f"Generated: {output_path}")

    print(f"\nTailoring Report")
    print(f"{'=' * 40}")
    print(f"Matched skills: {', '.join(sorted(score_result['matched'].keys()))}")
    print(f"Missing skills: {', '.join(sorted(score_result['missing'].keys()))}")
    print(f"Selected achievements: {sum(len(v) for v in selected.values())} across {len(selected)} roles")

    for company, achievements in selected.items():
        print(f"\n  {company}:")
        for a in achievements:
            print(f"    - {a['title']}")


def main():
    parser = argparse.ArgumentParser(description="Generate tailored CV from job description")
    parser.add_argument("--job-description", "-j", required=True,
                        help="Path to job description text file")
    parser.add_argument("--output", "-o",
                        default=os.path.join(OUTPUT_DIR, "cv-tailored.pdf"),
                        help="Output PDF path")
    args = parser.parse_args()

    with open(args.job_description, "r") as f:
        jd_text = f.read()

    generate_tailored_pdf(jd_text, args.output)


if __name__ == "__main__":
    main()
