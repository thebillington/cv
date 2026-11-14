{% set here = data.experience[0] %}

<div class="hero">
  <div class="hero-text">
    <h1>{{ data.profile.name }}</h1>
    <p class="hero-role">{{ data.profile.title }}</p>
    <p class="hero-contact">
      <span>{{ data.profile.location }}</span>
      <span class="sep">·</span>
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

## Currently

I lead the Engagement Pod at Blue Light Card and own the Auth0 and members
service handling 16 million requests per day.

## Core skills

<div class="expertise">
{% for line in data.skills.core %}
{% set parts = line.split(':') %}
<p><strong>{{ parts[0] }}</strong> {{ parts[1:] | join(':') | trim }}</p>
{% endfor %}
</div>

The [experience](experience.md) page carries the full history, including
[additional work](experience.md#additional-experience). The [projects](projects.md)
page has the homelab, the Game Boy work and the apps.
