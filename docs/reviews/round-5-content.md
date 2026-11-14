# Round 5 — four content reviews

Four independent readers, same artefacts, each with the owner brief (his own
words on the member platform, the corrections, and the exclusions) so they were
judging the writing rather than re-litigating facts.

| Reviewer | Lens | Verdict |
|---|---|---|
| A | UK hiring manager, senior IC | "Hireable, with one structural problem and one credibility problem" — the level story contradicts itself, and the best evidence is buried |
| B | Voice editor | "Fails on sentence shape more than vocabulary" — claim-then-restate bullets are a consulting-deck shape he has never written |
| C | Backend/platform engineer | "Substitutes nouns for mechanisms" — everything is coherent, but half the bullets answer *what did you own* and dodge *how did it work* |
| D | Technical recruiter | "Not as-is" for a backend brief; the keyword block is missing families he can actually evidence |

## Where all four agreed

1. **The level story.** Headline says Senior; the current title is Full Stack
   Engineer; the four years before that are management. Nobody explains the move,
   and it is the first thing a screener does arithmetic on.
2. **"Removing the legacy PHP proxy"** — the only gerund bullet in a past-tense
   list, and the weakest verbs ("aligned", "supported") on a strong fact.
3. **The 16M figure appears twice**, once in the summary and once in the role,
   and is unqualified (peak or average, which path).
4. **The AI bullets take two of six slots** in the current role; A and D both
   wanted them merged or demoted.

## Applied

- Summary rewritten: seven years in software, four managing, and since 2026 the
  member data platform. No "7+ years across Android, web and backend" claim, no
  second 16M, and native mobile demoted from the lead.
- Role summary in his own shape: owns member data from signup through
  eligibility to login and renewals; names the store, the service and Auth0;
  16M via API Gateway and serverless Lambdas; retention, right to erasure and
  subject access requests, S3 retention for uploads.
- `Removing` → `Removed`.
- `Terraform and HCL` → `Terraform (HCL)`.
- `automated testing` → `contract and parity testing` (the two things he can
  actually point at).
- "right-to-be-forgotten" → "GDPR right to erasure" (the statutory term).

## Open, needs his answer

| Question | Why it matters |
|---|---|
| Which store holds what? (Postgres = member records, Dynamo = eligibility lookups, Valkey = cache?) | C's strongest point: the three stores are listed but never used, and a panel asks "which store?" immediately. One clause fixes it, but it has to be true |
| 16M: peak or average, and which path? | C: ~185 rps average is unremarkable; naming the hot path makes the number credible |
| How was the cutover staged? | "100% of traffic without a rollback" is only impressive if the reader knows the rollback was possible and what it cost |
| Squad size at Blue Light Card | A, D: the reader cannot calibrate seniority without it |
| Docker / containers, yes or no? | D: the largest ATS gap for backend briefs; do not claim it if it is not real |
| First person or implied? | B argues his own CVs say "I am a Full Stack Software Engineer"; everything else in the PDF is implied. Pick one |
| Add the P1 renewal bug back? | A: the only senior-IC incident evidence available, currently missing |

## Declined

- B's full rewrite of every bullet into two-sentence form: it would lengthen the
  document, and the user has asked for short.
- D's merge of both AI bullets into one: they are recent, real and distinctive;
  merging loses the Qwen3 detail that makes them credible.
- A's suggestion to name the return-to-IC motive: that is an interview line, not
  a CV line.
