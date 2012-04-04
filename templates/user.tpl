{% extends "base.tpl" %}
{% block title %}{{ user.username if user else 'Error' }}{% endblock %}
{% block includes %}
<link rel="stylesheet" type="text/css" href="/static/css/users.css"/>
{% endblock %}
{% block content %}
{% if not user %}
  <h1>Error: Invalid user ID</h1>
{% else %}
  <div class="col narrow">
    {#<div class="userPic">
      <img src="{{ user.pic }}">
    </div>#}
    <div class="contact block">
      <h3>contact</h3>
      {#{% for link in user.contact %}
        <a class="contact" href="{{ link.href }}i">{{ link.type }}</a>
      {% endfor %}#}
    </div>
  </div>
  <div class="col wide">
    <h1>{{ user.username }}</h1>
    <div class="chars block">
    <h3>Characters</h3>
    {% for char in user.characters %}
      <a href="/characters/{{ char.id }}">{{ char.name }}</a>
    {% endfor %}
    </div>
  </div>
{% endif %}

{% endblock %}
