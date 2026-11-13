# Development pipeline

This CV is built as a small product, not a one-off document. Same shape as the
sibling `nat-cv` repo, tuned for software engineering roles.

```
data/ (YAML: facts and wording)
   │
   ├── market research (keywords, titles, seniority signals)
   ├── forum validation (what practitioners object to)
   ├── design direction (type, colour, layout, ATS)
   ├── build  ──►  Typst PDF  ──►  checks  ──┐
   │        └──►  MkDocs site  ──────────────┤
   │                                          ▼
   └── review rounds (forums, voice, design) ─► fixes → rebuild
```

## Why this shape

The PDF and the site answer different questions. The PDF has to survive a
twenty-second scan and an ATS parser; the site has to survive a click from an
engineer who wants to see the work. One source of facts, two renderings, no
drift.

`data/` is the only place a claim can be added or changed. Templates do not
invent content.

## Automated gates

`scripts/check_pdf.py` runs on every build and fails it on:

- a page count other than two
- a missing section (Profile, Core skills, Experience, Education)
- contact details that do not extract from the text layer
- broken glyphs
- a banned filler phrase (`data/keywords.yml` → `avoid`)
- a term in the Core skills block that appears nowhere else in the document

It also reports keyword coverage against the market bank and warns below 35%.
That number is a rough proxy for "would this survive a keyword sift", not a
score to maximise by keyword stuffing.

## Review rounds

Reviews are independent and adversarial, and each writes a memo to
`docs/reviews/` before anything is changed.

1. **Forums**: test each document decision against practitioner sentiment
   (Reddit, HN, recruiter guidance) rather than taste.
2. **Market and seniority**: read as the hiring manager; is the scope visible,
   does it read senior, does it answer "why is an ex-EM applying for this".
3. **Design and extraction**: type, spacing, print, ATS extraction, mobile
   layout and accessibility.

## Tailoring

`scripts/score_job.py` scores an advert against the keyword bank;
`scripts/generate_variant.py` picks the most relevant achievements per role and
renders the same template. Neither rewrites a sentence.

## Adding a role or achievement

1. Edit `data/experience/<company>.yml`.
2. Use Billy's wording. No claim that is not already evidenced there.
3. Tag it with terms from `data/keywords.yml`.
4. Decide whether it earns a place on the two-page PDF (`include_pdf: true`);
   everything else still appears on the site.
5. `make build`. Over two pages means cutting a bullet, not shrinking type.
