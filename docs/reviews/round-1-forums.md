# Round 1 - forum validation: software engineering CVs

**Subject:** Billy Rebecchi - UK senior software engineer / engineering manager,
2pp A4, single column, Source Sans 3 with a Source Serif 4 name.
**Purpose:** test ten document decisions against practitioner sentiment in public
forums and communities, rather than against taste.
**Date:** 13 November 2026.

---

## How this was researched (and what could not be reached)

| Route | Status |
|---|---|
| `reddit.com/.../search.json` | **Blocked** - 403 bot page |
| `old.reddit.com` JSON | **Blocked** - login shell, no JSON |
| Redlib / Libreddit mirrors (4 tried) | **Blocked** - 429, 410, or Anubis proof-of-work |
| `api.pullpush.io` | **Down** - 526 invalid certificate |
| Arctic Shift API (`arctic-shift.photon-reddit.com`) | **Working** - used for every Reddit quote below |
| Hacker News Algolia API | **Working** - used for the HN quotes below |
| Bing / DuckDuckGo HTML, built-in search | Returned pages but no parseable links; the built-in tool surfaced SEO aggregator blogs. **Nothing from them is quoted** |
| Ask a Manager, recruiter blogs | Not retrieved this round; nothing from them is quoted |

Reddit quotes were read from archived comment bodies via Arctic Shift, so they
are verbatim but sampled by thread title (a full-text search over large
subreddits repeatedly timed out). That biases the sample toward explicitly
titled threads and is recorded in the limitations.

Communities are marked: **r/ExperiencedDevs, r/cscareerquestions and Hacker
News are US-majority**; r/cscareerquestionsEU and r/UKJobs are mixed to UK.

## Verdict summary

| Decision | Verdict from the evidence |
|---|---|
| Two pages at 7+ years | **Accepted.** Nobody treats 2 pages as an error at this level; the live argument is density, not page count |
| Summary paragraph at top | **Split and conditional.** Wanted if it is 2-3 sentences; disparaged when generic or long |
| Skills / stack block | **Keep, but prune.** Expected for full-stack keyword matching; attacked as "word soup" when it is a 12-language list or soft-skill tail |
| Projects and GitHub link | **Optional and double-edged.** A linked GitHub will be read and judged; worth space only if the repos are presentable |
| Single vs two column | **Unresolved in the sources.** The concrete test practitioners use is text extractability, not column count |
| Metrics vs prose | **Wanted, but distrusted.** The resolution is a number tied to a mechanism, not a number alone |
| EM vs IC framing | **Be explicit about scope and honest about titles; the bullets decide which role you are read as** |
| AI/LLM on a CV in 2026 | **Expected but resented unless concrete.** Shipped systems and measured effects, never enthusiasm |
| UK specifics | Only length and photo conventions are evidenced; UK spelling and salary were not |

---

## 1. Two pages vs one page

