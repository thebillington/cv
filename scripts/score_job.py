#!/usr/bin/env python3
"""Score a job description against the keyword bank.

Reports which market terms the advert uses, which of those the CV already
covers, and which are gaps. Used by generate_variant.py and for gap analysis.

Usage:
    python scripts/score_job.py jd.txt
"""

import argparse
import re
import sys

from data_loader import load_all, load_keywords


def flatten(groups):
    terms = []
    for group in groups.values():
        terms.extend(group)
    return terms


def cv_text(data):
    parts = [data["profile"]["summary"], str(data["profile"].get("highlights", []))]
    for line in data["skills"].get("core", []):
        parts.append(line)
    for cat in data["skills"].get("categories", []):
        parts.extend(cat.get("skills", []))
    for role in data["experience"]:
        parts.append(role.get("summary", ""))
        parts.extend(role.get("stack", []))
        for a in role.get("achievements", []):
            parts.append(a.get("title", ""))
            parts.append(a.get("description", ""))
    return "\n".join(parts).lower()


def rank_achievements(jd_terms, experience):
    """Score each achievement against the advert's terms.

    Tags weigh most, then words in the title, then a small nudge for the
    achievement already being marked high impact.
    """
    terms = {t.lower() for t in jd_terms}
    ranked = []
    for role in experience:
        for achievement in role.get("achievements", []):
            tag_score = sum(1 for t in achievement.get("tags", []) if t.lower() in terms) * 3
            title_words = set(achievement.get("title", "").lower().split())
            title_score = len(title_words & terms) * 2
            impact_score = 1 if achievement.get("impact") == "high" else 0
            ranked.append(
                {
                    "achievement": achievement,
                    "role": role,
                    "score": tag_score + title_score + impact_score,
                }
            )
    ranked.sort(key=lambda x: x["score"], reverse=True)
    return ranked


def score_jd(jd_text):
    bank = flatten(load_keywords()["groups"])
    lower = jd_text.lower()
    data = load_all()
    mine = cv_text(data)

    matched, missing = {}, {}
    for term in bank:
        if term.lower() not in lower:
            continue
        bucket = matched if term.lower() in mine else missing
        bucket[term] = bucket.get(term, 0) + lower.count(term.lower())

    total = len(matched) + len(missing)
    return {
        "matched": matched,
        "missing": missing,
        "score": (100 * len(matched) / total) if total else 0.0,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("jd")
    args = parser.parse_args()

    with open(args.jd) as f:
        result = score_jd(f.read())

    print(f"Coverage: {result['score']:.0f}% of the advert's bank terms\n")
    print("Covered:")
    for term in sorted(result["matched"], key=result["matched"].get, reverse=True):
        print(f"  {term} ({result['matched'][term]})")
    print("\nGaps:")
    for term in sorted(result["missing"], key=result["missing"].get, reverse=True):
        print(f"  {term} ({result['missing'][term]})")

    return 0


if __name__ == "__main__":
    sys.exit(main())
