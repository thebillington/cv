#let cv(data) = {
  set page(
    paper: "a4",
    margin: (top: 1.5cm, bottom: 1.5cm, left: 2cm, right: 2cm),
    footer: context [
      #set text(font: "Helvetica", size: 8pt, fill: luma(150))
      #let p = counter(page).get()
      #align(right, [
        CV -- Billy Rebecchi -- Page #p.first()
      ])
    ],
  )

  set text(font: "Helvetica", size: 10pt)

  let c = block(
    width: 100%,
    inset: (bottom: 0.3cm),
    stroke: (bottom: 2pt + blue),
    align(center)[
      #text(size: 20pt, weight: "bold", data.profile.name)
      #linebreak()
      #text(size: 9pt, fill: luma(100))[
        #h(1fr) #data.profile.email #h(1fr) | #h(1fr) #link(data.profile.links.github)[#data.profile.links.github] #h(1fr) | #h(1fr) #link(data.profile.links.linkedin)[#data.profile.links.linkedin] #h(1fr)
      ]
      #linebreak()
      #text(size: 8pt, fill: blue, link(data.profile.links.website)[
        View CV in Github Pages \u{2192}
      ])
    ],
  )

  c += v(0.3cm)
  c += text(size: 10pt, weight: "bold", fill: blue)[Summary]
  c += v(0.15cm)
  c += text(size: 9.5pt)[#data.profile.summary]
  c += v(0.3cm)
  c += text(size: 10pt, weight: "bold", fill: blue)[Experience]
  c += v(0.15cm)

  for role in data.experience {
    let roles = if type(role) == "array" { role } else { (role,) }

    for r in roles {
      c += block(
        inset: (top: 0.15cm, bottom: 0.1cm),
        [
          #text(size: 10pt, weight: "bold")[#r.company]
          #h(1fr)
          #text(size: 9pt, fill: luma(120))[#r.title]
          #linebreak()
          #text(size: 8.5pt, fill: luma(130))[#r.start to #r.end]
          #v(0.1cm)
          #text(size: 9pt)[#r.summary]
        ],
      )

      let matching = r.achievements.filter(a =>
        a.tags.contains("architecture")
        or a.tags.contains("migration")
        or a.tags.contains("leadership")
        or a.tags.contains("platform")
        or a.tags.contains("strategy")
      )

      let to_show = if matching.len() > 0 { matching } else { r.achievements }

      for a in to_show {
        c += v(0.08cm)
        c += text(size: 9pt)[
          \u{2022} #a.title
        ]
      }
    }
  }

  c += v(0.3cm)
  c += text(size: 10pt, weight: "bold", fill: blue)[Skills]
  c += v(0.15cm)

  for cat in data.skills.categories {
    c += text(size: 9pt, weight: "bold")[#cat.name:]
    c += h(0.3cm)
    c += text(size: 9pt)[#cat.skills.join(", ")]
    c += v(0.1cm)
  }

  c += v(0.2cm)
  c += text(size: 10pt, weight: "bold", fill: blue)[Education]
  c += v(0.15cm)

  for edu in data.education.education {
    let qual = if "degree" in edu { edu.degree } else { edu.qualification }
    c += [
      #text(size: 9pt, weight: "bold")[#edu.institution]
      #h(0.3cm)
      #text(size: 8.5pt, fill: luma(130))[#edu.start -- #edu.end]
      #h(1fr)
      #text(size: 9pt)[#qual]
      #linebreak()
    ]
  }

  c
}
