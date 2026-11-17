# og/

The Open Graph card for billy.rebecchi.uk/assets/og-image.png.

- `card.html` — the design. Ordinary HTML and CSS, no image generation.
- `assets/` — what the card draws: the screenshots and fonts it needs.
- `render.py` — renders `card.html` at 1200x630 and writes the image.

## Rebuilding

```bash
pip install playwright pillow
playwright install chromium

python3 og/render.py          # write the image
python3 og/render.py --check  # fail if the committed image is stale
```

`--check` renders the card again and compares it with the committed PNG, so a
change to the card that never made it into the image fails rather than ships.

If Playwright cannot download a browser, point it at one already installed:

```bash
python3 og/render.py --browser /path/to/chrome
```

## Notes

The image is 1200x630 with no alpha channel and it is written into `docs/assets/`, which mkdocs copies to the site. The card uses this repository's own fonts from `assets/fonts/`.
