# Market research: UK software engineering, 2026

Research round for this CV. Sources are public web pages, job adverts and
recruiter guidance; the annotated set is in section 8. Findings decide content
and keyword weight, not Billy's voice.

## 1. What the roles are called, and what they pay

Advertised medians and recruiter bands diverge sharply in the UK, so both are
given. Advertised median is what job ads quote (ITJobsWatch, six months to Nov
2026); recruiter bands are placement data and skew to London and experienced
hires.

| Title | UK advertised median | London | Typical recruiter band |
|---|---|---|---|
| Senior Software Engineer | £75,000 (10th £60k, 90th £100k) | £95,000 | £85k to £120k base at London scale-ups |
| Staff Engineer | too few ads for a stable median | - | £115k to £150k |
| Engineering Manager | £85,000 (10th £60k, 90th £110k) | £100,000 | £90k to £130k, average £110k |
| Lead Engineer / Tech Lead | - | - | £100k to £150k London; £70k to £100k nationwide |
| Platform Engineer | £80,000 (10th £51k, 90th £100k) | £87,500 | senior £80k to £105k |
| Full Stack Engineer | £60,000 (10th £42.5k, 90th £95k) | £60,000 | £65k to £150k, average about £105k |

Two lessons for this CV:

- **"Engineer" beats "Developer" in the same data** by roughly £40k of seniority
  signal on the same work, so the document says engineer throughout.
- The **Full Stack** median understates senior full-stack pay at product
  companies by £25k to £40k. The title on the CV is not the target: the scope in
  the bullets is.

## 2. The vocabulary UK adverts actually use

The strongest evidence is ITJobsWatch's co-occurrence tables: the share of
adverts for a title that mention each term. Use them as priority order.

**Languages.** TypeScript is table stakes for this target set (28% of full-stack
ads); Python 10-15%; Kotlin 9% of full-stack ads. Kotlin and Swift are
differentiators on mobile-adjacent product teams, not headline keywords.

**Frontend.** React 29% of full-stack ads; Next.js, Tailwind and CSS appear
constantly in body text. Adverts name the framework, not "modern JavaScript".

**Backend.** Node.js 21.5%, microservices 16.9%, REST 11%, serverless 8.9%.

**Cloud and platform.** AWS 28% of full-stack ads; Terraform 36% of platform ads;
infrastructure as code 35%; CI/CD 22-35%; Kubernetes appears in a quarter of
platform ads (not a claim this CV makes). Azure outranks AWS in platform ads,
which is worth knowing if the target set shifts to enterprise.

**Testing and quality.** Adverts name the discipline and the tool: TDD, contract
testing, the framework. "Automated testing" is the safe, true phrase here.

**Observability.** Named in 15% of platform ads, usually with a culture phrase:
"you build it, you run it". Owning production, on-call and runbooks is the
signal; the tools (CloudWatch, Grafana) are the evidence.

**Architecture.** Microservices, event-driven, system design, "technical debt",
"reduce complexity". Migration leadership (multi-quarter, high-ambiguity work)
reads staff-level.

**Leadership (senior IC ads).** Mentoring 8.8%, technical leadership 5%,
problem-solving 4.6%. Senior IC adverts expect informal technical leadership,
not management.

## 3. What separates a senior CV from a mid-level one

Levels are defined by scope, autonomy and impact, not years or language count.

- **Mid:** owns features inside a team, needs guidance on priorities, improves
  the code they work in.
- **Senior:** owns a service, system or domain; given a problem, designs *and*
  delivers it; writes design docs; sets the testing bar; mentors; is trusted with
  production incidents in their area; communicates trade-offs.
- **Staff:** owns a problem that crosses teams and sets standards others adopt.

Signals this CV makes explicit: system ownership including on-call and runbooks,
technical debt as deliberate work, migration leadership, mentorship with an
outcome, cost and reliability, incident response and post-mortems.

The 3.5 years as an Engineering Manager is the most senior thing in the history,
so the profile says so directly and explains the move back to hands-on delivery
in the same sentence. EM-era outcomes are carried as evidence of scope, not as a
former job.

## 4. EM-specific vocabulary

Four clusters in UK EM adverts:

- **People.** Line management, 1:1s, progression and performance, the difficult
  conversations, onboarding, coaching, mentoring, team health.
- **Hiring.** Own the loop, scorecards, level calibration, offer conversations.
- **Delivery.** DORA and SPACE named explicitly; cycle time, WIP, throughput;
  roadmaps; stakeholder management.
- **Technical direction.** Own technical direction, technical credibility, "not
  a pure process manager", architectural trade-offs, and in 2026 AI-native
  engineering with guardrails.

Adverts split cleanly between hands-on and hands-off management. This history is
the hybrid shape: management with a technical remit, and a return to delivery.

## 5. ATS and format guidance

- **Format.** Text-based PDF by default; DOCX only when asked. Layout matters
  more than extension: two-column files reorder sections in both formats.
- **Layout.** Single column. No tables, text boxes, contact details in headers or
  footers, skill bars, icons or photos. Those are on Greenhouse's own
  parse-failure list; Greenhouse also cannot parse files over 2.5 MB.
- **Headings.** Standard names. Creative headings break section detection.
- **Dates.** Month and year, one format, right-aligned so they scan.
- **Test it.** Select all, paste into a plain-text editor: title, company and
  dates should arrive together and in order.
