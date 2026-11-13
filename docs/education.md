# Education

{% for edu in data.education.education %}
<h2>{{ edu.institution }}</h2>

<p class="role-meta"><strong>{{ edu.degree }}</strong> · {{ edu.start }} to {{ edu.end }}</p>

{% if edu.grade %}
<p class="role-summary">Grade: {{ edu.grade }}</p>
{% endif %}
{% endfor %}

I taught computer science for two years before moving into software full time,
which is where the explaining-to-people habit comes from.
