# Experience

{% for r in data.experience %}
<h2>{{ r.company }}</h2>

<p class="role-meta"><strong>{{ r.title }}</strong>{% if r.team %}, {{ r.team }}{% endif %} · {{ r.start }} to {% if r.end == 'present' %}now{% else %}{{ r.end }}{% endif %}</p>

{% if r.stack %}
<p class="role-stack">{{ r.stack | join(' · ') }}</p>
{% endif %}

<p class="role-summary">{{ r.summary }}</p>

{% if r.achievements %}
<ul class="role-list">
{% for a in r.achievements %}
  <li><strong>{{ a.title }}.</strong> {{ a.description }}</li>
{% endfor %}
</ul>
{% endif %}
{% endfor %}