- **File name.** `Billy-Rebecchi-CV.pdf`.
- **Links.** LinkedIn and GitHub as plain visible URLs in the body, not icons.
- **Length.** Two pages at seven years is the UK convention.

This CV's build enforces the parts a script can check: page count, sections,
contact extraction, glyphs, filler and core-skill presence.

## 6. Language to avoid in 2026

Cut entirely: passionate about, responsible for, duties included, helped with,
worked on, involved in, utilised, leveraged, spearheaded, orchestrated,
streamlined, fostered, dynamic, results-driven, detail-oriented, team player,
self-starter, go-getter, hard-working, proven track record, cutting-edge,
synergy, holistic, value-add, visionary, rockstar, ninja, guru, 10x, think
outside the box, works well under pressure, fast-paced environment.

"10x", "rockstar" and "ninja" now read as a culture warning rather than a
compliment.

**Do not avoid AI, avoid unsupported AI claims.** Named tools and workflow-level
detail (MCP servers, agent-targeted documentation, local models, token spend)
are genuine 2026 requirements. "AI guru", "prompt engineer" and "revolutionised
our workflow with AI" are the failure mode. Name the tool, the workflow and the
effect.

Replace each banned phrase with verb, scope and what changed.

## 7. Keyword bank

`data/keywords.yml` holds the bank used by `check_pdf.py` and `score_job.py`,
grouped as: languages, frontend, backend and API, mobile, cloud and platform,
testing and quality, observability and operations, security, architecture,
delivery, leadership, AI and tooling. It is deliberately smaller than the lists
below and covers only terms the history can evidence, so coverage means
something.

Terms seen across the market that this history does not claim, and should not
pretend to: Kubernetes, Docker, GraphQL, Go, Kafka, Postgres at scale, Azure,
TDD as a named practice, Playwright/Cypress.

## 8. Sources

Salary and market
- ITJobsWatch, Senior Software Engineer: https://www.itjobswatch.co.uk/jobs/uk/senior%20software%20engineer.do
- ITJobsWatch, Engineering Manager: https://www.itjobswatch.co.uk/jobs/uk/engineering%20manager.do
- ITJobsWatch, Platform Engineer: https://www.itjobswatch.co.uk/jobs/uk/platform%20engineer.do
- ITJobsWatch, Full-Stack Developer: https://www.itjobswatch.co.uk/jobs/uk/full%20stack%20developer.do
- Robert Walters UK Salary Survey 2026: https://www.robertwalters.co.uk/content/dam/robert-walters-redesign/country/united-kingdom/files/salary-survey/UK-Robert-Walters-Salary-Survey.pdf
- Hays UK Salary and Recruiting Trends 2026, Technology: https://www.hays.co.uk/documents/d/global/hays-pdf-tech-uksg26
- Ravio, software engineer salary trends: https://ravio.com/blog/software-engineer-salary-trends
- OpenSource, UK tech salary report: https://open-source.io/insights/uk-tech-salary-report-2026/
- ONS ASHE via Applyd: https://applyd.io/blog/uk-tech-salaries-2026
- Robert Half, most in-demand tech jobs Q3 2026: https://www.roberthalf.com/gb/en/insights/research/most-in-demand-tech-jobs-in-the-uk

Adverts read for vocabulary
- Legal and General, Senior Engineer: https://careers.legalandgeneral.com/job/senior-engineer-mongodb-and-aws-serverless-in-london-jid-8961
- Experian, Senior FullStack Engineer: https://jobs.experian.com/job/senior-fullstack-engineer-typescript-python-in-london-england-jid-6083
- giffgaff, Senior Software Engineer: https://talents.studysmarter.co.uk/companies/giffgaff-certified-b-corp/senior-software-engineer-frontend-15499488/
- Cancer Research UK, Senior Software Engineer: https://www.jobless.dev/jobs/senior-software-engineer-at-cancer-research-uk-80e10f85
- Octopus Legacy, Engineering Manager: https://builtin.com/job/engineering-manager/12161005
- DeepL, Engineering Manager: https://jobs.joinimagine.com/companies/deepl/jobs/87117632-engineering-manager-enterprise-acceleration
- Tide, Engineering Manager: https://job-boards.greenhouse.io/tide/jobs/7570173003
- Barclays, Engineering Manager, agentic engineering: https://search.jobs.barclays/job/knutsford/engineering-manager/13015/102902147680

Levels and craft
- Levelop, engineering career ladder: https://levelop.dev/blog/the-software-engineer-career-ladder-every-level-from-l3-to-staff-explained
- Talently, senior vs staff leveling: https://talently.tech/en/blog/senior-vs-staff-engineer-leveling-stuck-search/
- Will's View, engineering levels IC vs manager: https://willsview.dev/articles/engineering-levels-ic-vs-manager

ATS and format
- CitedCV, PDF or Word for an ATS: https://citedcv.com/en/pdf-or-word-for-ats
- Jobsistant, PDF vs DOCX controlled test: https://jobsistant.com/research/pdf-vs-docx-resume-ats-test
- ATS Score Checker, tables and columns: https://atsscorechecker.io/ats-friendly-resume/tables-columns-links
- StructuredCV, 30 resume buzzwords to delete: https://structuredcv.com/blog/resume-buzzwords-to-avoid
