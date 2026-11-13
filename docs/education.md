# Education

{% for edu in data.education.education %}
<h2>{{ edu.institution }}</h2>

<p class="role-meta"><strong>{{ edu.degree }}</strong> · {{ edu.start }} to {{ edu.end }}</p>

{% if edu.grade %}
<p class="role-summary">Grade: {{ edu.grade }}</p>
{% endif %}
{% endfor %}

Two years teaching computer science preceded full-time software engineering;
the curriculum materials remain in use.
