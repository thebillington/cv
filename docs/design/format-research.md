# Format research: what engineering CVs actually look like

Searched 14 November 2026, after the first redesign was called lifeless. The
question was narrow: what do engineers and the people who hire them say about
CV *format*, and what does "engineery" mean in practice?

## What the forums say

**Plain, dense, single column. This is not close.**

r/cscareerquestions, r/EngineeringResumes and r/resumes converge on the same
three rules, and the specific template they converge on is Jake's Resume:

> "The most common beginner mistake is overdesigning your resume. Columns,
> icons, colored sidebars, infographic elements, these things fail ATS and often
> annoy human reviewers who've seen thousands of resumes."
> — summary of r/resumes and r/cscareerquestions threads,
> [wildandfreetools](https://wildandfreetools.com/blog/simple-resume-format-reddit-recommendations-2026/)

> "Jake's Resume ... became the default recommendation. Not because anyone found
> it beautiful ... It parsed cleanly, recruiters at large employers recognised
> the shape of it instantly, and it fit a surprising amount of substance onto one
> dense, readable page."
> — [EvoResume](https://evoresume.com/blog/best-ats-resume-template-2026)

On Hacker News the same instinct appears as a preference for LaTeX output:

> "I use a plain pdf resume that is written in Latex. I host it on Overleaf so
> it's always easy to update."
> — [Ask HN: Are plain resumes still relevant?](https://news.ycombinator.com/item?id=12517980)

> "Your CV's format is irrelevant so long as it doesn't look like a dog's
> breakfast or a Xmas tree."
> — same thread

**But "plain" is not "undesigned".** The thing engineers recognise in a LaTeX CV
is *typesetting*: consistent baseline, real rules, someone thought about it.

> "Tech recruiters instantly recognize the clean, typeset margins, specific math
> ligatures, and classic fonts of TeX compilers. It signals that you are part of
> the technical community."
> — [Lampzi](https://lampzi.com/blogs/latex-resume-template-software-engineer)

And the counter-position, from the thread that argues LaTeX is signalling:

> "In your job, you probably share information in markdown or rst. If you're
> looking to signal, why not use those?"
> — [Hacker News](https://news.ycombinator.com/item?id=28198044)

**Dark mode is a screen idea, not a document idea.**

> "Imagine all the ink wasted from printing just a single copy" ... "Dark mode
> obviously means 100x SWE."
> — engineer comments on a dark-mode CV, [Blind](https://www.teamblind.com/post/you-open-a-resume-and-it-is-in-dark-mode-gpcsmtja)

> "Having worked for several small businesses, I would skip a dark resume because
> it would appear unprofessional to me. Additionally, black text on white paper
> is easier to read for those with accessibility concerns."
> — same thread

> "Make it boring ... no colors, no charts, no graphs, no pictures."
> — former Nvidia recruiter, [CNBC](https://www.cnbc.com/make-it/2024/05/28/dont-use-color-on-a-resume-be-boring-says-ex-nvidia-recruiter.html)

## What that means for this document

The honest reading is that a dark CV hurts with the person who screens it, and
delights the engineer who opens it. So: **both, with different jobs.**

| Surface | Decision |
|---|---|
| The CV you send | Light, single column, dense. The one an ATS and a recruiter see |
| Dark variant | Generated from the same source, offered on the site "for reading on screen", never the submitted file |
| Website | Dark by default when the system asks for it, with a toggle, and the same palette as the dark PDF |

## Making it feel engineered without decoration

The first version was clean but generic, because it borrowed a charity-sector
layout. The fix is typographic, not graphical:

- **Mono metadata.** Section labels, dates, stack lines, contact details and the
  page folio are set in IBM Plex Mono. Prose stays in Source Sans. That contrast
  is the same trick a terminal or a well-set spec sheet uses: the structured
  parts look structured.
- **Numbered sections.** `01 PROFILE`, `02 CORE SKILLS`, `03 EXPERIENCE`. It
  reads as a document with an outline, and it costs no space.
- **One accent, used for structure only.** The accent marks the section number,
  the rule, the skill labels and the links. It never carries meaning on its own
  and it survives greyscale.
- **No new graphics.** No icons, bars, chips or sidebars: the forum consensus is
  right that they cost more than they earn.

What was deliberately *not* done: a two-column "designer" layout, a photo, skill
bars, a coloured header block, or a mono body font (which reads as costume).
