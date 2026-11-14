# Projects

Things I build when nobody is paying me.

{% for item in data.profile.outside %}
<h2>{{ item.label }}</h2>

<p>{{ item.text }}</p>

{% if item.links %}
<p class="project-links">
  {% for l in item.links %}<a href="{{ l.url }}">{{ l.name }}</a>{% if not loop.last %} · {% endif %}{% endfor %}
</p>
{% endif %}
{% endfor %}

More repositories on [GitHub]({{ data.profile.links.github }}).
