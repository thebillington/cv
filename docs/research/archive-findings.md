# Archive findings

Search of the file store for prior appraisals, CVs and self-written work notes,
so the CV can use evidence rather than recollection. Searched 13/14 November
2026.

## What was searched

| Where | What | Result |
|---|---|---|
| CT 105 `/share/Documents` + `/share/Other` | 4,752 readable documents, scanned by **content** (not filename): docx, pdf, doc, pptx, xlsx, txt, md | **197 hits.** The Google Drive export lives here as converted Office files, which is why filenames do not give it away |
| CT 105 `/share/Archives` | 1.2 GB of coursework and teaching material | Nothing work-related |
| CT 105 `/share/takeout-incoming` | Takeout zip | **Mail only** (4.5 GB mbox, 50,379 messages), no Drive export |
| Gmail mbox | Full-text search plus a headers-only pass over all 206 self-sent messages | **No appraisals or self-reviews.** The mail export is personal; the Drive material is on disk |
| Nextcloud data (SSD) | 80 MB | Nothing relevant |

The first pass searched filenames only and found one appraisal. Scanning content
found the rest; that was the miss.

## Sources found

| Source | Date | What it gave |
|---|---|---|
| `Documents/Other/Appoly Appraisal Nov 2019.docx` | Nov 2019 | Per-project record of the Appoly year: AutoRing, BLE work, socket-level FTP, the Python binary stream service |
| `Admin/Jobs/cv-billy-rebecchi.docx` | 2026 | **Paperound as Co-founder/CTO**: £120k seed round, sole engineer, Sharetribe Go, Python scraper to Postgres RDS, Lambda jobs, revenue growth |
| `Admin/Jobs/CV-engineering-manager.docx` | 2025 | Paperound to £15k/month; Ecoworks trustee and the monitoring system; OCR moderation; CoderDojo |
| `Admin/Jobs/CV-engineering.docx` | 2025 | **20+ engineers across 3 squads**; GitLab to Redshift via Glue/Airflow; level 4 and 6 apprenticeships (76% eNPS); NTU lecturing |
| `Admin/resume-billy-rebecchi-ats.docx` | 2026 | DORA/SPACE pipelines **used by 50+ engineers**; zero active CVEs; apprenticeship 76% eNPS |
| `Documents/Other/Depop Notes.docx` | 2025 | Three squads (2 web, 1 backend), OKR setting, fortnightly DORA reporting to SMT, incident redesign, Android feature detail |
| `Documents/Other/BLC HoE Timeline.docx` | to Aug 2026 | RFC raised 1 April 2026; 100% of production traffic on 19 May 2026 with no issues; PR references |
| `Documents/Other/Monzo Interview Notes.docx` | 2026 | His own framing: backend-first, end-to-end ownership, senior trade-offs, the deliberate IC step-down |
| `Documents/Email/Employment/CV*.pdf`, `Admin/Copy of CV-android.pdf` | 2016 to 2020 | Sandwell line management (two teachers), Appoly MVVM, Student Beans test coverage |

## What changed in the CV

- **Paperound added** as a role (Oct 2020 to Nov 2022): co-founder and CTO, £120k
  raised, built as the only engineer, £15k/month gross revenue, Python scraper to
  Postgres on RDS, AWS Lambda jobs.
- **Pion EM**: 20+ engineers across three squads, DORA/SPACE pipelines used by
  50+ engineers with fortnightly reporting to the SMT, Level 4 and 6
  apprenticeships at 76% eNPS, ISO 27001 with zero active CVEs, incident redesign.
- **Pion Android**: impression tracking designed from scratch (Iglu/Snowplow,
  Looker in the self-serve CMS), OkHttp/Room/Navigation/ViewModels, Dagger/Hilt.
- **Appoly**: the real 2019 work (BLE state machine for the TPI DC710, socket-level
  FTP for Smartfill, Python binary stream service, AutoRing client lead).
- **Sandwell**: department line management restored.
- Roles are now ordered by end date, so the overlapping founder role reads
  cleanly against the day jobs.

## Deliberately not used

- The BLC timeline also records interpersonal grievances and names colleagues.
  None of it is used, quoted or published. The only facts taken from it are the
  RFC date and the 100% rollout.
- Sano offer terms (salary, equity), redundancy material, internal codenames
  ("blue crew"), and the internal ticketing or Slack links.
- The older ATS resume contains a few inflated phrases ("known for improving
  system reliability"); only the numbers that appear in more than one source
  were taken.

## Still to confirm

- **OCR A-Level moderator** (H446/03 and H446/04): two CVs say March 2022 to
  present. Worth a line if still current.
- **Nottingham Trent lecturer** (Level 6 apprenticeship): appears in a 2025 CV as
  February 2023 to present. Current?
- **Ecoworks trustee** and the monitoring system he built for them: current, and
  worth one line?
- **CoderDojo lead volunteer**: still running it?
- Whether the £120k raise and £15k/month revenue are publishable on a public CV.
- Team size and hiring numbers at Pion, if they can be stated.
