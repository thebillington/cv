# Voice guide

The CV has to sound like Billy explaining what he built, not like a CV writer.
The existing YAML was already written in his register; this file records what
that register is so future edits do not sand it off.

## Rules

1. **Concrete verbs first.** Built, wrote, moved, replaced, led, cut, mapped,
   traced. Avoid nominalisations ("the delivery of", "the optimisation of").
2. **Name the thing.** `Terraform`, `Auth0`, `JWT claims`, `Iglu schemas`,
   `Room`, `OkHttp`, `SST`, `GitLab API`. Specific nouns are the evidence; if a
   sentence needs a category word ("platform", "systems") it also needs the
   concrete thing beside it.
3. **State the mechanism, then the effect.** "Replaced SSO tokens with
   ephemeral GitHub Actions tokens, removing a manual rotation step that had to
   happen every three days" beats "improved CI/CD security".
4. **No first person in the PDF.** The site may use it, because the site is a
   conversation.
5. **British English.** Modernise, prioritise, organisation, behaviour.
6. **Tense.** Present for the current role's summary, past for everything
   finished, including the current role's achievements.
7. **Never invent a number, a framework or a qualification.** The figures in the
   CV are the ones already in `data/`: three brands, three days, seven years,
   three and a half years, two pages. If a number would help but is not known,
   leave it out rather than estimate.
8. **Trim by deletion.** If a sentence is too long, delete a clause. Do not
   replace his words with synonyms: the wording is the evidence of how he
   writes.

## Words he actually uses

| Phrase | Why it stays |
|---|---|
| "extracted ... from a legacy monorepo" | precise, and it is the work |
| "endpoint parity suite" | the actual testing approach, not "testing" |
| "runbook other engineers now use" | evidence of leverage, not a claim about it |
| "dropped the deprecated nullable fields" | the mechanism is the story |
| "blameless post-mortems" | his term, and a real practice |
| "known-good baseline" | how he describes templates |

## Test

Read a bullet aloud. If it could sit on any engineer's CV in any company, it has
failed: either name the system, or cut it.
