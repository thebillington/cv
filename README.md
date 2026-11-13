# CV as code

Billy Rebecchi's CV. Facts live in `data/` as YAML; the two-page PDF and the
website are both generated from it, so they cannot disagree.

Aimed at senior software engineering and engineering management roles in the
UK. The design and content decisions are recorded, with the evidence behind
them, in `docs/`.

## Layout

```
data/          facts and wording (profile, skills, experience, projects, keywords)
templates/     one Typst template, cv.typ
scripts/       build, PDF checks, preview, tailoring
docs/          the website; itself generated from data/
assets/fonts/  Source Sans 3 / Source Serif 4 (SIL OFL), embedded in the PDF
```

## Build

```bash
python -m venv .venv && .venv/bin/pip install -r requirements.txt
make build          # PDF, checks, website
make pdf            # PDF and checks only
make check          # re-run the PDF gates
make preview        # page images + site screenshots for visual review
```

The build fails rather than shipping a broken PDF: wrong page count, missing
sections, contact details that do not extract, banned filler or a missing core
skill all stop it (`scripts/check_pdf.py`).

## Tailoring a CV to a job description

```bash
python scripts/score_job.py jd.txt
python scripts/generate_variant.py -j jd.txt -o output/tailored.pdf
```

Both read the keyword bank in `data/keywords.yml`. The variant build only
selects which achievements lead; it never rewrites a sentence.

## Adding or editing a role

1. Edit `data/experience/<company>.yml`.
2. Keep Billy's own wording. If something is not evidenced in the file, it does
   not go in the CV.
3. Tag achievements with the terms in `data/keywords.yml`.
4. Mark the ones that belong on the two-page PDF with `include_pdf: true`.
5. `make build`. If it no longer fits two pages, cut an older bullet rather
   than shrinking the type.

## Deploy

Push to `main`. GitHub Actions builds, runs the checks, and publishes to
Pages at <https://billy.rebecchi.uk/>. A failing check fails the deploy.
