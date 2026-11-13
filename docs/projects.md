# Projects

Open-source and personal projects, each built to solve a specific problem.

{% for p in data.projects %}
<h2><a href="{{ p.url }}">{{ p.name }}</a></h2>

<p class="role-meta">{{ p.status }}</p>

{{ p.summary }}

{% if p.highlights %}
<ul class="role-list">
{% for h in p.highlights %}
  <li>{{ h }}</li>
{% endfor %}
</ul>
{% endif %}
{% endfor %}
