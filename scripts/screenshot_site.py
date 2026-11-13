#!/usr/bin/env python3
"""Screenshot the built website for visual review.

Usage:
    python scripts/screenshot_site.py            # desktop, every page
    python scripts/screenshot_site.py --mobile   # 390px, every page
"""

import argparse
import os
import sys

from playwright.sync_api import sync_playwright

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.join(SCRIPT_DIR, "..")
OUT = os.path.join(ROOT_DIR, "output", "preview")

PAGES = {
    "index": "index.html",
    "experience": "experience/index.html",
    "projects": "projects/index.html",
    "skills": "skills/index.html",
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--width", type=int, default=1280)
    parser.add_argument("--height", type=int, default=900)
    parser.add_argument("--mobile", action="store_true")
    parser.add_argument("--page", default=None, help="one of: " + ", ".join(PAGES))
    args = parser.parse_args()

    os.makedirs(OUT, exist_ok=True)
    pages = {args.page: PAGES[args.page]} if args.page else PAGES

    with sync_playwright() as p:
        browser = p.chromium.launch()
        if args.mobile:
            ctx = browser.new_context(
                viewport={"width": 390, "height": 844}, device_scale_factor=2
            )
        else:
            ctx = browser.new_context(
                viewport={"width": args.width, "height": args.height}
            )
        page = ctx.new_page()
        for name, rel in pages.items():
            url = "file://" + os.path.join(ROOT_DIR, "output", "site", rel)
            suffix = ".mobile" if args.mobile else ""
            out = os.path.join(OUT, f"site-{name}{suffix}.png")
            page.goto(url)
            page.wait_for_timeout(250)
            page.screenshot(path=out, full_page=True)
            print(out)
        browser.close()

    return 0


if __name__ == "__main__":
    sys.exit(main())
