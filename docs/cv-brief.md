# CV brief

The plan and the rules. Written before further edits, so decisions stop being
re-litigated mid-build.

## Target

Senior individual contributor, full-stack/backend, UK. AI-enabled is a stated
part of the positioning, not a hedge. Open to engineering management where the
role is hands-on.

## Voice

- First person in the summary and in each role summary. Implied subject in
  bullets, as in the 2019–2026 CVs.
- No self-description adjectives ("passionate", "results-driven", "calm read").
- His phrasing wins over mine. If a sentence has to change, delete a clause
  rather than paraphrase.
- No rhetorical contrasts ("rather than assumed", "within reach").

## Facts that are true and not in the older CV files

- The member data platform: signup, eligibility, login and renewals; private
  member data store, member service, Auth0; 16 million requests per day through
  API Gateway and Lambda.
- Retention, GDPR right to erasure, subject access requests, S3 retention for
  member document uploads.
- Squad of 10 engineers and 2 QE; now leads a pod of two full-stack and four
  mobile engineers, no title change.
- The PHP CVE response: PHP 7.3 with no upgrade path, 29 hours, members moved
  off the PHP database proxy onto the admin backend service via Lambda-to-Lambda
  calls, PHP switched off; auth route removed from the web app and monorepo, the
  reverse proxy disabled.
- The legacy app switch-off: Cognito and PHP sign-ins migrated to Auth0, CRM
  comms, automated password resets; the enabler of the PHP cutover.
- Terraform and HCL, Terraform Cloud, GitHub Actions to AWS and Cloudflare, OIDC
  between GitHub Actions, AWS and Terraform Cloud, Docker (partial), Postgres,
  DynamoDB, Valkey, Flutter.

## Excluded by decision

Paperound, OCR moderation, Nottingham Trent lecturing, Ecoworks trusteeship,
CoderDojo. The internal HoE document is not used and its disputes are not quoted.

## Page budget (two pages)

| Section | Lines |
|---|---|
| Header + summary | 4 |
| Skills | 7 |
| Blue Light Card | 20 |
| Sano Genetics | 8 |
| Pion, Engineering Manager | 12 |
| Pion, Android | 6 |
| Appoly | 5 |
| Sandwell | 2 |
| Education | 2 |
| Outside work | 5 |

If the total does not fit: trim Outside work to two items first, then the
least-recent role bullet. Do not cut a Blue Light Card bullet or shrink the type.

## Decisions

| Date | Decision |
|---|---|
| 14 Nov | Headline stays "Senior Software Engineer"; the summary carries the level |
| 14 Nov | No years of experience in the summary; capability over tenure |
| 14 Nov | First person in summaries, implied subject in bullets |
| 14 Nov | Skills block stays as the keyword surface; the summary names only the spine |
| 14 Nov | "Selected work" is removed from the website: it duplicates the headline and uses the best space on the page for it |
| 14 Nov | AI stays visible, but as evidence rather than a label: "Full Stack Engineer" in the summary, plus a line on AI tooling and an AI row in skills |

## Decisions on the outside work and additional experience

- **Sections**: "Projects" in the PDF (homelab, Game Boy, apps); the site keeps a
  Projects page plus an "Additional experience" section on the Experience page.
- **Paperound** goes in Additional experience, site only, linked to the live
  Jenson page (April 2021). Fallbacks if the domain moves again:
  `https://web.archive.org/web/20260512130208/https://jensonventures.com/jenson-seis-fund-invest-in-paperound/`
  and
  `https://web.archive.org/web/20210423095542/https://jensonfundingpartners.com/2021/04/20/jenson-seis-fund-invest-in-paperound/`
  The £120,000 is Billy's figure and is not in the article.
- **OCR** goes in Additional experience, site only.
- **Phone number** removed from the PDF and the site.
- **No dashes of any kind** anywhere: no em dash, no en dash, no dash as
  punctuation.
- **No Oxford commas.** Serial lists take no comma before the final "and".

## Open

Nothing outstanding.

## Process

1. Agree text in chat, section by section.
2. Apply everything in one commit, build, and show both pages.
3. One independent review of the render, one round of fixes.
4. Freeze. No incremental deployments.
