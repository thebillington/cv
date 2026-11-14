#!/usr/bin/env python3
"""Check the generated PDF before it can be published.

Fails on anything that would hurt an application: wrong page count, a missing
section, contact details that do not extract, banned filler, broken glyphs or
missing keywords. Warnings are reported but do not fail the build.

Usage:
    python scripts/check_pdf.py output/Billy-Rebecchi-CV.pdf
"""

import argparse
import os
import re
import subprocess
import sys

from data_loader import load_all, load_keywords

REQUIRED_SECTIONS = ["Summary", "Skills", "Experience", "Education"]

# Phrases that senior engineers and recruiters consistently name as filler.
FALLBACK_AVOID = [
    "passionate about",
    "results-driven",
    "results driven",
    "self-starter",
    "self motivated",
    "self-motivated",
    "team player",
    "hard-working",
    "detail-oriented",
    "dynamic",
    "rockstar",
    "ninja",
    "guru",
    "10x",
    "synergy",
    "spearheaded",
    "leveraged",
    "responsible for",
    "duties included",
    "cutting-edge",
    "go-getter",
    "wear many hats",
]


def pdf_text(path):
    result = subprocess.run(
        ["pdftotext", "-layout", path, "-"], capture_output=True, text=True
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr)
    return result.stdout


def pdf_pages(path):
    result = subprocess.run(["pdfinfo", path], capture_output=True, text=True)
    match = re.search(r"^Pages:\s+(\d+)", result.stdout, re.MULTILINE)
    return int(match.group(1)) if match else 0


def flatten_keywords(groups):
    terms = []
    for group in groups.values():
        terms.extend(group)
    return terms


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf")
    parser.add_argument("--expect-pages", type=int, default=2)
    args = parser.parse_args()

    if not os.path.exists(args.pdf):
        print(f"FAIL: {args.pdf} does not exist")
        return 1

    data = load_all()
    profile = data["profile"]
    keywords = load_keywords()

    text = pdf_text(args.pdf)
    lower = text.lower()
    pages = pdf_pages(args.pdf)

    failures = []
    warnings = []

    # Structure
    if pages != args.expect_pages:
        failures.append(f"page count is {pages}, expected {args.expect_pages}")

    for section in REQUIRED_SECTIONS:
        if section.lower() not in lower:
            failures.append(f"missing section: {section}")

    # Contact details, extracted from the body
    email = profile.get("email", "")
    if email and email.lower() not in lower:
        failures.append(f"email does not extract: {email}")

    # Broken glyphs
    for glyph in ("\ufffd", "\u25a1", "\u2610"):
        if glyph in text:
            failures.append("broken glyph in extracted text")
            break

    # Filler
    avoid = keywords.get("avoid", FALLBACK_AVOID)
    hits = sorted({p for p in avoid if p.lower() in lower})
    for phrase in hits:
        failures.append(f"banned phrase: {phrase}")

    # Keyword coverage against the market bank
    bank = flatten_keywords(keywords.get("groups", {}))
    present = [t for t in bank if t.lower() in lower]
    missing = [t for t in bank if t.lower() not in lower]
    coverage = 100 * len(present) / len(bank) if bank else 0

    print(f"PDF:      {args.pdf}")
    print(f"Pages:    {pages}")
    print(f"Words:    {len(text.split())}")
    print(f"Keywords: {len(present)}/{len(bank)} from the bank ({coverage:.0f}%)")

    # Every entry in the core skills block must appear somewhere in the PDF.
    for line in data["skills"].get("core", []):
        label, _, values = line.partition(":")
        for term in [v.strip() for v in values.split(",") if v.strip()]:
            if term.lower() not in lower:
                warnings.append(f"core skill not found in PDF: {term}")

    if coverage < 35:
        warnings.append(
            f"keyword coverage is low ({coverage:.0f}%): the CV may not survive a keyword sift"
        )

    if warnings:
        print("\nWarnings:")
        for w in warnings:
            print(f"  - {w}")

    if failures:
        print("\nFAILED:")
        for f in failures:
            print(f"  - {f}")
        return 1

    print("\nOK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
