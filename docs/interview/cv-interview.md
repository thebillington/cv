# CV discovery interview

Purpose: extract the specific, checkable detail that makes a senior engineering
CV persuasive, so the document stops reading like a summary and starts reading
like evidence. The current draft is accurate but generic; this fixes that.

**How to answer**

- Fragments are fine. Numbers, system names, timeframes, trade-offs. No prose.
- "I don't know" is a valid answer, and so is "about 40, I would not put a
  precise figure on it". A defensible round number beats a fake precise one.
- Mark anything you cannot say publicly (customer names, internal codenames,
  unreleased work). I will generalise it rather than drop the achievement.
- If a question is not interesting, skip it. If an answer opens something
  bigger, keep going; the follow-ups are the point.

**What happens next:** I rewrite the CV from your answers, in a formal register,
keeping only claims that survive an interview question. Then the PDF gates and
the site are rebuilt.

---

## Part 0 - Ground rules

0.1 Which target titles are you actually applying for, in priority order?
(Senior Software Engineer, Staff Engineer, Engineering Manager, Tech Lead,
Platform Engineer, something else?)

0.2 Are you open to management again, or is the next move deliberately IC?
What should the CV argue?

0.3 What must stay off the public site? (customer names, internal system names,
salary, notice period, anything under NDA.)

0.4 Which two or three things do you want a hiring manager to remember after
30 seconds?

0.5 What do you want to be interviewed about? (The things you would happily
talk about for 20 minutes.)

---

## Part 1 - Scale and scope at Blue Light Card

The appraisal gives the shape of the work; the CV needs the size of it.

1.1 How many members does the platform serve? How many brands and territories?

1.2 How big is the engineering organisation, and how big is your squad? Who do
you report to, and who reports to you (if anyone)?

1.3 The monorepo: how many services or packages, roughly how much code, how many
engineers working in it, how many deploys a week before and after your changes?

1.4 How many AWS accounts and environments does the platform run in? What does a
deploy look like now, end to end (branch to production, how long)?

1.5 Which services do you personally own or co-own today?

---

## Part 2 - The Members service extraction

The appraisal says you proposed it by RFC, delivered it, tested it, and owned the
result. That is a senior/ staff-level bullet waiting to happen.

2.1 What was wrong with the members stack and monorepo? Give the concrete
symptoms (build times, coupling, deploy failures, blast radius, version skew).

2.2 What did the RFC actually propose? Summarise the design in 3-4 points:
repository layout, infrastructure, data, deployment.

2.3 What alternatives did you reject, and why? (Stay in the monorepo, strangler
pattern, service mesh, shared database, etc.)

2.4 How did you keep the cutover safe? Traffic splitting, shadow reads, dual
writes, feature flags, rollback plan. What would have happened if it went wrong?

2.5 What did the endpoint parity suite cover: how many endpoints, what
assertions, what did it catch before release?

2.6 What did you instrument so it could be "monitored accurately"? Which
dashboards, which alerts, what thresholds?

2.7 How long did the migration take, and how many people worked on it? What was
your personal share of the code and the decisions?

2.8 Results, in numbers if they exist: deploy time before and after, number of
repos or services changed, incidents during cutover, code deleted, CI time,
onboarding time for a new engineer.

2.9 What was the hardest technical decision in it, and what did you trade away?

---

## Part 3 - Globalisation, PHP removal and the forced update

3.1 What did the PHP proxy actually do, and what depended on it? How many
services, routes, or clients?

3.2 How did you sequence the removal so nothing broke? What was the rollback
story?

3.3 "Pipelines so the admin panel can run auditable DB queries": what was the
risk being controlled, and what did you build? (Approval flow, audit log, read
replicas, query guardrails?)

3.4 The forced update work: which platforms and versions, how many members
affected, what was the business deadline, and what did you own?

3.5 The legacy apps: how many, what did they cost to run, and what does
"retired" mean in numbers (services off, cost saved, support tickets removed)?

