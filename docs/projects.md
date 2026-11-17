# Projects

Things I build when nobody is paying me.

Generally most of my historical work is available completely free. I have particular interest in tools for Computer Science Education and am a big proponent of teaching Computer Science from first principles. I have an interest in Assembly and low-level programming and have done significant work on the Game Boy in gbZ80 Assembly.

More recently I have built a homelab and have embraced Agentic Engineering, using open weight models both via subscription (Opencode) and locally (llama.cpp running on 2080 SUPER 8GB + 3060 12GB) to complete a number of personal projects I've had on the back burner.

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
