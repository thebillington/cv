# Round 2 - responses

What was done in response to `round-1-forums.md`, and what was deliberately not
done. Order follows the memo's closing list.

| Recommendation | Response |
|---|---|
| Two pages, page one is the whole story | **Done.** Two pages; the first carries profile, skills, the current role and the previous one; page two is the earlier history, education and open source |
| Profile in two or three sentences | **Done.** Cut from five lines to two sentences (43 words). The ISO 27001 and migration detail moved into the roles, where it belongs |
| Impact plus mechanism in every bullet | **Already true, tightened.** Each bullet names the system and then what changed; "three brands" and "every three days" are the only numbers, and both are measurable |
| Prune the skills block | **Done.** Six grouped lines: languages, frontend, backend, platform, mobile, practice. No soft-skill tail, no tool list |
| Pick one target and re-sound the document | **Done.** Senior software engineer is the target; the management history is carried as scope (squads, ISO 27001, DORA) rather than as the pitch, and the profile explains the return to hands-on delivery in one clause |
| Employer with real titles and dates | **Kept as two entries.** The second Pion role keeps its own title and dates rather than being nested under one Pion header. Every date is honest, and right-aligned chronology was the thing the same threads asked for; nesting would save a line but make the dates ragged |
| Copy-paste test | **Passed.** `pdftotext` returns sections in order, with company, title and dates together. The build embeds fonts and disables hyphenation so nothing splits |
| Decide whether the GitHub link earns its place | **Kept, with a condition.** The link stays because the open-source section names two presentable repositories (a game engine and a packaging tool). The pinned repos are the thing to maintain, not the link |
| AI only as shipped systems with outcomes | **Done.** AI appears as MCP servers, a local model delegation, an adoption policy and a token-spend reduction, inside the current role. There is no "AI enthusiast" framing |

## What was not taken

- **A one-page CV.** The r/ExperiencedDevs dissent is a volume argument, and
  this history has a management chapter that earns its space.
- **Dropping the profile entirely.** Two sentences answering "why is an ex-EM
  applying for an IC role" is worth more than the four lines it replaced.
- **Removing colour.** No retrieved source penalises a two-colour document, and
  the steel accent is the only thing separating sections. It survives greyscale
  and a photocopy.
- **Splitting the document into IC and EM variants.** The tailoring script can
  produce a role-weighted variant on demand; two maintained truths would drift.

## Numbers added and removed

The source data contained almost no metrics, and none were invented. What is on
the page is what was already claimed: three brands (migration validation), three
days (token rotation), seven years, four years of management, one two-page CV.
Where a number would strengthen a bullet but is not known (team size at Pion,
number of services in the monorepo, incident MTTR), it was left out.
