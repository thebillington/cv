# Skills

{% for cat in data.skills.categories %}
## {{ cat.name }}
{{ cat.skills | join(", ") }}

{% endfor %}
