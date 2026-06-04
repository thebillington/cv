# Education

{% for edu in data.education.education %}
## {{ edu.institution }}
**{{ edu.degree or edu.qualification }}** | {{ edu.start }} to {{ edu.end }}
{% if edu.grade %}Grade: `{{ edu.grade }}`{% endif %}

{% endfor %}
