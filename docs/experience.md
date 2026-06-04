# Experience

{% for r in data.experience %}
## {{ r.company }}
**{{ r.title }}** | {{ r.start }} to {{ r.end }}

{{ r.summary }}

{% if r.achievements %}
Key achievements:
{% for a in r.achievements %}
- {{ a.title }}
{% endfor %}
{% endif %}

{% endfor %}
