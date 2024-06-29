from django_components import component
from django_components import types as t

@component.register("favicon")
class favicon(component.Component):
    
    template:t.django_html = """
    {% load static %}
    <link rel="icon" href="{% static 'public/favicon.ico' %}">
    """