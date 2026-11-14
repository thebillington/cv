// Billy Rebecchi CV
// Single column, ATS-safe, tagged PDF (PDF/UA-1).
//
// Two variants from one source: light (the one you send) and dark (for screen,
// where the reader is an engineer rather than an ATS).
//
// Layout rules:
//   * employer first, then title, then stack, then evidence
//   * dates right-aligned on the employer line so the chronology scans
//   * serif for the name only; sans for prose; mono for metadata, stacks,
//     dates and section labels, which is what makes it read as a spec rather
//     than a brochure
//   * nothing that a parser has to untangle: no tables, columns or icons

#let cv(data, dark: false) = {
  // ---------------------------------------------------------------- palette
  let ink = if dark { rgb("#D8E1E9") } else { rgb("#1B1B1B") }
  let name-col = if dark { rgb("#F0F6FB") } else { rgb("#14314E") }
  let accent = if dark { rgb("#69ADD1") } else { rgb("#2A6F97") }
  let muted = if dark { rgb("#8996A4") } else { rgb("#5B6570") }
  let body-2 = if dark { rgb("#A9B5C1") } else { rgb("#3F4A56") }
  let rule = if dark { rgb("#2A3542") } else { rgb("#C9D2DA") }
  let paper = if dark { rgb("#0E141B") } else { white }

  let sans = "Source Sans 3"
  let serif = "Source Serif 4"
  let mono = "IBM Plex Mono"

  set document(
    title: data.profile.name + " CV" + if dark { " (dark)" } else { "" },
    author: data.profile.name,
    keywords: (
      "software engineer",
      "typescript",
      "python",
      "kotlin",
      "aws",
      "terraform",
      "platform engineering",
      "engineering management",
    ),
  )

  set page(
    paper: "a4",
    margin: (x: 17mm, top: 12mm, bottom: 11mm),
    fill: paper,
    footer: context {
      let total = counter(page).final().first()
      set text(font: mono, size: 7.5pt, fill: muted)
      pdf.artifact[
        #align(right)[PAGE #counter(page).get().first() / #total]
      ]
    },
  )

  set text(font: sans, size: 9.4pt, fill: ink, lang: "en", region: "GB", hyphenate: false)
  set par(justify: false, leading: 0.6em, spacing: 1em)
  set list(
    marker: text(fill: accent)[•],
    indent: 0.55em,
    body-indent: 0.5em,
    spacing: 0.34em,
  )

  // Name: the only serif on the page.
  show heading.where(level: 1): it => block(above: 0pt, below: 1pt)[
    #text(font: serif, size: 26pt, weight: 600, fill: name-col, tracking: -0.01em)[#it.body]
  ]

  // Section labels: numbered, mono, ruled. Reads like a document outline.
  let section-counter = counter("section")
  show heading.where(level: 2): it => {
    counter("section").step()
    block(
      above: 13pt,
      below: 6pt,
      width: 100%,
      sticky: true,
      stroke: (bottom: 0.6pt + rule),
      inset: (bottom: 3pt),
    )[
      #text(font: mono, size: 8pt, weight: 600, fill: accent)[#context counter("section").display("01")]
      #h(0.9em)
      #text(font: mono, size: 8.6pt, weight: 600, fill: name-col, tracking: 0.14em)[#upper(it.body)]
    ]
  }

  // ---------------------------------------------------------------- header
  heading(level: 1)[#data.profile.name]

  stack(spacing: 0pt,
    v(2pt),
    text(font: mono, size: 9.6pt, weight: 600, fill: accent, tracking: 0.06em)[#upper(data.profile.title)],
    v(7pt),
    text(font: mono, size: 8.2pt, fill: body-2)[
      #data.profile.location
      #h(1.4em) #link("tel:" + data.profile.phone.replace(" ", ""))[#data.profile.phone]
      #h(1.4em) #link("mailto:" + data.profile.email)[#data.profile.email]
    ],
    v(3pt),
    text(font: mono, size: 8.2pt, fill: body-2)[
      #link(data.profile.links.website)[#data.profile.links.website.replace("https://", "")]
      #h(1.4em) #link(data.profile.links.github)[#data.profile.links.github.replace("https://", "")]
      #h(1.4em) #link(data.profile.links.linkedin)[#data.profile.links.linkedin.replace("https://", "")]
    ],
    v(9pt),
    block(width: 100%, height: 1.4pt, fill: accent),
  )

  // --------------------------------------------------------------- profile
  heading(level: 2)[Profile]
  text(size: 9.4pt)[#data.profile.summary]

  // ---------------------------------------------------------------- skills
  heading(level: 2)[Core skills]
  for line in data.skills.core [
    #let parts = line.split(":")
    #text(font: mono, size: 7.6pt, weight: 600, fill: accent, tracking: 0.08em)[#upper(parts.at(0))]
    #h(0.6em)
    #text(size: 9pt, fill: body-2)[#parts.slice(1).join(":").trim()]
    #parbreak()
    #v(1.4pt)
  ]

  // -------------------------------------------------------------- experience
  heading(level: 2)[Experience]

  for role in data.experience {
    let achievements = role.at("achievements", default: ()).filter(
      a => a.at("include_pdf", default: true)
    )
    let title_line = role.title
    if role.at("team", default: "") != "" {
      title_line = title_line + ", " + role.team
    }

    block(above: 12pt, below: 0pt, breakable: false, sticky: true)[
      #text(size: 11pt, weight: 700, fill: name-col)[#role.company]
      #h(1fr)
      #text(font: mono, size: 8pt, fill: muted)[#role.start to #role.end]
      #linebreak()
      #text(size: 9.9pt, weight: 600)[#title_line]
      #if role.at("stack", default: ()).len() > 0 [
        #linebreak()
        #text(font: mono, size: 7.6pt, fill: muted)[#role.stack.join(" · ")]
      ]
      #v(4.5pt)
      #text(size: 9.4pt)[#role.summary]
    ]

    if achievements.len() > 0 [
      #block(inset: (top: 8pt))[
        #list(
          spacing: 0.34em,
          ..achievements.map(a => text(size: 9.2pt)[*#a.title.* #a.description]),
        )
      ]
    ]
  }

  // ------------------------------------------------------------- education
  heading(level: 2)[Education]
  for edu in data.education.education [
    #text(size: 9.6pt, weight: 600)[#edu.degree]
    #h(1fr)
    #text(font: mono, size: 8pt, fill: muted)[#edu.start to #edu.end]
    #linebreak()
    #text(size: 9pt, fill: body-2)[#edu.institution#text(size: 8.8pt, fill: muted)[, #edu.grade]]
    #parbreak()
    #v(2.5pt)
  ]

  // ------------------------------------------------------------ open source
  heading(level: 2)[Open source]
  for name in ("tphysics", "psx2rip") {
    for proj in data.projects {
      if proj.name == name {
        text(size: 9.2pt)[*#link(proj.url)[#proj.name].* #proj.summary]
        parbreak()
        v(2pt)
      }
    }
  }
}
