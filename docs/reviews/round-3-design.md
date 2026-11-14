# Round 3 — design review

Typographer, working from 110 dpi renders (4.333 px/mm). Measurements converted
back to points, ±0.5pt.

## Verdict

"The identity system is coherent and the body rhythm is regular; the pagination
is broken and three details undo the 'engineered' claim."

Hierarchy read cold: name ✓, employer ✓, dates weak, **job title identical to
body text** ✗, section starts ✓.

## Findings accepted

| # | Finding (measured) | What changed |
|---|---|---|
| 1 | Page 1 was 97.6mm empty (64% full) and the Pion role was cut 1/5 across the break | Margins and type size increased; the break now falls before the role, so page 2 opens with a complete Pion entry |
| 2 | Measure was 175.4mm at 118–124 characters per line, leading ratio 1.24 | Margins 17→21mm, body 9.5→9.8pt, leading ratio ≈1.3. Measure now ~150mm |
| 3 | Job title set at body size in body colour | Title now 10.2pt semibold on its own line above the stack; employer 11pt bold navy |
| 4 | Skills values started at seven different x positions (24px stagger) | Labels are a fixed 6.6em column; every value aligns |
| 5 | Dates shared size and grey with the stack line | Dates 8.4pt slate; stack 7.9pt muted — two sizes, two greys |
| 6 | Section numbers collided with date column and resumed as "04" on page 2 | **Numerals removed entirely** (also fixes the ATS finding), not moved |
| 7 | Contact block at 1.15 leading with three separator conventions | 8.4pt with wider spacing; middots removed from contact, kept in stacks |
| 8 | Bullets had no inter-item space | 0.36em between items, 8pt before the list |
| 9 | Folio 6mm from trim, outside the frame, landing mid-bullet | Removed |
| 10 | Mobile skills wrapped back to the left margin, losing label ownership | Hanging indent in CSS; wrapped values align under the value column |
| 11 | Desktop measure ~120 characters | Prose capped at 68ch |

## Findings declined

| # | Finding | Why |
|---|---|---|
| 1 | Add a running head on page 2 | Adds furniture to a two-page document; the folio removal already fixed the parsing issue |
| 2 | Abbreviate months ("Sep 2016 – Jul 2017") | Full months are unambiguous for parsers and read better in his own CVs |
| 3 | Move the numbers to the left rather than delete them | Deleted: the ATS review showed the numerals on the heading line break exact-match parsers |
| 4 | Two-row mobile button grid | Keeps four full-width targets; last round's instruction was that mobile buttons must be even and centred |

## Kept deliberately

Serif name; mono label over a hairline rule; mono stack lines; the colour system
(three hues, all ≥4.5:1, survives greyscale); right-aligned dates; bold lead-in
bullets; 17px mobile body.
