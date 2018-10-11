# Project: {{cookiecutter.project_slug}}

This project was created by {{cookiecutter.full_name}} on {{ cookiecutter.date_created }}.

It will be able to do the following:

{% if cookiecutter.count_bases == 'y' %} - Count bases {% endif %}
{% if cookiecutter.reverse_comp == 'y' %} - Reverse complement DNA {% endif %}
{% if cookiecutter.count_bases != 'y' and cookiecutter.reverse_comp != 'y' %} - Nothing{% endif %}
