{% set here = data.experience[0] %}

<div class="hero">
  <div class="hero-text">
    <h1>{{ data.profile.name }}</h1>
    <p class="hero-role">{{ data.profile.title }}</p>
    <p class="hero-contact">
      <span><a href="mailto:{{ data.profile.email }}">{{ data.profile.email }}</a></span>
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

## Current position

**{{ here.title }} at {{ here.company }}**, {{ here.start }} to now.
{{ data.profile.summary_role }}

## Core skills

<div class="expertise">
{% for line in data.skills.core %}
{% set parts = line.split(':') %}
<p><strong>{{ parts[0] }}</strong> {{ parts[1:] | join(':') | trim }}</p>
{% endfor %}
</div>
