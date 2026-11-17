# Education

{% for edu in data.education.education %}
<h2>{{ edu.institution }}</h2>

<p class="role-meta">
  <span class="role-title"><strong>{{ edu.degree }}</strong></span>
  <span class="dates">{{ edu.start }} to {{ edu.end }}</span>
</p>

{% if edu.grade %}
<p class="role-summary">Grade: {{ edu.grade }}</p>
{% endif %}
{% endfor %}
