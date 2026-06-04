# CV-as-Code

A CV management system that treats career history as structured data rather than a manually maintained document.

## Architecture

```
data/               YAML source-of-truth files
templates/          Typst PDF templates
scripts/            Python build and generation tools
docs/               MkDocs website pages
output/             Generated PDFs and website
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

# Build only PDFs
python scripts/build.py --pdf

# Build only website
python scripts/build.py --website
```

## Generate Specific CVs

```bash
# Full two-page CV
python scripts/generate_cv.py full

# One-page short CV
python scripts/generate_cv.py short

# Variant CV
python scripts/generate_cv.py --variant engineering-manager
python scripts/generate_cv.py --variant senior-engineer
python scripts/generate_cv.py --variant staff-engineer
python scripts/generate_cv.py --variant platform-engineer
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

## CV Variants

| Variant | Focus Areas |
|---|---|
| Senior Engineer | Architecture, technical delivery, hands-on implementation |
| Staff Engineer | Cross-team influence, technical strategy, org impact |
| Engineering Manager | Leadership, delivery, coaching, stakeholder management |
| Platform Engineer | Terraform, AWS, infrastructure, CI/CD, automation |

## CI/CD

On every push to `main`:
1. PDFs are generated from YAML data
2. Website is built with MkDocs
3. Both are deployed to GitHub Pages

## AI Support

Prompts are available in `docs/ai-prompts.md` for using LLMs to:
- Rewrite achievements
- Generate targeted summaries
- Create tailored CV variants
- Generate cover letters

Source YAML should never be modified automatically.
