# {{ data.profile.name }}

**{{ data.profile.title }}**

---

{{ data.profile.summary }}

## Quick Links

- [Download CV (PDF)](cv-{{ data.profile.name.lower().replace(" ", "-") }}.pdf)
- [View Experience](experience.md)
- [View Projects](projects.md)
- [View Skills](skills.md)
- [Showreel]({{ data.profile.links.portfolio }})

## Contact

- **Email:** {{ data.profile.email }}
- **GitHub:** [{{ data.profile.links.github }}]({{ data.profile.links.github }})
- **LinkedIn:** [{{ data.profile.links.linkedin }}]({{ data.profile.links.linkedin }})
