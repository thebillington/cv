# Round 3 — ATS and accessibility review

Run against the PDF with pdftotext (plain, -layout, -raw, -bbox), pdfinfo,
pdffonts and qpdf. Findings are about extraction, not content.

## Verdict

"Technically the strongest CV of the three rounds on the accessibility side, and
middling on the ATS side." Tagged structure tree is real (H1 + five H2s, list
structure, bookmarks), every font is embedded and Unicode-mapped, links are real
annotations with descriptions, no text is an image, contrast passes AA.

The ATS problems were extraction-order problems, all fixable in layout.

## Findings accepted

| # | Finding | What changed |
|---|---|---|
| 1 | Section numerals sat on the heading line, so a layout-aware parser sees `EXPERIENCE            03` | Numerals removed; headings are exactly `SUMMARY`, `SKILLS`, `EXPERIENCE`, `EDUCATION`, `OPEN SOURCE`, alone on the line |
| 2 | Dates were emitted between employer and title, and inconsistently by role | Dates now share the title's baseline for every role: employer → title → dates |
| 3 | Education institutions were emitted after both degrees, detached | Each entry is a single line: degree, institution, grade, dates |
| 4 | The folio was extracted between two bullets | Folio removed |
| 5 | `PROFILE` and `CORE SKILLS` are not the strings parsers look for | Renamed to `SUMMARY` and `SKILLS` |
| 6 | 7.6–8.2pt metadata is small for low vision; the stack line is the keyword line | Body 9.8pt, dates/contact 8.4pt, stack 7.9pt |
| 7 | `present` lowercase in dates | Rendered as `Present` |
| 8 | Website address extracts without a scheme | Left as the visible text `billy.rebecchi.uk` (the annotation carries `https://`); accepted risk |

## Checks that passed already

- Email, phone and location survive extraction and sit in the body, not a header.
- Bullets are U+2022, middots U+00B7, no soft hyphens, no broken glyphs.
- Six fonts, all embedded, subset, with ToUnicode.
- `/MarkInfo Marked true`, structure tree populated, `/Lang en-GB`, tab order set.
- Links: tel, mailto, site, GitHub, LinkedIn and two project links, each with a
  readable `/Contents` string.
- Contrast: body 17:1, navy 13:1, slate 9:1, accent 5.5:1 (AA, not AAA). The
  accent is now used only for the subtitle and skill labels.

## Left as is

- `/Subject` is absent from the metadata (title, author and keywords are present).
  Adding it needs a Typst document property that is not exposed; not worth a
  template fork for one field.
- `pdfinfo` prints a benign warning about `/MarkInfo /Suspects`; `qpdf --check`
  reports no syntax or stream errors.