3.6 What did the rollout involve outside engineering (comms, member ops,
support)? What did you personally coordinate?

---

## Part 4 - Renewals, Australia, and day-to-day delivery

4.1 Renewals: what was broken in the decoupling and rebuild, and what did you
change? What was the before/after in defects, delivery time or release cadence?

4.2 The mob sessions: how many engineers, what did you run, and what improved?
(Quality, ownership, review turnaround, onboarding?)

4.3 Australia data issues: what was wrong with the data, how large was the
problem, how did you diagnose it, and what changed as a result?

4.4 Give me two examples of ordinary engineering work you are proud of that a CV
would normally miss (a nasty bug, a performance fix, a design that removed a
class of failure).

---

## Part 5 - AI adoption (the part your manager singled out)

5.1 What exactly did you build? For each: the problem, the mechanism, the
result. (MCP servers, local model delegation, Grafana/CloudWatch automation,
agent-ready documentation, the API change validation tool.)

5.2 "A shared process for documenting AI-assisted work": what is the process?
Who uses it, and what changed in review quality or traceability?

5.3 "Shared configs with the wider engineering team": what is in them, and how
many engineers use them?

5.4 Which demos did you run, to whom, and what did people change afterwards?

5.5 Any measured effects: token spend, review turnaround, test coverage,
defects caught, time saved per week? Rough numbers are fine.

5.6 What guardrails did you set (data handling, review rules, which tools are
allowed), and what did they prevent?

5.7 What is the company-level version of this you want to do next (the appraisal
suggests a standard, a playbook or measured results)?

---

## Part 6 - Sano Genetics (Engineering Manager, 2025-06 to 2026-02)

6.1 How big was the squad, and what was the platform's scale (participants,
samples, kits shipped, orders processed)?

6.2 The kits and orders migration: what was the legacy shape, what was the V2
shape, how much data, and what did it remove?

6.3 Which logistics providers did you integrate, and what did the automation
replace?

6.4 Genetic data: what compliance constraints applied (GDPR, ISO 27001, NHS or
research ethics), and how did that shape the design?

6.5 What did you own as an EM versus as an engineer on that squad? Be honest
about the split.

---

## Part 7 - Pion (Engineering Manager, 2022-01 to 2025-06)

7.1 Headcount: how many engineers directly, how many across the squads you were
responsible for? Any hires, promotions, or exits you managed?

7.2 Hiring: how many loops did you run, and did you change the process (rubrics,
scorecards, level calibration)?

7.3 DORA/SPACE: which metrics did you surface, from what data, and what moved?
(Deploy frequency, lead time, change failure rate, MTTR. Before and after.)

7.4 ISO 27001: what was in scope, what did you have to change, how long did it
take, and what was the audit outcome?

7.5 Incidents: what was the process before and after, what happened to MTTR or
page volume, and did you run the post-mortems?

7.6 Templates: how many teams adopted them, and what did they save? (Time to a
deployed service, lines of duplicated config.)

7.7 What was the hardest people problem you handled, and what did you change
about how the team worked?

---

## Part 8 - Pion (Android Engineer, 2020-09 to 2022-01)

8.1 App scale: installs, monthly active users, release cadence, crash-free rate.

8.2 The OkHttp/Room migration: what was the measurable effect (startup time,
crash rate, developer velocity)?

8.3 Impression tracking: what volume of events, which clients used the Looker
dashboards, and what decision did the data change?

8.4 What did you design yourself versus implement to someone else's design?

---

## Part 9 - Appoly (2019-2020) and teaching (2017-2019)

9.1 Which clients and sectors, and what did you personally ship? (No client
names if confidential: "a gas utilities hardware vendor".)

9.2 The binary image stream and FTP work: what was the hardware, the data rate,
and why was it hard?

9.3 Teaching: cohort sizes, results, and what the open-source curriculum
actually became (schools using it, downloads, the Staffs University network).

---

## Part 10 - Projects and open source

