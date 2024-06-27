from django_components import component

@component.register("sidebar_content")
class sidebar_content(component.Component):
    template_name = 'feed/sidebar_content/template.html'