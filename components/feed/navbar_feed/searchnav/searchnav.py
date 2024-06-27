from django_components import component

@component.register("searchnav")
class searchnav(component.Component):
    template_name = 'feed/navbar_feed/searchnav/template.html'
    