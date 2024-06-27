from django_components import component

@component.register("footer")
class footer(component.Component):
    template_name = 'footer/template.html'