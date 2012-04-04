<!DOCTYPE HTML>
<head>
<title>{% block title %}{% endblock %} -- QuestCompanions</title>
<link rel="stylesheet" type="text/css" href="/static/css/core.css"/>
<link rel="stylesheet" type="text/css" href="/static/css/loggedOut.css"/>
<link rel="stylesheet" type="text/css" href="/static/css/forms.css"/>
<script src="/scripts/jquery-1.7.2.js"></script>
<script src="/rpc.js"></script>
{% block includes %}{% endblock %}
</head>
<body>
  <div class="header">
    <div class="logo"><img src="/static/img/logo.png"></div>
    <div class="name"></div>
    <div class="slogan">Who says mercenaries can't have fun?</div>
  </div>
  <div class="body">
{% block content %}{% endblock %}
  </div>
  <div id="footer">
  </div>
</body>