10.1 tphysics: users, stars, downloads, schools, and what was technically hard.

10.2 psx2rip: users, stars, what it automates, what was hard.

10.3 Mushy's Adventure: any recognition, downloads, constraints of writing for
real Game Boy hardware.

10.4 The browser Game Boy emulator and WASM CPython REPL: what was the
engineering problem, and who uses it?

10.5 Should these be on the CV, the site, or neither?

---

## Part 11 - Skills, honestly

11.1 For each language (TypeScript, Python, Kotlin, Swift, Java), rate your
depth and say where the deepest work was. Which would you defend in an
interview, and which are "have used"?

11.2 Same for AWS: which services have you operated in production, and which
have you only used? (Lambda, API Gateway, ECS/EKS, RDS, DynamoDB, S3, IAM,
CloudWatch, EventBridge, Step Functions...)

11.3 Terraform: modules you wrote, state and workspace patterns, provider
versioning, what you would not do again.

11.4 Testing: what do you actually write (unit, integration, contract,
end-to-end), which frameworks, and what is your view on coverage?

11.5 Observability: what have you instrumented, what alerts have you owned, and
what does "good" look like to you?

11.6 What are you deliberately not claiming on the CV, even though you have
touched it?

---

## Part 12 - Register and formality

12.1 Which of these is closer to how you want to sound?

A. "Owned the extraction of the Members service from a legacy monorepo,
delivering a Terraform stack, deployment pipeline and endpoint parity suite that
made the cutover verifiable and reversible."

B. "Split the Members service out of a legacy monorepo onto its own Terraform
stack, with a pipeline and parity tests so the cutover could be checked and
rolled back."

12.2 Any phrases you actively dislike? Any you want kept because they are how
your employer describes the work (for example "members", "squad", "RFC",
"guiding principles")?

12.3 Do you want the management history framed as a chapter you are proud of, or
as context for the IC return?

12.4 One page or two? (Two is the current build and the evidence says it is
fine at this level.)

---

## Where to find the numbers

| Number | Where to look |
|---|---|
| Deploy frequency, lead time, MTTR | GitHub Actions history, Grafana, your DORA pipelines at Pion |
| Members, brands, territories | Product or company dashboards, the business update |
| Code size, services, repos | Repo count in GitHub, `cloc` on the monorepo, service catalogue |
| Test counts, coverage | CI output, the parity suite report |
| Incident and page volume | PagerDuty / Opsgenie / incident tool |
| Cloud spend | AWS Cost Explorer by account and service |
| AI token spend | Provider billing, the local model usage you tracked |
| App scale | App Store / Play Console, Looker dashboards |
| Team size and hiring | Org chart, HR, your own records |
| Schools using the curriculum | Staffs University network, downloads |

---

## Claim check

Statements from the appraisal that can become CV bullets once confirmed. Fill in
the number or the detail, or cross it out if it would overstate.

| Said about you | CV-ready claim needs |
|---|---|
| "Identified two problems: the members stack and monorepo, and the lack of a shared approach to AI" | What was wrong, in numbers (build time, deploys, incidents) |
| "Proposed the approach through an RFC, delivered the work, tested it, took ownership" | RFC link or title, timeline, team size |
| "Easy to monitor accurately and easy to roll back" | Dashboards and alert thresholds, rollback time |
| "Removing the PHP proxy dependency... built pipelines so the admin panel can run auditable DB queries" | What the proxy did, how many routes/clients, the audit control |
| "Significant ownership of the forced update work... wider business comms and member ops support" | Platforms, user counts, deadline |
| "Retiring the legacy apps is now a realistic near-term milestone" | How many apps, cost, support load |
| "Engaged proactively with the Australian team to triage and analyse data issues" | Size of the data problem, root cause, fix |
| "Organise mob sessions during renewals that raised delivery quality and built ownership" | Team size, cadence, measured effect |
| "Main driver of AI adoption in the squad... documented process, shared configs, demos" | Adoption numbers, measured effect, guardrails |
