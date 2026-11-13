# Skills

The short version is on the [CV](Billy-Rebecchi-CV.pdf). This is the full list,
including the things I no longer use daily but can still hold a conversation
about.

{% for cat in data.skills.categories %}
<h2>{{ cat.name }}</h2>

<p class="skill-list">{{ cat.skills | join(' · ') }}</p>
{% endfor %}
