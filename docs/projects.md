# Projects

{% for p in data.projects %}
## {{ p.name }}

**Status:** {{ p.status }}

{{ p.summary }}

{% if p.highlights %}
{% for h in p.highlights %}
- {{ h }}
{% endfor %}
{% endif %}

{% if p.url %}
**URL:** [{{ p.url }}]({{ p.url }})
{% endif %}

{% endfor %}
