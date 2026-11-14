// Billy Rebecchi CV
// Single column, ATS-safe, tagged PDF (PDF/UA-1).
//
// Layout rules:
//   * employer, then title with the dates on the same line, then stack, then
//     evidence. That is the order every parser expects.
//   * serif for the name only; sans for prose; mono for labels, dates and
//     stacks, which is what makes it read as a spec rather than a brochure
//   * no tables, columns, icons or page furniture

#let cv(data) = {
  let ink = rgb("#1B1B1B")
  let name-col = rgb("#14314E")
  let accent = rgb("#2A6F97")
  let muted = rgb("#7E8790")
  let body-2 = rgb("#3F4A56")
  let rule = rgb("#C9D2DA")

  let base = 16pt
  let gap-par = 5.5pt
  let gap-role = 15pt
  let gap-section = 25pt

  let sans = "Source Sans 3"
  let serif = "Source Serif 4"
  let mono = "IBM Plex Mono"

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
    margin: (x: 21mm, top: 13mm, bottom: 12mm),
    fill: white,
  )

  set text(font: sans, size: 9.6pt, fill: ink, lang: "en", region: "GB", hyphenate: false)
  set par(justify: false, leading: 0.633em, spacing: gap-par)
  set list(
    marker: text(fill: accent)[•],
    indent: 0.55em,
    body-indent: 0.5em,
    spacing: 5pt,
  )

  // Name: the only serif on the page.
  show heading.where(level: 1): it => block(above: 0pt, below: 4pt)[
    #text(font: serif, size: 26pt, weight: 600, fill: name-col, tracking: -0.01em)[#it.body]
  ]

  // Section labels: mono, uppercase, ruled. No numbering: parsers match the word.
  show heading.where(level: 2): it => block(
    above: gap-section,
    below: 8pt,
    width: 100%,
    sticky: true,
    stroke: (bottom: 0.6pt + rule),
    inset: (bottom: 3.5pt),
  )[#text(font: mono, size: 8.6pt, weight: 600, fill: name-col, tracking: 0.12em)[#upper(it.body)]]

  // ---------------------------------------------------------------- header
  grid(
    columns: (auto, 1fr),
    column-gutter: 10pt,
    align: (left + bottom, left + bottom),
    heading(level: 1)[#data.profile.name],
    text(font: mono, size: 9pt, weight: 600, fill: accent, tracking: 0.06em)[#upper(data.profile.title)],
  )

  stack(spacing: 0pt,
    v(8pt),
    text(font: mono, size: 7.4pt, fill: body-2)[
      #link("mailto:" + data.profile.email)[#data.profile.email]
      #h(0.45em) #link(data.profile.links.website)[#data.profile.links.website.replace("https://", "")]
      #h(0.45em) #link(data.profile.links.github)[#data.profile.links.github.replace("https://", "")]
      #h(0.45em) #link(data.profile.links.linkedin)[#data.profile.links.linkedin.replace("https://", "")]
    ],
    v(10pt),
    block(width: 100%, height: 1.2pt, fill: accent),
  )

  // -------------------------------------------------------------- summary
  heading(level: 2)[Summary]
  text(size: 9.8pt)[#data.profile.summary]

  // --------------------------------------------------------------- skills
  heading(level: 2)[Skills]
  for line in data.skills.core [
    #let parts = line.split(":")
    #box(width: 6.6em)[#text(font: mono, size: 7.8pt, weight: 600, fill: accent, tracking: 0.08em)[#upper(parts.at(0))]]
    #text(size: 9.2pt, fill: body-2)[#parts.slice(1).join(":").trim()]
    #parbreak()
    #v(2.2pt)
  ]

  // ----------------------------------------------------------- experience
  heading(level: 2)[Experience]

  for role in data.experience {
    let achievements = role.at("achievements", default: ()).filter(
      a => a.at("include_pdf", default: true)
    )
    let title_line = role.title
    if role.at("team", default: "") != "" {
      title_line = title_line + ", " + role.team
    }
    let end = if role.end == "present" { "Present" } else { role.end }

    block(above: gap-role, below: 0pt, breakable: false, sticky: true)[
      #text(size: 11pt, weight: 700, fill: name-col)[#role.company]
      #linebreak()
      #text(size: 10.2pt, weight: 600)[#title_line]
      #h(1fr)
      #text(font: mono, size: 8.4pt, fill: body-2)[#role.start to #end]
      #if role.at("stack", default: ()).len() > 0 [
        #linebreak()
        #text(font: mono, size: 7.9pt, fill: muted)[#role.stack.join("\u{00A0}· ")]
      ]
      #v(5pt)
      #text(size: 9.6pt)[#role.summary]
    ]

    if achievements.len() > 0 [
      #block(inset: (top: 7pt))[
        #list(
          spacing: 5pt,
          ..achievements.map(a => text(size: 9.4pt)[*#a.title.* #a.description]),
        )
      ]
    ]
  }

  // ------------------------------------------------------------- education
  // One line per entry with the date at the end, so a parser cannot detach the
  // institution from the degree.
  heading(level: 2)[Education]
  for edu in data.education.education [
    #let end = if edu.end == "present" { "Present" } else { edu.end }
    #text(size: 9.8pt, weight: 600)[#edu.degree]#text(size: 9.6pt, fill: body-2)[, #edu.institution]
    #if edu.at("grade", default: none) != none [
      #text(size: 9.6pt, fill: body-2)[, #edu.grade]
    ]
    #text(size: 9.6pt, fill: body-2)[ · #edu.start to #end]
    #parbreak()
    #v(3pt)
  ]


  // ------------------------------------------------------------ outside work
  if data.profile.at("outside", default: ()).len() > 0 {
    heading(level: 2)[Projects]
    for item in data.profile.outside {
      text(size: 9.7pt, weight: 600)[#item.label.]
      h(0.3em)
      text(size: 9.4pt)[#item.text]
      if item.at("links", default: ()).len() > 0 {
        h(0.4em)
        let links = item.links.map(l => link(l.url)[#l.name])
        text(font: mono, size: 7.8pt, fill: muted)[#links.join([#h(0.5em) · #h(0.5em)])]
      }
      parbreak()
      v(2.5pt)
    }
  }
}
