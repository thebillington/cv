# Skills

The CV carries the core set. The full matrix is below, including
technologies no longer used daily.

{% for cat in data.skills.categories %}
<h2>{{ cat.name }}</h2>

<p class="skill-list">{{ cat.skills | join(' · ') }}</p>
{% endfor %}
