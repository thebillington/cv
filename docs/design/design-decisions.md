# Design decisions

The evidence is in `docs/research/design-research.md`; this file records what
was built and why.

## The one decision

A senior engineer's CV is read as a work sample. It should look like something
an engineer would ship: one column, tight typography, no decoration that has to
be parsed or ignored. Every choice below follows from that.

## Type

- **Source Serif 4** (SIL OFL) for the name only. One serif accent gives the
  document a masthead without turning the body into a magazine.
- **Source Sans 3** (SIL OFL) for everything else: narrow enough to fit a lot of
  evidence at 9.5pt, and unambiguous for `l`, `I` and `1`, which matters in a
  document full of `l`/`1` noise like `LLM`, `ISO 27001`, `GitLab`.
- Both statically instanced at 400/600/700 and embedded, so the PDF renders
  identically on every machine and in every viewer.
- No italics. No hyphenation, so `Terraform` and `TypeScript` never split.

## Colour

| Role | Hex | Contrast on white |
|---|---|---|
| Body | `#1B1B1B` | 16.9:1 |
| Navy (name, employer, headings) | `#14314E` | 12.9:1 |
| Steel (title line, rules, bullets) | `#2A6F97` | 6.3:1 |
| Slate (dates, stack, meta) | `#3F4A56` | 8.7:1 |

Colour is never the only carrier of meaning and the whole document survives a
greyscale photocopy. The palette is deliberately not a company's brand colours:
a CV in an employer's colours reads as over-eager.

## Layout

- A4, 18mm sides, 13mm top, 12mm bottom.
- Employer first, then title, then the stack, then the evidence. Recruiters scan
  for the company; engineers scan for the stack; the bullet is where the work is.
- Dates right-aligned on the employer line, so chronology can be scanned down
  one edge.
- The stack line is the ATS surface: plain, comma-separated, no logos.
- Role headers are blocks that stay with their first bullets, but the bullets
  themselves can break across a page, so no role leaves a hole behind it.
- The footer is a page number only, marked as an artefact so a screen reader
  does not announce it.

## What is deliberately left out

- Photo, date of birth, nationality, marital status, full address.
- Skill bars, dot ratings, icons, sidebars, timelines, tag clouds.
- "References available on request", hobbies, interests.
- A separate tools list: the tools that matter appear inside the work that used
  them, and in the stack line.
- Any claim not already in `data/`.

## Website

Same YAML, same palette, same type. The site carries the full history
(including achievements held back from the two-page PDF), the project detail,
and a download button for the PDF. It is a place to send someone who asks for
more, not a second CV.
