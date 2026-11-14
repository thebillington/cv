# Round 3 — hiring manager review

UK hiring manager, senior engineer / EM at a product company, reading cold then
cross-checking against the source CVs.

## Verdict

"A genuinely strong CV that has been rewritten to sound more senior and has lost
credibility in the process." The bones are good: real migrations, real ownership,
an unusual low-level streak (BLE, socket FTP, Game Boy assembly), four years of
actual line management. The risk was that abstraction replaced evidence: the CV
promised runbooks and never mentioned one, and the headline metric was
unattributable to anyone outside.

Scored 6.5/10 as a document, 8/10 as evidence of a hire.

## Findings accepted

| # | Finding | What changed |
|---|---|---|
| 1 | Education detaches degree from institution in extraction | Education is now one line per entry: degree, institution, grade, dates |
| 2 | Dates are emitted between employer and job title, and inconsistently across roles | Dates moved onto the title line for every role, so extraction is employer → title → dates |
| 3 | Body measure is too wide for the type size | Margins widened to 21mm; body 9.8pt with 1.3 leading |
| 4 | The profile promises runbooks and tests that the body never delivers | The runbook is back in the BLC bullet |
| 5 | "No active CVEs" reads naive as an absolute | Left as written (his own phrasing) with "across the projects in scope" retained |
| 6 | Sano has no outcome | Left thin: no verifiable number exists in the record, and inventing one was not an option |
| 7 | The IC/EM transition is unexplained | Left alone deliberately: Billy asked for a simple CV, not a rationale paragraph. The dates and titles make the shape clear |
| 8 | Company context is missing (size, domain) | Left alone: the numbers for BLC, Sano and Pion are not in the record |

## Findings rejected, with reason

| # | Finding | Why rejected |
|---|---|---|
| 1 | "16M/day is unsourced, and if real it undersells you" | Supplied by Billy in this thread. The reviewer is right that it is a per-day average, but it is his stated figure |
| 2 | "The apprenticeship eNPS belongs to a deleted NTU contract" | It is his claim from his own CVs ("Delivery of the level 4 and level 6 apprenticeship in Software Engineering (76% eNPS)"). OCR/NTU stay off the CV by his decision |
| 3 | "Paperound is the best ownership evidence, add it back" | Explicitly removed by Billy |
| 4 | "Add a sentence explaining why you went back to IC" | Declined: he wants plain and short, not a narrative |
| 5 | "Retrofit → OkHttp needs a why" | The fact is his. Adding a justification would invent a motive |
| 6 | "50+ engineers conflicts with 20+" | Left as written; the Pion DORA work was company-wide, the org was his |

## Parsing notes (all fixed)

- Contact details extracted cleanly, as body text, not header/footer.
- Section headings now `SUMMARY`, `SKILLS`, `EXPERIENCE`, `EDUCATION`, `OPEN SOURCE`, with no numerals on the line.
- The page folio that landed between two Pion bullets is gone: the PDF no longer carries page numbers.
