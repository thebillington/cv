# Skills

<div class="expertise">
{% for cat in data.skills.categories %}
<p><strong>{{ cat.name }}</strong> {{ cat.skills | join('&nbsp;· ') }}</p>
{% endfor %}
</div>