> "2 pages is plenty. Beyond that we're probably talking about things from 5+
> years ago and they're going to be so hazy (in recollection) that it isn't
> worth discussing."
> - r/ExperiencedDevs (US-majority), [nw61yj](https://www.reddit.com/r/ExperiencedDevs/comments/nw61yj/whats_your_resume_not_cv_cutoff_length_when/h179cx9/)

> "I have 2 pages and get interviews in the uk."
> - r/cscareerquestionsEU (UK commenter), [1ch1x4a](https://www.reddit.com/r/cscareerquestionsEU/comments/1ch1x4a/uk_uni_career_advisor_suggested_me_to_keep_2/l20eioz/)

Dissent, for balance:

> "One-page is even more preferred by most hiring teams these days."
> - r/ExperiencedDevs, [1ts5i2c](https://www.reddit.com/r/ExperiencedDevs/comments/1ts5i2c/at_some_point_should_you_go_with_a_2page_resume/oosrfmv/)

**Reading:** at seven years with a mixed IC and management history, two pages is
the norm and nobody in these threads calls it disqualifying. The risk is that
page two carries low-value material.

## 2. Summary / profile paragraph

> "Hiring manager here. I like them about tweet length. It should take less than
> 2 seconds to read and understand. It should relate who you are, what you know
> and what you want."
> - r/ExperiencedDevs (US-majority), [j0zwsx](https://www.reddit.com/r/ExperiencedDevs/comments/j0zwsx/any_advice_or_ideas_for_a_summary_statement/g7021hi/)

> "I'd change the career summary to bullet points or find another way to make it
> more skimmable... Nobody got time to read a paragraph."
> - r/EngineeringManagers, [1kytxve](https://www.reddit.com/r/EngineeringManagers/comments/1kytxve/em_resume_feedback/mv0a008/)

> "Objectives on resumes are useless fluff. Yours doesn't add anything useful."
> - Hacker News, [19351185](https://news.ycombinator.com/item?id=19351185)

**Reading:** two or three sentences, or drop it. A five-line profile is the
specific thing being objected to.

## 3. Skills sections and tech-stack blocks

> "Listing all these languages makes you look like a complete amateur. Any senior
> professional coder knows it is impossible to have expertise in all these
> languages."
> - r/cscareerquestions (US-majority), [15drx1g](https://www.reddit.com/r/cscareerquestions/comments/15drx1g/i_do_not_know_how_to_organize_my_skills_section/ju3njkg/)

Pushback in the same thread:

> "I disagree with this, this is a pretty standard skill section for a full stack
> developer. My skills as a senior full stack dev look fairly similar to this."
> - r/cscareerquestions, [15drx1g](https://www.reddit.com/r/cscareerquestions/comments/15drx1g/i_do_not_know_how_to_organize_my_skills_section/ju3s3ov/)

> "Your whole summary of skills sections is word soup. I would completely ignore
> it. Anyone can list technologies they touched once... In your experience
> section list how you actually used those technologies."
> - Hacker News, [19351185](https://news.ycombinator.com/item?id=19351185)

> "If the bulleted skills list is greater than 5 lines chances it has the same
> skill duplicated multiple times."
> - Hacker News, [33332489](https://news.ycombinator.com/item?id=33332489)

**Reading:** the block is expected for keyword matching but every defence of it
constrains it: short, grouped, and only things you would take a deep question
on. Nobody defended a soft-skill tail.

## 4. Projects, side projects, GitHub links

> "I've not met an engineer I'd respect who'd consider it malpractice to look at
> the GitHub link that the candidate specifically put on their resume."
> - r/ExperiencedDevs (US-majority), [s838si](https://www.reddit.com/r/ExperiencedDevs/comments/s838si/if_you_put_it_on_your_resume_i_will_look_at_your/hthm1zi/)

> "Consider not putting your GitHub on your resume ever since some biased manager
> might decide your side project code isn't high quality enough based on some
> arbitrary criteria..."
> - r/ExperiencedDevs, [s838si](https://www.reddit.com/r/ExperiencedDevs/comments/s838si/if_you_put_it_on_your_resume_i_will_look_at_your/hthlzob/)

> "I would only link to them, if you want someone to visit them."
> - r/cscareerquestionsEU, [sx3b9g](https://www.reddit.com/r/cscareerquestionsEU/comments/sx3b9g/github_and_linkedin_links_in_resume/hxpr76f/)

**Reading:** a project section is not a differentiator at this level, but a
*linked* GitHub converts from decoration into evidence. If it stays, the pinned
repos have to be presentable.

## 5. Formatting, parsing, ATS

> "The best test you can do to check your PDF is CTRL + A in the PDF then copy
> paste into a text editor. It should come out as nicely human readable."
> - r/cscareerquestions (US-majority), [d7xgwc](https://www.reddit.com/r/cscareerquestions/comments/d7xgwc/is_it_true_that_some_pdfs_arent_parseable_by_ats/f15yxiq/)

> "If you are able to ctrl c, ctrl v sections of text then so will the automated
> system that parses CVs."
> - r/cscareerquestions, [d7xgwc](https://www.reddit.com/r/cscareerquestions/comments/d7xgwc/is_it_true_that_some_pdfs_arent_parseable_by_ats/f15o7sq/)

> "So here it's best to make them 'machine readable, human-tolerable'."
> - Hacker News, [34520168](https://news.ycombinator.com/item?id=34520168)

**Reading:** the operative rule is text extractability and sane reading order.
No retrieved source demonstrates that two columns are categorically fatal; that
claim appears only in SEO content, which was excluded. This document stays
single column anyway, because the copy-paste test is trivially passed and there
is no upside to the risk.

## 6. Bullets: metrics vs prose, and banned phrases

> "Others pointed out that you don't mention impact, just responsibilities, and
> this is 100% the thing you need to fix."
> - Hacker News, [39013287](https://news.ycombinator.com/item?id=39013287)

> "I especially appreciate metrics that are presented with two components: how
> they can be tied to business objectives, [and] your contribution in achieving
> that metric."
> - Hacker News, [34520691](https://news.ycombinator.com/item?id=34520691)

Counter-current, same thread:

> "ehh, metrics oriented CVs feel like bullshitting"
> - Hacker News, [34520907](https://news.ycombinator.com/item?id=34520907)

**Reading:** the objection is to unfalsifiable claims, not to verbs. A number
needs a mechanism and has to survive an interview question. Nobody defended
"responsible for" or "passionate about".

## 7. EM vs IC framing, and title honesty

> "Resume reads like you are still a line manager..."
> - r/EngineeringManagers, [1kytxve](https://www.reddit.com/r/EngineeringManagers/comments/1kytxve/em_resume_feedback/mv3llhh/)

> "I put the company name as the header and then the 2 positions (in my case)
> below it as subheaders. I think you'll raise unwanted questions by putting
> 'Engineering Manager 2018-present' if you actually had 3 titles over 7 years."
> - r/EngineeringManagers, [1kytxve](https://www.reddit.com/r/EngineeringManagers/comments/1kytxve/em_resume_feedback/mv6yf6z/)

> "as an already experienced EM, it depends on what you enjoy more... If it's a
> close tie, I would lean to the IC roles, just so you'll have more time to stay
> current."
> - r/EngineeringManagers, [1ugu9uo](https://www.reddit.com/r/EngineeringManagers/comments/1ugu9uo/software_senior_engineering_manager_to_ic/ou3wiez/)

**Reading:** list real titles with real dates, and pick one target: the bullets
decide how the document is read. An EM-titled CV that does not show hiring,
headcount and people outcomes reads as a tech lead.

## 8. AI/LLM experience in 2026

> "I guess 'AI' is the new buzz word. To me it's a little annoying, it's like
> trying to check if you've ever googled something before."
> - r/ExperiencedDevs (US-majority), [1k6ie4j](https://www.reddit.com/r/ExperiencedDevs/comments/1k6ie4j/the_desire_to_see_ai_usage_in_a_resume_or/)

> "ai on a resume is mostly buzzwords unless you're building real stuff end to
> end... enough to talk concretely"
> - r/ExperiencedDevs, [1qg2f90](https://www.reddit.com/r/ExperiencedDevs/comments/1qg2f90/does_anyone_feel_left_behind_without_ai_on_their/o09codd/)

> "Corporate-speak is soulless and impersonal. AI-generated text is soulless and
> impersonal. Match the tone to what is expected."
> - r/ExperiencedDevs, [1mk1ncm](https://www.reddit.com/r/ExperiencedDevs/comments/1mk1ncm/whats_a_polite_way_to_say_im_good_at_fixing_the/n7fvcok/)

**Reading:** AI as a headline attribute earns an eye-roll; shipped systems with
outcomes are a real signal. Do not let AI-assisted phrasing show.

## 9. UK-specific points

> "My CV is exactly 2 pages long. The first is split into education and work
> experience... Bullet points and short sentences are best as many jobs have
> hundreds of applicants."
> - r/UKJobs, [ztzpc](https://www.reddit.com/r/UKJobs/comments/ztzpc/)

> "Remove the photo, there is no requirement to have one."
> - r/cscareerquestionsEU (Germany, adjacent market), [1fwtabl](https://www.reddit.com/r/cscareerquestionsEU/comments/1fwtabl/photo_or_not_2_pages_or_not_in_a_cv_germany/lqiopvx/)

**Explicit gap:** no retrieved forum evidence on UK spelling conventions,
graduate schemes, or salary in a CV. Nothing was inferred for those.

## What the community would change, in order

1. **Two pages, and make page one the whole story.** Do not pad page two.
2. **Two or three sentences of profile**, or none.
3. **Every bullet as impact plus mechanism**; numbers only where they can be
   explained.
4. **Prune the skills block** to things defensible under questioning, grouped,
   five or six lines.
5. **Pick one target role** and re-sound the whole document for it.
6. **List the employer with real titles and dates**, so a mixed history reads as
   progression rather than as a rewritten title.
7. **Run the copy-paste test** and fix anything that scrambles.
8. **Decide deliberately whether the GitHub link earns its place.**
9. **AI only as shipped systems with outcomes.**

## Limitations

- Every Reddit quote came through the Arctic Shift API. reddit.com could not be
  opened directly and full-text search over large subreddits failed, so threads
  were selected by title. This is not a random sample and vote counts were not
  verified at read time.
- r/ExperiencedDevs, r/cscareerquestions and Hacker News are US-majority; US
  resumes differ from UK CVs.
- UK evidence is the weakest part: two r/UKJobs comments from 2012, one 2024
  r/cscareerquestionsEU thread and one 2023 thread.
- The "two columns break ATS" claim appears only in SEO content and was
  excluded; the primary sources retrieved contradict its strong form.
