#!/usr/bin/env python3
"""Score a job description against the CV.

Analyses a job description, extracts keywords, and scores how well the
current CV matches. Used by generate_variant.py and for gap analysis.

Usage:
    python scripts/score_job.py jd.txt
"""

import argparse
import re
import sys

from data_loader import load_all, load_skills, load_experience


SKILL_KEYWORDS = [
    "typescript", "python", "kotlin", "java", "go", "ruby", "sql",
    "react", "next.js", "node.js", "express", "fastapi", "graphql",
    "rest", "postgres", "redis",
    "android", "jetpack compose", "compose multiplatform",
    "aws", "terraform", "docker", "kubernetes", "ci/cd", "github actions",
    "serverless", "ecs", "rds", "lambda", "cloudfront",
    "architecture", "microservices", "migration", "platform",
    "leadership", "management", "team building", "stakeholder",
    "agile", "scrum", "okr",
    "testing", "automation", "devops", "security",
    "frontend", "backend", "api", "full stack",
]


def extract_keywords(text):
    """Extract relevant keywords from job description text."""
    text_lower = text.lower()
    found = {}
    for keyword in SKILL_KEYWORDS:
        pattern = re.compile(re.escape(keyword), re.IGNORECASE)
        matches = pattern.findall(text_lower)
        if matches:
            found[keyword] = len(matches)
    return found


def load_skill_set():
    """Return a flat set of all skills from the CV."""
    skills = load_skills()
    skill_set = set()
    for cat in skills["categories"]:
        for s in cat["skills"]:
            skill_set.add(s.lower())
    return skill_set


def load_achievement_tags():
    """Return all tags used across achievements."""
    experience = load_experience()
    tags = set()
    for role in experience:
        roles = [role] if isinstance(role, dict) else role
        for r in roles:
            for a in r.get("achievements", []):
                for t in a.get("tags", []):
                    tags.add(t.lower())
    return tags


def score_jd(jd_text):
    """Score a job description against the CV."""
    jd_keywords = extract_keywords(jd_text)
    my_skills = load_skill_set()
    my_tags = load_achievement_tags()

    matched = {}
    missing = {}
    for keyword, count in sorted(jd_keywords.items(), key=lambda x: x[1], reverse=True):
        if keyword in my_skills or keyword in my_tags or keyword.replace("/", "").replace("-", "").replace(" ", "") in {s.replace("/", "").replace("-", "").replace(" ", "") for s in my_skills}:
            matched[keyword] = count
        else:
            missing[keyword] = count

    return {
        "total_keywords": len(jd_keywords),
        "matched": matched,
        "matched_count": len(matched),
        "missing": missing,
        "missing_count": len(missing),
        "match_rate": len(matched) / len(jd_keywords) * 100 if jd_keywords else 0,
    }


def main():
    parser = argparse.ArgumentParser(description="Score a job description against CV")
    parser.add_argument("job_description_file", help="Path to job description text file")
    parser.add_argument("--verbose", "-v", action="store_true", help="Show detailed output")
    args = parser.parse_args()

    with open(args.job_description_file, "r") as f:
        jd_text = f.read()

    result = score_jd(jd_text)

    print(f"Job Description Analysis")
    print(f"{'=' * 40}")
    print(f"Total keywords found: {result['total_keywords']}")
    print(f"Matched: {result['matched_count']}")
    print(f"Missing: {result['missing_count']}")
    print(f"Match rate: {result['match_rate']:.1f}%")
    print()

    if result["matched"]:
        print("Matched Skills:")
        for k, v in sorted(result["matched"].items()):
            print(f"  \u2713 {k} (x{v})")

    if result["missing"]:
        print()
        print("Missing Skills:")
        for k, v in sorted(result["missing"].items()):
            print(f"  \u2717 {k} (x{v})")

    return result


if __name__ == "__main__":
    main()
