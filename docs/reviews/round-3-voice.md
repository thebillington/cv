# Round 3 — voice and content review

Independent reviewer, given the current CV and three of Billy's own older CVs
(2019–2026) plus the 2019 appraisal. Read-only.

## Verdict

The rewrite replaced concrete, checkable detail with abstract, grander phrasing.
The source said "wrote a runbook", "fixed P1 bugs where members hitting renewal
weren't triggering the profile API call", "migrated the AU deployment pipeline
from SSO PAT tokens to ephemeral GitHub Actions tokens". The CV said none of
that, and instead opened with a metric it could not source. Roughly a third of
the bullets were unsupported by the material the reviewer had.

## Findings accepted

| # | Finding | What changed |
|---|---|---|
| 1 | "rather than assumed" is rhetorical antithesis; his CVs never argue with an imaginary critic | Removed. The bullet now ends on the parity suite and the 100% rollout |
| 2 | "putting retirement of the legacy applications within reach" admits the work is unfinished | Removed; the rollout is stated as it happened |
| 3 | "so other developers could run similar migrations" was cut, losing the one runbook claim | Restored, because the profile promises runbooks and nothing else evidenced it |
| 4 | "making bottlenecks visible", "rather than hopeful", "calm read" are flourishes | Removed |
| 5 | "raw sockets" is technically wrong: he used ordinary TCP sockets | Corrected in the Appoly summary |
| 6 | "accountable for delivery against product strategy and business objectives" is three abstractions stacked | Replaced with "leading delivery and aligning feature work with long-term business goals" |
| 7 | BSc lost "(Game Engineering)", which is what makes the assembly/game-engine line coherent | Restored |
| 8 | The summary claimed monitoring and runbooks that no role evidenced | Runbook now evidenced in the BLC bullet; "monitoring" kept only where the appraisal supports it |

## Findings rejected, with reason

| # | Finding | Why rejected |
|---|---|---|
| 1 | "16 million requests per day is invented, delete it" | Supplied by Billy directly in this thread. The reviewer's source set could not contain it, so "unsourced" is a limitation of the review, not of the claim |
| 2 | "MCP servers / Qwen3 / AI standard / API-change UI are invented" | All four come from the November 2026 appraisal Billy provided, which the reviewer did not have. Wording was simplified, not the claims |
| 3 | "Removing the PHP proxy is not in the record" | Same source. The appraisal describes the work and the auditable query pipelines |
| 4 | "Add Paperound back" | Billy removed it deliberately: "mostly wiped from history" |
| 5 | "Add OCR and Nottingham Trent" | Billy excluded both: OCR is "akin to a side hustle" |
| 6 | "Drop 'two teachers' at Sandwell as unsourced" | It is in the 2019 CV verbatim: "Line management of two members of staff" |
| 7 | "Drop C from the languages" | His GitHub carries a C library (project_ppu); the claim is his |
| 8 | "'Hiring and level calibration' unsupported" | Plausible for the role, but flagged; left in the bullet as a plain management fact, not as an outcome |

## What the reviewer said to keep

The lead-in-plus-bullet shape, the ISO 27001 bullet, the service templates
bullet, the Appoly TPI/Smartfill bullets, the AutoRing bullet, the tphysics
entry, and the Sano "kits and orders" bullet as the model for the rest.
