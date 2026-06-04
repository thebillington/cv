# CV-as-Code

A CV management system that treats career history as structured data rather than a manually maintained document. Both the PDF and website are generated from the same YAML source files.

## Architecture

```
data/               YAML source-of-truth files
templates/          Typst PDF template
scripts/            Python build and generation tools
docs/               MkDocs website templates (Jinja2)
output/             Generated PDF and website
.github/workflows/  CI/CD pipeline
```

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Install Typst (macOS)
brew install typst

# Build everything
python scripts/build.py

# Build only PDF
python scripts/build.py --pdf

# Build only website
python scripts/build.py --website
```

Output: `output/cv-billy-rebecchi.pdf` and website at `output/site/`.

## Generate CV

```bash
python scripts/generate_cv.py
```

## Tailor CV from Job Description

```bash
python scripts/generate_variant.py \
  --job-description path/to/job-description.txt \
  --output output/cv-tailored.pdf
```

## Score a Job Description

```bash
python scripts/score_job.py path/to/job-description.txt
```

## Data Model

Each role in `data/experience/` contains:

```yaml
company: Company Name
title: Job Title
start: YYYY-MM
end: YYYY-MM or "present"

summary: >
  Brief description of the role.

achievements:
  - title: Achievement title
    description: Detailed description
    impact: high|medium|low
    tags:
      - architecture
      - leadership
      - terraform
```

## CI/CD

On every push to `main`:
1. PDF is generated from YAML data
2. Website is built with MkDocs (pulling content from YAML via macros plugin)
3. Both are deployed to GitHub Pages

## AI Support

Prompts are available in `docs/ai-prompts.md` for using LLMs to:
- Rewrite achievements
- Generate summaries
- Write cover letters

Source YAML should never be modified automatically.
