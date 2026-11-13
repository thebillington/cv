{% set here = data.experience[0] %}

<div class="hero">
  <div class="hero-text">
    <h1>{{ data.profile.name }}</h1>
    <p class="hero-role">{{ data.profile.title }}</p>
    <p class="hero-contact">
      <span>{{ data.profile.location }}</span>
      <span class="sep">·</span>
      <span><a href="mailto:{{ data.profile.email }}">{{ data.profile.email }}</a></span>
      <span class="sep">·</span>
      <span><a href="tel:{{ data.profile.phone.replace(' ', '') }}">{{ data.profile.phone }}</a></span>
    </p>
  </div>
</div>

<div class="button-row">
  <a class="md-button md-button--primary" href="{{ pdf_name }}">Download CV (PDF)</a>
  <a class="md-button" href="{{ data.profile.links.github }}">GitHub</a>
  <a class="md-button" href="{{ data.profile.links.linkedin }}">LinkedIn</a>
  <a class="md-button" href="{{ data.profile.links.portfolio }}">Portfolio</a>
</div>

{{ data.profile.intro }}

## Currently

**{{ here.title }}** at **{{ here.company }}** ({{ here.start }} to now), in the
{{ here.team }} team.

## Selected work

<ul class="outcomes">
{% for item in data.profile.highlights %}
  <li>{{ item }}</li>
{% endfor %}
</ul>

## Core skills

<div class="expertise">
{% for line in data.skills.core %}
{% set parts = line.split(':') %}
<p><strong>{{ parts[0] }}</strong> {{ parts[1:] | join(':') | trim }}</p>
{% endfor %}
</div>

The [experience](experience.md) page has the full history with every role, or
you can [download the two-page CV]({{ pdf_name }}).
