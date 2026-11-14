# Archive findings

Search of the file store for prior appraisals and self-written work notes, so the
CV can use evidence rather than recollection. Searched on 13/14 November 2026.

## What was searched

| Where | What | Result |
|---|---|---|
| CT 105 `/share/Documents` | 2.0 GB of documents (Admin, Email, Employment, Other, Projects, Teaching, University) | **Useful**: one appraisal, one work timeline, interview notes, four older CVs |
| CT 105 `/share/Archives` | 1.2 GB of old coursework and teaching material | Nothing work-related beyond the CVs |
| CT 105 `/share/takeout-incoming` | `takeout-20261104T084710Z-1-001.zip` | Contains **Mail only** (a 4.5 GB mbox, 50,379 messages), no Drive export |
| `/srv/ssd/cloud` (Nextcloud data) | 80 MB, two users | No work documents |
| Gmail mbox | Full-text search for appraisal, performance review, mid-year, self-assessment, review cycle, Culture Amp, plus a headers-only pass over every message sent to self | **No appraisals or self-reviews found.** The export is overwhelmingly personal mail; the appraisal material lives in files, not email |

## Sources found

| Source | Date | Why it matters |
|---|---|---|
| `Documents/Other/Appoly Appraisal Nov 2019.docx` | Nov 2019 | Per-project record of the Appoly year: which apps, which devices, what he personally built |
| `Documents/Other/BLC HoE Timeline.docx` | to Aug 2026 | Dated record of the members migration: RFC raised 1 April 2026, 100% traffic on 19 May 2026, no issues during rollout, PR references |
| `Documents/Other/Monzo Interview Notes.docx` | 2025/26 | His own framing: backend-first, end-to-end ownership, senior judgement, the deliberate IC step-down |
| `Documents/Other/Student Beans Interview Notes.docx` | 2020 | Context for the Android role |
| `Documents/Admin/CV 2025 1-pager.docx` | 2025 | Natalie's CV, not Billy's |
| `Documents/Email/Employment/CV*.pdf`, `Documents/Admin/Copy of CV-android.pdf` | 2016 to 2020 | Earlier claims: Sandwell line management, Appoly MVVM, Student Beans test coverage |
| `Documents/Other/Sano Notes.docx` | 2025 | Offer terms. Private, not CV material |

## What changed in the CV as a result

- **Blue Light Card**: the extraction now says the service reached **100% of
  production traffic without a rollback** (19 May 2026), and the summary names
  the JWT claim enrichment and native-to-web session transfer.
- **Appoly**: replaced two generic bullets with the actual work from the 2019
  appraisal: leading the AutoRing Android client and its client/hardware
  relationship, and integrating devices over BLE (TPI DC710 flue gas analyser),
  socket-level FTP (Smartfill) and a Python service parsing binary image streams.
- **Sandwell Academy**: restored the department line management (two teachers)
  from the older CV.
- **Pion and Student Beans**: kept as they were. The 2019/2020 CVs add detail
  (MVVM, 70% unit-test coverage, CI pipelines) but not enough to earn space on a
  two-page document aimed at senior roles.

## Deliberately not used

- The BLC timeline document also records interpersonal grievances and names
  colleagues. None of that is on a public CV, and none of it is quoted here.
- Sano offer terms (salary, equity) and redundancy material.
- Anything that would require the reader to know an internal codename.

## Still missing

The archive confirms *what* was built but not *how much*. These are the numbers
the CV still needs, and they are in the interview:

- members: platform size, services in the monorepo, deploy frequency, parity
  suite size
- Pion: headcount, hiring, the DORA metrics before and after
- Student Beans: installs and the effect of the Room/OkHttp migration
- teaching: cohort sizes and curriculum reach
