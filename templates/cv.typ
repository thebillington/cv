// Billy Rebecchi CV
// Single column, ATS-safe, tagged PDF (PDF/UA-1).
//
// Layout rules, kept deliberately few:
//   * employer first, then title, then stack, then evidence
//   * dates right-aligned on the employer line so the chronology scans
//   * one font family for prose, a serif only for the name
//   * no colour used to carry meaning, and nothing that a parser has to
//     untangle (no tables, columns, text boxes or icons)

#let navy = rgb("#14314E")
#let steel = rgb("#2A6F97")
#let slate = rgb("#3F4A56")
#let meta = rgb("#5B6570")
#let ink = rgb("#1B1B1B")
#let rule = rgb("#C9D2DA")

#let sans = "Source Sans 3"
#let serif = "Source Serif 4"

#let cv(data) = {
  set document(
    title: data.profile.name + " CV",
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
    fill: white,
    footer: context {
      let total = counter(page).final().first()
      set text(font: sans, size: 8.5pt, fill: meta)
      pdf.artifact[
        #align(right)[#counter(page).get().first() / #total]
      ]
    },
  )

  set text(font: sans, size: 9.3pt, fill: ink, lang: "en", region: "GB", hyphenate: false)
  set par(justify: false, leading: 0.6em, spacing: 1em)
  set list(
    marker: text(fill: steel)[•],
    indent: 0.55em,
    body-indent: 0.5em,
    spacing: 0.33em,
  )

  show heading.where(level: 1): it => block(above: 0pt, below: 2pt)[
    #text(font: serif, size: 24pt, weight: 600, fill: navy)[#it.body]
  ]

  show heading.where(level: 2): it => block(
    above: 12pt,
    below: 6pt,
    width: 100%,
    sticky: true,
    stroke: (bottom: 0.6pt + rule),
    inset: (bottom: 3pt),
  )[#text(size: 10pt, weight: 700, fill: navy, tracking: 0.06em)[#upper(it.body)]]

  // ---------------------------------------------------------------- header
  heading(level: 1)[#data.profile.name]

  stack(spacing: 0pt,
    v(1pt),
    text(size: 11pt, weight: 600, fill: steel)[#data.profile.title],
    v(8pt),
    align(left, text(size: 9.2pt, fill: slate)[
      #data.profile.location
      #h(1.2em) #link("tel:" + data.profile.phone.replace(" ", ""))[#data.profile.phone]
      #h(1.2em) #link("mailto:" + data.profile.email)[#data.profile.email]
    ]),
    v(3pt),
    align(left, text(size: 9.2pt, fill: slate)[
      #link(data.profile.links.website)[#data.profile.links.website.replace("https://", "")]
      #h(1.2em) #link(data.profile.links.github)[#data.profile.links.github.replace("https://", "")]
      #h(1.2em) #link(data.profile.links.linkedin)[#data.profile.links.linkedin.replace("https://", "")]
    ]),
    v(10pt),
    block(width: 100%, height: 1.1pt, fill: steel),
  )

  // --------------------------------------------------------------- profile
  heading(level: 2)[Profile]
  text(size: 9.5pt)[#data.profile.summary]

  // ---------------------------------------------------------------- skills
  heading(level: 2)[Core skills]
  for line in data.skills.core [
    #let parts = line.split(":")
    #text(size: 9.4pt, weight: 600, fill: navy)[#parts.at(0):]
    #h(0.3em)
    #text(size: 9.4pt, fill: slate)[#parts.slice(1).join(":").trim()]
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

    // Header and summary stay together and keep with the first bullet;
    // the bullet list itself can break, so a long role never leaves a hole.
    block(above: 11pt, below: 0pt, breakable: false, sticky: true)[
      #text(size: 11.2pt, weight: 700, fill: navy)[#role.company]
      #h(1fr)
      #text(size: 9.2pt, fill: slate)[#role.start to #role.end]
      #linebreak()
      #text(size: 10.1pt, weight: 600)[#title_line]
      #if role.at("stack", default: ()).len() > 0 [
        #linebreak()
        #text(size: 8.6pt, fill: meta)[#role.stack.join(" · ")]
      ]
      #v(5pt)
      #text(size: 9.5pt)[#role.summary]
    ]

    if achievements.len() > 0 [
      #block(inset: (top: 8pt))[
        #list(
          spacing: 0.33em,
          ..achievements.map(a => text(size: 9.4pt)[*#a.title.* #a.description]),
        )
      ]
    ]
  }

  // ------------------------------------------------------------- education
  heading(level: 2)[Education]
  for edu in data.education.education [
    #text(size: 9.8pt, weight: 600)[#edu.degree]
    #h(1fr)
    #text(size: 9.2pt, fill: slate)[#edu.start to #edu.end]
    #linebreak()
    #text(size: 9.2pt, fill: slate)[#edu.institution#text(size: 9pt, fill: meta)[, #edu.grade]]
    #parbreak()
    #v(2.5pt)
  ]

  // ------------------------------------------------------------ open source
  heading(level: 2)[Open source]
  for name in ("tphysics", "psx2rip") {
    for proj in data.projects {
      if proj.name == name {
        text(size: 9.4pt)[*#link(proj.url)[#proj.name].* #proj.summary]
        parbreak()
        v(2pt)
      }
    }
  }
}
