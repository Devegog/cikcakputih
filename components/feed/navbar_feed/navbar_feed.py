from django_components import component

@component.register("navbar_feed")
class navbar_feed(component.Component):
    template_name = 'feed/navbar_feed/template.html'