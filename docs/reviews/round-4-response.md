# Round 4 — response

Four reviewers ran independently against the same artefacts: the PDF text, the
extracted plain text, both page renders and two site screenshots. Memos are
`round-3-voice.md`, `round-3-hiring.md`, `round-3-design.md`,
`round-3-ats.md`. This is what was applied.

## Changed

**Structure and parsing**
- Section numerals removed. Headings are now the exact strings a parser looks
  for: `SUMMARY`, `SKILLS`, `EXPERIENCE`, `EDUCATION`, `OPEN SOURCE`.
- Dates moved onto the title line, so every role extracts employer → title →
  dates, consistently.
- Education is one line per entry, so the institution can never detach from the
  degree.
- Page folio removed: it was landing between two bullets in extraction, and a
  two-page document does not need page numbers.
- `present` renders as `Present`.

**Type and layout**
- Margins 17 → 21mm; body 9.5 → 9.8pt with a 1.3 leading ratio. The measure was
  running to 118–124 characters; it is now ~95.
- Job title separated from body text: 10.2pt semibold on its own line.
- Skills values now align on a fixed 6.6em label column.
- Dates at 8.4pt slate, stack lines at 7.9pt muted: two sizes, two greys.
- Bullets get 0.36em between items and 8pt before the list.
- The page break now falls before the Pion entry, so page 2 opens with a whole
  role instead of an orphaned bullet.

**Prose**
- Removed "rather than assumed", "within reach", "made bottlenecks visible",
  "rather than hopeful".
- Restored the runbook clause, so the profile's claim is evidenced.
- "raw sockets" → "TCP sockets".
- "accountable for delivery against product strategy" → "leading delivery and
  aligning feature work with long-term business goals".
- "(Game Engineering)" restored on the degree.

**Site**
- Prose capped at 68ch rather than the full 921px column.
- Skills rows hang-indent, so wrapped values stay under their label.

## Not changed, and why

- **"16 million requests per day"** — three reviewers called it unsourced. It
  came from Billy directly in this thread; their source set could not contain it.
- **MCP servers, the AI standard, the API-change tooling, the PHP removal** —
  same: all four are in the appraisal Billy attached, which the reviewers did not
  have.
- **Paperound, OCR moderation, Nottingham Trent** — excluded by Billy.
- **A paragraph explaining the move from management back to IC** — the hiring
  reviewer wanted it; Billy asked for plain and short.
- **Abbreviated months, a page-2 running head, a two-row mobile button grid** —
  declined as furniture.
