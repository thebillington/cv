#let cv(data) = {
  set page(
    paper: "a4",
    margin: (top: 1.5cm, bottom: 1cm, left: 2cm, right: 2cm),
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
      #v(0.03cm)
      #text(size: 9pt, fill: luma(100))[
        #h(1fr) #data.profile.email #h(1fr) | #h(1fr) #link(data.profile.links.github)[#data.profile.links.github] #h(1fr) | #h(1fr) #link(data.profile.links.linkedin)[#data.profile.links.linkedin] #h(1fr)
      ]
    ],
  )

  c += align(center, text(size: 8pt, fill: luma(130))[
    Interactive CV: #link("https://thebillington.co.uk/cv")[https://thebillington.co.uk/cv]
    #h(2fr)
    Portfolio: #link(data.profile.links.portfolio)[#data.profile.links.portfolio]
  ])
  c += v(0.2cm)
  c += text(size: 10pt, weight: "bold", fill: blue)[Summary]
  c += v(0.1cm)
  c += text(size: 9.5pt)[#data.profile.summary]
  c += v(0.2cm)
  c += text(size: 10pt, weight: "bold", fill: blue)[Skills]
  c += v(0.1cm)

  for cat in data.skills.categories {
    c += text(size: 9pt, weight: "bold")[#cat.name:]
    c += h(0.3cm)
    c += text(size: 9pt)[#cat.skills.join(", ")]
    c += v(0.06cm)
  }

  c += v(0.2cm)
  c += text(size: 10pt, weight: "bold", fill: blue)[Experience]
  c += v(0.1cm)

  for role in data.experience {
    let roles = if type(role) == "array" { role } else { (role,) }

    for r in roles {
      c += block(
        breakable: false,
        inset: (top: 0.1cm, bottom: 0.05cm),
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
    }
  }

  c += v(0.2cm)
  c += text(size: 10pt, weight: "bold", fill: blue)[Education]
  c += v(0.1cm)

  for edu in data.education.education {
    let qual = if "degree" in edu { edu.degree } else { edu.qualification }
    c += [
      #text(size: 9pt, weight: "bold")[#edu.institution]
      #h(0.3cm)
      #text(size: 8.5pt, fill: luma(130))[#edu.start to #edu.end]
      #h(1fr)
      #text(size: 9pt)[#qual]
      #linebreak()
    ]
  }

  c += v(0.2cm)
  c += text(size: 10pt, weight: "bold", fill: blue)[Example Projects]
  c += v(0.1cm)

  let project_names = ("tphysics", "Mushy's Adventure", "psx2rip")
  for name in project_names {
    for proj in data.projects {
      if proj.name == name {
        c += text(size: 10pt, weight: "bold", link(proj.url)[#proj.name])
        c += linebreak()
        c += text(size: 9pt)[#proj.summary]
        c += v(0.05cm)
      }
    }
  }

  c += text(size: 8pt, fill: luma(130))[
    See all open source projects at #link(data.profile.links.github)[#data.profile.links.github]
  ]
  c += text(size: 8pt, fill: luma(130))[
    Visit my portfolio at #link(data.profile.links.portfolio)[#data.profile.links.portfolio]
  ]

  c
}
