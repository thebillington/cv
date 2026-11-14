{% set ns = namespace(prev='') %}
# Experience

{% for r in data.experience %}
{% if r.company != ns.prev %}
<h2>{{ r.company }}</h2>
{% endif %}

<p class="role-meta">
  <span class="role-title"><strong>{{ r.title }}</strong>{% if r.team %}, {{ r.team }}{% endif %}</span>
  <span class="dates">{{ r.start }} to {% if r.end == 'present' %}now{% else %}{{ r.end }}{% endif %}</span>
</p>

{% if r.stack %}
<p class="role-stack">{{ r.stack | join('&nbsp;· ') }}</p>
{% endif %}

<p class="role-summary">{{ r.summary }}</p>

{% if r.achievements %}
<ul class="role-list">
{% for a in r.achievements %}
  <li><strong>{{ a.title }}.</strong> {{ a.description }}</li>
{% endfor %}
</ul>
{% endif %}
{% set ns.prev = r.company %}
{% endfor %}

## Additional experience

{% for a in data.profile.additional %}
<h3>{{ a.company }}, {{ a.title }}</h3>

<p class="role-meta"><span class="dates">{{ a.dates }}</span></p>

<p class="role-summary">{{ a.text }}</p>

{% if a.url %}
<p class="role-meta"><a href="{{ a.url }}">Jenson SEIS Fund investment, April 2021</a></p>
{% endif %}
{% endfor %}
